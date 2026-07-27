import pygame
import math
from o100vhmy import*
from.vq3jzr25 import f935a0l7,l55nf4zw
from.mipwh0mx import xwk2rv23,qbbz2sf6
class cq0b8ic8(f935a0l7):
 def i01nouht(self,npejzhya,kybwmlun,i0x65muf):
  rm0j36tc=self.zflse45b.rm0j36tc-kybwmlun
  tza7x73q=self.zflse45b.tza7x73q-i0x65muf
  lztkkfzz=self.zflse45b.centerx-kybwmlun
  f2sehe2a=self.zflse45b.centery-i0x65muf
  npejzhya.blit(l55nf4zw,(lztkkfzz-l55nf4zw.get_width()//2,tza7x73q+self.zflse45b.height-6))
  l57p6bkl=self.zflse45b.width//2
  for(jl90pxrl,w8y72ivg)in((-6,4),(6,4),(0,-6)):
   (z0b6ugvs,bq349dxb)=(lztkkfzz+jl90pxrl-l57p6bkl//2,f2sehe2a+w8y72ivg-l57p6bkl//2)
   ykipu1wy=pygame.Rect(z0b6ugvs,bq349dxb,l57p6bkl,l57p6bkl)
   pygame.draw.rect(npejzhya,xwk2rv23(self.ebt3g2qz,0.6),ykipu1wy,border_radius=4)
   we4xyf9i=ykipu1wy.inflate(-3,-3)
   pygame.draw.rect(npejzhya,self.ebt3g2qz,we4xyf9i,border_radius=3)
   pygame.draw.rect(npejzhya,(15,15,15),ykipu1wy,width=1,border_radius=4)
  he9p3jpx=self.q7i6yuj7/self.k2ixivzk
  qbbz2sf6(npejzhya,rm0j36tc,tza7x73q-8,self.zflse45b.width,he9p3jpx,height=4)
 def lhgk5bwi(self,player,velos6zl,wzlm72je):
  mn89ltaj=k1wj0tpa[self.type]
  clkqzfpq=mn89ltaj['i6ozx2']
  for nyfkjfpn in range(clkqzfpq):
   k44nlz15=2*math.pi/clkqzfpq*nyfkjfpn
   jl90pxrl=self.zflse45b.centerx+math.cos(k44nlz15)*20
   w8y72ivg=self.zflse45b.centery+math.sin(k44nlz15)*20
   nd6357oo=f935a0l7(self.type,jl90pxrl-zxa3kx7e//2,w8y72ivg-zxa3kx7e//2)
   nd6357oo.q7i6yuj7=max(1,int(nd6357oo.k2ixivzk*0.4))
   nd6357oo.k2ixivzk=nd6357oo.q7i6yuj7
   wzlm72je.append(nd6357oo)
