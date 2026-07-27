import pygame
import math
from o100vhmy import*
from.vq3jzr25 import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,uc1xi04b,rm0j36tc,tza7x73q):
  super().__init__(uc1xi04b,rm0j36tc,tza7x73q)
  mn89ltaj=k1wj0tpa[uc1xi04b]
  self.f80ebkjf=mn89ltaj['og8cd3']
  self.t54piwzn=mn89ltaj['zmygy0']
  self.stv18kgy=mn89ltaj['wurvqt']
  self.z3olfark=mn89ltaj['c37qqy']
  self.jr5rdnpx=mn89ltaj['og8cd3']
  self.g1b3d505='hidden'
  self.xxns2zyb=self.t54piwzn
 def wkzorqqf(self):
  self.xxns2zyb-=1
  if self.xxns2zyb<=0:
   if self.g1b3d505=='hidden':
    self.g1b3d505='revealing'
    self.xxns2zyb=self.z3olfark
   elif self.g1b3d505=='revealing':
    self.g1b3d505='visible'
    self.xxns2zyb=self.stv18kgy
   else:
    self.g1b3d505='hidden'
    self.xxns2zyb=self.t54piwzn
  self.jr5rdnpx=self.f80ebkjf if self.g1b3d505=='hidden'else 255
 def j1ldqnk2(self,player):
  if self.q7i6yuj7<=0:
   self.vw6m7b5c=True
   return
  self.wkzorqqf()
  if self.g1b3d505=='visible'and abs(player.zflse45b.rm0j36tc-self.zflse45b.rm0j36tc)<cawudtse and(abs(player.zflse45b.tza7x73q-self.zflse45b.tza7x73q)<cawudtse):
   self.sne6loh2(player)
   return
  sl65wvjx=player.zflse45b.rm0j36tc-self.zflse45b.rm0j36tc
  yuibrsz1=player.zflse45b.tza7x73q-self.zflse45b.tza7x73q
  l9enulqj=math.hypot(sl65wvjx,yuibrsz1)
  if l9enulqj==0:
   return
  njka34mq=sl65wvjx/l9enulqj
  ayr1k12v=yuibrsz1/l9enulqj
  if njka34mq!=0 and ayr1k12v!=0:
   njka34mq*=0.707
   ayr1k12v*=0.707
  self.zflse45b.rm0j36tc+=njka34mq*self.k8qeoz0k
  self.zflse45b.tza7x73q+=ayr1k12v*self.k8qeoz0k
  self.zflse45b.rm0j36tc=round(self.zflse45b.rm0j36tc)
  self.zflse45b.tza7x73q=round(self.zflse45b.tza7x73q)
 def i01nouht(self,npejzhya,kybwmlun,i0x65muf):
  rm0j36tc=self.zflse45b.rm0j36tc-kybwmlun
  tza7x73q=self.zflse45b.tza7x73q-i0x65muf
  lztkkfzz=self.zflse45b.centerx-kybwmlun
  f2sehe2a=self.zflse45b.centery-i0x65muf
  if self.jr5rdnpx>=255:
   self.rrcbpljd(npejzhya,rm0j36tc,tza7x73q,lztkkfzz,f2sehe2a)
   return
  pcvsqame=24
  sfu38gl2=pygame.Surface((self.zflse45b.width+pcvsqame*2,self.zflse45b.height+pcvsqame*2),pygame.SRCALPHA)
  (zmybd2qe,fpa8hyex)=(pcvsqame,pcvsqame)
  (nvuprt77,ftrflqbm)=(zmybd2qe+self.zflse45b.width//2,fpa8hyex+self.zflse45b.height//2)
  self.rrcbpljd(sfu38gl2,zmybd2qe,fpa8hyex,nvuprt77,ftrflqbm)
  sfu38gl2.set_alpha(self.jr5rdnpx)
  npejzhya.blit(sfu38gl2,(rm0j36tc-pcvsqame,tza7x73q-pcvsqame))
