import pygame
import pygame.gfxdraw
import random
import math
from ygm55ff1 import qxaprpn6,ibps3y70
def nfn1r4kz(k8qeoz0k):
 if k8qeoz0k>0.75:
  return(255,255,int(200+55*(k8qeoz0k-0.75)/0.25))
 elif k8qeoz0k>0.5:
  eohswq40=(k8qeoz0k-0.5)/0.25
  return(255,int(200+55*eohswq40),int(80*eohswq40))
 elif k8qeoz0k>0.25:
  eohswq40=(k8qeoz0k-0.25)/0.25
  return(255,int(90+110*eohswq40),20)
 else:
  eohswq40=k8qeoz0k/0.25
  return(int(120+135*eohswq40),int(30*eohswq40),20)
class rqf5q14j:
 def __init__(self,yypp5zp7,tjy1o2rn):
  x37pqkoj=random.uniform(0,2*math.pi)
  qc06xq9j=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.yypp5zp7=yypp5zp7
  self.tjy1o2rn=tjy1o2rn
  self.l1rdxck3=math.cos(x37pqkoj)*qc06xq9j
  self.rh0w064w=math.sin(x37pqkoj)*qc06xq9j
  self.life=random.randint(15,35)
  self.ftrflqbm=self.life
  self.g1g1r1dw=random.uniform(1.5,3.5)
 def update(self):
  self.yypp5zp7+=self.l1rdxck3
  self.tjy1o2rn+=self.rh0w064w
  self.l1rdxck3*=0.96
  self.rh0w064w*=0.96
  self.rh0w064w+=0.05
  self.life-=1
 def izhwy9he(self,qertb74r,ra73jgzl,kmgfxc08):
  if self.life<=0:
   return
  k8qeoz0k=self.life/self.ftrflqbm
  (jl90pxrl,sygvwopl,eqrl1n75)=nfn1r4kz(k8qeoz0k)
  dtx63cfl=int(255*k8qeoz0k)
  w8y72ivg=max(1,int(self.g1g1r1dw*(0.5+k8qeoz0k)))
  l3swebnv=pygame.Surface((w8y72ivg*2+2,w8y72ivg*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(l3swebnv,w8y72ivg+1,w8y72ivg+1,w8y72ivg,(jl90pxrl,sygvwopl,eqrl1n75,dtx63cfl))
  pygame.gfxdraw.aacircle(l3swebnv,w8y72ivg+1,w8y72ivg+1,w8y72ivg,(jl90pxrl,sygvwopl,eqrl1n75,dtx63cfl))
  qertb74r.blit(l3swebnv,(self.yypp5zp7-ra73jgzl-w8y72ivg-1,self.tjy1o2rn-kmgfxc08-w8y72ivg-1),special_flags=pygame.BLEND_ADD)
class pi3qk2ia:
 def __init__(self,center,qbm1enf3=40):
  self.vk3g84ut=[rqf5q14j(*center)for gdzr1yxr in range(qbm1enf3)]
  self.center=center
  self.x6cnoljq=1.0
  self.y8dd2255=8.0
  self.a2wspofv=25
 def update(self):
  for mcup8ijl in self.vk3g84ut:
   mcup8ijl.update()
  self.vk3g84ut=[mcup8ijl for mcup8ijl in self.vk3g84ut if mcup8ijl.life>0]
  self.x6cnoljq+=self.y8dd2255
  self.y8dd2255*=0.9
  self.a2wspofv-=1
 def izhwy9he(self,qertb74r,ra73jgzl,kmgfxc08):
  for mcup8ijl in self.vk3g84ut:
   mcup8ijl.izhwy9he(qertb74r,ra73jgzl,kmgfxc08)
  if self.a2wspofv>0:
   pecruyf3=max(0,int(200*self.a2wspofv/40))
   su1hbj6t=max(1,int(self.a2wspofv/8))
   l3swebnv=pygame.Surface((qxaprpn6,ibps3y70),pygame.SRCALPHA)
   pygame.draw.circle(l3swebnv,(255,120,40,pecruyf3),(self.center[0]-ra73jgzl,self.center[1]-kmgfxc08),int(self.x6cnoljq),su1hbj6t)
   qertb74r.blit(l3swebnv,(0,0))
 def ebt3g2qz(self):
  return not self.vk3g84ut and self.a2wspofv<=0
