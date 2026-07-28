import pygame
import math
from z1yhxso7 import*
from.pxq7bzeg import f935a0l7
class vve92mpn(f935a0l7):
 def __init__(self,vhuds3qs,jslulzfy,zpfb3hn1):
  super().__init__(vhuds3qs,jslulzfy,zpfb3hn1)
  self.cnqt3wve=0
  self.do2m71hs=0
  self.n01uyzpd=0
 def ejbzutru(self,player):
  self.n01uyzpd+=0.35*(self.u15pdtz9/self.nrpj1epk if self.nrpj1epk else 1)
  n64fgwje=k1wj0tpa[self.type]
  if self.do2m71hs>0:
   self.do2m71hs-=1
   if self.do2m71hs<=0:
    self.u15pdtz9=self.nrpj1epk
   return False
  if self.cnqt3wve>0:
   self.cnqt3wve-=1
   return False
  if abs(player.wgcl9lcq.jslulzfy-self.wgcl9lcq.jslulzfy)<n64fgwje['kqbrmq']and abs(player.wgcl9lcq.zpfb3hn1-self.wgcl9lcq.zpfb3hn1)<n64fgwje['kqbrmq']:
   self.u15pdtz9=self.nrpj1epk*n64fgwje['fkmuso']
   self.do2m71hs=n64fgwje['i6ozx2']
   self.cnqt3wve=n64fgwje['w1q8f6']
  return False
 def wzlm72je(self,ukshy8nb,dzsedfqs,nd6357oo):
  jslulzfy=self.wgcl9lcq.jslulzfy-dzsedfqs
  zpfb3hn1=self.wgcl9lcq.zpfb3hn1-nd6357oo
  hfb85p86=self.wgcl9lcq.centerx-dzsedfqs
  k7zgf9q5=self.wgcl9lcq.centery-nd6357oo
  mpyxdw2z=self.wgcl9lcq.width//2
  sf337kuu=zpfb3hn1+self.wgcl9lcq.height-3
  fpa8hyex=(25,25,25)
  f55dmcxx=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(rk43safy,zpajssuu,la3kkrzd)in f55dmcxx:
   sfu38gl2=math.sin(self.n01uyzpd+la3kkrzd)
   o4dd1vn8=max(0,sfu38gl2)*4
   vmxb9yo1=(hfb85p86+rk43safy*mpyxdw2z*0.7,k7zgf9q5+zpajssuu)
   eatvzkhi=hfb85p86+rk43safy*(mpyxdw2z+9)+sfu38gl2*3
   s4rxyj38=sf337kuu-o4dd1vn8
   w5iz31yr=((vmxb9yo1[0]+eatvzkhi)/2,(vmxb9yo1[1]+s4rxyj38)/2-2)
   pygame.draw.line(ukshy8nb,fpa8hyex,vmxb9yo1,w5iz31yr,3)
   pygame.draw.line(ukshy8nb,fpa8hyex,w5iz31yr,(eatvzkhi,s4rxyj38),3)
  self.t1w1ht7p(ukshy8nb,jslulzfy,zpfb3hn1,hfb85p86,k7zgf9q5)
