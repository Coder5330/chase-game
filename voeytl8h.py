import pygame
from z1yhxso7 import*
from entities import d1hm38ks
from abc2be3y import yswjckjl,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.wgcl9lcq=pygame.Rect(rrcbpljd//2-qqu7eeqt//2,rla5ju9b-90,qqu7eeqt,qqu7eeqt)
  self.u15pdtz9=rv86wzs3
  self.izhwy9he=iq5c34dx['iwu3bf']
  self.xk7n8la1={'cm3v2p':0,'zmygy0':-1}
 def ob7p0rnp(self):
  v3e1ocjx=pygame.key.get_pressed()
  uc1xi04b=fp47b42g=0
  if v3e1ocjx[pygame.K_UP]:
   fp47b42g-=self.u15pdtz9
  if v3e1ocjx[pygame.K_DOWN]:
   fp47b42g+=self.u15pdtz9
  if v3e1ocjx[pygame.K_LEFT]:
   uc1xi04b-=self.u15pdtz9
  if v3e1ocjx[pygame.K_RIGHT]:
   uc1xi04b+=self.u15pdtz9
  if uc1xi04b!=0 and fp47b42g!=0:
   uc1xi04b*=0.707
   fp47b42g*=0.707
  if uc1xi04b!=0 or fp47b42g!=0:
   self.xk7n8la1['cm3v2p']=uc1xi04b
   self.xk7n8la1['zmygy0']=fp47b42g
  self.wgcl9lcq.jslulzfy+=uc1xi04b
  self.wgcl9lcq.zpfb3hn1+=fp47b42g
  self.wgcl9lcq.jslulzfy=max(0,min(self.wgcl9lcq.jslulzfy,rrcbpljd-self.wgcl9lcq.width))
  self.wgcl9lcq.zpfb3hn1=max(60,min(self.wgcl9lcq.zpfb3hn1,rla5ju9b-self.wgcl9lcq.height))
 def wzlm72je(self,ukshy8nb):
  (jslulzfy,zpfb3hn1)=(self.wgcl9lcq.jslulzfy,self.wgcl9lcq.zpfb3hn1)
  (hfb85p86,k7zgf9q5)=(self.wgcl9lcq.centerx,self.wgcl9lcq.centery)
  wd6r30oj=pygame.Surface((self.wgcl9lcq.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(wd6r30oj,(0,0,0,80),wd6r30oj.get_rect())
  ukshy8nb.blit(wd6r30oj,(hfb85p86-wd6r30oj.get_width()//2,zpfb3hn1+self.wgcl9lcq.height-6))
  mal2w37d=pygame.Rect(jslulzfy,zpfb3hn1,self.wgcl9lcq.width,self.wgcl9lcq.height)
  pygame.draw.rect(ukshy8nb,d1hm38ks(self.izhwy9he,0.55),mal2w37d,border_radius=10)
  i13n3bzt=mal2w37d.inflate(-5,-5)
  pygame.draw.rect(ukshy8nb,self.izhwy9he,i13n3bzt,border_radius=8)
  xqzpky32=pygame.Rect(i13n3bzt.jslulzfy+3,i13n3bzt.zpfb3hn1+3,i13n3bzt.width//2,i13n3bzt.height//3)
  pygame.draw.rect(ukshy8nb,d1hm38ks(self.izhwy9he,2.0),xqzpky32,border_radius=4)
  pygame.draw.rect(ukshy8nb,(15,15,30),mal2w37d,width=2,border_radius=10)
class gncxll4z:
 def __init__(self,zsw2292m,li9nb74x,color,jslulzfy,zpfb3hn1):
  self.zsw2292m=zsw2292m
  self.li9nb74x=li9nb74x
  self.izhwy9he=color
  self.wgcl9lcq=pygame.Rect(jslulzfy,zpfb3hn1,34,34)
  self.wvpw232u=False
 def wzlm72je(self,ukshy8nb,mqxlm5q2):
  wd6r30oj=pygame.Surface((self.wgcl9lcq.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(wd6r30oj,(0,0,0,70),wd6r30oj.get_rect())
  ukshy8nb.blit(wd6r30oj,(self.wgcl9lcq.centerx-wd6r30oj.get_width()//2,self.wgcl9lcq.bottom-4))
  mal2w37d=pygame.Rect(self.wgcl9lcq.jslulzfy,self.wgcl9lcq.zpfb3hn1,self.wgcl9lcq.width,self.wgcl9lcq.height)
  pygame.draw.rect(ukshy8nb,d1hm38ks(self.izhwy9he,0.6),mal2w37d,border_radius=8)
  i13n3bzt=mal2w37d.inflate(-5,-5)
  pygame.draw.rect(ukshy8nb,self.izhwy9he,i13n3bzt,border_radius=6)
  pygame.draw.rect(ukshy8nb,(15,15,15),mal2w37d,width=2,border_radius=8)
  (hfb85p86,k7zgf9q5)=(self.wgcl9lcq.centerx,self.wgcl9lcq.centery)
  pygame.draw.circle(ukshy8nb,iq5c34dx['yl4zjd'],(hfb85p86-6,k7zgf9q5-3),3)
  pygame.draw.circle(ukshy8nb,iq5c34dx['yl4zjd'],(hfb85p86+6,k7zgf9q5-3),3)
  pygame.draw.circle(ukshy8nb,iq5c34dx['ibxanj'],(hfb85p86-6,k7zgf9q5-3),1)
  pygame.draw.circle(ukshy8nb,iq5c34dx['ibxanj'],(hfb85p86+6,k7zgf9q5-3),1)
  swwnc21o=mqxlm5q2.render(self.zsw2292m,True,(20,20,20))
  ukshy8nb.blit(swwnc21o,(hfb85p86-swwnc21o.get_width()//2,self.wgcl9lcq.zpfb3hn1-20))
def jxxgaear():
 return[gncxll4z('Vera','i1yy1j',iq5c34dx['w65dlx'],120,140),gncxll4z('Duncan','bdoz6w',iq5c34dx['fnn16u'],383,110),gncxll4z('Mira','e0s41k',iq5c34dx['v5ff1b'],650,140)]
yex8fsv8={'i1yy1j':'Vitality Shop - Vera','bdoz6w':'Combat Shop - Duncan','e0s41k':'Mobility Shop - Mira'}
def eq3tq1s0(key,pcvsqame):
 rk2u1rsu=ibps3y70[key]
 return int(rk2u1rsu['yl6lgj']*rk2u1rsu['wzwl3z']**pcvsqame)
def i0x65muf(cq2q4qer,li9nb74x,xq46nouh):
 (mqxlm5q2,stv18kgy,ncyh3fvl,qbm1enf3)=xq46nouh
 v3e1ocjx=[k for(k,bu4xszjn)in ibps3y70.items()if bu4xszjn['k1yjfe']==li9nb74x]
 lztkkfzz=110*len(v3e1ocjx)+20
 ee1g983e=yswjckjl(420,lztkkfzz+yswjckjl.gokc1msy+60,my6wktak,title=yex8fsv8.get(li9nb74x,'Shop'),title_font=ncyh3fvl)
 f2sehe2a=ee1g983e.wgcl9lcq.zpfb3hn1+ee1g983e.a8lw2lm3
 wppsfnko=lztkkfzz//len(v3e1ocjx)
 for(sdeekgys,key)in enumerate(v3e1ocjx):
  rk2u1rsu=ibps3y70[key]
  b78okz1p=cq2q4qer['meta_upgrades'].get(key,0)
  lnf74t60=b78okz1p>=rk2u1rsu['hzj7ub']
  if lnf74t60:
   title=f"{rk2u1rsu['cxf5x9']}  MAX LEVEL"
  else:
   wzs13c9x=eq3tq1s0(key,b78okz1p)
   title=f"{rk2u1rsu['cxf5x9']}  Lv.{b78okz1p} -> {b78okz1p + 1}   [{wzs13c9x} res]"
  bq349dxb=hc58drc1(ee1g983e.wgcl9lcq.jslulzfy+12,f2sehe2a+sdeekgys*wppsfnko+6,ee1g983e.wgcl9lcq.width-24,wppsfnko-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,qbm1enf3,title,12,subtitle=rk2u1rsu['mviifr'],sub_font=stv18kgy,kind='meta',key=key)
  bq349dxb.maxed=lnf74t60
  ee1g983e.add(bq349dxb)
 obc2nnuv=f2sehe2a+len(v3e1ocjx)*wppsfnko+12
 uos0fb4y=hc58drc1(ee1g983e.wgcl9lcq.jslulzfy+12,obc2nnuv,ee1g983e.wgcl9lcq.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),qbm1enf3,'Close (ESC)',10,kind='close',key=None)
 ee1g983e.add(uos0fb4y)
 return ee1g983e
def tby49e7e(ukshy8nb,x5m9j98c,cq2q4qer,pllkstn3):
 mqxlm5q2=pygame.font.SysFont('arial',22)
 stv18kgy=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 ncyh3fvl=pygame.font.SysFont('arial',22,bold=True)
 qbm1enf3=pygame.font.SysFont('arial',20,bold=True)
 z8z3v6di=pygame.font.SysFont('arial',15)
 xq46nouh=(mqxlm5q2,stv18kgy,ncyh3fvl,qbm1enf3)
 am2vajep=zbqe7ckw()
 jl90pxrl=jxxgaear()
 f8rtm4j3=pygame.Rect(rrcbpljd//2-70,rla5ju9b-60,140,44)
 j1i2hgj1=None
 ia529603=None
 while True:
  gubmc97c=pygame.event.get()
  for ouuylaja in gubmc97c:
   if ouuylaja.type==pygame.QUIT:
    return'quit'
   if ouuylaja.type==pygame.KEYDOWN and ouuylaja.key==pygame.K_ESCAPE and j1i2hgj1:
    j1i2hgj1=None
    ia529603=None
  if j1i2hgj1 is None:
   am2vajep.ob7p0rnp()
   i33e1i1p=None
   for d448n7od in jl90pxrl:
    if am2vajep.wgcl9lcq.colliderect(d448n7od.wgcl9lcq.inflate(24,24)):
     if not d448n7od.wvpw232u:
      i33e1i1p=d448n7od
      d448n7od.wvpw232u=True
      break
    else:
     d448n7od.wvpw232u=False
   if i33e1i1p:
    ia529603=i33e1i1p.li9nb74x
    j1i2hgj1=i0x65muf(cq2q4qer,ia529603,xq46nouh)
   if am2vajep.wgcl9lcq.colliderect(f8rtm4j3):
    return'start_game'
  else:
   for sygvwopl in j1i2hgj1.nd31k9qm:
    sygvwopl.update(gubmc97c)
   clkqzfpq=next((x875aud9 for x875aud9 in j1i2hgj1.nd31k9qm if x875aud9.clkqzfpq),None)
   if clkqzfpq is not None:
    if clkqzfpq.kind=='close':
     j1i2hgj1=None
     ia529603=None
    elif clkqzfpq.kind=='meta'and(not getattr(clkqzfpq,'maxed',False)):
     key=clkqzfpq.key
     b78okz1p=cq2q4qer['meta_upgrades'].get(key,0)
     wzs13c9x=eq3tq1s0(key,b78okz1p)
     if cq2q4qer['resources']>=wzs13c9x:
      cq2q4qer['resources']-=wzs13c9x
      cq2q4qer['meta_upgrades'][key]=b78okz1p+1
      pllkstn3(cq2q4qer)
      j1i2hgj1=i0x65muf(cq2q4qer,ia529603,xq46nouh)
  ukshy8nb.fill((190,225,190))
  for x9bp4m18 in range(0,rrcbpljd,y38daly8):
   pygame.draw.line(ukshy8nb,(160,205,160),(x9bp4m18,0),(x9bp4m18,rla5ju9b),1)
  for m8lw2qit in range(0,rla5ju9b,y38daly8):
   pygame.draw.line(ukshy8nb,(160,205,160),(0,m8lw2qit),(rrcbpljd,m8lw2qit),1)
  pygame.draw.rect(ukshy8nb,iq5c34dx['hb1ajo'],f8rtm4j3,border_radius=10)
  pygame.draw.rect(ukshy8nb,(150,110,0),f8rtm4j3,width=3,border_radius=10)
  l3swebnv=stv18kgy.render('ENTER RUN',True,(40,30,0))
  ukshy8nb.blit(l3swebnv,(f8rtm4j3.centerx-l3swebnv.get_width()//2,f8rtm4j3.centery-l3swebnv.get_height()//2))
  for d448n7od in jl90pxrl:
   d448n7od.wzlm72je(ukshy8nb,stv18kgy)
  am2vajep.wzlm72je(ukshy8nb)
  gqj5sxvw=pygame.Rect(12,12,220,40)
  semqgy27=pygame.Surface((gqj5sxvw.width,gqj5sxvw.height),pygame.SRCALPHA)
  pygame.draw.rect(semqgy27,(255,255,255,160),semqgy27.get_rect(),border_radius=10)
  ukshy8nb.blit(semqgy27,gqj5sxvw.topleft)
  yg87oi0e=mqxlm5q2.render(f"Resources: {cq2q4qer['resources']}",True,(20,20,20))
  ukshy8nb.blit(yg87oi0e,(20,22))
  qxt6ridl=title_font.render('HOMEBASE',True,(20,40,20))
  ukshy8nb.blit(qxt6ridl,(rrcbpljd//2-qxt6ridl.get_width()//2,12))
  o9ros7yt=z8z3v6di.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  ukshy8nb.blit(o9ros7yt,(rrcbpljd//2-o9ros7yt.get_width()//2,rla5ju9b-105))
  if j1i2hgj1:
   j1i2hgj1.wzlm72je(ukshy8nb)
  pygame.display.flip()
  x5m9j98c.tick(pi3qk2ia)
