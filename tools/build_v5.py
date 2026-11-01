# Generates the v5 sections. Every output file is fully self-contained (one GHL custom code block each).
import os, re, json
OUT='/home/claude/azeez-portfolio/sections'
FONT='''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400;0,500;0,600;0,700;0,800;1,500&display=swap" rel="stylesheet">
'''
LINKS="{ home:'/', work:'/work', project:'/work/project', services:'/services', process:'/process', about:'/about', contact:'/contact' }"
ARROW='<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10h12M11 5l5 5-5 5"/></svg>'

BASE_CSS='''
.__P__{--ag-bg:#07070a;--ag-surface:#101014;--ag-surface-2:#16161b;--ag-line:rgba(255,255,255,.12);--ag-text:#f8f3e9;--ag-muted:#b9b1a1;--ag-gold:#f0b93e;--ag-gold-hi:#ffd479;--ag-gold-ink:#1a1204;
  position:relative;background:var(--ag-bg);color:var(--ag-text);font-family:'Figtree',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;padding:104px 24px;box-sizing:border-box;overflow:hidden}
.__P__ *,.__P__ *::before,.__P__ *::after{box-sizing:border-box}
.__P__ .ag-wrap{max-width:1248px;margin:0 auto;position:relative;z-index:1}
.__P__ .ag-head{max-width:760px;margin:0 0 52px}
.__P__ .ag-eye{display:inline-flex;align-items:center;gap:10px;font-size:.8rem;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--ag-gold)}
.__P__ .ag-eye::before{content:"";width:34px;height:1.5px;background:var(--ag-gold)}
.__P__ .ag-h2{margin:18px 0 0;font-weight:800;letter-spacing:-.03em;line-height:1.08;font-size:clamp(1.8rem,2.1vw + 1rem,3.05rem)}
.__P__ .ag-h2 em{font-style:normal;color:var(--ag-gold)}
.__P__ .ag-lead{margin:16px 0 0;font-size:clamp(1rem,.3vw + .95rem,1.18rem);line-height:1.65;color:var(--ag-muted);max-width:58ch}
.__P__ .ag-btn{display:inline-flex;align-items:center;gap:10px;padding:15px 26px;border-radius:999px;font:700 1rem/1 'Figtree',sans-serif;text-decoration:none;cursor:pointer;border:1px solid transparent;transition:transform .25s,background .25s,border-color .25s,box-shadow .25s}
.__P__ .ag-btn svg{width:18px;height:18px;transition:transform .25s}
.__P__ .ag-btn:hover svg{transform:translateX(4px)}
.__P__ .ag-btn--gold{background:var(--ag-gold);color:var(--ag-gold-ink);box-shadow:0 14px 38px -12px rgba(240,185,62,.7)}
.__P__ .ag-btn--gold:hover{background:var(--ag-gold-hi);transform:translateY(-2px)}
.__P__ .ag-btn--ghost{background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.22);color:var(--ag-text)}
.__P__ .ag-btn--ghost:hover{border-color:var(--ag-gold);transform:translateY(-2px)}
.__P__ a:focus-visible,.__P__ button:focus-visible{outline:2px solid var(--ag-gold-hi);outline-offset:3px;border-radius:6px}
.__P__ .ag-glow{position:absolute;z-index:0;pointer-events:none;border-radius:50%;background:radial-gradient(closest-side,rgba(240,185,62,.22),rgba(240,185,62,.07) 55%,transparent 74%)}
.__P__ .ag-ph{display:grid;place-content:center;text-align:center;gap:6px;color:var(--ag-gold);background:repeating-linear-gradient(135deg,rgba(240,185,62,.07) 0 12px,rgba(240,185,62,.02) 12px 24px);border:1.5px dashed rgba(240,185,62,.5)}
.__P__ .ag-ph b{font-size:.74rem;letter-spacing:.14em;text-transform:uppercase}
.__P__ .ag-ph span{font-size:.78rem;color:var(--ag-muted)}
.__P__[data-pre] [data-r]{opacity:0;filter:blur(8px);transform:translateY(24px)}
.__P__ [data-r]{transition:opacity .85s cubic-bezier(.2,.7,.2,1),filter .85s cubic-bezier(.2,.7,.2,1),transform .85s cubic-bezier(.2,.7,.2,1);transition-delay:calc(var(--i,0) * 80ms)}
.__P__[data-pre] [data-r].ag-in{opacity:1;filter:none;transform:none}
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
  em(); links(); reveal(); tilt();
})();
</script>
'''

def sec(name, p, css, html, js='', comment=''):
    s=f'<!-- ========== AG SECTION: {name} {comment}==========\n     Paste into its own GHL Custom Code block. -->\n'+FONT
    s+='<style>'+(BASE_CSS+css).replace('__P__',p)+'</style>\n'
    s+=html.replace('__P__',p)
    s+=(JS_HEAD+js+JS_TAIL).replace('__P__',p).replace('__LINKS__',LINKS)
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
TOOLS=[('HTML5','html5'),('CSS3','css3'),('JavaScript','javascript'),('React','react'),('Supabase','supabase'),('Vercel','vercel'),('Figma','figma'),('GitHub','github')]

# ============ LOGO MARQUEE ============
def tile(t):
    n,slug=t
    return f'<span class="ag-tl" title="{n}"><img{' class="ag-inv"' if slug in ('vercel','github') else ''} loading="lazy" alt="{n}" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons/{slug}/{slug}-original.svg"></span>'
def tile_make(): return '<span class="ag-tl" title="Make"><span class="ag-mk" role="img" aria-label="Make"></span></span>'
def tile_ghl(): return '<span class="ag-tl ag-tl--word" title="GoHighLevel"><b>GoHighLevel</b></span>'
items=[tile(TOOLS[0]),tile(TOOLS[1]),tile(TOOLS[2]),tile(TOOLS[3]),tile_ghl(),tile(TOOLS[4]),tile(TOOLS[5]),tile_make(),tile(TOOLS[6]),tile(TOOLS[7])]
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
<section class="__P__" id="__P__" aria-label="Tools I build with">
  <p class="ag-lbl">The tools I build with</p>
  <div class="ag-row"><div class="ag-track">{track}{track}</div></div>
</section>
''','','(Home, under the hero) ')

# ============ PAGE HEROES ============
def page_hero(key,eye,title,lead,e1,e2,e3):
    sec(f'page-hero-{key}',f'ag-ph-{key}','''
.__P__{padding:150px 24px 70px}
.__P__ .ag-wrap{display:grid;grid-template-columns:1.2fr .8fr;gap:30px;align-items:center}
.__P__ h1{margin:18px 0 0;font-weight:800;letter-spacing:-.035em;line-height:1.06;font-size:clamp(2.1rem,2.8vw + 1.1rem,3.9rem);max-width:16ch}
.__P__ h1 em{font-style:normal;color:var(--ag-gold);text-shadow:0 0 30px rgba(240,185,62,.35)}
.__P__ .ag-art{position:relative;aspect-ratio:1.1/1;max-width:420px;width:100%;margin-left:auto}
.__P__ .ag-art img{position:absolute;display:block;filter:drop-shadow(0 22px 20px rgba(0,0,0,.6));animation:ag-ph-float 6s ease-in-out infinite}
.__P__ .ag-art img:nth-child(1){width:52%;left:24%;top:14%}
.__P__ .ag-art img:nth-child(2){width:30%;left:0;top:56%;animation-delay:-2s}
.__P__ .ag-art img:nth-child(3){width:26%;right:2%;top:2%;animation-delay:-4s}
@keyframes ag-ph-float{0%,100%{transform:translateY(0) rotate(-5deg)}50%{transform:translateY(-14px) rotate(5deg)}}
@media (max-width:860px){.__P__{padding:120px 20px 40px}.__P__ .ag-wrap{grid-template-columns:1fr}.__P__ .ag-art{max-width:260px;margin:10px 0 0}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-art img{animation:none}}
''',f'''
<section class="__P__" id="__P__" aria-label="{eye}">
  <div class="ag-glow" style="right:-8%;top:-10%;width:60vw;height:60vw;max-width:800px;max-height:800px"></div>
  <div class="ag-wrap">
    <div>
      <div class="ag-eye" data-r>{eye}</div>
      <h1 data-r style="--i:1">{title}</h1>
      <p class="ag-lead" data-r style="--i:2">{lead}</p>
    </div>
    <div class="ag-art" aria-hidden="true">{emimg(e1)}{emimg(e2)}{emimg(e3)}</div>
  </div>
</section>
''','','(top of the page) ')
page_hero('work','Selected work','Work that shows the <em>thinking</em>, not just the screens.','Each project below pairs the finished design with the objective, my role and the decisions behind it.','Trophy|trophy','Laptop|laptop','Sparkles|sparkles')
page_hero('services','Services and pricing','Clear services. <em>Honest</em> starting prices.','Six ways I can help. Prices are indicative starting points, and a tailored proposal confirms the final scope, cost and timeline.','Money bag|money_bag','Rocket|rocket','Gem stone|gem_stone')
page_hero('process','How I work','A structured process from the <em>first conversation</em> to launch.','No unnecessary complexity. No unclear expectations. Six stages, each with a clear outcome and timeline.','Compass|compass','Magic wand|magic_wand','Light bulb|light_bulb')
page_hero('about','About me','From graphic design to <em>building</em> digital experiences.','A multidisciplinary route into web design and development, and how it shapes the way I work with clients.','Artist palette|artist_palette','Keyboard|keyboard','Sparkles|sparkles')

# ============ HOME ABOUT ============
sec('home-about','ag-habout','''
.__P__ .ag-wrap{display:grid;grid-template-columns:.8fr 1.2fr;gap:64px;align-items:center}
.__P__ .ag-fig{position:relative;max-width:400px;margin:0 auto;width:100%}
.__P__ .ag-arch{position:relative;aspect-ratio:3/4;border-radius:999px 999px 24px 24px;border:1px solid rgba(240,185,62,.55);overflow:hidden;box-shadow:0 0 90px -12px rgba(240,185,62,.4);background:linear-gradient(180deg,rgba(240,185,62,.14),rgba(0,0,0,.4))}
.__P__ .ag-arch .ag-ph{position:absolute;inset:14px;border-radius:999px 999px 12px 12px;padding:12%}
.__P__ .ag-arch img.ag-photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.__P__ .ag-fig>img{position:absolute;width:24%;filter:drop-shadow(0 18px 16px rgba(0,0,0,.6));animation:ag-ha-float 6s ease-in-out infinite}
.__P__ .ag-fig>img:nth-of-type(1){right:-8%;top:8%}
.__P__ .ag-fig>img:nth-of-type(2){left:-10%;bottom:12%;width:20%;animation-delay:-3s}
@keyframes ag-ha-float{0%,100%{transform:translateY(0) rotate(-6deg)}50%{transform:translateY(-12px) rotate(6deg)}}
.__P__ p.ag-body{margin:18px 0 0;font-size:1.08rem;line-height:1.75;color:var(--ag-muted);max-width:60ch}
.__P__ .ag-facts{display:flex;flex-wrap:wrap;gap:12px 36px;margin:32px 0;padding:24px 0;border-top:1px solid var(--ag-line);border-bottom:1px solid var(--ag-line)}
.__P__ .ag-facts strong{display:block;font-size:1.9rem;font-weight:800;letter-spacing:-.03em;line-height:1}
.__P__ .ag-facts span{display:block;margin-top:6px;font-size:.84rem;color:var(--ag-muted)}
@media (max-width:900px){.__P__ .ag-wrap{grid-template-columns:1fr;gap:44px}.__P__ .ag-fig{max-width:320px}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-fig>img{animation:none}}
''','''
<section class="__P__" id="__P__" aria-label="About">
  <div class="ag-glow" style="left:-10%;top:10%;width:46vw;height:46vw;max-width:640px;max-height:640px"></div>
  <div class="ag-wrap">
    <div class="ag-fig" data-r>
      <div class="ag-arch"><div class="ag-ph"><b>Portrait placeholder</b><span>Replace with your photo (PHOTO_URL)</span></div><img class="ag-photo" id="ag-habout-photo" alt="Azeez Gazalle" hidden></div>
      <img data-em="Sparkles|sparkles" alt=""><img data-em="Laptop|laptop" alt="">
    </div>
    <div>
      <div class="ag-eye" data-r>About me</div>
      <h2 class="ag-h2" data-r style="--i:1">A designer who <em>learned to build</em>.</h2>
      <p class="ag-body" data-r style="--i:2">I started in graphic design, then taught myself Python by building a calculator and a ping-pong game. That curiosity led to web development, Figma and GoHighLevel, where I learned how websites, funnels and CRM automation fit together.</p>
      <p class="ag-body" data-r style="--i:3">Today I design and build websites and landing pages that look considered, work reliably and are aimed at the goals of the business behind them.</p>
      <div class="ag-facts" data-r style="--i:4">
        <div><strong>6+</strong><span>Business websites</span></div>
        <div><strong>5+</strong><span>Landing pages</span></div>
        <div><strong>3-4 yrs</strong><span>Designing and building</span></div>
      </div>
      <a class="ag-btn ag-btn--ghost" data-ag-link="about" href="/about" data-r style="--i:5">More about me '''+ARROW+'''</a>
    </div>
  </div>
</section>
''','''
  var PHOTO_URL=''; /* your photo (any aspect, it is cropped to the arch) */
  if(PHOTO_URL){var im=document.getElementById('ag-habout-photo');im.src=PHOTO_URL;im.hidden=false;root.querySelector('.ag-ph').style.display='none';}
''','(Home) ')

# ============ HOME SERVICES TEASER ============
rows=''.join(f'''<a class="ag-row" data-ag-link="services" href="/services" data-r style="--i:{i}">
  <span class="ag-n">0{i+1}</span><span class="ag-nm">{s[0]}</span><span class="ag-ds">{s[4]}</span>
  <span class="ag-go"><img data-em="{s[3]}" alt="">{ARROW}</span></a>''' for i,s in enumerate(SERVICES))
sec('home-services','ag-hsvc','''
.__P__ .ag-list{border-top:1px solid var(--ag-line)}
.__P__ .ag-row{position:relative;display:grid;grid-template-columns:70px 1.1fr 1.3fr 110px;gap:24px;align-items:center;padding:30px 12px;border-bottom:1px solid var(--ag-line);text-decoration:none;color:inherit;transition:background .3s,padding .3s}
.__P__ .ag-row:hover{background:linear-gradient(90deg,rgba(240,185,62,.1),transparent 70%);padding-left:26px}
.__P__ .ag-n{font-weight:800;color:var(--ag-gold);font-size:.95rem}
.__P__ .ag-nm{font-size:clamp(1.15rem,.9vw + .9rem,1.65rem);font-weight:800;letter-spacing:-.02em;line-height:1.2}
.__P__ .ag-ds{color:var(--ag-muted);line-height:1.55;font-size:1rem}
.__P__ .ag-go{display:flex;justify-content:flex-end;align-items:center;gap:12px;color:var(--ag-gold)}
.__P__ .ag-go img{width:52px;height:52px;opacity:0;transform:translateY(8px) scale(.8) rotate(-8deg);transition:opacity .3s,transform .35s cubic-bezier(.2,.7,.2,1);filter:drop-shadow(0 12px 10px rgba(0,0,0,.5))}
.__P__ .ag-row:hover .ag-go img{opacity:1;transform:none}
.__P__ .ag-go svg{width:22px;height:22px;transition:transform .3s}
.__P__ .ag-row:hover .ag-go svg{transform:translateX(5px)}
.__P__ .ag-foot{margin-top:40px;display:flex;flex-wrap:wrap;gap:16px 24px;align-items:center}
.__P__ .ag-foot p{margin:0;color:var(--ag-muted);font-size:.95rem}
@media (max-width:900px){.__P__ .ag-row{grid-template-columns:44px 1fr 40px;gap:14px;padding:24px 4px}.__P__ .ag-ds{display:none}.__P__ .ag-go img{display:none}}
@media (hover:none){.__P__ .ag-go img{opacity:1;transform:none}}
''',f'''
<section class="__P__" id="__P__" aria-label="Services">
  <div class="ag-wrap">
    <div class="ag-head">
      <div class="ag-eye" data-r>What I build</div>
      <h2 class="ag-h2" data-r style="--i:1">Six ways I can help your <em>business</em>.</h2>
      <p class="ag-lead" data-r style="--i:2">From a single landing page to a custom web application. Details, inclusions and starting prices are on the services page.</p>
    </div>
    <div class="ag-list">{rows}</div>
    <div class="ag-foot" data-r><a class="ag-btn ag-btn--gold" data-ag-link="services" href="/services">Services and pricing {ARROW}</a><p>Every price is a starting point. You get a tailored proposal before anything begins.</p></div>
  </div>
</section>
''','','(Home) ')

# ============ HOME PROCESS TEASER ============
steps=''.join(f'<li class="ag-st" data-r style="--i:{i}"><span class="ag-num">0{i+1}</span><img data-em="{s[3]}" alt=""><h3>{s[0]}</h3><span class="ag-tm">{s[1]}</span></li>' for i,s in enumerate(STEPS))
sec('home-process','ag-hproc','''
.__P__{background:linear-gradient(180deg,#07070a,#0c0b08 50%,#07070a)}
.__P__ ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,1fr);gap:0;position:relative}
.__P__ ol::before{content:"";position:absolute;left:0;right:0;top:61px;height:1.5px;background:linear-gradient(90deg,transparent,rgba(240,185,62,.7),transparent)}
.__P__ .ag-st{position:relative;padding:0 14px;text-align:left}
.__P__ .ag-num{display:block;font-weight:800;color:var(--ag-gold);font-size:.9rem;margin-bottom:8px}
.__P__ .ag-st img{display:block;width:76px;height:76px;margin-bottom:14px;filter:drop-shadow(0 14px 12px rgba(0,0,0,.6));transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-st:hover img{transform:translateY(-8px) rotate(-6deg) scale(1.08)}
.__P__ .ag-st h3{margin:0;font-size:1.12rem;font-weight:800;letter-spacing:-.01em;line-height:1.25}
.__P__ .ag-tm{display:block;margin-top:6px;font-size:.84rem;color:var(--ag-muted)}
.__P__ .ag-foot{margin-top:48px}
@media (max-width:980px){.__P__ ol{grid-template-columns:1fr 1fr;gap:34px 0}.__P__ ol::before{display:none}}
@media (max-width:520px){.__P__ ol{grid-template-columns:1fr}}
''',f'''
<section class="__P__" id="__P__" aria-label="Process">
  <div class="ag-wrap">
    <div class="ag-head">
      <div class="ag-eye" data-r>My process</div>
      <h2 class="ag-h2" data-r style="--i:1">No unnecessary complexity. <em>No unclear expectations.</em></h2>
      <p class="ag-lead" data-r style="--i:2">Just a structured process from the first conversation to launch.</p>
    </div>
    <ol>{steps}</ol>
    <div class="ag-foot" data-r><a class="ag-btn ag-btn--ghost" data-ag-link="process" href="/process">See the full process {ARROW}</a></div>
  </div>
</section>
''','','(Home) ')

# ============ HOME CTA ============
sec('home-cta','ag-hcta','''
.__P__{padding:110px 24px}
.__P__ .ag-box{position:relative;overflow:hidden;border-radius:36px;border:1px solid rgba(240,185,62,.4);padding:clamp(40px,6vw,88px);background:linear-gradient(135deg,#17130a,#0b0b0e 60%);box-shadow:0 40px 120px -40px rgba(240,185,62,.35)}
.__P__ h2{margin:0;font-weight:800;letter-spacing:-.035em;line-height:1.05;font-size:clamp(2rem,3vw + 1rem,4rem);max-width:15ch}
.__P__ h2 em{font-style:normal;color:var(--ag-gold);text-shadow:0 0 34px rgba(240,185,62,.4)}
.__P__ .ag-cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:34px}
.__P__ .ag-note{margin:18px 0 0;color:var(--ag-muted);font-size:.95rem;max-width:52ch;line-height:1.6}
.__P__ .ag-big{position:absolute;right:4%;top:50%;width:min(30%,340px);transform:translateY(-50%);filter:drop-shadow(0 30px 30px rgba(0,0,0,.6));animation:ag-hc-float 6s ease-in-out infinite}
.__P__ .ag-big2{position:absolute;right:26%;bottom:8%;width:min(11%,120px);animation:ag-hc-float 5s ease-in-out infinite -2s;filter:drop-shadow(0 18px 16px rgba(0,0,0,.6))}
@keyframes ag-hc-float{0%,100%{transform:translateY(-50%) rotate(-6deg)}50%{transform:translateY(-56%) rotate(6deg)}}
.__P__ .ag-big2{animation-name:ag-hc-float2}
@keyframes ag-hc-float2{0%,100%{transform:translateY(0) rotate(6deg)}50%{transform:translateY(-14px) rotate(-6deg)}}
@media (max-width:820px){.__P__ .ag-big{opacity:.35;width:46%}.__P__ .ag-big2{display:none}.__P__ .ag-box{border-radius:26px}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-big,.__P__ .ag-big2{animation:none}}
''',f'''
<section class="__P__" id="__P__" aria-label="Start a project">
  <div class="ag-wrap">
    <div class="ag-box" data-r>
      <img class="ag-big" data-em="Rocket|rocket" alt=""><img class="ag-big2" data-em="Sparkles|sparkles" alt="">
      <div style="position:relative;z-index:1">
        <div class="ag-eye">Start a project</div>
        <h2 style="margin-top:18px">Have a project in mind? Let's build something <em>that works</em>.</h2>
        <div class="ag-cta"><a class="ag-btn ag-btn--gold" data-ag-link="contact" href="/contact">Start a project {ARROW}</a><a class="ag-btn ag-btn--ghost" data-ag-link="contact" href="/contact#book">Book a discovery call</a></div>
        <p class="ag-note">I typically respond to project inquiries within 24 business hours, Monday to Friday. The discovery call is free and lasts 20 minutes.</p>
      </div>
    </div>
  </div>
</section>
''','','(Home, before the footer) ')

# ============ WORK SHOWCASE ============
SHOWCASE_CSS='''
.__P__ .ag-proj{position:relative;margin:0 0 110px;display:grid;grid-template-columns:repeat(12,1fr);gap:28px 32px;align-items:center}
.__P__ .ag-proj:last-of-type{margin-bottom:0}
.__P__ .ag-mock{grid-column:1/8;position:relative;transition:transform .3s ease-out;transform-style:preserve-3d;will-change:transform}
.__P__ .ag-proj.ag-alt .ag-mock{grid-column:6/13;grid-row:1}
.__P__ .ag-proj.ag-alt .ag-meta{grid-column:1/6;grid-row:1}
.__P__ .ag-meta{grid-column:8/13}
.__P__ .ag-proj.ag-feat .ag-mock{grid-column:1/13}
.__P__ .ag-proj.ag-feat .ag-meta{grid-column:1/13;display:grid;grid-template-columns:repeat(12,1fr);gap:28px 32px}
.__P__ .ag-proj.ag-feat .ag-m1{grid-column:1/6}.__P__ .ag-proj.ag-feat .ag-m2{grid-column:6/13}
.__P__ .ag-frame{position:relative;border-radius:18px;border:1px solid rgba(255,255,255,.16);background:#0d0d11;overflow:hidden;box-shadow:0 50px 90px -40px rgba(0,0,0,.9),0 0 90px -30px rgba(240,185,62,.35)}
.__P__ .ag-bar{display:flex;align-items:center;gap:8px;padding:12px 16px;border-bottom:1px solid rgba(255,255,255,.1);background:#131318}
.__P__ .ag-bar i{width:10px;height:10px;border-radius:50%;background:#34343c}
.__P__ .ag-url{margin-left:12px;flex:1;max-width:340px;padding:6px 14px;border-radius:999px;background:#0b0b0e;color:var(--ag-muted);font-size:.78rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.__P__ .ag-shot{position:relative;aspect-ratio:16/10;overflow:hidden;clip-path:inset(0 100% 0 0);transition:clip-path 1.1s cubic-bezier(.7,0,.2,1) .15s}
.__P__ .ag-in .ag-shot,.__P__ .ag-shot.ag-in,.__P__[data-pre] .ag-mock.ag-in .ag-shot{clip-path:inset(0 0 0 0)}
.__P__ .ag-shot img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-mock:hover .ag-shot img{transform:scale(1.04)}
.__P__ .ag-shot .ag-ph{position:absolute;inset:0;border:0;border-radius:0}
.__P__ .ag-flag{position:absolute;left:14px;top:14px;z-index:2;padding:6px 12px;border-radius:999px;background:var(--ag-gold);color:var(--ag-gold-ink);font-size:.7rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.__P__ .ag-no{font-weight:800;font-size:clamp(3.4rem,5vw,5.6rem);line-height:.9;letter-spacing:-.05em;color:transparent;-webkit-text-stroke:1.5px rgba(240,185,62,.7)}
.__P__ .ag-cat{margin:14px 0 0;font-size:.8rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--ag-gold)}
.__P__ .ag-meta h3{margin:8px 0 0;font-size:clamp(1.6rem,1.4vw + 1rem,2.4rem);font-weight:800;letter-spacing:-.03em;line-height:1.1}
.__P__ .ag-ind{margin:6px 0 0;color:var(--ag-muted);font-size:1rem}
.__P__ dl{margin:22px 0 0;display:grid;gap:16px}
.__P__ dt{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ dd{margin:4px 0 0;line-height:1.6;font-size:1rem}
.__P__ dd ul{margin:0;padding-left:18px;display:grid;gap:4px}
.__P__ .ag-chips{display:flex;flex-wrap:wrap;gap:8px}
.__P__ .ag-chips span{padding:6px 14px;border-radius:999px;border:1px solid var(--ag-line);font-size:.86rem;background:rgba(255,255,255,.03)}
.__P__ .ag-links{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.__P__ .ag-btn.ag-off{opacity:.55;pointer-events:none;border-style:dashed}
.__P__ .ag-all{margin-top:64px;display:flex;justify-content:center}
@media (max-width:980px){
  .__P__ .ag-proj,.__P__ .ag-proj.ag-feat .ag-meta{display:flex;flex-direction:column;align-items:stretch;gap:26px;margin-bottom:76px}
  .__P__ .ag-mock,.__P__ .ag-meta{width:100%}
}
@media (prefers-reduced-motion:reduce){.__P__ .ag-shot{clip-path:none;transition:none}}
'''
SHOWCASE_JS='''
  /* ---------- CONFIG: replace the placeholders with your real projects ----------
     image: URL of a screenshot (16:10, about 1600x1000). Leave '' to show the placeholder.
     live / caseStudy: URLs, or '' to hide the button. */
  var PROJECTS=[
    /* { name:'Project name', industry:'Client or industry', category:'Business website',
         objective:'What the client needed.', role:'Design and development',
         decisions:['Key design decision','Key technical decision'], deliverables:['Website','Analytics'],
         image:'https://...', live:'https://...', caseStudy:'/work/project' }, */
  ];
  var PLACEHOLDERS=[
    {name:'Project name',industry:'Client or industry',category:'Business website',objective:'Placeholder. Describe what this client needed and the goal of the project.',role:'Placeholder. For example: UX, visual design and development.',decisions:['Placeholder: a key design decision','Placeholder: a key technical decision'],deliverables:['Deliverable one','Deliverable two','Deliverable three'],image:'',live:'',caseStudy:'',ph:true},
    {name:'Project name',industry:'Client or industry',category:'Sales funnel',objective:'Placeholder. Describe what this client needed and the goal of the project.',role:'Placeholder. Your role on this project.',decisions:['Placeholder: a key design decision','Placeholder: a key technical decision'],deliverables:['Deliverable one','Deliverable two'],image:'',live:'',caseStudy:'',ph:true},
    {name:'Project name',industry:'Client or industry',category:'Landing page',objective:'Placeholder. Describe what this client needed and the goal of the project.',role:'Placeholder. Your role on this project.',decisions:['Placeholder: a key design decision','Placeholder: a key technical decision'],deliverables:['Deliverable one','Deliverable two'],image:'',live:'',caseStudy:'',ph:true}
  ];
  var MODE='__MODE__'; /* 'home' shows 2 projects, 'work' shows all */
  /* ------------------------------------------------------------------------- */
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  var list=(PROJECTS.length?PROJECTS:PLACEHOLDERS); if(MODE==='home')list=list.slice(0,2);
  var host=document.getElementById('__P__-list');
  list.forEach(function(p,i){
    var feat=(MODE==='work'&&i===0), alt=(!feat&&i%2===(MODE==='work'?0:1));
    var host2=(p.live||'').replace(/^https?:\\/\\//,'').replace(/\\/$/,'')||'yourclient.com';
    var shot=p.image?'<img loading="lazy" alt="'+esc(p.name)+' screenshot" src="'+esc(p.image)+'">':'<div class="ag-ph"><b>Project screenshot placeholder</b><span>1600 x 1000 px</span></div>';
    var mock='<div class="ag-mock" data-r data-tilt="5">'+(p.ph?'<span class="ag-flag">Placeholder</span>':'')+'<div class="ag-frame"><div class="ag-bar"><i></i><i></i><i></i><span class="ag-url">'+esc(host2)+'</span></div><div class="ag-shot">'+shot+'</div></div></div>';
    var dec=(p.decisions||[]).map(function(d){return '<li>'+esc(d)+'</li>';}).join('');
    var del=(p.deliverables||[]).map(function(d){return '<span>'+esc(d)+'</span>';}).join('');
    var btns='<a class="ag-btn ag-btn--gold'+(p.caseStudy?'':' ag-off')+'" '+(p.caseStudy?'href="'+esc(p.caseStudy)+'"':'data-ag-link="project" href="'+LINKS.project+'"')+'>'+(p.ph?'Case study template':'View case study')+' __ARROW__</a>'+(p.live?'<a class="ag-btn ag-btn--ghost" target="_blank" rel="noopener" href="'+esc(p.live)+'">Visit live site</a>':'');
    var head='<div class="ag-no">0'+(i+1)+'</div><p class="ag-cat">'+esc(p.category)+'</p><h3>'+esc(p.name)+'</h3><p class="ag-ind">'+esc(p.industry)+'</p>';
    var l1='<dl><div><dt>Objective</dt><dd>'+esc(p.objective)+'</dd></div><div><dt>My role</dt><dd>'+esc(p.role)+'</dd></div></dl>';
    var l2='<dl><div><dt>Key decisions</dt><dd><ul>'+dec+'</ul></dd></div><div><dt>Deliverables</dt><dd><div class="ag-chips">'+del+'</div></dd></div></dl><div class="ag-links">'+btns+'</div>';
    var meta=feat?'<div class="ag-meta" data-r><div class="ag-m1">'+head+l1+'</div><div class="ag-m2">'+l2+'</div></div>':'<div class="ag-meta" data-r style="--i:1">'+head+l1+l2+'</div>';
    var art=document.createElement('article'); art.className='ag-proj'+(feat?' ag-feat':'')+(alt?' ag-alt':'');
    art.innerHTML=mock+meta; host.appendChild(art);
  });
  links(host);
'''.replace('__ARROW__',ARROW.replace("'","\\'"))

for mode,name,p in [('home','home-work','ag-hwork'),('work','work-showcase','ag-wshow')]:
    head=('''<div class="ag-head"><div class="ag-eye" data-r>Selected work</div><h2 class="ag-h2" data-r style="--i:1">Websites and funnels built to <em>perform</em>.</h2><p class="ag-lead" data-r style="--i:2">Placeholders below show the layout. Your real projects, screenshots and case studies replace them.</p></div>'''
          if mode=='home' else '')
    tail=(f'<div class="ag-all" data-r><a class="ag-btn ag-btn--gold" data-ag-link="work" href="/work">See all work {ARROW}</a></div>' if mode=='home' else '')
    sec(name,p,SHOWCASE_CSS,f'''
<section class="__P__" id="__P__" aria-label="Selected work">
  <div class="ag-glow" style="right:-12%;top:20%;width:50vw;height:50vw;max-width:700px;max-height:700px"></div>
  <div class="ag-wrap">{head}<div id="__P__-list"></div>{tail}<noscript><p style="color:#b9b1a1">Enable JavaScript to see the project showcase.</p></noscript></div>
</section>
''',SHOWCASE_JS.replace('__MODE__',mode),'(%s) ' % ('Home' if mode=='home' else 'Work page'))

# ============ PROJECT DETAIL (case-study template) ============
sec('project-detail','ag-pd','''
.__P__{padding:150px 24px 90px}
.__P__ .ag-back{display:inline-flex;gap:8px;align-items:center;color:var(--ag-muted);text-decoration:none;font-weight:600;font-size:.92rem;margin-bottom:28px}
.__P__ .ag-back:hover{color:var(--ag-gold)}
.__P__ h1{margin:12px 0 0;font-weight:800;letter-spacing:-.035em;line-height:1.05;font-size:clamp(2.2rem,3.2vw + 1rem,4.4rem);max-width:16ch}
.__P__ .ag-flag{display:inline-block;margin-left:14px;vertical-align:middle;padding:6px 12px;border-radius:999px;background:var(--ag-gold);color:var(--ag-gold-ink);font-size:.7rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.__P__ .ag-facts{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin:44px 0;border-top:1px solid var(--ag-line);border-bottom:1px solid var(--ag-line)}
.__P__ .ag-facts div{padding:22px 20px 22px 0}
.__P__ dt{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ dd{margin:6px 0 0;font-weight:600;line-height:1.5}
.__P__ .ag-frame{border-radius:20px;border:1px solid rgba(255,255,255,.16);background:#0d0d11;overflow:hidden;box-shadow:0 60px 100px -40px rgba(0,0,0,.9),0 0 110px -30px rgba(240,185,62,.35)}
.__P__ .ag-bar{display:flex;align-items:center;gap:8px;padding:12px 16px;border-bottom:1px solid rgba(255,255,255,.1);background:#131318}
.__P__ .ag-bar i{width:10px;height:10px;border-radius:50%;background:#34343c}
.__P__ .ag-url{margin-left:12px;padding:6px 14px;border-radius:999px;background:#0b0b0e;color:var(--ag-muted);font-size:.78rem}
.__P__ .ag-shot{aspect-ratio:16/10;display:block}
.__P__ .ag-shot.ag-ph{border:0;border-radius:0}
.__P__ .ag-body{display:grid;grid-template-columns:.8fr 1.2fr;gap:30px 70px;margin-top:80px}
.__P__ .ag-body h2{margin:0;font-size:1.5rem;font-weight:800;letter-spacing:-.02em}
.__P__ .ag-body p,.__P__ .ag-body li{color:var(--ag-muted);line-height:1.75;font-size:1.05rem;margin:0}
.__P__ .ag-body ul{margin:0;padding-left:20px;display:grid;gap:8px}
.__P__ .ag-gal{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:80px}
.__P__ .ag-gal .ag-ph{aspect-ratio:4/3;border-radius:18px}
.__P__ .ag-gal .ag-ph.ag-w{grid-column:1/-1;aspect-ratio:16/8}
.__P__ .ag-next{margin-top:90px;padding-top:36px;border-top:1px solid var(--ag-line);display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;align-items:center}
.__P__ .ag-next b{font-size:clamp(1.4rem,1.5vw + 1rem,2.2rem);letter-spacing:-.02em}
@media (max-width:900px){.__P__{padding:120px 20px 70px}.__P__ .ag-facts{grid-template-columns:1fr 1fr}.__P__ .ag-body{grid-template-columns:1fr;margin-top:56px}.__P__ .ag-gal{grid-template-columns:1fr}}
''',f'''
<section class="__P__" id="__P__" aria-label="Case study template">
  <div class="ag-glow" style="right:-10%;top:0;width:50vw;height:50vw;max-width:720px;max-height:720px"></div>
  <div class="ag-wrap">
    <a class="ag-back" data-ag-link="work" href="/work">&larr; All work</a>
    <div class="ag-eye" data-r>Case study template</div>
    <h1 data-r style="--i:1">Project name<span class="ag-flag">Placeholder</span></h1>
    <p class="ag-lead" data-r style="--i:2">One or two sentences on what the project was and who it was for. Replace every line on this page with verified details about the real project.</p>
    <dl class="ag-facts" data-r>
      <div><dt>Client / industry</dt><dd>Placeholder</dd></div>
      <div><dt>My role</dt><dd>Placeholder</dd></div>
      <div><dt>Timeline</dt><dd>Placeholder</dd></div>
      <div><dt>Tools</dt><dd>Placeholder</dd></div>
    </dl>
    <div class="ag-frame" data-r><div class="ag-bar"><i></i><i></i><i></i><span class="ag-url">yourclient.com</span></div><div class="ag-shot ag-ph"><b>Hero screenshot placeholder</b><span>1600 x 1000 px</span></div></div>
    <div class="ag-body" data-r>
      <h2>Objective</h2><p>Placeholder. What did the client need, and what was the goal of the project?</p>
      <h2>The challenge</h2><p>Placeholder. What made this project difficult or interesting?</p>
      <h2>Approach and key decisions</h2><ul><li>Placeholder: a design decision and why you made it</li><li>Placeholder: a technical decision and why you made it</li><li>Placeholder: how the structure supports the goal</li></ul>
      <h2>Deliverables</h2><p>Placeholder. For example: website design, development, form and CRM integration, launch and handover.</p>
      <h2>Outcome</h2><p>Placeholder. Add only results you can verify, such as what launched, what changed, or a client comment you have permission to use. No invented numbers.</p>
    </div>
    <div class="ag-gal" data-r><div class="ag-ph ag-w"><b>Wide image placeholder</b><span>1600 x 800 px</span></div><div class="ag-ph"><b>Image placeholder</b><span>1200 x 900 px</span></div><div class="ag-ph"><b>Image placeholder</b><span>1200 x 900 px</span></div></div>
    <div class="ag-next" data-r><div><span style="color:#b9b1a1;font-size:.85rem">Next</span><br><b>Next project name</b></div><a class="ag-btn ag-btn--ghost" data-ag-link="work" href="/work">Back to all work {ARROW}</a></div>
  </div>
</section>
''','','(Project page) ')

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
.__P__ .ag-n{font-weight:800;color:var(--ag-gold);font-size:.95rem}
.__P__ .ag-nm{font-size:clamp(1.15rem,1.1vw + .9rem,1.8rem);font-weight:800;letter-spacing:-.02em;line-height:1.2}
.__P__ .ag-pr{text-align:right}
.__P__ .ag-pr b{display:block;font-size:clamp(1.15rem,.8vw + 1rem,1.55rem);font-weight:800;color:var(--ag-gold-hi);letter-spacing:-.02em}
.__P__ .ag-pr small{display:block;color:var(--ag-muted);font-size:.8rem;margin-top:2px}
.__P__ .ag-plus{position:relative;width:44px;height:44px;border-radius:50%;border:1px solid var(--ag-line);transition:background .3s,border-color .3s,transform .3s}
.__P__ .ag-plus::before,.__P__ .ag-plus::after{content:"";position:absolute;left:50%;top:50%;width:16px;height:2px;margin:-1px 0 0 -8px;background:var(--ag-text);transition:transform .3s,background .3s}
.__P__ .ag-plus::after{transform:rotate(90deg)}
.__P__ .ag-sh:hover .ag-plus{border-color:var(--ag-gold)}
.__P__ .ag-open .ag-plus{background:var(--ag-gold);border-color:var(--ag-gold)}
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
.__P__ .ag-it em{font-style:normal;color:var(--ag-gold-hi);font-weight:700}
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
.__P__ .ag-pn{position:relative;z-index:1;width:70px;height:70px;border-radius:50%;display:grid;place-items:center;background:var(--ag-bg);border:1.5px solid rgba(240,185,62,.6);color:var(--ag-gold);font-weight:800;font-size:1.15rem}
.__P__ .ag-pc{display:flex;gap:26px;align-items:flex-start;padding:26px 30px;border:1px solid var(--ag-line);border-radius:24px;background:var(--ag-surface);transition:border-color .3s,transform .3s}
.__P__ .ag-ps:hover .ag-pc{border-color:rgba(240,185,62,.5);transform:translateX(6px)}
.__P__ .ag-pc img{width:84px;height:84px;flex:none;filter:drop-shadow(0 14px 12px rgba(0,0,0,.6))}
.__P__ h3{margin:0;font-size:clamp(1.3rem,1vw + 1rem,1.8rem);font-weight:800;letter-spacing:-.02em}
.__P__ .ag-tm{display:inline-block;margin-top:10px;padding:5px 12px;border-radius:999px;background:rgba(240,185,62,.13);color:var(--ag-gold-hi);font-size:.8rem;font-weight:700}
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
.__P__ .ag-wn{font-weight:800;color:var(--ag-gold);font-size:.9rem}
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
.__P__ .ag-qb:hover i{border-color:var(--ag-gold)}
.__P__ .ag-open .ag-qb i{background:var(--ag-gold);border-color:var(--ag-gold)}
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
('Digital experiences','Design, development and strategy in one practice.','Sparkles|sparkles')]
jn=''.join(f'<li class="ag-j" data-r style="--i:{i%3}"><img data-em="{e}" alt=""><span class="ag-jn">0{i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i,(t,d,e) in enumerate(J))
sec('about-story','ag-abt','''
.__P__ .ag-top{display:grid;grid-template-columns:.85fr 1.15fr;gap:72px;align-items:center}
.__P__ .ag-fig{position:relative;max-width:440px;width:100%;margin:0 auto}
.__P__ .ag-arch{position:relative;aspect-ratio:3/4;border-radius:999px 999px 26px 26px;border:1px solid rgba(240,185,62,.55);overflow:hidden;box-shadow:0 0 110px -10px rgba(240,185,62,.45);background:linear-gradient(180deg,rgba(240,185,62,.14),rgba(0,0,0,.4))}
.__P__ .ag-arch .ag-ph{position:absolute;inset:14px;border-radius:999px 999px 12px 12px;padding:12%}
.__P__ .ag-arch img.ag-photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.__P__ .ag-fig>img{position:absolute;width:22%;filter:drop-shadow(0 18px 16px rgba(0,0,0,.6));animation:ag-ab-float 6s ease-in-out infinite}
.__P__ .ag-fig>img:nth-of-type(1){right:-9%;top:10%}.__P__ .ag-fig>img:nth-of-type(2){left:-9%;bottom:14%;width:18%;animation-delay:-3s}
@keyframes ag-ab-float{0%,100%{transform:translateY(0) rotate(-6deg)}50%{transform:translateY(-12px) rotate(6deg)}}
.__P__ .ag-prose p{margin:0 0 20px;font-size:1.12rem;line-height:1.8;color:var(--ag-muted);max-width:62ch}
.__P__ .ag-prose p:first-child{color:var(--ag-text);font-size:1.3rem;line-height:1.6}
.__P__ ol.ag-jl{list-style:none;margin:96px 0 0;padding:0;display:grid;grid-template-columns:repeat(6,1fr);gap:0;border-top:1px solid var(--ag-line)}
.__P__ .ag-j{position:relative;padding:28px 18px 10px 0}
.__P__ .ag-j::before{content:"";position:absolute;left:0;top:-5px;width:9px;height:9px;border-radius:50%;background:var(--ag-gold);box-shadow:0 0 14px var(--ag-gold)}
.__P__ .ag-j img{display:block;width:60px;height:60px;margin-bottom:14px;filter:drop-shadow(0 12px 10px rgba(0,0,0,.6));transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-j:hover img{transform:translateY(-6px) rotate(-6deg)}
.__P__ .ag-jn{font-size:.8rem;font-weight:800;color:var(--ag-gold)}
.__P__ .ag-j h3{margin:4px 0 0;font-size:1.1rem;font-weight:800;letter-spacing:-.01em}
.__P__ .ag-j p{margin:8px 0 0;color:var(--ag-muted);font-size:.9rem;line-height:1.55}
.__P__ .ag-ms{margin-top:96px;display:grid;grid-template-columns:1fr 1fr;gap:70px}
.__P__ .ag-ms h2{margin:0 0 22px;font-size:1.7rem;font-weight:800;letter-spacing:-.02em}
.__P__ .ag-it{display:flex;gap:18px;padding:20px 0;border-top:1px solid var(--ag-line)}
.__P__ .ag-it:last-of-type{border-bottom:1px solid var(--ag-line)}
.__P__ .ag-it strong{flex:none;min-width:84px;font-size:1.6rem;font-weight:800;letter-spacing:-.03em;color:var(--ag-gold-hi);line-height:1.1}
.__P__ .ag-it b{display:block;margin-bottom:4px}
.__P__ .ag-it p{margin:0;color:var(--ag-muted);line-height:1.6;font-size:.96rem}
.__P__ .ag-note{margin:18px 0 0;font-size:.82rem;color:var(--ag-muted)}
.__P__ .ag-phi{margin:0;padding:0;list-style:none;display:grid;gap:0}
.__P__ .ag-phi li{padding:20px 0;border-top:1px solid var(--ag-line)}
.__P__ .ag-phi li:last-child{border-bottom:1px solid var(--ag-line)}
.__P__ .ag-phi b{display:block;font-size:1.1rem;margin-bottom:4px}
.__P__ .ag-phi p{margin:0;color:var(--ag-muted);line-height:1.6;font-size:.98rem}
.__P__ .ag-quote{margin-top:96px;text-align:left;font-size:clamp(1.6rem,2.4vw + .8rem,3rem);font-weight:800;letter-spacing:-.03em;line-height:1.12;max-width:20ch}
.__P__ .ag-quote em{font-style:normal;color:var(--ag-gold);text-shadow:0 0 30px rgba(240,185,62,.35)}
@media (max-width:1000px){.__P__ ol.ag-jl{grid-template-columns:1fr 1fr 1fr;gap:26px 0}.__P__ .ag-top{grid-template-columns:1fr;gap:48px}.__P__ .ag-ms{grid-template-columns:1fr;gap:56px}}
@media (max-width:560px){.__P__ ol.ag-jl{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-fig>img{animation:none}}
''',f'''
<section class="__P__" id="__P__" aria-label="About Azeez Gazalle">
  <div class="ag-glow" style="left:-10%;top:0;width:50vw;height:50vw;max-width:700px;max-height:700px"></div>
  <div class="ag-wrap">
    <div class="ag-top">
      <div class="ag-fig" data-r>
        <div class="ag-arch"><div class="ag-ph"><b>Portrait placeholder</b><span>Replace with your photo (PHOTO_URL)</span></div><img class="ag-photo" id="ag-abt-photo" alt="Azeez Gazalle" hidden></div>
        <img data-em="Sparkles|sparkles" alt=""><img data-em="Keyboard|keyboard" alt="">
      </div>
      <div class="ag-prose">
        <div class="ag-eye" data-r>The short version</div>
        <h2 class="ag-h2" data-r style="--i:1">I'm Azeez, a web designer and developer who started in <em>graphic design</em>.</h2>
        <p data-r style="--i:2;margin-top:26px">My journey into digital design and development began with graphic design, where I learned how visual communication shapes the way people understand a brand.</p>
        <p data-r style="--i:3">That curiosity moved beyond static visuals. I taught myself Python and built a calculator and a ping-pong game, which introduced me to programming logic and interactive experiences. From there I moved into web development and Figma-based interface design.</p>
        <p data-r style="--i:4">Discovering GoHighLevel changed how I think about the work. Websites, landing pages, funnels, CRM and automation can work together to support a business's whole customer journey. Today I bring design, development and digital strategy together, and I work as an independent professional with clients in Nigeria and abroad.</p>
      </div>
    </div>
    <ol class="ag-jl">{jn}</ol>
    <div class="ag-ms">
      <div data-r>
        <h2>Experience so far</h2>
        <div class="ag-it"><strong>6+</strong><div><b>Business websites built</b><p>Platforms that help businesses present their brand, services and value online.</p></div></div>
        <div class="ag-it"><strong>5+</strong><div><b>Landing pages developed</b><p>Focused pages that communicate an offer clearly and guide visitors to one action.</p></div></div>
        <div class="ag-it"><strong>3-4</strong><div><b>Years designing and building</b><p>Across graphic design, Python fundamentals, web development, Figma and GoHighLevel.</p></div></div>
        <p class="ag-note">Self-reported figures. Sales funnels are also part of my work.</p>
      </div>
      <div data-r style="--i:1">
        <h2>How I approach the work</h2>
        <ul class="ag-phi">
          <li><b>Design with intention</b><p>Every layout, visual element and interaction should contribute to one coherent experience.</p></li>
          <li><b>Build for functionality</b><p>A site should work reliably on every device and make it easy to navigate and take action.</p></li>
          <li><b>Think beyond the page</b><p>Websites, funnels and connected systems belong to a wider customer journey.</p></li>
        </ul>
      </div>
    </div>
    <p class="ag-quote" data-r>Thoughtful design. Functional development. <em>Built with purpose.</em></p>
  </div>
</section>
''','''
  var PHOTO_URL='';
  if(PHOTO_URL){var im=document.getElementById('ag-abt-photo');im.src=PHOTO_URL;im.hidden=false;root.querySelector('.ag-ph').style.display='none';}
''','(About page) ')
print('built')
