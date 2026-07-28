import pygame
import pygame.gfxdraw
import random
import math
from vnbnqbnx import ygspk9p3,tp0lvsnu
def semqgy27(kodpvjtu):
 if kodpvjtu>0.75:
  return(255,255,int(200+55*(kodpvjtu-0.75)/0.25))
 elif kodpvjtu>0.5:
  r98s4c3b=(kodpvjtu-0.5)/0.25
  return(255,int(200+55*r98s4c3b),int(80*r98s4c3b))
 elif kodpvjtu>0.25:
  r98s4c3b=(kodpvjtu-0.25)/0.25
  return(255,int(90+110*r98s4c3b),20)
 else:
  r98s4c3b=kodpvjtu/0.25
  return(int(120+135*r98s4c3b),int(30*r98s4c3b),20)
class yur7ko64:
 def __init__(self,iimoe0sy,gdg1wjui):
  am2vajep=random.uniform(0,2*math.pi)
  w0p4e05q=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.iimoe0sy=iimoe0sy
  self.gdg1wjui=gdg1wjui
  self.m81udp2f=math.cos(am2vajep)*w0p4e05q
  self.kcubods1=math.sin(am2vajep)*w0p4e05q
  self.life=random.randint(15,35)
  self.gqq4d3kz=self.life
  self.u15pdtz9=random.uniform(1.5,3.5)
 def update(self):
  self.iimoe0sy+=self.m81udp2f
  self.gdg1wjui+=self.kcubods1
  self.m81udp2f*=0.96
  self.kcubods1*=0.96
  self.kcubods1+=0.05
  self.life-=1
 def sygvwopl(self,ej16dvtj,xp8mgyn2,i20cv3tl):
  if self.life<=0:
   return
  kodpvjtu=self.life/self.gqq4d3kz
  (ytb9xxay,damdvlnk,sv5f1bcp)=semqgy27(kodpvjtu)
  i4fejgxa=int(255*kodpvjtu)
  npejzhya=max(1,int(self.u15pdtz9*(0.5+kodpvjtu)))
  k8qeoz0k=pygame.Surface((npejzhya*2+2,npejzhya*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(k8qeoz0k,npejzhya+1,npejzhya+1,npejzhya,(ytb9xxay,damdvlnk,sv5f1bcp,i4fejgxa))
  pygame.gfxdraw.aacircle(k8qeoz0k,npejzhya+1,npejzhya+1,npejzhya,(ytb9xxay,damdvlnk,sv5f1bcp,i4fejgxa))
  ej16dvtj.blit(k8qeoz0k,(self.iimoe0sy-xp8mgyn2-npejzhya-1,self.gdg1wjui-i20cv3tl-npejzhya-1),special_flags=pygame.BLEND_ADD)
class zy0ifznb:
 def __init__(self,center,pv4ykade=40):
  self.exvaj2k8=[yur7ko64(*center)for t1w1ht7p in range(pv4ykade)]
  self.center=center
  self.h4l1vznq=1.0
  self.wd6r30oj=8.0
  self.d1hm38ks=25
 def update(self):
  for f8rtm4j3 in self.exvaj2k8:
   f8rtm4j3.update()
  self.exvaj2k8=[f8rtm4j3 for f8rtm4j3 in self.exvaj2k8 if f8rtm4j3.life>0]
  self.h4l1vznq+=self.wd6r30oj
  self.wd6r30oj*=0.9
  self.d1hm38ks-=1
 def sygvwopl(self,ej16dvtj,xp8mgyn2,i20cv3tl):
  for f8rtm4j3 in self.exvaj2k8:
   f8rtm4j3.sygvwopl(ej16dvtj,xp8mgyn2,i20cv3tl)
  if self.d1hm38ks>0:
   reqy08p0=max(0,int(200*self.d1hm38ks/40))
   e1rhouu9=max(1,int(self.d1hm38ks/8))
   k8qeoz0k=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
   pygame.draw.circle(k8qeoz0k,(255,120,40,reqy08p0),(self.center[0]-xp8mgyn2,self.center[1]-i20cv3tl),int(self.h4l1vznq),e1rhouu9)
   ej16dvtj.blit(k8qeoz0k,(0,0))
 def wc7x0h3j(self):
  return not self.exvaj2k8 and self.d1hm38ks<=0
