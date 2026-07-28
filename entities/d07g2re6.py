import pygame
import math
from r1yohmi9 import*
from.xqup06id import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,jqzpniqf,un9sz6rv,ehet25lz):
  super().__init__(jqzpniqf,un9sz6rv,ehet25lz)
  self.jq1ddpus=0
 def zgomf9pm(self,player):
  self.jq1ddpus+=1
  return False
 def fo75rh8l(self,vmy9x8sy,d1ieixwc,pvasifpw):
  un9sz6rv=self.nxxjve3d.un9sz6rv-d1ieixwc
  ehet25lz=self.nxxjve3d.ehet25lz-pvasifpw
  cnqt3wve=self.nxxjve3d.centerx-d1ieixwc
  do2m71hs=self.nxxjve3d.centery-pvasifpw
  ej16dvtj=(math.sin(self.jq1ddpus*0.08)+1)/2
  xasez2nx=int(self.nxxjve3d.width*0.9+ej16dvtj*6)
  v982n2at=int(50+ej16dvtj*60)
  cjn2fomd=pygame.Surface((xasez2nx*2,xasez2nx*2),pygame.SRCALPHA)
  pygame.draw.circle(cjn2fomd,(255,215,0,v982n2at),(xasez2nx,xasez2nx),xasez2nx,width=4)
  vmy9x8sy.blit(cjn2fomd,(cnqt3wve-xasez2nx,do2m71hs-xasez2nx))
  self.nd96qe3r(vmy9x8sy,un9sz6rv,ehet25lz,cnqt3wve,do2m71hs)
