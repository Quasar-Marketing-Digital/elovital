#!/usr/bin/env python3
"""Monta a pasta dist/ pronta para subir no servidor (HTML estático, sem WordPress/Elementor).
   Cada página vira <endereço>/index.html; assets e imagens ficam em /assets e /imagens (caminhos absolutos)."""
import os, re, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
DIST = ROOT + 'dist/'
MAP = {  # arquivo do projeto -> caminho publicado
  'elo_vital_home_v5.html': 'index.html',
  'elo_vital_psicologia_junguiana.html': 'psicologia-junguiana/index.html',
  'elo_vital_jogo_do_heroi.html': 'o-jogo-do-heroi/index.html',
  'elo_vital_blog.html': 'blog/index.html',
  'elo_vital_post_herois_e_heroinas.html': 'herois-e-heroinas/index.html',
  'elo_vital_post_como_comeca_uma_jornada_heroica.html': 'como-comeca-uma-jornada-heroica/index.html',
  'elo_vital_post_ah_esse_tal_de_inconsciente.html': 'ah-esse-tal-de-inconsciente/index.html',
  'elo_vital_404.html': '404.html',
}
USADAS = set()
if os.path.isdir(DIST): shutil.rmtree(DIST)
for src, dst in MAP.items():
    s = open(ROOT + src, encoding='utf-8').read()
    # caminhos relativos -> absolutos (a página fica em subpasta)
    s = re.sub(r'((?:src|href)=")(assets/|imagens/)', r'\1/\2', s)
    s = re.sub(r"(url\(')(imagens/)", r"\1/\2", s)
    USADAS.update(re.findall(r'/(imagens/[^"\')]+)', s))
    USADAS.update(re.findall(r'/(assets/[^"\')]+)', s))
    os.makedirs(os.path.dirname(DIST + dst) or DIST, exist_ok=True)
    open(DIST + dst, 'w', encoding='utf-8').write(s)
for f in sorted(USADAS):
    os.makedirs(os.path.dirname(DIST + f), exist_ok=True); shutil.copy(ROOT + f, DIST + f)
print(len(MAP), 'páginas +', len(USADAS), 'arquivos de apoio em', DIST)
