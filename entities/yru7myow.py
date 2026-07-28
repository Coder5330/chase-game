import pygame
import math
from z1yhxso7 import*
from.pxq7bzeg import f935a0l7
class ukxvf1t2(f935a0l7):
 def __init__(self,vhuds3qs,jslulzfy,zpfb3hn1):
  super().__init__(vhuds3qs,jslulzfy,zpfb3hn1)
  self.uj64qhks=0
 def ejbzutru(self,player):
  self.uj64qhks+=1
  return False
 def pf0i9g5d(self,player,aicvqy5i,yjluujmi):
  from b63dw4c3 import zy0ifznb
  aicvqy5i.append(zy0ifznb(self.wgcl9lcq.center))
  n64fgwje=k1wj0tpa[self.type]
  yuibrsz1=math.hypot(player.wgcl9lcq.centerx-self.wgcl9lcq.centerx,player.wgcl9lcq.centery-self.wgcl9lcq.centery)
  if yuibrsz1<=n64fgwje['og8cd3']:
   rmm1zxyv=self.wehlxslg*(100/(100+player.pa5u6hc3))
   player.u9el8hl8-=rmm1zxyv
   player.vyb6li07.append((player.wgcl9lcq.centerx,player.wgcl9lcq.zpfb3hn1,f'-{int(rmm1zxyv)}',iq5c34dx['xy79kv']))
 def wzlm72je(self,ukshy8nb,dzsedfqs,nd6357oo):
  hfb85p86=self.wgcl9lcq.centerx-dzsedfqs
  k7zgf9q5=self.wgcl9lcq.centery-nd6357oo
  hcxhgnze=(math.sin(self.uj64qhks*0.15)+1)/2
  ljk4q5v7=int(self.wgcl9lcq.width*0.6+hcxhgnze*6)
  yx4w6xlp=int(70+hcxhgnze*90)
  q7i6yuj7=pygame.Surface((ljk4q5v7*2,ljk4q5v7*2),pygame.SRCALPHA)
  pygame.draw.circle(q7i6yuj7,(200,30,20,yx4w6xlp),(ljk4q5v7,ljk4q5v7),ljk4q5v7)
  ukshy8nb.blit(q7i6yuj7,(hfb85p86-ljk4q5v7,k7zgf9q5-ljk4q5v7))
  jslulzfy=self.wgcl9lcq.jslulzfy-dzsedfqs
  zpfb3hn1=self.wgcl9lcq.zpfb3hn1-nd6357oo
  self.t1w1ht7p(ukshy8nb,jslulzfy,zpfb3hn1,hfb85p86,k7zgf9q5)
  (rh0w064w,w0p4e05q)=(8,12)
  l1rdxck3=pygame.Rect(hfb85p86-rh0w064w//2,zpfb3hn1-w0p4e05q+2,rh0w064w,w0p4e05q)
  pygame.draw.rect(ukshy8nb,(180,30,20),l1rdxck3,border_radius=1)
  pygame.draw.rect(ukshy8nb,(20,20,20),l1rdxck3,width=1,border_radius=1)
  for u1ni10kq in(l1rdxck3.top+3,l1rdxck3.top+8):
   pygame.draw.line(ukshy8nb,(240,240,230),(l1rdxck3.left,u1ni10kq),(l1rdxck3.right,u1ni10kq),1)
  ao4izasn=(l1rdxck3.centerx,l1rdxck3.top)
  r98s4c3b=(l1rdxck3.centerx+4,l1rdxck3.top-6)
  pygame.draw.line(ukshy8nb,(90,60,30),ao4izasn,r98s4c3b,1)
  h8s2ftom=(math.sin(self.uj64qhks*0.4)+1)/2
  uwxrum2l=(255,int(150+h8s2ftom*100),40)
  pygame.draw.circle(ukshy8nb,uwxrum2l,r98s4c3b,2+int(h8s2ftom))
