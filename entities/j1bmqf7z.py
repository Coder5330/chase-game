import pygame
import math
from entfk7or import*
from.pmpxkc5i import y9ayq6ww,vhuds3qs
pygame.init()
rv86wzs3=pygame.Surface((rqf5q14j+16,14),pygame.SRCALPHA)
pygame.draw.ellipse(rv86wzs3,(0,0,0,90),rv86wzs3.get_rect())
def ouuylaja(h8s2ftom,npcxa5s0,ejwtl9tq=120,tj0nmeoq=10):
 p7pchcbn=pygame.Surface((npcxa5s0.width,npcxa5s0.height),pygame.SRCALPHA)
 pygame.draw.rect(p7pchcbn,(255,255,255,ejwtl9tq),p7pchcbn.get_rect(),border_radius=tj0nmeoq)
 h8s2ftom.blit(p7pchcbn,npcxa5s0.topleft)
class r0tvhhpb:
 def __init__(self,meta_upgrades=None):
  meta_upgrades=meta_upgrades or{}
  wg25cfzf=meta_upgrades.get('START_HEALTH',0)
  j0kgazu4=meta_upgrades.get('START_SPEED',0)
  s8438tgb=meta_upgrades.get('START_DAMAGE',0)
  hu9n79gi=meta_upgrades.get('START_COOLDOWN',0)
  fdxj37c9=meta_upgrades.get('START_ARMOR',0)
  w8y72ivg=meta_upgrades.get('START_REGEN',0)
  self.llxxezdu=yswjckjl*y8bv78hu(j0kgazu4)
  self.q6nqqb9l=self.llxxezdu
  self.npcxa5s0=pygame.Rect((v83tqll8-rqf5q14j)//2,(cqoldfor-rqf5q14j)//2,rqf5q14j,rqf5q14j)
  self.pa8s8hmb=iq5c34dx['tjng7l']
  self.wppsfnko=int(1000*d448n7od(wg25cfzf))
  self.r2muljav=self.wppsfnko
  self.ftrflqbm=self.wppsfnko
  self.m9bn18gp=0
  self.xwqvr1h6=1
  self.zpfb3hn1=False
  self.ls2zge2j={'nddqhk':0,'gbwcv6':self.q6nqqb9l}
  self.hiac2e4q={}
  self.w2kql0ht={key:0 for key in rcfnfhol}
  self.jc54wsqt=bihsa7he(s8438tgb)
  self.j2vmcqbn=k3z6bz8u(hu9n79gi)
  self.f8wquuy5=a62c9t19(fdxj37c9)
  self.i0x65muf=jl90pxrl(w8y72ivg)
  self.wc7x0h3j=self.jc54wsqt
  self.do2m71hs=self.j2vmcqbn
  self.o3q0e27z=1.0
  self.duhxid4n=self.f8wquuy5
  self.xu9ymszd=self.i0x65muf
  self.v0rxxf36=pi3qk2ia
  self.qcd81twh=False
  self.u15pdtz9=0
  self.cqheyto5=[]
  self.zflv1xxl=0
  self.n04cdpqv=0
  self.m8lw2qit=pygame.font.SysFont('arial',20,bold=True)
 def x03uvule(self,key):
  self.w2kql0ht[key]+=1
  gqq4d3kz=self.w2kql0ht[key]
  if key=='jyzqii':
   wydmt8vt=int(self.wppsfnko*(1+0.2*gqq4d3kz))
   self.ftrflqbm+=wydmt8vt-self.r2muljav
   self.r2muljav=wydmt8vt
  elif key=='m44c68':
   self.q6nqqb9l=self.llxxezdu*(1+0.08*gqq4d3kz)
  elif key=='y3lxch':
   self.xu9ymszd=self.i0x65muf+gqq4d3kz
  elif key=='z9kvls':
   self.wc7x0h3j=self.jc54wsqt*(1+0.06*gqq4d3kz)
  elif key=='c14cqe':
   self.do2m71hs=self.j2vmcqbn*max(0.6,1-0.05*gqq4d3kz)
  elif key=='eff1bl':
   self.duhxid4n=self.f8wquuy5+gqq4d3kz*5
  elif key=='hzj7ub':
   self.o3q0e27z=1+0.15*gqq4d3kz
 def a8ax40dt(self,cu8el501):
  self.hiac2e4q[cu8el501]=self.hiac2e4q.get(cu8el501,1)+1
 def oc4kl8cg(self):
  b78okz1p=pygame.key.get_pressed()
  mq7nc85e=le9oe941=0
  if b78okz1p[pygame.K_UP]:
   le9oe941-=self.q6nqqb9l
  if b78okz1p[pygame.K_DOWN]:
   le9oe941+=self.q6nqqb9l
  if b78okz1p[pygame.K_LEFT]:
   mq7nc85e-=self.q6nqqb9l
  if b78okz1p[pygame.K_RIGHT]:
   mq7nc85e+=self.q6nqqb9l
  if mq7nc85e!=0 and le9oe941!=0:
   mq7nc85e*=0.707
   le9oe941*=0.707
  if mq7nc85e!=0 or le9oe941!=0:
   self.ls2zge2j['nddqhk']=mq7nc85e
   self.ls2zge2j['gbwcv6']=le9oe941
  self.npcxa5s0.w2sq3b9s+=mq7nc85e+self.zflv1xxl
  self.npcxa5s0.owdz09wf+=le9oe941+self.n04cdpqv
  if self.zflv1xxl>0:
   self.zflv1xxl=max(0,self.zflv1xxl-1)
  elif self.zflv1xxl<0:
   self.zflv1xxl=min(0,self.zflv1xxl+1)
  if self.n04cdpqv>0:
   self.n04cdpqv=max(0,self.n04cdpqv-1)
  elif self.n04cdpqv<0:
   self.n04cdpqv=min(0,self.n04cdpqv+1)
  self.npcxa5s0.w2sq3b9s=max(min(self.npcxa5s0.w2sq3b9s,v83tqll8-self.npcxa5s0.width),0)
  self.npcxa5s0.owdz09wf=max(min(self.npcxa5s0.owdz09wf,cqoldfor-self.npcxa5s0.height),0)
  if self.xu9ymszd>0 and self.ftrflqbm<self.r2muljav:
   self.v0rxxf36-=1
   if self.v0rxxf36<=0:
    self.v0rxxf36=pi3qk2ia
    self.ftrflqbm=min(self.r2muljav,self.ftrflqbm+self.xu9ymszd)
  if self.m9bn18gp>=m53a5qbs[min(self.xwqvr1h6,len(m53a5qbs)-1)]:
   self.zpfb3hn1=True
   self.m9bn18gp=0
   self.xwqvr1h6+=1
 def tnz61231(self,h8s2ftom,obc2nnuv,vqnpcenl):
  w2sq3b9s=self.npcxa5s0.w2sq3b9s-obc2nnuv
  owdz09wf=self.npcxa5s0.owdz09wf-vqnpcenl
  g8kk791z=self.npcxa5s0.centerx-obc2nnuv
  wzlm72je=self.npcxa5s0.centery-vqnpcenl
  h8s2ftom.blit(rv86wzs3,(g8kk791z-rv86wzs3.get_width()//2,owdz09wf+self.npcxa5s0.height-8))
  tk0qtl3q=pygame.Rect(w2sq3b9s,owdz09wf,self.npcxa5s0.width,self.npcxa5s0.height)
  pygame.draw.rect(h8s2ftom,y9ayq6ww(self.pa8s8hmb,0.55),tk0qtl3q,border_radius=10)
  ub68rerv=tk0qtl3q.inflate(-5,-5)
  pygame.draw.rect(h8s2ftom,self.pa8s8hmb,ub68rerv,border_radius=8)
  nd31k9qm=pygame.Rect(ub68rerv.w2sq3b9s+3,ub68rerv.owdz09wf+3,ub68rerv.width//2,ub68rerv.height//3)
  pygame.draw.rect(h8s2ftom,y9ayq6ww(self.pa8s8hmb,2.0),nd31k9qm,border_radius=4)
  pygame.draw.rect(h8s2ftom,(15,15,30),tk0qtl3q,width=2,border_radius=10)
  j1ldqnk2=math.hypot(self.ls2zge2j['nddqhk'],self.ls2zge2j['gbwcv6'])or 1
  (mu4fmpkx,trdhw9re)=(self.ls2zge2j['nddqhk']/j1ldqnk2,self.ls2zge2j['gbwcv6']/j1ldqnk2)
  tza7x73q=(g8kk791z+mu4fmpkx*20,wzlm72je+trdhw9re*20)
  sye0a4ab=(g8kk791z-trdhw9re*7+mu4fmpkx*4,wzlm72je+mu4fmpkx*7+trdhw9re*4)
  q26yg3dx=(g8kk791z+trdhw9re*7+mu4fmpkx*4,wzlm72je-mu4fmpkx*7+trdhw9re*4)
  pygame.draw.polygon(h8s2ftom,iq5c34dx['mmgvu4'],[tza7x73q,sye0a4ab,q26yg3dx])
  pygame.draw.polygon(h8s2ftom,(15,15,30),[tza7x73q,sye0a4ab,q26yg3dx],width=1)
  myrp5ge0=self.ftrflqbm/self.r2muljav
  vhuds3qs(h8s2ftom,w2sq3b9s,owdz09wf-10,self.npcxa5s0.width,myrp5ge0,height=6)
  ouuylaja(h8s2ftom,pygame.Rect(225,12,372,40))
  p7pchcbn=self.m8lw2qit.render('Hp.',True,(20,20,20))
  h8s2ftom.blit(p7pchcbn,(233,23))
  vhuds3qs(h8s2ftom,297,25,290,myrp5ge0,height=19)
  p7pchcbn=self.m8lw2qit.render(f'{round(self.ftrflqbm)}/{self.r2muljav}',True,(20,20,20))
  width=p7pchcbn.get_width()
  height=p7pchcbn.get_height()
  h8s2ftom.blit(p7pchcbn,(442-width//2,34.5-height//2))
