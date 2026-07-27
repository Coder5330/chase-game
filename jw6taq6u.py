import pygame
import pygame.gfxdraw
import random
import math
from c8v341on import jdiuovw1,rla5ju9b
def v76ub7l8(cb2uuijn):
 if cb2uuijn>0.75:
  return(255,255,int(200+55*(cb2uuijn-0.75)/0.25))
 elif cb2uuijn>0.5:
  tnz61231=(cb2uuijn-0.5)/0.25
  return(255,int(200+55*tnz61231),int(80*tnz61231))
 elif cb2uuijn>0.25:
  tnz61231=(cb2uuijn-0.25)/0.25
  return(255,int(90+110*tnz61231),20)
 else:
  tnz61231=cb2uuijn/0.25
  return(int(120+135*tnz61231),int(30*tnz61231),20)
class qqu7eeqt:
 def __init__(self,jh55hewl,rm0j36tc):
  u8c2jwoc=random.uniform(0,2*math.pi)
  qertb74r=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.jh55hewl=jh55hewl
  self.rm0j36tc=rm0j36tc
  self.vm65q57t=math.cos(u8c2jwoc)*qertb74r
  self.e8zgvwwu=math.sin(u8c2jwoc)*qertb74r
  self.life=random.randint(15,35)
  self.f55dmcxx=self.life
  self.tby49e7e=random.uniform(1.5,3.5)
 def update(self):
  self.jh55hewl+=self.vm65q57t
  self.rm0j36tc+=self.e8zgvwwu
  self.vm65q57t*=0.96
  self.e8zgvwwu*=0.96
  self.e8zgvwwu+=0.05
  self.life-=1
 def pv4ykade(self,u15pdtz9,wppsfnko,kybwmlun):
  if self.life<=0:
   return
  cb2uuijn=self.life/self.f55dmcxx
  (ncyh3fvl,nfn1r4kz,v982n2at)=v76ub7l8(cb2uuijn)
  sld4d6af=int(255*cb2uuijn)
  x6cnoljq=max(1,int(self.tby49e7e*(0.5+cb2uuijn)))
  wgcl9lcq=pygame.Surface((x6cnoljq*2+2,x6cnoljq*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(wgcl9lcq,x6cnoljq+1,x6cnoljq+1,x6cnoljq,(ncyh3fvl,nfn1r4kz,v982n2at,sld4d6af))
  pygame.gfxdraw.aacircle(wgcl9lcq,x6cnoljq+1,x6cnoljq+1,x6cnoljq,(ncyh3fvl,nfn1r4kz,v982n2at,sld4d6af))
  u15pdtz9.blit(wgcl9lcq,(self.jh55hewl-wppsfnko-x6cnoljq-1,self.rm0j36tc-kybwmlun-x6cnoljq-1),special_flags=pygame.BLEND_ADD)
class zy0ifznb:
 def __init__(self,center,i20cv3tl=40):
  self.j0kgazu4=[qqu7eeqt(*center)for ocij2v2h in range(i20cv3tl)]
  self.center=center
  self.z3olfark=1.0
  self.vt26ys44=8.0
  self.no0u93mz=25
 def update(self):
  for d448n7od in self.j0kgazu4:
   d448n7od.update()
  self.j0kgazu4=[d448n7od for d448n7od in self.j0kgazu4 if d448n7od.life>0]
  self.z3olfark+=self.vt26ys44
  self.vt26ys44*=0.9
  self.no0u93mz-=1
 def pv4ykade(self,u15pdtz9,wppsfnko,kybwmlun):
  for d448n7od in self.j0kgazu4:
   d448n7od.pv4ykade(u15pdtz9,wppsfnko,kybwmlun)
  if self.no0u93mz>0:
   wkzorqqf=max(0,int(200*self.no0u93mz/40))
   qxt6ridl=max(1,int(self.no0u93mz/8))
   wgcl9lcq=pygame.Surface((jdiuovw1,rla5ju9b),pygame.SRCALPHA)
   pygame.draw.circle(wgcl9lcq,(255,120,40,wkzorqqf),(self.center[0]-wppsfnko,self.center[1]-kybwmlun),int(self.z3olfark),qxt6ridl)
   u15pdtz9.blit(wgcl9lcq,(0,0))
 def iektsg7f(self):
  return not self.j0kgazu4 and self.no0u93mz<=0
