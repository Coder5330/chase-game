import pygame
import math
from v7bnhjw6 import*
from.e1gnfiue import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,gubmc97c,qic1l7dy,vsjchzjq):
  super().__init__(gubmc97c,qic1l7dy,vsjchzjq)
  self.mytn02yc=0
 def gsrtwlxd(self,player):
  self.mytn02yc+=1
  return False
 def wc7x0h3j(self,gg7oq2zd,li9nb74x,zfb7r31q):
  qic1l7dy=self.jenvg3kk.qic1l7dy-li9nb74x
  vsjchzjq=self.jenvg3kk.vsjchzjq-zfb7r31q
  pa8s8hmb=self.jenvg3kk.centerx-li9nb74x
  pv4ykade=self.jenvg3kk.centery-zfb7r31q
  xxkdq95g=(math.sin(self.mytn02yc*0.08)+1)/2
  g1g1r1dw=int(self.jenvg3kk.width*0.9+xxkdq95g*6)
  sne6loh2=int(50+xxkdq95g*60)
  sf337kuu=pygame.Surface((g1g1r1dw*2,g1g1r1dw*2),pygame.SRCALPHA)
  pygame.draw.circle(sf337kuu,(255,215,0,sne6loh2),(g1g1r1dw,g1g1r1dw),g1g1r1dw,width=4)
  gg7oq2zd.blit(sf337kuu,(pa8s8hmb-g1g1r1dw,pv4ykade-g1g1r1dw))
  self.wrbw2zla(gg7oq2zd,qic1l7dy,vsjchzjq,pa8s8hmb,pv4ykade)
