# Generates the v6 sections. Every output file is fully self-contained (one GHL custom code block each).
import os, re, json
OUT='/home/claude/azeez-portfolio/sections'
FONT='''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,500&display=swap" rel="stylesheet">
'''
LINKS="{ home:'/', work:'/work', project:'/work/project', services:'/services', process:'/process', about:'/about', contact:'/contact', start:'/start' }"
ARROW='<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10h12M11 5l5 5-5 5"/></svg>'

BASE_CSS='''
.__P__{--ag-bg:#07070a;--ag-surface:#15151b;--ag-surface-2:#1d1d25;--ag-line:rgba(255,255,255,.10);--ag-text:#f8f3e9;--ag-muted:#b9b1a1;--ag-gold:#f0b93e;--ag-gold-hi:#ffd479;--ag-gold-ink:#1a1204;
  position:relative;background:var(--ag-bg);color:var(--ag-text);font-family:'Figtree',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;padding:104px 24px;box-sizing:border-box;overflow-x:clip;--ag-gold-t:var(--ag-gold);--ag-line-2:rgba(255,255,255,.18);--ag-ghost:rgba(255,255,255,.05);--ag-stroke:rgba(248,243,233,.6);--ag-fillc:#f8f3e9;--ag-card:#0b0b0f;--ag-bd-hi:rgba(255,255,255,.28);--ag-bd-soft:rgba(255,255,255,.14);--ag-bg-alt:#0e0e13}
.__P__ *,.__P__ *::before,.__P__ *::after{box-sizing:border-box}
.__P__ .ag-wrap{max-width:1248px;margin:0 auto;position:relative;z-index:1}
.__P__ .ag-head{max-width:760px;margin:0 0 52px}
.__P__ .ag-eye{display:inline-flex;align-items:center;gap:10px;font-size:.8rem;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ .ag-eye::before{content:"";width:34px;height:1.5px;background:var(--ag-gold-t)}
.__P__ .ag-h2{margin:18px 0 0;font-weight:800;letter-spacing:-.03em;line-height:1.08;font-size:clamp(1.8rem,2.1vw + 1rem,3.05rem)}
.__P__ .ag-h2 em{font-style:normal;color:var(--ag-gold-t)}
.__P__ .ag-lead{margin:16px 0 0;font-size:clamp(1rem,.3vw + .95rem,1.18rem);line-height:1.65;color:var(--ag-muted);max-width:58ch}
.__P__ .ag-btn{display:inline-flex;align-items:center;gap:10px;padding:15px 26px;border-radius:999px;font:700 1rem/1 'Figtree',sans-serif;text-decoration:none;cursor:pointer;border:1px solid transparent;transition:transform .25s,background .25s,border-color .25s,box-shadow .25s}
.__P__ .ag-btn svg{width:18px;height:18px;transition:transform .25s}
.__P__ .ag-btn:hover svg{transform:translateX(4px)}
.__P__ .ag-btn--gold{background:var(--ag-gold);color:var(--ag-gold-ink);box-shadow:0 14px 38px -12px rgba(240,185,62,.7)}
.__P__ .ag-btn--gold:hover{background:var(--ag-gold-hi);transform:translateY(-2px)}
.__P__ .ag-btn--ghost{background:var(--ag-ghost);border-color:var(--ag-line-2);color:var(--ag-text)}
.__P__ .ag-btn--ghost:hover{border-color:var(--ag-gold);transform:translateY(-2px)}
.__P__ a:focus-visible,.__P__ button:focus-visible{outline:2px solid var(--ag-gold-hi);outline-offset:3px;border-radius:6px}
.__P__ .ag-glow{position:absolute;z-index:0;pointer-events:none;border-radius:50%;background:radial-gradient(closest-side,rgba(240,185,62,.22),rgba(240,185,62,.07) 55%,transparent 74%)}
.__P__ .ag-ph{display:grid;place-content:center;text-align:center;gap:6px;color:var(--ag-gold-t);background:repeating-linear-gradient(135deg,rgba(240,185,62,.07) 0 12px,rgba(240,185,62,.02) 12px 24px);border:1.5px dashed rgba(240,185,62,.5)}
.__P__ .ag-ph b{font-size:.74rem;letter-spacing:.14em;text-transform:uppercase}
.__P__ .ag-ph span{font-size:.78rem;color:var(--ag-muted)}
.__P__[data-pre] [data-r]{opacity:0;filter:blur(8px);transform:translateY(24px)}
.__P__ [data-r]{transition:opacity .85s cubic-bezier(.2,.7,.2,1),filter .85s cubic-bezier(.2,.7,.2,1),transform .85s cubic-bezier(.2,.7,.2,1);transition-delay:calc(var(--i,0) * 80ms)}
.__P__[data-pre] [data-r].ag-in{opacity:1;filter:none;transform:none}

.__P__.ag-light{--ag-bg:#f4efe3;--ag-surface:#fffdf8;--ag-surface-2:#ebe4d3;--ag-line:rgba(10,10,12,.14);--ag-line-2:rgba(10,10,12,.34);--ag-ghost:rgba(10,10,12,.04);--ag-text:#0b0b0e;--ag-muted:#5a5446;--ag-gold-t:#7a4f00;--ag-stroke:rgba(11,11,14,.6);--ag-fillc:#0b0b0e;--ag-card:#fffdf8;--ag-bd-hi:rgba(10,10,12,.3);--ag-bd-soft:rgba(10,10,12,.16);--ag-bg-alt:#ebe4d3}
html[data-ag-theme="light"] .__P__:not(.ag-light):not(.ag-nf){--ag-bg:#f4efe3;--ag-surface:#fffdf8;--ag-surface-2:#ebe4d3;--ag-line:rgba(10,10,12,.14);--ag-line-2:rgba(10,10,12,.34);--ag-ghost:rgba(10,10,12,.04);--ag-text:#0b0b0e;--ag-muted:#5a5446;--ag-gold-t:#7a4f00;--ag-stroke:rgba(11,11,14,.6);--ag-fillc:#0b0b0e;--ag-card:#fffdf8;--ag-bd-hi:rgba(10,10,12,.3);--ag-bd-soft:rgba(10,10,12,.16);--ag-bg-alt:#ebe4d3}
html[data-ag-theme="light"] .__P__.ag-light:not(.ag-nf){--ag-bg:#07070a;--ag-surface:#15151b;--ag-surface-2:#1d1d25;--ag-line:rgba(255,255,255,.10);--ag-line-2:rgba(255,255,255,.18);--ag-ghost:rgba(255,255,255,.05);--ag-text:#f8f3e9;--ag-muted:#b9b1a1;--ag-gold-t:#f0b93e;--ag-stroke:rgba(248,243,233,.6);--ag-fillc:#f8f3e9;--ag-card:#0b0b0f;--ag-bd-hi:rgba(255,255,255,.28);--ag-bd-soft:rgba(255,255,255,.14);--ag-bg-alt:#0e0e13}
html[data-ag-theme="light"] .__P__:not(.ag-light):not(.ag-nf) .ag-pill::before{background:linear-gradient(90deg,#7a4f00,#a56f10)}
html[data-ag-theme="light"] .__P__:not(.ag-light):not(.ag-nf) .ag-pill.ag-solid{background:#0b0b0e;color:#f8f3e9}
html[data-ag-theme="light"] .__P__:not(.ag-light):not(.ag-nf) .ag-pill.ag-solid::before{background:transparent}
html[data-ag-theme="light"] .__P__.ag-light:not(.ag-nf) .ag-pill::before{background:linear-gradient(90deg,#f0b93e,#ffd479 50%,#d99a1f)}
html[data-ag-theme="light"] .__P__.ag-light:not(.ag-nf) .ag-pill.ag-solid{background:#f8f3e9;color:#07070a}
.__P__.ag-sheet{border-radius:44px 44px 0 0;margin-top:-44px;z-index:2;padding-top:148px;box-shadow:0 -24px 60px -30px rgba(0,0,0,.7)}
.__P__ .ag-big{margin:0;font-weight:900;text-transform:uppercase;letter-spacing:-.045em;line-height:.9;font-size:clamp(3rem,11vw,10.5rem);color:transparent;-webkit-text-stroke:2px var(--ag-stroke);padding:0 .02em .06em;
  background:linear-gradient(90deg,var(--ag-fillc) var(--p,100%),transparent calc(var(--p,100%) + .01%));-webkit-background-clip:text;background-clip:text}
.__P__ .ag-big--md{font-size:clamp(2.4rem,6.6vw,6.4rem)}
.__P__ .ag-pill{position:relative;display:inline-flex;align-items:center;gap:10px;padding:16px 30px;border-radius:999px;background:var(--ag-bg);color:var(--ag-text);font:800 .82rem/1 'Figtree',sans-serif;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;cursor:pointer;border:0;transition:transform .25s,background .25s,color .25s}
.__P__ .ag-pill::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1.5px;background:linear-gradient(90deg,#f0b93e,#ffd479 50%,#f07a3e);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none}
.__P__.ag-light .ag-pill::before{background:linear-gradient(90deg,#7a4f00,#a56f10)}
.__P__.ag-light .ag-pill.ag-solid::before{background:transparent}
.__P__ .ag-pill:hover{background:var(--ag-gold);color:var(--ag-gold-ink);transform:translateY(-2px)}
.__P__ .ag-pill svg{width:16px;height:16px}
.__P__ .ag-prop{position:absolute;z-index:1;pointer-events:none;width:var(--w,10vw);max-width:200px;min-width:54px;left:var(--x);top:var(--y);will-change:transform}
.__P__ .ag-prop img{display:block;width:100%;filter:drop-shadow(0 22px 20px rgba(0,0,0,.45));animation:ag-prop-f var(--t,7s) ease-in-out infinite;animation-delay:var(--o,0s)}
@keyframes ag-prop-f{0%,100%{transform:translateY(0) rotate(var(--r0,-8deg))}50%{transform:translateY(-16px) rotate(var(--r1,8deg))}}
.__P__ .ag-wj span{opacity:.45;transition:opacity .35s}
.__P__ .ag-wj span.ag-won{opacity:1}
@media (max-width:760px){.__P__.ag-sheet{border-radius:30px 30px 0 0;margin-top:-30px;padding-top:112px}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-prop img{animation:none}.__P__ .ag-wj span{opacity:1;transition:none}}
@media (max-width:760px){.__P__{padding:72px 20px}.__P__ .ag-head{margin-bottom:36px}}
@media (prefers-reduced-motion:reduce){.__P__[data-pre] [data-r]{opacity:1;filter:none;transform:none}.__P__ [data-r]{transition:none}}
'''

JS_HEAD='''
<script>
(function(){
  var root=document.getElementById('__P__'); if(!root||root.getAttribute('data-ag-init')) return; root.setAttribute('data-ag-init','1');
  var LINKS=__LINKS__;
  var BASE='https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@main/assets/';
  function emUrl(spec){var p=spec.split('|');if(window.AGE&&window.AGE[p[0]])return window.AGE[p[0]];var f=p[1],t='';if(f.indexOf('@')>-1){var q=f.split('@');f=q[0];t=q[1];}return BASE+encodeURIComponent(p[0])+(t?'/'+t:'')+'/3D/'+f+'_3d'+(t?'_'+t.toLowerCase():'')+'.png';}
  function em(scope){var im=(scope||root).querySelectorAll('img[data-em]');for(var i=0;i<im.length;i++){if(im[i].getAttribute('src'))continue;im[i].onerror=function(){this.style.visibility='hidden'};im[i].src=emUrl(im[i].getAttribute('data-em'));}}
  function links(scope){var a=(scope||root).querySelectorAll('[data-ag-link]');for(var j=0;j<a.length;j++){var k=a[j].getAttribute('data-ag-link');if(LINKS[k])a[j].setAttribute('href',LINKS[k]);}}
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine=window.matchMedia&&window.matchMedia('(pointer:fine)').matches;
  var io=null;
  function reveal(scope){
    var els=(scope||root).querySelectorAll('[data-r]:not(.ag-in)');
    if(!('IntersectionObserver' in window)||reduce){for(var i=0;i<els.length;i++)els[i].classList.add('ag-in');return;}
    if(!io){root.setAttribute('data-pre','');io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('ag-in');io.unobserve(e.target);}});},{threshold:.1,rootMargin:'0px 0px -5% 0px'});
      setTimeout(function(){var all=root.querySelectorAll('[data-r]');for(var i=0;i<all.length;i++)all[i].classList.add('ag-in');},7000);}
    for(var j=0;j<els.length;j++)io.observe(els[j]);
  }

  var frames=[],ticking=false;
  function onFrame(fn){frames.push(fn);fn();}
  function runFrames(){ticking=false;for(var i=0;i<frames.length;i++)frames[i]();}
  window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(runFrames);}},{passive:true});
  window.addEventListener('resize',function(){requestAnimationFrame(runFrames);});
  function clamp(v){return Math.max(0,Math.min(1,v));}
  /* big titles that fill in as you scroll (or on load) */
  function fills(){var ts=root.querySelectorAll('[data-fill]');if(reduce)return;
    ts.forEach(function(t){
      if(t.getAttribute('data-fill')==='load'){var st=null;t.style.setProperty('--p','0%');(function step(n){if(st===null)st=n;var k=clamp((n-st-250)/1300);t.style.setProperty('--p',(k*100).toFixed(1)+'%');if(k<1)requestAnimationFrame(step);})(performance.now());return;}
      onFrame(function(){var r=t.getBoundingClientRect(),vh=window.innerHeight;t.style.setProperty('--p',(clamp((vh*.9-r.top)/(vh*.5))*100).toFixed(1)+'%');});});}
  /* paragraphs whose words light up as you scroll */
  function words(){var ps=root.querySelectorAll('[data-words]');if(reduce)return;
    ps.forEach(function(p){var txt=p.textContent.trim().split(/\\s+/);p.innerHTML=txt.map(function(w){return '<span>'+w+'</span>';}).join(' ');p.className+=' ag-wj';var sp=p.querySelectorAll('span');
      onFrame(function(){var r=p.getBoundingClientRect(),vh=window.innerHeight;var k=clamp((vh*.85-r.top)/(vh*.55+r.height*.4));var n=Math.round(k*sp.length);for(var i=0;i<sp.length;i++){if(i<n)sp[i].classList.add('ag-won');else sp[i].classList.remove('ag-won');}});});}
  /* floating props with scroll parallax */
  function props(){var ps=root.querySelectorAll('[data-par]');if(reduce)return;
    ps.forEach(function(p){var d=parseFloat(p.getAttribute('data-par'))||1;onFrame(function(){var r=p.parentNode.getBoundingClientRect(),vh=window.innerHeight;var m=(r.top+r.height/2-vh/2);p.style.transform='translate3d(0,'+(-m*.08*d).toFixed(1)+'px,0)';});});}
  function tilt(scope){
    if(!fine||reduce)return;
    var cs=(scope||root).querySelectorAll('[data-tilt]:not([data-tilt-on])');
    for(var i=0;i<cs.length;i++)(function(c){c.setAttribute('data-tilt-on','1');
      var amt=parseFloat(c.getAttribute('data-tilt'))||8;
      c.addEventListener('mousemove',function(e){var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform='perspective(1000px) rotateY('+(x*amt).toFixed(2)+'deg) rotateX('+(-y*amt).toFixed(2)+'deg) translateY(-4px)';});
      c.addEventListener('mouseleave',function(){c.style.transform='';});})(cs[i]);
  }
'''
JS_TAIL='''
  em(); links(); reveal(); tilt(); fills(); words(); props();
})();
</script>
'''

ALT=set(['faq','about-story','work-showcase','services-terms'])
LIGHT=set(['services-list','process-steps','home-services','home-process','home-cta'])
NOFLIP=set(['logo-marquee'])
NOSHEET=set(['logo-marquee','page-hero-work','page-hero-services','page-hero-process','page-hero-about','contact-section','home-hero'])

def sec(name, p, css, html, js='', comment=''):
    s=f'<!-- ========== AG SECTION: {name} {comment}==========\n     Paste into its own GHL Custom Code block. -->\n'+FONT
    s+='<style>'+(BASE_CSS+css).replace('__P__',p)+'</style>\n'
    cls='__P__'+('' if name in NOSHEET else ' ag-sheet')+(' ag-light' if name in LIGHT else '')+(' ag-nf' if name in NOFLIP else '')
    if name in ALT: s+='<style>#'+p+'{--ag-bg:#0e0e13}html[data-ag-theme="light"] #'+p+'{--ag-bg:#ebe4d3}</style>\n'
    s+=html.replace('class="__P__"','class="'+cls+'"').replace('__P__',p)
    s+=(JS_HEAD+js+JS_TAIL).replace('__P__',p).replace('__LINKS__',LINKS)
    s=s.replace('__ABOUT__',__import__('json').load(open('/home/claude/azeez-portfolio/tools/photos.json'))['about'])
    open(os.path.join(OUT,name+'.html'),'w').write(s)

def emimg(spec,cls='',style=''):
    return f'<img {"class=%s " % chr(34)+cls+chr(34) if cls else ""}data-em="{spec}" alt="" {("style=%s" % chr(34)+style+chr(34)) if style else ""}>'

# ============ SHARED DATA ============

SERVICES=[
 ('Landing Page Design & Development','from $250','','Bullseye|bullseye','One focused page built to turn a visit into an enquiry, sale or booking.',
  ['One custom landing page, fully responsive','6 to 8 sections planned around one clear goal','Call-to-action and form integration','Basic SEO setup and agreed tracking'],'Single offers, campaigns and lead capture.','5 to 10 business days'),
 ('Business Website Design & Development','from $600','','Desktop computer|desktop_computer','A credible, fast website that explains what you do and makes it easy to contact you.',
  ['Up to five pages, designed and built to fit your brand','Contact integration and basic SEO','Analytics setup','Deployment and launch'],'Companies that need a professional online presence.','2 to 3 weeks'),
 ('Sales Funnel Design & Development','from $750','','Rocket|rocket','A scoped funnel that moves visitors from first click to lead or customer.',
  ['Sales or lead-generation page plus thank-you page','Form integration and basic CRM integration','One basic automation workflow','Standard conversion tracking','GoHighLevel implementation where it fits'],'Businesses ready to capture and follow up leads properly.','2 to 4 weeks'),
 ('Custom Web Application Development','from $2,000','subject to scope','Gear|gear','A custom build for a clearly defined MVP, quoted per project.',
  ['Scoped around your required features','Authentication and database where needed','Integrations and security requirements reviewed','Milestone-based payments'],'Products and internal tools with a defined first version.','4 to 10+ weeks'),
 ('Website Redesign','from $400','','Artist palette|artist_palette','A clearer, faster, better-looking version of a website you already have.',
  ['Review of your current website and goals','New structure, layout and visual design','Responsive rebuild','Final price set by pages, condition and functionality'],'Sites that look dated or are not converting visitors.','Confirmed in your proposal'),
 ('Website Maintenance','from $75','per month','Hammer and wrench|hammer_and_wrench','Routine care so your website stays secure, current and working.',
  ['Routine website checks and supported updates','Backups and recovery checks where applicable','Minor content updates within an agreed allowance','Basic troubleshooting and technical support'],'Owners who want a dependable person looking after the site.','Billed monthly in advance'),
]
STEPS=[
 ('Discovery','1 to 2 business days','We talk through your business, goals, audience, required features, budget and timeline, so the scope is defined before anything is built.','Speech balloon|speech_balloon'),
 ('Strategy and structure','1 to 3 business days','You receive a tailored proposal. Once it is approved, I plan the page structure and user journey around what the site needs to achieve.','Compass|compass'),
 ('Design','3 to 7 business days','I design the visual direction and layouts. You review and give feedback before any development starts.','Artist palette|artist_palette'),
 ('Development','3 to 15+ business days','The approved design becomes responsive pages, forms, integrations and the features included in the agreed scope.','Laptop|laptop'),
 ('Testing and launch','2 to 5 business days','I test across screen sizes, check forms and integrations, and fix issues within scope. Then I configure the launch and connect your domain where applicable.','Rocket|rocket'),
 ('Handover and support','1 to 2 business days','You get the access details and guidance for what the project covers, plus 14 days of post-launch support for in-scope bugs.','Handshake|handshake'),
]
TOOLS=[('HTML5','html5'),('CSS3','css3'),('JavaScript','javascript'),('React','react'),('Supabase','supabase'),('Vercel','vercel'),('Figma','figma'),('GitHub','github'),('Firebase','firebase'),('WordPress','wordpress')]

# ============ LOGO MARQUEE ============

def tile(t):
    n,slug=t
    return f'<span class="ag-tl" title="{n}"><img{' class="ag-inv"' if slug in ('vercel','github') else ''} loading="lazy" alt="{n}" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons/{slug}/{slug}-original.svg"></span>'
def tile_make(): return '<span class="ag-tl" title="Make"><span class="ag-mk" role="img" aria-label="Make"></span></span>'
def tile_ghl(): return '<span class="ag-tl ag-tl--word" title="GoHighLevel"><b>GoHighLevel</b></span>'
items=[tile(TOOLS[0]),tile(TOOLS[1]),tile(TOOLS[2]),tile(TOOLS[3]),tile_ghl(),tile(TOOLS[4]),tile(TOOLS[8]),tile(TOOLS[5]),tile_make(),tile(TOOLS[9]),tile(TOOLS[6]),tile(TOOLS[7])]
track=''.join(items)
sec('logo-marquee','ag-logos','''
.__P__{padding:34px 0;border-top:1px solid var(--ag-line);border-bottom:1px solid var(--ag-line);background:#0a0a0d}
.__P__ .ag-lbl{margin:0 0 20px;text-align:center;font-size:.8rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ .ag-row{overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 9%,#000 91%,transparent);mask-image:linear-gradient(90deg,transparent,#000 9%,#000 91%,transparent)}
.__P__ .ag-track{display:flex;gap:16px;width:max-content;animation:ag-logos-run 44s linear infinite}
.__P__ .ag-row:hover .ag-track{animation-play-state:paused}
.__P__ .ag-tl{flex:none;display:grid;place-items:center;width:88px;height:88px;border-radius:22px;border:1px solid var(--ag-line);background:linear-gradient(160deg,#17171c,#0e0e12);transition:transform .3s,border-color .3s,box-shadow .3s}
.__P__ .ag-tl:hover{transform:translateY(-6px) scale(1.05);border-color:rgba(240,185,62,.6);box-shadow:0 18px 40px -16px rgba(240,185,62,.5)}
.__P__ .ag-tl img{width:44px;height:44px;display:block}
.__P__ .ag-tl img.ag-inv{filter:invert(1)}
.__P__ .ag-tl--word{width:auto;padding:0 26px}
.__P__ .ag-tl--word b{font-size:1.02rem;letter-spacing:-.01em;color:var(--ag-text)}
.__P__ .ag-mk{display:block;width:46px;height:46px;background:#a45cff;-webkit-mask:url(https://cdn.jsdelivr.net/npm/simple-icons@13.21.0/icons/make.svg) center/contain no-repeat;mask:url(https://cdn.jsdelivr.net/npm/simple-icons@13.21.0/icons/make.svg) center/contain no-repeat}
@keyframes ag-logos-run{to{transform:translateX(-50%)}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-track{animation:none;flex-wrap:wrap;justify-content:center;width:auto}}
@media (max-width:640px){.__P__ .ag-tl{width:72px;height:72px;border-radius:18px}.__P__ .ag-tl img{width:36px;height:36px}}
''',f'''
<section class="__P__" id="__P__" aria-label="Skills I build with">
  <p class="ag-lbl">Skills I build with</p>
  <div class="ag-row"><div class="ag-track">{track}{track}</div></div>
</section>
''','','(Home, under the hero) ')

# ============ SERVICES LIST (accordion) ============

def svc_row(i,s):
    name,price,note,e,desc,inc,best,tl=s
    li=''.join(f'<li>{x}</li>' for x in inc)
    op=' ag-open' if i==0 else ''
    return f'''<div class="ag-sv{op}" data-r style="--i:{i}">
  <button class="ag-sh" type="button" aria-expanded="{'true' if i==0 else 'false'}" aria-controls="ag-svc-p{i}" id="ag-svc-b{i}">
    <span class="ag-n">0{i+1}</span><span class="ag-nm">{name}</span>
    <span class="ag-pr"><b>{price}</b>{('<small>'+note+'</small>') if note else ''}</span><span class="ag-plus" aria-hidden="true"></span>
  </button>
  <div class="ag-sp" id="ag-svc-p{i}" role="region" aria-labelledby="ag-svc-b{i}"><div class="ag-spi">
    <div><p class="ag-sd">{desc}</p><h4>What is included</h4><ul>{li}</ul></div>
    <div class="ag-side"><img data-em="{e}" alt=""><h4>Best for</h4><p>{best}</p><h4>Typical timeline</h4><p>{tl}</p>
    <a class="ag-btn ag-btn--gold" data-ag-link="contact" href="/contact">{'Get a quote' if i in (3,5) else 'Discuss your project'} {ARROW}</a></div>
  </div></div></div>'''
rows=''.join(svc_row(i,s) for i,s in enumerate(SERVICES))
sec('services-list','ag-svc','''
.__P__ .ag-lst{border-top:1px solid var(--ag-line)}
.__P__ .ag-sv{border-bottom:1px solid var(--ag-line);transition:background .3s}
.__P__ .ag-sv.ag-open{background:linear-gradient(90deg,rgba(240,185,62,.07),transparent 80%)}
.__P__ .ag-sh{width:100%;display:grid;grid-template-columns:64px 1fr auto 44px;gap:22px;align-items:center;padding:32px 10px;background:none;border:0;color:inherit;text-align:left;cursor:pointer;font-family:inherit}
.__P__ .ag-n{font-weight:800;color:var(--ag-text);font-size:.95rem}
.__P__ .ag-nm{font-size:clamp(1.15rem,1.1vw + .9rem,1.8rem);font-weight:800;letter-spacing:-.02em;line-height:1.2}
.__P__ .ag-pr{text-align:right}
.__P__ .ag-pr b{display:block;font-size:clamp(1.15rem,.8vw + 1rem,1.55rem);font-weight:800;color:var(--ag-text);letter-spacing:-.02em}
.__P__ .ag-pr small{display:block;color:var(--ag-muted);font-size:.8rem;margin-top:2px}
.__P__ .ag-plus{position:relative;width:44px;height:44px;border-radius:50%;border:1px solid var(--ag-line);transition:background .3s,border-color .3s,transform .3s}
.__P__ .ag-plus::before,.__P__ .ag-plus::after{content:"";position:absolute;left:50%;top:50%;width:16px;height:2px;margin:-1px 0 0 -8px;background:var(--ag-text);transition:transform .3s,background .3s}
.__P__ .ag-plus::after{transform:rotate(90deg)}
.__P__ .ag-sh:hover .ag-plus{border-color:var(--ag-gold-t)}
.__P__ .ag-open .ag-plus{background:var(--ag-gold);border-color:var(--ag-gold-t)}
.__P__ .ag-open .ag-plus::before,.__P__ .ag-open .ag-plus::after{background:var(--ag-gold-ink)}
.__P__ .ag-open .ag-plus::after{transform:rotate(0)}
.__P__ .ag-sp{display:grid;grid-template-rows:0fr;transition:grid-template-rows .5s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-open .ag-sp{grid-template-rows:1fr}
.__P__ .ag-spi{overflow:hidden;min-height:0;display:grid;grid-template-columns:1.3fr .7fr;gap:50px;padding:0 10px 0 86px}
.__P__ .ag-open .ag-spi{padding-bottom:42px}
.__P__ .ag-sd{margin:0 0 22px;font-size:1.12rem;line-height:1.65;color:var(--ag-text);max-width:54ch}
.__P__ h4{margin:0 0 10px;font-size:.74rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ ul{list-style:none;margin:0 0 6px;padding:0;display:grid;gap:12px}
.__P__ li{position:relative;padding-left:28px;line-height:1.5}
.__P__ li::before{content:"";position:absolute;left:0;top:.2em;width:18px;height:18px;border-radius:50%;background:rgba(240,185,62,.16) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M5 9.4l2.6 2.6L13 6.4' fill='none' stroke='%23f0b93e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/18px no-repeat}
.__P__ .ag-side{position:relative;padding:26px;border:1px solid var(--ag-line);border-radius:22px;background:var(--ag-surface)}
.__P__ .ag-side img{position:absolute;right:14px;top:-28px;width:72px;filter:drop-shadow(0 14px 12px rgba(0,0,0,.6))}
.__P__ .ag-side p{margin:0 0 18px;line-height:1.5}
.__P__ .ag-side .ag-btn{width:100%;justify-content:center;padding:14px 18px;font-size:.95rem}
.__P__ .ag-fine{margin:34px 0 0;color:var(--ag-muted);font-size:.92rem;line-height:1.65;max-width:78ch}
@media (max-width:900px){
  .__P__ .ag-sh{grid-template-columns:36px 1fr 40px;gap:12px;padding:24px 0}
  .__P__ .ag-pr{grid-column:2;grid-row:2;text-align:left}
  .__P__ .ag-plus{grid-column:3;grid-row:1/3;width:38px;height:38px}
  .__P__ .ag-spi{grid-template-columns:1fr;gap:34px;padding:0 0 0 0}
}
@media (prefers-reduced-motion:reduce){.__P__ .ag-sp{transition:none}}
''',f'''
<section class="__P__" id="__P__" aria-label="Services and starting prices">
  <div class="ag-wrap">
    <div class="ag-lst">{rows}</div>
    <p class="ag-fine" data-r>These are indicative starting prices, not fixed quotations. A tailored proposal confirms the final scope, cost and timeline. Hosting, domain registration, software subscriptions and third-party fees are paid separately unless included in your proposal. Maintenance excludes unlimited development, major redesigns and new features.</p>
  </div>
</section>
''','''
  var svs=root.querySelectorAll('.ag-sv');
  svs.forEach(function(sv){
    sv.querySelector('.ag-sh').addEventListener('click',function(){
      var open=sv.classList.contains('ag-open');
      svs.forEach(function(o){o.classList.remove('ag-open');o.querySelector('.ag-sh').setAttribute('aria-expanded','false');});
      if(!open){sv.classList.add('ag-open');sv.querySelector('.ag-sh').setAttribute('aria-expanded','true');}
    });
  });
''','(Services page) ')

# ============ SERVICES TERMS ============

sec('services-terms','ag-terms','''
.__P__{background:#0a0a0d;border-top:1px solid var(--ag-line)}
.__P__ .ag-cols{display:grid;grid-template-columns:1fr 1fr;gap:64px}
.__P__ h3{margin:0 0 24px;font-size:1.7rem;font-weight:800;letter-spacing:-.02em;display:flex;align-items:center;gap:14px}
.__P__ h3 img{width:48px;height:48px;filter:drop-shadow(0 10px 10px rgba(0,0,0,.5))}
.__P__ .ag-it{padding:20px 0;border-top:1px solid var(--ag-line)}
.__P__ .ag-it:last-child{border-bottom:1px solid var(--ag-line)}
.__P__ .ag-it b{display:block;font-size:1.05rem;margin-bottom:6px}
.__P__ .ag-it p{margin:0;color:var(--ag-muted);line-height:1.65;font-size:.98rem}
.__P__ .ag-it em{font-style:normal;color:var(--ag-gold-t);font-weight:700}
@media (max-width:900px){.__P__ .ag-cols{grid-template-columns:1fr;gap:56px}}
''','''
<section class="__P__" id="__P__" aria-label="Payment terms and after launch">
  <div class="ag-wrap">
    <div class="ag-cols">
      <div data-r>
        <h3><img data-em="Money bag|money_bag" alt="">Payment terms</h3>
        <div class="ag-it"><b>Standard projects: <em>50% / 50%</em></b><p>Landing pages, business websites and standard funnels. 50% upfront reserves your slot and starts the work. 50% is due before final launch or handover.</p></div>
        <div class="ag-it"><b>Web applications: milestones</b><p>Typically 40% upfront, 30% after the core design and development milestone is approved, and 30% before final deployment and handover. Confirmed in your proposal.</p></div>
        <div class="ag-it"><b>Monthly maintenance</b><p>Billed monthly in advance. Scope, service period and cancellation terms are set out in the service agreement.</p></div>
        <div class="ag-it"><b>Good to know</b><p>Work begins after the initial payment and receipt of required materials. Quotes are valid for 14 days. Work outside the agreed scope is quoted separately. Final terms are confirmed in your individual proposal.</p></div>
      </div>
      <div data-r style="--i:1">
        <h3><img data-em="Package|package" alt="">After launch</h3>
        <div class="ag-it"><b><em>14 days</em> of post-launch support</b><p>Covers bugs in the work I delivered, within the agreed scope. New features, redesigns and issues caused by third-party services are handled separately.</p></div>
        <div class="ag-it"><b>Two revision rounds included</b><p>Two rounds of revisions are included within the agreed scope, so feedback is organised and the project stays on schedule.</p></div>
        <div class="ag-it"><b>Hosting and domain</b><p>I deploy your site and connect your domain where the scope includes it. Domain registration, hosting subscriptions, premium software and third-party fees are paid separately unless agreed otherwise.</p></div>
        <div class="ag-it"><b>Handover and ongoing care</b><p>You receive access details and guidance for what the project covers. Monthly maintenance and further development can be added whenever you need them.</p></div>
      </div>
    </div>
  </div>
</section>
''','','(Services page) ')

# ============ PROCESS STEPS (vertical timeline) ============

ps=''.join(f'''<li class="ag-ps" data-r style="--i:0"><span class="ag-pn">0{i+1}</span>
  <div class="ag-pc"><img data-em="{s[3]}" alt=""><div><h3>{s[0]}</h3><span class="ag-tm">{s[1]}</span><p>{s[2]}</p></div></div></li>''' for i,s in enumerate(STEPS))
sec('process-steps','ag-pst','''
.__P__ ol{list-style:none;margin:0;padding:0;position:relative}
.__P__ ol::before,.__P__ ol::after{content:"";position:absolute;left:34px;top:20px;bottom:20px;width:2px;background:var(--ag-line)}
.__P__ ol::after{background:linear-gradient(180deg,var(--ag-gold),rgba(240,185,62,.5));height:calc((100% - 40px) * var(--prog,0));bottom:auto;box-shadow:0 0 16px rgba(240,185,62,.7)}
.__P__ .ag-ps{position:relative;display:grid;grid-template-columns:70px 1fr;gap:34px;padding:0 0 64px}
.__P__ .ag-ps:last-child{padding-bottom:0}
.__P__ .ag-pn{position:relative;z-index:1;width:70px;height:70px;border-radius:50%;display:grid;place-items:center;background:var(--ag-bg);border:1.5px solid rgba(240,185,62,.6);color:var(--ag-gold-t);font-weight:800;font-size:1.15rem}
.__P__ .ag-pc{display:flex;gap:26px;align-items:flex-start;padding:26px 30px;border:1px solid var(--ag-line);border-radius:24px;background:var(--ag-surface);transition:border-color .3s,transform .3s}
.__P__ .ag-ps:hover .ag-pc{border-color:rgba(240,185,62,.5);transform:translateX(6px)}
.__P__ .ag-pc img{width:84px;height:84px;flex:none;filter:drop-shadow(0 14px 12px rgba(0,0,0,.6))}
.__P__ h3{margin:0;font-size:clamp(1.3rem,1vw + 1rem,1.8rem);font-weight:800;letter-spacing:-.02em}
.__P__ .ag-tm{display:inline-block;margin-top:10px;padding:5px 12px;border-radius:999px;background:rgba(240,185,62,.13);color:var(--ag-text);font-size:.8rem;font-weight:700}
.__P__ .ag-pc p{margin:14px 0 0;color:var(--ag-muted);line-height:1.7;max-width:62ch}
.__P__ .ag-tt{margin-top:90px;display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:1px solid var(--ag-line);border-bottom:1px solid var(--ag-line)}
.__P__ .ag-tt div{padding:26px 22px 26px 0}
.__P__ .ag-tt b{display:block;font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ .ag-tt span{display:block;margin-top:8px;font-size:clamp(1.15rem,.8vw + 1rem,1.55rem);font-weight:800;letter-spacing:-.02em}
.__P__ .ag-fine{margin:22px 0 0;color:var(--ag-muted);font-size:.92rem;line-height:1.65;max-width:76ch}
@media (max-width:760px){
  .__P__ ol::before,.__P__ ol::after{left:21px}
  .__P__ .ag-ps{grid-template-columns:44px 1fr;gap:16px;padding-bottom:36px}
  .__P__ .ag-pn{width:44px;height:44px;font-size:.9rem}
  .__P__ .ag-pc{flex-direction:column;gap:14px;padding:22px}
  .__P__ .ag-pc img{width:64px;height:64px}
  .__P__ .ag-tt{grid-template-columns:1fr 1fr}
}
''',f'''
<section class="__P__" id="__P__" aria-label="Process">
  <div class="ag-wrap">
    <ol id="__P__-ol">{ps}</ol>
    <div class="ag-tt" data-r>
      <div><b>Landing page</b><span>5 to 10 business days</span></div>
      <div><b>Business website</b><span>2 to 3 weeks</span></div>
      <div><b>Sales funnel</b><span>2 to 4 weeks</span></div>
      <div><b>Web application MVP</b><span>4 to 10+ weeks</span></div>
    </div>
    <p class="ag-fine" data-r>Timelines begin once the project is approved, the first payment is received and the required materials are available. Your feedback and approvals keep the project on schedule. Complex functionality, extra integrations or changes to scope can extend delivery. Your exact timeline is confirmed in your proposal.</p>
  </div>
</section>
''','''
  var ol=document.getElementById('__P__-ol');
  function prog(){var r=ol.getBoundingClientRect(),vh=window.innerHeight;var p=(vh*.62-r.top)/Math.max(1,r.height);ol.style.setProperty('--prog',Math.max(0,Math.min(1,p)).toFixed(3));}
  prog();window.addEventListener('scroll',prog,{passive:true});window.addEventListener('resize',prog);
'''.replace('__P__','ag-pst'),'(Process page) ')

# ============ WHY ME ============

WHY=[('Design and development, together','I design the layout and build it myself, so what you approve is what ships, with no hand-off gap.','Artist palette|artist_palette'),
('Business objectives first','Every page starts with what it needs to achieve for your business, then the design follows.','Bullseye|bullseye'),
('Attention to user experience','Clear structure, readable type, quick pages and layouts that work on a phone.','Mobile phone|mobile_phone'),
('Structured communication','You know the scope, the stage, the next step and the timeline throughout.','Speech balloon|speech_balloon'),
('Conversion-conscious thinking','Clear calls to action, sensible forms and tracking set up around the action that matters.','Chart increasing|chart_increasing'),
('Clean implementation','Tidy, maintainable code and sensible integrations, so the site is easy to extend later.','Gear|gear'),
('Professional handover','Access details, guidance and 14 days of support, so you are never left guessing.','Handshake|handshake')]
w=''.join(f'<div class="ag-w" data-r style="--i:{i%3}"><span class="ag-wn">0{i+1}</span><img data-em="{e}" alt=""><h3>{t}</h3><p>{d}</p></div>' for i,(t,d,e) in enumerate(WHY))
sec('why-me','ag-why','''
.__P__{background:#0a0a0d;border-top:1px solid var(--ag-line)}
.__P__ .ag-g{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--ag-line);border-left:1px solid var(--ag-line)}
.__P__ .ag-w{position:relative;padding:34px 30px 38px;border-right:1px solid var(--ag-line);border-bottom:1px solid var(--ag-line);transition:background .3s}
.__P__ .ag-w:hover{background:linear-gradient(160deg,rgba(240,185,62,.1),transparent 70%)}
.__P__ .ag-wn{font-weight:800;color:var(--ag-text);font-size:.9rem}
.__P__ .ag-w img{display:block;width:64px;height:64px;margin:14px 0 18px;filter:drop-shadow(0 12px 10px rgba(0,0,0,.6));transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-w:hover img{transform:translateY(-6px) rotate(-6deg)}
.__P__ h3{margin:0;font-size:1.25rem;font-weight:800;letter-spacing:-.02em;line-height:1.25}
.__P__ .ag-w p{margin:10px 0 0;color:var(--ag-muted);line-height:1.65;font-size:.98rem}
@media (max-width:980px){.__P__ .ag-g{grid-template-columns:1fr 1fr}}
@media (max-width:620px){.__P__ .ag-g{grid-template-columns:1fr}}
''',f'''
<section class="__P__" id="__P__" aria-label="Why work with me">
  <div class="ag-wrap">
    <div class="ag-head"><div class="ag-eye" data-r>Why work with me</div><h2 class="ag-h2" data-r style="--i:1">Working principles you can <em>hold me to</em>.</h2><p class="ag-lead" data-r style="--i:2">No grand claims. This is how I work on every project.</p></div>
    <div class="ag-g">{w}</div>
  </div>
</section>
''','','(Process page) ')

# ============ FAQ ============

FAQ=[('How long does a project take?','Typically 5 to 10 business days for a landing page, 2 to 3 weeks for a business website, 2 to 4 weeks for a sales funnel and 4 to 10+ weeks for a web application MVP. Timelines start once the proposal is approved, the first payment is in and I have your materials. Your proposal confirms the exact timeline.'),
('How does payment work?','Standard projects are 50% upfront and 50% before final launch or handover. Web applications use milestones, typically 40%, 30% and 30%. Maintenance is billed monthly in advance. Final terms are confirmed in your individual proposal.'),
('How many revisions are included?','Two revision rounds are included within the agreed scope. Work outside that scope is quoted separately.'),
('Who pays for hosting and domains?','Hosting, domain registration and third-party subscriptions are billed separately unless we agree otherwise. I can deploy the site and connect your domain where it is part of the project scope.'),
('Do you offer maintenance?','Yes. Monthly maintenance starts from $75 per month and can include routine checks, supported updates, backups where applicable, minor content changes and basic technical support. The final price depends on your platform and the level of support.'),
('Can you work with international clients?','Yes. I work remotely with clients in Nigeria and internationally. We communicate by email, WhatsApp and video call, and your proposal sets out the payment details.'),
('What support do I get after launch?','Fourteen days of post-launch support covering bugs in the work I delivered, within the agreed scope. After that, maintenance or further development can be added whenever you need it.')]
fq=''.join(f'''<div class="ag-q" data-r style="--i:{i%3}"><button type="button" class="ag-qb" aria-expanded="false" aria-controls="ag-faq-a{i}" id="ag-faq-b{i}"><span>{q}</span><i aria-hidden="true"></i></button><div class="ag-qa" id="ag-faq-a{i}" role="region" aria-labelledby="ag-faq-b{i}"><div><p>{a}</p></div></div></div>''' for i,(q,a) in enumerate(FAQ))
sec('faq','ag-faq','''
.__P__ .ag-cols{display:grid;grid-template-columns:.8fr 1.2fr;gap:70px;align-items:start}
.__P__ .ag-head{margin:0;position:sticky;top:120px}
.__P__ .ag-q{border-bottom:1px solid var(--ag-line)}
.__P__ .ag-q:first-child{border-top:1px solid var(--ag-line)}
.__P__ .ag-qb{width:100%;display:flex;justify-content:space-between;align-items:center;gap:20px;padding:26px 0;background:none;border:0;color:var(--ag-text);font:700 1.15rem/1.35 'Figtree',sans-serif;text-align:left;cursor:pointer;letter-spacing:-.01em}
.__P__ .ag-qb i{position:relative;flex:none;width:34px;height:34px;border-radius:50%;border:1px solid var(--ag-line);transition:background .3s,border-color .3s}
.__P__ .ag-qb i::before,.__P__ .ag-qb i::after{content:"";position:absolute;left:50%;top:50%;width:12px;height:2px;margin:-1px 0 0 -6px;background:var(--ag-text);transition:transform .3s,background .3s}
.__P__ .ag-qb i::after{transform:rotate(90deg)}
.__P__ .ag-qb:hover i{border-color:var(--ag-gold-t)}
.__P__ .ag-open .ag-qb i{background:var(--ag-gold);border-color:var(--ag-gold-t)}
.__P__ .ag-open .ag-qb i::before,.__P__ .ag-open .ag-qb i::after{background:var(--ag-gold-ink)}
.__P__ .ag-open .ag-qb i::after{transform:rotate(0)}
.__P__ .ag-qa{display:grid;grid-template-rows:0fr;transition:grid-template-rows .45s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-open .ag-qa{grid-template-rows:1fr}
.__P__ .ag-qa>div{overflow:hidden;min-height:0}
.__P__ .ag-qa p{margin:0 0 26px;color:var(--ag-muted);line-height:1.75;max-width:62ch}
@media (max-width:900px){.__P__ .ag-cols{grid-template-columns:1fr;gap:34px}.__P__ .ag-head{position:static}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-qa{transition:none}}
''',f'''
<section class="__P__" id="__P__" aria-label="Frequently asked questions">
  <div class="ag-wrap"><div class="ag-cols">
    <div class="ag-head"><div class="ag-eye" data-r>FAQ</div><h2 class="ag-h2" data-r style="--i:1">Practical <em>answers</em> before you ask.</h2><p class="ag-lead" data-r style="--i:2">Still unsure about something? Send a message and I'll answer within 24 business hours.</p></div>
    <div>{fq}</div>
  </div></div>
</section>
''','''
  var qs=root.querySelectorAll('.ag-q');
  qs.forEach(function(q){q.querySelector('.ag-qb').addEventListener('click',function(){
    var b=q.querySelector('.ag-qb'),o=q.classList.toggle('ag-open');b.setAttribute('aria-expanded',o?'true':'false');});});
''','(Process page) ')

# ============ ABOUT STORY ============

J=[('Graphic design','Where it began: visual communication and how design shapes perception.','Artist palette|artist_palette'),
('Python experiments','A calculator and a ping-pong game taught me programming logic.','Joystick|joystick'),
('Web development','Moving from single graphics to complete, working websites.','Laptop|laptop'),
('Figma','Designing interfaces properly before building them.','Pencil|pencil'),
('GoHighLevel','Funnels, CRM and automation working together.','Gear|gear'),
('Meta Ads','Around 3 to 4 years of campaign strategy and management.','Chart increasing|chart_increasing'),
('One practice','Design, development and advertising working as one.','Sparkles|sparkles')]
jn=''.join(f'<li class="ag-j" data-r style="--i:{i%3}"><img data-em="{e}" alt=""><span class="ag-jn">0{i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i,(t,d,e) in enumerate(J))
sec('about-story','ag-abt','''
.__P__ .ag-tt{display:grid;grid-template-columns:.85fr 1.15fr;gap:72px;align-items:center}
.__P__ .ag-fig{position:relative;max-width:440px;width:100%;margin:0 auto}
.__P__ .ag-arch{position:relative;aspect-ratio:3/4;border-radius:999px 999px 26px 26px;border:1px solid rgba(240,185,62,.55);overflow:hidden;box-shadow:0 0 110px -10px rgba(240,185,62,.45);background:linear-gradient(180deg,rgba(240,185,62,.14),rgba(0,0,0,.4))}
.__P__ .ag-arch .ag-ph{position:absolute;inset:14px;border-radius:999px 999px 12px 12px;padding:12%}
.__P__ .ag-arch img.ag-photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.__P__ .ag-fig>img{position:absolute;width:22%;filter:drop-shadow(0 18px 16px rgba(0,0,0,.6));animation:ag-ab-float 6s ease-in-out infinite}
.__P__ .ag-fig>img:nth-of-type(1){right:-9%;top:10%}.__P__ .ag-fig>img:nth-of-type(2){left:-9%;bottom:14%;width:18%;animation-delay:-3s}
@keyframes ag-ab-float{0%,100%{transform:translateY(0) rotate(-6deg)}50%{transform:translateY(-12px) rotate(6deg)}}
.__P__ .ag-prose p{margin:0 0 20px;font-size:1.12rem;line-height:1.8;color:var(--ag-muted);max-width:62ch}
.__P__ .ag-prose p:first-child{color:var(--ag-text);font-size:1.3rem;line-height:1.6}
.__P__ .ag-pls{margin-top:96px}
.__P__ .ag-pl{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:30px}
.__P__ .ag-pc{padding:30px 28px 28px;border-radius:24px;border:1px solid var(--ag-line);background:var(--ag-surface);transition:transform .3s,border-color .3s,box-shadow .3s}
.__P__ .ag-pc:hover{transform:translateY(-6px);border-color:rgba(240,185,62,.55);box-shadow:0 24px 50px -24px rgba(240,185,62,.4)}
.__P__ .ag-pc img{display:block;width:58px;height:58px;margin-bottom:18px;filter:drop-shadow(0 12px 10px rgba(0,0,0,.45))}
.__P__ .ag-pc h3{margin:0;font-size:1.28rem;font-weight:800;letter-spacing:-.02em}
.__P__ .ag-pc p{margin:10px 0 0;color:var(--ag-muted);line-height:1.65;font-size:.98rem}
.__P__ .ag-pc .ag-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.__P__ .ag-pc .ag-chips span{padding:6px 12px;border-radius:999px;border:1px solid var(--ag-line);font-size:.82rem;color:var(--ag-text)}
.__P__ .ag-pbridge{margin:26px 0 0;max-width:70ch;color:var(--ag-muted);line-height:1.75;font-size:1.05rem}
.__P__ ol.ag-jl{list-style:none;margin:96px 0 0;padding:0;display:grid;grid-template-columns:repeat(7,1fr);gap:0;border-top:1px solid var(--ag-line)}
.__P__ .ag-j{position:relative;padding:28px 18px 10px 0}
.__P__ .ag-j::before{content:"";position:absolute;left:0;top:-5px;width:9px;height:9px;border-radius:50%;background:var(--ag-gold);box-shadow:0 0 14px var(--ag-gold)}
.__P__ .ag-j img{display:block;width:60px;height:60px;margin-bottom:14px;filter:drop-shadow(0 12px 10px rgba(0,0,0,.6));transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-j:hover img{transform:translateY(-6px) rotate(-6deg)}
.__P__ .ag-jn{font-size:.8rem;font-weight:800;color:var(--ag-text)}
.__P__ .ag-j h3{margin:4px 0 0;font-size:1.1rem;font-weight:800;letter-spacing:-.01em}
.__P__ .ag-j p{margin:8px 0 0;color:var(--ag-muted);font-size:.9rem;line-height:1.55}
.__P__ .ag-ms{margin-top:96px;display:grid;grid-template-columns:1fr 1fr;gap:70px}
.__P__ .ag-ms h2{margin:0 0 22px;font-size:1.7rem;font-weight:800;letter-spacing:-.02em}
.__P__ .ag-it{display:flex;gap:18px;padding:20px 0;border-top:1px solid var(--ag-line)}
.__P__ .ag-it:last-of-type{border-bottom:1px solid var(--ag-line)}
.__P__ .ag-it strong{flex:none;min-width:84px;font-size:1.6rem;font-weight:800;letter-spacing:-.03em;color:var(--ag-text);line-height:1.1}
.__P__ .ag-it b{display:block;margin-bottom:4px}
.__P__ .ag-it p{margin:0;color:var(--ag-muted);line-height:1.6;font-size:.96rem}
.__P__ .ag-note{margin:18px 0 0;font-size:.82rem;color:var(--ag-muted)}
.__P__ .ag-phi{margin:0;padding:0;list-style:none;display:grid;gap:0}
.__P__ .ag-phi li{padding:20px 0;border-top:1px solid var(--ag-line)}
.__P__ .ag-phi li:last-child{border-bottom:1px solid var(--ag-line)}
.__P__ .ag-phi b{display:block;font-size:1.1rem;margin-bottom:4px}
.__P__ .ag-phi p{margin:0;color:var(--ag-muted);line-height:1.6;font-size:.98rem}
.__P__ .ag-quote{margin-top:96px;text-align:left;font-size:clamp(1.6rem,2.4vw + .8rem,3rem);font-weight:800;letter-spacing:-.03em;line-height:1.12;max-width:20ch}
.__P__ .ag-quote em{font-style:normal;color:var(--ag-gold-t);text-shadow:0 0 30px rgba(240,185,62,.35)}
@media (max-width:1000px){.__P__ .ag-pl{grid-template-columns:1fr}.__P__ ol.ag-jl{grid-template-columns:repeat(4,1fr);gap:26px 0}.__P__ .ag-tt{grid-template-columns:1fr;gap:48px}.__P__ .ag-ms{grid-template-columns:1fr;gap:56px}}
@media (max-width:760px){.__P__ ol.ag-jl{grid-template-columns:1fr 1fr 1fr}}
@media (max-width:520px){.__P__ ol.ag-jl{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-fig>img{animation:none}}
''',f'''
<section class="__P__" id="__P__" aria-label="About Azeez Gazalle">
  <div class="ag-glow" style="left:-10%;top:0;width:50vw;height:50vw;max-width:700px;max-height:700px"></div>
  <div class="ag-wrap">
    <div class="ag-tt">
      <div class="ag-fig" data-r>
        <div class="ag-arch"><div class="ag-ph"><b>Portrait placeholder</b><span>Replace with your photo (PHOTO_URL)</span></div><img class="ag-photo" id="ag-abt-photo" alt="Azeez Gazalle" hidden></div>
        <img data-em="Sparkles|sparkles" alt=""><img data-em="Keyboard|keyboard" alt="">
      </div>
      <div class="ag-prose">
        <div class="ag-eye" data-r>The short version</div>
        <h2 class="ag-h2" data-r style="--i:1">I'm Azeez, a web designer, developer and Meta Ads specialist who started in <em>graphic design</em>.</h2>
        <p data-r style="--i:2;margin-top:26px">My journey into digital design and development began with graphic design, where I learned how visual communication shapes the way people understand a brand.</p>
        <p data-r style="--i:3">That curiosity moved beyond static visuals. I taught myself Python and built a calculator and a ping-pong game, which introduced me to programming logic and interactive experiences. From there I moved into web development and Figma-based interface design.</p>
        <p data-r style="--i:4">Discovering GoHighLevel changed how I think about the work. Websites, landing pages, funnels, CRM and automation can work together to support a business's whole customer journey. </p>
        <p data-r style="--i:5">Alongside building websites, I have spent roughly 3 to 4 years working with Meta Ads, planning campaign strategy and managing campaigns, including the day-to-day work of running ads. That gives me both sides of digital marketing: the creative that earns attention and the campaign thinking that turns it into enquiries. Today I bring design, development and advertising together, and I work as an independent professional with clients in Nigeria and abroad.</p>
      </div>
    </div>
    <div class="ag-pls">
      <div class="ag-eye" data-r>What I do</div>
      <h2 class="ag-h2" data-r style="--i:1">Three disciplines, <em>one practice</em>.</h2>
      <div class="ag-pl">
        <div class="ag-pc" data-r><img data-em="Artist palette|artist_palette" alt=""><h3>Graphic design</h3><p>Where I started: visual communication and how design shapes the way people see a brand.</p><div class="ag-chips"><span>Visual communication</span><span>Layout</span><span>Brand visuals</span></div></div>
        <div class="ag-pc" data-r style="--i:1"><img data-em="Laptop|laptop" alt=""><h3>Website design and development</h3><p>Websites, landing pages and sales funnels, designed in Figma and built to work well on every device.</p><div class="ag-chips"><span>Websites</span><span>Landing pages</span><span>Sales funnels</span></div></div>
        <div class="ag-pc" data-r style="--i:2"><img data-em="Chart increasing|chart_increasing" alt=""><h3>Meta Ads strategy and management</h3><p>Around 3 to 4 years planning and managing campaigns on Meta, from strategy through to running the ads.</p><div class="ag-chips"><span>Campaign strategy</span><span>Campaign management</span><span>Running ads</span></div></div>
      </div>
      <p class="ag-pbridge" data-r>The pieces support each other. A well-designed page converts better when the ad that sends people to it is built for the same audience, and an ad is easier to run well when the page behind it is clear. I can handle both sides, or the part you need.</p>
    </div>
    <ol class="ag-jl">{jn}</ol>
    <div class="ag-ms">
      <div data-r>
        <h2>Experience so far</h2>
        <div class="ag-it"><strong>7+</strong><div><b>Business websites built</b><p>Platforms that help businesses present their brand, services and value online.</p></div></div>
        <div class="ag-it"><strong>10+</strong><div><b>Landing pages developed</b><p>Focused pages that communicate an offer clearly and guide visitors to one action.</p></div></div>
        <div class="ag-it"><strong>10+</strong><div><b>Clients served</b><p>Businesses and entrepreneurs in Nigeria and abroad.</p></div></div>
        <div class="ag-it"><strong>3-4</strong><div><b>Years designing and building</b><p>Across graphic design, Python fundamentals, web development, Figma and GoHighLevel.</p></div></div>
        <div class="ag-it"><strong>3-4</strong><div><b>Years working with Meta Ads</b><p>Campaign strategy and management on Meta.</p></div></div>
        <p class="ag-note">Self-reported figures. Sales funnels are also part of my work.</p>
      </div>
      <div data-r style="--i:1">
        <h2>How I approach the work</h2>
        <ul class="ag-phi">
          <li><b>Design with intention</b><p>Every layout, visual element and interaction should contribute to one coherent experience.</p></li>
          <li><b>Build for functionality</b><p>A site should work reliably on every device and make it easy to navigate and take action.</p></li>
          <li><b>Think beyond the page</b><p>Websites, funnels and connected systems belong to a wider customer journey.</p></li>
          <li><b>Join creative and performance</b><p>Good design gets attention. Good campaign management makes sure that attention reaches the right people.</p></li>
        </ul>
      </div>
    </div>
    <p class="ag-quote" data-r>Thoughtful design. Functional development. <em>Built with purpose.</em></p>
  </div>
</section>
''','''
  var PHOTO_URL='__ABOUT__';
  if(PHOTO_URL){var im=document.getElementById('ag-abt-photo');im.src=PHOTO_URL;im.hidden=false;root.querySelector('.ag-ph').style.display='none';}
''','(About page) ')


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
.__P__ .ag-big{font-size:clamp(3.4rem,13.5vw,13rem);margin-top:22px;background-image:linear-gradient(90deg,var(--ag-fillc) var(--p,100%),transparent calc(var(--p,100%) + .01%))}
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
page_hero('about','About me','About','A route from graphic design into web development and Meta Ads, and how it shapes the way I work with clients.',
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
        <div><strong>7+</strong><span>Business websites</span></div>
        <div><strong>10+</strong><span>Landing pages</span></div>
        <div><strong>10+</strong><span>Clients served</span></div>
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

# ---------- PROJECTS (00-projects, home-work, work-showcase, project pages) ----------
exec(open('/home/claude/azeez-portfolio/tools/projects_part.py').read())

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
.__P__ .ag-tt{padding:0 24px;max-width:1248px;margin:0 auto 44px;display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.__P__ h2{margin:0;font-weight:900;text-transform:uppercase;letter-spacing:-.04em;line-height:.95;font-size:clamp(2.2rem,5.4vw,5.2rem);max-width:12ch}
.__P__ .ag-tt img{width:clamp(54px,7vw,100px);animation:ag-prop-f 6s ease-in-out infinite;filter:drop-shadow(0 16px 14px rgba(0,0,0,.5))}
.__P__ .ag-wall{margin:0}
.__P__ .ag-lane{overflow:hidden;padding:6px 0}
.__P__ .ag-track{display:flex;gap:20px;width:max-content;animation:ag-ht-run 60s linear infinite}
.__P__ .ag-lane:hover .ag-track{animation-play-state:paused}
.__P__ .ag-q{flex:none;width:clamp(270px,24vw,340px);display:flex;flex-direction:column;gap:18px;padding:24px;border-radius:20px;border:1px solid var(--ag-bd-hi);background:var(--ag-card)}
.__P__ .ag-q:before{content:"\\201C";font-size:2.6rem;line-height:.6;height:18px;font-weight:900;color:var(--ag-gold-t)}
.__P__ .ag-q p{margin:0;flex:1;font-size:.9rem;line-height:1.6;color:var(--ag-text)}
.__P__ .ag-by{display:flex;align-items:center;gap:12px;padding-top:16px;border-top:1px solid var(--ag-bd-hi)}
.__P__ .ag-av{flex:none;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;border:1.5px solid rgba(240,185,62,.6);color:var(--ag-gold-t);font-size:1rem;font-weight:800;line-height:1;overflow:hidden}
.__P__ .ag-by b{display:block;font-size:.9rem;font-weight:700;line-height:1.25;color:var(--ag-text)}
.__P__ .ag-by small{display:block;margin-top:2px;font-size:.74rem;font-weight:600;letter-spacing:.04em;color:var(--ag-muted)}
.__P__ .ag-q em{font-style:normal;color:var(--ag-gold-t);font-weight:800}
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
    {quote:'Azeez did a great job with our website. He understood what we wanted and was able to turn our ideas into something clean, professional, and easy to navigate. I particularly liked his attention to detail and how he handled our feedback throughout the project.',name:'Engr Ismail',role:'Nubidesnl'},
    {quote:'We wanted a website that would give our business a more professional online presence, and Azeez delivered exactly that. The design was impressive, the pages were well structured, and he made sure everything aligned with our brand. Working with him was a good experience.',name:'Engr Saheed',role:'Caliph Engineering Limited'},
    {quote:'Azeez understood the objective of the project from the beginning. He helped us structure the page, arrange the information properly, and create a better experience for potential customers. He was professional, receptive to feedback, and committed to getting the work done properly.',name:'Miss Precious',role:'Preshub Store'},
    {quote:'Working with Azeez was a smooth experience. He was patient enough to understand our requirements, offered useful suggestions, and paid attention to the little things that made a difference in the final website. I appreciate his creativity and professionalism.',name:'Mr Olasunkanmi',role:''}
  ];
  /* ------------------------------------------------------------------ */
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  var real=TESTIMONIALS.length>0, base=real?TESTIMONIALS:[1,2,3,4].map(function(){return {ph:true,quote:'Placeholder. A real quote from a client, used with their permission, goes here.',name:'Client name',role:'Business'};});
  function card(t){var nm=esc(t.name), ini=esc((t.name||'').replace(/^(Engr|Mr|Miss|Mrs)\\s+/,'').charAt(0)), av=t.photo?'<img alt="" src="'+esc(t.photo)+'" style="width:100%;height:100%;object-fit:cover">':ini;return '<figure class="ag-q" style="margin:0"><p>'+(t.ph?'<em>Placeholder.</em> '+esc(t.quote.replace(/^Placeholder\\.\\s*/,'')):esc(t.quote))+'</p><figcaption class="ag-by"><span class="ag-av">'+av+'</span><span><b>'+nm+'</b>'+(t.role?'<small>'+esc(t.role)+'</small>':'')+'</span></figcaption></figure>';}
  function lane(arr,cls){var h=arr.map(card).join('');return '<div class="ag-lane '+cls+'"><div class="ag-track">'+h+h+h+h+'</div></div>';}
  var rev=base.slice().reverse();
  document.getElementById('ag-htest-wall').innerHTML=lane(base,'');
''','(Home) ')

# ---------- CTA (light, "let's get in touch") with cartoon portrait + flying 3D emoji ----------
sec('home-cta','ag-hcta','''
.__P__{padding-bottom:0;overflow:hidden}
.__P__ .ag-wrap{min-height:min(84vh,720px)}
.__P__ .ag-big{font-size:clamp(3rem,10vw,9.6rem);line-height:.92;position:relative;z-index:3}
.__P__ .ag-sub{margin:30px 0 0;max-width:36ch;font-size:clamp(1.05rem,.4vw + 1rem,1.3rem);line-height:1.6;color:var(--ag-muted);position:relative;z-index:3}
.__P__ .ag-cta{display:flex;flex-wrap:wrap;gap:14px;margin-top:34px;position:relative;z-index:3}
.__P__ .ag-pill.ag-solid{background:var(--ag-text);color:var(--ag-bg)}
.__P__ .ag-pill.ag-solid:hover{background:var(--ag-gold);color:var(--ag-gold-ink)}
.__P__ .ag-note{margin:22px 0 120px;color:var(--ag-muted);font-size:.92rem;max-width:44ch;line-height:1.6;position:relative;z-index:3}
.__P__ .ag-me{position:absolute;z-index:2;right:max(24px,calc((100vw - 1248px)/2 + 24px + 3vw));bottom:0;width:min(37vw,540px);aspect-ratio:560/681;pointer-events:none}
.__P__ .ag-me .ag-meph{position:absolute;inset:0;display:grid;place-content:center;text-align:center;gap:6px;padding:12%;border:1.5px dashed rgba(138,90,0,.55);border-bottom:0;border-radius:999px 999px 0 0;background:radial-gradient(closest-side,rgba(240,185,62,.28),rgba(240,185,62,.06) 70%,transparent);color:var(--ag-gold-t)}
.__P__ .ag-me .ag-meph svg{width:46px;height:46px;margin:0 auto}
.__P__ .ag-me .ag-meph b{font-size:.74rem;letter-spacing:.14em;text-transform:uppercase}
.__P__ .ag-me .ag-meph span{font-size:.78rem;color:var(--ag-muted);line-height:1.4}
.__P__ .ag-me img.ag-mephoto{position:absolute;left:0;bottom:0;width:100%;height:100%;object-fit:contain;object-position:bottom;filter:drop-shadow(0 24px 30px rgba(0,0,0,.3))}
.__P__ .ag-me.ag-has .ag-meph{display:none}
.__P__ .ag-glow2{position:absolute;z-index:0;right:6%;bottom:-10%;width:54vw;height:54vw;max-width:760px;max-height:760px;border-radius:50%;background:radial-gradient(closest-side,rgba(240,185,62,.5),rgba(240,185,62,.14) 60%,transparent 76%);pointer-events:none}
@media (max-width:900px){.__P__ .ag-wrap{min-height:0}.__P__ .ag-note{margin-bottom:36px}.__P__ .ag-me{position:relative;right:auto;margin:0 auto;width:min(86vw,420px)}.__P__ .ag-prop{--w:22vw !important;--x:70% !important;--y:41% !important}}
@media (max-width:560px){.__P__ .ag-prop{--x:76% !important;--y:2.5% !important}}
''',f'''
<section class="__P__" id="__P__" aria-label="Start a project">
  <div class="ag-glow2"></div>
  {props([('Me neutral badge|me','49%','45%','9vw',1.3,-6,6,7,0)])}
  <div class="ag-wrap">
    <h2 class="ag-big" data-fill>Let's get in touch</h2>
    <p class="ag-sub" data-r>Have a project in mind? Let's build something that works.</p>
    <div class="ag-cta" data-r><a class="ag-pill ag-solid" data-ag-link="start" href="/start">Start a project {PILL_ARROW}</a><a class="ag-pill" data-ag-link="contact" href="/contact#book">Book a discovery call</a></div>
    <p class="ag-note" data-r>I typically respond to project inquiries within 24 business hours, Monday to Friday. The discovery call is free and lasts 20 minutes.</p>
  </div>
  <div class="ag-me" id="__P__-meb"><img class="ag-mephoto" data-em="Me smile|me" alt="Azeez Gazalle, web designer and developer" width="560" height="681"></div>
</section>
''','''

''','(Home and most pages, before the footer) ')

print('built v6')
