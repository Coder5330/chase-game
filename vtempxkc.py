import pygame
from zfiblejg import*
from entities import gxlk8wru
from wczh9ier import oohp6vz4,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.tby49e7e=pygame.Rect(ygspk9p3//2-rqf5q14j//2,tp0lvsnu-90,rqf5q14j,rqf5q14j)
  self.p7b1ijiy=yswjckjl
  self.k7zgf9q5=iq5c34dx['c37qqy']
  self.jxxgaear={'v00vhm':0,'w9laac':-1}
 def mmn32u1i(self):
  ry181acj=pygame.key.get_pressed()
  pbo119xp=mq7nc85e=0
  if ry181acj[pygame.K_UP]:
   mq7nc85e-=self.p7b1ijiy
  if ry181acj[pygame.K_DOWN]:
   mq7nc85e+=self.p7b1ijiy
  if ry181acj[pygame.K_LEFT]:
   pbo119xp-=self.p7b1ijiy
  if ry181acj[pygame.K_RIGHT]:
   pbo119xp+=self.p7b1ijiy
  if pbo119xp!=0 and mq7nc85e!=0:
   pbo119xp*=0.707
   mq7nc85e*=0.707
  if pbo119xp!=0 or mq7nc85e!=0:
   self.jxxgaear['v00vhm']=pbo119xp
   self.jxxgaear['w9laac']=mq7nc85e
  self.tby49e7e.x3zo7utx+=pbo119xp
  self.tby49e7e.cjy62zee+=mq7nc85e
  self.tby49e7e.x3zo7utx=max(0,min(self.tby49e7e.x3zo7utx,ygspk9p3-self.tby49e7e.width))
  self.tby49e7e.cjy62zee=max(60,min(self.tby49e7e.cjy62zee,tp0lvsnu-self.tby49e7e.height))
 def dw7nh8rq(self,uwxrum2l):
  (x3zo7utx,cjy62zee)=(self.tby49e7e.x3zo7utx,self.tby49e7e.cjy62zee)
  (rmm1zxyv,g8kk791z)=(self.tby49e7e.centerx,self.tby49e7e.centery)
  y9ayq6ww=pygame.Surface((self.tby49e7e.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(y9ayq6ww,(0,0,0,80),y9ayq6ww.get_rect())
  uwxrum2l.blit(y9ayq6ww,(rmm1zxyv-y9ayq6ww.get_width()//2,cjy62zee+self.tby49e7e.height-6))
  qbm1enf3=pygame.Rect(x3zo7utx,cjy62zee,self.tby49e7e.width,self.tby49e7e.height)
  pygame.draw.rect(uwxrum2l,gxlk8wru(self.k7zgf9q5,0.55),qbm1enf3,border_radius=10)
  o4dd1vn8=qbm1enf3.inflate(-5,-5)
  pygame.draw.rect(uwxrum2l,self.k7zgf9q5,o4dd1vn8,border_radius=8)
  rk2u1rsu=pygame.Rect(o4dd1vn8.x3zo7utx+3,o4dd1vn8.cjy62zee+3,o4dd1vn8.width//2,o4dd1vn8.height//3)
  pygame.draw.rect(uwxrum2l,gxlk8wru(self.k7zgf9q5,2.0),rk2u1rsu,border_radius=4)
  pygame.draw.rect(uwxrum2l,(15,15,30),qbm1enf3,width=2,border_radius=10)
class my6wktak:
 def __init__(self,wb7f6fdh,vqnpcenl,color,x3zo7utx,cjy62zee):
  self.wb7f6fdh=wb7f6fdh
  self.vqnpcenl=vqnpcenl
  self.k7zgf9q5=color
  self.tby49e7e=pygame.Rect(x3zo7utx,cjy62zee,34,34)
  self.ub68rerv=False
 def dw7nh8rq(self,uwxrum2l,x9bp4m18):
  y9ayq6ww=pygame.Surface((self.tby49e7e.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(y9ayq6ww,(0,0,0,70),y9ayq6ww.get_rect())
  uwxrum2l.blit(y9ayq6ww,(self.tby49e7e.centerx-y9ayq6ww.get_width()//2,self.tby49e7e.bottom-4))
  qbm1enf3=pygame.Rect(self.tby49e7e.x3zo7utx,self.tby49e7e.cjy62zee,self.tby49e7e.width,self.tby49e7e.height)
  pygame.draw.rect(uwxrum2l,gxlk8wru(self.k7zgf9q5,0.6),qbm1enf3,border_radius=8)
  o4dd1vn8=qbm1enf3.inflate(-5,-5)
  pygame.draw.rect(uwxrum2l,self.k7zgf9q5,o4dd1vn8,border_radius=6)
  pygame.draw.rect(uwxrum2l,(15,15,15),qbm1enf3,width=2,border_radius=8)
  (rmm1zxyv,g8kk791z)=(self.tby49e7e.centerx,self.tby49e7e.centery)
  pygame.draw.circle(uwxrum2l,iq5c34dx['edxoq2'],(rmm1zxyv-6,g8kk791z-3),3)
  pygame.draw.circle(uwxrum2l,iq5c34dx['edxoq2'],(rmm1zxyv+6,g8kk791z-3),3)
  pygame.draw.circle(uwxrum2l,iq5c34dx['p4ta5i'],(rmm1zxyv-6,g8kk791z-3),1)
  pygame.draw.circle(uwxrum2l,iq5c34dx['p4ta5i'],(rmm1zxyv+6,g8kk791z-3),1)
  n04cdpqv=x9bp4m18.render(self.wb7f6fdh,True,(20,20,20))
  uwxrum2l.blit(n04cdpqv,(rmm1zxyv-n04cdpqv.get_width()//2,self.tby49e7e.cjy62zee-20))
def dq2fa39e():
 return[my6wktak('Vera','sce4qg',iq5c34dx['da7yvd'],120,140),my6wktak('Duncan','ijj0v6',iq5c34dx['k1yjfe'],383,110),my6wktak('Mira','hrctlt',iq5c34dx['tudttj'],650,140)]
yex8fsv8={'sce4qg':'Vitality Shop - Vera','ijj0v6':'Combat Shop - Duncan','hrctlt':'Mobility Shop - Mira'}
def zpfb3hn1(key,j1ldqnk2):
 avfmh07w=jsylztgx[key]
 return int(avfmh07w['ktaq6u']*avfmh07w['xfq3jz']**j1ldqnk2)
def hugysm8t(f80ebkjf,vqnpcenl,m8lw2qit):
 (x9bp4m18,hdw6lqwl,uz6kf162,jm25len6)=m8lw2qit
 ry181acj=[k for(k,acxx6mdk)in jsylztgx.items()if acxx6mdk['kp82kb']==vqnpcenl]
 pv4ykade=110*len(ry181acj)+20
 tkyrmjlj=oohp6vz4(420,pv4ykade+oohp6vz4.rla5ju9b+60,z0xkxwd8,title=yex8fsv8.get(vqnpcenl,'Shop'),title_font=uz6kf162)
 i01nouht=tkyrmjlj.tby49e7e.cjy62zee+tkyrmjlj.sdeekgys
 d1ieixwc=pv4ykade//len(ry181acj)
 for(bokzixza,key)in enumerate(ry181acj):
  avfmh07w=jsylztgx[key]
  yvffqot8=f80ebkjf['meta_upgrades'].get(key,0)
  jr5rdnpx=yvffqot8>=avfmh07w['jz6wmd']
  if jr5rdnpx:
   title=f"{avfmh07w['riny2e']}  MAX LEVEL"
  else:
   do2m71hs=zpfb3hn1(key,yvffqot8)
   title=f"{avfmh07w['riny2e']}  Lv.{yvffqot8} -> {yvffqot8 + 1}   [{do2m71hs} res]"
  tacj4t0s=hc58drc1(tkyrmjlj.tby49e7e.x3zo7utx+12,i01nouht+bokzixza*d1ieixwc+6,tkyrmjlj.tby49e7e.width-24,d1ieixwc-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,jm25len6,title,12,subtitle=avfmh07w['kj2jvq'],sub_font=hdw6lqwl,kind='meta',key=key)
  tacj4t0s.maxed=jr5rdnpx
  tkyrmjlj.add(tacj4t0s)
 bfoqmf5l=i01nouht+len(ry181acj)*d1ieixwc+12
 rk8r2ykc=hc58drc1(tkyrmjlj.tby49e7e.x3zo7utx+12,bfoqmf5l,tkyrmjlj.tby49e7e.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),jm25len6,'Close (ESC)',10,kind='close',key=None)
 tkyrmjlj.add(rk8r2ykc)
 return tkyrmjlj
def rk43safy(uwxrum2l,u1jhuwb6,f80ebkjf,stv18kgy):
 x9bp4m18=pygame.font.SysFont('arial',22)
 hdw6lqwl=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 uz6kf162=pygame.font.SysFont('arial',22,bold=True)
 jm25len6=pygame.font.SysFont('arial',20,bold=True)
 cp91i3vm=pygame.font.SysFont('arial',15)
 m8lw2qit=(x9bp4m18,hdw6lqwl,uz6kf162,jm25len6)
 g11kerpe=zbqe7ckw()
 ncyh3fvl=dq2fa39e()
 jenvg3kk=pygame.Rect(ygspk9p3//2-70,tp0lvsnu-60,140,44)
 b06xkxb9=None
 d0r2sds8=None
 while True:
  mqxlm5q2=pygame.event.get()
  for yrivh6t1 in mqxlm5q2:
   if yrivh6t1.type==pygame.QUIT:
    return'quit'
   if yrivh6t1.type==pygame.KEYDOWN and yrivh6t1.key==pygame.K_ESCAPE and b06xkxb9:
    b06xkxb9=None
    d0r2sds8=None
  if b06xkxb9 is None:
   g11kerpe.mmn32u1i()
   hjkuuhcl=None
   for ee1g983e in ncyh3fvl:
    if g11kerpe.tby49e7e.colliderect(ee1g983e.tby49e7e.inflate(24,24)):
     if not ee1g983e.ub68rerv:
      hjkuuhcl=ee1g983e
      ee1g983e.ub68rerv=True
      break
    else:
     ee1g983e.ub68rerv=False
   if hjkuuhcl:
    d0r2sds8=hjkuuhcl.vqnpcenl
    b06xkxb9=hugysm8t(f80ebkjf,d0r2sds8,m8lw2qit)
   if g11kerpe.tby49e7e.colliderect(jenvg3kk):
    return'start_game'
  else:
   for aicvqy5i in b06xkxb9.k2ixivzk:
    aicvqy5i.update(mqxlm5q2)
   vw6m7b5c=next((le9oe941 for le9oe941 in b06xkxb9.k2ixivzk if le9oe941.vw6m7b5c),None)
   if vw6m7b5c is not None:
    if vw6m7b5c.kind=='close':
     b06xkxb9=None
     d0r2sds8=None
    elif vw6m7b5c.kind=='meta'and(not getattr(vw6m7b5c,'maxed',False)):
     key=vw6m7b5c.key
     yvffqot8=f80ebkjf['meta_upgrades'].get(key,0)
     do2m71hs=zpfb3hn1(key,yvffqot8)
     if f80ebkjf['resources']>=do2m71hs:
      f80ebkjf['resources']-=do2m71hs
      f80ebkjf['meta_upgrades'][key]=yvffqot8+1
      stv18kgy(f80ebkjf)
      b06xkxb9=hugysm8t(f80ebkjf,d0r2sds8,m8lw2qit)
  uwxrum2l.fill((190,225,190))
  for zpajssuu in range(0,ygspk9p3,m7hv3izk):
   pygame.draw.line(uwxrum2l,(160,205,160),(zpajssuu,0),(zpajssuu,tp0lvsnu),1)
  for onqyyf9r in range(0,tp0lvsnu,m7hv3izk):
   pygame.draw.line(uwxrum2l,(160,205,160),(0,onqyyf9r),(ygspk9p3,onqyyf9r),1)
  pygame.draw.rect(uwxrum2l,iq5c34dx['ew6tm2'],jenvg3kk,border_radius=10)
  pygame.draw.rect(uwxrum2l,(150,110,0),jenvg3kk,width=3,border_radius=10)
  k1taa0i5=hdw6lqwl.render('ENTER RUN',True,(40,30,0))
  uwxrum2l.blit(k1taa0i5,(jenvg3kk.centerx-k1taa0i5.get_width()//2,jenvg3kk.centery-k1taa0i5.get_height()//2))
  for ee1g983e in ncyh3fvl:
   ee1g983e.dw7nh8rq(uwxrum2l,hdw6lqwl)
  g11kerpe.dw7nh8rq(uwxrum2l)
  fpa8hyex=pygame.Rect(12,12,220,40)
  f55dmcxx=pygame.Surface((fpa8hyex.width,fpa8hyex.height),pygame.SRCALPHA)
  pygame.draw.rect(f55dmcxx,(255,255,255,160),f55dmcxx.get_rect(),border_radius=10)
  uwxrum2l.blit(f55dmcxx,fpa8hyex.topleft)
  cq2q4qer=x9bp4m18.render(f"Resources: {f80ebkjf['resources']}",True,(20,20,20))
  uwxrum2l.blit(cq2q4qer,(20,22))
  it04chsd=title_font.render('HOMEBASE',True,(20,40,20))
  uwxrum2l.blit(it04chsd,(ygspk9p3//2-it04chsd.get_width()//2,12))
  nd31k9qm=cp91i3vm.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  uwxrum2l.blit(nd31k9qm,(ygspk9p3//2-nd31k9qm.get_width()//2,tp0lvsnu-105))
  if b06xkxb9:
   b06xkxb9.dw7nh8rq(uwxrum2l)
  pygame.display.flip()
  u1jhuwb6.tick(pi3qk2ia)
