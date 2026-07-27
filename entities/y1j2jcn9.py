import pygame
import math
from en1x2gdg import*
from.y7iyojtp import f935a0l7
class khl1n13j(f935a0l7):
 def __init__(self,x875aud9,qxb7gbdg,n01uyzpd):
  super().__init__(x875aud9,qxb7gbdg,n01uyzpd)
  self.iektsg7f=0
  self.vw6m7b5c=0
  self.j7f00ter=0
 def njka34mq(self,player):
  self.j7f00ter+=0.35*(self.kz1uu7zy/self.tp2ex5t5 if self.tp2ex5t5 else 1)
  iaq7b7v1=k1wj0tpa[self.type]
  if self.vw6m7b5c>0:
   self.vw6m7b5c-=1
   if self.vw6m7b5c<=0:
    self.kz1uu7zy=self.tp2ex5t5
   return False
  if self.iektsg7f>0:
   self.iektsg7f-=1
   return False
  if abs(player.f8rtm4j3.qxb7gbdg-self.f8rtm4j3.qxb7gbdg)<iaq7b7v1['k7rrbe']and abs(player.f8rtm4j3.n01uyzpd-self.f8rtm4j3.n01uyzpd)<iaq7b7v1['k7rrbe']:
   self.kz1uu7zy=self.tp2ex5t5*iaq7b7v1['ew6tm2']
   self.vw6m7b5c=iaq7b7v1['kou83g']
   self.iektsg7f=iaq7b7v1['clslay']
  return False
 def do2m71hs(self,gmoft6yr,kybwmlun,i0x65muf):
  qxb7gbdg=self.f8rtm4j3.qxb7gbdg-kybwmlun
  n01uyzpd=self.f8rtm4j3.n01uyzpd-i0x65muf
  ruq9e5co=self.f8rtm4j3.centerx-kybwmlun
  wzs13c9x=self.f8rtm4j3.centery-i0x65muf
  tw76xato=self.f8rtm4j3.width//2
  s4rxyj38=n01uyzpd+self.f8rtm4j3.height-3
  i13n3bzt=(25,25,25)
  nd31k9qm=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(pllkstn3,m20u9isy,got7txkd)in nd31k9qm:
   y9ayq6ww=math.sin(self.j7f00ter+got7txkd)
   swwnc21o=max(0,y9ayq6ww)*4
   damdvlnk=(ruq9e5co+pllkstn3*tw76xato*0.7,wzs13c9x+m20u9isy)
   boih5csk=ruq9e5co+pllkstn3*(tw76xato+9)+y9ayq6ww*3
   xuu13i59=s4rxyj38-swwnc21o
   sdeekgys=((damdvlnk[0]+boih5csk)/2,(damdvlnk[1]+xuu13i59)/2-2)
   pygame.draw.line(gmoft6yr,i13n3bzt,damdvlnk,sdeekgys,3)
   pygame.draw.line(gmoft6yr,i13n3bzt,sdeekgys,(boih5csk,xuu13i59),3)
  self.rrcbpljd(gmoft6yr,qxb7gbdg,n01uyzpd,ruq9e5co,wzs13c9x)
