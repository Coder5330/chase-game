import pygame
import math
from en1x2gdg import*
from.y7iyojtp import f935a0l7
class ukxvf1t2(f935a0l7):
 def __init__(self,x875aud9,qxb7gbdg,n01uyzpd):
  super().__init__(x875aud9,qxb7gbdg,n01uyzpd)
  self.ncyh3fvl=0
 def njka34mq(self,player):
  self.ncyh3fvl+=1
  return False
 def zsw2292m(self,player,tnz61231,wc7x0h3j):
  from j7qy8yb7 import zy0ifznb
  tnz61231.append(zy0ifznb(self.f8rtm4j3.center))
  iaq7b7v1=k1wj0tpa[self.type]
  hfb85p86=math.hypot(player.f8rtm4j3.centerx-self.f8rtm4j3.centerx,player.f8rtm4j3.centery-self.f8rtm4j3.centery)
  if hfb85p86<=iaq7b7v1['hn3ksg']:
   i01nouht=self.pv4ykade*(100/(100+player.iy6qktc8))
   player.sf337kuu-=i01nouht
   player.wb7f6fdh.append((player.f8rtm4j3.centerx,player.f8rtm4j3.n01uyzpd,f'-{int(i01nouht)}',iq5c34dx['xutxzb']))
 def do2m71hs(self,gmoft6yr,kybwmlun,i0x65muf):
  ruq9e5co=self.f8rtm4j3.centerx-kybwmlun
  wzs13c9x=self.f8rtm4j3.centery-i0x65muf
  n64fgwje=(math.sin(self.ncyh3fvl*0.15)+1)/2
  zflse45b=int(self.f8rtm4j3.width*0.6+n64fgwje*6)
  u8c2jwoc=int(70+n64fgwje*90)
  xq46nouh=pygame.Surface((zflse45b*2,zflse45b*2),pygame.SRCALPHA)
  pygame.draw.circle(xq46nouh,(200,30,20,u8c2jwoc),(zflse45b,zflse45b),zflse45b)
  gmoft6yr.blit(xq46nouh,(ruq9e5co-zflse45b,wzs13c9x-zflse45b))
  qxb7gbdg=self.f8rtm4j3.qxb7gbdg-kybwmlun
  n01uyzpd=self.f8rtm4j3.n01uyzpd-i0x65muf
  self.rrcbpljd(gmoft6yr,qxb7gbdg,n01uyzpd,ruq9e5co,wzs13c9x)
  (qcd81twh,byl68ntk)=(8,12)
  q3n2qb6g=pygame.Rect(ruq9e5co-qcd81twh//2,n01uyzpd-byl68ntk+2,qcd81twh,byl68ntk)
  pygame.draw.rect(gmoft6yr,(180,30,20),q3n2qb6g,border_radius=1)
  pygame.draw.rect(gmoft6yr,(20,20,20),q3n2qb6g,width=1,border_radius=1)
  for yp3cyazb in(q3n2qb6g.top+3,q3n2qb6g.top+8):
   pygame.draw.line(gmoft6yr,(240,240,230),(q3n2qb6g.left,yp3cyazb),(q3n2qb6g.right,yp3cyazb),1)
  nfn1r4kz=(q3n2qb6g.centerx,q3n2qb6g.top)
  nubmxnsz=(q3n2qb6g.centerx+4,q3n2qb6g.top-6)
  pygame.draw.line(gmoft6yr,(90,60,30),nfn1r4kz,nubmxnsz,1)
  qertb74r=(math.sin(self.ncyh3fvl*0.4)+1)/2
  nbwye6qv=(255,int(150+qertb74r*100),40)
  pygame.draw.circle(gmoft6yr,nbwye6qv,nubmxnsz,2+int(qertb74r))
