import pygame
import math
from e87f8tsx import*
from.odog8cfe import f935a0l7
class ozp08j3t(f935a0l7):
 def __init__(self,yrivh6t1,j1kfk7y6,f1bl08kg):
  super().__init__(yrivh6t1,j1kfk7y6,f1bl08kg)
  self.rzewviyt=0
  self.uidlrye8=0
  self.q6p61xuf=0
 def ceb8753a(self,player):
  self.q6p61xuf+=0.35*(self.hcxhgnze/self.bq349dxb if self.bq349dxb else 1)
  yypp5zp7=k1wj0tpa[self.type]
  if self.uidlrye8>0:
   self.uidlrye8-=1
   if self.uidlrye8<=0:
    self.hcxhgnze=self.bq349dxb
   return False
  if self.rzewviyt>0:
   self.rzewviyt-=1
   return False
  if abs(player.pllkstn3.j1kfk7y6-self.pllkstn3.j1kfk7y6)<yypp5zp7['rw8p74']and abs(player.pllkstn3.f1bl08kg-self.pllkstn3.f1bl08kg)<yypp5zp7['rw8p74']:
   self.hcxhgnze=self.bq349dxb*yypp5zp7['kj2jvq']
   self.uidlrye8=yypp5zp7['onlt8d']
   self.rzewviyt=yypp5zp7['mrf5a7']
  return False
 def dw7nh8rq(self,byl68ntk,i20cv3tl,clkqzfpq):
  j1kfk7y6=self.pllkstn3.j1kfk7y6-i20cv3tl
  f1bl08kg=self.pllkstn3.f1bl08kg-clkqzfpq
  rmm1zxyv=self.pllkstn3.centerx-i20cv3tl
  g8kk791z=self.pllkstn3.centery-clkqzfpq
  gsmdzqcb=self.pllkstn3.width//2
  vmxb9yo1=f1bl08kg+self.pllkstn3.height-3
  lnf74t60=(25,25,25)
  v6g298cq=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(v24479qt,rktlzkj4,upprat08)in v6g298cq:
   kodpvjtu=math.sin(self.q6p61xuf+upprat08)
   qo6q0usw=max(0,kodpvjtu)*4
   wvpw232u=(rmm1zxyv+v24479qt*gsmdzqcb*0.7,g8kk791z+rktlzkj4)
   cjn2fomd=rmm1zxyv+v24479qt*(gsmdzqcb+9)+kodpvjtu*3
   jq1ddpus=vmxb9yo1-qo6q0usw
   mctwjlsh=((wvpw232u[0]+cjn2fomd)/2,(wvpw232u[1]+jq1ddpus)/2-2)
   pygame.draw.line(byl68ntk,lnf74t60,wvpw232u,mctwjlsh,3)
   pygame.draw.line(byl68ntk,lnf74t60,mctwjlsh,(cjn2fomd,jq1ddpus),3)
  self.eqrl1n75(byl68ntk,j1kfk7y6,f1bl08kg,rmm1zxyv,g8kk791z)
