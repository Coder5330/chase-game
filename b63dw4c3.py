import pygame
import pygame.gfxdraw
import random
import math
from z1yhxso7 import rrcbpljd,rla5ju9b
def mn7h9g1a(hcxhgnze):
 if hcxhgnze>0.75:
  return(255,255,int(200+55*(hcxhgnze-0.75)/0.25))
 elif hcxhgnze>0.5:
  qhkc856w=(hcxhgnze-0.5)/0.25
  return(255,int(200+55*qhkc856w),int(80*qhkc856w))
 elif hcxhgnze>0.25:
  qhkc856w=(hcxhgnze-0.25)/0.25
  return(255,int(90+110*qhkc856w),20)
 else:
  qhkc856w=hcxhgnze/0.25
  return(int(120+135*qhkc856w),int(30*qhkc856w),20)
class rcfnfhol:
 def __init__(self,jslulzfy,zpfb3hn1):
  sne6loh2=random.uniform(0,2*math.pi)
  u15pdtz9=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.jslulzfy=jslulzfy
  self.zpfb3hn1=zpfb3hn1
  self.tza7x73q=math.cos(sne6loh2)*u15pdtz9
  self.ucu7onz3=math.sin(sne6loh2)*u15pdtz9
  self.life=random.randint(15,35)
  self.d1b3jczu=self.life
  self.gj29yfc2=random.uniform(1.5,3.5)
 def update(self):
  self.jslulzfy+=self.tza7x73q
  self.zpfb3hn1+=self.ucu7onz3
  self.tza7x73q*=0.96
  self.ucu7onz3*=0.96
  self.ucu7onz3+=0.05
  self.life-=1
 def wzlm72je(self,mnx4sn6s,dzsedfqs,nd6357oo):
  if self.life<=0:
   return
  hcxhgnze=self.life/self.d1b3jczu
  (vt26ys44,fddfgs3j,d0r2sds8)=mn7h9g1a(hcxhgnze)
  yx4w6xlp=int(255*hcxhgnze)
  rgdej31g=max(1,int(self.gj29yfc2*(0.5+hcxhgnze)))
  xu9ymszd=pygame.Surface((rgdej31g*2+2,rgdej31g*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(xu9ymszd,rgdej31g+1,rgdej31g+1,rgdej31g,(vt26ys44,fddfgs3j,d0r2sds8,yx4w6xlp))
  pygame.gfxdraw.aacircle(xu9ymszd,rgdej31g+1,rgdej31g+1,rgdej31g,(vt26ys44,fddfgs3j,d0r2sds8,yx4w6xlp))
  mnx4sn6s.blit(xu9ymszd,(self.jslulzfy-dzsedfqs-rgdej31g-1,self.zpfb3hn1-nd6357oo-rgdej31g-1),special_flags=pygame.BLEND_ADD)
class zy0ifznb:
 def __init__(self,center,oqse3tv1=40):
  self.x6cnoljq=[rcfnfhol(*center)for v83tqll8 in range(oqse3tv1)]
  self.center=center
  self.qc06xq9j=1.0
  self.d46aexl6=8.0
  self.bdgbk2l0=25
 def update(self):
  for co4busu9 in self.x6cnoljq:
   co4busu9.update()
  self.x6cnoljq=[co4busu9 for co4busu9 in self.x6cnoljq if co4busu9.life>0]
  self.qc06xq9j+=self.d46aexl6
  self.d46aexl6*=0.9
  self.bdgbk2l0-=1
 def wzlm72je(self,mnx4sn6s,dzsedfqs,nd6357oo):
  for co4busu9 in self.x6cnoljq:
   co4busu9.wzlm72je(mnx4sn6s,dzsedfqs,nd6357oo)
  if self.bdgbk2l0>0:
   t5wi6fqj=max(0,int(200*self.bdgbk2l0/40))
   it04chsd=max(1,int(self.bdgbk2l0/8))
   xu9ymszd=pygame.Surface((rrcbpljd,rla5ju9b),pygame.SRCALPHA)
   pygame.draw.circle(xu9ymszd,(255,120,40,t5wi6fqj),(self.center[0]-dzsedfqs,self.center[1]-nd6357oo),int(self.qc06xq9j),it04chsd)
   mnx4sn6s.blit(xu9ymszd,(0,0))
 def elwf90km(self):
  return not self.x6cnoljq and self.bdgbk2l0<=0
