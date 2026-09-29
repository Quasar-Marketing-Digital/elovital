#!/usr/bin/env python3
# Gera as páginas do Blog (listagem + 3 posts) no estilo do site. Textos = os do site atual, sem alteração.
import html

ROOT = '/home/user/elovital/'
WA = 'https://wa.me/5516988209196'
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path class="b" d="M12 2.6a9.4 9.4 0 0 0-8.1 14.1L2.7 21.3l4.7-1.2A9.4 9.4 0 1 0 12 2.6z"/><path class="p" transform="translate(7.2 7.2) scale(.4)" d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>'

POSTS = [
 dict(slug='como-comeca-uma-jornada-heroica', file='elo_vital_post_como_comeca_uma_jornada_heroica.html',
      title='Como começa uma jornada heroica?', ghost='Jornada', light=False,
      hero='post_jornada_hero.jpg', card='post_jornada_card.jpg',
      alt='Tabuleiro do Jogo do Herói com esferas de vidro e dados',
      excerpt='Tudo pode começar por um sentimento de busca… Uma inquietação que persiste, uma forte insatisfação, o anseio ou a ambição que nos …',
      paras=[
        'Tudo pode começar por um sentimento de busca…',
        'Uma inquietação que persiste, uma forte insatisfação, o anseio ou a ambição que nos move em direção a melhorar nossa vida.',
        'A partir de uma angústia, de grandes conflitos em nossas emoções e ideias, de crises que passamos diante de uma perda, de adoecimento físico e emocional, quando buscamos auxílio para lidar com uma persistente ansiedade ou depressão.',
        'Ou pode começar por algo que esteja muito desafiador em nossa vida, seja porque percebemos uma situação que está bloqueada, ou ao contrário, há uma grande oportunidade que ao mesmo tempo nos incita e assusta.',
        'Uma aventura que nos chama e traz ao mesmo tempo, novas realizações e também conflitos.',
        'Chamamos de jornada heroica essa atitude de encarar nós mesmos e as nossa circunstâncias, atitudes que nos levam a ter mais consciência sobre nossa própria história, e sobre o que estamos criando na nossa vida. Caminhos que nos levam a descobrir e a desenvolver novas habilidades.',
        'Movimentos que levam a outras formas de compreender o mundo e de nos inserirmos nele. Travessias que nos transformam, semelhantes a ritos de passagem.',
        'Algo que na psicologia Junguiana também chamamos de processo de individuação.']),
 dict(slug='ah-esse-tal-de-inconsciente', file='elo_vital_post_ah_esse_tal_de_inconsciente.html',
      title='Ah, esse tal de inconsciente…', ghost='Sonhos', light=False,
      hero='post_inconsciente_hero.jpg', card='post_inconsciente_card.jpg',
      alt='Rosto dividido entre claro e escuro',
      excerpt='Umas das coisas que mais me impressiona e fascina é perceber o vasto campo de expressões e criações da nossa mente atuando …',
      paras=[
        'Umas das coisas que mais me impressiona e fascina é perceber o vasto campo de expressões e criações da nossa mente atuando de modo inconsciente.',
        'Você se lembra de seus sonhos noturnos? Já se percebeu criando pequenas histórias e fantasias enquanto faz outra coisa?',
        'Já se percebeu agindo de forma automática, sem prestar atenção no que está fazendo? Se viu dizendo algo que não queria, ou expressando alguma ideia que não havia pensado conscientemente antes? Alguma “inspiração nascida de súbito”?',
        'Para a Psicologia Junguiana ” o inconsciente não é um simples depósito do passado, também pensamentos inteiramente novos e ideias criadoras podem surgir do inconsciente – ideias e pensamentos que nunca foram conscientes” (O homem e seus símbolos…) .',
        'Essa capacidade psíquica de produzir material novo é ainda mais significativa quando se trata dos conteúdos simbólicos dos nossos sonhos. Eles não são apenas memórias das nossas experiências anteriores, mas também expressam criatividade própria!',
        'A partir da nossa vida onírica, dos nossos sonhos gestados inconscientemente enquanto dormimos, emergem grande parte de nossos símbolos e criações.',
        'Além de rememorar e criar, nossos pensamentos e imagens inconscientes atuam em diálogo com os sentimentos e experiências, frequentemente buscando caminhos, respostas, e integrações, que, quando compreendidos podem contribuir para nossa saúde e desenvolvimento da nossa personalidade.']),
 dict(slug='herois-e-heroinas', file='elo_vital_post_herois_e_heroinas.html',
      title='Heróis e heroínas', ghost='Heróis', light=True,
      hero='post_herois_hero.jpg', card='post_herois_card.jpg',
      alt='imagens de figuras humanas arquetípicas',
      excerpt='A Jornada do Herói e sua temática são abordados com frequência nas mais diversas áreas. Nas artes, especialmente no cinema e na …',
      paras=[
        'A Jornada do Herói e sua temática são abordados com frequência nas mais diversas áreas. Nas artes, especialmente no cinema e na literatura, na mitologia, na filosofia, e em estudos sobre o ser humano, especialmente na psicologia de Carl Gustav Jung. Mas será que são vistos pelo mesmo prisma em todos esse âmbitos? Podemos afirmar que não.',
        'Aqui, a visão que nos guia, é tecida principalmente pelos trabalhos de Joseph Campbell, importante estudioso de mitologia comparada e propositor da jornada, e autores da psicologia Junguiana que estabelecem relações entre a jornada heroica e o processo de individuação, proposto por Jung.',
        'Embora algumas pessoas associem o heroísmo com bravura e luta através da força física tal qual um guerreiro de combate, a definição da jornada heroica de Campbell, James Hollis e outras figuras centrais sobre o tema, apontam o heroísmo como uma jornada essencialmente interna. Uma busca de si, um processo de tornar-se, histórias e experiências de seres humanos buscando viver com mais inteireza.',
        'A jornada heroica pode também envolver algum tipo de luta e bravura física, mas este é apenas um dos elementos e formas possíveis de vivenciá-la. No entanto, a bravura é, em muitas circunstâncias, expressão simbólica de forças psicológicas, no enfrentamento de algo que vai além de seu ego e de sua consciência. Heróis e heroínas são aqui, o homem ou a mulher que ultrapassam de alguma forma, suas limitações históricas pessoais e locais, ultrapassam seu mundo conhecido, consciente e retornam a seu mundo renovados.']),
]
LIST_ORDER = ['como-comeca-uma-jornada-heroica', 'ah-esse-tal-de-inconsciente', 'herois-e-heroinas']   # ordem da listagem do site
BY = {p['slug']: p for p in POSTS}

BASE = 'https://elovital.com.br'
DESC = {
 '/blog/': 'Artigos sobre a jornada heroica, o inconsciente e a Psicologia Junguiana.',
 '/como-comeca-uma-jornada-heroica/': 'Tudo pode começar por um sentimento de busca, uma inquietação que persiste. Entenda como começa uma jornada heroica e o processo de individuação.',
 '/ah-esse-tal-de-inconsciente/': 'O vasto campo de expressões e criações da nossa mente atuando de modo inconsciente, na visão da Psicologia Junguiana.',
 '/herois-e-heroinas/': 'A Jornada do Herói na mitologia, na literatura e na psicologia de Jung: heróis e heroínas como uma jornada essencialmente interna.',
}
def meta(title, path):
    d = html.escape(DESC[path], quote=True); t = html.escape(title + ' — Elo Vital', quote=True)
    return (f'\n<meta name="description" content="{d}">\n<meta name="theme-color" content="#0a0a0b">\n'
      '<link rel="icon" type="image/png" sizes="32x32" href="imagens/favicon-32.png">\n<link rel="apple-touch-icon" href="imagens/apple-touch-icon.png">\n'
      f'<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Elo Vital">\n'
      f'<meta property="og:description" content="{d}"><meta property="og:url" content="{BASE}{path}"><meta property="og:image" content="{BASE}/imagens/favicon-192.png">\n<meta property="og:title" content="{t}">')

def head(title, css, path):
    return f'''<!doctype html>
<html lang="pt-BR" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)} — Elo Vital</title>{meta(title, path)}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Newsreader:ital,wght@0,400;1,400&family=Archivo:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/site.css">
<style>
{css}
</style>
</head>
<body>
'''

HEADER = f'''
<header class="topbar">
  <a href="/" class="brand" aria-label="Elo Vital — início"><img class="logo-mark" src="imagens/logo_elo_vital.png" alt=""><b>Elo Vital</b></a>
  <div class="social">
    <a class="insta" href="#" aria-label="Instagram" title="Instagram">{IG_SVG}</a>
    <a class="whats" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp" title="WhatsApp">{WA_SVG}</a>
  </div>
  <nav class="nav" id="nav" aria-label="Principal"><a href="/">Início</a><a href="/psicologia-junguiana/">Psicologia Junguiana</a><a href="/o-jogo-do-heroi/">O Jogo do Herói</a><a href="/blog/" aria-current="page">Blog</a><a href="#contato">Contato</a></nav>
  <button class="menu-btn" id="menubtn" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
</header>
<div class="vmark">psicologia junguiana</div>
'''

FOOTER = f'''<footer id="contato" role="contentinfo">
  <div class="foot-in">
    <span class="foot-brand"><img src="imagens/logo_elo_vital.png" alt=""> Elo Vital</span>
    <nav class="foot-nav" aria-label="Redes"><a href="#">Instagram</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></nav>
    <p class="copy">© Elo Vital — Todos os direitos reservados — Desenvolvido por Pulsar Marketing e Comunicação</p>
  </div>
</footer>

</main>

<script src="assets/site.js"></script>
</body>
</html>
'''

BTN = lambda label: f'<a class="btn" data-rev href="{WA}" target="_blank" rel="noopener">{WA_SVG}{label}</a>'

PAULA = f'''  <!-- PAULA CORDERO -->
  <section class="sec" id="paula">
    <div class="ghost" data-speed="0.5" data-x="16" aria-hidden="true">Paula</div>
    <div class="wrap"><div class="pad"><div class="cols b">
      <div class="photo" data-speed="-0.06"><div class="in" data-rev><img data-para alt="Paula Cordero" src="imagens/paula_cordero.jpg"></div><div class="frame" style="inset:-18px 18px 18px -18px"></div></div>
      <div>
        <h2 class="display" data-rev>Paula Cordero</h2>
        <p class="who" data-rev>Psicóloga, especializada em Psicologia Junguiana e facilitadora certificada no ‘O Jogo do Herói’, em Breathwork.</p>
        {BTN('Agende Sua Consulta')}
      </div>
    </div></div></div>
  </section>
'''

COMMON_CSS = '''  main .sec:not(#topo){ min-height:0; }
  .light .eyebrow{ color:#5b5953; }
  .pad{ padding-block:clamp(96px,14vh,150px); width:100%; }
  .cols{ display:grid; gap:clamp(30px,6vw,96px); align-items:center; width:100%; }
  .cols.b{ grid-template-columns:.85fr 1.15fr; }
  @media (max-width:860px){ .cols.b{ grid-template-columns:1fr; max-width:560px; margin-inline:auto; } }
  h2.display{ font-size:clamp(40px,5.6vw,78px); margin-bottom:clamp(22px,3vh,34px); }
  #paula .ghost{ bottom:1vh; font-size:clamp(150px,28vw,420px); }
  #paula .photo .in{ aspect-ratio:808/439; }
  #paula .who{ font-size:clamp(20px,2vw,27px); line-height:1.5; color:var(--paper); max-width:34ch; margin:0 0 26px; }
  .light .photo .in, .light .photo .frame{ border-color:rgba(10,10,11,.14); }'''

# ---------------------------------------------------------------- LISTAGEM
def listing():
    css = COMMON_CSS + '''

  /* Blog (lista): mesma composição da home — branco, 3 fotos proporcionais à altura da tela, texto centralizado */
  #lista .ghost{ top:6vh; font-size:clamp(200px,38vw,560px); }
  #lista .wrap{ align-items:stretch; }
  .blog-inner{ width:100%; padding-block:clamp(96px,14vh,132px); }
  .sec-head{ margin-bottom:clamp(36px,5vh,56px); }
  .sec-head .display{ font-size:clamp(48px,7vw,92px); }
  .grid3{ display:grid; grid-template-columns:repeat(3,1fr); gap:clamp(20px,2.4vw,34px); align-items:start; }
  @media (max-width:560px){ .grid3{ grid-template-columns:1fr; max-width:440px; margin-inline:auto; } }
  .post{ display:flex; flex-direction:column; }
  .post .media{ display:block; aspect-ratio:4/5; overflow:hidden; border:1px solid rgba(10,10,11,.14); }
  .post .media img{ width:100%; height:100%; object-fit:cover; display:block; will-change:transform; transform:scale(1.3); filter:grayscale(1) contrast(1.06) brightness(.95); }
  .post h3{ font-family:var(--f-display); font-weight:500; font-size:clamp(24px,2.3vw,31px); line-height:1.12; margin:20px 0 8px; letter-spacing:-.005em; }
  .post p{ margin:0; color:#5b5953; font-size:15.5px; line-height:1.55; }
  .post .more{ font-family:var(--f-label); font-size:11px; letter-spacing:.18em; text-transform:uppercase; color:var(--ink);
    margin-top:16px; border-bottom:1px solid rgba(10,10,11,.3); padding-bottom:4px; align-self:flex-start; transition:.25s; }
  .post .more:hover{ letter-spacing:.24em; }
  @media (pointer:coarse){ .post .more{ padding-block:10px 8px; } }
  /* a lista trava e o texto continua subindo (fotos ficam paradas); a Paula sobe e cobre */
  #lista > .wrap{ transform:none; }
  #lista .sec-head, #lista .post h3, #lista .post p, #lista .post .more{ translate:0 calc(var(--cy,0) * -1px); }
  @media (max-width:860px), (max-height:600px){ #lista .sec-head, #lista .post h3, #lista .post p, #lista .post .more{ translate:none; } }
  @media (min-width:861px) and (min-height:601px){
    #lista{ height:calc(100svh - 20px); min-height:0;
      --phv:clamp(170px, calc(94svh - 440px), 400px);
      --pw:min(calc(var(--phv) * .8), calc((min(1360px, 92vw) - 100px - 280px) / 3));
      --ph:calc(var(--pw) / .8); }
    .blog-inner{ height:100%; display:flex; flex-direction:column; justify-content:flex-start; padding-top:clamp(84px,11vh,112px); padding-bottom:clamp(20px,4vh,44px); }
    .sec-head{ margin-bottom:clamp(18px,3.4vh,40px); }
    #lista .wrap{ max-width:1440px; }
    .grid3{ display:flex; justify-content:space-between; gap:0; padding-inline:50px; }
    .post{ flex:0 0 var(--pw); }
    .post .media{ aspect-ratio:auto; width:var(--pw); height:var(--ph); }
    .post h3{ margin:16px -50px 6px; text-align:center; }
    .post p{ margin:0 -50px; text-align:center; }
    .post .more{ align-self:center; }
  }'''
    cards = ''
    speeds = {'como-comeca-uma-jornada-heroica': '-0.06', 'ah-esse-tal-de-inconsciente': '0.10', 'herois-e-heroinas': '-0.16'}
    for i, slug in enumerate(LIST_ORDER):
        p = BY[slug]; delay = f' style="transition-delay:{i*0.08:.2f}s"' if i else ''
        cards += f'''        <article class="post" data-speed="{speeds[slug]}">
          <a class="media" data-rev{delay} href="/{slug}/"><img data-para data-scale="1.3" data-amp="40" alt="{html.escape(p['alt'])}" src="imagens/{p['card']}"></a>
          <h3 data-rev{delay}><a href="/{slug}/">{html.escape(p['title'])}</a></h3>
          <p data-rev{delay}>{html.escape(p['excerpt'])}</p>
          <a class="more" data-rev{delay} href="/{slug}/">Leia mais →</a>
        </article>
'''
    body = f'''
<main>

  <!-- LISTA (trava; a Paula sobe e cobre) -->
  <section class="sec light" id="lista" data-pin>
    <div class="ghost" data-speed="0.55" data-x="-14" aria-hidden="true">Blog</div>
    <div class="rule" data-speed="-0.25" style="left:14%; top:-10%; height:60%"></div>
    <div class="rule" data-speed="0.3" style="right:11%; top:30%; height:70%"></div>
    <div class="wrap"><div class="blog-inner">
      <div class="sec-head" data-speed="0.12"><h1 class="display" data-rev>Blog</h1></div>
      <div class="grid3">
{cards}      </div>
    </div></div>
  </section>

{PAULA}
'''
    return head('Blog', css, '/blog/') + HEADER + body + FOOTER

# ---------------------------------------------------------------- POST
def post_page(p):
    light = ' light' if p['light'] else ''
    css = COMMON_CSS + '''

  /* abertura do post: a foto é uma camada separada (fica parada); o texto sobe junto com a seção que cobre */
  #topo{ align-items:flex-end; background:var(--ink-2); }
  #topo.light{ background:#fff; }
  #topo .ghost{ top:8vh; font-size:clamp(130px,24vw,380px); }
  .hero-photo{ position:absolute; z-index:1; top:50%; height:min(66vh,640px); height:min(66svh,640px); aspect-ratio:1600/2211; transform:translateY(-46%);
    left:max(clamp(16px,4vw,40px), calc((100vw - var(--maxw)) / 2 + clamp(16px,4vw,40px))); }
  .hero-photo .in{ height:100%; }
  #topo .wrap{ padding-block:clamp(84px,14vh,130px); align-items:flex-end; }
  #topo .hero-text{ margin-left:calc(min(66vh,640px) * .7237 + clamp(30px,6vw,96px)); margin-left:calc(min(66svh,640px) * .7237 + clamp(30px,6vw,96px)); }
  #topo .back{ display:inline-block; font-family:var(--f-label); font-weight:500; font-size:11.5px; letter-spacing:.28em; text-transform:uppercase; color:var(--paper-dim); margin-bottom:22px; padding-block:6px; }
  #topo.light .back{ color:#5b5953; }
  #topo .back:hover{ color:var(--paper); } #topo.light .back:hover{ color:var(--ink); }
  #topo h1{ font-family:var(--f-display); font-weight:300; margin:0; font-size:clamp(34px,4.6vw,72px); line-height:1.02; text-wrap:balance; }
  #topo.light h1{ color:var(--ink); }
  @media (max-width:860px){
    .hero-photo{ top:calc(50% - 14vh); top:calc(50% - 14svh); height:min(46vh,420px); height:min(46svh,420px); left:50%; transform:translate(-50%,-50%); }
    #topo .hero-text{ margin-left:0; }
    #topo .wrap{ padding-block:clamp(72px,10vh,110px); }
  }

  /* artigo */
  #artigo .ghost{ bottom:2vh; font-size:clamp(150px,30vw,460px); }
  .article{ max-width:720px; margin-inline:auto; }
  .article .lead-p{ font-family:var(--f-display); font-weight:300; font-size:clamp(26px,3vw,40px); line-height:1.22; color:var(--paper); margin:0 0 clamp(28px,5vh,48px); }
  .article p{ font-size:clamp(18px,1.5vw,20px); line-height:1.7; color:var(--paper-dim); margin:0 0 1.25em; }
  .article .lead-p + p{ padding-top:clamp(4px,1vh,10px); }
  #artigo .end{ display:inline-block; margin-top:14px; font-family:var(--f-label); font-weight:500; font-size:11.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--paper); border-bottom:1px solid var(--line); padding-block:8px 6px; transition:letter-spacing .25s; }
  #artigo .end:hover{ letter-spacing:.26em; }

  /* continue lendo */
  #mais{ background:var(--ink); }
  #mais .row{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:clamp(24px,4vw,64px); max-width:820px; margin-inline:auto; }
  @media (max-width:640px){ #mais .row{ grid-template-columns:1fr; max-width:420px; } }
  #mais .card{ display:block; }
  #mais .card .in{ aspect-ratio:4/5; overflow:hidden; border:1px solid var(--line); }
  #mais .card img{ width:100%; height:100%; object-fit:cover; display:block; filter:grayscale(1) contrast(1.06) brightness(.9); transition:transform .8s cubic-bezier(.2,.7,.2,1), filter .4s; }
  #mais .card:hover img{ transform:scale(1.04); filter:grayscale(.6) contrast(1.06) brightness(1); }
  #mais .card h3{ font-family:var(--f-display); font-weight:500; font-size:clamp(24px,2.3vw,31px); line-height:1.12; margin:18px 0 0; }
  #mais .head{ display:flex; align-items:baseline; justify-content:space-between; gap:24px; max-width:820px; margin:0 auto clamp(28px,5vh,44px); }
  #mais .head a{ font-family:var(--f-label); font-weight:500; font-size:11.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--paper-dim); padding-block:8px; }
  #mais .head a:hover{ color:var(--paper); }'''
    body_paras = f'<p class="lead-p" data-rev>{html.escape(p["paras"][0])}</p>\n' + '\n'.join(
        f'        <p data-rev>{html.escape(t)}</p>' for t in p['paras'][1:])
    others = [BY[s] for s in LIST_ORDER if s != p['slug']]
    cards = ''.join(f'''
        <a class="card" data-rev href="/{o['slug']}/"><div class="in"><img alt="{html.escape(o['alt'])}" src="imagens/{o['card']}"></div><h3>{html.escape(o['title'])}</h3></a>''' for o in others)
    body = f'''
<main>

  <!-- 1 · ABERTURA (trava; o artigo sobe e cobre) -->
  <section class="sec{light}" id="topo" data-pin data-textscroll>
    <div class="ghost" data-speed="0.4" data-x="-10" aria-hidden="true">{html.escape(p['ghost'])}</div>
    <div class="photo hero-photo"><div class="in"><img data-para alt="{html.escape(p['alt'])}" src="imagens/{p['hero']}"></div><div class="frame" style="inset:-16px 16px 16px -16px"></div></div>
    <div class="wrap"><div class="hero-text">
      <a class="back" href="/blog/">← Blog</a>
      <h1>{html.escape(p['title'])}</h1>
    </div></div>
  </section>

  <!-- 2 · ARTIGO -->
  <section class="sec" id="artigo">
    <div class="ghost" data-speed="0.5" data-x="12" aria-hidden="true">{html.escape(p['ghost'])}</div>
    <div class="rule" data-speed="-0.25" style="left:12%; top:-10%; height:55%"></div>
    <div class="wrap"><div class="pad"><div class="article">
        {body_paras}
        <a class="end" data-rev href="/blog/">← Voltar ao Blog</a>
    </div></div></div>
  </section>

  <!-- 3 · CONTINUE LENDO -->
  <section class="sec" id="mais">
    <div class="wrap"><div class="pad">
      <div class="head" data-rev><p class="eyebrow" style="margin:0">Continue lendo</p><a href="/blog/">Ver todos os posts →</a></div>
      <div class="row">{cards}
      </div>
    </div></div>
  </section>

'''
    return head(p['title'], css, '/' + p['slug'] + '/') + HEADER + body + FOOTER

if __name__ == '__main__':
    open(ROOT + 'elo_vital_blog.html', 'w', encoding='utf-8').write(listing())
    for p in POSTS:
        open(ROOT + p['file'], 'w', encoding='utf-8').write(post_page(p))
    print('geradas:', 'elo_vital_blog.html', *[p['file'] for p in POSTS])
