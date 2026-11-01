import re
S='/home/claude/azeez-portfolio/sections/'
foot=open(S+'footer.html').read()
LOGO=re.search(r'src="(data:image/webp;base64,[^"]+)"',foot).group(1)

# ---------- START FORM (own page, nothing but the questions) ----------
c=open(S+'contact-section.html').read()
style=c[c.index('<style>'):c.index('</style>')+8]
script=c[c.index('<script>'):]
script=script[:script.index('  (function(){try{var el=document.getElementById(\'ag-tz\')')]+'</script>\n'
# remove call-button logic
script=re.sub(r"  /\* secondary call button \*/.*?\n  function render","  function waLink(msg){ return 'https://wa.me/'+WHATSAPP+'?text='+encodeURIComponent(msg); }\n\n  function render",script,flags=re.S)
script=script.replace("var CALENDLY_URL=''","var CALENDLY_URL=''")
extra='''<style>
  .ag-contact{min-height:100vh;min-height:100svh;display:flex;align-items:center;justify-content:center;padding:84px 24px 40px;border-top:0}
  .ag-contact__inner{display:block;width:100%;max-width:640px}
  .ag-contact::before{left:50%;right:auto;top:50%;transform:translate(-50%,-50%);width:90vw;height:90vw}
  .ag-sf__bar{position:absolute;z-index:3;left:0;right:0;top:0;display:flex;align-items:center;justify-content:space-between;padding:22px max(24px,calc((100vw - 1248px)/2))}
  .ag-sf__bar img{width:64px;height:auto;display:block}
  .ag-sf__x{display:grid;place-items:center;width:44px;height:44px;border-radius:50%;border:1px solid rgba(255,255,255,.25);color:#f8f3e9;background:rgba(255,255,255,.04);text-decoration:none;transition:background .25s,border-color .25s,transform .25s}
  .ag-sf__x:hover{border-color:#f0b93e;background:rgba(240,185,62,.15);transform:rotate(90deg)}
  .ag-sf__x svg{width:18px;height:18px}
  .ag-form{border-radius:28px;background:rgba(16,16,20,.82);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);padding:40px;min-height:0;box-shadow:0 40px 120px -40px rgba(240,185,62,.35)}
  .ag-form legend{font-size:clamp(1.5rem,1.6vw + 1.1rem,2.2rem)}
  .ag-form__bar i{background:linear-gradient(90deg,#f0b93e,#ffd479)}
  .ag-btn2{border-radius:999px;padding:16px 30px}
  .ag-btn2--gold{box-shadow:0 14px 38px -12px rgba(240,185,62,.7)}
  @media (max-width:560px){.ag-contact{padding:78px 16px 24px;align-items:flex-start}.ag-form{padding:26px 20px;border-radius:22px}}
</style>
'''
html=f'''
<section class="ag-contact" id="ag-contact" aria-label="Start a project">
  <div class="ag-sf__bar"><a data-ag-link="home" href="/" aria-label="Home"><img alt="Azeez Gazalle" src="{LOGO}"></a><a class="ag-sf__x" data-ag-link="home" href="/" aria-label="Close and go home"><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 4l12 12M16 4L4 16"/></svg></a></div>
  <div class="ag-contact__inner">
    <form class="ag-form" id="ag-form" novalidate aria-label="Start a project">
      <div class="ag-form__top"><span id="ag-step-label">Step 1 of 7</span><span></span></div>
      <div class="ag-form__bar" aria-hidden="true"><i id="ag-bar"></i></div>
      <div id="ag-step" aria-live="polite"></div>
      <div class="ag-form__hp" aria-hidden="true"><label>Leave this empty<input type="text" name="website" id="ag-hp" tabindex="-1" autocomplete="off"></label></div>
      <p class="ag-form__err" id="ag-err" role="alert"></p>
      <div class="ag-form__nav" id="ag-nav">
        <button type="button" class="ag-form__back" id="ag-back" hidden>Back</button>
        <button type="submit" class="ag-btn2 ag-btn2--gold" id="ag-next">Continue</button>
      </div>
    </form>
  </div>
</section>
'''
link_js='''<script>(function(){var L={home:'/'};var a=document.querySelectorAll('#ag-contact [data-ag-link]');for(var i=0;i<a.length;i++){var k=a[i].getAttribute('data-ag-link');if(L[k])a[i].setAttribute('href',L[k]);}})();</script>
'''
head=c[:c.index('<style>')].split('\n')
hdr='<!-- ========== AG SECTION: start-form (the "Start a project" page, path /start) ==========\n     ONLY this block on the page: no header, no footer, no other text. One question at a time.\n     Set WEBHOOK_URL in the script (empty = the details are sent through WhatsApp). The X returns home. -->\n'
fonts='\n'.join(l for l in head if l.startswith('<link'))+'\n'
body=style+extra+html+script
body=re.sub(r'\bag-(contact|form|step-label|step|err|next|back|bar|hp|nav|q|f)\b',r'ag-sf-\1',body)
open(S+'start-form.html','w').write(hdr+fonts+body+link_js)

# ---------- LOADER ----------
loader='''<!-- ========== AG SECTION: 00-loader (paste at the VERY TOP of EVERY page, above everything else) ==========
     Black screen with your logo and a ring of lightning. Shows when a page opens, then fades into the page.
     It also shows briefly when a visitor clicks any link to another page of your site. -->
<style>
  #ag-load{position:fixed;inset:0;z-index:2147483000;background:#050507;display:grid;place-items:center;opacity:1;visibility:visible;transition:opacity .55s ease,visibility .55s ease}
  #ag-load.ag-out{opacity:0;visibility:hidden;pointer-events:none}
  #ag-load .ag-l-wrap{position:relative;width:min(46vw,200px);aspect-ratio:1}
  #ag-load .ag-l-ring{position:absolute;inset:-14%;border-radius:50%;background:conic-gradient(from 0deg,rgba(240,185,62,0) 0deg,rgba(240,185,62,.15) 120deg,#f0b93e 300deg,#fff3cf 350deg,rgba(240,185,62,0) 360deg);-webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 3px),#000 calc(100% - 2px));mask:radial-gradient(farthest-side,transparent calc(100% - 3px),#000 calc(100% - 2px));animation:ag-l-spin 1.1s linear infinite;filter:drop-shadow(0 0 10px rgba(240,185,62,.9))}
  #ag-load .ag-l-ring2{position:absolute;inset:-26%;border-radius:50%;border:1px solid rgba(240,185,62,.18);animation:ag-l-pulse 1.8s ease-in-out infinite}
  #ag-load .ag-l-bolts{position:absolute;inset:-34%;width:168%;height:168%;overflow:visible;animation:ag-l-spin 3.2s linear infinite reverse}
  #ag-load .ag-l-bolts path{fill:none;stroke:#ffe9b0;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;filter:drop-shadow(0 0 6px #f0b93e);opacity:0;animation:ag-l-flash 1.4s infinite}
  #ag-load .ag-l-bolts path:nth-child(2){animation-delay:.45s}
  #ag-load .ag-l-bolts path:nth-child(3){animation-delay:.9s}
  #ag-load img{position:relative;width:100%;height:auto;display:block;animation:ag-l-in .8s cubic-bezier(.2,.7,.2,1) both;filter:drop-shadow(0 0 24px rgba(240,185,62,.45))}
  #ag-load .ag-l-glow{position:absolute;inset:-60%;background:radial-gradient(closest-side,rgba(240,185,62,.28),transparent 70%);animation:ag-l-pulse 1.8s ease-in-out infinite}
  @keyframes ag-l-spin{to{transform:rotate(360deg)}}
  @keyframes ag-l-pulse{0%,100%{opacity:.5;transform:scale(.97)}50%{opacity:1;transform:scale(1.04)}}
  @keyframes ag-l-flash{0%,55%,100%{opacity:0}60%{opacity:1}68%{opacity:.2}74%{opacity:1}86%{opacity:0}}
  @keyframes ag-l-in{from{opacity:0;transform:scale(.8) rotate(-8deg);filter:blur(8px)}to{opacity:1;transform:none}}
  @media (prefers-reduced-motion:reduce){#ag-load .ag-l-ring,#ag-load .ag-l-bolts,#ag-load .ag-l-glow,#ag-load .ag-l-ring2,#ag-load img{animation:none}#ag-load .ag-l-ring{opacity:.8}}
</style>
<div id="ag-load" role="status" aria-label="Loading"><div class="ag-l-wrap">
  <div class="ag-l-glow"></div><div class="ag-l-ring2"></div><div class="ag-l-ring"></div>
  <svg class="ag-l-bolts" viewBox="-100 -100 200 200" aria-hidden="true"><path d="M-6 -98 L2 -84 L-4 -80 L6 -66"/><path d="M92 -34 L80 -26 L84 -20 L70 -10"/><path d="M-84 52 L-72 48 L-76 40 L-62 34"/></svg>
  <img alt="Azeez Gazalle" width="320" height="320" src="__LOGO__">
</div></div>
<script>
(function(){
  var el=document.getElementById('ag-load'); if(!el||el.getAttribute('data-ag-init'))return; el.setAttribute('data-ag-init','1');
  var FIRST_SHOW=1300;  /* ms the logo stays the first time a visitor opens the site in a session */
  var NEXT_SHOW=450;    /* ms on later page opens in the same session */
  var LEAVE=400;        /* ms the logo shows before moving to another page */
  var seen=false; try{ seen=!!sessionStorage.getItem('agSeen'); sessionStorage.setItem('agSeen','1'); }catch(x){}
  var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var MIN_SHOW=rm?150:(seen?NEXT_SHOW:FIRST_SHOW); if(rm)LEAVE=150;
  var t0=Date.now(), hidden=false;
  function hide(){ if(hidden)return; hidden=true; var w=Math.max(0,MIN_SHOW-(Date.now()-t0)); setTimeout(function(){ el.className+=' ag-out'; },w); }
  function show(){ hidden=false; t0=Date.now(); el.className=el.className.replace(/\\s*ag-out/g,''); }
  if(document.readyState==='complete') hide(); else window.addEventListener('load',hide);
  setTimeout(hide,6000);                                  /* never trap a visitor */
  window.addEventListener('pageshow',function(e){ if(e.persisted){ hidden=false; hide(); } });   /* back button */
  window.AGLoader={show:show,hide:hide};
  document.addEventListener('click',function(e){
    if(e.defaultPrevented||e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
    var a=e.target.closest&&e.target.closest('a'); if(!a)return;
    var h=a.getAttribute('href')||''; if(!h||h.charAt(0)==='#'||a.target==='_blank'||a.hasAttribute('download'))return;
    var u; try{u=new URL(a.href,location.href);}catch(x){return;}
    if(u.origin!==location.origin||/^(mailto|tel):/i.test(h))return;
    if(u.pathname===location.pathname&&u.search===location.search)return;       /* same page: let the browser scroll */
    e.preventDefault(); show();
    setTimeout(function(){ if(window.__agPreviewNav) window.__agPreviewNav(u.pathname+u.hash,hide); else location.href=u.href; },LEAVE);
  },true);
})();
</script>
'''.replace('__LOGO__','data:image/webp;base64,'+__import__('base64').b64encode(open('/home/claude/azeez-portfolio/assets/avatars/avatar-smile-badge.webp','rb').read()).decode())
open(S+'00-loader.html','w').write(loader)
print('ok')
