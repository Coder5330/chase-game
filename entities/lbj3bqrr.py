import pygame
import math
from en1x2gdg import*
from.y7iyojtp import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,x875aud9,qxb7gbdg,n01uyzpd):
  super().__init__(x875aud9,qxb7gbdg,n01uyzpd)
  self.eatvzkhi=0
 def njka34mq(self,player):
  self.eatvzkhi+=1
  return False
 def do2m71hs(self,gmoft6yr,kybwmlun,i0x65muf):
  qxb7gbdg=self.f8rtm4j3.qxb7gbdg-kybwmlun
  n01uyzpd=self.f8rtm4j3.n01uyzpd-i0x65muf
  ruq9e5co=self.f8rtm4j3.centerx-kybwmlun
  wzs13c9x=self.f8rtm4j3.centery-i0x65muf
  n64fgwje=(math.sin(self.eatvzkhi*0.08)+1)/2
  zflse45b=int(self.f8rtm4j3.width*0.9+n64fgwje*6)
  u8c2jwoc=int(50+n64fgwje*60)
  xq46nouh=pygame.Surface((zflse45b*2,zflse45b*2),pygame.SRCALPHA)
  pygame.draw.circle(xq46nouh,(255,215,0,u8c2jwoc),(zflse45b,zflse45b),zflse45b,width=4)
  gmoft6yr.blit(xq46nouh,(ruq9e5co-zflse45b,wzs13c9x-zflse45b))
  self.rrcbpljd(gmoft6yr,qxb7gbdg,n01uyzpd,ruq9e5co,wzs13c9x)
