import pygame
from v7bnhjw6 import*
from entities import qertb74r
from zhm40oey import rcfnfhol,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.jenvg3kk=pygame.Rect(v4u89yjb//2-rv86wzs3//2,rla5ju9b-90,rv86wzs3,rv86wzs3)
  self.xvzc7d2k=rqf5q14j
  self.lztkkfzz=iq5c34dx['m314cq']
  self.fpa8hyex={'e56waf':0,'eqkwqh':-1}
 def r2muljav(self):
  swwnc21o=pygame.key.get_pressed()
  x875aud9=jqxs6esj=0
  if swwnc21o[pygame.K_UP]:
   jqxs6esj-=self.xvzc7d2k
  if swwnc21o[pygame.K_DOWN]:
   jqxs6esj+=self.xvzc7d2k
  if swwnc21o[pygame.K_LEFT]:
   x875aud9-=self.xvzc7d2k
  if swwnc21o[pygame.K_RIGHT]:
   x875aud9+=self.xvzc7d2k
  if x875aud9!=0 and jqxs6esj!=0:
   x875aud9*=0.707
   jqxs6esj*=0.707
  if x875aud9!=0 or jqxs6esj!=0:
   self.fpa8hyex['e56waf']=x875aud9
   self.fpa8hyex['eqkwqh']=jqxs6esj
  self.jenvg3kk.qic1l7dy+=x875aud9
  self.jenvg3kk.vsjchzjq+=jqxs6esj
  self.jenvg3kk.qic1l7dy=max(0,min(self.jenvg3kk.qic1l7dy,v4u89yjb-self.jenvg3kk.width))
  self.jenvg3kk.vsjchzjq=max(60,min(self.jenvg3kk.vsjchzjq,rla5ju9b-self.jenvg3kk.height))
 def wc7x0h3j(self,gg7oq2zd):
  (qic1l7dy,vsjchzjq)=(self.jenvg3kk.qic1l7dy,self.jenvg3kk.vsjchzjq)
  (pa8s8hmb,pv4ykade)=(self.jenvg3kk.centerx,self.jenvg3kk.centery)
  q26yg3dx=pygame.Surface((self.jenvg3kk.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(q26yg3dx,(0,0,0,80),q26yg3dx.get_rect())
  gg7oq2zd.blit(q26yg3dx,(pa8s8hmb-q26yg3dx.get_width()//2,vsjchzjq+self.jenvg3kk.height-6))
  divsolml=pygame.Rect(qic1l7dy,vsjchzjq,self.jenvg3kk.width,self.jenvg3kk.height)
  pygame.draw.rect(gg7oq2zd,qertb74r(self.lztkkfzz,0.55),divsolml,border_radius=10)
  cp91i3vm=divsolml.inflate(-5,-5)
  pygame.draw.rect(gg7oq2zd,self.lztkkfzz,cp91i3vm,border_radius=8)
  o9ros7yt=pygame.Rect(cp91i3vm.qic1l7dy+3,cp91i3vm.vsjchzjq+3,cp91i3vm.width//2,cp91i3vm.height//3)
  pygame.draw.rect(gg7oq2zd,qertb74r(self.lztkkfzz,2.0),o9ros7yt,border_radius=4)
  pygame.draw.rect(gg7oq2zd,(15,15,30),divsolml,width=2,border_radius=10)
class jsylztgx:
 def __init__(self,hu9n79gi,tacj4t0s,color,qic1l7dy,vsjchzjq):
  self.hu9n79gi=hu9n79gi
  self.tacj4t0s=tacj4t0s
  self.lztkkfzz=color
  self.jenvg3kk=pygame.Rect(qic1l7dy,vsjchzjq,34,34)
  self.v3e1ocjx=False
 def wc7x0h3j(self,gg7oq2zd,eatvzkhi):
  q26yg3dx=pygame.Surface((self.jenvg3kk.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(q26yg3dx,(0,0,0,70),q26yg3dx.get_rect())
  gg7oq2zd.blit(q26yg3dx,(self.jenvg3kk.centerx-q26yg3dx.get_width()//2,self.jenvg3kk.bottom-4))
  divsolml=pygame.Rect(self.jenvg3kk.qic1l7dy,self.jenvg3kk.vsjchzjq,self.jenvg3kk.width,self.jenvg3kk.height)
  pygame.draw.rect(gg7oq2zd,qertb74r(self.lztkkfzz,0.6),divsolml,border_radius=8)
  cp91i3vm=divsolml.inflate(-5,-5)
  pygame.draw.rect(gg7oq2zd,self.lztkkfzz,cp91i3vm,border_radius=6)
  pygame.draw.rect(gg7oq2zd,(15,15,15),divsolml,width=2,border_radius=8)
  (pa8s8hmb,pv4ykade)=(self.jenvg3kk.centerx,self.jenvg3kk.centery)
  pygame.draw.circle(gg7oq2zd,iq5c34dx['v9hbn5'],(pa8s8hmb-6,pv4ykade-3),3)
  pygame.draw.circle(gg7oq2zd,iq5c34dx['v9hbn5'],(pa8s8hmb+6,pv4ykade-3),3)
  pygame.draw.circle(gg7oq2zd,iq5c34dx['uk99jc'],(pa8s8hmb-6,pv4ykade-3),1)
  pygame.draw.circle(gg7oq2zd,iq5c34dx['uk99jc'],(pa8s8hmb+6,pv4ykade-3),1)
  zmybd2qe=eatvzkhi.render(self.hu9n79gi,True,(20,20,20))
  gg7oq2zd.blit(zmybd2qe,(pa8s8hmb-zmybd2qe.get_width()//2,self.jenvg3kk.vsjchzjq-20))
def sye0a4ab():
 return[jsylztgx('Vera','mjz6us',iq5c34dx['jl1qwe'],120,140),jsylztgx('Duncan','i6ozx2',iq5c34dx['pqpva5'],383,110),jsylztgx('Mira','fuxk0a',iq5c34dx['iwu3bf'],650,140)]
yex8fsv8={'mjz6us':'Vitality Shop - Vera','i6ozx2':'Combat Shop - Duncan','fuxk0a':'Mobility Shop - Mira'}
def bu4xszjn(key,o4dd1vn8):
 nd31k9qm=gncxll4z[key]
 return int(nd31k9qm['bdoz6w']*nd31k9qm['kqbrmq']**o4dd1vn8)
def llxxezdu(d1hm38ks,tacj4t0s,s4rxyj38):
 (eatvzkhi,h8s2ftom,njxurgow,tk0qtl3q)=s4rxyj38
 swwnc21o=[k for(k,htgsiwg0)in gncxll4z.items()if htgsiwg0['wzwl3z']==tacj4t0s]
 ruq9e5co=110*len(swwnc21o)+20
 y8dd2255=rcfnfhol(420,ruq9e5co+rcfnfhol.gokc1msy+60,n2vlpys2,title=yex8fsv8.get(tacj4t0s,'Shop'),title_font=njxurgow)
 wzs13c9x=y8dd2255.jenvg3kk.vsjchzjq+y8dd2255.kkzruin3
 kybwmlun=ruq9e5co//len(swwnc21o)
 for(ftrflqbm,key)in enumerate(swwnc21o):
  nd31k9qm=gncxll4z[key]
  jxxgaear=d1hm38ks['meta_upgrades'].get(key,0)
  xwqvr1h6=jxxgaear>=nd31k9qm['kp82kb']
  if xwqvr1h6:
   title=f"{nd31k9qm['e0s41k']}  MAX LEVEL"
  else:
   ep6beffl=bu4xszjn(key,jxxgaear)
   title=f"{nd31k9qm['e0s41k']}  Lv.{jxxgaear} -> {jxxgaear + 1}   [{ep6beffl} res]"
  wppsfnko=hc58drc1(y8dd2255.jenvg3kk.qic1l7dy+12,wzs13c9x+ftrflqbm*kybwmlun+6,y8dd2255.jenvg3kk.width-24,kybwmlun-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,tk0qtl3q,title,12,subtitle=nd31k9qm['y3lxch'],sub_font=h8s2ftom,kind='meta',key=key)
  wppsfnko.maxed=xwqvr1h6
  y8dd2255.add(wppsfnko)
 iie0rnuj=wzs13c9x+len(swwnc21o)*kybwmlun+12
 vqnpcenl=hc58drc1(y8dd2255.jenvg3kk.qic1l7dy+12,iie0rnuj,y8dd2255.jenvg3kk.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),tk0qtl3q,'Close (ESC)',10,kind='close',key=None)
 y8dd2255.add(vqnpcenl)
 return y8dd2255
def tbxf445c(gg7oq2zd,obc2nnuv,d1hm38ks,h4l1vznq):
 eatvzkhi=pygame.font.SysFont('arial',22)
 h8s2ftom=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 njxurgow=pygame.font.SysFont('arial',22,bold=True)
 tk0qtl3q=pygame.font.SysFont('arial',20,bold=True)
 zpajssuu=pygame.font.SysFont('arial',15)
 s4rxyj38=(eatvzkhi,h8s2ftom,njxurgow,tk0qtl3q)
 d0r2sds8=zbqe7ckw()
 pf0i9g5d=sye0a4ab()
 uj64qhks=pygame.Rect(v4u89yjb//2-70,rla5ju9b-60,140,44)
 yx4w6xlp=None
 j1i2hgj1=None
 while True:
  mq7nc85e=pygame.event.get()
  for pbo119xp in mq7nc85e:
   if pbo119xp.type==pygame.QUIT:
    return'quit'
   if pbo119xp.type==pygame.KEYDOWN and pbo119xp.key==pygame.K_ESCAPE and yx4w6xlp:
    yx4w6xlp=None
    j1i2hgj1=None
  if yx4w6xlp is None:
   d0r2sds8.r2muljav()
   f2voi8uy=None
   for y8bv78hu in pf0i9g5d:
    if d0r2sds8.jenvg3kk.colliderect(y8bv78hu.jenvg3kk.inflate(24,24)):
     if not y8bv78hu.v3e1ocjx:
      f2voi8uy=y8bv78hu
      y8bv78hu.v3e1ocjx=True
      break
    else:
     y8bv78hu.v3e1ocjx=False
   if f2voi8uy:
    j1i2hgj1=f2voi8uy.tacj4t0s
    yx4w6xlp=llxxezdu(d1hm38ks,j1i2hgj1,s4rxyj38)
   if d0r2sds8.jenvg3kk.colliderect(uj64qhks):
    return'start_game'
  else:
   for yjluujmi in yx4w6xlp.wvpw232u:
    yjluujmi.update(mq7nc85e)
   uos0fb4y=next((zefqjg02 for zefqjg02 in yx4w6xlp.wvpw232u if zefqjg02.uos0fb4y),None)
   if uos0fb4y is not None:
    if uos0fb4y.kind=='close':
     yx4w6xlp=None
     j1i2hgj1=None
    elif uos0fb4y.kind=='meta'and(not getattr(uos0fb4y,'maxed',False)):
     key=uos0fb4y.key
     jxxgaear=d1hm38ks['meta_upgrades'].get(key,0)
     ep6beffl=bu4xszjn(key,jxxgaear)
     if d1hm38ks['resources']>=ep6beffl:
      d1hm38ks['resources']-=ep6beffl
      d1hm38ks['meta_upgrades'][key]=jxxgaear+1
      h4l1vznq(d1hm38ks)
      yx4w6xlp=llxxezdu(d1hm38ks,j1i2hgj1,s4rxyj38)
  gg7oq2zd.fill((190,225,190))
  for mpyxdw2z in range(0,v4u89yjb,m7hv3izk):
   pygame.draw.line(gg7oq2zd,(160,205,160),(mpyxdw2z,0),(mpyxdw2z,rla5ju9b),1)
  for cjn2fomd in range(0,rla5ju9b,m7hv3izk):
   pygame.draw.line(gg7oq2zd,(160,205,160),(0,cjn2fomd),(v4u89yjb,cjn2fomd),1)
  pygame.draw.rect(gg7oq2zd,iq5c34dx['dq3b9s'],uj64qhks,border_radius=10)
  pygame.draw.rect(gg7oq2zd,(150,110,0),uj64qhks,width=3,border_radius=10)
  exvaj2k8=h8s2ftom.render('ENTER RUN',True,(40,30,0))
  gg7oq2zd.blit(exvaj2k8,(uj64qhks.centerx-exvaj2k8.get_width()//2,uj64qhks.centery-exvaj2k8.get_height()//2))
  for y8bv78hu in pf0i9g5d:
   y8bv78hu.wc7x0h3j(gg7oq2zd,h8s2ftom)
  d0r2sds8.wc7x0h3j(gg7oq2zd)
  sdeekgys=pygame.Rect(12,12,220,40)
  nvuprt77=pygame.Surface((sdeekgys.width,sdeekgys.height),pygame.SRCALPHA)
  pygame.draw.rect(nvuprt77,(255,255,255,160),nvuprt77.get_rect(),border_radius=10)
  gg7oq2zd.blit(nvuprt77,sdeekgys.topleft)
  nxxjve3d=eatvzkhi.render(f"Resources: {d1hm38ks['resources']}",True,(20,20,20))
  gg7oq2zd.blit(nxxjve3d,(20,22))
  m3hcws2w=title_font.render('HOMEBASE',True,(20,40,20))
  gg7oq2zd.blit(m3hcws2w,(v4u89yjb//2-m3hcws2w.get_width()//2,12))
  vmxb9yo1=zpajssuu.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  gg7oq2zd.blit(vmxb9yo1,(v4u89yjb//2-vmxb9yo1.get_width()//2,rla5ju9b-105))
  if yx4w6xlp:
   yx4w6xlp.wc7x0h3j(gg7oq2zd)
  pygame.display.flip()
  obc2nnuv.tick(pi3qk2ia)
