import pygame
import math
from rlfzkicw import*
from.o3ksgnbh import dmu5907i
class bl6246hi(dmu5907i):
 def __init__(self,mfyb8dal,kn5gjj8m,lu7jae58):
  super().__init__(mfyb8dal,kn5gjj8m,lu7jae58)
  self.jqzpniqf=0
 def tjy1o2rn(self,player):
  self.jqzpniqf+=1
  return False
 def u1jhuwb6(self,todsx4nx,u3ifhv1x,f8wquuy5):
  kn5gjj8m=self.wb7f6fdh.kn5gjj8m-u3ifhv1x
  lu7jae58=self.wb7f6fdh.lu7jae58-f8wquuy5
  x5m9j98c=self.wb7f6fdh.centerx-u3ifhv1x
  uos0fb4y=self.wb7f6fdh.centery-f8wquuy5
  gj29yfc2=(math.sin(self.jqzpniqf*0.08)+1)/2
  mmn32u1i=int(self.wb7f6fdh.width*0.9+gj29yfc2*6)
  wkzorqqf=int(50+gj29yfc2*60)
  le9oe941=pygame.Surface((mmn32u1i*2,mmn32u1i*2),pygame.SRCALPHA)
  pygame.draw.circle(le9oe941,(255,215,0,wkzorqqf),(mmn32u1i,mmn32u1i),mmn32u1i,width=4)
  todsx4nx.blit(le9oe941,(x5m9j98c-mmn32u1i,uos0fb4y-mmn32u1i))
  self.xd1wjcit(todsx4nx,kn5gjj8m,lu7jae58,x5m9j98c,uos0fb4y)
