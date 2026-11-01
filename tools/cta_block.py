# ---------- CTA (light, "let's get in touch") with cartoon portrait + flying 3D emoji ----------
sec('home-cta','ag-hcta','''
.__P__{padding-bottom:0;overflow:hidden}
.__P__ .ag-wrap{min-height:min(76vh,640px)}
.__P__ .ag-big{font-size:clamp(3rem,10vw,9.6rem);line-height:.92;position:relative;z-index:3}
.__P__ .ag-sub{margin:30px 0 0;max-width:36ch;font-size:clamp(1.05rem,.4vw + 1rem,1.3rem);line-height:1.6;color:var(--ag-muted);position:relative;z-index:3}
.__P__ .ag-cta{display:flex;flex-wrap:wrap;gap:14px;margin-top:34px;position:relative;z-index:3}
.__P__ .ag-pill.ag-solid{background:var(--ag-text);color:var(--ag-bg)}
.__P__ .ag-pill.ag-solid:hover{background:var(--ag-gold);color:var(--ag-gold-ink)}
.__P__ .ag-note{margin:22px 0 120px;color:var(--ag-muted);font-size:.92rem;max-width:44ch;line-height:1.6;position:relative;z-index:3}
.__P__ .ag-me{position:absolute;z-index:2;right:max(24px,calc((100vw - 1248px)/2 + 24px));bottom:0;width:min(34vw,430px);aspect-ratio:3/4;pointer-events:none}
.__P__ .ag-me .ag-meph{position:absolute;inset:0;display:grid;place-content:center;text-align:center;gap:6px;padding:12%;border:1.5px dashed rgba(138,90,0,.55);border-bottom:0;border-radius:999px 999px 0 0;background:radial-gradient(closest-side,rgba(240,185,62,.28),rgba(240,185,62,.06) 70%,transparent);color:var(--ag-gold-t)}
.__P__ .ag-me .ag-meph svg{width:46px;height:46px;margin:0 auto}
.__P__ .ag-me .ag-meph b{font-size:.74rem;letter-spacing:.14em;text-transform:uppercase}
.__P__ .ag-me .ag-meph span{font-size:.78rem;color:var(--ag-muted);line-height:1.4}
.__P__ .ag-me img.ag-mephoto{position:absolute;left:50%;bottom:0;height:100%;width:auto;max-width:none;transform:translateX(-50%);filter:drop-shadow(0 24px 30px rgba(0,0,0,.25))}
.__P__ .ag-me.ag-has .ag-meph{display:none}
.__P__ .ag-glow2{position:absolute;z-index:0;right:6%;bottom:-10%;width:54vw;height:54vw;max-width:760px;max-height:760px;border-radius:50%;background:radial-gradient(closest-side,rgba(240,185,62,.5),rgba(240,185,62,.14) 60%,transparent 76%);pointer-events:none}
@media (max-width:900px){.__P__ .ag-wrap{min-height:0}.__P__ .ag-note{margin-bottom:36px}.__P__ .ag-me{position:relative;right:auto;margin:0 auto;width:min(70vw,320px)}.__P__ .ag-prop{--w:19vw !important}}
''',f'''
<section class="__P__" id="__P__" aria-label="Start a project">
  <div class="ag-glow2"></div>
  {props([('Rocket|rocket','52%','10%','11vw',1.5,-10,8,6.5,0),('Woman technologist|woman_technologist@Medium-Dark','58%','52%','10vw',1.1,8,-8,7,-2),('Sparkles|sparkles','90%','14%','7vw',.9,8,-8,6,-1),('Woman artist|woman_artist@Medium-Dark','92%','52%','9vw',1.7,-8,10,7.5,-3),('Handshake|handshake','47%','70%','8vw',1.9,-6,10,7,-3)])}
  <div class="ag-wrap">
    <h2 class="ag-big" data-fill>Let's get in touch</h2>
    <p class="ag-sub" data-r>Have a project in mind? Let's build something that works.</p>
    <div class="ag-cta" data-r><a class="ag-pill ag-solid" data-ag-link="start" href="/start">Start a project {PILL_ARROW}</a><a class="ag-pill" data-ag-link="contact" href="/contact#book">Book a discovery call</a></div>
    <p class="ag-note" data-r>I typically respond to project inquiries within 24 business hours, Monday to Friday. The discovery call is free and lasts 20 minutes.</p>
  </div>
  <div class="ag-me" id="__P__-meb"><div class="ag-meph"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="24" cy="18" r="8"/><path d="M8 42c2-9 8-14 16-14s14 5 16 14"/></svg><b>Cartoon portrait placeholder</b><span>Transparent PNG of your cartoon avatar (PHOTO_URL)</span></div><img class="ag-mephoto" id="__P__-me" alt="Azeez Gazalle" hidden></div>
</section>
''','''
  var PHOTO_URL='';   /* transparent PNG of your cartoon avatar. Empty = placeholder. */
  if(PHOTO_URL){var me=document.getElementById('ag-hcta-me');me.src=PHOTO_URL;me.hidden=false;document.getElementById('ag-hcta-meb').className+=' ag-has';}
''','(Home and most pages, before the footer) ')
