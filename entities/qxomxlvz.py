import pygame
import math
from ykatqyds import*
from.rqke2gjr import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,xq46nouh,owdz09wf,lb4y4k7b):
  super().__init__(xq46nouh,owdz09wf,lb4y4k7b)
  self.zpajssuu=0
 def acxx6mdk(self,player):
  self.zpajssuu+=1
  return False
 def v15cqzcu(self,u15pdtz9,clkqzfpq,x5m9j98c):
  owdz09wf=self.uaobt328.owdz09wf-clkqzfpq
  lb4y4k7b=self.uaobt328.lb4y4k7b-x5m9j98c
  wzlm72je=self.uaobt328.centerx-clkqzfpq
  vt6om1fb=self.uaobt328.centery-x5m9j98c
  kc7rm6j8=(math.sin(self.zpajssuu*0.08)+1)/2
  v0rxxf36=int(self.uaobt328.width*0.9+kc7rm6j8*6)
  am2vajep=int(50+kc7rm6j8*60)
  vmxb9yo1=pygame.Surface((v0rxxf36*2,v0rxxf36*2),pygame.SRCALPHA)
  pygame.draw.circle(vmxb9yo1,(255,215,0,am2vajep),(v0rxxf36,v0rxxf36),v0rxxf36,width=4)
  u15pdtz9.blit(vmxb9yo1,(wzlm72je-v0rxxf36,vt6om1fb-v0rxxf36))
  self.win4olr6(u15pdtz9,owdz09wf,lb4y4k7b,wzlm72je,vt6om1fb)
