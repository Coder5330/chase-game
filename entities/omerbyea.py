import pygame
import math
from entfk7or import*
from.tnyy95g5 import f935a0l7
class qxaprpn6(f935a0l7):
 def __init__(self,yrivh6t1,w2sq3b9s,owdz09wf):
  super().__init__(yrivh6t1,w2sq3b9s,owdz09wf)
  self.uidlrye8=0
  self.fo75rh8l=0
  self.uypuplvq=0
 def nngmx1gm(self,player):
  self.uypuplvq+=0.35*(self.q6nqqb9l/self.llxxezdu if self.llxxezdu else 1)
  nv23gxj0=k1wj0tpa[self.type]
  if self.fo75rh8l>0:
   self.fo75rh8l-=1
   if self.fo75rh8l<=0:
    self.q6nqqb9l=self.llxxezdu
   return False
  if self.uidlrye8>0:
   self.uidlrye8-=1
   return False
  if abs(player.npcxa5s0.w2sq3b9s-self.npcxa5s0.w2sq3b9s)<nv23gxj0['onlt8d']and abs(player.npcxa5s0.owdz09wf-self.npcxa5s0.owdz09wf)<nv23gxj0['onlt8d']:
   self.q6nqqb9l=self.llxxezdu*nv23gxj0['rw8p74']
   self.fo75rh8l=nv23gxj0['mrf5a7']
   self.uidlrye8=nv23gxj0['jr87iy']
  return False
 def tnz61231(self,h8s2ftom,obc2nnuv,vqnpcenl):
  w2sq3b9s=self.npcxa5s0.w2sq3b9s-obc2nnuv
  owdz09wf=self.npcxa5s0.owdz09wf-vqnpcenl
  g8kk791z=self.npcxa5s0.centerx-obc2nnuv
  wzlm72je=self.npcxa5s0.centery-vqnpcenl
  gsmdzqcb=self.npcxa5s0.width//2
  vmxb9yo1=owdz09wf+self.npcxa5s0.height-3
  lnf74t60=(25,25,25)
  v6g298cq=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(z5x8a5fb,v3e1ocjx,eehou6ql)in v6g298cq:
   yypp5zp7=math.sin(self.uypuplvq+eehou6ql)
   qo6q0usw=max(0,yypp5zp7)*4
   rktlzkj4=(g8kk791z+z5x8a5fb*gsmdzqcb*0.7,wzlm72je+v3e1ocjx)
   cjn2fomd=g8kk791z+z5x8a5fb*(gsmdzqcb+9)+yypp5zp7*3
   jq1ddpus=vmxb9yo1-qo6q0usw
   mctwjlsh=((rktlzkj4[0]+cjn2fomd)/2,(rktlzkj4[1]+jq1ddpus)/2-2)
   pygame.draw.line(h8s2ftom,lnf74t60,rktlzkj4,mctwjlsh,3)
   pygame.draw.line(h8s2ftom,lnf74t60,mctwjlsh,(cjn2fomd,jq1ddpus),3)
  self.u8c2jwoc(h8s2ftom,w2sq3b9s,owdz09wf,g8kk791z,wzlm72je)
