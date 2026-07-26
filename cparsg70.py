import pygame
import pygame.gfxdraw
import random
import math
from rlfzkicw import azebbk7w,gokc1msy
def eatvzkhi(gj29yfc2):
 if gj29yfc2>0.75:
  return(255,255,int(200+55*(gj29yfc2-0.75)/0.25))
 elif gj29yfc2>0.5:
  uidlrye8=(gj29yfc2-0.5)/0.25
  return(255,int(200+55*uidlrye8),int(80*uidlrye8))
 elif gj29yfc2>0.25:
  uidlrye8=(gj29yfc2-0.25)/0.25
  return(255,int(90+110*uidlrye8),20)
 else:
  uidlrye8=gj29yfc2/0.25
  return(int(120+135*uidlrye8),int(30*uidlrye8),20)
class wa11dpg8:
 def __init__(self,kn5gjj8m,lu7jae58):
  g7s55j2o=random.uniform(0,2*math.pi)
  tj0nmeoq=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.kn5gjj8m=kn5gjj8m
  self.lu7jae58=lu7jae58
  self.wigbiaf9=math.cos(g7s55j2o)*tj0nmeoq
  self.yoyohaz7=math.sin(g7s55j2o)*tj0nmeoq
  self.life=random.randint(15,35)
  self.rk2u1rsu=self.life
  self.k1taa0i5=random.uniform(1.5,3.5)
 def update(self):
  self.kn5gjj8m+=self.wigbiaf9
  self.lu7jae58+=self.yoyohaz7
  self.wigbiaf9*=0.96
  self.yoyohaz7*=0.96
  self.yoyohaz7+=0.05
  self.life-=1
 def u1jhuwb6(self,kz1uu7zy,u3ifhv1x,f8wquuy5):
  if self.life<=0:
   return
  gj29yfc2=self.life/self.rk2u1rsu
  (pf0i9g5d,ouuylaja,ia529603)=eatvzkhi(gj29yfc2)
  wkzorqqf=int(255*gj29yfc2)
  wy0mahym=max(1,int(self.k1taa0i5*(0.5+gj29yfc2)))
  l3swebnv=pygame.Surface((wy0mahym*2+2,wy0mahym*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(l3swebnv,wy0mahym+1,wy0mahym+1,wy0mahym,(pf0i9g5d,ouuylaja,ia529603,wkzorqqf))
  pygame.gfxdraw.aacircle(l3swebnv,wy0mahym+1,wy0mahym+1,wy0mahym,(pf0i9g5d,ouuylaja,ia529603,wkzorqqf))
  kz1uu7zy.blit(l3swebnv,(self.kn5gjj8m-u3ifhv1x-wy0mahym-1,self.lu7jae58-f8wquuy5-wy0mahym-1),special_flags=pygame.BLEND_ADD)
class f935a0l7:
 def __init__(self,center,amcixdu1=40):
  self.lhgk5bwi=[wa11dpg8(*center)for mqp49kwv in range(amcixdu1)]
  self.center=center
  self.vyb6li07=1.0
  self.he9p3jpx=8.0
  self.la3kkrzd=25
 def update(self):
  for mnwxuj3a in self.lhgk5bwi:
   mnwxuj3a.update()
  self.lhgk5bwi=[mnwxuj3a for mnwxuj3a in self.lhgk5bwi if mnwxuj3a.life>0]
  self.vyb6li07+=self.he9p3jpx
  self.he9p3jpx*=0.9
  self.la3kkrzd-=1
 def u1jhuwb6(self,kz1uu7zy,u3ifhv1x,f8wquuy5):
  for mnwxuj3a in self.lhgk5bwi:
   mnwxuj3a.u1jhuwb6(kz1uu7zy,u3ifhv1x,f8wquuy5)
  if self.la3kkrzd>0:
   cqoldfor=max(0,int(200*self.la3kkrzd/40))
   rk36m8jv=max(1,int(self.la3kkrzd/8))
   l3swebnv=pygame.Surface((azebbk7w,gokc1msy),pygame.SRCALPHA)
   pygame.draw.circle(l3swebnv,(255,120,40,cqoldfor),(self.center[0]-u3ifhv1x,self.center[1]-f8wquuy5),int(self.vyb6li07),rk36m8jv)
   kz1uu7zy.blit(l3swebnv,(0,0))
 def f2sehe2a(self):
  return not self.lhgk5bwi and self.la3kkrzd<=0
