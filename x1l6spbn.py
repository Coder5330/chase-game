import pygame
import pygame.gfxdraw
import random
import math
from j1bmqf7z import ygspk9p3,tp0lvsnu
def rk2u1rsu(oa47sh2s):
 if oa47sh2s>0.75:
  return(255,255,int(200+55*(oa47sh2s-0.75)/0.25))
 elif oa47sh2s>0.5:
  cx41dntc=(oa47sh2s-0.5)/0.25
  return(255,int(200+55*cx41dntc),int(80*cx41dntc))
 elif oa47sh2s>0.25:
  cx41dntc=(oa47sh2s-0.25)/0.25
  return(255,int(90+110*cx41dntc),20)
 else:
  cx41dntc=oa47sh2s/0.25
  return(int(120+135*cx41dntc),int(30*cx41dntc),20)
class yur7ko64:
 def __init__(self,x,y):
  nqimqodp=random.uniform(0,2*math.pi)
  p7b1ijiy=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.x=x
  self.y=y
  self.un9sz6rv=math.cos(nqimqodp)*p7b1ijiy
  self.cgsq7ait=math.sin(nqimqodp)*p7b1ijiy
  self.life=random.randint(15,35)
  self.lhgk5bwi=self.life
  self.size=random.uniform(1.5,3.5)
 def update(self):
  self.x+=self.un9sz6rv
  self.y+=self.cgsq7ait
  self.un9sz6rv*=0.96
  self.cgsq7ait*=0.96
  self.cgsq7ait+=0.05
  self.life-=1
 def v15cqzcu(self,p7pchcbn,vqnpcenl,iie0rnuj):
  if self.life<=0:
   return
  oa47sh2s=self.life/self.lhgk5bwi
  (qc06xq9j,kkzruin3,mal2w37d)=rk2u1rsu(oa47sh2s)
  tp2ex5t5=int(255*oa47sh2s)
  bdgbk2l0=max(1,int(self.size*(0.5+oa47sh2s)))
  mn89ltaj=pygame.Surface((bdgbk2l0*2+2,bdgbk2l0*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(mn89ltaj,bdgbk2l0+1,bdgbk2l0+1,bdgbk2l0,(qc06xq9j,kkzruin3,mal2w37d,tp2ex5t5))
  pygame.gfxdraw.aacircle(mn89ltaj,bdgbk2l0+1,bdgbk2l0+1,bdgbk2l0,(qc06xq9j,kkzruin3,mal2w37d,tp2ex5t5))
  p7pchcbn.blit(mn89ltaj,(self.x-vqnpcenl-bdgbk2l0-1,self.y-iie0rnuj-bdgbk2l0-1),special_flags=pygame.BLEND_ADD)
class zy0ifznb:
 def __init__(self,center,qtzk3ny9=40):
  self.no0u93mz=[yur7ko64(*center)for t1w1ht7p in range(qtzk3ny9)]
  self.center=center
  self.t5sn961j=1.0
  self.wtl0thhz=8.0
  self.k8qeoz0k=25
 def update(self):
  for tkyrmjlj in self.no0u93mz:
   tkyrmjlj.update()
  self.no0u93mz=[tkyrmjlj for tkyrmjlj in self.no0u93mz if tkyrmjlj.life>0]
  self.t5sn961j+=self.wtl0thhz
  self.wtl0thhz*=0.9
  self.k8qeoz0k-=1
 def v15cqzcu(self,p7pchcbn,vqnpcenl,iie0rnuj):
  for tkyrmjlj in self.no0u93mz:
   tkyrmjlj.v15cqzcu(p7pchcbn,vqnpcenl,iie0rnuj)
  if self.k8qeoz0k>0:
   i4fejgxa=max(0,int(200*self.k8qeoz0k/40))
   kr0aymk9=max(1,int(self.k8qeoz0k/8))
   mn89ltaj=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
   pygame.draw.circle(mn89ltaj,(255,120,40,i4fejgxa),(self.center[0]-vqnpcenl,self.center[1]-iie0rnuj),int(self.t5sn961j),kr0aymk9)
   p7pchcbn.blit(mn89ltaj,(0,0))
 def x875aud9(self):
  return not self.no0u93mz and self.k8qeoz0k<=0
