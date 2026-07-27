import pygame
import math
from i1arxabo import*
from.lhkgad7x import f935a0l7,l55nf4zw
from.uu86zjq7 import fd6rupw2,eohswq40
class m7hv3izk(f935a0l7):
 def sl65wvjx(self,tj0nmeoq,uysal8m1,giec4d14):
  htgsiwg0=self.todsx4nx.htgsiwg0-uysal8m1
  hhl1737s=self.todsx4nx.hhl1737s-giec4d14
  wi8skch8=self.todsx4nx.centerx-uysal8m1
  iektsg7f=self.todsx4nx.centery-giec4d14
  tj0nmeoq.blit(l55nf4zw,(wi8skch8-l55nf4zw.get_width()//2,hhl1737s+self.todsx4nx.height-6))
  kmgfxc08=self.todsx4nx.width//2
  for(zdan085r,mmn32u1i)in((-6,4),(6,4),(0,-6)):
   (i0x65muf,llxxezdu)=(wi8skch8+zdan085r-kmgfxc08//2,iektsg7f+mmn32u1i-kmgfxc08//2)
   sv5f1bcp=pygame.Rect(i0x65muf,llxxezdu,kmgfxc08,kmgfxc08)
   pygame.draw.rect(tj0nmeoq,fd6rupw2(self.i20cv3tl,0.6),sv5f1bcp,border_radius=4)
   sdeekgys=sv5f1bcp.inflate(-3,-3)
   pygame.draw.rect(tj0nmeoq,self.i20cv3tl,sdeekgys,border_radius=3)
   pygame.draw.rect(tj0nmeoq,(15,15,15),sv5f1bcp,width=1,border_radius=4)
  exvaj2k8=self.mpyxdw2z/self.mctwjlsh
  eohswq40(tj0nmeoq,htgsiwg0,hhl1737s-8,self.todsx4nx.width,exvaj2k8,height=4)
 def hu9n79gi(self,player,ouuylaja,uc1xi04b):
  byl68ntk=k1wj0tpa[self.type]
  iie0rnuj=byl68ntk['kk2y77']
  for jo8e7flq in range(iie0rnuj):
   t5wi6fqj=2*math.pi/iie0rnuj*jo8e7flq
   zdan085r=self.todsx4nx.centerx+math.cos(t5wi6fqj)*20
   mmn32u1i=self.todsx4nx.centery+math.sin(t5wi6fqj)*20
   pvasifpw=f935a0l7(self.type,zdan085r-zxa3kx7e//2,mmn32u1i-zxa3kx7e//2)
   pvasifpw.mpyxdw2z=max(1,int(pvasifpw.mctwjlsh*0.4))
   pvasifpw.mctwjlsh=pvasifpw.mpyxdw2z
   uc1xi04b.append(pvasifpw)
