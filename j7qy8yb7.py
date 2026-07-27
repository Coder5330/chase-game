import pygame
import pygame.gfxdraw
import random
import math
from en1x2gdg import mqp49kwv,rla5ju9b
def x9bp4m18(n64fgwje):
 if n64fgwje>0.75:
  return(255,255,int(200+55*(n64fgwje-0.75)/0.25))
 elif n64fgwje>0.5:
  vhuds3qs=(n64fgwje-0.5)/0.25
  return(255,int(200+55*vhuds3qs),int(80*vhuds3qs))
 elif n64fgwje>0.25:
  vhuds3qs=(n64fgwje-0.25)/0.25
  return(255,int(90+110*vhuds3qs),20)
 else:
  vhuds3qs=n64fgwje/0.25
  return(int(120+135*vhuds3qs),int(30*vhuds3qs),20)
class qqu7eeqt:
 def __init__(self,qxb7gbdg,n01uyzpd):
  k44nlz15=random.uniform(0,2*math.pi)
  kz1uu7zy=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.qxb7gbdg=qxb7gbdg
  self.n01uyzpd=n01uyzpd
  self.arml29q2=math.cos(k44nlz15)*kz1uu7zy
  self.kc1fjotg=math.sin(k44nlz15)*kz1uu7zy
  self.life=random.randint(15,35)
  self.avfmh07w=self.life
  self.cq2q4qer=random.uniform(1.5,3.5)
 def update(self):
  self.qxb7gbdg+=self.arml29q2
  self.n01uyzpd+=self.kc1fjotg
  self.arml29q2*=0.96
  self.kc1fjotg*=0.96
  self.kc1fjotg+=0.05
  self.life-=1
 def do2m71hs(self,z5x8a5fb,kybwmlun,i0x65muf):
  if self.life<=0:
   return
  n64fgwje=self.life/self.avfmh07w
  (la3kkrzd,vvbc2vyh,on0jnwny)=x9bp4m18(n64fgwje)
  u8c2jwoc=int(255*n64fgwje)
  he9p3jpx=max(1,int(self.cq2q4qer*(0.5+n64fgwje)))
  yg87oi0e=pygame.Surface((he9p3jpx*2+2,he9p3jpx*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(yg87oi0e,he9p3jpx+1,he9p3jpx+1,he9p3jpx,(la3kkrzd,vvbc2vyh,on0jnwny,u8c2jwoc))
  pygame.gfxdraw.aacircle(yg87oi0e,he9p3jpx+1,he9p3jpx+1,he9p3jpx,(la3kkrzd,vvbc2vyh,on0jnwny,u8c2jwoc))
  z5x8a5fb.blit(yg87oi0e,(self.qxb7gbdg-kybwmlun-he9p3jpx-1,self.n01uyzpd-i0x65muf-he9p3jpx-1),special_flags=pygame.BLEND_ADD)
class zy0ifznb:
 def __init__(self,center,x5m9j98c=40):
  self.mmn32u1i=[qqu7eeqt(*center)for dtx63cfl in range(x5m9j98c)]
  self.center=center
  self.cqheyto5=1.0
  self.wgcl9lcq=8.0
  self.eehou6ql=25
 def update(self):
  for pf0i9g5d in self.mmn32u1i:
   pf0i9g5d.update()
  self.mmn32u1i=[pf0i9g5d for pf0i9g5d in self.mmn32u1i if pf0i9g5d.life>0]
  self.cqheyto5+=self.wgcl9lcq
  self.wgcl9lcq*=0.9
  self.eehou6ql-=1
 def do2m71hs(self,z5x8a5fb,kybwmlun,i0x65muf):
  for pf0i9g5d in self.mmn32u1i:
   pf0i9g5d.do2m71hs(z5x8a5fb,kybwmlun,i0x65muf)
  if self.eehou6ql>0:
   g7s55j2o=max(0,int(200*self.eehou6ql/40))
   i33e1i1p=max(1,int(self.eehou6ql/8))
   yg87oi0e=pygame.Surface((mqp49kwv,rla5ju9b),pygame.SRCALPHA)
   pygame.draw.circle(yg87oi0e,(255,120,40,g7s55j2o),(self.center[0]-kybwmlun,self.center[1]-i0x65muf),int(self.cqheyto5),i33e1i1p)
   z5x8a5fb.blit(yg87oi0e,(0,0))
 def rk8r2ykc(self):
  return not self.mmn32u1i and self.eehou6ql<=0
