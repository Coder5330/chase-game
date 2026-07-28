import pygame
import math
from zfiblejg import*
from.vpbnqs3q import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,g5l8a78e,x3zo7utx,cjy62zee):
  super().__init__(g5l8a78e,x3zo7utx,cjy62zee)
  xxkdq95g=k1wj0tpa[g5l8a78e]
  self.qy3vg6v5=xxkdq95g['prf7bn']
  self.nv23gxj0=xxkdq95g['tn1th1']
  self.k7vcneas=xxkdq95g['vhbef4']
  self.gg7oq2zd=xxkdq95g['th2p39']
  self.vyb6li07=xxkdq95g['prf7bn']
  self.nabufwbu='hidden'
  self.bf7so8w5=self.nv23gxj0
 def reqy08p0(self):
  self.bf7so8w5-=1
  if self.bf7so8w5<=0:
   if self.nabufwbu=='hidden':
    self.nabufwbu='revealing'
    self.bf7so8w5=self.gg7oq2zd
   elif self.nabufwbu=='revealing':
    self.nabufwbu='visible'
    self.bf7so8w5=self.k7vcneas
   else:
    self.nabufwbu='hidden'
    self.bf7so8w5=self.nv23gxj0
  self.vyb6li07=self.qy3vg6v5 if self.nabufwbu=='hidden'else 255
 def mmn32u1i(self,player):
  if self.nvuprt77<=0:
   self.uc1xi04b=True
   return
  self.reqy08p0()
  if self.nabufwbu=='visible'and abs(player.tby49e7e.x3zo7utx-self.tby49e7e.x3zo7utx)<cawudtse and(abs(player.tby49e7e.cjy62zee-self.tby49e7e.cjy62zee)<cawudtse):
   self.sv5f1bcp(player)
   return
  pbo119xp=player.tby49e7e.x3zo7utx-self.tby49e7e.x3zo7utx
  mq7nc85e=player.tby49e7e.cjy62zee-self.tby49e7e.cjy62zee
  zefqjg02=math.hypot(pbo119xp,mq7nc85e)
  if zefqjg02==0:
   return
  yjr0fzau=pbo119xp/zefqjg02
  vsjchzjq=mq7nc85e/zefqjg02
  if yjr0fzau!=0 and vsjchzjq!=0:
   yjr0fzau*=0.707
   vsjchzjq*=0.707
  self.tby49e7e.x3zo7utx+=yjr0fzau*self.p7b1ijiy
  self.tby49e7e.cjy62zee+=vsjchzjq*self.p7b1ijiy
  self.tby49e7e.x3zo7utx=round(self.tby49e7e.x3zo7utx)
  self.tby49e7e.cjy62zee=round(self.tby49e7e.cjy62zee)
 def dw7nh8rq(self,uwxrum2l,uos0fb4y,obc2nnuv):
  x3zo7utx=self.tby49e7e.x3zo7utx-uos0fb4y
  cjy62zee=self.tby49e7e.cjy62zee-obc2nnuv
  rmm1zxyv=self.tby49e7e.centerx-uos0fb4y
  g8kk791z=self.tby49e7e.centery-obc2nnuv
  if self.vyb6li07>=255:
   self.sld4d6af(uwxrum2l,x3zo7utx,cjy62zee,rmm1zxyv,g8kk791z)
   return
  mnwxuj3a=24
  n8sa3idy=pygame.Surface((self.tby49e7e.width+mnwxuj3a*2,self.tby49e7e.height+mnwxuj3a*2),pygame.SRCALPHA)
  (gqq4d3kz,tb4ldims)=(mnwxuj3a,mnwxuj3a)
  (ls2zge2j,d1b3jczu)=(gqq4d3kz+self.tby49e7e.width//2,tb4ldims+self.tby49e7e.height//2)
  self.sld4d6af(n8sa3idy,gqq4d3kz,tb4ldims,ls2zge2j,d1b3jczu)
  n8sa3idy.set_alpha(self.vyb6li07)
  uwxrum2l.blit(n8sa3idy,(x3zo7utx-mnwxuj3a,cjy62zee-mnwxuj3a))
