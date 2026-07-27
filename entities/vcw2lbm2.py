import pygame
import math
from en1x2gdg import*
from.y7iyojtp import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,x875aud9,qxb7gbdg,n01uyzpd):
  super().__init__(x875aud9,qxb7gbdg,n01uyzpd)
  self.ouuylaja=(0,1)
  self.f32ejx5t=False
  self.gn89qkns=0
  self.tk0qtl3q=18
 def njka34mq(self,player):
  mfyb8dal=player.f8rtm4j3.centerx-self.f8rtm4j3.centerx
  eohswq40=player.f8rtm4j3.centery-self.f8rtm4j3.centery
  cp91i3vm=math.hypot(mfyb8dal,eohswq40)or 1
  self.ouuylaja=(mfyb8dal/cp91i3vm,eohswq40/cp91i3vm)
  if self.f32ejx5t:
   self.gn89qkns-=1
   if self.gn89qkns<=0:
    self.f32ejx5t=False
    self.le9oe941(player)
   return True
  if abs(player.f8rtm4j3.qxb7gbdg-self.f8rtm4j3.qxb7gbdg)<b8cgvyie and abs(player.f8rtm4j3.n01uyzpd-self.f8rtm4j3.n01uyzpd)<b8cgvyie:
   if self.lt63j3r3>0:
    self.lt63j3r3-=1
    return True
   self.f32ejx5t=True
   self.gn89qkns=self.tk0qtl3q
   return True
  return False
 def le9oe941(self,player):
  self.lt63j3r3=self.nqimqodp
  from c4kek4ae import rpqk51fp
  cq2q4qer=uqjiujv6['n1p0vu']['mviifr']
  (mfyb8dal,eohswq40)=(player.f8rtm4j3.centerx-self.f8rtm4j3.centerx,player.f8rtm4j3.centery-self.f8rtm4j3.centery)
  sk8yqk94=rpqk51fp('n1p0vu',self.f8rtm4j3.centerx-cq2q4qer//2,self.f8rtm4j3.centery-cq2q4qer//2,cq2q4qer,cq2q4qer,mfyb8dal,eohswq40)
  sk8yqk94.oqse3tv1=self.pv4ykade
  self.ia529603.append(sk8yqk94)
 def do2m71hs(self,gmoft6yr,kybwmlun,i0x65muf):
  qxb7gbdg=self.f8rtm4j3.qxb7gbdg-kybwmlun
  n01uyzpd=self.f8rtm4j3.n01uyzpd-i0x65muf
  ruq9e5co=self.f8rtm4j3.centerx-kybwmlun
  wzs13c9x=self.f8rtm4j3.centery-i0x65muf
  self.rrcbpljd(gmoft6yr,qxb7gbdg,n01uyzpd,ruq9e5co,wzs13c9x)
  (zqcootnj,kx74d0gj)=self.ouuylaja
  (y8dd2255,njxurgow)=(-kx74d0gj,zqcootnj)
  (nrpj1epk,vvslh9bh)=(ruq9e5co+zqcootnj*14,wzs13c9x+kx74d0gj*14)
  bsp7bm41=(nrpj1epk+y8dd2255*13-zqcootnj*6,vvslh9bh+njxurgow*13-kx74d0gj*6)
  o9zqyahu=(nrpj1epk-y8dd2255*13-zqcootnj*6,vvslh9bh-njxurgow*13-kx74d0gj*6)
  fcwtg1m8=(nrpj1epk+zqcootnj*6,vvslh9bh+kx74d0gj*6)
  pygame.draw.lines(gmoft6yr,(110,70,30),False,[bsp7bm41,fcwtg1m8,o9zqyahu],3)
  qbbz2sf6=1-self.gn89qkns/self.tk0qtl3q if self.f32ejx5t else 0
  dq2fa39e=(nrpj1epk-zqcootnj*(3+qbbz2sf6*10),vvslh9bh-kx74d0gj*(3+qbbz2sf6*10))
  pygame.draw.line(gmoft6yr,(225,225,215),bsp7bm41,dq2fa39e,2)
  pygame.draw.line(gmoft6yr,(225,225,215),o9zqyahu,dq2fa39e,2)
  if self.f32ejx5t:
   diuu9k9x=(nrpj1epk+zqcootnj*8,vvslh9bh+kx74d0gj*8)
   pygame.draw.line(gmoft6yr,iq5c34dx['mabkae'],dq2fa39e,diuu9k9x,3)
