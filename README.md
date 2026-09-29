# Elo Vital — site estático

Site em HTML puro (sem WordPress/Elementor). A pasta **`dist/`** é o site pronto para subir no servidor.

## Páginas
| Endereço | Arquivo de origem |
|---|---|
| `/` | `elo_vital_home_v5.html` |
| `/psicologia-junguiana/` | `elo_vital_psicologia_junguiana.html` |
| `/o-jogo-do-heroi/` | `elo_vital_jogo_do_heroi.html` |
| `/blog/` | `elo_vital_blog.html` |
| `/herois-e-heroinas/` | `elo_vital_post_herois_e_heroinas.html` |
| `/como-comeca-uma-jornada-heroica/` | `elo_vital_post_como_comeca_uma_jornada_heroica.html` |
| `/ah-esse-tal-de-inconsciente/` | `elo_vital_post_ah_esse_tal_de_inconsciente.html` |

Os endereços são os mesmos do site atual, exceto `/o-jogo-do-heroi/` (hoje é `/o-jogo-do-heroi-new-copy/`; configurar um redirecionamento no servidor).

## Como publicar
1. Subir o conteúdo de `dist/` para a raiz do servidor (`/`, `/assets/`, `/imagens/` e as pastas das páginas).
2. O servidor precisa servir `index.html` ao abrir uma pasta (padrão em Apache, Nginx, Netlify, Vercel, Cloudflare Pages, GitHub Pages).
3. Antes de trocar o site no ar, conferir os endereços antigos que precisam de redirecionamento.

## Como alterar
- Estilo e comportamento compartilhados: `assets/site.css` e `assets/site.js`.
- Blog (listagem e posts): `python3 tools/gerar_blog.py` regera as 4 páginas.
- Depois de qualquer mudança: `python3 tools/montar_site.py` refaz a pasta `dist/`.

## Pendências
- Instagram: link ainda `#` (a conta não existe), no topo e no rodapé, em todas as páginas.
- Foto do Jogo do Herói: o arquivo original tem 598 px (ampliada, perde nitidez); trocar por versão maior.
- Foto da Paula: 808 px, sRGB. A versão Adobe RGB de teste fica em `imagens/`, mas não é usada.
- Textos copiados sem correção; erros de digitação do site original (acentos, "tranformações", "aEles").
- Sem `meta description`, favicon e página 404.
