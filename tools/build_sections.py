# Generates the v4 content sections (each output file is fully self-contained for a GHL code block)
import os, json
OUT='/home/claude/azeez-portfolio/sections'
FONT='''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">
'''
def base(p):  # fallback tokens + shared rules for a section with class prefix p
    return f'''
  .{p}{{--ag-bg:#060607;--ag-surface:#0e0e10;--ag-surface-2:#151518;--ag-line:rgba(255,255,255,.1);--ag-text:#f3eee3;--ag-muted:#a8a193;--ag-gold:#e5b040;--ag-gold-ink:#1a1204;
    position:relative;background:var(--ag-bg);color:var(--ag-text);font-family:'Figtree',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;padding:96px 24px;box-sizing:border-box;overflow:hidden}}
  .{p} *,.{p} *::before,.{p} *::after{{box-sizing:border-box}}
  .{p}__wrap{{max-width:1248px;margin:0 auto}}
  .{p}__head{{max-width:720px;margin-bottom:48px}}
  .{p}__kick{{display:inline-flex;align-items:center;gap:10px;padding:7px 16px 7px 8px;border:1px solid var(--ag-line);border-radius:999px;font-size:.86rem;color:var(--ag-muted);background:rgba(255,255,255,.03)}}
  .{p}__kick img{{width:26px;height:26px}}
  .{p}__title{{margin:20px 0 0;font-weight:800;letter-spacing:-.03em;line-height:1.06;font-size:clamp(2rem,2.6vw + 1rem,3.4rem)}}
  .{p}__title em{{font-style:normal;color:var(--ag-gold)}}
  .{p}__lead{{margin:16px 0 0;font-size:1.1rem;line-height:1.6;color:var(--ag-muted);max-width:56ch}}
  .{p}.ag-pre [data-r]{{opacity:0;filter:blur(8px);transform:translateY(22px)}}
  .{p} [data-r]{{transition:opacity .8s cubic-bezier(.2,.7,.2,1),filter .8s cubic-bezier(.2,.7,.2,1),transform .8s cubic-bezier(.2,.7,.2,1);transition-delay:calc(var(--i,0) * 80ms)}}
  .{p}.ag-pre [data-r].ag-in{{opacity:1;filter:none;transform:none}}
  @media (max-width:700px){{.{p}{{padding:68px 20px}}}}
  @media (prefers-reduced-motion:reduce){{.{p}.ag-pre [data-r]{{opacity:1;filter:none;transform:none}}.{p} [data-r]{{transition:none}}}}
'''
def js(p, body=''):
    return f'''
<script>
(function(){{
  var root=document.getElementById('{p}'); if(!root||root.getAttribute('data-ag-init')) return; root.setAttribute('data-ag-init','1');
  var BASE='https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@main/assets/';
  function em(scope){{var im=(scope||root).querySelectorAll('img[data-em]');for(var i=0;i<im.length;i++){{if(im[i].getAttribute('src'))continue;var p=im[i].getAttribute('data-em').split('|');im[i].onerror=function(){{this.style.visibility='hidden'}};im[i].src=(window.AGE&&window.AGE[p[0]])||(BASE+encodeURIComponent(p[0])+'/3D/'+p[1]+'_3d.png');}}}}
  {body}
  em();
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var els=root.querySelectorAll('[data-r]');
  if('IntersectionObserver' in window&&!reduce){{
    root.className+=' ag-pre';
    var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('ag-in');io.unobserve(e.target);}}}});}},{{threshold:.12,rootMargin:'0px 0px -6% 0px'}});
    for(var i=0;i<els.length;i++)io.observe(els[i]);
    setTimeout(function(){{for(var i=0;i<els.length;i++)els[i].classList.add('ag-in');}},6000);
  }}
  /* 3D tilt on cards */
  var fine=window.matchMedia&&window.matchMedia('(pointer:fine)').matches;
  if(fine&&!reduce){{
    var cards=root.querySelectorAll('[data-tilt]');
    cards.forEach(function(c){{
      c.addEventListener('mousemove',function(e){{var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
        c.style.transform='perspective(900px) rotateY('+(x*10).toFixed(2)+'deg) rotateX('+(-y*10).toFixed(2)+'deg) translateY(-4px)';}});
      c.addEventListener('mouseleave',function(){{c.style.transform='';}});
    }});
  }}
}})();
</script>
'''
def kick(emj, text): return f'<div class="{{p}}__kick" data-r><img data-em="{emj}" alt=""><span>{text}</span></div>'
def write(name, html):
    open(os.path.join(OUT,name),'w').write(html)

# ---------------- TOOLS MARQUEE ----------------
p='ag-tools'
tools1=['HTML','CSS','JavaScript','React','Supabase','Vercel','GoHighLevel','Make','Figma','GitHub']
def row(items,rev=False):
    s=''.join(f'<span class="ag-tools__pill">{t}</span>' for t in items)
    return f'<div class="ag-tools__row{" ag-rev" if rev else ""}"><div class="ag-tools__track">{s}{s}{s}{s}</div></div>'
html=f'''<!-- ========== AG SECTION: tools-marquee (Home, under the hero) ========== -->
{FONT}<style>{base(p)}
  .{p}{{padding:28px 0 28px;border-top:1px solid var(--ag-line);border-bottom:1px solid var(--ag-line)}}
  .{p}__label{{text-align:center;margin:0 0 18px;font-size:.84rem;font-weight:600;color:var(--ag-muted)}}
  .{p}__row{{overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent)}}
  .{p}__row+.{p}__row{{margin-top:12px}}
  .{p}__track{{display:flex;gap:12px;width:max-content;animation:ag-tools-run 38s linear infinite}}
  .{p}__row.ag-rev .{p}__track{{animation-direction:reverse;animation-duration:46s}}
  .{p}__pill{{flex:none;padding:13px 26px;border:1px solid var(--ag-line);border-radius:999px;background:var(--ag-surface);font-weight:700;font-size:1.02rem;letter-spacing:-.01em}}
  @keyframes ag-tools-run{{to{{transform:translateX(-25%)}}}}
  .{p}__row:hover .{p}__track{{animation-play-state:paused}}
  @media (prefers-reduced-motion:reduce){{.{p}__track{{animation:none}}}}
</style>
<section class="{p}" id="{p}" aria-label="Tools I build with">
  <p class="{p}__label">The stack I build with</p>
  {row(tools1)}
  {row(list(reversed(tools1)),True)}
</section>
<script>(function(){{var r=document.getElementById('{p}');if(r)r.setAttribute('data-ag-init','1');}})();</script>
'''
write('home-tools-marquee.html', html)

# ---------------- WORK ----------------
p='ag-work'
html=f'''<!-- ========== AG SECTION: home-work (Home page) ==========
     Fill the PROJECTS list with your real projects. Until then three "coming soon" cards show. -->
{FONT}<style>{base(p)}
  .{p}__grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
  .{p}__card{{display:flex;flex-direction:column;border:1px solid var(--ag-line);border-radius:22px;background:var(--ag-surface);overflow:hidden;text-decoration:none;color:inherit;transition:transform .25s ease-out,border-color .25s;transform-style:preserve-3d;will-change:transform}}
  .{p}__card:hover{{border-color:rgba(229,176,64,.55)}}
  .{p}__shot{{position:relative;aspect-ratio:16/10;background:linear-gradient(145deg,#17140e,#0b0b0c);display:grid;place-items:center;overflow:hidden;border-bottom:1px solid var(--ag-line)}}
  .{p}__shot img.ag-shot{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top}}
  .{p}__shot .ag-emo{{width:34%;filter:drop-shadow(0 16px 16px rgba(0,0,0,.55));animation:ag-work-float 6s ease-in-out infinite;transform:translateZ(40px)}}
  @keyframes ag-work-float{{0%,100%{{transform:translateY(0) rotate(-5deg)}}50%{{transform:translateY(-10px) rotate(5deg)}}}}
  .{p}__tag{{position:absolute;left:14px;top:14px;padding:6px 12px;border-radius:999px;background:rgba(6,6,7,.8);border:1px solid var(--ag-line);font-size:.78rem;font-weight:700}}
  .{p}__body{{padding:22px 22px 24px}}
  .{p}__body h3{{margin:0;font-size:1.3rem;font-weight:800;letter-spacing:-.02em}}
  .{p}__body p{{margin:8px 0 0;color:var(--ag-muted);font-size:.98rem;line-height:1.55}}
  .{p}__more{{display:inline-flex;margin-top:16px;color:var(--ag-gold);font-weight:700;font-size:.94rem}}
  .{p}__all{{margin-top:36px;display:flex;justify-content:center}}
  .{p}__btn{{display:inline-flex;align-items:center;gap:10px;padding:15px 26px;border-radius:14px;border:1px solid rgba(255,255,255,.18);color:var(--ag-text);text-decoration:none;font-weight:700;transition:border-color .2s,transform .2s}}
  .{p}__btn:hover{{border-color:var(--ag-gold);transform:translateY(-2px)}}
  @media (max-width:980px){{.{p}__grid{{grid-template-columns:1fr 1fr}}}}
  @media (max-width:640px){{.{p}__grid{{grid-template-columns:1fr}}}}
</style>
<section class="{p}" id="{p}" aria-label="Selected work">
  <div class="{p}__wrap">
    <div class="{p}__head">
      <div class="{p}__kick" data-r><img data-em="Trophy|trophy" alt=""><span>Selected work</span></div>
      <h2 class="{p}__title" data-r style="--i:1">Websites and funnels <em>built to perform</em>.</h2>
      <p class="{p}__lead" data-r style="--i:2">A few recent projects. Each one has a short case study: the problem, what I built, and the result.</p>
    </div>
    <div class="{p}__grid" id="{p}-grid"></div>
    <div class="{p}__all" data-r><a class="{p}__btn" data-ag-link="work" href="/projects">See all projects <span aria-hidden="true">&rarr;</span></a></div>
  </div>
</section>
''' + js(p, '''
  /* ---------- CONFIG ---------- */
  var LINKS={ work:'/projects' };
  /* Add your projects here. image = screenshot URL. */
  var PROJECTS=[
    /* { title:'Project name', tag:'Business website', blurb:'One line on what it does and the result.', image:'https://...', url:'/projects/slug' }, */
  ];
  var SOON=[
    {title:'Business website',tag:'Business website',blurb:'Case study coming soon.',emo:'Desktop computer|desktop_computer'},
    {title:'Sales funnel',tag:'Sales funnel',blurb:'Case study coming soon.',emo:'Rocket|rocket'},
    {title:'Web application',tag:'Web application',blurb:'Case study coming soon.',emo:'Gear|gear'}
  ];
  /* ---------------------------- */
  var grid=document.getElementById('ag-work-grid'), list=PROJECTS.length?PROJECTS:SOON;
  list.forEach(function(x,i){
    var a=document.createElement(x.url?'a':'div'); a.className='ag-work__card'; a.setAttribute('data-r','');a.setAttribute('data-tilt','');a.style.setProperty('--i',i);
    if(x.url)a.href=x.url;
    var shot=x.image?'<img class="ag-shot" loading="lazy" alt="" src="'+x.image+'">':'<img class="ag-emo" data-em="'+x.emo+'" alt="">';
    a.innerHTML='<div class="ag-work__shot">'+shot+'<span class="ag-work__tag">'+x.tag+'</span></div><div class="ag-work__body"><h3>'+x.title+'</h3><p>'+x.blurb+'</p>'+(x.url?'<span class="ag-work__more">View case study &rarr;</span>':'')+'</div>';
    grid.appendChild(a);
  });
  var al=root.querySelectorAll('[data-ag-link]');for(var j=0;j<al.length;j++){var k=al[j].getAttribute('data-ag-link');if(LINKS[k])al[j].setAttribute('href',LINKS[k]);}
''')
write('home-work.html', html)

# ---------------- PROCESS ----------------
p='ag-process'
steps=[('Discovery','1 to 2 business days','We talk about your business, goals, audience, features, budget and timeline, then define the scope.','Speech balloon|speech_balloon'),
('Proposal & kickoff','1 to 3 business days','You get a tailored proposal with deliverables, price, timeline and payment terms. Work starts once it is approved and the first payment is in.','Envelope|envelope'),
('Structure & design','3 to 7 business days','I plan the page structure, user journey and visual direction. You review and give feedback before development.','Artist palette|artist_palette'),
('Development','3 to 15+ business days','The approved design becomes responsive pages, forms, integrations and the features in scope.','Laptop|laptop'),
('Testing & revisions','2 to 5 business days','I test across screen sizes, check forms and integrations, and fix issues in scope. You get revision rounds to refine the result.','Magic wand|magic_wand'),
('Launch & handover','1 to 2 business days','Final payment, launch, domain connection where applicable, final checks, and a handover with access details and guidance.','Rocket|rocket')]
cards=''.join(f'<li class="ag-process__step" data-r data-tilt style="--i:{i}"><div class="ag-process__top"><img data-em="{e}" alt=""><span class="ag-process__n">0{i+1}</span></div><h3>{t}</h3><span class="ag-process__time">{tm}</span><p>{d}</p></li>' for i,(t,tm,d,e) in enumerate(steps))
html=f'''<!-- ========== AG SECTION: process (Home and Services) ========== -->
{FONT}<style>{base(p)}
  .{p}__list{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
  .{p}__step{{padding:26px;border:1px solid var(--ag-line);border-radius:22px;background:var(--ag-surface);transition:transform .25s ease-out,border-color .25s;will-change:transform}}
  .{p}__step:hover{{border-color:rgba(229,176,64,.5)}}
  .{p}__top{{display:flex;align-items:flex-start;justify-content:space-between}}
  .{p}__top img{{width:68px;height:68px;filter:drop-shadow(0 12px 12px rgba(0,0,0,.5))}}
  .{p}__n{{font-weight:800;font-size:1rem;color:var(--ag-gold)}}
  .{p}__step h3{{margin:18px 0 0;font-size:1.3rem;font-weight:800;letter-spacing:-.02em}}
  .{p}__time{{display:inline-block;margin-top:8px;padding:5px 12px;border-radius:999px;background:rgba(229,176,64,.12);color:var(--ag-gold);font-size:.8rem;font-weight:700}}
  .{p}__step p{{margin:14px 0 0;color:var(--ag-muted);line-height:1.6;font-size:.98rem}}
  .{p}__table{{margin-top:28px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}
  .{p}__t{{padding:18px 20px;border:1px solid var(--ag-line);border-radius:16px;background:var(--ag-surface-2)}}
  .{p}__t b{{display:block;font-size:.84rem;color:var(--ag-muted);font-weight:600}}
  .{p}__t span{{display:block;margin-top:6px;font-weight:800;font-size:1.1rem;letter-spacing:-.01em}}
  .{p}__fine{{margin:18px 0 0;color:var(--ag-muted);font-size:.9rem;line-height:1.6;max-width:70ch}}
  @media (max-width:980px){{.{p}__list{{grid-template-columns:1fr 1fr}}.{p}__table{{grid-template-columns:1fr 1fr}}}}
  @media (max-width:640px){{.{p}__list{{grid-template-columns:1fr}}}}
</style>
<section class="{p}" id="{p}" aria-label="How I work">
  <div class="{p}__wrap">
    <div class="{p}__head">
      <div class="{p}__kick" data-r><img data-em="Compass|compass" alt=""><span>How I work</span></div>
      <h2 class="{p}__title" data-r style="--i:1">From first conversation to <em>launch</em>.</h2>
      <p class="{p}__lead" data-r style="--i:2">A clear, collaborative process that keeps things organised and avoids surprises.</p>
    </div>
    <ol class="{p}__list">{cards}</ol>
    <div class="{p}__table" data-r>
      <div class="{p}__t"><b>Landing page</b><span>5 to 10 business days</span></div>
      <div class="{p}__t"><b>Business website</b><span>2 to 3 weeks</span></div>
      <div class="{p}__t"><b>Sales funnel</b><span>2 to 4 weeks</span></div>
      <div class="{p}__t"><b>Web application MVP</b><span>4 to 10+ weeks</span></div>
    </div>
    <p class="{p}__fine" data-r>Timelines begin once the project is approved, the first payment is received and the required materials are available. Complex features or scope changes can extend delivery. Your exact timeline is confirmed in your proposal.</p>
  </div>
</section>
''' + js(p)
write('process.html', html)

# ---------------- PRICING ----------------
p='ag-price'
plans=[('Landing Pages','$150','from','One focused page built to get a visitor to act.',['One custom landing page','Responsive, 6 to 8 sections','Call-to-action integration','Basic SEO and agreed tracking'],'Discuss your project','Bullseye|bullseye',False),
('Business Websites','$400','from','A professional site that presents your business online.',['Up to five pages','Contact integration','Basic SEO and analytics','Deployment included'],'Discuss your project','Desktop computer|desktop_computer',True),
('Sales Funnels','$750','from','A scoped funnel that turns visitors into leads and customers.',['Sales or lead-gen page and thank-you page','Form and basic CRM integration','One basic automation workflow','Conversion tracking'],'Discuss your project','Rocket|rocket',False),
('Web Applications','$1,000','custom-scoped from','A custom build for a clearly defined MVP, quoted per project.',['Scoped around your features','Authentication and database as needed','Integrations and security reviewed','Milestone-based payments'],'Get a quote','Gear|gear',False),
('Website Redesign','$300','from','A fresh, faster version of a site you already have.',['Review of your current site','New layout and design','Responsive rebuild','Priced by pages and condition'],'Discuss your project','Artist palette|artist_palette',False),
('Website Maintenance','$75','per month, from','Routine care so your site stays healthy.',['Routine checks and supported updates','Backups where applicable','Minor content changes','Basic technical support'],'Get a quote','Hammer and wrench|hammer_and_wrench',False)]
def card(i,pl):
    n,price,lab,d,inc,cta,e,feat=pl
    li=''.join(f'<li>{x}</li>' for x in inc)
    return f'''<article class="ag-price__card{' ag-feat' if feat else ''}" data-r data-tilt style="--i:{i}">
      <img class="ag-price__emo" data-em="{e}" alt="">
      
      <h3>{n}</h3><p class="ag-price__d">{d}</p>
      <div class="ag-price__amt"><small>{lab}</small><strong>{price}</strong>{'<small>/month</small>' if 'month' in lab else ''}</div>
      <ul>{li}</ul>
      <a class="ag-price__cta" data-ag-link="contact" href="/contact">{cta}</a></article>'''
cards=''.join(card(i,pl) for i,pl in enumerate(plans))
html=f'''<!-- ========== AG SECTION: pricing (Home preview and Services page) ========== -->
{FONT}<style>{base(p)}
  .{p}__grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
  .{p}__card{{position:relative;display:flex;flex-direction:column;padding:30px 28px 28px;border:1px solid var(--ag-line);border-radius:24px;background:var(--ag-surface);transition:transform .25s ease-out,border-color .25s;will-change:transform}}
  .{p}__card:hover{{border-color:rgba(229,176,64,.5)}}
  .{p}__card.ag-feat{{border-color:rgba(229,176,64,.55);background:linear-gradient(180deg,#17130b,#0e0e10 60%)}}
  .{p}__emo{{width:76px;height:76px;filter:drop-shadow(0 14px 12px rgba(0,0,0,.5));margin-bottom:6px}}
  .{p}__badge{{position:absolute;right:22px;top:24px;padding:6px 12px;border-radius:999px;background:var(--ag-gold);color:var(--ag-gold-ink);font-size:.76rem;font-weight:800}}
  .{p}__card h3{{margin:12px 0 0;font-size:1.4rem;font-weight:800;letter-spacing:-.02em}}
  .{p}__d{{margin:8px 0 0;color:var(--ag-muted);line-height:1.55;font-size:.98rem;min-height:3.1em}}
  .{p}__amt{{margin-top:20px;display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}}
  .{p}__amt strong{{font-size:2.5rem;font-weight:800;letter-spacing:-.04em;line-height:1}}
  .{p}__amt small{{color:var(--ag-muted);font-size:.86rem;font-weight:600}}
  .{p}__card ul{{list-style:none;margin:20px 0 26px;padding:0;display:grid;gap:11px;flex:1}}
  .{p}__card li{{position:relative;padding-left:28px;color:var(--ag-text);font-size:.96rem;line-height:1.45}}
  .{p}__card li::before{{content:"";position:absolute;left:0;top:.2em;width:18px;height:18px;border-radius:50%;background:rgba(229,176,64,.16) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M5 9.4l2.6 2.6L13 6.4' fill='none' stroke='%23e5b040' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/18px no-repeat}}
  .{p}__cta{{display:flex;justify-content:center;padding:15px 20px;border-radius:14px;border:1px solid rgba(255,255,255,.18);color:var(--ag-text);text-decoration:none;font-weight:700;transition:background .2s,border-color .2s,color .2s}}
  .{p}__cta:hover{{border-color:var(--ag-gold);background:rgba(229,176,64,.08)}}
  .{p}__card.ag-feat .{p}__cta{{background:var(--ag-gold);color:var(--ag-gold-ink);border-color:var(--ag-gold)}}
  .{p}__card.ag-feat .{p}__cta:hover{{background:#f2c35c}}
  .{p}__note{{margin:26px 0 0;color:var(--ag-muted);font-size:.92rem;line-height:1.6;max-width:78ch}}
  @media (max-width:1020px){{.{p}__grid{{grid-template-columns:1fr 1fr}}}}
  @media (max-width:660px){{.{p}__grid{{grid-template-columns:1fr}}}}
</style>
<section class="{p}" id="{p}" aria-label="Services and pricing">
  <div class="{p}__wrap">
    <div class="{p}__head">
      <div class="{p}__kick" data-r><img data-em="Money bag|money_bag" alt=""><span>Services and pricing</span></div>
      <h2 class="{p}__title" data-r style="--i:1">Clear starting prices. <em>No guesswork.</em></h2>
      <p class="{p}__lead" data-r style="--i:2">Pick the closest fit. After a short conversation you get a tailored proposal with the final scope, cost and timeline.</p>
    </div>
    <div class="{p}__grid">{cards}</div>
    <p class="{p}__note" data-r>All prices are starting estimates. A tailored proposal confirms the final scope, cost and timeline. Hosting, domain registration, software subscriptions and third-party fees are paid separately unless included in your proposal. Maintenance excludes unlimited development, major redesigns, new features and third-party costs.</p>
  </div>
</section>
''' + js(p, '''
  var LINKS={ contact:'/contact' };
  var al=root.querySelectorAll('[data-ag-link]');for(var j=0;j<al.length;j++){var k=al[j].getAttribute('data-ag-link');if(LINKS[k])al[j].setAttribute('href',LINKS[k]);}
''')
write('pricing.html', html)
print('ok')
