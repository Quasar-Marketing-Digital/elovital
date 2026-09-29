#!/usr/bin/env python3
"""Prepara as páginas para o WordPress: cada uma vira UM bloco de HTML autossuficiente (CSS e JS embutidos),
com imagens como marcadores {{IMG:arquivo}} a trocar pelos endereços da biblioteca de mídia.
Saída: wp_pages/<slug>.html + wp_pages/manifesto.json (título, slug, modelo e lista de mídias a enviar).
Não usa nenhuma credencial."""
import os, re, json, base64, shutil, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
OUT = ROOT + 'wp_pages/'
PREFIX = 'cc_'
PAGES = [  # (arquivo fonte, título, slug de teste, endereço-alvo no site definitivo)
 ('elo_vital_home_v5.html', 'Home', 'cc-home', '/'),
 ('elo_vital_psicologia_junguiana.html', 'Psicologia Junguiana', 'cc-psicologia-junguiana', '/psicologia-junguiana/'),
 ('elo_vital_jogo_do_heroi.html', 'O Jogo do Herói', 'cc-o-jogo-do-heroi', '/o-jogo-do-heroi/'),
 ('elo_vital_blog.html', 'Blog', 'cc-blog', '/blog/'),
 ('elo_vital_post_herois_e_heroinas.html', 'Heróis e heroínas', 'cc-herois-e-heroinas', '/herois-e-heroinas/'),
 ('elo_vital_post_como_comeca_uma_jornada_heroica.html', 'Como começa uma jornada heroica?', 'cc-como-comeca-uma-jornada-heroica', '/como-comeca-uma-jornada-heroica/'),
 ('elo_vital_post_ah_esse_tal_de_inconsciente.html', 'Ah, esse tal de inconsciente…', 'cc-ah-esse-tal-de-inconsciente', '/ah-esse-tal-de-inconsciente/'),
]
SLUG_OF = {alvo: slug for _, _, slug, alvo in PAGES}
CSS = open(ROOT + 'assets/site.css', encoding='utf-8').read()
JS = open(ROOT + 'assets/site.js', encoding='utf-8').read()

# Reforço contra o CSS do tema (Hello Elementor): botões e links não podem herdar cor/fundo do tema
GUARD = """
/* proteção contra o CSS do tema WordPress */
.menu-btn,.menu-btn:hover,.menu-btn:focus{ background:none !important; border:0 !important; color:var(--paper) !important; box-shadow:none !important; }
.btn,.btn:hover{ text-decoration:none !important; }
.topbar a,.sec a,footer a{ text-decoration:none; }
"""

def media_names(text):
    return set(re.findall(r'\{\{IMG:([^}]+)\}\}', text))

def build(src, title):
    s = open(ROOT + src, encoding='utf-8').read()
    media = {}
    # 1) mídias embutidas em data: -> arquivos próprios (vídeo e cartaz da home, logo)
    def extract(m):
        mime, b64 = m.group(1), m.group(2)
        ext = {'video/mp4': 'mp4', 'image/jpeg': 'jpg', 'image/png': 'png'}[mime]
        raw = base64.b64decode(b64); h = hashlib.md5(b64.encode()).hexdigest()[:8]
        name = f'{"video" if ext=="mp4" else "inline"}_{h}.{ext}'
        os.makedirs(OUT + '_media/', exist_ok=True); open(OUT + '_media/' + name, 'wb').write(raw)
        media[name] = OUT + '_media/' + name
        return '{{IMG:%s}}' % name
    s = re.sub(r'data:(video/mp4|image/jpeg|image/png);base64,([A-Za-z0-9+/=]+)', extract, s)
    # 2) imagens do projeto -> marcadores
    def img(m):
        name = m.group(2); media[name] = ROOT + 'imagens/' + name
        return m.group(1) + '{{IMG:%s}}' % name
    s = re.sub(r'((?:src|href)=")imagens/([^"]+)(")', lambda m: img(m) + m.group(3), s)
    s = re.sub(r"(url\(')imagens/([^']+)('\))", lambda m: img(m) + m.group(3), s)
    # 3) links entre páginas -> páginas de teste (cc-...)
    for alvo, slug in SLUG_OF.items():
        s = s.replace(f'href="{alvo}"', f'href="/{slug}/"')
    # 4) partes: <style> do head (todos) + corpo (sem <script src>)
    styles = ''.join(re.findall(r'<style>.*?</style>', s[:s.index('</head>')], flags=re.S)) if '</head>' in s else ''
    fonts = ''.join(re.findall(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>', s))
    body = s[s.index('<body') :]
    body = re.sub(r'^<body[^>]*>', '', body)
    body = re.sub(r'</body>.*$', '', body, flags=re.S)
    body = re.sub(r'<script src="assets/site\.js"></script>', '', body)
    body = re.sub(r'<script src="/assets/site\.js"></script>', '', body)
    # 5) juntar: site.css + estilos da página + guarda; HTML; site.js (a home já tem JS próprio inline)
    has_inline_js = '<script>' in body
    pieces = [fonts, '<style>\n' + CSS + GUARD + '\n</style>']
    if styles and not src.endswith('home_v5.html'):
        pieces.append(styles)
    elif src.endswith('home_v5.html'):
        pieces.append(styles)  # a home traz o CSS completo no próprio <style>
    pieces.append(body.strip())
    if not has_inline_js:
        pieces.append('<script>\n' + JS + '\n</script>')
    html = '\n'.join(p for p in pieces if p)
    if src.endswith('home_v5.html'):
        # a home tem CSS/JS próprios completos: não misturar com o site.css
        html = '\n'.join([fonts, styles, GUARD.join(['<style>', '</style>']), body.strip()])
    # 6) o WordPress troca "&" por "&#038;" no conteúdo (quebra "&&" do JavaScript): reescrever sem "&"
    for a, b in [('menuBtn && navEl', 'menuBtn ? navEl : null'),
                 ('r.top < y && r.bottom > y', '(r.top < y ? r.bottom > y : false)'),
                 ('b.top < y && b.bottom > y && s.top > y', '(b.top < y ? (b.bottom > y ? s.top > y : false) : false)'),
                 ('vw <= 860 && !l.deco ?', '(vw <= 860 ? !l.deco : false) ?')]:
        html = html.replace(a, b)
    html = html.replace('&family', '&amp;family').replace('&display', '&amp;display')
    assert '&&' not in html and not re.search(r'&(?![a-z#0-9]+;)', html), 'sobrou & solto'
    return html, media

if __name__ == '__main__':
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    manifest = {'prefixo_titulo': PREFIX, 'paginas': [], 'midias': {}}
    for src, title, slug, alvo in PAGES:
        html, media = build(src, title)
        open(OUT + slug + '.html', 'w', encoding='utf-8').write(html)
        manifest['paginas'].append({'arquivo': slug + '.html', 'titulo': PREFIX + title, 'slug': slug, 'alvo_definitivo': alvo, 'midias': sorted(media)})
        manifest['midias'].update({k: os.path.relpath(v, ROOT) for k, v in media.items()})
        print(f'{slug:42s} {len(html.encode())//1024:5d} KB  mídias: {len(media)}')
    json.dump(manifest, open(OUT + 'manifesto.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    tot = sum(os.path.getsize(ROOT + p) for p in set(manifest['midias'].values()))
    print(f'\n{len(manifest["midias"])} arquivos de mídia distintos, {tot//1024} KB no total')
