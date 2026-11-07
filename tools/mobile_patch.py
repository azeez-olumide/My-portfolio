"""Phone-only polish (<=760px). Appends one CSS block to each Home section. Idempotent. Run LAST in the pipeline."""
import re
D='/home/claude/azeez-portfolio/sections/'
M='/* AG-MOBILE-FIX */'
P={}
P['home-hero']='''
.ag-hero__bar{padding-top:18px}
.ag-hero__eyebrow{font-size:.62rem;letter-spacing:.1em;gap:8px;white-space:nowrap}
.ag-hero__eyebrow::before,.ag-hero__eyebrow::after{width:10px}
.ag-hero__right{width:100%;align-items:stretch;gap:12px;box-sizing:border-box}
.ag-hero__pill{justify-content:center;width:100%;box-sizing:border-box}
.ag-hero__link{display:flex;justify-content:center;align-items:center;width:100%;box-sizing:border-box;padding:16px;border:1.5px solid rgba(240,185,62,.5);border-radius:999px;color:var(--ag-text);font-weight:700;font-size:.82rem;letter-spacing:.08em;text-transform:uppercase}
.ag-hero__note{text-align:center;font-size:.8rem}
'''
P['home-about']='''
.ag-habout .ag-wrap,.ag-habout .ag-box,.ag-habout .ag-big,.ag-habout .ag-words{text-align:left}
.ag-habout .ag-words{font-size:1.2rem;line-height:1.55;font-weight:600}
.ag-habout .ag-facts{display:grid;grid-template-columns:1fr 1fr;gap:26px 16px;justify-content:stretch;margin:34px 0 30px;padding-top:28px;text-align:left}
.ag-habout .ag-facts strong{font-size:2rem;white-space:nowrap}
.ag-habout .ag-prop:nth-of-type(2),.ag-habout .ag-prop:nth-of-type(3){display:none}
.ag-habout .ag-prop{--w:12vw !important;max-width:60px}
'''
P['home-services']='''
.ag-hsvc .ag-prop,.ag-hsvc .ag-go img{display:none !important}
'''
P['home-work']='''
.ag-hwork .ag-prop{display:none !important}
.ag-hwork .ag-stack{counter-reset:agn}
.ag-hwork .ag-card{counter-increment:agn;position:sticky}
.ag-hwork .ag-ch{display:flex;flex-direction:column;align-items:flex-start;gap:14px;padding:8px 6px 16px}
.ag-hwork .ag-ct{display:block}
.ag-hwork .ag-no{font-size:0;display:block;margin-bottom:10px}
.ag-hwork .ag-no::before{content:"0" counter(agn);font-size:1.6rem;font-weight:900;letter-spacing:-.04em;line-height:1}
.ag-hwork .ag-ct small{font-size:.62rem;letter-spacing:.1em;line-height:1.5;margin-bottom:6px}
.ag-hwork .ag-ct b{font-size:1.2rem;line-height:1.25;letter-spacing:-.02em}
.ag-hwork .ag-ind{display:block;margin-top:5px;font-size:.84rem;line-height:1.4}
.ag-hwork .ag-ind i{display:none}
.ag-hwork .ag-lv{padding:0;border:0;border-radius:0;background:none;color:var(--ag-gold);font-size:.74rem;letter-spacing:.12em}
.ag-hwork .ag-lv::before{content:"";position:absolute;inset:0;border-radius:inherit;z-index:3}
.ag-hwork .ag-lv::after{content:"  \\2192"}
'''
P['home-process']='''
.ag-hproc .ag-prop{display:none !important}
.ag-hproc .ag-st{position:relative;grid-template-columns:42px 1fr;gap:6px 14px;padding:26px 0}
.ag-hproc .ag-st>img{position:absolute;right:0;top:26px;width:34px;height:34px}
.ag-hproc .ag-st h3{padding-right:46px}
.ag-hproc .ag-st p{font-size:.94rem}
'''
P['home-testimonials']='''
.ag-htest .ag-tt{flex-wrap:nowrap;gap:12px;padding:0 20px;margin-bottom:24px;align-items:center}
.ag-htest .ag-tt h2{margin:0}
.ag-htest .ag-tt img{width:40px;flex:none}
.ag-htest.ag-sheet{padding-bottom:56px}
'''
P['home-cta']='''
.ag-hcta .ag-mephoto{-webkit-mask-image:linear-gradient(#000 78%,transparent);mask-image:linear-gradient(#000 78%,transparent)}
.ag-hcta .ag-note{font-size:.92rem}
'''
P['footer']='''
.ag-footer{padding:56px 20px 22px}
.ag-footer__grid{grid-template-columns:1fr;gap:30px;padding-bottom:36px}
.ag-footer__about{font-size:.95rem;line-height:1.65}
.ag-footer__h{margin-bottom:8px}
.ag-footer__grid>div:nth-child(2) .ag-footer__list{display:grid;grid-template-columns:repeat(3,auto);justify-content:space-between;column-gap:12px}
.ag-footer__grid>div:nth-child(3) .ag-footer__list{display:flex;flex-wrap:wrap;column-gap:22px}
.ag-footer__word{font-size:2.4rem;margin-top:0}
.ag-footer__bottom{flex-direction:column;align-items:flex-start;gap:2px;font-size:.82rem}
'''
for n,c in P.items():
    f=D+n+'.html'; s=open(f).read()
    s=re.sub(r'\n?/\* AG-MOBILE-FIX \*/.*?/\* /AG-MOBILE-FIX \*/','',s,flags=re.S)
    i=s.rindex('</style>')
    s=s[:i]+'\n'+M+'\n@media (max-width:760px){'+c+'}\n/* /AG-MOBILE-FIX */\n'+s[i:]
    open(f,'w').write(s)
print('mobile patch applied')
