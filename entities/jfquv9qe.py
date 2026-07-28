import pygame
import math
from e87f8tsx import*
from.odog8cfe import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,yrivh6t1,j1kfk7y6,f1bl08kg):
  super().__init__(yrivh6t1,j1kfk7y6,f1bl08kg)
  self.cx41dntc=(0,1)
  self.f2sehe2a=False
  self.lztkkfzz=0
  self.cq6qdy4l=18
 def ceb8753a(self,player):
  pbo119xp=player.pllkstn3.centerx-self.pllkstn3.centerx
  mq7nc85e=player.pllkstn3.centery-self.pllkstn3.centery
  j1ldqnk2=math.hypot(pbo119xp,mq7nc85e)or 1
  self.cx41dntc=(pbo119xp/j1ldqnk2,mq7nc85e/j1ldqnk2)
  if self.f2sehe2a:
   self.lztkkfzz-=1
   if self.lztkkfzz<=0:
    self.f2sehe2a=False
    self.mytn02yc(player)
   return True
  if abs(player.pllkstn3.j1kfk7y6-self.pllkstn3.j1kfk7y6)<b8cgvyie and abs(player.pllkstn3.f1bl08kg-self.pllkstn3.f1bl08kg)<b8cgvyie:
   if self.ra73jgzl>0:
    self.ra73jgzl-=1
    return True
   self.f2sehe2a=True
   self.lztkkfzz=self.cq6qdy4l
   return True
  return False
 def mytn02yc(self,player):
  self.ra73jgzl=self.wppsfnko
  from bdnwnguc import rpqk51fp
  jyjhu8my=uqjiujv6['pqpva5']['jo31yh']
  (pbo119xp,mq7nc85e)=(player.pllkstn3.centerx-self.pllkstn3.centerx,player.pllkstn3.centery-self.pllkstn3.centery)
  nqimqodp=rpqk51fp('pqpva5',self.pllkstn3.centerx-jyjhu8my//2,self.pllkstn3.centery-jyjhu8my//2,jyjhu8my,jyjhu8my,pbo119xp,mq7nc85e)
  nqimqodp.wzlm72je=self.mygfliji
  self.x03uvule.append(nqimqodp)
 def dw7nh8rq(self,byl68ntk,i20cv3tl,clkqzfpq):
  j1kfk7y6=self.pllkstn3.j1kfk7y6-i20cv3tl
  f1bl08kg=self.pllkstn3.f1bl08kg-clkqzfpq
  rmm1zxyv=self.pllkstn3.centerx-i20cv3tl
  g8kk791z=self.pllkstn3.centery-clkqzfpq
  self.eqrl1n75(byl68ntk,j1kfk7y6,f1bl08kg,rmm1zxyv,g8kk791z)
  (cn7zrwqe,a8lw2lm3)=self.cx41dntc
  (bdgbk2l0,d46aexl6)=(-a8lw2lm3,cn7zrwqe)
  (gn89qkns,f32ejx5t)=(rmm1zxyv+cn7zrwqe*14,g8kk791z+a8lw2lm3*14)
  ucu7onz3=(gn89qkns+bdgbk2l0*13-cn7zrwqe*6,f32ejx5t+d46aexl6*13-a8lw2lm3*6)
  it04chsd=(gn89qkns-bdgbk2l0*13-cn7zrwqe*6,f32ejx5t-d46aexl6*13-a8lw2lm3*6)
  d1ieixwc=(gn89qkns+cn7zrwqe*6,f32ejx5t+a8lw2lm3*6)
  pygame.draw.lines(byl68ntk,(110,70,30),False,[ucu7onz3,d1ieixwc,it04chsd],3)
  tnz61231=1-self.lztkkfzz/self.cq6qdy4l if self.f2sehe2a else 0
  ncyh3fvl=(gn89qkns-cn7zrwqe*(3+tnz61231*10),f32ejx5t-a8lw2lm3*(3+tnz61231*10))
  pygame.draw.line(byl68ntk,(225,225,215),ucu7onz3,ncyh3fvl,2)
  pygame.draw.line(byl68ntk,(225,225,215),it04chsd,ncyh3fvl,2)
  if self.f2sehe2a:
   vj8yrddp=(gn89qkns+cn7zrwqe*8,f32ejx5t+a8lw2lm3*8)
   pygame.draw.line(byl68ntk,iq5c34dx['umfbuv'],ncyh3fvl,vj8yrddp,3)
