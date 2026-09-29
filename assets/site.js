/* Elo Vital — comportamento compartilhado das páginas (tirado da home v5, já aprovada).
   Menu, reveal, parallax de fundo (0,3×), camadas com velocidades diferentes, fotos com parallax interno. */
(function(){
  const rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clamp = (v,a,b)=>Math.max(a,Math.min(b,v));
  document.documentElement.classList.add('js');

  // ---- menu (celular/tablet): abre/fecha; fecha ao escolher um item ou com Esc
  const menuBtn = document.getElementById('menubtn'), navEl = document.getElementById('nav');
  if(menuBtn && navEl){
    const setMenu = open => { navEl.classList.toggle('open', open); menuBtn.setAttribute('aria-expanded', open); menuBtn.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu'); };
    menuBtn.addEventListener('click', ()=> setMenu(!navEl.classList.contains('open')));
    navEl.addEventListener('click', e=>{ if(e.target.closest('a')) setMenu(false); });
    addEventListener('keydown', e=>{ if(e.key==='Escape') setMenu(false); });
    addEventListener('resize', ()=>{ if(innerWidth>980) setMenu(false); }, {passive:true});
  }

  // ---- reveal ao entrar na tela
  const io = new IntersectionObserver(es=>{ es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }); },
    {threshold:.16, rootMargin:'0px 0px -6% 0px'});
  document.querySelectorAll('[data-rev]').forEach(el=>io.observe(el));

  // ---- texto vertical claro/escuro conforme a seção por baixo (seções brancas têm .light)
  const lights = [...document.querySelectorAll('.sec.light')];
  function updChrome(){
    const y = innerHeight - 90;
    document.body.classList.toggle('vm-light', lights.some(s=>{ const r=s.getBoundingClientRect(); return r.top < y && r.bottom > y; }));
  }
  if(lights.length){ addEventListener('scroll', updChrome, {passive:true}); addEventListener('resize', updChrome, {passive:true}); updChrome(); }

  if(rm) return;

  // ---- parallax
  const K = 0.7;   // fundo anda ~0,3× do scroll (igual ao Jogo do Herói da home)
  const bgs = [...document.querySelectorAll('[data-bgpar]')].map(el=>({ el, host: el.parentElement, s: parseFloat(el.dataset.scale)||1.15 }));
  const layers = [...document.querySelectorAll('[data-speed]')].map(el=>({
    el, host: el.parentElement, sp: parseFloat(el.dataset.speed)||0, x: parseFloat(el.dataset.x)||0,
    deco: el.classList.contains('ghost') || el.classList.contains('rule') }));
  const inner = [...document.querySelectorAll('[data-para]')].map(el=>({
    el, host: el.closest('.in')||el.parentElement, s: parseFloat(el.dataset.scale)||1.1, amp: parseFloat(el.dataset.amp)||12 }));
  let tk = false;
  function upd(){
    const vh = innerHeight, vw = innerWidth;
    for(const b of bgs){
      const r = b.host.getBoundingClientRect(); if(r.bottom < -vh || r.top > 2*vh) continue;
      const prog = clamp((r.top + r.height/2 - vh/2)/vh, -0.9, 0.9);
      // seção mais baixa que a tela precisa de mais folga de imagem: 0,35×(vh - altura) + 8px, para nunca aparecer vazio
      const need = (K/2)*Math.max(0, vh - r.height) + 8;
      const s = Math.max(b.s, 1 + 2*need/r.height);
      b.el.style.transform = 'translateY(' + (-prog*K*vh).toFixed(2) + 'px) scale(' + s.toFixed(4) + ')';
    }
    for(const l of layers){
      const r = l.host.getBoundingClientRect(); if(r.bottom < -vh || r.top > 2*vh) continue;
      const prog = clamp((r.top + r.height/2 - vh/2)/vh, -1.2, 1.2);
      // telas estreitas: conteúdo não deriva (evita sobreposição quando empilhado); só ghost/linhas seguem
      const sp = vw <= 860 && !l.deco ? l.sp*0.3 : l.sp;
      l.el.style.transform = 'translate3d(' + (prog*l.x*vw/100).toFixed(1) + 'px,' + (-prog*sp*vh).toFixed(1) + 'px,0)';
    }
    for(const i of inner){
      const r = i.host.getBoundingClientRect(); if(r.bottom < -vh || r.top > 2*vh) continue;
      const prog = clamp((r.top + r.height/2 - vh/2)/vh, -1, 1);
      i.el.style.transform = 'translateY(' + (prog*i.amp).toFixed(1) + 'px) scale(' + i.s + ')';
    }
    tk = false;
  }
  addEventListener('scroll', ()=>{ if(!tk){ tk = true; requestAnimationFrame(upd); } }, {passive:true});
  addEventListener('resize', upd, {passive:true});
  upd();
})();
