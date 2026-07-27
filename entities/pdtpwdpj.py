import pygame
import math
from en1x2gdg import*
from.y7iyojtp import f935a0l7,l55nf4zw
from.um4vxjj2 import qc06xq9j,qtzk3ny9
class cq0b8ic8(f935a0l7):
 def do2m71hs(self,gmoft6yr,kybwmlun,i0x65muf):
  qxb7gbdg=self.f8rtm4j3.qxb7gbdg-kybwmlun
  n01uyzpd=self.f8rtm4j3.n01uyzpd-i0x65muf
  ruq9e5co=self.f8rtm4j3.centerx-kybwmlun
  wzs13c9x=self.f8rtm4j3.centery-i0x65muf
  gmoft6yr.blit(l55nf4zw,(ruq9e5co-l55nf4zw.get_width()//2,n01uyzpd+self.f8rtm4j3.height-6))
  l57p6bkl=self.f8rtm4j3.width//2
  for(j0kgazu4,y8bv78hu)in((-6,4),(6,4),(0,-6)):
   (z0b6ugvs,bq349dxb)=(ruq9e5co+j0kgazu4-l57p6bkl//2,wzs13c9x+y8bv78hu-l57p6bkl//2)
   ykipu1wy=pygame.Rect(z0b6ugvs,bq349dxb,l57p6bkl,l57p6bkl)
   pygame.draw.rect(gmoft6yr,qc06xq9j(self.ugez7bh2,0.6),ykipu1wy,border_radius=4)
   vpbwhvnz=ykipu1wy.inflate(-3,-3)
   pygame.draw.rect(gmoft6yr,self.ugez7bh2,vpbwhvnz,border_radius=3)
   pygame.draw.rect(gmoft6yr,(15,15,15),ykipu1wy,width=1,border_radius=4)
  g5hcbbmh=self.sf337kuu/self.ub68rerv
  qtzk3ny9(gmoft6yr,qxb7gbdg,n01uyzpd-8,self.f8rtm4j3.width,g5hcbbmh,height=4)
 def zsw2292m(self,player,tnz61231,wc7x0h3j):
  iaq7b7v1=k1wj0tpa[self.type]
  x5m9j98c=iaq7b7v1['cm3v2p']
  for z8z3v6di in range(x5m9j98c):
   k44nlz15=2*math.pi/x5m9j98c*z8z3v6di
   j0kgazu4=self.f8rtm4j3.centerx+math.cos(k44nlz15)*20
   y8bv78hu=self.f8rtm4j3.centery+math.sin(k44nlz15)*20
   li9nb74x=f935a0l7(self.type,j0kgazu4-zxa3kx7e//2,y8bv78hu-zxa3kx7e//2)
   li9nb74x.sf337kuu=max(1,int(li9nb74x.ub68rerv*0.4))
   li9nb74x.ub68rerv=li9nb74x.sf337kuu
   wc7x0h3j.append(li9nb74x)
