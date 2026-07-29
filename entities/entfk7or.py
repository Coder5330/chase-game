import pygame
import math
from j1bmqf7z import*
from.kier7u8h import f935a0l7
class qxaprpn6(f935a0l7):
 def __init__(self,mqxlm5q2,x,y):
  super().__init__(mqxlm5q2,x,y)
  self.fo75rh8l=0
  self.uc1xi04b=0
  self.iimoe0sy=0
 def qic1l7dy(self,player):
  self.iimoe0sy+=0.35*(self.p7b1ijiy/self.u23y30ys if self.u23y30ys else 1)
  xxkdq95g=k1wj0tpa[self.type]
  if self.uc1xi04b>0:
   self.uc1xi04b-=1
   if self.uc1xi04b<=0:
    self.p7b1ijiy=self.u23y30ys
   return False
  if self.fo75rh8l>0:
   self.fo75rh8l-=1
   return False
  if abs(player.npcxa5s0.x-self.npcxa5s0.x)<xxkdq95g['hx0gu4']and abs(player.npcxa5s0.y-self.npcxa5s0.y)<xxkdq95g['hx0gu4']:
   self.p7b1ijiy=self.u23y30ys*xxkdq95g['bx1ego']
   self.uc1xi04b=xxkdq95g['t7fr91']
   self.fo75rh8l=xxkdq95g['pgsb98']
  return False
 def v15cqzcu(self,h8s2ftom,vqnpcenl,iie0rnuj):
  x=self.npcxa5s0.x-vqnpcenl
  y=self.npcxa5s0.y-iie0rnuj
  wzlm72je=self.npcxa5s0.centerx-vqnpcenl
  vt6om1fb=self.npcxa5s0.centery-iie0rnuj
  we4xyf9i=self.npcxa5s0.width//2
  zpajssuu=y+self.npcxa5s0.height-3
  nii6l3ue=(25,25,25)
  j1ldqnk2=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(z5x8a5fb,w5iz31yr,eehou6ql)in j1ldqnk2:
   rserev36=math.sin(self.iimoe0sy+eehou6ql)
   mcup8ijl=max(0,rserev36)*4
   v3e1ocjx=(wzlm72je+z5x8a5fb*we4xyf9i*0.7,vt6om1fb+w5iz31yr)
   jq1ddpus=wzlm72je+z5x8a5fb*(we4xyf9i+9)+rserev36*3
   damdvlnk=zpajssuu-mcup8ijl
   zflv1xxl=((v3e1ocjx[0]+jq1ddpus)/2,(v3e1ocjx[1]+damdvlnk)/2-2)
   pygame.draw.line(h8s2ftom,nii6l3ue,v3e1ocjx,zflv1xxl,3)
   pygame.draw.line(h8s2ftom,nii6l3ue,zflv1xxl,(jq1ddpus,damdvlnk),3)
  self.k44nlz15(h8s2ftom,x,y,wzlm72je,vt6om1fb)
