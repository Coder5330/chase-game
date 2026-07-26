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
 def u1jhuwb6(self,uz6kf162,u3ifhv1x,f8wquuy5):
  kn5gjj8m=self.mu4fmpkx.kn5gjj8m-u3ifhv1x
  lu7jae58=self.mu4fmpkx.lu7jae58-f8wquuy5
  x5m9j98c=self.mu4fmpkx.centerx-u3ifhv1x
  uos0fb4y=self.mu4fmpkx.centery-f8wquuy5
  g1b3d505=(math.sin(self.jqzpniqf*0.08)+1)/2
  mfc79m96=int(self.mu4fmpkx.width*0.9+g1b3d505*6)
  wkzorqqf=int(50+g1b3d505*60)
  le9oe941=pygame.Surface((mfc79m96*2,mfc79m96*2),pygame.SRCALPHA)
  pygame.draw.circle(le9oe941,(255,215,0,wkzorqqf),(mfc79m96,mfc79m96),mfc79m96,width=4)
  uz6kf162.blit(le9oe941,(x5m9j98c-mfc79m96,uos0fb4y-mfc79m96))
  self.xd1wjcit(uz6kf162,kn5gjj8m,lu7jae58,x5m9j98c,uos0fb4y)
