import pygame
import math
from e87f8tsx import*
from.odog8cfe import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,yrivh6t1,j1kfk7y6,f1bl08kg):
  super().__init__(yrivh6t1,j1kfk7y6,f1bl08kg)
  yypp5zp7=k1wj0tpa[yrivh6t1]
  self.az2ueaxy=yypp5zp7['c6zvlh']
  self.p2nv01zd=yypp5zp7['gpm21b']
  self.ej16dvtj=yypp5zp7['xbtfbs']
  self.t5sn961j=yypp5zp7['yoztp7']
  self.gp6orsnc=yypp5zp7['c6zvlh']
  self.qy3vg6v5='hidden'
  self.rserev36=self.p2nv01zd
 def v982n2at(self):
  self.rserev36-=1
  if self.rserev36<=0:
   if self.qy3vg6v5=='hidden':
    self.qy3vg6v5='revealing'
    self.rserev36=self.t5sn961j
   elif self.qy3vg6v5=='revealing':
    self.qy3vg6v5='visible'
    self.rserev36=self.ej16dvtj
   else:
    self.qy3vg6v5='hidden'
    self.rserev36=self.p2nv01zd
  self.gp6orsnc=self.az2ueaxy if self.qy3vg6v5=='hidden'else 255
 def wb7f6fdh(self,player):
  if self.ftrflqbm<=0:
   self.uc1xi04b=True
   return
  self.v982n2at()
  if self.qy3vg6v5=='visible'and abs(player.pllkstn3.j1kfk7y6-self.pllkstn3.j1kfk7y6)<cawudtse and(abs(player.pllkstn3.f1bl08kg-self.pllkstn3.f1bl08kg)<cawudtse):
   self.ykipu1wy(player)
   return
  pbo119xp=player.pllkstn3.j1kfk7y6-self.pllkstn3.j1kfk7y6
  mq7nc85e=player.pllkstn3.f1bl08kg-self.pllkstn3.f1bl08kg
  zefqjg02=math.hypot(pbo119xp,mq7nc85e)
  if zefqjg02==0:
   return
  un9sz6rv=pbo119xp/zefqjg02
  cgsq7ait=mq7nc85e/zefqjg02
  if un9sz6rv!=0 and cgsq7ait!=0:
   un9sz6rv*=0.707
   cgsq7ait*=0.707
  self.pllkstn3.j1kfk7y6+=un9sz6rv*self.hcxhgnze
  self.pllkstn3.f1bl08kg+=cgsq7ait*self.hcxhgnze
  self.pllkstn3.j1kfk7y6=round(self.pllkstn3.j1kfk7y6)
  self.pllkstn3.f1bl08kg=round(self.pllkstn3.f1bl08kg)
 def dw7nh8rq(self,byl68ntk,i20cv3tl,clkqzfpq):
  j1kfk7y6=self.pllkstn3.j1kfk7y6-i20cv3tl
  f1bl08kg=self.pllkstn3.f1bl08kg-clkqzfpq
  rmm1zxyv=self.pllkstn3.centerx-i20cv3tl
  g8kk791z=self.pllkstn3.centery-clkqzfpq
  if self.gp6orsnc>=255:
   self.eqrl1n75(byl68ntk,j1kfk7y6,f1bl08kg,rmm1zxyv,g8kk791z)
   return
  lhgk5bwi=24
  bsp7bm41=pygame.Surface((self.pllkstn3.width+lhgk5bwi*2,self.pllkstn3.height+lhgk5bwi*2),pygame.SRCALPHA)
  (dq2fa39e,mnwxuj3a)=(lhgk5bwi,lhgk5bwi)
  (d1b3jczu,crsb4gf1)=(dq2fa39e+self.pllkstn3.width//2,mnwxuj3a+self.pllkstn3.height//2)
  self.eqrl1n75(bsp7bm41,dq2fa39e,mnwxuj3a,d1b3jczu,crsb4gf1)
  bsp7bm41.set_alpha(self.gp6orsnc)
  byl68ntk.blit(bsp7bm41,(j1kfk7y6-lhgk5bwi,f1bl08kg-lhgk5bwi))
