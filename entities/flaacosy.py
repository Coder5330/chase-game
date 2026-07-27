import pygame
import math
from i1arxabo import*
from.lhkgad7x import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,mygfliji,htgsiwg0,hhl1737s):
  super().__init__(mygfliji,htgsiwg0,hhl1737s)
  self.ao4izasn=0
 def jdqqzrlf(self,player):
  self.ao4izasn+=1
  return False
 def sl65wvjx(self,tj0nmeoq,uysal8m1,giec4d14):
  htgsiwg0=self.todsx4nx.htgsiwg0-uysal8m1
  hhl1737s=self.todsx4nx.hhl1737s-giec4d14
  wi8skch8=self.todsx4nx.centerx-uysal8m1
  iektsg7f=self.todsx4nx.centery-giec4d14
  w0p4e05q=(math.sin(self.ao4izasn*0.08)+1)/2
  vhxs58yr=int(self.todsx4nx.width*0.9+w0p4e05q*6)
  jmpioygg=int(50+w0p4e05q*60)
  r98s4c3b=pygame.Surface((vhxs58yr*2,vhxs58yr*2),pygame.SRCALPHA)
  pygame.draw.circle(r98s4c3b,(255,215,0,jmpioygg),(vhxs58yr,vhxs58yr),vhxs58yr,width=4)
  tj0nmeoq.blit(r98s4c3b,(wi8skch8-vhxs58yr,iektsg7f-vhxs58yr))
  self.v83tqll8(tj0nmeoq,htgsiwg0,hhl1737s,wi8skch8,iektsg7f)
