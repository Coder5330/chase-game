import pygame
from omerbyea import*
from entities import u15pdtz9
from odog8cfe import oohp6vz4,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.cq2q4qer=pygame.Rect(cqoldfor//2-rqf5q14j//2,tp0lvsnu-90,rqf5q14j,rqf5q14j)
  self.holeyrvx=yswjckjl
  self.k7zgf9q5=iq5c34dx['mviifr']
  self.d1b3jczu={'dzjq7w':0,'i1yy1j':-1}
 def got7txkd(self):
  mctwjlsh=pygame.key.get_pressed()
  mq7nc85e=le9oe941=0
  if mctwjlsh[pygame.K_UP]:
   le9oe941-=self.holeyrvx
  if mctwjlsh[pygame.K_DOWN]:
   le9oe941+=self.holeyrvx
  if mctwjlsh[pygame.K_LEFT]:
   mq7nc85e-=self.holeyrvx
  if mctwjlsh[pygame.K_RIGHT]:
   mq7nc85e+=self.holeyrvx
  if mq7nc85e!=0 and le9oe941!=0:
   mq7nc85e*=0.707
   le9oe941*=0.707
  if mq7nc85e!=0 or le9oe941!=0:
   self.d1b3jczu['dzjq7w']=mq7nc85e
   self.d1b3jczu['i1yy1j']=le9oe941
  self.cq2q4qer.eolaq665+=mq7nc85e
  self.cq2q4qer.t5ivrocv+=le9oe941
  self.cq2q4qer.eolaq665=max(0,min(self.cq2q4qer.eolaq665,cqoldfor-self.cq2q4qer.width))
  self.cq2q4qer.t5ivrocv=max(60,min(self.cq2q4qer.t5ivrocv,tp0lvsnu-self.cq2q4qer.height))
 def tnz61231(self,q3n2qb6g):
  (eolaq665,t5ivrocv)=(self.cq2q4qer.eolaq665,self.cq2q4qer.t5ivrocv)
  (g8kk791z,wzlm72je)=(self.cq2q4qer.centerx,self.cq2q4qer.centery)
  yp3cyazb=pygame.Surface((self.cq2q4qer.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(yp3cyazb,(0,0,0,80),yp3cyazb.get_rect())
  q3n2qb6g.blit(yp3cyazb,(g8kk791z-yp3cyazb.get_width()//2,t5ivrocv+self.cq2q4qer.height-6))
  uysal8m1=pygame.Rect(eolaq665,t5ivrocv,self.cq2q4qer.width,self.cq2q4qer.height)
  pygame.draw.rect(q3n2qb6g,u15pdtz9(self.k7zgf9q5,0.55),uysal8m1,border_radius=10)
  wa45hvgo=uysal8m1.inflate(-5,-5)
  pygame.draw.rect(q3n2qb6g,self.k7zgf9q5,wa45hvgo,border_radius=8)
  i13n3bzt=pygame.Rect(wa45hvgo.eolaq665+3,wa45hvgo.t5ivrocv+3,wa45hvgo.width//2,wa45hvgo.height//3)
  pygame.draw.rect(q3n2qb6g,u15pdtz9(self.k7zgf9q5,2.0),i13n3bzt,border_radius=4)
  pygame.draw.rect(q3n2qb6g,(15,15,30),uysal8m1,width=2,border_radius=10)
class my6wktak:
 def __init__(self,zorxdtg5,uos0fb4y,color,eolaq665,t5ivrocv):
  self.zorxdtg5=zorxdtg5
  self.uos0fb4y=uos0fb4y
  self.k7zgf9q5=color
  self.cq2q4qer=pygame.Rect(eolaq665,t5ivrocv,34,34)
  self.ry181acj=False
 def tnz61231(self,q3n2qb6g,mpyxdw2z):
  yp3cyazb=pygame.Surface((self.cq2q4qer.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(yp3cyazb,(0,0,0,70),yp3cyazb.get_rect())
  q3n2qb6g.blit(yp3cyazb,(self.cq2q4qer.centerx-yp3cyazb.get_width()//2,self.cq2q4qer.bottom-4))
  uysal8m1=pygame.Rect(self.cq2q4qer.eolaq665,self.cq2q4qer.t5ivrocv,self.cq2q4qer.width,self.cq2q4qer.height)
  pygame.draw.rect(q3n2qb6g,u15pdtz9(self.k7zgf9q5,0.6),uysal8m1,border_radius=8)
  wa45hvgo=uysal8m1.inflate(-5,-5)
  pygame.draw.rect(q3n2qb6g,self.k7zgf9q5,wa45hvgo,border_radius=6)
  pygame.draw.rect(q3n2qb6g,(15,15,15),uysal8m1,width=2,border_radius=8)
  (g8kk791z,wzlm72je)=(self.cq2q4qer.centerx,self.cq2q4qer.centery)
  pygame.draw.circle(q3n2qb6g,iq5c34dx['qc6dr0'],(g8kk791z-6,wzlm72je-3),3)
  pygame.draw.circle(q3n2qb6g,iq5c34dx['qc6dr0'],(g8kk791z+6,wzlm72je-3),3)
  pygame.draw.circle(q3n2qb6g,iq5c34dx['m314cq'],(g8kk791z-6,wzlm72je-3),1)
  pygame.draw.circle(q3n2qb6g,iq5c34dx['m314cq'],(g8kk791z+6,wzlm72je-3),1)
  ls2zge2j=mpyxdw2z.render(self.zorxdtg5,True,(20,20,20))
  q3n2qb6g.blit(ls2zge2j,(g8kk791z-ls2zge2j.get_width()//2,self.cq2q4qer.t5ivrocv-20))
def lhgk5bwi():
 return[my6wktak('Vera','qbtr23',iq5c34dx['bdoz6w'],120,140),my6wktak('Duncan','jr87iy',iq5c34dx['c37qqy'],383,110),my6wktak('Mira','f4c3ev',iq5c34dx['w1q8f6'],650,140)]
yex8fsv8={'qbtr23':'Vitality Shop - Vera','jr87iy':'Combat Shop - Duncan','f4c3ev':'Mobility Shop - Mira'}
def acxx6mdk(key,y2f7atwy):
 k2ixivzk=jsylztgx[key]
 return int(k2ixivzk['xfq3jz']*k2ixivzk['mrf5a7']**y2f7atwy)
def d1ieixwc(y9ayq6ww,uos0fb4y,cjn2fomd):
 (mpyxdw2z,su1hbj6t,v6xii5p5,ugez7bh2)=cjn2fomd
 mctwjlsh=[k for(k,iimoe0sy)in jsylztgx.items()if iimoe0sy['pgsb98']==uos0fb4y]
 pv4ykade=110*len(mctwjlsh)+20
 rgdej31g=oohp6vz4(420,pv4ykade+oohp6vz4.rla5ju9b+60,z0xkxwd8,title=yex8fsv8.get(uos0fb4y,'Shop'),title_font=v6xii5p5)
 i01nouht=rgdej31g.cq2q4qer.t5ivrocv+rgdej31g.ftrflqbm
 zfb7r31q=pv4ykade//len(mctwjlsh)
 for(pcvsqame,key)in enumerate(mctwjlsh):
  k2ixivzk=jsylztgx[key]
  dq2fa39e=y9ayq6ww['meta_upgrades'].get(key,0)
  fdxj37c9=dq2fa39e>=k2ixivzk['ua6wix']
  if fdxj37c9:
   title=f"{k2ixivzk['hrctlt']}  MAX LEVEL"
  else:
   do2m71hs=acxx6mdk(key,dq2fa39e)
   title=f"{k2ixivzk['hrctlt']}  Lv.{dq2fa39e} -> {dq2fa39e + 1}   [{do2m71hs} res]"
  li9nb74x=hc58drc1(rgdej31g.cq2q4qer.eolaq665+12,i01nouht+pcvsqame*zfb7r31q+6,rgdej31g.cq2q4qer.width-24,zfb7r31q-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,ugez7bh2,title,12,subtitle=k2ixivzk['en1x2g'],sub_font=su1hbj6t,kind='meta',key=key)
  li9nb74x.maxed=fdxj37c9
  rgdej31g.add(li9nb74x)
 bfoqmf5l=i01nouht+len(mctwjlsh)*zfb7r31q+12
 rk8r2ykc=hc58drc1(rgdej31g.cq2q4qer.eolaq665+12,bfoqmf5l,rgdej31g.cq2q4qer.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),ugez7bh2,'Close (ESC)',10,kind='close',key=None)
 rgdej31g.add(rk8r2ykc)
 return rgdej31g
def stv18kgy(q3n2qb6g,u1jhuwb6,y9ayq6ww,gxlk8wru):
 mpyxdw2z=pygame.font.SysFont('arial',22)
 su1hbj6t=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 v6xii5p5=pygame.font.SysFont('arial',22,bold=True)
 ugez7bh2=pygame.font.SysFont('arial',20,bold=True)
 wvpw232u=pygame.font.SysFont('arial',15)
 cjn2fomd=(mpyxdw2z,su1hbj6t,v6xii5p5,ugez7bh2)
 sv5f1bcp=zbqe7ckw()
 njxurgow=lhgk5bwi()
 npejzhya=pygame.Rect(cqoldfor//2-70,tp0lvsnu-60,140,44)
 i4fejgxa=None
 ytv3i12v=None
 while True:
  eatvzkhi=pygame.event.get()
  for xq46nouh in eatvzkhi:
   if xq46nouh.type==pygame.QUIT:
    return'quit'
   if xq46nouh.type==pygame.KEYDOWN and xq46nouh.key==pygame.K_ESCAPE and i4fejgxa:
    i4fejgxa=None
    ytv3i12v=None
  if i4fejgxa is None:
   sv5f1bcp.got7txkd()
   m81udp2f=None
   for y8dd2255 in njxurgow:
    if sv5f1bcp.cq2q4qer.colliderect(y8dd2255.cq2q4qer.inflate(24,24)):
     if not y8dd2255.ry181acj:
      m81udp2f=y8dd2255
      y8dd2255.ry181acj=True
      break
    else:
     y8dd2255.ry181acj=False
   if m81udp2f:
    ytv3i12v=m81udp2f.uos0fb4y
    i4fejgxa=d1ieixwc(y9ayq6ww,ytv3i12v,cjn2fomd)
   if sv5f1bcp.cq2q4qer.colliderect(npejzhya):
    return'start_game'
  else:
   for boih5csk in i4fejgxa.ub68rerv:
    boih5csk.update(eatvzkhi)
   vw6m7b5c=next((jqzpniqf for jqzpniqf in i4fejgxa.ub68rerv if jqzpniqf.vw6m7b5c),None)
   if vw6m7b5c is not None:
    if vw6m7b5c.kind=='close':
     i4fejgxa=None
     ytv3i12v=None
    elif vw6m7b5c.kind=='meta'and(not getattr(vw6m7b5c,'maxed',False)):
     key=vw6m7b5c.key
     dq2fa39e=y9ayq6ww['meta_upgrades'].get(key,0)
     do2m71hs=acxx6mdk(key,dq2fa39e)
     if y9ayq6ww['resources']>=do2m71hs:
      y9ayq6ww['resources']-=do2m71hs
      y9ayq6ww['meta_upgrades'][key]=dq2fa39e+1
      gxlk8wru(y9ayq6ww)
      i4fejgxa=d1ieixwc(y9ayq6ww,ytv3i12v,cjn2fomd)
  q3n2qb6g.fill((190,225,190))
  for jo8e7flq in range(0,cqoldfor,vve92mpn):
   pygame.draw.line(q3n2qb6g,(160,205,160),(jo8e7flq,0),(jo8e7flq,tp0lvsnu),1)
  for gsmdzqcb in range(0,tp0lvsnu,vve92mpn):
   pygame.draw.line(q3n2qb6g,(160,205,160),(0,gsmdzqcb),(cqoldfor,gsmdzqcb),1)
  pygame.draw.rect(q3n2qb6g,iq5c34dx['l226pa'],npejzhya,border_radius=10)
  pygame.draw.rect(q3n2qb6g,(150,110,0),npejzhya,width=3,border_radius=10)
  ytb9xxay=su1hbj6t.render('ENTER RUN',True,(40,30,0))
  q3n2qb6g.blit(ytb9xxay,(npejzhya.centerx-ytb9xxay.get_width()//2,npejzhya.centery-ytb9xxay.get_height()//2))
  for y8dd2255 in njxurgow:
   y8dd2255.tnz61231(q3n2qb6g,su1hbj6t)
  sv5f1bcp.tnz61231(q3n2qb6g)
  f55dmcxx=pygame.Rect(12,12,220,40)
  bokzixza=pygame.Surface((f55dmcxx.width,f55dmcxx.height),pygame.SRCALPHA)
  pygame.draw.rect(bokzixza,(255,255,255,160),bokzixza.get_rect(),border_radius=10)
  q3n2qb6g.blit(bokzixza,f55dmcxx.topleft)
  gg7oq2zd=mpyxdw2z.render(f"Resources: {y9ayq6ww['resources']}",True,(20,20,20))
  q3n2qb6g.blit(gg7oq2zd,(20,22))
  zgomf9pm=title_font.render('HOMEBASE',True,(20,40,20))
  q3n2qb6g.blit(zgomf9pm,(cqoldfor//2-zgomf9pm.get_width()//2,12))
  cp91i3vm=wvpw232u.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  q3n2qb6g.blit(cp91i3vm,(cqoldfor//2-cp91i3vm.get_width()//2,tp0lvsnu-105))
  if i4fejgxa:
   i4fejgxa.tnz61231(q3n2qb6g)
  pygame.display.flip()
  u1jhuwb6.tick(pi3qk2ia)
