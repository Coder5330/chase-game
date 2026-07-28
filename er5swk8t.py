import pygame
import pygame.gfxdraw
import random
import math
from e87f8tsx import ygspk9p3,tp0lvsnu
def w4rcb1kj(mu118qqv):
 if mu118qqv>0.75:
  return(255,255,int(200+55*(mu118qqv-0.75)/0.25))
 elif mu118qqv>0.5:
  mc8qizk3=(mu118qqv-0.5)/0.25
  return(255,int(200+55*mc8qizk3),int(80*mc8qizk3))
 elif mu118qqv>0.25:
  mc8qizk3=(mu118qqv-0.25)/0.25
  return(255,int(90+110*mc8qizk3),20)
 else:
  mc8qizk3=mu118qqv/0.25
  return(int(120+135*mc8qizk3),int(30*mc8qizk3),20)
class yur7ko64:
 def __init__(self,j1kfk7y6,f1bl08kg):
  am2vajep=random.uniform(0,2*math.pi)
  hcxhgnze=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.j1kfk7y6=j1kfk7y6
  self.f1bl08kg=f1bl08kg
  self.qjcjn997=math.cos(am2vajep)*hcxhgnze
  self.iimoe0sy=math.sin(am2vajep)*hcxhgnze
  self.life=random.randint(15,35)
  self.jr5rdnpx=self.life
  self.jyjhu8my=random.uniform(1.5,3.5)
 def update(self):
  self.j1kfk7y6+=self.qjcjn997
  self.f1bl08kg+=self.iimoe0sy
  self.qjcjn997*=0.96
  self.iimoe0sy*=0.96
  self.iimoe0sy+=0.05
  self.life-=1
 def dw7nh8rq(self,gqoagsus,i20cv3tl,clkqzfpq):
  if self.life<=0:
   return
  mu118qqv=self.life/self.jr5rdnpx
  (myrp5ge0,u9el8hl8,sv5f1bcp)=w4rcb1kj(mu118qqv)
  i4fejgxa=int(255*mu118qqv)
  fd6rupw2=max(1,int(self.jyjhu8my*(0.5+mu118qqv)))
  f80ebkjf=pygame.Surface((fd6rupw2*2+2,fd6rupw2*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(f80ebkjf,fd6rupw2+1,fd6rupw2+1,fd6rupw2,(myrp5ge0,u9el8hl8,sv5f1bcp,i4fejgxa))
  pygame.gfxdraw.aacircle(f80ebkjf,fd6rupw2+1,fd6rupw2+1,fd6rupw2,(myrp5ge0,u9el8hl8,sv5f1bcp,i4fejgxa))
  gqoagsus.blit(f80ebkjf,(self.j1kfk7y6-i20cv3tl-fd6rupw2-1,self.f1bl08kg-clkqzfpq-fd6rupw2-1),special_flags=pygame.BLEND_ADD)
class zy0ifznb:
 def __init__(self,center,do2m71hs=40):
  self.v6xii5p5=[yur7ko64(*center)for t1w1ht7p in range(do2m71hs)]
  self.center=center
  self.vmy9x8sy=1.0
  self.rk43safy=8.0
  self.kz1uu7zy=25
 def update(self):
  for no0u93mz in self.v6xii5p5:
   no0u93mz.update()
  self.v6xii5p5=[no0u93mz for no0u93mz in self.v6xii5p5 if no0u93mz.life>0]
  self.vmy9x8sy+=self.rk43safy
  self.rk43safy*=0.9
  self.kz1uu7zy-=1
 def dw7nh8rq(self,gqoagsus,i20cv3tl,clkqzfpq):
  for no0u93mz in self.v6xii5p5:
   no0u93mz.dw7nh8rq(gqoagsus,i20cv3tl,clkqzfpq)
  if self.kz1uu7zy>0:
   reqy08p0=max(0,int(200*self.kz1uu7zy/40))
   uypuplvq=max(1,int(self.kz1uu7zy/8))
   f80ebkjf=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
   pygame.draw.circle(f80ebkjf,(255,120,40,reqy08p0),(self.center[0]-i20cv3tl,self.center[1]-clkqzfpq),int(self.vmy9x8sy),uypuplvq)
   gqoagsus.blit(f80ebkjf,(0,0))
 def uc1xi04b(self):
  return not self.v6xii5p5 and self.kz1uu7zy<=0
