import pygame
from e87f8tsx import*
from.odog8cfe import f935a0l7
class gmjkv5us(f935a0l7):
 def __init__(self,yrivh6t1,j1kfk7y6,f1bl08kg):
  super().__init__(yrivh6t1,j1kfk7y6,f1bl08kg)
  yypp5zp7=k1wj0tpa[yrivh6t1]
  self.ftlpq2wg=0
  self.vpbwhvnz=yypp5zp7['urf1hx']
  self.gkz2u2tn=yypp5zp7['ozdcuj']
  self.gqj5sxvw=yypp5zp7['ozdcuj']
  self.semqgy27=yypp5zp7['oarxab']
 def ceb8753a(self,player):
  self.ftlpq2wg+=1
  if self.ftlpq2wg>=self.vpbwhvnz and self.gqj5sxvw>0:
   self.ftlpq2wg=0
   self.x875aud9+=self.semqgy27
   self.gqj5sxvw-=self.semqgy27
  return False
 def dw7nh8rq(self,byl68ntk,i20cv3tl,clkqzfpq):
  j1kfk7y6=self.pllkstn3.j1kfk7y6-i20cv3tl
  f1bl08kg=self.pllkstn3.f1bl08kg-clkqzfpq
  rmm1zxyv=self.pllkstn3.centerx-i20cv3tl
  g8kk791z=self.pllkstn3.centery-clkqzfpq
  self.eqrl1n75(byl68ntk,j1kfk7y6,f1bl08kg,rmm1zxyv,g8kk791z)
  xwk2rv23=1-self.gqj5sxvw/self.gkz2u2tn if self.gkz2u2tn else 0
  xsspye9r=int(xwk2rv23*3)
  jenvg3kk=(70,70,75)
  exvaj2k8=(30,30,30)
  for bokzixza in range(xsspye9r):
   g11kerpe=f1bl08kg+6+bokzixza*8
   vvslh9bh=pygame.Rect(j1kfk7y6+2,g11kerpe,self.pllkstn3.width-4,5)
   pygame.draw.rect(byl68ntk,jenvg3kk,vvslh9bh,border_radius=1)
   pygame.draw.rect(byl68ntk,exvaj2k8,vvslh9bh,width=1,border_radius=1)
