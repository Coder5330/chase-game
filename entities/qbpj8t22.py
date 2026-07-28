import pygame
import math
from omerbyea import*
from.erp0aga2 import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,mqxlm5q2,eolaq665,t5ivrocv):
  super().__init__(mqxlm5q2,eolaq665,t5ivrocv)
  self.azc4xl99=(0,1)
  self.ruq9e5co=False
  self.f2sehe2a=0
  self.lztkkfzz=18
 def yjr0fzau(self,player):
  mq7nc85e=player.cq2q4qer.centerx-self.cq2q4qer.centerx
  le9oe941=player.cq2q4qer.centery-self.cq2q4qer.centery
  xwqvr1h6=math.hypot(mq7nc85e,le9oe941)or 1
  self.azc4xl99=(mq7nc85e/xwqvr1h6,le9oe941/xwqvr1h6)
  if self.ruq9e5co:
   self.f2sehe2a-=1
   if self.f2sehe2a<=0:
    self.ruq9e5co=False
    self.x9bp4m18(player)
   return True
  if abs(player.cq2q4qer.eolaq665-self.cq2q4qer.eolaq665)<b8cgvyie and abs(player.cq2q4qer.t5ivrocv-self.cq2q4qer.t5ivrocv)<b8cgvyie:
   if self.kmgfxc08>0:
    self.kmgfxc08-=1
    return True
   self.ruq9e5co=True
   self.f2sehe2a=self.lztkkfzz
   return True
  return False
 def x9bp4m18(self,player):
  self.kmgfxc08=self.kybwmlun
  from wh0imjyj import rpqk51fp
  hdw6lqwl=uqjiujv6['tk7bpg']['lpug99']
  (mq7nc85e,le9oe941)=(player.cq2q4qer.centerx-self.cq2q4qer.centerx,player.cq2q4qer.centery-self.cq2q4qer.centery)
  vj8yrddp=rpqk51fp('tk7bpg',self.cq2q4qer.centerx-hdw6lqwl//2,self.cq2q4qer.centery-hdw6lqwl//2,hdw6lqwl,hdw6lqwl,mq7nc85e,le9oe941)
  vj8yrddp.vt6om1fb=self.yjluujmi
  self.l57p6bkl.append(vj8yrddp)
 def tnz61231(self,q3n2qb6g,clkqzfpq,x5m9j98c):
  eolaq665=self.cq2q4qer.eolaq665-clkqzfpq
  t5ivrocv=self.cq2q4qer.t5ivrocv-x5m9j98c
  g8kk791z=self.cq2q4qer.centerx-clkqzfpq
  wzlm72je=self.cq2q4qer.centery-x5m9j98c
  self.win4olr6(q3n2qb6g,eolaq665,t5ivrocv,g8kk791z,wzlm72je)
  (a8lw2lm3,u9el8hl8)=self.azc4xl99
  (d46aexl6,tj0nmeoq)=(-u9el8hl8,a8lw2lm3)
  (f32ejx5t,dzsedfqs)=(g8kk791z+a8lw2lm3*14,wzlm72je+u9el8hl8*14)
  htgsiwg0=(f32ejx5t+d46aexl6*13-a8lw2lm3*6,dzsedfqs+tj0nmeoq*13-u9el8hl8*6)
  n01uyzpd=(f32ejx5t-d46aexl6*13-a8lw2lm3*6,dzsedfqs-tj0nmeoq*13-u9el8hl8*6)
  pvasifpw=(f32ejx5t+a8lw2lm3*6,dzsedfqs+u9el8hl8*6)
  pygame.draw.lines(q3n2qb6g,(110,70,30),False,[htgsiwg0,pvasifpw,n01uyzpd],3)
  v15cqzcu=1-self.f2sehe2a/self.lztkkfzz if self.ruq9e5co else 0
  x6cnoljq=(f32ejx5t-a8lw2lm3*(3+v15cqzcu*10),dzsedfqs-u9el8hl8*(3+v15cqzcu*10))
  pygame.draw.line(q3n2qb6g,(225,225,215),htgsiwg0,x6cnoljq,2)
  pygame.draw.line(q3n2qb6g,(225,225,215),n01uyzpd,x6cnoljq,2)
  if self.ruq9e5co:
   x03uvule=(f32ejx5t+a8lw2lm3*8,dzsedfqs+u9el8hl8*8)
   pygame.draw.line(q3n2qb6g,iq5c34dx['o0mb1l'],x6cnoljq,x03uvule,3)
