import pygame
import math
from zfiblejg import*
from.vpbnqs3q import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,g5l8a78e,x3zo7utx,cjy62zee):
  super().__init__(g5l8a78e,x3zo7utx,cjy62zee)
  self.mc8qizk3=(0,1)
  self.wzs13c9x=False
  self.ruq9e5co=0
  self.f2sehe2a=18
 def qic1l7dy(self,player):
  pbo119xp=player.tby49e7e.centerx-self.tby49e7e.centerx
  mq7nc85e=player.tby49e7e.centery-self.tby49e7e.centery
  v6g298cq=math.hypot(pbo119xp,mq7nc85e)or 1
  self.mc8qizk3=(pbo119xp/v6g298cq,mq7nc85e/v6g298cq)
  if self.wzs13c9x:
   self.ruq9e5co-=1
   if self.ruq9e5co<=0:
    self.wzs13c9x=False
    self.sf337kuu(player)
   return True
  if abs(player.tby49e7e.x3zo7utx-self.tby49e7e.x3zo7utx)<b8cgvyie and abs(player.tby49e7e.cjy62zee-self.tby49e7e.cjy62zee)<b8cgvyie:
   if self.nrpj1epk>0:
    self.nrpj1epk-=1
    return True
   self.wzs13c9x=True
   self.ruq9e5co=self.f2sehe2a
   return True
  return False
 def sf337kuu(self,player):
  self.nrpj1epk=self.llxxezdu
  from uc6lbpj8 import rpqk51fp
  z5x8a5fb=uqjiujv6['s55ff1']['yoztp7']
  (pbo119xp,mq7nc85e)=(player.tby49e7e.centerx-self.tby49e7e.centerx,player.tby49e7e.centery-self.tby49e7e.centery)
  duhxid4n=rpqk51fp('s55ff1',self.tby49e7e.centerx-z5x8a5fb//2,self.tby49e7e.centery-z5x8a5fb//2,z5x8a5fb,z5x8a5fb,pbo119xp,mq7nc85e)
  duhxid4n.wzlm72je=self.mygfliji
  self.ra73jgzl.append(duhxid4n)
 def dw7nh8rq(self,uwxrum2l,uos0fb4y,obc2nnuv):
  x3zo7utx=self.tby49e7e.x3zo7utx-uos0fb4y
  cjy62zee=self.tby49e7e.cjy62zee-obc2nnuv
  rmm1zxyv=self.tby49e7e.centerx-uos0fb4y
  g8kk791z=self.tby49e7e.centery-obc2nnuv
  self.sld4d6af(uwxrum2l,x3zo7utx,cjy62zee,rmm1zxyv,g8kk791z)
  (fekrcppr,cn7zrwqe)=self.mc8qizk3
  (xwk2rv23,gmoft6yr)=(-cn7zrwqe,fekrcppr)
  (nd6357oo,li9nb74x)=(rmm1zxyv+fekrcppr*14,g8kk791z+cn7zrwqe*14)
  tza7x73q=(nd6357oo+xwk2rv23*13-fekrcppr*6,li9nb74x+gmoft6yr*13-cn7zrwqe*6)
  ucu7onz3=(nd6357oo-xwk2rv23*13-fekrcppr*6,li9nb74x-gmoft6yr*13-cn7zrwqe*6)
  z9toqw9j=(nd6357oo+fekrcppr*6,li9nb74x+cn7zrwqe*6)
  pygame.draw.lines(uwxrum2l,(110,70,30),False,[tza7x73q,z9toqw9j,ucu7onz3],3)
  tnz61231=1-self.ruq9e5co/self.f2sehe2a if self.wzs13c9x else 0
  m3pt5r5r=(nd6357oo-fekrcppr*(3+tnz61231*10),li9nb74x-cn7zrwqe*(3+tnz61231*10))
  pygame.draw.line(uwxrum2l,(225,225,215),tza7x73q,m3pt5r5r,2)
  pygame.draw.line(uwxrum2l,(225,225,215),ucu7onz3,m3pt5r5r,2)
  if self.wzs13c9x:
   ykipu1wy=(nd6357oo+fekrcppr*8,li9nb74x+cn7zrwqe*8)
   pygame.draw.line(uwxrum2l,iq5c34dx['d68a1a'],m3pt5r5r,ykipu1wy,3)
