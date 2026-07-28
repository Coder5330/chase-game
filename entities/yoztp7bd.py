import pygame
import math
from r1yohmi9 import*
from.xqup06id import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,jqzpniqf,un9sz6rv,ehet25lz):
  super().__init__(jqzpniqf,un9sz6rv,ehet25lz)
  self.yrivh6t1=(0,1)
  self.i20cv3tl=False
  self.xp8mgyn2=0
  self.jm25len6=18
 def zgomf9pm(self,player):
  mygfliji=player.nxxjve3d.centerx-self.nxxjve3d.centerx
  yjluujmi=player.nxxjve3d.centery-self.nxxjve3d.centery
  ry181acj=math.hypot(mygfliji,yjluujmi)or 1
  self.yrivh6t1=(mygfliji/ry181acj,yjluujmi/ry181acj)
  if self.i20cv3tl:
   self.xp8mgyn2-=1
   if self.xp8mgyn2<=0:
    self.i20cv3tl=False
    self.u0q0mftg(player)
   return True
  if abs(player.nxxjve3d.un9sz6rv-self.nxxjve3d.un9sz6rv)<b8cgvyie and abs(player.nxxjve3d.ehet25lz-self.nxxjve3d.ehet25lz)<b8cgvyie:
   if self.b06xkxb9>0:
    self.b06xkxb9-=1
    return True
   self.i20cv3tl=True
   self.xp8mgyn2=self.jm25len6
   return True
  return False
 def u0q0mftg(self,player):
  self.b06xkxb9=self.mal2w37d
  from cw2maiet import rpqk51fp
  y9ayq6ww=uqjiujv6['k4fbl9']['yc1nlc']
  (mygfliji,yjluujmi)=(player.nxxjve3d.centerx-self.nxxjve3d.centerx,player.nxxjve3d.centery-self.nxxjve3d.centery)
  lcj883dh=rpqk51fp('k4fbl9',self.nxxjve3d.centerx-y9ayq6ww//2,self.nxxjve3d.centery-y9ayq6ww//2,y9ayq6ww,y9ayq6ww,mygfliji,yjluujmi)
  lcj883dh.qbbz2sf6=self.wc7x0h3j
  self.ytv3i12v.append(lcj883dh)
 def fo75rh8l(self,vmy9x8sy,d1ieixwc,pvasifpw):
  un9sz6rv=self.nxxjve3d.un9sz6rv-d1ieixwc
  ehet25lz=self.nxxjve3d.ehet25lz-pvasifpw
  cnqt3wve=self.nxxjve3d.centerx-d1ieixwc
  do2m71hs=self.nxxjve3d.centery-pvasifpw
  self.nd96qe3r(vmy9x8sy,un9sz6rv,ehet25lz,cnqt3wve,do2m71hs)
  (q7i6yuj7,v76ub7l8)=self.yrivh6t1
  (g1g1r1dw,upprat08)=(-v76ub7l8,q7i6yuj7)
  (wppsfnko,kybwmlun)=(cnqt3wve+q7i6yuj7*14,do2m71hs+v76ub7l8*14)
  kc1fjotg=(wppsfnko+g1g1r1dw*13-q7i6yuj7*6,kybwmlun+upprat08*13-v76ub7l8*6)
  i33e1i1p=(wppsfnko-g1g1r1dw*13-q7i6yuj7*6,kybwmlun-upprat08*13-v76ub7l8*6)
  qbm1enf3=(wppsfnko+q7i6yuj7*6,kybwmlun+v76ub7l8*6)
  pygame.draw.lines(vmy9x8sy,(110,70,30),False,[kc1fjotg,qbm1enf3,i33e1i1p],3)
  uc1xi04b=1-self.xp8mgyn2/self.jm25len6 if self.i20cv3tl else 0
  mmn32u1i=(wppsfnko-q7i6yuj7*(3+uc1xi04b*10),kybwmlun-v76ub7l8*(3+uc1xi04b*10))
  pygame.draw.line(vmy9x8sy,(225,225,215),kc1fjotg,mmn32u1i,2)
  pygame.draw.line(vmy9x8sy,(225,225,215),i33e1i1p,mmn32u1i,2)
  if self.i20cv3tl:
   uva2ieuc=(wppsfnko+q7i6yuj7*8,kybwmlun+v76ub7l8*8)
   pygame.draw.line(vmy9x8sy,iq5c34dx['e2dg1w'],mmn32u1i,uva2ieuc,3)
