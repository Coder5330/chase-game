import pygame
import pygame.gfxdraw
import random
import math
from o100vhmy import mqp49kwv,rla5ju9b
def sf337kuu(ck7n3bfh):
 if ck7n3bfh>0.75:
  return(255,255,int(200+55*(ck7n3bfh-0.75)/0.25))
 elif ck7n3bfh>0.5:
  v15cqzcu=(ck7n3bfh-0.5)/0.25
  return(255,int(200+55*v15cqzcu),int(80*v15cqzcu))
 elif ck7n3bfh>0.25:
  v15cqzcu=(ck7n3bfh-0.25)/0.25
  return(255,int(90+110*v15cqzcu),20)
 else:
  v15cqzcu=ck7n3bfh/0.25
  return(int(120+135*v15cqzcu),int(30*v15cqzcu),20)
class qqu7eeqt:
 def __init__(self,rm0j36tc,tza7x73q):
  k44nlz15=random.uniform(0,2*math.pi)
  k8qeoz0k=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.rm0j36tc=rm0j36tc
  self.tza7x73q=tza7x73q
  self.m3hcws2w=math.cos(k44nlz15)*k8qeoz0k
  self.wyk03o4g=math.sin(k44nlz15)*k8qeoz0k
  self.life=random.randint(15,35)
  self.nyrid3dn=self.life
  self.v0rxxf36=random.uniform(1.5,3.5)
 def update(self):
  self.rm0j36tc+=self.m3hcws2w
  self.tza7x73q+=self.wyk03o4g
  self.m3hcws2w*=0.96
  self.wyk03o4g*=0.96
  self.wyk03o4g+=0.05
  self.life-=1
 def i01nouht(self,uoloeazc,kybwmlun,i0x65muf):
  if self.life<=0:
   return
  ck7n3bfh=self.life/self.nyrid3dn
  (y8dd2255,zqcootnj,on0jnwny)=sf337kuu(ck7n3bfh)
  u8c2jwoc=int(255*ck7n3bfh)
  njxurgow=max(1,int(self.v0rxxf36*(0.5+ck7n3bfh)))
  k1taa0i5=pygame.Surface((njxurgow*2+2,njxurgow*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(k1taa0i5,njxurgow+1,njxurgow+1,njxurgow,(y8dd2255,zqcootnj,on0jnwny,u8c2jwoc))
  pygame.gfxdraw.aacircle(k1taa0i5,njxurgow+1,njxurgow+1,njxurgow,(y8dd2255,zqcootnj,on0jnwny,u8c2jwoc))
  uoloeazc.blit(k1taa0i5,(self.rm0j36tc-kybwmlun-njxurgow-1,self.tza7x73q-i0x65muf-njxurgow-1),special_flags=pygame.BLEND_ADD)
class zy0ifznb:
 def __init__(self,center,clkqzfpq=40):
  self.wy0mahym=[qqu7eeqt(*center)for dtx63cfl in range(clkqzfpq)]
  self.center=center
  self.rgdej31g=1.0
  self.ljk4q5v7=8.0
  self.v6xii5p5=25
 def update(self):
  for j0kgazu4 in self.wy0mahym:
   j0kgazu4.update()
  self.wy0mahym=[j0kgazu4 for j0kgazu4 in self.wy0mahym if j0kgazu4.life>0]
  self.rgdej31g+=self.ljk4q5v7
  self.ljk4q5v7*=0.9
  self.v6xii5p5-=1
 def i01nouht(self,uoloeazc,kybwmlun,i0x65muf):
  for j0kgazu4 in self.wy0mahym:
   j0kgazu4.i01nouht(uoloeazc,kybwmlun,i0x65muf)
  if self.v6xii5p5>0:
   g7s55j2o=max(0,int(200*self.v6xii5p5/40))
   jdqqzrlf=max(1,int(self.v6xii5p5/8))
   k1taa0i5=pygame.Surface((mqp49kwv,rla5ju9b),pygame.SRCALPHA)
   pygame.draw.circle(k1taa0i5,(255,120,40,g7s55j2o),(self.center[0]-kybwmlun,self.center[1]-i0x65muf),int(self.rgdej31g),jdqqzrlf)
   uoloeazc.blit(k1taa0i5,(0,0))
 def vw6m7b5c(self):
  return not self.wy0mahym and self.v6xii5p5<=0
