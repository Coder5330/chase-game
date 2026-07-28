import pygame
import math
from entfk7or import*
from.tnyy95g5 import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,yrivh6t1,w2sq3b9s,owdz09wf):
  super().__init__(yrivh6t1,w2sq3b9s,owdz09wf)
  self.cx41dntc=(0,1)
  self.oqse3tv1=False
  self.wzs13c9x=0
  self.ruq9e5co=18
 def nngmx1gm(self,player):
  mq7nc85e=player.npcxa5s0.centerx-self.npcxa5s0.centerx
  le9oe941=player.npcxa5s0.centery-self.npcxa5s0.centery
  j1ldqnk2=math.hypot(mq7nc85e,le9oe941)or 1
  self.cx41dntc=(mq7nc85e/j1ldqnk2,le9oe941/j1ldqnk2)
  if self.oqse3tv1:
   self.wzs13c9x-=1
   if self.wzs13c9x<=0:
    self.oqse3tv1=False
    self.mytn02yc(player)
   return True
  if abs(player.npcxa5s0.w2sq3b9s-self.npcxa5s0.w2sq3b9s)<b8cgvyie and abs(player.npcxa5s0.owdz09wf-self.npcxa5s0.owdz09wf)<b8cgvyie:
   if self.vvslh9bh>0:
    self.vvslh9bh-=1
    return True
   self.oqse3tv1=True
   self.wzs13c9x=self.ruq9e5co
   return True
  return False
 def mytn02yc(self,player):
  self.vvslh9bh=self.u23y30ys
  from k0b8y5dn import rpqk51fp
  svt8k06m=uqjiujv6['x1qwee']['pca7zv']
  (mq7nc85e,le9oe941)=(player.npcxa5s0.centerx-self.npcxa5s0.centerx,player.npcxa5s0.centery-self.npcxa5s0.centery)
  ykipu1wy=rpqk51fp('x1qwee',self.npcxa5s0.centerx-svt8k06m//2,self.npcxa5s0.centery-svt8k06m//2,svt8k06m,svt8k06m,mq7nc85e,le9oe941)
  ykipu1wy.vt6om1fb=self.yjluujmi
  self.kmgfxc08.append(ykipu1wy)
 def tnz61231(self,h8s2ftom,obc2nnuv,vqnpcenl):
  w2sq3b9s=self.npcxa5s0.w2sq3b9s-obc2nnuv
  owdz09wf=self.npcxa5s0.owdz09wf-vqnpcenl
  g8kk791z=self.npcxa5s0.centerx-obc2nnuv
  wzlm72je=self.npcxa5s0.centery-vqnpcenl
  self.u8c2jwoc(h8s2ftom,w2sq3b9s,owdz09wf,g8kk791z,wzlm72je)
  (cn7zrwqe,a8lw2lm3)=self.cx41dntc
  (gmoft6yr,hay64yfd)=(-a8lw2lm3,cn7zrwqe)
  (li9nb74x,zfb7r31q)=(g8kk791z+cn7zrwqe*14,wzlm72je+a8lw2lm3*14)
  ucu7onz3=(li9nb74x+gmoft6yr*13-cn7zrwqe*6,zfb7r31q+hay64yfd*13-a8lw2lm3*6)
  it04chsd=(li9nb74x-gmoft6yr*13-cn7zrwqe*6,zfb7r31q-hay64yfd*13-a8lw2lm3*6)
  amcixdu1=(li9nb74x+cn7zrwqe*6,zfb7r31q+a8lw2lm3*6)
  pygame.draw.lines(h8s2ftom,(110,70,30),False,[ucu7onz3,amcixdu1,it04chsd],3)
  v15cqzcu=1-self.wzs13c9x/self.ruq9e5co if self.oqse3tv1 else 0
  co4busu9=(li9nb74x-cn7zrwqe*(3+v15cqzcu*10),zfb7r31q-a8lw2lm3*(3+v15cqzcu*10))
  pygame.draw.line(h8s2ftom,(225,225,215),ucu7onz3,co4busu9,2)
  pygame.draw.line(h8s2ftom,(225,225,215),it04chsd,co4busu9,2)
  if self.oqse3tv1:
   ra73jgzl=(li9nb74x+cn7zrwqe*8,zfb7r31q+a8lw2lm3*8)
   pygame.draw.line(h8s2ftom,iq5c34dx['za5ivr'],co4busu9,ra73jgzl,3)
