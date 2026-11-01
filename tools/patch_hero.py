import re
p='../sections/home-hero.html'
s=open(p).read()
js=s[s.index('<script src="https://cdnjs'):]
head=s[:s.index('<style>')]
head=head.replace('home-hero v5','home-hero v6')
css='''<style>
  .ag-hero{--ag-bg:#07070a;--ag-line:rgba(255,255,255,.12);--ag-text:#f8f3e9;--ag-muted:#b9b1a1;--ag-gold:#f0b93e;--ag-gold-hi:#ffd479;--ag-gold-ink:#1a1204;
    position:relative;overflow:hidden;background:var(--ag-bg);color:var(--ag-text);isolation:isolate;font-family:'Figtree',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    min-height:max(100vh,640px);box-sizing:border-box;padding:110px 24px 0;display:flex;flex-direction:column;--sp:0}
  .ag-hero *,.ag-hero *::before,.ag-hero *::after{box-sizing:border-box}
  .ag-hero__glow{position:absolute;z-index:-1;left:50%;top:42%;width:min(90vw,1100px);height:min(90vw,1100px);transform:translate(-50%,-50%);background:radial-gradient(closest-side,rgba(240,185,62,.3),rgba(240,185,62,.1) 50%,transparent 74%);pointer-events:none}
  .ag-hero__canvas{position:absolute;inset:0;width:100%;height:100%;z-index:4;pointer-events:none;display:block;-webkit-mask-image:linear-gradient(180deg,#000 82%,transparent 100%);mask-image:linear-gradient(180deg,#000 82%,transparent 100%)}
  .ag-hero [data-i]{opacity:0;filter:blur(10px);transform:translateY(18px);animation:ag-hero-in .9s cubic-bezier(.2,.7,.2,1) forwards;animation-delay:calc(var(--d,0) * 110ms + 100ms)}
  @keyframes ag-hero-in{to{opacity:1;filter:blur(0);transform:none}}
  .ag-hero__bar{position:relative;z-index:2;text-align:center}
  .ag-hero__eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:.78rem;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--ag-gold)}
  .ag-hero__eyebrow::before,.ag-hero__eyebrow::after{content:"";width:28px;height:1.5px;background:var(--ag-gold)}
  .ag-hero__title{position:absolute;z-index:1;left:0;right:0;top:calc(21% + var(--sp) * -60px);margin:0;text-align:center;font-weight:900;text-transform:uppercase;white-space:nowrap;letter-spacing:-.05em;line-height:.9;font-size:clamp(3.4rem,13.4vw,15.5rem);
    background:linear-gradient(180deg,#fff3cf 0%,#ffd479 28%,#f0b93e 52%,#a8741a 78%,#f0b93e 100%);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 0 40px rgba(240,185,62,.35))}
  .ag-hero__title span{display:block}
  .ag-hero__title .ag-l2{display:none}
  .ag-hero__stage{position:relative;z-index:3;margin:auto auto 0;width:min(36vw,470px);aspect-ratio:3/4;transform:translateY(calc(var(--sp) * 40px));align-self:center}
  .ag-hero__arch{position:absolute;inset:0;border-radius:999px 999px 0 0;border:1px solid rgba(240,185,62,.55);border-bottom:0;overflow:hidden;background:linear-gradient(180deg,rgba(240,185,62,.2),rgba(255,255,255,.03) 60%,rgba(0,0,0,.4));box-shadow:0 0 110px -10px rgba(240,185,62,.5),inset 0 0 70px rgba(240,185,62,.1)}
  .ag-hero__ph{position:absolute;inset:14px 14px 0;border:1.5px dashed rgba(240,185,62,.5);border-bottom:0;border-radius:999px 999px 0 0;display:grid;place-content:center;text-align:center;gap:6px;padding:10%;color:var(--ag-gold)}
  .ag-hero__ph svg{width:46px;height:46px;margin:0 auto;opacity:.9}
  .ag-hero__ph b{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase}
  .ag-hero__ph span{font-size:.78rem;color:var(--ag-muted);line-height:1.4}
  .ag-hero__photo{position:absolute;left:50%;bottom:0;height:104%;width:auto;max-width:none;transform:translateX(-50%);display:none}
  .ag-hero.ag-has-photo .ag-hero__photo{display:block}
  .ag-hero.ag-has-photo .ag-hero__ph{display:none}
  .ag-hero.ag-has-photo .ag-hero__arch{background:none;border:0;box-shadow:none;overflow:visible}
  .ag-hero__left{position:absolute;z-index:5;left:max(24px,calc((100vw - 1248px)/2));bottom:64px;max-width:min(300px,26vw)}
  .ag-hero__left h2{margin:0;font-weight:700;font-size:clamp(1.05rem,1vw + .7rem,1.5rem);line-height:1.3;letter-spacing:-.02em}
  .ag-hero__left p{margin:12px 0 0;font-size:.92rem;line-height:1.55;color:var(--ag-muted)}
  .ag-rot{display:inline-grid;vertical-align:bottom;color:var(--ag-gold);text-shadow:0 0 24px rgba(240,185,62,.45)}
  .ag-rot__w{grid-area:1/1;opacity:0;filter:blur(8px);transform:translateY(.4em);transition:opacity .55s ease,filter .55s ease,transform .55s cubic-bezier(.2,.7,.2,1);white-space:nowrap}
  .ag-rot__w.ag-on{opacity:1;filter:none;transform:none}
  .ag-rot__w.ag-off{opacity:0;filter:blur(8px);transform:translateY(-.4em)}
  .ag-hero__vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
  .ag-hero__right{position:absolute;z-index:5;right:max(24px,calc((100vw - 1248px)/2));bottom:64px;display:flex;flex-direction:column;align-items:flex-end;gap:12px}
  .ag-hero__pill{position:relative;display:inline-flex;align-items:center;gap:10px;padding:18px 32px;border-radius:999px;background:var(--ag-bg);color:var(--ag-text);font:800 .82rem/1 'Figtree',sans-serif;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;transition:transform .25s,background .25s,color .25s}
  .ag-hero__pill::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1.5px;background:linear-gradient(90deg,#f0b93e,#ffd479 50%,#f07a3e);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none}
  .ag-hero__pill:hover{background:var(--ag-gold);color:var(--ag-gold-ink);transform:translateY(-2px)}
  .ag-hero__pill svg{width:16px;height:16px}
  .ag-hero__link{color:var(--ag-muted);font-size:.84rem;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.25)}
  .ag-hero__link:hover{color:var(--ag-gold);border-color:var(--ag-gold)}
  .ag-hero__note{font-size:.8rem;color:var(--ag-muted);text-align:right;max-width:24ch}
  .ag-hero__props{display:none}
  .ag-hero.ag-nogl .ag-hero__props{display:block;position:absolute;inset:0;pointer-events:none;z-index:4}
  .ag-hero__prop{position:absolute;width:var(--s,10%);left:var(--x);top:var(--y)}
  .ag-hero__prop img{display:block;width:100%;filter:drop-shadow(0 18px 18px rgba(0,0,0,.55));animation:ag-hero-float var(--t,6s) ease-in-out infinite;animation-delay:var(--o,0s)}
  @keyframes ag-hero-float{0%,100%{transform:translateY(0) rotate(-6deg)}50%{transform:translateY(-14px) rotate(6deg)}}
  @media (max-width:900px){
    .ag-hero{padding:96px 20px 0;min-height:max(100svh,700px)}
    .ag-hero__title{top:calc(20% + var(--sp) * -40px);font-size:24vw;line-height:.86}
    .ag-hero__eyebrow{font-size:.62rem;letter-spacing:.12em}.ag-hero__eyebrow::before,.ag-hero__eyebrow::after{width:14px}
    .ag-hero__title .ag-l1{display:none}
    .ag-hero__title .ag-l2{display:block}
    .ag-hero__title{white-space:normal}
    .ag-hero__stage{width:min(72vw,360px);margin-bottom:0}
    .ag-hero__left{position:relative;left:auto;bottom:auto;max-width:none;z-index:5;order:3;margin:0;padding:22px 0 8px;background:linear-gradient(0deg,var(--ag-bg) 70%,transparent)}
    .ag-hero__right{position:relative;right:auto;bottom:auto;align-items:flex-start;order:4;padding:0 0 36px}
    .ag-hero__note{text-align:left;max-width:none}
    .ag-hero__stage{order:2}
    .ag-hero__bar{order:1}
  }
  @media (prefers-reduced-motion:reduce){.ag-hero [data-i]{animation:none;opacity:1;filter:none;transform:none}.ag-hero__prop img{animation:none!important}.ag-rot__w{transition:none}}
</style>
'''
arrow='<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10h12M11 5l5 5-5 5"/></svg>'
html=f'''
<section class="ag-hero" id="ag-hero" aria-label="Introduction">
  <div class="ag-hero__glow"></div>
  <canvas class="ag-hero__canvas" id="ag-hero-canvas" aria-hidden="true"></canvas>
  <div class="ag-hero__bar" data-i style="--d:0"><span class="ag-hero__eyebrow">Beyond Beautiful. Built to Perform.</span></div>
  <h1 class="ag-hero__title" data-i style="--d:1" aria-label="Hi, I'm Azeez"><span class="ag-l1" aria-hidden="true">Hi, I'm Azeez</span><span class="ag-l2" aria-hidden="true">Hi, I'm</span><span class="ag-l2" aria-hidden="true">Azeez</span></h1>
  <div class="ag-hero__stage" id="ag-hero-stage" data-i style="--d:2">
    <div class="ag-hero__arch">
      <div class="ag-hero__ph"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="24" cy="18" r="8"/><path d="M8 42c2-9 8-14 16-14s14 5 16 14"/></svg><b>Portrait placeholder</b><span>Add a transparent PNG of yourself (PHOTO_URL)</span></div>
      <img class="ag-hero__photo" id="ag-hero-photo" alt="Azeez Gazalle">
    </div>
  </div>
  <div class="ag-hero__left" data-i style="--d:3">
    <h2><span class="ag-hero__vh">I design and build websites, landing pages, sales funnels, web apps and redesigns.</span><span aria-hidden="true">I design and build<br><span class="ag-rot" id="ag-rot"><span class="ag-rot__w ag-on">websites</span><span class="ag-rot__w">landing pages</span><span class="ag-rot__w">sales funnels</span><span class="ag-rot__w">web apps</span><span class="ag-rot__w">redesigns</span></span></span></h2>
    <p>Web designer and developer for businesses in Nigeria and abroad.</p>
  </div>
  <div class="ag-hero__right" data-i style="--d:4">
    <a class="ag-hero__pill" data-ag-link="start" href="/start">Start a project {arrow}</a>
    <a class="ag-hero__link" data-ag-link="work" href="/work">View my work</a>
    <span class="ag-hero__note">Free 20-minute call. Replies within 24 business hours.</span>
  </div>
  <div class="ag-hero__props">
      </div>
</section>

'''
new_sprites='''
  var SPRITES=[
    /* emoji, rx, ry (relative to the portrait, rx +-1 = its edge), z depth, size, speed, phase */
    ['Woman technologist|woman_technologist@Medium-Dark',-1.85,.5,2.2,2.1,.9,0],
    ['Rocket|rocket',1.95,.62,2.6,2.0,1.1,1.3],
    ['Woman artist|woman_artist@Medium-Dark',-1.2,-.05,1.4,1.5,1.0,.6],
    ['Light bulb|light_bulb',1.3,.0,1.2,1.35,.8,2.1],
    ['Sparkles|sparkles',.1,1.1,.8,1.0,1.3,5.1],
    ['Laptop|laptop',2.75,.28,-1.8,1.25,.6,2.8]
  ];
'''
js=re.sub(r"  var SPRITES=\[.*?\n  \];\n",lambda m:new_sprites,js,flags=re.S)
js=js.replace("sc=Math.max(.3,(sr.width/520)*(96.6*visW/W)); mobile=W<700; spx=mobile?1.12:1.05; spy=mobile?.72:1.05; if(mobile)sc*=.7;",
 "mobile=W<900; sc=Math.max(.3,(sr.width/(mobile?400:520))*(96.6*visW/W)*(mobile?.55:1)); spx=mobile?.6:1.0; spy=mobile?.9:1.0;")
js=js.replace("mobile=window.innerWidth<700, list=mobile?SPRITES.slice(0,4):SPRITES","mobile=window.innerWidth<900, list=mobile?SPRITES.slice(0,4):SPRITES")
# scroll progress var for CSS parallax
js=js.replace("scrollP=Math.max(0,Math.min(1,-r.top/Math.max(1,r.height)));needRender=true;","scrollP=Math.max(0,Math.min(1,-r.top/Math.max(1,r.height)));root.style.setProperty('--sp',scrollP.toFixed(3));needRender=true;")
js=js.replace("var LINKS={ contact:'/contact', start:'/start', work:'/work' };","var LINKS={ contact:'/contact', start:'/start', work:'/work' };")
open(p,'w').write(head+css+html+js)
