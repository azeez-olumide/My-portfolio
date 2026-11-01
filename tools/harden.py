# Post-process pass (idempotent): token unification, minimum label size, softer borders, tap targets.
import re,glob
S='/home/claude/azeez-portfolio/sections/'
MAP=[('#f0bb4a','#f0b93e'),('#fbf6ea','#f8f3e9'),('#fbf6e9','#f8f3e9'),('#a8a193','#b9b1a1'),('#6f6a5f','#8f8878'),
     ('#0e0e10','#0e0e13'),('#151518','#15151b'),('#101014','#15151b'),('#16161b','#1d1d25'),('#0b0b0f','#0e0e13'),('#0a0a0d','#0a0a0e'),
     ('#8a5a00','#7a4f00'),('#f07a3e','#d99a1f'),('#8d8677','#9a9283')]
def fs(m):
    v=float(m.group(1)); return 'font-size:'+('.78' if v<.78 else m.group(1))+'rem'
TAP='''<style>
/* tap targets and reading size (v6.2) */
.ag-top__bar{height:44px}
.ag-top__bar a{display:inline-flex;align-items:center;min-height:44px;padding:0 6px}
.ag-top__link{padding:12px 14px;min-height:44px;display:inline-flex;align-items:center}
.ag-top__brand{min-height:44px}
.ag-footer__list{gap:0}
.ag-footer__list a{display:inline-block;padding:10px 0}
.ag-footer__bottom a{display:inline-block;padding:10px 0}
.ag-hero__link{display:inline-block;padding:14px 4px}
.ag-hero__note{font-size:.84rem}
.ag-contact__direct a{display:inline-block;padding:10px 0}
.ag-contact__direct{gap:0}
@media (max-width:900px){.ag-top__link{padding:16px 0;min-height:48px}}
</style>
'''
for f in glob.glob(S+'*.html'):
    if f.endswith('00-emoji-pack.html'): continue
    s=open(f).read(); o=s
    # keep base64 payloads out of the substitutions
    parts=re.split(r'(data:image/[a-z+]+;base64,[A-Za-z0-9+/=]+)',s)
    for i in range(0,len(parts),2):
        t=parts[i]
        for a,b in MAP: t=t.replace(a,b)
        t=re.sub(r'font-size:(\.[0-9]+)rem',fs,t)
        t=re.sub(r'rgba\(255,255,255,\.(26|28)\)',lambda m:'rgba(255,255,255,.2)' if 'home-testimonials' in f else m.group(0),t)
        parts[i]=t
    s=''.join(parts)
    if any(f.endswith(n) for n in ('header.html','footer.html','home-hero.html','contact-section.html')) and '/* tap targets and reading size' not in s:
        k=s.rindex('</style>')+8; s=s[:k]+'\n'+TAP+s[k:]
    if s!=o: open(f,'w').write(s)
print('hardened')
