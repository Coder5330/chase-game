import pygame
import math
from v7bnhjw6 import*
from.e1gnfiue import f935a0l7,l55nf4zw
from.czvky2re import qertb74r,fo75rh8l
class ozp08j3t(f935a0l7):
 def wc7x0h3j(self,gg7oq2zd,li9nb74x,zfb7r31q):
  qic1l7dy=self.jenvg3kk.qic1l7dy-li9nb74x
  vsjchzjq=self.jenvg3kk.vsjchzjq-zfb7r31q
  pa8s8hmb=self.jenvg3kk.centerx-li9nb74x
  pv4ykade=self.jenvg3kk.centery-zfb7r31q
  gg7oq2zd.blit(l55nf4zw,(pa8s8hmb-l55nf4zw.get_width()//2,vsjchzjq+self.jenvg3kk.height-6))
  mal2w37d=self.jenvg3kk.width//2
  for(ncyh3fvl,x6cnoljq)in((-6,4),(6,4),(0,-6)):
   (f32ejx5t,dzsedfqs)=(pa8s8hmb+ncyh3fvl-mal2w37d//2,pv4ykade+x6cnoljq-mal2w37d//2)
   fcwtg1m8=pygame.Rect(f32ejx5t,dzsedfqs,mal2w37d,mal2w37d)
   pygame.draw.rect(gg7oq2zd,qertb74r(self.lztkkfzz,0.6),fcwtg1m8,border_radius=4)
   rktlzkj4=fcwtg1m8.inflate(-3,-3)
   pygame.draw.rect(gg7oq2zd,self.lztkkfzz,rktlzkj4,border_radius=3)
   pygame.draw.rect(gg7oq2zd,(15,15,15),fcwtg1m8,width=1,border_radius=4)
  upprat08=self.mn7h9g1a/self.y2f7atwy
  fo75rh8l(gg7oq2zd,qic1l7dy,vsjchzjq-8,self.jenvg3kk.width,upprat08,height=4)
 def oc4kl8cg(self,player,xuu13i59,dw7nh8rq):
  sfu38gl2=k1wj0tpa[self.type]
  wi8skch8=sfu38gl2['onlt8d']
  for ftrflqbm in range(wi8skch8):
   lt63j3r3=2*math.pi/wi8skch8*ftrflqbm
   ncyh3fvl=self.jenvg3kk.centerx+math.cos(lt63j3r3)*20
   x6cnoljq=self.jenvg3kk.centery+math.sin(lt63j3r3)*20
   i20cv3tl=f935a0l7(self.type,ncyh3fvl-zxa3kx7e//2,x6cnoljq-zxa3kx7e//2)
   i20cv3tl.mn7h9g1a=max(1,int(i20cv3tl.y2f7atwy*0.4))
   i20cv3tl.y2f7atwy=i20cv3tl.mn7h9g1a
   dw7nh8rq.append(i20cv3tl)
