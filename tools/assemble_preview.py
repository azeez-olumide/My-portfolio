# Builds a single-file multi-page preview with a tiny client-side router (for review only; on GHL each page is its own page)
import sys
S='/home/claude/azeez-portfolio/sections/'
def r(n): return open(S+n+'.html').read()
PAGES={
 'home':['home-hero','logo-marquee','home-about','home-services','home-work','home-process','home-testimonials'],
 'work':['page-hero-work','work-showcase'],
 'services':['page-hero-services','services-list','services-terms'],
 'process':['page-hero-process','process-steps','why-me','faq'],
 'about':['page-hero-about','about-story'],
 'contact':['contact-section'],
 'start':['start-form'],
}
import json as _j
SLUGS=list(_j.load(open('/home/claude/azeez-portfolio/tools/project_images.json')).keys())
for _s in SLUGS: PAGES['p-'+_s]=['project-'+_s]
ROUTES={'/':'home','/work':'work','/services':'services','/process':'process','/about':'about','/contact':'contact','/start':'start'}
for _s in SLUGS: ROUTES['/work/'+_s]='p-'+_s
NUMS=['cropzone-africa','nubid-engineering','quietpalm','caliph-engineering','pilgrim-prive','proventa','faucet-water-purifier-funnel','ginseng-five-treasure-tea-funnel','talk-to-ai-like-a-pro','adjustable-laptop-workstation','foldable-hand-fan']
for _i,_s in enumerate(NUMS,1): ROUTES['/project-%d'%_i]='p-'+_s
out=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Azeez Gazalle Portfolio</title><style>html{scroll-behavior:auto}body{margin:0;background:#07070a}[data-page]{display:none}[data-page].on{display:block}</style></head><body>']
import json,re
out.append(r('00-loader'))
out.append(r('00-global'))
out.append(r('00-emoji-pack'))
out.append(r('00-avatars'))
import base64,re as _re
_pj=r('00-projects')
_pj=_re.sub(r'assets/projects/[a-z0-9-]+\.webp',lambda m:'data:image/webp;base64,'+base64.b64encode(open('/home/claude/azeez-portfolio/'+m.group(0),'rb').read()).decode(),_pj)
out.append(_pj)
out.append('<div id="ag-h">'+r('header')+'</div>')
for k,secs in PAGES.items():
    out.append(f'<main data-page="{k}"{" class=on" if k=="home" else ""}>'+''.join(r(s) for s in secs)+'</main>')
out.append('<div id="ag-shared-cta">'+r('home-cta')+'</div>')
out.append('<div id="ag-f">'+r('footer')+'</div>'); out.append('<div id="ag-w">'+r('whatsapp-float')+'</div>')
out.append('''<script>
(function(){
  var R=%s;
  function show(path){
    var h='',p=path;var i=p.indexOf('#');if(i>-1){h=p.slice(i+1);p=p.slice(0,i);}
    p=p.replace(/\\/+$/,'')||'/'; var k=R[p]; if(!k)return false;
    document.querySelectorAll('[data-page]').forEach(function(m){m.classList.toggle('on',m.getAttribute('data-page')===k);});
    var cta=document.getElementById('ag-shared-cta'), m=document.querySelector('[data-page="'+k+'"]');
    if(k!=='contact'&&k!=='start'){m.appendChild(cta);cta.style.display='';}else{cta.style.display='none';}
    ['ag-h','ag-f','ag-w'].forEach(function(id){document.getElementById(id).style.display=(k==='start')?'none':'';});
    document.querySelectorAll('.ag-top__link').forEach(function(a){var q=(a.getAttribute('href')||'').replace(/\\/+$/,'')||'/';a.classList.toggle('ag-active',q===p||(k.indexOf('p-')===0&&q==='/work'));});
    window.scrollTo(0,0); if(h){var t=document.getElementById(h);if(t)setTimeout(function(){t.scrollIntoView();},60);}
    window.dispatchEvent(new Event('resize'));
    return true;
  }
  window.__agPreviewNav=function(h,done){show(h);setTimeout(done,150);};
  window.__show=show; show('/');
})();
</script></body></html>''' % str(ROUTES).replace("'",'"'))
LOGOS=json.load(open('/home/claude/azeez-portfolio/tools/logos.json'))
txt='\n'.join(out)
txt=re.sub(r'https://cdn\.jsdelivr\.net/gh/devicons/devicon@v2\.16\.0/icons/([a-z0-9]+)/\1-original\.svg',lambda m:LOGOS[m.group(1)],txt)
txt=txt.replace('https://cdn.jsdelivr.net/npm/simple-icons@13.21.0/icons/make.svg',LOGOS['make'])
open(sys.argv[1],'w').write(txt)
print(len(txt))
