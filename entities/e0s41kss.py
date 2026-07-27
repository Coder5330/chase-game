import pygame
import math
from c8v341on import*
from.tdr08cw2 import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,fo75rh8l,jh55hewl,rm0j36tc):
  super().__init__(fo75rh8l,jh55hewl,rm0j36tc)
  self.yrivh6t1=0
 def y06nkwfg(self,player):
  self.yrivh6t1+=1
  return False
 def pv4ykade(self,yg87oi0e,wppsfnko,kybwmlun):
  jh55hewl=self.la3kkrzd.jh55hewl-wppsfnko
  rm0j36tc=self.la3kkrzd.rm0j36tc-kybwmlun
  cq6qdy4l=self.la3kkrzd.centerx-wppsfnko
  lztkkfzz=self.la3kkrzd.centery-kybwmlun
  cb2uuijn=(math.sin(self.yrivh6t1*0.08)+1)/2
  y8dd2255=int(self.la3kkrzd.width*0.9+cb2uuijn*6)
  sld4d6af=int(50+cb2uuijn*60)
  g5l8a78e=pygame.Surface((y8dd2255*2,y8dd2255*2),pygame.SRCALPHA)
  pygame.draw.circle(g5l8a78e,(255,215,0,sld4d6af),(y8dd2255,y8dd2255),y8dd2255,width=4)
  yg87oi0e.blit(g5l8a78e,(cq6qdy4l-y8dd2255,lztkkfzz-y8dd2255))
  self.x37pqkoj(yg87oi0e,jh55hewl,rm0j36tc,cq6qdy4l,lztkkfzz)
