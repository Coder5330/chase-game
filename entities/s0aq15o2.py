import pygame
import math
from entfk7or import*
from.tnyy95g5 import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,yrivh6t1,w2sq3b9s,owdz09wf):
  super().__init__(yrivh6t1,w2sq3b9s,owdz09wf)
  nv23gxj0=k1wj0tpa[yrivh6t1]
  self.rserev36=nv23gxj0['xbtfbs']
  self.k7vcneas=nv23gxj0['prf7bn']
  self.qy3vg6v5=nv23gxj0['gpm21b']
  self.nbwye6qv=nv23gxj0['zhbgcj']
  self.la3kkrzd=nv23gxj0['xbtfbs']
  self.bf7so8w5='hidden'
  self.xxkdq95g=self.k7vcneas
 def e5x4w7ky(self):
  self.xxkdq95g-=1
  if self.xxkdq95g<=0:
   if self.bf7so8w5=='hidden':
    self.bf7so8w5='revealing'
    self.xxkdq95g=self.nbwye6qv
   elif self.bf7so8w5=='revealing':
    self.bf7so8w5='visible'
    self.xxkdq95g=self.qy3vg6v5
   else:
    self.bf7so8w5='hidden'
    self.xxkdq95g=self.k7vcneas
  self.la3kkrzd=self.rserev36 if self.bf7so8w5=='hidden'else 255
 def oc4kl8cg(self,player):
  if self.ftrflqbm<=0:
   self.fp47b42g=True
   return
  self.e5x4w7ky()
  if self.bf7so8w5=='visible'and abs(player.npcxa5s0.w2sq3b9s-self.npcxa5s0.w2sq3b9s)<cawudtse and(abs(player.npcxa5s0.owdz09wf-self.npcxa5s0.owdz09wf)<cawudtse):
   self.nrpj1epk(player)
   return
  mq7nc85e=player.npcxa5s0.w2sq3b9s-self.npcxa5s0.w2sq3b9s
  le9oe941=player.npcxa5s0.owdz09wf-self.npcxa5s0.owdz09wf
  sygvwopl=math.hypot(mq7nc85e,le9oe941)
  if sygvwopl==0:
   return
  vsjchzjq=mq7nc85e/sygvwopl
  acxx6mdk=le9oe941/sygvwopl
  if vsjchzjq!=0 and acxx6mdk!=0:
   vsjchzjq*=0.707
   acxx6mdk*=0.707
  self.npcxa5s0.w2sq3b9s+=vsjchzjq*self.q6nqqb9l
  self.npcxa5s0.owdz09wf+=acxx6mdk*self.q6nqqb9l
  self.npcxa5s0.w2sq3b9s=round(self.npcxa5s0.w2sq3b9s)
  self.npcxa5s0.owdz09wf=round(self.npcxa5s0.owdz09wf)
 def tnz61231(self,h8s2ftom,obc2nnuv,vqnpcenl):
  w2sq3b9s=self.npcxa5s0.w2sq3b9s-obc2nnuv
  owdz09wf=self.npcxa5s0.owdz09wf-vqnpcenl
  g8kk791z=self.npcxa5s0.centerx-obc2nnuv
  wzlm72je=self.npcxa5s0.centery-vqnpcenl
  if self.la3kkrzd>=255:
   self.u8c2jwoc(h8s2ftom,w2sq3b9s,owdz09wf,g8kk791z,wzlm72je)
   return
  chx3d43e=24
  kc7rm6j8=pygame.Surface((self.npcxa5s0.width+chx3d43e*2,self.npcxa5s0.height+chx3d43e*2),pygame.SRCALPHA)
  (tb4ldims,vk3g84ut)=(chx3d43e,chx3d43e)
  (d1b3jczu,crsb4gf1)=(tb4ldims+self.npcxa5s0.width//2,vk3g84ut+self.npcxa5s0.height//2)
  self.u8c2jwoc(kc7rm6j8,tb4ldims,vk3g84ut,d1b3jczu,crsb4gf1)
  kc7rm6j8.set_alpha(self.la3kkrzd)
  h8s2ftom.blit(kc7rm6j8,(w2sq3b9s-chx3d43e,owdz09wf-chx3d43e))
