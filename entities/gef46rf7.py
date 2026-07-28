import pygame
import math
from vnbnqbnx import*
from.s84d4r9v import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,nfn1r4kz,iimoe0sy,gdg1wjui):
  super().__init__(nfn1r4kz,iimoe0sy,gdg1wjui)
  w8wj0uun=k1wj0tpa[nfn1r4kz]
  self.hcxhgnze=w8wj0uun['rfu7bf']
  self.mnx4sn6s=w8wj0uun['zq9bc2']
  self.l3m25a5p=w8wj0uun['bohxs7']
  self.cq2q4qer=w8wj0uun['oarxab']
  self.ncyh3fvl=w8wj0uun['rfu7bf']
  self.p7b1ijiy='hidden'
  self.q6nqqb9l=self.mnx4sn6s
 def v982n2at(self):
  self.q6nqqb9l-=1
  if self.q6nqqb9l<=0:
   if self.p7b1ijiy=='hidden':
    self.p7b1ijiy='revealing'
    self.q6nqqb9l=self.cq2q4qer
   elif self.p7b1ijiy=='revealing':
    self.p7b1ijiy='visible'
    self.q6nqqb9l=self.l3m25a5p
   else:
    self.p7b1ijiy='hidden'
    self.q6nqqb9l=self.mnx4sn6s
  self.ncyh3fvl=self.hcxhgnze if self.p7b1ijiy=='hidden'else 255
 def j0kgazu4(self,player):
  if self.gkz2u2tn<=0:
   self.wc7x0h3j=True
   return
  self.v982n2at()
  if self.p7b1ijiy=='visible'and abs(player.bdgbk2l0.iimoe0sy-self.bdgbk2l0.iimoe0sy)<cawudtse and(abs(player.bdgbk2l0.gdg1wjui-self.bdgbk2l0.gdg1wjui)<cawudtse):
   self.ykipu1wy(player)
   return
  b36htf4p=player.bdgbk2l0.iimoe0sy-self.bdgbk2l0.iimoe0sy
  vhuds3qs=player.bdgbk2l0.gdg1wjui-self.bdgbk2l0.gdg1wjui
  uc1xi04b=math.hypot(b36htf4p,vhuds3qs)
  if uc1xi04b==0:
   return
  x3n27m5p=b36htf4p/uc1xi04b
  d5ixva1n=vhuds3qs/uc1xi04b
  if x3n27m5p!=0 and d5ixva1n!=0:
   x3n27m5p*=0.707
   d5ixva1n*=0.707
  self.bdgbk2l0.iimoe0sy+=x3n27m5p*self.w0p4e05q
  self.bdgbk2l0.gdg1wjui+=d5ixva1n*self.w0p4e05q
  self.bdgbk2l0.iimoe0sy=round(self.bdgbk2l0.iimoe0sy)
  self.bdgbk2l0.gdg1wjui=round(self.bdgbk2l0.gdg1wjui)
 def sygvwopl(self,g1b3d505,xp8mgyn2,i20cv3tl):
  iimoe0sy=self.bdgbk2l0.iimoe0sy-xp8mgyn2
  gdg1wjui=self.bdgbk2l0.gdg1wjui-i20cv3tl
  yuibrsz1=self.bdgbk2l0.centerx-xp8mgyn2
  mfyb8dal=self.bdgbk2l0.centery-i20cv3tl
  if self.ncyh3fvl>=255:
   self.eqrl1n75(g1b3d505,iimoe0sy,gdg1wjui,yuibrsz1,mfyb8dal)
   return
  yvffqot8=24
  wigbiaf9=pygame.Surface((self.bdgbk2l0.width+yvffqot8*2,self.bdgbk2l0.height+yvffqot8*2),pygame.SRCALPHA)
  (hp89fkbi,qo6q0usw)=(yvffqot8,yvffqot8)
  (b78okz1p,mctwjlsh)=(hp89fkbi+self.bdgbk2l0.width//2,qo6q0usw+self.bdgbk2l0.height//2)
  self.eqrl1n75(wigbiaf9,hp89fkbi,qo6q0usw,b78okz1p,mctwjlsh)
  wigbiaf9.set_alpha(self.ncyh3fvl)
  g1b3d505.blit(wigbiaf9,(iimoe0sy-yvffqot8,gdg1wjui-yvffqot8))
