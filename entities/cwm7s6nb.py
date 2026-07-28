import pygame
import math
from omerbyea import*
from.erp0aga2 import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,mqxlm5q2,eolaq665,t5ivrocv):
  super().__init__(mqxlm5q2,eolaq665,t5ivrocv)
  p2nv01zd=k1wj0tpa[mqxlm5q2]
  self.kodpvjtu=p2nv01zd['nf7qne']
  self.ej16dvtj=p2nv01zd['v6idii']
  self.az2ueaxy=p2nv01zd['n5nhqr']
  self.k8qeoz0k=p2nv01zd['jo31yh']
  self.zflse45b=p2nv01zd['nf7qne']
  self.rserev36='hidden'
  self.yypp5zp7=self.ej16dvtj
 def on0jnwny(self):
  self.yypp5zp7-=1
  if self.yypp5zp7<=0:
   if self.rserev36=='hidden':
    self.rserev36='revealing'
    self.yypp5zp7=self.k8qeoz0k
   elif self.rserev36=='revealing':
    self.rserev36='visible'
    self.yypp5zp7=self.az2ueaxy
   else:
    self.rserev36='hidden'
    self.yypp5zp7=self.ej16dvtj
  self.zflse45b=self.kodpvjtu if self.rserev36=='hidden'else 255
 def got7txkd(self,player):
  if self.arhnuxor<=0:
   self.fp47b42g=True
   return
  self.on0jnwny()
  if self.rserev36=='visible'and abs(player.cq2q4qer.eolaq665-self.cq2q4qer.eolaq665)<cawudtse and(abs(player.cq2q4qer.t5ivrocv-self.cq2q4qer.t5ivrocv)<cawudtse):
   self.ra73jgzl(player)
   return
  mq7nc85e=player.cq2q4qer.eolaq665-self.cq2q4qer.eolaq665
  le9oe941=player.cq2q4qer.t5ivrocv-self.cq2q4qer.t5ivrocv
  sygvwopl=math.hypot(mq7nc85e,le9oe941)
  if sygvwopl==0:
   return
  kr0aymk9=mq7nc85e/sygvwopl
  qjcjn997=le9oe941/sygvwopl
  if kr0aymk9!=0 and qjcjn997!=0:
   kr0aymk9*=0.707
   qjcjn997*=0.707
  self.cq2q4qer.eolaq665+=kr0aymk9*self.holeyrvx
  self.cq2q4qer.t5ivrocv+=qjcjn997*self.holeyrvx
  self.cq2q4qer.eolaq665=round(self.cq2q4qer.eolaq665)
  self.cq2q4qer.t5ivrocv=round(self.cq2q4qer.t5ivrocv)
 def tnz61231(self,q3n2qb6g,clkqzfpq,x5m9j98c):
  eolaq665=self.cq2q4qer.eolaq665-clkqzfpq
  t5ivrocv=self.cq2q4qer.t5ivrocv-x5m9j98c
  g8kk791z=self.cq2q4qer.centerx-clkqzfpq
  wzlm72je=self.cq2q4qer.centery-x5m9j98c
  if self.zflse45b>=255:
   self.win4olr6(q3n2qb6g,eolaq665,t5ivrocv,g8kk791z,wzlm72je)
   return
  jr5rdnpx=24
  o9zqyahu=pygame.Surface((self.cq2q4qer.width+jr5rdnpx*2,self.cq2q4qer.height+jr5rdnpx*2),pygame.SRCALPHA)
  (mnwxuj3a,chx3d43e)=(jr5rdnpx,jr5rdnpx)
  (crsb4gf1,sye0a4ab)=(mnwxuj3a+self.cq2q4qer.width//2,chx3d43e+self.cq2q4qer.height//2)
  self.win4olr6(o9zqyahu,mnwxuj3a,chx3d43e,crsb4gf1,sye0a4ab)
  o9zqyahu.set_alpha(self.zflse45b)
  q3n2qb6g.blit(o9zqyahu,(eolaq665-jr5rdnpx,t5ivrocv-jr5rdnpx))
