import os,sys
S='/home/claude/azeez-portfolio/sections/'
R=lambda n:open(S+n).read()
pages={'home':['home-hero','home-logos','home-about','home-work','home-services','home-process','cta-strip'],
'work':['page-hero-work','work-grid','cta-strip'],
'services':['page-hero-services','pricing','process','after-launch','payment-terms','cta-strip'],
'about':['page-hero-about','about-story','about-approach','cta-strip'],
'contact':['page-hero-contact','contact-section']}
out=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Azeez Gazalle Portfolio</title><style>body{margin:0;background:#060607}[data-page]{display:none}[data-page].on{display:block}</style></head><body>',R('00-global.html'),R('00-emoji-pack.html'),R('header.html')]
used=set()
for pg,secs in pages.items():
    out.append('<div data-page="%s"%s>'%(pg,' class="on"' if pg=='home' else ''))
    for s in secs:
        h=R(s+'.html')
        if s=='cta-strip' and pg!='home':  # ids must be unique per DOM; the CTA repeats per page
            h=h.replace('ag-cta','ag-cta-'+pg)
        out.append(h)
    out.append('</div>')
out+= [R('footer.html'),R('whatsapp-float.html')]
out.append('''<script>(function(){var map={'/':'home','/projects':'work','/services':'services','/about':'about','/contact':'contact'};
function show(p){var els=document.querySelectorAll('[data-page]');for(var i=0;i<els.length;i++)els[i].className=els[i].getAttribute('data-page')===p?'on':'';window.scrollTo(0,0);try{history.replaceState(null,'','#'+p)}catch(e){}}
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a');if(!a)return;var h=a.getAttribute('href');if(h&&map[h]){e.preventDefault();show(map[h]);}});
var h=(location.hash||'').replace('#','');if(h&&document.querySelector('[data-page="'+h+'"]'))show(h);})();</script></body></html>''')
open(sys.argv[1],'w').write('\n'.join(out))
