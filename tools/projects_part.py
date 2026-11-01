# Executed from build_v6.py (after sec(), props(), ARROW and PILL_ARROW exist).
# Builds: 00-projects (data + image map), home-work, work-showcase and one case-study page per project.
import json,re
exec(open('/home/claude/azeez-portfolio/tools/projects_data.py').read())
IMGS=json.load(open('/home/claude/azeez-portfolio/tools/project_images.json'))
for p in PROJECTS:
    im=IMGS[p['slug']]; p['cover']=im['cover']; p['shots']=im['shots']
    if p['type']=='website': p['label']='Website'
    else: p['label']='Sales funnel'

# ---------- 00-projects: the one place that holds every project's text and image addresses ----------
data=json.dumps({'filters':FILTERS,'projects':PROJECTS},ensure_ascii=False)
open(os.path.join(OUT,'00-projects.html'),'w').write('''<!-- ========== AG SECTION: 00-projects (paste once on the Home, Work and every Project page, above the other sections) ==========
     All 9 projects in one place: names, descriptions, links and image addresses. The Home projects, the Work page and every case-study page read from it.
     IMAGES: each project has a "cover" and "shots" address. They start as relative paths (assets/projects/...). After you upload the
     images to the GoHighLevel media library, replace each path with its full https address (find and replace works well).
     TEXT: edit the words here once and every page updates. -->
<script>window.AGPROJ='''+data+''';</script>
''')

SHARED_CSS='''
.__P__ .ag-cv{position:relative;display:block;border-radius:22px;overflow:hidden;aspect-ratio:2624/1632;background:#0d0d11;border:1px solid var(--ag-line-2);box-shadow:0 50px 90px -40px rgba(0,0,0,.75),0 0 90px -30px rgba(240,185,62,.3)}
.__P__ .ag-cv img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;transition:transform 1.1s cubic-bezier(.2,.7,.2,1)}
'''

# ---------- HOME: sticky stack of featured projects ----------
sec('home-work','ag-hwork',SHARED_CSS+'''
.__P__{padding-bottom:140px}
.__P__ .ag-stack{margin-top:60px}
.__P__ .ag-card{position:sticky;top:calc(92px + var(--k) * 28px);margin-bottom:6vh;border-radius:34px;border:1.5px solid var(--ag-bd-hi);background:var(--ag-card);padding:22px;box-shadow:0 -20px 50px -20px rgba(0,0,0,.5),0 0 0 6px var(--ag-bg),0 0 0 7.5px var(--ag-line)}
.__P__ .ag-ch{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:6px 10px 18px}
.__P__ .ag-no{font-weight:900;font-size:clamp(1.8rem,3vw,3rem);letter-spacing:-.05em;line-height:1}
.__P__ .ag-ct{display:flex;align-items:center;gap:20px;min-width:0}
.__P__ .ag-ct small{display:block;font-size:.68rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ .ag-ct b{display:block;font-size:1.05rem;letter-spacing:-.01em}
.__P__ .ag-lv{flex:none;padding:12px 22px;border-radius:999px;border:1.5px solid var(--ag-bd-hi);color:var(--ag-text);font-size:.72rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;transition:background .25s,color .25s,border-color .25s}
.__P__ a.ag-lv:hover{background:var(--ag-gold);color:var(--ag-gold-ink);border-color:var(--ag-gold)}
.__P__ .ag-imgs{display:grid;grid-template-columns:1.6fr 1fr;grid-template-rows:1fr 1fr;gap:14px;height:clamp(240px,38vw,440px)}
.__P__ .ag-im{position:relative;border-radius:22px;overflow:hidden;border:1px solid var(--ag-bd-soft);background:#0d0d11}
.__P__ .ag-im:first-child{grid-row:1/3}
.__P__ .ag-im img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.__P__ .ag-im:first-child img{object-position:center}
.__P__ .ag-all{margin-top:48px;display:flex;justify-content:center}
@media (max-width:760px){.__P__ .ag-card{padding:14px;border-radius:26px;top:calc(76px + var(--k) * 18px)}.__P__ .ag-imgs{grid-template-columns:1fr;grid-template-rows:auto;height:auto}.__P__ .ag-im{aspect-ratio:16/10}.__P__ .ag-im:first-child{grid-row:auto}.__P__ .ag-im:nth-child(n+2){display:none}.__P__ .ag-ct{gap:12px}.__P__ .ag-lv{padding:12px 16px}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-card{position:relative;top:0}}
''',f'''
<section class="__P__" id="__P__" aria-label="Selected work">
  {props([('Trophy|trophy','80%','1%','10vw',1.6,-8,8,6,0),('Sparkles|sparkles','4%','7%','7vw',1.2,8,-8,7,-2)])}
  <div class="ag-wrap">
    <h2 class="ag-big" data-fill>Projects</h2>
    <p class="ag-lead" data-r style="margin-top:22px">A few recent builds. Each one has a full case study with the goal, my role and the decisions behind it.</p>
    <div class="ag-stack" id="__P__-stack"></div>
    <div class="ag-all" data-r><a class="ag-pill" data-ag-link="work" href="/work">See all {len(PROJECTS)} projects {PILL_ARROW}</a></div>
  </div>
</section>
''',r'''
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  var D=window.AGPROJ, host=document.getElementById('ag-hwork-stack');
  if(!D){host.innerHTML='<p style="color:#b9b1a1">Add the 00-projects block above this section to show your projects.</p>';}
  else{
    var all=D.projects, list=all.filter(function(p){return p.featured;}).slice(0,4);
    list.forEach(function(p,i){
      var n=all.indexOf(p)+1;
      var cells='<div class="ag-im"><img loading="lazy" alt="'+esc(p.name)+' website mockup" src="'+esc(p.cover)+'"></div>';
      for(var k=0;k<2;k++){ if(p.shots[k]) cells+='<div class="ag-im"><img loading="lazy" alt="'+esc(p.name)+' screenshot '+(k+1)+'" src="'+esc(p.shots[k])+'"></div>'; }
      var a=document.createElement('article'); a.className='ag-card'; a.style.setProperty('--k',i);
      a.innerHTML='<div class="ag-ch"><div class="ag-ct"><span class="ag-no">0'+n+'</span><div><small>'+esc(p.category)+'</small><b>'+esc(p.name)+' <span style="color:#b9b1a1;font-weight:600">&middot; '+esc(p.industry)+'</span></b></div></div><a class="ag-lv" href="/work/'+esc(p.slug)+'">Case study</a></div><div class="ag-imgs">'+cells+'</div>';
      host.appendChild(a);
    });
  }
''','(Home) ')

# ---------- WORK PAGE: filter + list ----------
sec('work-showcase','ag-wshow',SHARED_CSS+'''
.__P__ .ag-fb{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 56px}
.__P__ .ag-fb button{appearance:none;cursor:pointer;padding:12px 22px;min-height:44px;border-radius:999px;border:1px solid var(--ag-line-2);background:transparent;color:var(--ag-text);font:700 .92rem/1 'Figtree',sans-serif;transition:background .25s,color .25s,border-color .25s}
.__P__ .ag-fb button:hover{border-color:var(--ag-gold)}
.__P__ .ag-fb button[aria-pressed="true"]{background:var(--ag-gold);color:var(--ag-gold-ink);border-color:var(--ag-gold)}
.__P__ .ag-fb span{opacity:.7;margin-left:6px;font-weight:600}
.__P__ .ag-proj{position:relative;margin:0 0 110px;display:grid;grid-template-columns:repeat(12,1fr);gap:28px 32px;align-items:center}
.__P__ .ag-proj:last-of-type{margin-bottom:0}
.__P__ .ag-mock{grid-column:1/8;position:relative;transition:transform .3s ease-out;transform-style:preserve-3d;will-change:transform;text-decoration:none;color:inherit}
.__P__ .ag-proj.ag-alt .ag-mock{grid-column:6/13;grid-row:1}
.__P__ .ag-proj.ag-alt .ag-meta{grid-column:1/6;grid-row:1}
.__P__ .ag-meta{grid-column:8/13}
.__P__ .ag-proj.ag-feat .ag-mock{grid-column:1/13}
.__P__ .ag-proj.ag-feat .ag-meta{grid-column:1/13;display:grid;grid-template-columns:repeat(12,1fr);gap:28px 32px}
.__P__ .ag-proj.ag-feat .ag-m1{grid-column:1/6}.__P__ .ag-proj.ag-feat .ag-m2{grid-column:6/13}
.__P__ .ag-mock:hover .ag-cv img{transform:scale(1.04)}
.__P__ .ag-tag{position:absolute;left:16px;top:16px;z-index:2;padding:7px 14px;border-radius:999px;background:var(--ag-gold);color:var(--ag-gold-ink);font-size:.7rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.__P__ .ag-no{font-weight:800;font-size:clamp(3.4rem,5vw,5.6rem);line-height:.9;letter-spacing:-.05em;color:transparent;-webkit-text-stroke:1.5px rgba(240,185,62,.7)}
.__P__ .ag-cat{margin:14px 0 0;font-size:.8rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ .ag-meta h3{margin:8px 0 0;font-size:clamp(1.6rem,1.4vw + 1rem,2.4rem);font-weight:800;letter-spacing:-.03em;line-height:1.1}
.__P__ .ag-ind{margin:6px 0 0;color:var(--ag-muted);font-size:1rem}
.__P__ .ag-sum{margin:18px 0 0;line-height:1.65;font-size:1.05rem}
.__P__ .ag-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}
.__P__ .ag-chips span{padding:6px 14px;border-radius:999px;border:1px solid var(--ag-line);font-size:.86rem;background:rgba(255,255,255,.03)}
.__P__ .ag-links{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.__P__ dl{margin:22px 0 0;display:grid;gap:16px}
.__P__ dt{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ dd{margin:4px 0 0;line-height:1.6;font-size:1rem}
@media (max-width:980px){
  .__P__ .ag-proj,.__P__ .ag-proj.ag-feat .ag-meta{display:flex;flex-direction:column;align-items:stretch;gap:26px;margin-bottom:76px}
  .__P__ .ag-mock,.__P__ .ag-meta{width:100%}
}
''',f'''
<section class="__P__" id="__P__" aria-label="Selected work">
  <div class="ag-glow" style="right:-12%;top:20%;width:50vw;height:50vw;max-width:700px;max-height:700px"></div>
  <div class="ag-wrap"><div class="ag-fb" id="__P__-fb" role="group" aria-label="Filter projects"></div><div id="__P__-list" aria-live="polite"></div><noscript><p style="color:#b9b1a1">Enable JavaScript to see the project showcase.</p></noscript></div>
</section>
''',r'''
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  var D=window.AGPROJ, host=document.getElementById('ag-wshow-list'), fb=document.getElementById('ag-wshow-fb'), ARW='__ARROW__';
  function draw(f){
    host.innerHTML='';
    var all=D.projects, shown=all.filter(function(p){return f==='all'||p.type===f;});
    shown.forEach(function(p,i){
      var n=all.indexOf(p)+1, feat=(i===0), alt=(!feat&&i%2===1), href='/work/'+p.slug;
      var mock='<a class="ag-mock" href="'+href+'" aria-label="Read the '+esc(p.name)+' case study" data-r data-tilt="4"><span class="ag-tag">'+esc(p.label)+'</span><span class="ag-cv"><img '+(i<2?'':'loading="lazy" ')+'alt="'+esc(p.name)+(p.type==='website'?' website':' sales funnel')+' mockup on desktop and mobile screens" src="'+esc(p.cover)+'"></span></a>';
      var chips=p.tools.slice(0,5).map(function(t){return '<span>'+esc(t)+'</span>';}).join('');
      var head='<div class="ag-no">0'+n+'</div><p class="ag-cat">'+esc(p.category)+'</p><h3>'+esc(p.name)+'</h3><p class="ag-ind">'+esc(p.industry)+' &middot; '+esc(p.date)+'</p>';
      var btns='<a class="ag-btn ag-btn--gold" href="'+href+'">View case study '+ARW+'</a>'+(p.live?'<a class="ag-btn ag-btn--ghost" target="_blank" rel="noopener" href="'+esc(p.live)+'">'+esc(p.liveLabel||'Visit live site')+'</a>':'');
      var l1='<p class="ag-sum">'+esc(p.summary)+'</p><dl><div><dt>Objective</dt><dd>'+esc(p.objective)+'</dd></div></dl>';
      var l2='<dl><div><dt>My role</dt><dd>'+esc(p.role)+'</dd></div></dl><div class="ag-chips">'+chips+'</div><div class="ag-links">'+btns+'</div>';
      var meta=feat?'<div class="ag-meta" data-r><div class="ag-m1">'+head+l1+'</div><div class="ag-m2">'+l2+'</div></div>':'<div class="ag-meta" data-r style="--i:1">'+head+l1+l2+'</div>';
      var art=document.createElement('article'); art.className='ag-proj'+(feat?' ag-feat':'')+(alt?' ag-alt':'');
      art.innerHTML=mock+meta; host.appendChild(art);
    });
    links(host); reveal(host); tilt(host);
  }
  if(!D){host.innerHTML='<p style="color:#b9b1a1">Add the 00-projects block above this section to show your projects.</p>';}
  else{
    D.filters.forEach(function(f,i){
      var c=f[0]==='all'?D.projects.length:D.projects.filter(function(p){return p.type===f[0];}).length;
      var b=document.createElement('button'); b.type='button'; b.setAttribute('aria-pressed',i===0?'true':'false'); b.innerHTML=esc(f[1])+'<span>'+c+'</span>';
      b.addEventListener('click',function(){ var all=fb.querySelectorAll('button'); for(var q=0;q<all.length;q++)all[q].setAttribute('aria-pressed','false'); b.setAttribute('aria-pressed','true'); draw(f[0]); });
      fb.appendChild(b);
    });
    draw('all');
  }
'''.replace('__ARROW__',ARROW.replace("'","\\'")),'(Work page) ')

# ---------- ONE CASE-STUDY PAGE PER PROJECT ----------
PJ_CSS=SHARED_CSS+'''
.__P__{padding:150px 24px 90px}
.__P__ .ag-back{display:inline-flex;gap:8px;align-items:center;color:var(--ag-muted);text-decoration:none;font-weight:600;font-size:.92rem;margin-bottom:28px;min-height:44px}
.__P__ .ag-back:hover{color:var(--ag-gold-t)}
.__P__ h1{margin:12px 0 0;font-weight:800;letter-spacing:-.035em;line-height:1.05;font-size:clamp(2.2rem,3.2vw + 1rem,4.4rem);max-width:18ch}
.__P__ .ag-lead{max-width:60ch}
.__P__ .ag-facts{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin:44px 0;border-top:1px solid var(--ag-line);border-bottom:1px solid var(--ag-line)}
.__P__ .ag-facts div{padding:22px 20px 22px 0}
.__P__ dt{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ag-muted)}
.__P__ dd{margin:6px 0 0;font-weight:600;line-height:1.5}
.__P__ .ag-chips{display:flex;flex-wrap:wrap;gap:6px}
.__P__ .ag-chips span{padding:4px 12px;border-radius:999px;border:1px solid var(--ag-line);font-size:.82rem;font-weight:600}
.__P__ .ag-hero-cv{display:block;position:relative}
.__P__ .ag-links{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px}
.__P__ .ag-body{display:grid;grid-template-columns:.8fr 1.2fr;gap:44px 70px;margin-top:84px}
.__P__ .ag-body h2{margin:0;font-size:1.5rem;font-weight:800;letter-spacing:-.02em}
.__P__ .ag-body p,.__P__ .ag-body li{color:var(--ag-muted);line-height:1.75;font-size:1.05rem;margin:0}
.__P__ .ag-body ul{margin:0;padding-left:20px;display:grid;gap:10px}
.__P__ .ag-lay{position:relative;margin-top:96px;perspective:1600px}
.__P__ .ag-lay-in{position:relative;aspect-ratio:16/8.6;transform-style:preserve-3d}
.__P__ .ag-win{position:absolute;border-radius:16px;overflow:hidden;border:1px solid var(--ag-line-2);background:#0d0d11;box-shadow:0 40px 70px -30px rgba(0,0,0,.85),0 0 70px -30px rgba(240,185,62,.3);transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-win img{display:block;width:100%;height:auto}
.__P__ .ag-win .ag-wb{display:flex;gap:6px;padding:8px 12px;background:#131318;border-bottom:1px solid rgba(255,255,255,.1)}
.__P__ .ag-win .ag-wb i{width:8px;height:8px;border-radius:50%;background:#34343c}
.__P__ .ag-w1{width:50%;left:1%;top:14%;transform:rotateY(9deg) rotateZ(-2deg);z-index:1}
.__P__ .ag-w2{width:56%;left:22%;top:0;z-index:3}
.__P__ .ag-w3{width:48%;right:1%;top:22%;transform:rotateY(-9deg) rotateZ(2deg);z-index:2}
.__P__ .ag-lay-in:hover .ag-w1{transform:rotateY(5deg) rotateZ(-1deg) translateX(-1%)}
.__P__ .ag-lay-in:hover .ag-w3{transform:rotateY(-5deg) rotateZ(1deg) translateX(1%)}
.__P__ .ag-fun .ag-w1{transform:rotateY(-9deg) rotateZ(2deg);left:auto;right:1%;width:50%}
.__P__ .ag-fun .ag-w3{transform:rotateY(9deg) rotateZ(-2deg);right:auto;left:1%;width:48%}
.__P__ .ag-gal{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:96px}
.__P__ .ag-gal figure{margin:0;border-radius:18px;overflow:hidden;border:1px solid var(--ag-line-2);background:#0d0d11;cursor:zoom-in}
.__P__ .ag-gal figure:first-child{grid-column:1/-1}
.__P__ .ag-gal img{display:block;width:100%;height:auto;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.__P__ .ag-gal figure:hover img{transform:scale(1.03)}
.__P__ .ag-gal figcaption{padding:12px 16px;color:var(--ag-muted);font-size:.84rem;border-top:1px solid var(--ag-line)}
.__P__ .ag-gh{margin:96px 0 0;font-size:1.5rem;font-weight:800;letter-spacing:-.02em}
.__P__ .ag-gal{margin-top:28px}
.__P__ .ag-next{margin-top:90px;padding-top:36px;border-top:1px solid var(--ag-line);display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;align-items:center}
.__P__ .ag-next b{font-size:clamp(1.4rem,1.5vw + 1rem,2.2rem);letter-spacing:-.02em}
.__P__ .ag-next a.ag-nx{color:inherit;text-decoration:none}
.__P__ .ag-lb{position:fixed;inset:0;z-index:2147482000;background:rgba(5,5,7,.92);display:none;align-items:center;justify-content:center;padding:24px;cursor:zoom-out}
.__P__ .ag-lb.ag-on{display:flex}
.__P__ .ag-lb img{max-width:100%;max-height:100%;border-radius:12px;box-shadow:0 30px 90px rgba(0,0,0,.7)}
@media (max-width:900px){.__P__{padding:120px 20px 70px}.__P__ .ag-facts{grid-template-columns:1fr 1fr}.__P__ .ag-body{grid-template-columns:1fr;gap:18px;margin-top:56px}.__P__ .ag-body h2:not(:first-child){margin-top:26px}.__P__ .ag-gal{grid-template-columns:1fr}.__P__ .ag-lay{margin-top:64px}.__P__ .ag-win .ag-wb{display:none}.__P__ .ag-w1{width:60%;top:10%}.__P__ .ag-w3{width:56%;top:26%}}
@media (prefers-reduced-motion:reduce){.__P__ .ag-win,.__P__ .ag-gal img{transition:none}}
'''
PJ_HTML=f'''
<section class="__P__" id="__P__" aria-label="Case study">
  <div class="ag-glow" style="right:-10%;top:0;width:50vw;height:50vw;max-width:720px;max-height:720px"></div>
  <div class="ag-wrap" id="__P__-root"></div>
  <div class="ag-lb" id="__P__-lb" role="dialog" aria-label="Enlarged screenshot"><img alt=""></div>
</section>
'''
PJ_JS=r'''
  var SLUG='__SLUG__', ARW='__ARROW__';
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  var D=window.AGPROJ, host=document.getElementById('__P__-root');
  var all=D?D.projects:[], p=null, idx=-1;
  for(var i=0;i<all.length;i++){if(all[i].slug===SLUG){p=all[i];idx=i;}}
  if(!p){host.innerHTML='<p style="color:#b9b1a1">Add the 00-projects block above this section to show this project.</p>';}
  else{
    document.title=p.name+' | Case study | Azeez Gazalle';
    var nx=all[(idx+1)%all.length], web=(p.type==='website');
    var lis=function(a){return '<ul>'+a.map(function(x){return '<li>'+esc(x)+'</li>';}).join('')+'</ul>';};
    var tools='<div class="ag-chips">'+p.tools.map(function(t){return '<span>'+esc(t)+'</span>';}).join('')+'</div>';
    var s=p.shots, win=function(c,im,n){return im?'<div class="ag-win '+c+'"><div class="ag-wb"><i></i><i></i><i></i></div><img '+(n>0?'loading="lazy" ':'')+'alt="'+esc(p.name)+' screenshot" src="'+esc(im)+'"></div>':'';};
    var lay=(s.length>=3)?'<div class="ag-lay" data-r><div class="ag-lay-in'+(web?'':' ag-fun')+'">'+win('ag-w1',s[1],1)+win('ag-w3',s[2],1)+win('ag-w2',s[0],0)+'</div></div>':'';
    var gal=s.map(function(im,k){return '<figure data-full="'+esc(im)+'"><img loading="lazy" alt="'+esc(p.name)+' screenshot '+(k+1)+' of '+s.length+'" src="'+esc(im)+'"><figcaption>Screenshot '+(k+1)+' of '+s.length+'</figcaption></figure>';}).join('');
    var btns=(p.live?'<a class="ag-btn ag-btn--gold" target="_blank" rel="noopener" href="'+esc(p.live)+'">'+esc(p.liveLabel||'Visit live site')+' '+ARW+'</a>':'')+'<a class="ag-btn ag-btn--ghost" data-ag-link="start" href="/start">Start a similar project</a>';
    host.innerHTML=
      '<a class="ag-back" data-ag-link="work" href="/work">&larr; All work</a>'+
      '<div class="ag-eye" data-r>'+esc(p.category)+'</div>'+
      '<h1 data-r style="--i:1">'+esc(p.name)+'</h1>'+
      '<p class="ag-lead" data-r style="--i:2">'+esc(p.summary)+'</p>'+
      '<dl class="ag-facts" data-r><div><dt>Client</dt><dd>'+esc(p.client)+'</dd></div><div><dt>Industry</dt><dd>'+esc(p.industry)+'</dd></div><div><dt>Date</dt><dd>'+esc(p.date)+'</dd></div><div><dt>Tools</dt><dd>'+tools+'</dd></div></dl>'+
      '<a class="ag-cv ag-hero-cv" data-r><img alt="'+esc(p.name)+(web?' website':' sales funnel')+' mockup on desktop and mobile screens" src="'+esc(p.cover)+'"></a>'+
      '<div class="ag-links" data-r>'+btns+'</div>'+
      '<div class="ag-body" data-r>'+
        '<h2>Overview</h2><p>'+esc(p.context)+'</p>'+
        '<h2>Objective</h2><p>'+esc(p.objective)+'</p>'+
        '<h2>My role</h2><p>'+esc(p.role)+'</p>'+
        '<h2>Approach and key decisions</h2>'+lis(p.approach)+
        '<h2>Deliverables</h2>'+lis(p.deliverables)+
        '<h2>Status</h2><p>'+esc(p.status)+'</p>'+
      '</div>'+lay+
      '<h2 class="ag-gh" data-r>Screens from the project</h2><div class="ag-gal" data-r>'+gal+'</div>'+
      '<div class="ag-next" data-r><div><span style="color:#b9b1a1;font-size:.85rem">Next project</span><br><a class="ag-nx" href="/work/'+esc(nx.slug)+'"><b>'+esc(nx.name)+'</b></a></div><a class="ag-btn ag-btn--ghost" data-ag-link="work" href="/work">Back to all work '+ARW+'</a></div>';
    var lb=document.getElementById('__P__-lb'), lbi=lb.querySelector('img');
    host.querySelectorAll('.ag-gal figure').forEach(function(f){f.addEventListener('click',function(){lbi.src=f.getAttribute('data-full');lb.className='ag-lb ag-on';});});
    lb.addEventListener('click',function(){lb.className='ag-lb';});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.className='ag-lb';});
  }
'''
for p in PROJECTS:
    nm='project-'+p['slug']; NOSHEET.add(nm)
    sec(nm,'ag-pj-'+p['slug'],PJ_CSS,PJ_HTML,PJ_JS.replace('__SLUG__',p['slug']).replace('__ARROW__',ARROW.replace("'","\\'")),'(Project page: /work/%s) '%p['slug'])
