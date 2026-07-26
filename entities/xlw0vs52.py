import pygame
import math
from ygm55ff1 import*
from.qdq55it9 import zy0ifznb
class f935a0l7(zy0ifznb):
 def __init__(self,cnqt3wve,yypp5zp7,tjy1o2rn):
  super().__init__(cnqt3wve,yypp5zp7,tjy1o2rn)
  self.tnz61231=0
 def svt8k06m(self,player):
  self.tnz61231+=1
  return False
 def izhwy9he(self,uj64qhks,ra73jgzl,kmgfxc08):
  yypp5zp7=self.zdan085r.yypp5zp7-ra73jgzl
  tjy1o2rn=self.zdan085r.tjy1o2rn-kmgfxc08
  nd6357oo=self.zdan085r.centerx-ra73jgzl
  li9nb74x=self.zdan085r.centery-kmgfxc08
  k8qeoz0k=(math.sin(self.tnz61231*0.08)+1)/2
  y8bv78hu=int(self.zdan085r.width*0.9+k8qeoz0k*6)
  dtx63cfl=int(50+k8qeoz0k*60)
  dw7nh8rq=pygame.Surface((y8bv78hu*2,y8bv78hu*2),pygame.SRCALPHA)
  pygame.draw.circle(dw7nh8rq,(255,215,0,dtx63cfl),(y8bv78hu,y8bv78hu),y8bv78hu,width=4)
  uj64qhks.blit(dw7nh8rq,(nd6357oo-y8bv78hu,li9nb74x-y8bv78hu))
  self.zakoixnt(uj64qhks,yypp5zp7,tjy1o2rn,nd6357oo,li9nb74x)
