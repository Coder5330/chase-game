import pygame
import math
from omerbyea import*
from.erp0aga2 import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,mqxlm5q2,eolaq665,t5ivrocv):
  super().__init__(mqxlm5q2,eolaq665,t5ivrocv)
  self.vmxb9yo1=0
 def yjr0fzau(self,player):
  self.vmxb9yo1+=1
  return False
 def tnz61231(self,q3n2qb6g,clkqzfpq,x5m9j98c):
  eolaq665=self.cq2q4qer.eolaq665-clkqzfpq
  t5ivrocv=self.cq2q4qer.t5ivrocv-x5m9j98c
  g8kk791z=self.cq2q4qer.centerx-clkqzfpq
  wzlm72je=self.cq2q4qer.centery-x5m9j98c
  arjn2hz2=(math.sin(self.vmxb9yo1*0.08)+1)/2
  xu9ymszd=int(self.cq2q4qer.width*0.9+arjn2hz2*6)
  am2vajep=int(50+arjn2hz2*60)
  z8z3v6di=pygame.Surface((xu9ymszd*2,xu9ymszd*2),pygame.SRCALPHA)
  pygame.draw.circle(z8z3v6di,(255,215,0,am2vajep),(xu9ymszd,xu9ymszd),xu9ymszd,width=4)
  q3n2qb6g.blit(z8z3v6di,(g8kk791z-xu9ymszd,wzlm72je-xu9ymszd))
  self.win4olr6(q3n2qb6g,eolaq665,t5ivrocv,g8kk791z,wzlm72je)
