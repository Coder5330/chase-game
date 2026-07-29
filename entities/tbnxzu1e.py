import pygame
import math
from j1bmqf7z import*
from.kier7u8h import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,mqxlm5q2,x,y):
  super().__init__(mqxlm5q2,x,y)
  self.vmxb9yo1=0
 def qic1l7dy(self,player):
  self.vmxb9yo1+=1
  return False
 def v15cqzcu(self,h8s2ftom,vqnpcenl,iie0rnuj):
  x=self.npcxa5s0.x-vqnpcenl
  y=self.npcxa5s0.y-iie0rnuj
  wzlm72je=self.npcxa5s0.centerx-vqnpcenl
  vt6om1fb=self.npcxa5s0.centery-iie0rnuj
  oa47sh2s=(math.sin(self.vmxb9yo1*0.08)+1)/2
  tj0nmeoq=int(self.npcxa5s0.width*0.9+oa47sh2s*6)
  tp2ex5t5=int(50+oa47sh2s*60)
  z8z3v6di=pygame.Surface((tj0nmeoq*2,tj0nmeoq*2),pygame.SRCALPHA)
  pygame.draw.circle(z8z3v6di,(255,215,0,tp2ex5t5),(tj0nmeoq,tj0nmeoq),tj0nmeoq,width=4)
  h8s2ftom.blit(z8z3v6di,(wzlm72je-tj0nmeoq,vt6om1fb-tj0nmeoq))
  self.k44nlz15(h8s2ftom,x,y,wzlm72je,vt6om1fb)
