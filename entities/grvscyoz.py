import pygame
import math
from omerbyea import*
from.erp0aga2 import f935a0l7
class ozp08j3t(f935a0l7):
 def __init__(self,mqxlm5q2,eolaq665,t5ivrocv):
  super().__init__(mqxlm5q2,eolaq665,t5ivrocv)
  self.uidlrye8=0
  self.fo75rh8l=0
  self.n8k03w0f=0
 def yjr0fzau(self,player):
  self.n8k03w0f+=0.35*(self.holeyrvx/self.wppsfnko if self.wppsfnko else 1)
  p2nv01zd=k1wj0tpa[self.type]
  if self.fo75rh8l>0:
   self.fo75rh8l-=1
   if self.fo75rh8l<=0:
    self.holeyrvx=self.wppsfnko
   return False
  if self.uidlrye8>0:
   self.uidlrye8-=1
   return False
  if abs(player.cq2q4qer.eolaq665-self.cq2q4qer.eolaq665)<p2nv01zd['w9laac']and abs(player.cq2q4qer.t5ivrocv-self.cq2q4qer.t5ivrocv)<p2nv01zd['w9laac']:
   self.holeyrvx=self.wppsfnko*p2nv01zd['nddqhk']
   self.fo75rh8l=p2nv01zd['v00vhm']
   self.uidlrye8=p2nv01zd['kj2jvq']
  return False
 def tnz61231(self,q3n2qb6g,clkqzfpq,x5m9j98c):
  eolaq665=self.cq2q4qer.eolaq665-clkqzfpq
  t5ivrocv=self.cq2q4qer.t5ivrocv-x5m9j98c
  g8kk791z=self.cq2q4qer.centerx-clkqzfpq
  wzlm72je=self.cq2q4qer.centery-x5m9j98c
  we4xyf9i=self.cq2q4qer.width//2
  zpajssuu=t5ivrocv+self.cq2q4qer.height-3
  nii6l3ue=(25,25,25)
  j1ldqnk2=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(jyjhu8my,v3e1ocjx,k1taa0i5)in j1ldqnk2:
   tjy1o2rn=math.sin(self.n8k03w0f+k1taa0i5)
   mcup8ijl=max(0,tjy1o2rn)*4
   rktlzkj4=(g8kk791z+jyjhu8my*we4xyf9i*0.7,wzlm72je+v3e1ocjx)
   jq1ddpus=g8kk791z+jyjhu8my*(we4xyf9i+9)+tjy1o2rn*3
   damdvlnk=zpajssuu-mcup8ijl
   zflv1xxl=((rktlzkj4[0]+jq1ddpus)/2,(rktlzkj4[1]+damdvlnk)/2-2)
   pygame.draw.line(q3n2qb6g,nii6l3ue,rktlzkj4,zflv1xxl,3)
   pygame.draw.line(q3n2qb6g,nii6l3ue,zflv1xxl,(jq1ddpus,damdvlnk),3)
  self.win4olr6(q3n2qb6g,eolaq665,t5ivrocv,g8kk791z,wzlm72je)
