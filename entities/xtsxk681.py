import pygame
import math
from zfiblejg import*
from.vpbnqs3q import f935a0l7
class qxaprpn6(f935a0l7):
 def __init__(self,g5l8a78e,x3zo7utx,cjy62zee):
  super().__init__(g5l8a78e,x3zo7utx,cjy62zee)
  self.rzewviyt=0
  self.uidlrye8=0
  self.iimoe0sy=0
 def qic1l7dy(self,player):
  self.iimoe0sy+=0.35*(self.p7b1ijiy/self.i0x65muf if self.i0x65muf else 1)
  xxkdq95g=k1wj0tpa[self.type]
  if self.uidlrye8>0:
   self.uidlrye8-=1
   if self.uidlrye8<=0:
    self.p7b1ijiy=self.i0x65muf
   return False
  if self.rzewviyt>0:
   self.rzewviyt-=1
   return False
  if abs(player.tby49e7e.x3zo7utx-self.tby49e7e.x3zo7utx)<xxkdq95g['jr87iy']and abs(player.tby49e7e.cjy62zee-self.tby49e7e.cjy62zee)<xxkdq95g['jr87iy']:
   self.p7b1ijiy=self.i0x65muf*xxkdq95g['mrf5a7']
   self.uidlrye8=xxkdq95g['bx1ego']
   self.rzewviyt=xxkdq95g['hx0gu4']
  return False
 def dw7nh8rq(self,uwxrum2l,uos0fb4y,obc2nnuv):
  x3zo7utx=self.tby49e7e.x3zo7utx-uos0fb4y
  cjy62zee=self.tby49e7e.cjy62zee-obc2nnuv
  rmm1zxyv=self.tby49e7e.centerx-uos0fb4y
  g8kk791z=self.tby49e7e.centery-obc2nnuv
  jo8e7flq=self.tby49e7e.width//2
  z8z3v6di=cjy62zee+self.tby49e7e.height-3
  sye0a4ab=(25,25,25)
  nii6l3ue=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(xo2t8fy6,rktlzkj4,cqheyto5)in nii6l3ue:
   rserev36=math.sin(self.iimoe0sy+cqheyto5)
   hp89fkbi=max(0,rserev36)*4
   wvpw232u=(rmm1zxyv+xo2t8fy6*jo8e7flq*0.7,g8kk791z+rktlzkj4)
   mpyxdw2z=rmm1zxyv+xo2t8fy6*(jo8e7flq+9)+rserev36*3
   cjn2fomd=z8z3v6di-hp89fkbi
   b78okz1p=((wvpw232u[0]+mpyxdw2z)/2,(wvpw232u[1]+cjn2fomd)/2-2)
   pygame.draw.line(uwxrum2l,sye0a4ab,wvpw232u,b78okz1p,3)
   pygame.draw.line(uwxrum2l,sye0a4ab,b78okz1p,(mpyxdw2z,cjn2fomd),3)
  self.sld4d6af(uwxrum2l,x3zo7utx,cjy62zee,rmm1zxyv,g8kk791z)
