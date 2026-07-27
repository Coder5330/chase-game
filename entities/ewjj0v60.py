import pygame
import math
from o100vhmy import*
from.vq3jzr25 import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,uc1xi04b,rm0j36tc,tza7x73q):
  super().__init__(uc1xi04b,rm0j36tc,tza7x73q)
  self.mqxlm5q2=0
 def mlikwe4b(self,player):
  self.mqxlm5q2+=1
  return False
 def i01nouht(self,npejzhya,kybwmlun,i0x65muf):
  rm0j36tc=self.zflse45b.rm0j36tc-kybwmlun
  tza7x73q=self.zflse45b.tza7x73q-i0x65muf
  lztkkfzz=self.zflse45b.centerx-kybwmlun
  f2sehe2a=self.zflse45b.centery-i0x65muf
  ck7n3bfh=(math.sin(self.mqxlm5q2*0.08)+1)/2
  la3kkrzd=int(self.zflse45b.width*0.9+ck7n3bfh*6)
  u8c2jwoc=int(50+ck7n3bfh*60)
  yrivh6t1=pygame.Surface((la3kkrzd*2,la3kkrzd*2),pygame.SRCALPHA)
  pygame.draw.circle(yrivh6t1,(255,215,0,u8c2jwoc),(la3kkrzd,la3kkrzd),la3kkrzd,width=4)
  npejzhya.blit(yrivh6t1,(lztkkfzz-la3kkrzd,f2sehe2a-la3kkrzd))
  self.rrcbpljd(npejzhya,rm0j36tc,tza7x73q,lztkkfzz,f2sehe2a)
