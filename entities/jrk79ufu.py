import pygame
import math
from ykatqyds import*
from.kupnhzx9 import cb2uuijn,ouuylaja
pygame.init()
rv86wzs3=pygame.Surface((rqf5q14j+16,14),pygame.SRCALPHA)
pygame.draw.ellipse(rv86wzs3,(0,0,0,90),rv86wzs3.get_rect())
def gubmc97c(u15pdtz9,uaobt328,am2vajep=120,v0rxxf36=10):
 mu118qqv=pygame.Surface((uaobt328.width,uaobt328.height),pygame.SRCALPHA)
 pygame.draw.rect(mu118qqv,(255,255,255,am2vajep),mu118qqv.get_rect(),border_radius=v0rxxf36)
 u15pdtz9.blit(mu118qqv,uaobt328.topleft)
class ky20479t:
 def __init__(self,meta_upgrades=None):
  meta_upgrades=meta_upgrades or{}
  j0kgazu4=meta_upgrades.get('START_HEALTH',0)
  zdan085r=meta_upgrades.get('START_SPEED',0)
  jl90pxrl=meta_upgrades.get('START_DAMAGE',0)
  wg25cfzf=meta_upgrades.get('START_COOLDOWN',0)
  bihsa7he=meta_upgrades.get('START_ARMOR',0)
  wy0mahym=meta_upgrades.get('START_REGEN',0)
  self.wppsfnko=yswjckjl*mmn32u1i(zdan085r)
  self.bf7so8w5=self.wppsfnko
  self.uaobt328=pygame.Rect((m53a5qbs-rqf5q14j)//2,(v83tqll8-rqf5q14j)//2,rqf5q14j,rqf5q14j)
  self.pa8s8hmb=iq5c34dx['wurvqt']
  self.jc54wsqt=int(1000*y8bv78hu(j0kgazu4))
  self.k3z6bz8u=self.jc54wsqt
  self.w4rcb1kj=self.jc54wsqt
  self.rn16uxf5=0
  self.a8ax40dt=1
  self.un9sz6rv=False
  self.crsb4gf1={'igc9ho':0,'urf1hx':self.bf7so8w5}
  self.m9bn18gp={}
  self.kr0aymk9={key:0 for key in rcfnfhol}
  self.f8wquuy5=w8y72ivg(jl90pxrl)
  self.u3ifhv1x=d448n7od(wg25cfzf)
  self.divsolml=s8438tgb(bihsa7he)
  self.bq349dxb=pf0i9g5d(wy0mahym)
  self.rzewviyt=self.f8wquuy5
  self.do2m71hs=self.u3ifhv1x
  self.e8a1arr3=1.0
  self.nqimqodp=self.divsolml
  self.ukshy8nb=self.bq349dxb
  self.h4l1vznq=pi3qk2ia
  self.ck7n3bfh=False
  self.xo2t8fy6=0
  self.k1taa0i5=[]
  self.jxxgaear=0
  self.ls2zge2j=0
  self.cjn2fomd=pygame.font.SysFont('arial',20,bold=True)
 def ejwtl9tq(self,key):
  self.kr0aymk9[key]+=1
  mnwxuj3a=self.kr0aymk9[key]
  if key=='zmygy0':
   ncyh3fvl=int(self.jc54wsqt*(1+0.2*mnwxuj3a))
   self.w4rcb1kj+=ncyh3fvl-self.k3z6bz8u
   self.k3z6bz8u=ncyh3fvl
  elif key=='t7wqp3':
   self.bf7so8w5=self.wppsfnko*(1+0.08*mnwxuj3a)
  elif key=='hpvwzo':
   self.ukshy8nb=self.bq349dxb+mnwxuj3a
  elif key=='p2xrw6':
   self.rzewviyt=self.f8wquuy5*(1+0.06*mnwxuj3a)
  elif key=='gyjckt':
   self.do2m71hs=self.u3ifhv1x*max(0.6,1-0.05*mnwxuj3a)
  elif key=='s2gqu7':
   self.nqimqodp=self.divsolml+mnwxuj3a*5
  elif key=='t00ucr':
   self.e8a1arr3=1+0.15*mnwxuj3a
 def qo6q0usw(self,o5rlqiob):
  self.m9bn18gp[o5rlqiob]=self.m9bn18gp.get(o5rlqiob,1)+1
 def mu4fmpkx(self):
  zflv1xxl=pygame.key.get_pressed()
  le9oe941=jqzpniqf=0
  if zflv1xxl[pygame.K_UP]:
   jqzpniqf-=self.bf7so8w5
  if zflv1xxl[pygame.K_DOWN]:
   jqzpniqf+=self.bf7so8w5
  if zflv1xxl[pygame.K_LEFT]:
   le9oe941-=self.bf7so8w5
  if zflv1xxl[pygame.K_RIGHT]:
   le9oe941+=self.bf7so8w5
  if le9oe941!=0 and jqzpniqf!=0:
   le9oe941*=0.707
   jqzpniqf*=0.707
  if le9oe941!=0 or jqzpniqf!=0:
   self.crsb4gf1['igc9ho']=le9oe941
   self.crsb4gf1['urf1hx']=jqzpniqf
  self.uaobt328.owdz09wf+=le9oe941+self.jxxgaear
  self.uaobt328.lb4y4k7b+=jqzpniqf+self.ls2zge2j
  if self.jxxgaear>0:
   self.jxxgaear=max(0,self.jxxgaear-1)
  elif self.jxxgaear<0:
   self.jxxgaear=min(0,self.jxxgaear+1)
  if self.ls2zge2j>0:
   self.ls2zge2j=max(0,self.ls2zge2j-1)
  elif self.ls2zge2j<0:
   self.ls2zge2j=min(0,self.ls2zge2j+1)
  self.uaobt328.owdz09wf=max(min(self.uaobt328.owdz09wf,m53a5qbs-self.uaobt328.width),0)
  self.uaobt328.lb4y4k7b=max(min(self.uaobt328.lb4y4k7b,v83tqll8-self.uaobt328.height),0)
  if self.ukshy8nb>0 and self.w4rcb1kj<self.k3z6bz8u:
   self.h4l1vznq-=1
   if self.h4l1vznq<=0:
    self.h4l1vznq=pi3qk2ia
    self.w4rcb1kj=min(self.k3z6bz8u,self.w4rcb1kj+self.ukshy8nb)
  if self.rn16uxf5>=t1w1ht7p[min(self.a8ax40dt,len(t1w1ht7p)-1)]:
   self.un9sz6rv=True
   self.rn16uxf5=0
   self.a8ax40dt+=1
 def v15cqzcu(self,u15pdtz9,clkqzfpq,x5m9j98c):
  owdz09wf=self.uaobt328.owdz09wf-clkqzfpq
  lb4y4k7b=self.uaobt328.lb4y4k7b-x5m9j98c
  wzlm72je=self.uaobt328.centerx-clkqzfpq
  vt6om1fb=self.uaobt328.centery-x5m9j98c
  u15pdtz9.blit(rv86wzs3,(wzlm72je-rv86wzs3.get_width()//2,lb4y4k7b+self.uaobt328.height-8))
  giec4d14=pygame.Rect(owdz09wf,lb4y4k7b,self.uaobt328.width,self.uaobt328.height)
  pygame.draw.rect(u15pdtz9,cb2uuijn(self.pa8s8hmb,0.55),giec4d14,border_radius=10)
  ry181acj=giec4d14.inflate(-5,-5)
  pygame.draw.rect(u15pdtz9,self.pa8s8hmb,ry181acj,border_radius=8)
  cp91i3vm=pygame.Rect(ry181acj.owdz09wf+3,ry181acj.lb4y4k7b+3,ry181acj.width//2,ry181acj.height//3)
  pygame.draw.rect(u15pdtz9,cb2uuijn(self.pa8s8hmb,2.0),cp91i3vm,border_radius=4)
  pygame.draw.rect(u15pdtz9,(15,15,30),giec4d14,width=2,border_radius=10)
  y2f7atwy=math.hypot(self.crsb4gf1['igc9ho'],self.crsb4gf1['urf1hx'])or 1
  (wydmt8vt,m3pt5r5r)=(self.crsb4gf1['igc9ho']/y2f7atwy,self.crsb4gf1['urf1hx']/y2f7atwy)
  n01uyzpd=(wzlm72je+wydmt8vt*20,vt6om1fb+m3pt5r5r*20)
  nii6l3ue=(wzlm72je-m3pt5r5r*7+wydmt8vt*4,vt6om1fb+wydmt8vt*7+m3pt5r5r*4)
  rk43safy=(wzlm72je+m3pt5r5r*7+wydmt8vt*4,vt6om1fb-wydmt8vt*7+m3pt5r5r*4)
  pygame.draw.polygon(u15pdtz9,iq5c34dx['kp82kb'],[n01uyzpd,nii6l3ue,rk43safy])
  pygame.draw.polygon(u15pdtz9,(15,15,30),[n01uyzpd,nii6l3ue,rk43safy],width=1)
  tbxf445c=self.w4rcb1kj/self.k3z6bz8u
  ouuylaja(u15pdtz9,owdz09wf,lb4y4k7b-10,self.uaobt328.width,tbxf445c,height=6)
  gubmc97c(u15pdtz9,pygame.Rect(225,12,372,40))
  mu118qqv=self.cjn2fomd.render('Hp.',True,(20,20,20))
  u15pdtz9.blit(mu118qqv,(233,23))
  ouuylaja(u15pdtz9,297,25,290,tbxf445c,height=19)
  mu118qqv=self.cjn2fomd.render(f'{round(self.w4rcb1kj)}/{self.k3z6bz8u}',True,(20,20,20))
  width=mu118qqv.get_width()
  height=mu118qqv.get_height()
  u15pdtz9.blit(mu118qqv,(442-width//2,34.5-height//2))
