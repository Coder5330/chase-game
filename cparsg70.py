import pygame
import pygame.gfxdraw
import random
import math
from rlfzkicw import azebbk7w,gokc1msy
def eatvzkhi(g1b3d505):
 if g1b3d505>0.75:
  return(255,255,int(200+55*(g1b3d505-0.75)/0.25))
 elif g1b3d505>0.5:
  uidlrye8=(g1b3d505-0.5)/0.25
  return(255,int(200+55*uidlrye8),int(80*uidlrye8))
 elif g1b3d505>0.25:
  uidlrye8=(g1b3d505-0.25)/0.25
  return(255,int(90+110*uidlrye8),20)
 else:
  uidlrye8=g1b3d505/0.25
  return(int(120+135*uidlrye8),int(30*uidlrye8),20)
class wa11dpg8:
 def __init__(self,kn5gjj8m,lu7jae58):
  g7s55j2o=random.uniform(0,2*math.pi)
  fd6rupw2=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.kn5gjj8m=kn5gjj8m
  self.lu7jae58=lu7jae58
  self.wigbiaf9=math.cos(g7s55j2o)*fd6rupw2
  self.yoyohaz7=math.sin(g7s55j2o)*fd6rupw2
  self.life=random.randint(15,35)
  self.nd31k9qm=self.life
  self.xsspye9r=random.uniform(1.5,3.5)
 def update(self):
  self.kn5gjj8m+=self.wigbiaf9
  self.lu7jae58+=self.yoyohaz7
  self.wigbiaf9*=0.96
  self.yoyohaz7*=0.96
  self.yoyohaz7+=0.05
  self.life-=1
 def u1jhuwb6(self,rk43safy,u3ifhv1x,f8wquuy5):
  if self.life<=0:
   return
  g1b3d505=self.life/self.nd31k9qm
  (zdan085r,ouuylaja,ia529603)=eatvzkhi(g1b3d505)
  wkzorqqf=int(255*g1b3d505)
  mmn32u1i=max(1,int(self.xsspye9r*(0.5+g1b3d505)))
  cknfu84x=pygame.Surface((mmn32u1i*2+2,mmn32u1i*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(cknfu84x,mmn32u1i+1,mmn32u1i+1,mmn32u1i,(zdan085r,ouuylaja,ia529603,wkzorqqf))
  pygame.gfxdraw.aacircle(cknfu84x,mmn32u1i+1,mmn32u1i+1,mmn32u1i,(zdan085r,ouuylaja,ia529603,wkzorqqf))
  rk43safy.blit(cknfu84x,(self.kn5gjj8m-u3ifhv1x-mmn32u1i-1,self.lu7jae58-f8wquuy5-mmn32u1i-1),special_flags=pygame.BLEND_ADD)
class f935a0l7:
 def __init__(self,center,amcixdu1=40):
  self.zsw2292m=[wa11dpg8(*center)for mqp49kwv in range(amcixdu1)]
  self.center=center
  self.la3kkrzd=1.0
  self.gp6orsnc=8.0
  self.he9p3jpx=25
 def update(self):
  for ob7p0rnp in self.zsw2292m:
   ob7p0rnp.update()
  self.zsw2292m=[ob7p0rnp for ob7p0rnp in self.zsw2292m if ob7p0rnp.life>0]
  self.la3kkrzd+=self.gp6orsnc
  self.gp6orsnc*=0.9
  self.he9p3jpx-=1
 def u1jhuwb6(self,rk43safy,u3ifhv1x,f8wquuy5):
  for ob7p0rnp in self.zsw2292m:
   ob7p0rnp.u1jhuwb6(rk43safy,u3ifhv1x,f8wquuy5)
  if self.he9p3jpx>0:
   cqoldfor=max(0,int(200*self.he9p3jpx/40))
   rk36m8jv=max(1,int(self.he9p3jpx/8))
   cknfu84x=pygame.Surface((azebbk7w,gokc1msy),pygame.SRCALPHA)
   pygame.draw.circle(cknfu84x,(255,120,40,cqoldfor),(self.center[0]-u3ifhv1x,self.center[1]-f8wquuy5),int(self.la3kkrzd),rk36m8jv)
   rk43safy.blit(cknfu84x,(0,0))
 def f2sehe2a(self):
  return not self.zsw2292m and self.he9p3jpx<=0
