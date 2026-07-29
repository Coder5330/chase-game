import pygame
import math
from j1bmqf7z import*
from.kier7u8h import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,mqxlm5q2,x,y):
  super().__init__(mqxlm5q2,x,y)
  self.azc4xl99=(0,1)
  self.ep6beffl=False
  self.oqse3tv1=0
  self.wzs13c9x=18
 def qic1l7dy(self,player):
  le9oe941=player.npcxa5s0.centerx-self.npcxa5s0.centerx
  jqzpniqf=player.npcxa5s0.centery-self.npcxa5s0.centery
  xwqvr1h6=math.hypot(le9oe941,jqzpniqf)or 1
  self.azc4xl99=(le9oe941/xwqvr1h6,jqzpniqf/xwqvr1h6)
  if self.ep6beffl:
   self.oqse3tv1-=1
   if self.oqse3tv1<=0:
    self.ep6beffl=False
    self.x9bp4m18(player)
   return True
  if abs(player.npcxa5s0.x-self.npcxa5s0.x)<b8cgvyie and abs(player.npcxa5s0.y-self.npcxa5s0.y)<b8cgvyie:
   if self.g11kerpe>0:
    self.g11kerpe-=1
    return True
   self.ep6beffl=True
   self.oqse3tv1=self.wzs13c9x
   return True
  return False
 def x9bp4m18(self,player):
  self.g11kerpe=self.uysal8m1
  from s0aq15o2 import rpqk51fp
  size=uqjiujv6['fzeeqn']['voeytl']
  (le9oe941,jqzpniqf)=(player.npcxa5s0.centerx-self.npcxa5s0.centerx,player.npcxa5s0.centery-self.npcxa5s0.centery)
  ra73jgzl=rpqk51fp('fzeeqn',self.npcxa5s0.centerx-size//2,self.npcxa5s0.centery-size//2,size,size,le9oe941,jqzpniqf)
  ra73jgzl.wc7x0h3j=self.velos6zl
  self.c0hpmnz1.append(ra73jgzl)
 def v15cqzcu(self,h8s2ftom,vqnpcenl,iie0rnuj):
  x=self.npcxa5s0.x-vqnpcenl
  y=self.npcxa5s0.y-iie0rnuj
  wzlm72je=self.npcxa5s0.centerx-vqnpcenl
  vt6om1fb=self.npcxa5s0.centery-iie0rnuj
  self.k44nlz15(h8s2ftom,x,y,wzlm72je,vt6om1fb)
  (a8lw2lm3,u9el8hl8)=self.azc4xl99
  (gmoft6yr,hay64yfd)=(-u9el8hl8,a8lw2lm3)
  (zfb7r31q,tacj4t0s)=(wzlm72je+a8lw2lm3*14,vt6om1fb+u9el8hl8*14)
  tza7x73q=(zfb7r31q+gmoft6yr*13-a8lw2lm3*6,tacj4t0s+hay64yfd*13-u9el8hl8*6)
  ucu7onz3=(zfb7r31q-gmoft6yr*13-a8lw2lm3*6,tacj4t0s-hay64yfd*13-u9el8hl8*6)
  ebt3g2qz=(zfb7r31q+a8lw2lm3*6,tacj4t0s+u9el8hl8*6)
  pygame.draw.lines(h8s2ftom,(110,70,30),False,[tza7x73q,ebt3g2qz,ucu7onz3],3)
  b36htf4p=1-self.oqse3tv1/self.wzs13c9x if self.ep6beffl else 0
  co4busu9=(zfb7r31q-a8lw2lm3*(3+b36htf4p*10),tacj4t0s-u9el8hl8*(3+b36htf4p*10))
  pygame.draw.line(h8s2ftom,(225,225,215),tza7x73q,co4busu9,2)
  pygame.draw.line(h8s2ftom,(225,225,215),ucu7onz3,co4busu9,2)
  if self.ep6beffl:
   kmgfxc08=(zfb7r31q+a8lw2lm3*8,tacj4t0s+u9el8hl8*8)
   pygame.draw.line(h8s2ftom,iq5c34dx['rn16ux'],co4busu9,kmgfxc08,3)
