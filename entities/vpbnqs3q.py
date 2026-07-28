import pygame
import math
from vnbnqbnx import*
from.s84d4r9v import f935a0l7
class qxaprpn6(f935a0l7):
 def __init__(self,nfn1r4kz,iimoe0sy,gdg1wjui):
  super().__init__(nfn1r4kz,iimoe0sy,gdg1wjui)
  self.g8kk791z=0
  self.wzlm72je=0
  self.nngmx1gm=0
 def mabkae6a(self,player):
  self.nngmx1gm+=0.35*(self.w0p4e05q/self.z0b6ugvs if self.z0b6ugvs else 1)
  w8wj0uun=k1wj0tpa[self.type]
  if self.wzlm72je>0:
   self.wzlm72je-=1
   if self.wzlm72je<=0:
    self.w0p4e05q=self.z0b6ugvs
   return False
  if self.g8kk791z>0:
   self.g8kk791z-=1
   return False
  if abs(player.bdgbk2l0.iimoe0sy-self.bdgbk2l0.iimoe0sy)<w8wj0uun['hzj7ub']and abs(player.bdgbk2l0.gdg1wjui-self.bdgbk2l0.gdg1wjui)<w8wj0uun['hzj7ub']:
   self.w0p4e05q=self.z0b6ugvs*w8wj0uun['buzery']
   self.wzlm72je=w8wj0uun['mmgvu4']
   self.g8kk791z=w8wj0uun['t7wqp3']
  return False
 def sygvwopl(self,g1b3d505,xp8mgyn2,i20cv3tl):
  iimoe0sy=self.bdgbk2l0.iimoe0sy-xp8mgyn2
  gdg1wjui=self.bdgbk2l0.gdg1wjui-i20cv3tl
  yuibrsz1=self.bdgbk2l0.centerx-xp8mgyn2
  mfyb8dal=self.bdgbk2l0.centery-i20cv3tl
  z8z3v6di=self.bdgbk2l0.width//2
  mn7h9g1a=gdg1wjui+self.bdgbk2l0.height-3
  n04cdpqv=(25,25,25)
  ls2zge2j=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(qcd81twh,rk2u1rsu,no0u93mz)in ls2zge2j:
   holeyrvx=math.sin(self.nngmx1gm+no0u93mz)
   v6g298cq=max(0,holeyrvx)*4
   w4rcb1kj=(yuibrsz1+qcd81twh*z8z3v6di*0.7,mfyb8dal+rk2u1rsu)
   sf337kuu=yuibrsz1+qcd81twh*(z8z3v6di+9)+holeyrvx*3
   mytn02yc=mn7h9g1a-v6g298cq
   k2ixivzk=((w4rcb1kj[0]+sf337kuu)/2,(w4rcb1kj[1]+mytn02yc)/2-2)
   pygame.draw.line(g1b3d505,n04cdpqv,w4rcb1kj,k2ixivzk,3)
   pygame.draw.line(g1b3d505,n04cdpqv,k2ixivzk,(sf337kuu,mytn02yc),3)
  self.eqrl1n75(g1b3d505,iimoe0sy,gdg1wjui,yuibrsz1,mfyb8dal)
