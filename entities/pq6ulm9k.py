import pygame
import math
from en1x2gdg import*
from.y7iyojtp import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,x875aud9,qxb7gbdg,n01uyzpd):
  super().__init__(x875aud9,qxb7gbdg,n01uyzpd)
  iaq7b7v1=k1wj0tpa[x875aud9]
  self.gxlk8wru=iaq7b7v1['w9mda9']
  self.uwxrum2l=iaq7b7v1['eqkwqh']
  self.h8s2ftom=iaq7b7v1['kk2y77']
  self.rgdej31g=iaq7b7v1['w2lx2t']
  self.r2muljav=iaq7b7v1['w9mda9']
  self.stv18kgy='hidden'
  self.f80ebkjf=self.uwxrum2l
 def wkzorqqf(self):
  self.f80ebkjf-=1
  if self.f80ebkjf<=0:
   if self.stv18kgy=='hidden':
    self.stv18kgy='revealing'
    self.f80ebkjf=self.rgdej31g
   elif self.stv18kgy=='revealing':
    self.stv18kgy='visible'
    self.f80ebkjf=self.h8s2ftom
   else:
    self.stv18kgy='hidden'
    self.f80ebkjf=self.uwxrum2l
  self.r2muljav=self.gxlk8wru if self.stv18kgy=='hidden'else 255
 def y2f7atwy(self,player):
  if self.sf337kuu<=0:
   self.rk8r2ykc=True
   return
  self.wkzorqqf()
  if self.stv18kgy=='visible'and abs(player.f8rtm4j3.qxb7gbdg-self.f8rtm4j3.qxb7gbdg)<cawudtse and(abs(player.f8rtm4j3.n01uyzpd-self.f8rtm4j3.n01uyzpd)<cawudtse):
   self.sne6loh2(player)
   return
  mfyb8dal=player.f8rtm4j3.qxb7gbdg-self.f8rtm4j3.qxb7gbdg
  eohswq40=player.f8rtm4j3.n01uyzpd-self.f8rtm4j3.n01uyzpd
  k7zgf9q5=math.hypot(mfyb8dal,eohswq40)
  if k7zgf9q5==0:
   return
  wyk03o4g=mfyb8dal/k7zgf9q5
  jdqqzrlf=eohswq40/k7zgf9q5
  if wyk03o4g!=0 and jdqqzrlf!=0:
   wyk03o4g*=0.707
   jdqqzrlf*=0.707
  self.f8rtm4j3.qxb7gbdg+=wyk03o4g*self.kz1uu7zy
  self.f8rtm4j3.n01uyzpd+=jdqqzrlf*self.kz1uu7zy
  self.f8rtm4j3.qxb7gbdg=round(self.f8rtm4j3.qxb7gbdg)
  self.f8rtm4j3.n01uyzpd=round(self.f8rtm4j3.n01uyzpd)
 def do2m71hs(self,gmoft6yr,kybwmlun,i0x65muf):
  qxb7gbdg=self.f8rtm4j3.qxb7gbdg-kybwmlun
  n01uyzpd=self.f8rtm4j3.n01uyzpd-i0x65muf
  ruq9e5co=self.f8rtm4j3.centerx-kybwmlun
  wzs13c9x=self.f8rtm4j3.centery-i0x65muf
  if self.r2muljav>=255:
   self.rrcbpljd(gmoft6yr,qxb7gbdg,n01uyzpd,ruq9e5co,wzs13c9x)
   return
  je11e9ft=24
  su1hbj6t=pygame.Surface((self.f8rtm4j3.width+je11e9ft*2,self.f8rtm4j3.height+je11e9ft*2),pygame.SRCALPHA)
  (f55dmcxx,bokzixza)=(je11e9ft,je11e9ft)
  (arhnuxor,w4rcb1kj)=(f55dmcxx+self.f8rtm4j3.width//2,bokzixza+self.f8rtm4j3.height//2)
  self.rrcbpljd(su1hbj6t,f55dmcxx,bokzixza,arhnuxor,w4rcb1kj)
  su1hbj6t.set_alpha(self.r2muljav)
  gmoft6yr.blit(su1hbj6t,(qxb7gbdg-je11e9ft,n01uyzpd-je11e9ft))
