
# ============ v6 NEW / REWRITTEN SECTIONS (appended to part_keep.py by build_v6.py) ============
def props(items):
    """items: (emoji, x, y, width, depth, rot0, rot1, t, o)"""
    out=''
    for (e,x,y,w,d,r0,r1,t,o) in items:
        out+=f'<span class="ag-prop" data-par="{d}" style="--x:{x};--y:{y};--w:{w};--r0:{r0}deg;--r1:{r1}deg;--t:{t}s;--o:{o}s"><img data-em="{e}" alt=""></span>'
    return out

PILL_ARROW='<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10h12M11 5l5 5-5 5"/></svg>'

# ---------- PAGE HEROES ----------
def page_hero(key,word,eye,lead,pr):
    sec(f'page-hero-{key}',f'ag-ph-{key}','''
.__P__{padding:150px 24px 90px;min-height:min(78vh,760px);display:flex;align-items:center}
.__P__ .ag-wrap{width:100%}
.__P__ .ag-big{font-size:clamp(3.4rem,13.5vw,13rem);margin-top:22px;background-image:linear-gradient(90deg,#fff3cf var(--p,100%),transparent calc(var(--p,100%) + .01%))}
.__P__ .ag-lead{margin-top:28px;max-width:52ch;position:relative;z-index:2}
.__P__ .ag-big,.__P__ .ag-eye{position:relative;z-index:2}
@media (max-width:760px){.__P__{padding:120px 20px 60px;min-height:0}.__P__ .ag-prop{--w:22vw !important}}
''',f'''
<section class="__P__" id="__P__" aria-label="{eye}">
  <div class="ag-glow" style="right:0;top:0;width:60vw;height:60vw;max-width:800px;max-height:800px"></div>
  {props(pr)}
  <div class="ag-wrap">
    <div class="ag-eye" data-r>{eye}</div>
    <h1 class="ag-big" data-fill="load" aria-label="{word}">{word}</h1>
    <p class="ag-lead" data-r style="--i:1">{lead}</p>
  </div>
</section>
''','','(top of the page) ')
page_hero('work','Work','Selected work','Websites, funnels and builds, with the objective, my role and the decisions behind each one.',
  [('Trophy|trophy','70%','10%','12vw',1.4,-10,6,6,0),('Laptop|laptop','82%','48%','13vw',.8,8,-6,7,-2),('Sparkles|sparkles','58%','62%','7vw',1.8,-6,10,5,-1)])
page_hero('services','Services','Services and pricing','Six ways I can help. Prices are indicative starting points, and a tailored proposal confirms the final scope, cost and timeline.',
  [('Money bag|money_bag','72%','8%','13vw',1.2,-8,8,6,0),('Rocket|rocket','84%','46%','12vw',.8,10,-8,7,-2),('Gem stone|gem_stone','60%','64%','8vw',1.6,-6,8,5,-1)])
page_hero('process','Process','How I work','No unnecessary complexity. No unclear expectations. Just a structured process from the first conversation to launch.',
  [('Compass|compass','72%','10%','12vw',1.3,-12,6,6,0),('Magic wand|magic_wand','86%','44%','11vw',.8,8,-8,7,-2),('Light bulb|light_bulb','58%','62%','8vw',1.7,-6,10,5,-1)])
page_hero('about','About me','About','A multidisciplinary route into web design and development, and how it shapes the way I work with clients.',
  [('Artist palette|artist_palette','72%','8%','12vw',1.3,-10,8,6,0),('Keyboard|keyboard','84%','46%','13vw',.8,8,-6,7,-2),('Sparkles|sparkles','60%','64%','7vw',1.8,-6,10,5,-1)])

# ---------- HOME GALLERY (marquee of image tiles; placeholders = service categories, not fake work) ----------
TILES=[('Landing pages','Bullseye|bullseye','#3a2a08,#120d03'),('Business websites','Desktop computer|desktop_computer','#2a2a31,#0d0d11'),('Sales funnels','Rocket|rocket','#4a2a0c,#150c04'),
       ('Web applications','Gear|gear','#26262b,#0c0c0f'),('Website redesigns','Artist palette|artist_palette','#3b300c,#130f03'),('Maintenance','Hammer and wrench|hammer_and_wrench','#2b2013,#0e0a05')]
def tiles(order):
    out=''
    for lab,e,g in order:
        a,b=g.split(',')
        out+=f'<div class="ag-t" style="--a:{a};--b:{b}"><span class="ag-tg">{lab}</span><img data-em="{e}" alt=""></div>'
    return out
r1=tiles(TILES)*3; r2=tiles(list(reversed(TILES)))*3
sec('home-gallery','ag-gal','''
.__P__{padding:20px 0 120px;background:var(--ag-bg)}
.__P__.ag-sheet{padding-top:20px}
.__P__ .ag-row{overflow:hidden;margin-bottom:18px}
.__P__ .ag-track{display:flex;gap:18px;width:max-content;animation:ag-gal-run 60s linear infinite}
.__P__ .ag-row.ag-b .ag-track{animation-direction:reverse;animation-duration:70s}
.__P__ .ag-t{position:relative;flex:none;width:clamp(240px,24vw,340px);aspect-ratio:3/2;border-radius:26px;border:1px solid rgba(255,255,255,.14);overflow:hidden;background:linear-gradient(150deg,var(--a),var(--b))}
.__P__ .ag-t img{position:absolute;right:-4%;bottom:-8%;width:62%;filter:drop-shadow(0 18px 18px rgba(0,0,0,.5));transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-t:hover img{transform:scale(1.1) rotate(-6deg)}
.__P__ .ag-tg{position:absolute;left:18px;top:16px;z-index:1;font-size:.74rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#fff;padding:6px 12px;border-radius:999px;background:rgba(0,0,0,.4);border:1px solid rgba(255,255,255,.18)}
@keyframes ag-gal-run{to{transform:translateX(-33.333%)}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-track{animation:none}}
''',f'''
<section class="__P__" id="__P__" aria-label="What I build">
  <div class="ag-row"><div class="ag-track">{r1}</div></div>
  <div class="ag-row ag-b"><div class="ag-track">{r2}</div></div>
</section>
''','','(Home, under the logos) ')

# ---------- HOME ABOUT ----------
sec('home-about','ag-habout','''
.__P__{padding-bottom:130px}
.__P__ .ag-box{position:relative;max-width:1000px;margin:56px auto 0;text-align:center}
.__P__ .ag-words{margin:0;font-size:clamp(1.35rem,1.6vw + .9rem,2.2rem);font-weight:700;line-height:1.45;letter-spacing:-.015em}
.__P__ .ag-facts{display:flex;flex-wrap:wrap;gap:12px 48px;justify-content:center;margin:48px 0 40px;padding-top:36px;border-top:1px solid var(--ag-line)}
.__P__ .ag-facts strong{display:block;font-size:2.4rem;font-weight:900;letter-spacing:-.04em;line-height:1}
.__P__ .ag-facts span{display:block;margin-top:6px;font-size:.84rem;color:var(--ag-muted)}
.__P__ .ag-big{text-align:center}
@media (max-width:760px){.__P__{padding-bottom:80px}.__P__ .ag-prop{--w:20vw !important}}
''',f'''
<section class="__P__" id="__P__" aria-label="About">
  <div class="ag-glow" style="left:20%;top:10%;width:60vw;height:60vw;max-width:900px;max-height:900px"></div>
  {props([('Sparkles|sparkles','4%','18%','9vw',1.6,-8,10,6,0),('Laptop|laptop','82%','10%','13vw',1.1,8,-8,7,-2),('Artist palette|artist_palette','86%','62%','11vw',1.8,-10,8,6.5,-1),('Light bulb|light_bulb','3%','66%','10vw',.8,6,-8,7.5,-3)])}
  <div class="ag-wrap">
    <h2 class="ag-big" data-fill>About me</h2>
    <div class="ag-box">
      <p class="ag-words" data-words>I started in graphic design, then taught myself Python by building a calculator and a ping-pong game. That curiosity led to web development, Figma and GoHighLevel, where I learned how websites, funnels and CRM automation work together. Today I design and build websites that look considered, work reliably and serve the goals of the business behind them.</p>
      <div class="ag-facts" data-r>
        <div><strong>6+</strong><span>Business websites</span></div>
        <div><strong>5+</strong><span>Landing pages</span></div>
        <div><strong>3-4 yrs</strong><span>Designing and building</span></div>
      </div>
      <a class="ag-pill" data-ag-link="about" href="/about" data-r>More about me {PILL_ARROW}</a>
    </div>
  </div>
</section>
''','','(Home) ')

# ---------- HOME SERVICES (light) ----------
rows=''.join(f'''<a class="ag-row" data-ag-link="services" href="/services" data-r style="--i:{i%3}">
  <span class="ag-n">0{i+1}</span><span class="ag-nm">{s[0].replace(' Design & Development','').replace(' Development','')}</span><span class="ag-ds">{s[4]}</span>
  <span class="ag-go"><img data-em="{s[3]}" alt="">{ARROW}</span></a>''' for i,s in enumerate(SERVICES))
sec('home-services','ag-hsvc','''
.__P__ .ag-list{margin-top:60px;border-top:1.5px solid var(--ag-text)}
.__P__ .ag-row{position:relative;display:grid;grid-template-columns:clamp(70px,9vw,120px) 1fr 1.2fr 120px;gap:24px;align-items:center;padding:34px 0;border-bottom:1px solid var(--ag-line-2);text-decoration:none;color:inherit;transition:padding .35s cubic-bezier(.2,.7,.2,1),background .3s}
.__P__ .ag-row:hover{padding-left:22px;background:linear-gradient(90deg,rgba(240,185,62,.28),transparent 70%)}
.__P__ .ag-n{font-weight:900;font-size:clamp(2rem,3.6vw,3.6rem);letter-spacing:-.05em;line-height:1}
.__P__ .ag-nm{font-weight:800;font-size:clamp(1rem,.8vw + .8rem,1.4rem);text-transform:uppercase;letter-spacing:.02em;line-height:1.25}
.__P__ .ag-ds{color:var(--ag-muted);line-height:1.55;font-size:.98rem}
.__P__ .ag-go{display:flex;justify-content:flex-end;align-items:center;gap:12px}
.__P__ .ag-go img{width:56px;height:56px;opacity:0;transform:translateY(8px) scale(.8) rotate(-8deg);transition:opacity .3s,transform .35s cubic-bezier(.2,.7,.2,1);filter:drop-shadow(0 12px 10px rgba(0,0,0,.35))}
.__P__ .ag-row:hover .ag-go img{opacity:1;transform:none}
.__P__ .ag-go svg{width:24px;height:24px;transition:transform .3s}
.__P__ .ag-row:hover .ag-go svg{transform:translateX(6px)}
.__P__ .ag-foot{margin-top:56px;display:flex;flex-wrap:wrap;gap:16px 28px;align-items:center}
.__P__ .ag-foot p{margin:0;color:var(--ag-muted);font-size:.95rem;max-width:46ch}
@media (max-width:900px){.__P__ .ag-row{grid-template-columns:56px 1fr 36px;gap:14px;padding:26px 0}.__P__ .ag-ds{display:none}.__P__ .ag-go img{display:none}}
@media (hover:none){.__P__ .ag-go img{opacity:1;transform:none}}
''',f'''
<section class="__P__" id="__P__" aria-label="Services">
  {props([('Rocket|rocket','78%','2%','11vw',1.4,-8,8,6.5,0),('Gem stone|gem_stone','90%','24%','7vw',.8,8,-8,7,-2)])}
  <div class="ag-wrap">
    <h2 class="ag-big" data-fill>Services</h2>
    <div class="ag-list">{rows}</div>
    <div class="ag-foot" data-r><a class="ag-pill" data-ag-link="services" href="/services">Pricing and details {PILL_ARROW}</a><p>Every price is a starting point. You get a tailored proposal before anything begins.</p></div>
  </div>
</section>
''','','(Home) ')

# ---------- HOME WORK (sticky stacked project cards) ----------
sec('home-work','ag-hwork','''
.__P__{padding-bottom:140px}
.__P__ .ag-stack{margin-top:60px}
.__P__ .ag-card{position:sticky;top:calc(92px + var(--k) * 28px);margin-bottom:6vh;border-radius:34px;border:1.5px solid rgba(255,255,255,.28);background:#0b0b0f;padding:22px;box-shadow:0 -20px 50px -20px rgba(0,0,0,.8),0 0 0 6px #07070a,0 0 0 7.5px rgba(255,255,255,.1)}
.__P__ .ag-ch{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:6px 10px 18px}
.__P__ .ag-no{font-weight:900;font-size:clamp(1.8rem,3vw,3rem);letter-spacing:-.05em;line-height:1}
.__P__ .ag-ct{display:flex;align-items:center;gap:20px;min-width:0}
.__P__ .ag-ct small{display:block;font-size:.68rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ .ag-ct b{display:block;font-size:1.05rem;letter-spacing:-.01em}
.__P__ .ag-lv{flex:none;padding:10px 20px;border-radius:999px;border:1.5px solid rgba(255,255,255,.4);color:var(--ag-text);font-size:.7rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;transition:background .25s,color .25s,border-color .25s}
.__P__ a.ag-lv:hover{background:var(--ag-gold);color:var(--ag-gold-ink);border-color:var(--ag-gold)}
.__P__ .ag-lv.ag-off{opacity:.6;border-style:dashed}
.__P__ .ag-imgs{display:grid;grid-template-columns:1.6fr 1fr;grid-template-rows:1fr 1fr;gap:14px;height:clamp(240px,38vw,440px)}
.__P__ .ag-im{position:relative;border-radius:22px;overflow:hidden;border:1px solid rgba(255,255,255,.14);background:repeating-linear-gradient(135deg,rgba(240,185,62,.08) 0 14px,rgba(240,185,62,.02) 14px 28px)}
.__P__ .ag-im:first-child{grid-row:1/3}
.__P__ .ag-im img.ag-shot{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top}
.__P__ .ag-im .ag-ph{position:absolute;inset:0;border:0;display:grid;place-content:center;text-align:center;gap:6px;padding:10px}
.__P__ .ag-im .ag-emo{position:absolute;left:50%;top:38%;width:min(28%,150px);transform:translate(-50%,-50%);filter:drop-shadow(0 16px 16px rgba(0,0,0,.5))}
.__P__ .ag-im:not(:first-child) .ag-emo{display:none}
.__P__ .ag-flag{position:absolute;left:14px;top:14px;z-index:2;padding:6px 12px;border-radius:999px;background:var(--ag-gold);color:var(--ag-gold-ink);font-size:.68rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.__P__ .ag-all{margin-top:48px;display:flex;justify-content:center}
@media (max-width:760px){.__P__ .ag-card{padding:14px;border-radius:26px;top:calc(76px + var(--k) * 18px)}.__P__ .ag-imgs{grid-template-columns:1fr;grid-template-rows:auto;height:auto}.__P__ .ag-im{aspect-ratio:16/10}.__P__ .ag-im:first-child{grid-row:auto}.__P__ .ag-im:nth-child(n+2){display:none}.__P__ .ag-ct{gap:12px}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-card{position:relative;top:0}}
''',f'''
<section class="__P__" id="__P__" aria-label="Selected work">
  {props([('Trophy|trophy','80%','1%','10vw',1.6,-8,8,6,0),('Sparkles|sparkles','4%','7%','7vw',1.2,8,-8,7,-2)])}
  <div class="ag-wrap">
    <h2 class="ag-big" data-fill>Projects</h2>
    <p class="ag-lead" data-r style="margin-top:22px">Placeholders show the layout. Your real projects, screenshots and links replace them.</p>
    <div class="ag-stack" id="__P__-stack"></div>
    <div class="ag-all" data-r><a class="ag-pill" data-ag-link="work" href="/work">See all work {PILL_ARROW}</a></div>
  </div>
</section>
''','''
  /* ---------- CONFIG: your real projects ---------- */
  var PROJECTS=[
    /* { name:'Project name', client:'Client or industry', category:'Business website', live:'https://...', caseStudy:'/work/project',
         images:['https://.../1.jpg','https://.../2.jpg','https://.../3.jpg'] }, */
  ];
  var PLACEHOLDERS=[
    {name:'Project name',client:'Client or industry',category:'Business website',emo:'Desktop computer|desktop_computer'},
    {name:'Project name',client:'Client or industry',category:'Sales funnel',emo:'Rocket|rocket'},
    {name:'Project name',client:'Client or industry',category:'Landing page',emo:'Bullseye|bullseye'}
  ];
  /* ------------------------------------------------ */
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  var real=PROJECTS.length>0, list=(real?PROJECTS:PLACEHOLDERS).slice(0,4), host=document.getElementById('ag-hwork-stack');
  list.forEach(function(p,i){
    var cells='';
    for(var k=0;k<3;k++){
      var img=real&&p.images&&p.images[k];
      cells+='<div class="ag-im">'+(img?'<img class="ag-shot" loading="lazy" alt="'+esc(p.name)+'" src="'+esc(img)+'">':'<div class="ag-ph"><b>Image placeholder</b><span>'+(k===0?'1600 x 1000':'800 x 500')+' px</span></div>'+(k===0?'<img class="ag-emo" data-em="'+p.emo+'" alt="">':''))+(!real&&k===0?'<span class="ag-flag">Placeholder</span>':'')+'</div>';
    }
    var lv=p.live?'<a class="ag-lv" target="_blank" rel="noopener" href="'+esc(p.live)+'">Live project</a>':'<span class="ag-lv ag-off">'+(real?'Case study':'Add link')+'</span>';
    var a=document.createElement('article'); a.className='ag-card'; a.style.setProperty('--k',i);
    a.innerHTML='<div class="ag-ch"><div class="ag-ct"><span class="ag-no">0'+(i+1)+'</span><div><small>'+esc(p.category)+'</small><b>'+esc(p.name)+' <span style="color:#b9b1a1;font-weight:600">&middot; '+esc(p.client)+'</span></b></div></div>'+lv+'</div><div class="ag-imgs">'+cells+'</div>';
    host.appendChild(a);
  });
''','(Home) ')

# ---------- HOME PROCESS (light) ----------
psr=''.join(f'''<li class="ag-st" data-r style="--i:{i%2}"><span class="ag-n">0{i+1}</span><div><h3>{s[0]}</h3><span class="ag-tm">{s[1]}</span><p>{s[2]}</p></div><img data-em="{s[3]}" alt=""></li>''' for i,s in enumerate(STEPS))
sec('home-process','ag-hproc','''
.__P__ ol{list-style:none;margin:60px 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:0 64px;border-top:1.5px solid var(--ag-text)}
.__P__ .ag-st{display:grid;grid-template-columns:clamp(60px,6vw,96px) 1fr 64px;gap:20px;align-items:start;padding:32px 0;border-bottom:1px solid var(--ag-line-2)}
.__P__ .ag-n{font-weight:900;font-size:clamp(2rem,3.2vw,3.2rem);letter-spacing:-.05em;line-height:1}
.__P__ h3{margin:0;font-size:1.15rem;font-weight:800;text-transform:uppercase;letter-spacing:.02em}
.__P__ .ag-tm{display:inline-block;margin-top:8px;padding:4px 12px;border-radius:999px;background:rgba(240,185,62,.3);font-size:.78rem;font-weight:800}
.__P__ .ag-st p{margin:12px 0 0;color:var(--ag-muted);line-height:1.6;font-size:.96rem}
.__P__ .ag-st img{width:64px;height:64px;filter:drop-shadow(0 12px 10px rgba(0,0,0,.35));transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-st:hover img{transform:translateY(-6px) rotate(-8deg) scale(1.08)}
.__P__ .ag-foot{margin-top:56px}
@media (max-width:900px){.__P__ ol{grid-template-columns:1fr}.__P__ .ag-st{grid-template-columns:50px 1fr 48px}.__P__ .ag-st img{width:48px;height:48px}}
''',f'''
<section class="__P__" id="__P__" aria-label="Process">
  {props([('Compass|compass','80%','1%','10vw',1.4,-8,8,6.5,0)])}
  <div class="ag-wrap">
    <h2 class="ag-big" data-fill>Process</h2>
    <p class="ag-lead" data-r style="margin-top:22px;max-width:48ch">No unnecessary complexity. No unclear expectations. Just a structured process from the first conversation to launch.</p>
    <ol>{psr}</ol>
    <div class="ag-foot" data-r><a class="ag-pill" data-ag-link="process" href="/process">The full process {PILL_ARROW}</a></div>
  </div>
</section>
''','','(Home) ')

# ---------- HOME TESTIMONIALS (placeholder wall) ----------
sec('home-testimonials','ag-htest','''
.__P__{padding-left:0;padding-right:0;padding-bottom:130px}
.__P__ .ag-tt{padding:0 24px;max-width:1248px;margin:0 auto 70px;display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.__P__ h2{margin:0;font-weight:900;text-transform:uppercase;letter-spacing:-.04em;line-height:.95;font-size:clamp(2.2rem,5.4vw,5.2rem);max-width:12ch}
.__P__ .ag-tt img{width:clamp(54px,7vw,100px);animation:ag-prop-f 6s ease-in-out infinite;filter:drop-shadow(0 16px 14px rgba(0,0,0,.5))}
.__P__ .ag-wall{transform:rotate(-3deg);margin:0 -4vw}
.__P__ .ag-lane{overflow:hidden;margin-bottom:18px}
.__P__ .ag-track{display:flex;gap:18px;width:max-content;animation:ag-ht-run 70s linear infinite}
.__P__ .ag-lane.ag-b .ag-track{animation-direction:reverse;animation-duration:82s}
.__P__ .ag-q{flex:none;width:clamp(300px,30vw,440px);display:flex;gap:16px;align-items:flex-start;padding:22px;border-radius:28px;border:1.5px solid rgba(255,255,255,.26);background:#0b0b0f}
.__P__ .ag-av{flex:none;width:64px;height:64px;border-radius:50%;display:grid;place-items:center;border:1.5px dashed rgba(240,185,62,.6);color:var(--ag-gold);font-size:.62rem;font-weight:800;text-align:center;letter-spacing:.06em;text-transform:uppercase;line-height:1.2}
.__P__ .ag-q p{margin:0;font-size:.95rem;line-height:1.55;color:var(--ag-text)}
.__P__ .ag-q small{display:block;margin-top:12px;font-size:.7rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ .ag-q em{font-style:normal;color:var(--ag-gold);font-weight:800}
@keyframes ag-ht-run{to{transform:translateX(-50%)}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-track{animation:none}.__P__ .ag-tt img{animation:none}}
''','''
<section class="__P__" id="__P__" aria-label="Client testimonials">
  <div class="ag-tt"><h2 data-r>What clients are saying</h2><img data-em="Sparkles|sparkles" alt=""></div>
  <div class="ag-wall" id="__P__-wall"></div>
</section>
''','''
  /* ---------- CONFIG: add real, approved testimonials only ---------- */
  var TESTIMONIALS=[
    /* { quote:'A real client quote.', name:'Client name', role:'Business', photo:'https://...' }, */
  ];
  /* ------------------------------------------------------------------ */
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  var real=TESTIMONIALS.length>0, base=real?TESTIMONIALS:[1,2,3,4].map(function(){return {ph:true,quote:'Placeholder. A real quote from a client, used with their permission, goes here.',name:'Client name',role:'Business'};});
  function card(t){return '<div class="ag-q"><div class="ag-av">'+(t.photo?'<img alt="" src="'+esc(t.photo)+'" style="width:100%;height:100%;border-radius:50%;object-fit:cover">':'Photo')+'</div><div><p>'+(t.ph?'<em>Placeholder.</em> '+esc(t.quote.replace(/^Placeholder\\.\\s*/,'')):esc(t.quote))+'</p><small>'+esc(t.name)+' &middot; '+esc(t.role)+'</small></div></div>';}
  function lane(arr,cls){var h=arr.map(card).join('');return '<div class="ag-lane '+cls+'"><div class="ag-track">'+h+h+h+h+'</div></div>';}
  var rev=base.slice().reverse();
  document.getElementById('ag-htest-wall').innerHTML=lane(base,'')+lane(rev,'ag-b');
''','(Home) ')

# ---------- CTA (light, "let's get in touch") ----------
sec('home-cta','ag-hcta','''
.__P__{padding-bottom:140px}
.__P__ .ag-big{font-size:clamp(3rem,10.4vw,10rem);line-height:.92}
.__P__ .ag-sub{margin:34px 0 0;max-width:46ch;font-size:clamp(1.05rem,.4vw + 1rem,1.3rem);line-height:1.6;color:var(--ag-muted)}
.__P__ .ag-cta{display:flex;flex-wrap:wrap;gap:14px;margin-top:38px;position:relative;z-index:2}
.__P__ .ag-pill.ag-solid{background:var(--ag-text);color:var(--ag-bg)}
.__P__ .ag-pill.ag-solid:hover{background:var(--ag-gold);color:var(--ag-gold-ink)}
.__P__ .ag-note{margin:22px 0 0;color:var(--ag-muted);font-size:.92rem;max-width:56ch;line-height:1.6;position:relative;z-index:2}
.__P__ .ag-big,.__P__ .ag-sub{position:relative;z-index:2}
@media (max-width:760px){.__P__ .ag-prop{--w:24vw !important;opacity:.9}}
''',f'''
<section class="__P__" id="__P__" aria-label="Start a project">
  {props([('Rocket|rocket','74%','10%','15vw',1.5,-10,8,6.5,0),('Sparkles|sparkles','90%','52%','8vw',.9,8,-8,6,-2),('Handshake|handshake','66%','60%','11vw',1.9,-6,10,7,-3)])}
  <div class="ag-wrap">
    <h2 class="ag-big" data-fill>Let's get in touch</h2>
    <p class="ag-sub" data-r>Have a project in mind? Let's build something that works.</p>
    <div class="ag-cta" data-r><a class="ag-pill ag-solid" data-ag-link="start" href="/start">Start a project {PILL_ARROW}</a><a class="ag-pill" data-ag-link="contact" href="/contact#book">Book a discovery call</a></div>
    <p class="ag-note" data-r>I typically respond to project inquiries within 24 business hours, Monday to Friday. The discovery call is free and lasts 20 minutes.</p>
  </div>
</section>
''','','(Home and most pages, before the footer) ')
print('built v6')
