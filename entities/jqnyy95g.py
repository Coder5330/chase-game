import pygame
import math
from e87f8tsx import*
from.odog8cfe import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,yrivh6t1,j1kfk7y6,f1bl08kg):
  super().__init__(yrivh6t1,j1kfk7y6,f1bl08kg)
  self.z8z3v6di=0
 def ceb8753a(self,player):
  self.z8z3v6di+=1
  return False
 def dw7nh8rq(self,byl68ntk,i20cv3tl,clkqzfpq):
  j1kfk7y6=self.pllkstn3.j1kfk7y6-i20cv3tl
  f1bl08kg=self.pllkstn3.f1bl08kg-clkqzfpq
  rmm1zxyv=self.pllkstn3.centerx-i20cv3tl
  g8kk791z=self.pllkstn3.centery-clkqzfpq
  mu118qqv=(math.sin(self.z8z3v6di*0.08)+1)/2
  npcxa5s0=int(self.pllkstn3.width*0.9+mu118qqv*6)
  i4fejgxa=int(50+mu118qqv*60)
  o9ros7yt=pygame.Surface((npcxa5s0*2,npcxa5s0*2),pygame.SRCALPHA)
  pygame.draw.circle(o9ros7yt,(255,215,0,i4fejgxa),(npcxa5s0,npcxa5s0),npcxa5s0,width=4)
  byl68ntk.blit(o9ros7yt,(rmm1zxyv-npcxa5s0,g8kk791z-npcxa5s0))
  self.eqrl1n75(byl68ntk,j1kfk7y6,f1bl08kg,rmm1zxyv,g8kk791z)
