# Builds the 3D-avatar assets from the supplied images (originals are never modified).
import json,base64,io,os
from PIL import Image,ImageDraw,ImageFilter
import numpy as np
S='/tmp/claude-0/-home-claude/23737cca-b3a2-52c2-9cc6-2c8bc3e401fe/scratchpad/av/'
OUT='/home/claude/azeez-portfolio/assets/avatars/'
def fade(im,frac=.14):
    a=np.array(im); h=a.shape[0]; n=int(h*frac)
    ramp=np.ones(h); ramp[h-n:]=np.linspace(1,0,n)**1.2
    a[:,:,3]=(a[:,:,3]*ramp[:,None]).astype(np.uint8); return Image.fromarray(a)
def webp(im,path,q=86):
    im.save(path,'WEBP',quality=q,method=6,lossless=False); return os.path.getsize(path)
def badge(cut,size=320):
    # circular medallion: warm dark disc + the cut-out avatar (face and headphones) + gold ring
    ss=size*2; disc=Image.new('RGBA',(ss,ss),(0,0,0,0)); d=ImageDraw.Draw(disc)
    grad=Image.new('RGBA',(ss,ss)); gp=grad.load()
    for y in range(ss):
        for x in range(ss):
            r=((x-ss*.5)**2+(y-ss*.38)**2)**.5/(ss*.62); r=min(1,r)
            gp[x,y]=(int(88-70*r),int(62-52*r),int(14-8*r),255)
    mask=Image.new('L',(ss,ss),0); ImageDraw.Draw(mask).ellipse((6,6,ss-6,ss-6),fill=255)
    disc.paste(grad,(0,0),mask)
    # centre the head (hair to chin, ears included) on the disc: measure it from the alpha channel
    al=np.array(cut.getchannel('A')); H0=al.shape[0]; band=al[:int(H0*.58)]>40
    cols=np.where(band.any(axis=0))[0]; rows=np.where(band.any(axis=1))[0]
    hx0,hx1=cols[0],cols[-1]; hw=hx1-hx0; top=rows[0]; chin=top+1.38*hw
    k=(ss*.56)/hw; c=cut.resize((int(cut.width*k),int(cut.height*k)),Image.LANCZOS)
    cxs=(hx0+hx1)/2*k; cys=(top+chin)/2*k
    layer=Image.new('RGBA',(ss,ss),(0,0,0,0)); layer.paste(c,(int(ss/2-cxs),int(ss*.50-cys)),c)
    layer.putalpha(Image.fromarray((np.array(layer.getchannel('A'))*(np.array(mask)/255)).astype(np.uint8)))
    disc=Image.alpha_composite(disc,layer)
    ring=Image.new('RGBA',(ss,ss),(0,0,0,0)); ImageDraw.Draw(ring).ellipse((6,6,ss-6,ss-6),outline=(240,185,62,255),width=14)
    disc=Image.alpha_composite(disc,ring)
    return disc.resize((size,size),Image.LANCZOS)
pack={}; rep=[]
for key,src,w in [('smile','smile.png',560),('neutral','neutral.png',560)]:
    cut=Image.open(S+src).convert('RGBA')
    big=fade(cut.resize((w,int(cut.height*w/cut.width)),Image.LANCZOS))
    p=OUT+f'avatar-{key}.webp'; sz=webp(big,p); rep.append((p,big.size,sz))
    pack['Me '+key]=p
    bd=badge(cut); p2=OUT+f'avatar-{key}-badge.webp'; sz2=webp(bd,p2,88); rep.append((p2,bd.size,sz2)); pack['Me '+key+' badge']=p2
    big.save(OUT+f'avatar-{key}.png'); bd.save(OUT+f'avatar-{key}-badge.png')
d={k:'data:image/webp;base64,'+base64.b64encode(open(p,'rb').read()).decode() for k,p in pack.items()}
json.dump(d,open('/home/claude/azeez-portfolio/tools/avatars.json','w'))
for r in rep: print(r)
