import pygame
import math
from e87f8tsx import*
from.qxomxlvz import qcd81twh,b36htf4p
pygame.init()
rv86wzs3=pygame.Surface((rqf5q14j+16,14),pygame.SRCALPHA)
pygame.draw.ellipse(rv86wzs3,(0,0,0,90),rv86wzs3.get_rect())
def vhuds3qs(byl68ntk,pllkstn3,i4fejgxa=120,npcxa5s0=10):
 rk36m8jv=pygame.Surface((pllkstn3.width,pllkstn3.height),pygame.SRCALPHA)
 pygame.draw.rect(rk36m8jv,(255,255,255,i4fejgxa),rk36m8jv.get_rect(),border_radius=npcxa5s0)
 byl68ntk.blit(rk36m8jv,pllkstn3.topleft)
class ky20479t:
 def __init__(self,meta_upgrades=None):
  meta_upgrades=meta_upgrades or{}
  jl90pxrl=meta_upgrades.get('START_HEALTH',0)
  pf0i9g5d=meta_upgrades.get('START_SPEED',0)
  wg25cfzf=meta_upgrades.get('START_DAMAGE',0)
  s8438tgb=meta_upgrades.get('START_COOLDOWN',0)
  k3z6bz8u=meta_upgrades.get('START_ARMOR',0)
  y8bv78hu=meta_upgrades.get('START_REGEN',0)
  self.bq349dxb=yswjckjl*wy0mahym(pf0i9g5d)
  self.hcxhgnze=self.bq349dxb
  self.pllkstn3=pygame.Rect((v83tqll8-rqf5q14j)//2,(cqoldfor-rqf5q14j)//2,rqf5q14j,rqf5q14j)
  self.hfb85p86=iq5c34dx['kqbrmq']
  self.j2vmcqbn=int(1000*w8y72ivg(jl90pxrl))
  self.fdxj37c9=self.j2vmcqbn
  self.ftrflqbm=self.j2vmcqbn
  self.o3q0e27z=0
  self.xwqvr1h6=1
  self.w2kql0ht=False
  self.ls2zge2j={'gbwcv6':0,'g8wze4':self.hcxhgnze}
  self.a78iyhhg={}
  self.vsjchzjq={key:0 for key in rcfnfhol}
  self.u3ifhv1x=d448n7od(wg25cfzf)
  self.fcwtg1m8=bihsa7he(s8438tgb)
  self.mal2w37d=hu9n79gi(k3z6bz8u)
  self.z0b6ugvs=j0kgazu4(y8bv78hu)
  self.vt6om1fb=self.u3ifhv1x
  self.i01nouht=self.fcwtg1m8
  self.cjy62zee=1.0
  self.tp2ex5t5=self.mal2w37d
  self.cq2q4qer=self.z0b6ugvs
  self.uaobt328=pi3qk2ia
  self.cb2uuijn=False
  self.uoloeazc=0
  self.g1g1r1dw=[]
  self.zflv1xxl=0
  self.n04cdpqv=0
  self.m8lw2qit=pygame.font.SysFont('arial',20,bold=True)
 def mpdzp6lf(self,key):
  self.vsjchzjq[key]+=1
  vk3g84ut=self.vsjchzjq[key]
  if key=='i6ozx2':
   co4busu9=int(self.j2vmcqbn*(1+0.2*vk3g84ut))
   self.ftrflqbm+=co4busu9-self.fdxj37c9
   self.fdxj37c9=co4busu9
  elif key=='az3m55':
   self.hcxhgnze=self.bq349dxb*(1+0.08*vk3g84ut)
  elif key=='e56waf':
   self.cq2q4qer=self.z0b6ugvs+vk3g84ut
  elif key=='wkgeq2':
   self.vt6om1fb=self.u3ifhv1x*(1+0.06*vk3g84ut)
  elif key=='xy79kv':
   self.i01nouht=self.fcwtg1m8*max(0.6,1-0.05*vk3g84ut)
  elif key=='pta5iv':
   self.tp2ex5t5=self.mal2w37d+vk3g84ut*5
  elif key=='buzery':
   self.cjy62zee=1+0.15*vk3g84ut
 def a8ax40dt(self,gdg1wjui):
  self.a78iyhhg[gdg1wjui]=self.a78iyhhg.get(gdg1wjui,1)+1
 def wb7f6fdh(self):
  b78okz1p=pygame.key.get_pressed()
  pbo119xp=mq7nc85e=0
  if b78okz1p[pygame.K_UP]:
   mq7nc85e-=self.hcxhgnze
  if b78okz1p[pygame.K_DOWN]:
   mq7nc85e+=self.hcxhgnze
  if b78okz1p[pygame.K_LEFT]:
   pbo119xp-=self.hcxhgnze
  if b78okz1p[pygame.K_RIGHT]:
   pbo119xp+=self.hcxhgnze
  if pbo119xp!=0 and mq7nc85e!=0:
   pbo119xp*=0.707
   mq7nc85e*=0.707
  if pbo119xp!=0 or mq7nc85e!=0:
   self.ls2zge2j['gbwcv6']=pbo119xp
   self.ls2zge2j['g8wze4']=mq7nc85e
  self.pllkstn3.j1kfk7y6+=pbo119xp+self.zflv1xxl
  self.pllkstn3.f1bl08kg+=mq7nc85e+self.n04cdpqv
  if self.zflv1xxl>0:
   self.zflv1xxl=max(0,self.zflv1xxl-1)
  elif self.zflv1xxl<0:
   self.zflv1xxl=min(0,self.zflv1xxl+1)
  if self.n04cdpqv>0:
   self.n04cdpqv=max(0,self.n04cdpqv-1)
  elif self.n04cdpqv<0:
   self.n04cdpqv=min(0,self.n04cdpqv+1)
  self.pllkstn3.j1kfk7y6=max(min(self.pllkstn3.j1kfk7y6,v83tqll8-self.pllkstn3.width),0)
  self.pllkstn3.f1bl08kg=max(min(self.pllkstn3.f1bl08kg,cqoldfor-self.pllkstn3.height),0)
  if self.cq2q4qer>0 and self.ftrflqbm<self.fdxj37c9:
   self.uaobt328-=1
   if self.uaobt328<=0:
    self.uaobt328=pi3qk2ia
    self.ftrflqbm=min(self.fdxj37c9,self.ftrflqbm+self.cq2q4qer)
  if self.o3q0e27z>=m53a5qbs[min(self.xwqvr1h6,len(m53a5qbs)-1)]:
   self.w2kql0ht=True
   self.o3q0e27z=0
   self.xwqvr1h6+=1
 def dw7nh8rq(self,byl68ntk,i20cv3tl,clkqzfpq):
  j1kfk7y6=self.pllkstn3.j1kfk7y6-i20cv3tl
  f1bl08kg=self.pllkstn3.f1bl08kg-clkqzfpq
  rmm1zxyv=self.pllkstn3.centerx-i20cv3tl
  g8kk791z=self.pllkstn3.centery-clkqzfpq
  byl68ntk.blit(rv86wzs3,(rmm1zxyv-rv86wzs3.get_width()//2,f1bl08kg+self.pllkstn3.height-8))
  uysal8m1=pygame.Rect(j1kfk7y6,f1bl08kg,self.pllkstn3.width,self.pllkstn3.height)
  pygame.draw.rect(byl68ntk,qcd81twh(self.hfb85p86,0.55),uysal8m1,border_radius=10)
  ub68rerv=uysal8m1.inflate(-5,-5)
  pygame.draw.rect(byl68ntk,self.hfb85p86,ub68rerv,border_radius=8)
  i13n3bzt=pygame.Rect(ub68rerv.j1kfk7y6+3,ub68rerv.f1bl08kg+3,ub68rerv.width//2,ub68rerv.height//3)
  pygame.draw.rect(byl68ntk,qcd81twh(self.hfb85p86,2.0),i13n3bzt,border_radius=4)
  pygame.draw.rect(byl68ntk,(15,15,30),uysal8m1,width=2,border_radius=10)
  j1ldqnk2=math.hypot(self.ls2zge2j['gbwcv6'],self.ls2zge2j['g8wze4'])or 1
  (zorxdtg5,lgbpj4uf)=(self.ls2zge2j['gbwcv6']/j1ldqnk2,self.ls2zge2j['g8wze4']/j1ldqnk2)
  tza7x73q=(rmm1zxyv+zorxdtg5*20,g8kk791z+lgbpj4uf*20)
  sye0a4ab=(rmm1zxyv-lgbpj4uf*7+zorxdtg5*4,g8kk791z+zorxdtg5*7+lgbpj4uf*4)
  wtl0thhz=(rmm1zxyv+lgbpj4uf*7+zorxdtg5*4,g8kk791z-zorxdtg5*7+lgbpj4uf*4)
  pygame.draw.polygon(byl68ntk,iq5c34dx['hzj7ub'],[tza7x73q,sye0a4ab,wtl0thhz])
  pygame.draw.polygon(byl68ntk,(15,15,30),[tza7x73q,sye0a4ab,wtl0thhz],width=1)
  xu9ymszd=self.ftrflqbm/self.fdxj37c9
  b36htf4p(byl68ntk,j1kfk7y6,f1bl08kg-10,self.pllkstn3.width,xu9ymszd,height=6)
  vhuds3qs(byl68ntk,pygame.Rect(225,12,372,40))
  rk36m8jv=self.m8lw2qit.render('Hp.',True,(20,20,20))
  byl68ntk.blit(rk36m8jv,(233,23))
  b36htf4p(byl68ntk,297,25,290,xu9ymszd,height=19)
  rk36m8jv=self.m8lw2qit.render(f'{round(self.ftrflqbm)}/{self.fdxj37c9}',True,(20,20,20))
  width=rk36m8jv.get_width()
  height=rk36m8jv.get_height()
  byl68ntk.blit(rk36m8jv,(442-width//2,34.5-height//2))
