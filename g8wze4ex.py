import pygame
import pygame.gfxdraw
import random
import math
from i1arxabo import dtx63cfl,rla5ju9b
def jq1ddpus(w0p4e05q):
 if w0p4e05q>0.75:
  return(255,255,int(200+55*(w0p4e05q-0.75)/0.25))
 elif w0p4e05q>0.5:
  mq7nc85e=(w0p4e05q-0.5)/0.25
  return(255,int(200+55*mq7nc85e),int(80*mq7nc85e))
 elif w0p4e05q>0.25:
  mq7nc85e=(w0p4e05q-0.25)/0.25
  return(255,int(90+110*mq7nc85e),20)
 else:
  mq7nc85e=w0p4e05q/0.25
  return(int(120+135*mq7nc85e),int(30*mq7nc85e),20)
class rcfnfhol:
 def __init__(self,htgsiwg0,hhl1737s):
  t5wi6fqj=random.uniform(0,2*math.pi)
  mn89ltaj=random.uniform(1,6)*random.choice([1,1,1,1.5])
  self.htgsiwg0=htgsiwg0
  self.hhl1737s=hhl1737s
  self.jh55hewl=math.cos(t5wi6fqj)*mn89ltaj
  self.f2voi8uy=math.sin(t5wi6fqj)*mn89ltaj
  self.life=random.randint(15,35)
  self.ub68rerv=self.life
  self.wd6r30oj=random.uniform(1.5,3.5)
 def update(self):
  self.htgsiwg0+=self.jh55hewl
  self.hhl1737s+=self.f2voi8uy
  self.jh55hewl*=0.96
  self.f2voi8uy*=0.96
  self.f2voi8uy+=0.05
  self.life-=1
 def sl65wvjx(self,hdw6lqwl,uysal8m1,giec4d14):
  if self.life<=0:
   return
  w0p4e05q=self.life/self.ub68rerv
  (l3swebnv,xq46nouh,e5x4w7ky)=jq1ddpus(w0p4e05q)
  jmpioygg=int(255*w0p4e05q)
  f8rtm4j3=max(1,int(self.wd6r30oj*(0.5+w0p4e05q)))
  xwk2rv23=pygame.Surface((f8rtm4j3*2+2,f8rtm4j3*2+2),pygame.SRCALPHA)
  pygame.gfxdraw.filled_circle(xwk2rv23,f8rtm4j3+1,f8rtm4j3+1,f8rtm4j3,(l3swebnv,xq46nouh,e5x4w7ky,jmpioygg))
  pygame.gfxdraw.aacircle(xwk2rv23,f8rtm4j3+1,f8rtm4j3+1,f8rtm4j3,(l3swebnv,xq46nouh,e5x4w7ky,jmpioygg))
  hdw6lqwl.blit(xwk2rv23,(self.htgsiwg0-uysal8m1-f8rtm4j3-1,self.hhl1737s-giec4d14-f8rtm4j3-1),special_flags=pygame.BLEND_ADD)
class zy0ifznb:
 def __init__(self,center,iie0rnuj=40):
  self.got7txkd=[rcfnfhol(*center)for ygspk9p3 in range(iie0rnuj)]
  self.center=center
  self.k1taa0i5=1.0
  self.xsspye9r=8.0
  self.jenvg3kk=25
 def update(self):
  for oc4kl8cg in self.got7txkd:
   oc4kl8cg.update()
  self.got7txkd=[oc4kl8cg for oc4kl8cg in self.got7txkd if oc4kl8cg.life>0]
  self.k1taa0i5+=self.xsspye9r
  self.xsspye9r*=0.9
  self.jenvg3kk-=1
 def sl65wvjx(self,hdw6lqwl,uysal8m1,giec4d14):
  for oc4kl8cg in self.got7txkd:
   oc4kl8cg.sl65wvjx(hdw6lqwl,uysal8m1,giec4d14)
  if self.jenvg3kk>0:
   mnx39rbs=max(0,int(200*self.jenvg3kk/40))
   wvndfdw7=max(1,int(self.jenvg3kk/8))
   xwk2rv23=pygame.Surface((dtx63cfl,rla5ju9b),pygame.SRCALPHA)
   pygame.draw.circle(xwk2rv23,(255,120,40,mnx39rbs),(self.center[0]-uysal8m1,self.center[1]-giec4d14),int(self.k1taa0i5),wvndfdw7)
   hdw6lqwl.blit(xwk2rv23,(0,0))
 def k7zgf9q5(self):
  return not self.got7txkd and self.jenvg3kk<=0
