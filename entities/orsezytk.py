import pygame
import math
from entfk7or import*
from.tnyy95g5 import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,yrivh6t1,w2sq3b9s,owdz09wf):
  super().__init__(yrivh6t1,w2sq3b9s,owdz09wf)
  self.z8z3v6di=0
 def nngmx1gm(self,player):
  self.z8z3v6di+=1
  return False
 def tnz61231(self,h8s2ftom,obc2nnuv,vqnpcenl):
  w2sq3b9s=self.npcxa5s0.w2sq3b9s-obc2nnuv
  owdz09wf=self.npcxa5s0.owdz09wf-vqnpcenl
  g8kk791z=self.npcxa5s0.centerx-obc2nnuv
  wzlm72je=self.npcxa5s0.centery-vqnpcenl
  wigbiaf9=(math.sin(self.z8z3v6di*0.08)+1)/2
  tj0nmeoq=int(self.npcxa5s0.width*0.9+wigbiaf9*6)
  ejwtl9tq=int(50+wigbiaf9*60)
  o9ros7yt=pygame.Surface((tj0nmeoq*2,tj0nmeoq*2),pygame.SRCALPHA)
  pygame.draw.circle(o9ros7yt,(255,215,0,ejwtl9tq),(tj0nmeoq,tj0nmeoq),tj0nmeoq,width=4)
  h8s2ftom.blit(o9ros7yt,(g8kk791z-tj0nmeoq,wzlm72je-tj0nmeoq))
  self.u8c2jwoc(h8s2ftom,w2sq3b9s,owdz09wf,g8kk791z,wzlm72je)
