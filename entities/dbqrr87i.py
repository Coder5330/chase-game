import pygame
import math
from c8v341on import*
from.tdr08cw2 import f935a0l7
class khl1n13j(f935a0l7):
 def __init__(self,fo75rh8l,jh55hewl,rm0j36tc):
  super().__init__(fo75rh8l,jh55hewl,rm0j36tc)
  self.oqse3tv1=0
  self.ep6beffl=0
  self.ayr1k12v=0
 def y06nkwfg(self,player):
  self.ayr1k12v+=0.35*(self.qertb74r/self.ejwtl9tq if self.ejwtl9tq else 1)
  gj29yfc2=k1wj0tpa[self.type]
  if self.ep6beffl>0:
   self.ep6beffl-=1
   if self.ep6beffl<=0:
    self.qertb74r=self.ejwtl9tq
   return False
  if self.oqse3tv1>0:
   self.oqse3tv1-=1
   return False
  if abs(player.la3kkrzd.jh55hewl-self.la3kkrzd.jh55hewl)<gj29yfc2['txzuu8']and abs(player.la3kkrzd.rm0j36tc-self.la3kkrzd.rm0j36tc)<gj29yfc2['txzuu8']:
   self.qertb74r=self.ejwtl9tq*gj29yfc2['xu7dkn']
   self.ep6beffl=gj29yfc2['k7bpgy']
   self.oqse3tv1=gj29yfc2['umfbuv']
  return False
 def pv4ykade(self,yg87oi0e,wppsfnko,kybwmlun):
  jh55hewl=self.la3kkrzd.jh55hewl-wppsfnko
  rm0j36tc=self.la3kkrzd.rm0j36tc-kybwmlun
  cq6qdy4l=self.la3kkrzd.centerx-wppsfnko
  lztkkfzz=self.la3kkrzd.centery-kybwmlun
  u0q0mftg=self.la3kkrzd.width//2
  mqxlm5q2=rm0j36tc+self.la3kkrzd.height-3
  nvuprt77=(25,25,25)
  ftrflqbm=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(fd6rupw2,cjn2fomd,wy0mahym)in ftrflqbm:
   t54piwzn=math.sin(self.ayr1k12v+wy0mahym)
   cp91i3vm=max(0,t54piwzn)*4
   mpyxdw2z=(cq6qdy4l+fd6rupw2*u0q0mftg*0.7,lztkkfzz+cjn2fomd)
   jqzpniqf=cq6qdy4l+fd6rupw2*(u0q0mftg+9)+t54piwzn*3
   g70e3p15=mqxlm5q2-cp91i3vm
   ftlpq2wg=((mpyxdw2z[0]+jqzpniqf)/2,(mpyxdw2z[1]+g70e3p15)/2-2)
   pygame.draw.line(yg87oi0e,nvuprt77,mpyxdw2z,ftlpq2wg,3)
   pygame.draw.line(yg87oi0e,nvuprt77,ftlpq2wg,(jqzpniqf,g70e3p15),3)
  self.x37pqkoj(yg87oi0e,jh55hewl,rm0j36tc,cq6qdy4l,lztkkfzz)
