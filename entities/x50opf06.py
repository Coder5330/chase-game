import pygame
import math
from ykatqyds import*
from.rqke2gjr import f935a0l7
class ozp08j3t(f935a0l7):
 def __init__(self,xq46nouh,owdz09wf,lb4y4k7b):
  super().__init__(xq46nouh,owdz09wf,lb4y4k7b)
  self.fo75rh8l=0
  self.uc1xi04b=0
  self.hiac2e4q=0
 def acxx6mdk(self,player):
  self.hiac2e4q+=0.35*(self.bf7so8w5/self.wppsfnko if self.wppsfnko else 1)
  az2ueaxy=k1wj0tpa[self.type]
  if self.uc1xi04b>0:
   self.uc1xi04b-=1
   if self.uc1xi04b<=0:
    self.bf7so8w5=self.wppsfnko
   return False
  if self.fo75rh8l>0:
   self.fo75rh8l-=1
   return False
  if abs(player.uaobt328.owdz09wf-self.uaobt328.owdz09wf)<az2ueaxy['g8wze4']and abs(player.uaobt328.lb4y4k7b-self.uaobt328.lb4y4k7b)<az2ueaxy['g8wze4']:
   self.bf7so8w5=self.wppsfnko*az2ueaxy['en1x2g']
   self.uc1xi04b=az2ueaxy['gbwcv6']
   self.fo75rh8l=az2ueaxy['nddqhk']
  return False
 def v15cqzcu(self,u15pdtz9,clkqzfpq,x5m9j98c):
  owdz09wf=self.uaobt328.owdz09wf-clkqzfpq
  lb4y4k7b=self.uaobt328.lb4y4k7b-x5m9j98c
  wzlm72je=self.uaobt328.centerx-clkqzfpq
  vt6om1fb=self.uaobt328.centery-x5m9j98c
  ftlpq2wg=self.uaobt328.width//2
  onqyyf9r=lb4y4k7b+self.uaobt328.height-3
  v6g298cq=(25,25,25)
  xwqvr1h6=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(sfu38gl2,w5iz31yr,jenvg3kk)in xwqvr1h6:
   d0qzfhom=math.sin(self.hiac2e4q+jenvg3kk)
   zo3lqi7e=max(0,d0qzfhom)*4
   v3e1ocjx=(wzlm72je+sfu38gl2*ftlpq2wg*0.7,vt6om1fb+w5iz31yr)
   damdvlnk=wzlm72je+sfu38gl2*(ftlpq2wg+9)+d0qzfhom*3
   m20u9isy=onqyyf9r-zo3lqi7e
   n04cdpqv=((v3e1ocjx[0]+damdvlnk)/2,(v3e1ocjx[1]+m20u9isy)/2-2)
   pygame.draw.line(u15pdtz9,v6g298cq,v3e1ocjx,n04cdpqv,3)
   pygame.draw.line(u15pdtz9,v6g298cq,n04cdpqv,(damdvlnk,m20u9isy),3)
  self.win4olr6(u15pdtz9,owdz09wf,lb4y4k7b,wzlm72je,vt6om1fb)
