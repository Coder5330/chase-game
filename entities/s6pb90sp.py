import pygame
import math
from jggz62fe import*
from.wh0imjyj import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,xq46nouh,x,y):
  super().__init__(xq46nouh,x,y)
  self.q7i6yuj7=(0,1)
  self.wi8skch8=False
  self.ep6beffl=0
  self.oqse3tv1=18
 def nngmx1gm(self,player):
  jqzpniqf=player.xu9ymszd.centerx-self.xu9ymszd.centerx
  g70e3p15=player.xu9ymszd.centery-self.xu9ymszd.centery
  y2f7atwy=math.hypot(jqzpniqf,g70e3p15)or 1
  self.q7i6yuj7=(jqzpniqf/y2f7atwy,g70e3p15/y2f7atwy)
  if self.wi8skch8:
   self.ep6beffl-=1
   if self.ep6beffl<=0:
    self.wi8skch8=False
    self.m8lw2qit(player)
   return True
  if abs(player.xu9ymszd.x-self.xu9ymszd.x)<b8cgvyie and abs(player.xu9ymszd.y-self.xu9ymszd.y)<b8cgvyie:
   if self.rzs43c5b>0:
    self.rzs43c5b-=1
    return True
   self.wi8skch8=True
   self.ep6beffl=self.oqse3tv1
   return True
  return False
 def m8lw2qit(self,player):
  self.rzs43c5b=self.giec4d14
  from mg5wzawn import rpqk51fp
  size=uqjiujv6['x2s8nn']['zhbgcj']
  (jqzpniqf,g70e3p15)=(player.xu9ymszd.centerx-self.xu9ymszd.centerx,player.xu9ymszd.centery-self.xu9ymszd.centery)
  kmgfxc08=rpqk51fp('x2s8nn',self.xu9ymszd.centerx-size//2,self.xu9ymszd.centery-size//2,size,size,jqzpniqf,g70e3p15)
  kmgfxc08.rzewviyt=self.dw7nh8rq
  self.sv5f1bcp.append(kmgfxc08)
 def b36htf4p(self,gxlk8wru,iie0rnuj,izhwy9he):
  x=self.xu9ymszd.x-iie0rnuj
  y=self.xu9ymszd.y-izhwy9he
  vt6om1fb=self.xu9ymszd.centerx-iie0rnuj
  wc7x0h3j=self.xu9ymszd.centery-izhwy9he
  self.bwiykid9(gxlk8wru,x,y,vt6om1fb,wc7x0h3j)
  (u9el8hl8,kkzruin3)=self.q7i6yuj7
  (hay64yfd,qc06xq9j)=(-kkzruin3,u9el8hl8)
  (tacj4t0s,d1ieixwc)=(vt6om1fb+u9el8hl8*14,wc7x0h3j+kkzruin3*14)
  ucu7onz3=(tacj4t0s+hay64yfd*13-u9el8hl8*6,d1ieixwc+qc06xq9j*13-kkzruin3*6)
  it04chsd=(tacj4t0s-hay64yfd*13-u9el8hl8*6,d1ieixwc-qc06xq9j*13-kkzruin3*6)
  ugez7bh2=(tacj4t0s+u9el8hl8*6,d1ieixwc+kkzruin3*6)
  pygame.draw.lines(gxlk8wru,(110,70,30),False,[ucu7onz3,ugez7bh2,it04chsd],3)
  vhuds3qs=1-self.ep6beffl/self.oqse3tv1 if self.wi8skch8 else 0
  ee1g983e=(tacj4t0s-u9el8hl8*(3+vhuds3qs*10),d1ieixwc-kkzruin3*(3+vhuds3qs*10))
  pygame.draw.line(gxlk8wru,(225,225,215),ucu7onz3,ee1g983e,2)
  pygame.draw.line(gxlk8wru,(225,225,215),it04chsd,ee1g983e,2)
  if self.wi8skch8:
   c0hpmnz1=(tacj4t0s+u9el8hl8*8,d1ieixwc+kkzruin3*8)
   pygame.draw.line(gxlk8wru,iq5c34dx['egzpl1'],ee1g983e,c0hpmnz1,3)
