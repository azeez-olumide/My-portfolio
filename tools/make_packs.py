import re,glob,base64,io,json,os
from PIL import Image
root='/home/claude/azeez-portfolio/'
names=set()
for f in glob.glob(root+'sections/*.html'):
    if f.endswith('00-emoji-pack.html'): continue
    s=open(f).read()
    names|=set(re.findall(r'(?:data-em="|\[\')([A-Za-z][A-Za-z ]+)\|[a-z_]+',s))
names=sorted(names)
pack={};missing=[]
for n in names:
    p=root+'assets/emoji/'+n.lower().replace(' ','_')+'_3d.png'
    if not os.path.exists(p): missing.append(n); continue
    im=Image.open(p).convert('RGBA').resize((144,144),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'WEBP',quality=84,method=6)
    pack[n]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
print(len(pack),'packed; missing:',missing)
html='<!-- ========== AG SECTION: emoji-pack (OPTIONAL. Paste once per page, above the other sections) ==========\n     Holds the 3D emoji images inside the page itself (no CDN needed, loads instantly). If you skip it, every section loads the same emoji from jsDelivr.\n     3D emoji: Microsoft Fluent Emoji, MIT licence. -->\n<script>window.AGE=Object.assign(window.AGE||{},'+json.dumps(pack,separators=(',',':'))+');</script>\n'
open(root+'sections/00-emoji-pack.html','w').write(html)
print(len(html)//1024,'KB')
# logos pack for preview
logos={}
for slug in ['html5','css3','javascript','react','supabase','vercel','figma','github','firebase','wordpress']:
    svg=open(f'/tmp/dv/icons/{slug}/{slug}-original.svg','rb').read()
    logos[slug]='data:image/svg+xml;base64,'+base64.b64encode(svg).decode()
logos['make']='data:image/svg+xml;base64,'+base64.b64encode(open('/tmp/si/icons/make.svg','rb').read()).decode()
json.dump(logos,open(root+'tools/logos.json','w'))
print({k:len(v) for k,v in logos.items()})
