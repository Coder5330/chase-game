import pygame
import math
from o100vhmy import*
from.vq3jzr25 import f935a0l7
class khl1n13j(f935a0l7):
 def __init__(self,uc1xi04b,rm0j36tc,tza7x73q):
  super().__init__(uc1xi04b,rm0j36tc,tza7x73q)
  self.ep6beffl=0
  self.wi8skch8=0
  self.arml29q2=0
 def mlikwe4b(self,player):
  self.arml29q2+=0.35*(self.k8qeoz0k/self.tp2ex5t5 if self.tp2ex5t5 else 1)
  mn89ltaj=k1wj0tpa[self.type]
  if self.wi8skch8>0:
   self.wi8skch8-=1
   if self.wi8skch8<=0:
    self.k8qeoz0k=self.tp2ex5t5
   return False
  if self.ep6beffl>0:
   self.ep6beffl-=1
   return False
  if abs(player.zflse45b.rm0j36tc-self.zflse45b.rm0j36tc)<mn89ltaj['wkgeq2']and abs(player.zflse45b.tza7x73q-self.zflse45b.tza7x73q)<mn89ltaj['wkgeq2']:
   self.k8qeoz0k=self.tp2ex5t5*mn89ltaj['x429om']
   self.wi8skch8=mn89ltaj['pswrgv']
   self.ep6beffl=mn89ltaj['kjuw7w']
  return False
 def i01nouht(self,npejzhya,kybwmlun,i0x65muf):
  rm0j36tc=self.zflse45b.rm0j36tc-kybwmlun
  tza7x73q=self.zflse45b.tza7x73q-i0x65muf
  lztkkfzz=self.zflse45b.centerx-kybwmlun
  f2sehe2a=self.zflse45b.centery-i0x65muf
  r98s4c3b=self.zflse45b.width//2
  xq46nouh=tza7x73q+self.zflse45b.height-3
  w4rcb1kj=(25,25,25)
  rk2u1rsu=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(xu9ymszd,jq1ddpus,oc4kl8cg)in rk2u1rsu:
   iaq7b7v1=math.sin(self.arml29q2+oc4kl8cg)
   v3e1ocjx=max(0,iaq7b7v1)*4
   cjn2fomd=(lztkkfzz+xu9ymszd*r98s4c3b*0.7,f2sehe2a+jq1ddpus)
   g70e3p15=lztkkfzz+xu9ymszd*(r98s4c3b+9)+iaq7b7v1*3
   aicvqy5i=xq46nouh-v3e1ocjx
   gqj5sxvw=((cjn2fomd[0]+g70e3p15)/2,(cjn2fomd[1]+aicvqy5i)/2-2)
   pygame.draw.line(npejzhya,w4rcb1kj,cjn2fomd,gqj5sxvw,3)
   pygame.draw.line(npejzhya,w4rcb1kj,gqj5sxvw,(g70e3p15,aicvqy5i),3)
  self.rrcbpljd(npejzhya,rm0j36tc,tza7x73q,lztkkfzz,f2sehe2a)
