import pygame
import math
from z4w1arag import*
from.bohxs75t import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,b36htf4p,d5ixva1n,nngmx1gm):
  super().__init__(b36htf4p,d5ixva1n,nngmx1gm)
  self.q7i6yuj7=0
 def ywcxz2ei(self,player):
  self.q7i6yuj7+=1
  return False
 def g8kk791z(self,cq2q4qer,f32ejx5t,dzsedfqs):
  d5ixva1n=self.cqheyto5.d5ixva1n-f32ejx5t
  nngmx1gm=self.cqheyto5.nngmx1gm-dzsedfqs
  l9enulqj=self.cqheyto5.centerx-f32ejx5t
  hfb85p86=self.cqheyto5.centery-dzsedfqs
  mnx4sn6s=(math.sin(self.q7i6yuj7*0.08)+1)/2
  rgdej31g=int(self.cqheyto5.width*0.9+mnx4sn6s*6)
  j1i2hgj1=int(50+mnx4sn6s*60)
  azc4xl99=pygame.Surface((rgdej31g*2,rgdej31g*2),pygame.SRCALPHA)
  pygame.draw.circle(azc4xl99,(255,215,0,j1i2hgj1),(rgdej31g,rgdej31g),rgdej31g,width=4)
  cq2q4qer.blit(azc4xl99,(l9enulqj-rgdej31g,hfb85p86-rgdej31g))
  self.t1w1ht7p(cq2q4qer,d5ixva1n,nngmx1gm,l9enulqj,hfb85p86)
