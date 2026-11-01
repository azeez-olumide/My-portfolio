# Adds the dark/light toggle: header button, early theme init in the loader, start-form button, contact/start light overrides. Idempotent.
import re
S='/home/claude/azeez-portfolio/sections/'
ICON='<svg class="ag-th-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></svg><svg class="ag-th-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 0 1 9.8 3.5a8.5 8.5 0 1 0 10.7 10.7z"/></svg>'
THEME_JS="""function(){try{var t=localStorage.getItem('agTheme');if(t==='light'||t==='dark'){document.documentElement.setAttribute('data-ag-theme',t);}}catch(e){}}"""
BTN_CSS='''.ag-theme{flex:none;display:inline-grid;place-items:center;width:44px;height:44px;margin-left:8px;border-radius:50%;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.05);color:#f8f3e9;cursor:pointer;padding:0;transition:background .25s,border-color .25s,transform .35s}
.ag-theme:hover{border-color:#f0b93e;background:rgba(240,185,62,.16);transform:rotate(18deg)}
.ag-theme:focus-visible{outline:2px solid #ffd479;outline-offset:3px}
.ag-theme svg{width:20px;height:20px;grid-area:1/1;transition:opacity .25s,transform .35s}
.ag-theme .ag-th-moon{opacity:0;transform:scale(.6) rotate(-40deg)}
html[data-ag-theme="light"] .ag-theme .ag-th-sun{opacity:0;transform:scale(.6) rotate(40deg)}
html[data-ag-theme="light"] .ag-theme .ag-th-moon{opacity:1;transform:none}
'''
CLICK_JS="""
  function agToggleTheme(){var h=document.documentElement,n=h.getAttribute('data-ag-theme')==='light'?'dark':'light';h.setAttribute('data-ag-theme',n);try{localStorage.setItem('agTheme',n);}catch(e){}var b=document.querySelectorAll('.ag-theme');for(var i=0;i<b.length;i++){b[i].setAttribute('aria-pressed',n==='light'?'true':'false');b[i].setAttribute('aria-label',n==='light'?'Switch to dark mode':'Switch to light mode');}}
  (function(){var b=document.querySelectorAll('.ag-theme');for(var i=0;i<b.length;i++){if(b[i].getAttribute('data-ag-b'))continue;b[i].setAttribute('data-ag-b','1');b[i].addEventListener('click',agToggleTheme);var l=document.documentElement.getAttribute('data-ag-theme')==='light';b[i].setAttribute('aria-pressed',l?'true':'false');b[i].setAttribute('aria-label',l?'Switch to dark mode':'Switch to light mode');}})();
"""
BUTTON='<button class="ag-theme" type="button" aria-label="Switch to light mode" aria-pressed="false" title="Dark / light mode">'+ICON+'</button>'

# ---- header
p=S+'header.html'; s=open(p).read()
if 'ag-theme' not in s:
    s=s.replace('</nav>\n    </div>','</nav>\n      '+BUTTON+'\n    </div>',1)
    s=s.replace('<style>','<style>\n'+BTN_CSS+'@media (max-width:900px){.ag-top__toggle{order:3}.ag-theme{order:2;margin-left:auto;margin-right:8px}.ag-top__brand{order:1}}\n',1)
    k=s.rindex('})();'); s=s[:k]+CLICK_JS+s[k:]
    open(p,'w').write(s)

# ---- loader: apply the saved theme before anything paints
p=S+'00-loader.html'; s=open(p).read()
if 'agTheme' not in s:
    s=s.replace('<style>','<script>('+THEME_JS+')();</script>\n<style>',1)
    open(p,'w').write(s)

# ---- start form: toggle next to the X, plus light overrides for contact + start
LIGHT_OVR='''html[data-ag-theme="light"] .CCLS{--ag-bg:#f4efe3;--ag-surface:#fffdf8;--ag-surface-2:#ebe4d3;--ag-line:rgba(10,10,12,.14);--ag-text:#0b0b0e;--ag-muted:#5a5446;background:#f4efe3;color:#0b0b0e}
html[data-ag-theme="light"] .CCLS::before{opacity:.6}
html[data-ag-theme="light"] .CCLS .FCLS{background:#fffdf8;border-color:rgba(10,10,12,.16);box-shadow:0 30px 80px -40px rgba(122,79,0,.35)}
html[data-ag-theme="light"] .CCLS legend,html[data-ag-theme="light"] .CCLS .FCLS__done h3,html[data-ag-theme="light"] .CCLS__title,html[data-ag-theme="light"] .CCLS__call h3{color:#0b0b0e}
html[data-ag-theme="light"] .CCLS .FCLS input[type=text],html[data-ag-theme="light"] .CCLS .FCLS input[type=email],html[data-ag-theme="light"] .CCLS .FCLS textarea{background:#fff;color:#0b0b0e;border-color:rgba(10,10,12,.3)}
html[data-ag-theme="light"] .CCLS .FCLS input::placeholder,html[data-ag-theme="light"] .CCLS .FCLS textarea::placeholder{color:#7a7364}
html[data-ag-theme="light"] .CCLS .FCLS__choice span{background:#fff;color:#0b0b0e;border-color:rgba(10,10,12,.3)}
html[data-ag-theme="light"] .CCLS .FCLS__choice input:checked+span{background:rgba(240,185,62,.28);border-color:#7a4f00;color:#0b0b0e}
html[data-ag-theme="light"] .CCLS .FCLS__back:hover{color:#0b0b0e}
html[data-ag-theme="light"] .CCLS .FCLS__bar{background:#ebe4d3}
html[data-ag-theme="light"] .CCLS .FCLS__sum b{color:#0b0b0e}
html[data-ag-theme="light"] .CCLS .BTN2--line{color:#0b0b0e!important;border-color:rgba(10,10,12,.35)}
html[data-ag-theme="light"] .CCLS__call{background:#fffdf8}
html[data-ag-theme="light"] .CCLS a{color:#0b0b0e}
html[data-ag-theme="light"] .CCLS .BTN2--gold{color:#1a1204}
html[data-ag-theme="light"] .CCLS__tz b{color:#7a4f00}
html[data-ag-theme="light"] .CCLS__tz{color:#5a5446}
html[data-ag-theme="light"] .SFX{color:#0b0b0e;border-color:rgba(10,10,12,.3);background:rgba(10,10,12,.04)}
'''
for fn,(cc,fc,b2,sfx) in {'contact-section.html':('ag-contact','ag-form','ag-btn2','ag-sf__x'),'start-form.html':('ag-sf-contact','ag-sf-form','ag-btn2','ag-sf__x')}.items():
    p=S+fn; s=open(p).read()
    if fn=='start-form.html' and 'ag-th-sun' in s: continue
    if fn=='contact-section.html' and 'data-ag-theme' in s: continue
    css=LIGHT_OVR.replace('CCLS',cc).replace('FCLS',fc).replace('BTN2',b2).replace('SFX',sfx)
    if 'data-ag-theme' not in s: s=s[:s.index('</style>')]+css+s[s.index('</style>'):]
    if fn=='start-form.html':
        s=s.replace('<a class="ag-sf__x"','<button class="ag-theme" type="button" aria-label="Switch to light mode" aria-pressed="false" title="Dark / light mode" style="margin-left:auto;margin-right:10px">'+ICON+'</button><a class="ag-sf__x"',1)
        s=s.replace('<style>','<style>\n'+BTN_CSS,1)
        s=s.replace('.ag-sf__bar img{','.ag-sf__bar{gap:0}.ag-sf__bar img{',1)
        k=s.rindex('</script>'); 
        # add toggle logic as its own script block at the end
        s=s+'<script>(function(){'+CLICK_JS+'})();</script>\n'
    open(p,'w').write(s)
# header: solid dark bar in light mode so the logo and links stay readable
p=S+'header.html'; s=open(p).read()
if 'agHdrLight' not in s:
    s=s.replace('</style>','/* agHdrLight */\nhtml[data-ag-theme="light"] .ag-top__nav{background:rgba(7,7,10,.94);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}\n</style>',1)
    open(p,'w').write(s)
p=S+'start-form.html'; s=open(p).read()
if 'agStartTh' not in s:
    s=s.replace('</style>','/* agStartTh */\nhtml[data-ag-theme="light"] .ag-sf__bar .ag-theme{color:#0b0b0e;border-color:rgba(10,10,12,.3);background:rgba(10,10,12,.04)}\n</style>',1)
    open(p,'w').write(s)
print('theme ok')
