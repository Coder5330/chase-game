import pygame
import math
from ykatqyds import*
from.rqke2gjr import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,xq46nouh,owdz09wf,lb4y4k7b):
  super().__init__(xq46nouh,owdz09wf,lb4y4k7b)
  self.q7i6yuj7=(0,1)
  self.ruq9e5co=False
  self.f2sehe2a=0
  self.lztkkfzz=18
 def acxx6mdk(self,player):
  le9oe941=player.uaobt328.centerx-self.uaobt328.centerx
  jqzpniqf=player.uaobt328.centery-self.uaobt328.centery
  y2f7atwy=math.hypot(le9oe941,jqzpniqf)or 1
  self.q7i6yuj7=(le9oe941/y2f7atwy,jqzpniqf/y2f7atwy)
  if self.ruq9e5co:
   self.f2sehe2a-=1
   if self.f2sehe2a<=0:
    self.ruq9e5co=False
    self.m8lw2qit(player)
   return True
  if abs(player.uaobt328.owdz09wf-self.uaobt328.owdz09wf)<b8cgvyie and abs(player.uaobt328.lb4y4k7b-self.uaobt328.lb4y4k7b)<b8cgvyie:
   if self.kmgfxc08>0:
    self.kmgfxc08-=1
    return True
   self.ruq9e5co=True
   self.f2sehe2a=self.lztkkfzz
   return True
  return False
 def m8lw2qit(self,player):
  self.kmgfxc08=self.kybwmlun
  from tnyy95g5 import rpqk51fp
  w0p4e05q=uqjiujv6['c1l631']['prf7bn']
  (le9oe941,jqzpniqf)=(player.uaobt328.centerx-self.uaobt328.centerx,player.uaobt328.centery-self.uaobt328.centery)
  vj8yrddp=rpqk51fp('c1l631',self.uaobt328.centerx-w0p4e05q//2,self.uaobt328.centery-w0p4e05q//2,w0p4e05q,w0p4e05q,le9oe941,jqzpniqf)
  vj8yrddp.wc7x0h3j=self.velos6zl
  self.l57p6bkl.append(vj8yrddp)
 def v15cqzcu(self,u15pdtz9,clkqzfpq,x5m9j98c):
  owdz09wf=self.uaobt328.owdz09wf-clkqzfpq
  lb4y4k7b=self.uaobt328.lb4y4k7b-x5m9j98c
  wzlm72je=self.uaobt328.centerx-clkqzfpq
  vt6om1fb=self.uaobt328.centery-x5m9j98c
  self.win4olr6(u15pdtz9,owdz09wf,lb4y4k7b,wzlm72je,vt6om1fb)
  (u9el8hl8,kkzruin3)=self.q7i6yuj7
  (tj0nmeoq,myrp5ge0)=(-kkzruin3,u9el8hl8)
  (f32ejx5t,dzsedfqs)=(wzlm72je+u9el8hl8*14,vt6om1fb+kkzruin3*14)
  zgomf9pm=(f32ejx5t+tj0nmeoq*13-u9el8hl8*6,dzsedfqs+myrp5ge0*13-kkzruin3*6)
  kt94ow3l=(f32ejx5t-tj0nmeoq*13-u9el8hl8*6,dzsedfqs-myrp5ge0*13-kkzruin3*6)
  pvasifpw=(f32ejx5t+u9el8hl8*6,dzsedfqs+kkzruin3*6)
  pygame.draw.lines(u15pdtz9,(110,70,30),False,[zgomf9pm,pvasifpw,kt94ow3l],3)
  b36htf4p=1-self.f2sehe2a/self.lztkkfzz if self.ruq9e5co else 0
  a2wspofv=(f32ejx5t-u9el8hl8*(3+b36htf4p*10),dzsedfqs-kkzruin3*(3+b36htf4p*10))
  pygame.draw.line(u15pdtz9,(225,225,215),zgomf9pm,a2wspofv,2)
  pygame.draw.line(u15pdtz9,(225,225,215),kt94ow3l,a2wspofv,2)
  if self.ruq9e5co:
   x03uvule=(f32ejx5t+u9el8hl8*8,dzsedfqs+kkzruin3*8)
   pygame.draw.line(u15pdtz9,iq5c34dx['nszwd0'],a2wspofv,x03uvule,3)
