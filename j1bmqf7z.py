import pygame
import pygame.gfxdraw
import random
import math
from ykatqyds import cqoldfor,tp0lvsnu
def i13n3bzt(kc7rm6j8):
 if kc7rm6j8>0.75:
  return(255,255,int(200+55*(kc7rm6j8-0.75)/0.25))
 elif kc7rm6j8>0.5:
  azc4xl99=(kc7rm6j8-0.5)/0.25
  return(255,int(200+55*azc4xl99),int(80*azc4xl99))
 elif kc7rm6j8>0.25:
  azc4xl99=(kc7rm6j8-0.25)/0.25
  return(255,int(90+110*azc4xl99),20)
 else:
  azc4xl99=kc7rm6j8/0.25
  return(int(120+135*azc4xl99),int(30*azc4xl99),20)
class yur7ko64:
 def __init__(self,owdz09wf,lb4y4k7b):
  d0r2sds8=random.uniform(0,2*math.pi)
  bf7so8w5=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.owdz09wf=owdz09wf
  self.lb4y4k7b=lb4y4k7b
  self.q6p61xuf=math.cos(d0r2sds8)*bf7so8w5
  self.cu8el501=math.sin(d0r2sds8)*bf7so8w5
  self.life=random.randint(15,35)
  self.r2muljav=self.life
  self.w0p4e05q=random.uniform(1.5,3.5)
 def update(self):
  self.owdz09wf+=self.q6p61xuf
  self.lb4y4k7b+=self.cu8el501
  self.q6p61xuf*=0.96
  self.cu8el501*=0.96
  self.cu8el501+=0.05
  self.life-=1
 def v15cqzcu(self,arjn2hz2,clkqzfpq,x5m9j98c):
  if self.life<=0:
   return
  kc7rm6j8=self.life/self.r2muljav
  (tby49e7e,mn7h9g1a,nrpj1epk)=i13n3bzt(kc7rm6j8)
  am2vajep=int(255*kc7rm6j8)
  npcxa5s0=max(1,int(self.w0p4e05q*(0.5+kc7rm6j8)))
  h8s2ftom=pygame.Surface((npcxa5s0*2+2,npcxa5s0*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(h8s2ftom,npcxa5s0+1,npcxa5s0+1,npcxa5s0,(tby49e7e,mn7h9g1a,nrpj1epk,am2vajep))
  pygame.gfxdraw.aacircle(h8s2ftom,npcxa5s0+1,npcxa5s0+1,npcxa5s0,(tby49e7e,mn7h9g1a,nrpj1epk,am2vajep))
  arjn2hz2.blit(h8s2ftom,(self.owdz09wf-clkqzfpq-npcxa5s0-1,self.lb4y4k7b-x5m9j98c-npcxa5s0-1),special_flags=pygame.BLEND_ADD)
class zy0ifznb:
 def __init__(self,center,elwf90km=40):
  self.cqheyto5=[yur7ko64(*center)for wrbw2zla in range(elwf90km)]
  self.center=center
  self.gj29yfc2=1.0
  self.xxns2zyb=8.0
  self.g1b3d505=25
 def update(self):
  for rgdej31g in self.cqheyto5:
   rgdej31g.update()
  self.cqheyto5=[rgdej31g for rgdej31g in self.cqheyto5 if rgdej31g.life>0]
  self.gj29yfc2+=self.xxns2zyb
  self.xxns2zyb*=0.9
  self.g1b3d505-=1
 def v15cqzcu(self,arjn2hz2,clkqzfpq,x5m9j98c):
  for rgdej31g in self.cqheyto5:
   rgdej31g.v15cqzcu(arjn2hz2,clkqzfpq,x5m9j98c)
  if self.g1b3d505>0:
   e5x4w7ky=max(0,int(200*self.g1b3d505/40))
   n8k03w0f=max(1,int(self.g1b3d505/8))
   h8s2ftom=pygame.Surface((cqoldfor,tp0lvsnu),pygame.SRCALPHA)
   pygame.draw.circle(h8s2ftom,(255,120,40,e5x4w7ky),(self.center[0]-clkqzfpq,self.center[1]-x5m9j98c),int(self.gj29yfc2),n8k03w0f)
   arjn2hz2.blit(h8s2ftom,(0,0))
 def x875aud9(self):
  return not self.cqheyto5 and self.g1b3d505<=0
