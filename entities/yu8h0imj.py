import pygame
import math
from zfiblejg import*
from.vpbnqs3q import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,g5l8a78e,x3zo7utx,cjy62zee):
  super().__init__(g5l8a78e,x3zo7utx,cjy62zee)
  self.o9ros7yt=0
 def qic1l7dy(self,player):
  self.o9ros7yt+=1
  return False
 def dw7nh8rq(self,uwxrum2l,uos0fb4y,obc2nnuv):
  x3zo7utx=self.tby49e7e.x3zo7utx-uos0fb4y
  cjy62zee=self.tby49e7e.cjy62zee-obc2nnuv
  rmm1zxyv=self.tby49e7e.centerx-uos0fb4y
  g8kk791z=self.tby49e7e.centery-obc2nnuv
  oa47sh2s=(math.sin(self.o9ros7yt*0.08)+1)/2
  d46aexl6=int(self.tby49e7e.width*0.9+oa47sh2s*6)
  mpdzp6lf=int(50+oa47sh2s*60)
  nyfkjfpn=pygame.Surface((d46aexl6*2,d46aexl6*2),pygame.SRCALPHA)
  pygame.draw.circle(nyfkjfpn,(255,215,0,mpdzp6lf),(d46aexl6,d46aexl6),d46aexl6,width=4)
  uwxrum2l.blit(nyfkjfpn,(rmm1zxyv-d46aexl6,g8kk791z-d46aexl6))
  self.sld4d6af(uwxrum2l,x3zo7utx,cjy62zee,rmm1zxyv,g8kk791z)
