import pygame
import pygame.gfxdraw
import random
import math
from v7bnhjw6 import v4u89yjb,rla5ju9b
def nyfkjfpn(xxkdq95g):
 if xxkdq95g>0.75:
  return(255,255,int(200+55*(xxkdq95g-0.75)/0.25))
 elif xxkdq95g>0.5:
  nfn1r4kz=(xxkdq95g-0.5)/0.25
  return(255,int(200+55*nfn1r4kz),int(80*nfn1r4kz))
 elif xxkdq95g>0.25:
  nfn1r4kz=(xxkdq95g-0.25)/0.25
  return(255,int(90+110*nfn1r4kz),20)
 else:
  nfn1r4kz=xxkdq95g/0.25
  return(int(120+135*nfn1r4kz),int(30*nfn1r4kz),20)
class oohp6vz4:
 def __init__(self,qic1l7dy,vsjchzjq):
  lt63j3r3=random.uniform(0,2*math.pi)
  xvzc7d2k=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.qic1l7dy=qic1l7dy
  self.vsjchzjq=vsjchzjq
  self.n01uyzpd=math.cos(lt63j3r3)*xvzc7d2k
  self.zgomf9pm=math.sin(lt63j3r3)*xvzc7d2k
  self.life=random.randint(15,35)
  self.nii6l3ue=self.life
  self.t54piwzn=random.uniform(1.5,3.5)
 def update(self):
  self.qic1l7dy+=self.n01uyzpd
  self.vsjchzjq+=self.zgomf9pm
  self.n01uyzpd*=0.96
  self.zgomf9pm*=0.96
  self.zgomf9pm+=0.05
  self.life-=1
 def wc7x0h3j(self,nabufwbu,li9nb74x,zfb7r31q):
  if self.life<=0:
   return
  xxkdq95g=self.life/self.nii6l3ue
  (cqheyto5,cx41dntc,b06xkxb9)=nyfkjfpn(xxkdq95g)
  sne6loh2=int(255*xxkdq95g)
  eehou6ql=max(1,int(self.t54piwzn*(0.5+xxkdq95g)))
  cq2q4qer=pygame.Surface((eehou6ql*2+2,eehou6ql*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(cq2q4qer,eehou6ql+1,eehou6ql+1,eehou6ql,(cqheyto5,cx41dntc,b06xkxb9,sne6loh2))
  pygame.gfxdraw.aacircle(cq2q4qer,eehou6ql+1,eehou6ql+1,eehou6ql,(cqheyto5,cx41dntc,b06xkxb9,sne6loh2))
  nabufwbu.blit(cq2q4qer,(self.qic1l7dy-li9nb74x-eehou6ql-1,self.vsjchzjq-zfb7r31q-eehou6ql-1),special_flags=pygame.BLEND_ADD)
class zy0ifznb:
 def __init__(self,center,wi8skch8=40):
  self.vyb6li07=[oohp6vz4(*center)for m53a5qbs in range(wi8skch8)]
  self.center=center
  self.myrp5ge0=1.0
  self.tby49e7e=8.0
  self.fd6rupw2=25
 def update(self):
  for a2wspofv in self.vyb6li07:
   a2wspofv.update()
  self.vyb6li07=[a2wspofv for a2wspofv in self.vyb6li07 if a2wspofv.life>0]
  self.myrp5ge0+=self.tby49e7e
  self.tby49e7e*=0.9
  self.fd6rupw2-=1
 def wc7x0h3j(self,nabufwbu,li9nb74x,zfb7r31q):
  for a2wspofv in self.vyb6li07:
   a2wspofv.wc7x0h3j(nabufwbu,li9nb74x,zfb7r31q)
  if self.fd6rupw2>0:
   iy6qktc8=max(0,int(200*self.fd6rupw2/40))
   kt94ow3l=max(1,int(self.fd6rupw2/8))
   cq2q4qer=pygame.Surface((v4u89yjb,rla5ju9b),pygame.SRCALPHA)
   pygame.draw.circle(cq2q4qer,(255,120,40,iy6qktc8),(self.center[0]-li9nb74x,self.center[1]-zfb7r31q),int(self.myrp5ge0),kt94ow3l)
   nabufwbu.blit(cq2q4qer,(0,0))
 def sl65wvjx(self):
  return not self.vyb6li07 and self.fd6rupw2<=0
