import pygame
import math
from v7bnhjw6 import*
from.e1gnfiue import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,gubmc97c,qic1l7dy,vsjchzjq):
  super().__init__(gubmc97c,qic1l7dy,vsjchzjq)
  self.zqcootnj=(0,1)
  self.bllo3rbx=False
  self.ugez7bh2=0
  self.ebt3g2qz=18
 def gsrtwlxd(self,player):
  x875aud9=player.jenvg3kk.centerx-self.jenvg3kk.centerx
  jqxs6esj=player.jenvg3kk.centery-self.jenvg3kk.centery
  avfmh07w=math.hypot(x875aud9,jqxs6esj)or 1
  self.zqcootnj=(x875aud9/avfmh07w,jqxs6esj/avfmh07w)
  if self.bllo3rbx:
   self.ugez7bh2-=1
   if self.ugez7bh2<=0:
    self.bllo3rbx=False
    self.mqxlm5q2(player)
   return True
  if abs(player.jenvg3kk.qic1l7dy-self.jenvg3kk.qic1l7dy)<b8cgvyie and abs(player.jenvg3kk.vsjchzjq-self.jenvg3kk.vsjchzjq)<b8cgvyie:
   if self.i4fejgxa>0:
    self.i4fejgxa-=1
    return True
   self.bllo3rbx=True
   self.ugez7bh2=self.ebt3g2qz
   return True
  return False
 def mqxlm5q2(self,player):
  self.i4fejgxa=self.g11kerpe
  from xu7bfxq7 import rpqk51fp
  t54piwzn=uqjiujv6['wdl5tg']['mrf5a7']
  (x875aud9,jqxs6esj)=(player.jenvg3kk.centerx-self.jenvg3kk.centerx,player.jenvg3kk.centery-self.jenvg3kk.centery)
  reqy08p0=rpqk51fp('wdl5tg',self.jenvg3kk.centerx-t54piwzn//2,self.jenvg3kk.centery-t54piwzn//2,t54piwzn,t54piwzn,x875aud9,jqxs6esj)
  reqy08p0.i01nouht=self.g8kk791z
  self.gp84dyt9.append(reqy08p0)
 def wc7x0h3j(self,gg7oq2zd,li9nb74x,zfb7r31q):
  qic1l7dy=self.jenvg3kk.qic1l7dy-li9nb74x
  vsjchzjq=self.jenvg3kk.vsjchzjq-zfb7r31q
  pa8s8hmb=self.jenvg3kk.centerx-li9nb74x
  pv4ykade=self.jenvg3kk.centery-zfb7r31q
  self.wrbw2zla(gg7oq2zd,qic1l7dy,vsjchzjq,pa8s8hmb,pv4ykade)
  (fddfgs3j,mc8qizk3)=self.zqcootnj
  (rgdej31g,v6xii5p5)=(-mc8qizk3,fddfgs3j)
  (jc54wsqt,z0b6ugvs)=(pa8s8hmb+fddfgs3j*14,pv4ykade+mc8qizk3*14)
  ayr1k12v=(jc54wsqt+rgdej31g*13-fddfgs3j*6,z0b6ugvs+v6xii5p5*13-mc8qizk3*6)
  zanouof0=(jc54wsqt-rgdej31g*13-fddfgs3j*6,z0b6ugvs-v6xii5p5*13-mc8qizk3*6)
  u23y30ys=(jc54wsqt+fddfgs3j*6,z0b6ugvs+mc8qizk3*6)
  pygame.draw.lines(gg7oq2zd,(110,70,30),False,[ayr1k12v,u23y30ys,zanouof0],3)
  rzewviyt=1-self.ugez7bh2/self.ebt3g2qz if self.bllo3rbx else 0
  w8y72ivg=(jc54wsqt-fddfgs3j*(3+rzewviyt*10),z0b6ugvs-mc8qizk3*(3+rzewviyt*10))
  pygame.draw.line(gg7oq2zd,(225,225,215),ayr1k12v,w8y72ivg,2)
  pygame.draw.line(gg7oq2zd,(225,225,215),zanouof0,w8y72ivg,2)
  if self.bllo3rbx:
   e5x4w7ky=(jc54wsqt+fddfgs3j*8,z0b6ugvs+mc8qizk3*8)
   pygame.draw.line(gg7oq2zd,iq5c34dx['jmofmm'],w8y72ivg,e5x4w7ky,3)
