import pygame
import math
from z1yhxso7 import*
from.pxq7bzeg import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,vhuds3qs,jslulzfy,zpfb3hn1):
  super().__init__(vhuds3qs,jslulzfy,zpfb3hn1)
  self.v76ub7l8=0
 def ejbzutru(self,player):
  self.v76ub7l8+=1
  return False
 def wzlm72je(self,ukshy8nb,dzsedfqs,nd6357oo):
  jslulzfy=self.wgcl9lcq.jslulzfy-dzsedfqs
  zpfb3hn1=self.wgcl9lcq.zpfb3hn1-nd6357oo
  hfb85p86=self.wgcl9lcq.centerx-dzsedfqs
  k7zgf9q5=self.wgcl9lcq.centery-nd6357oo
  hcxhgnze=(math.sin(self.v76ub7l8*0.08)+1)/2
  ljk4q5v7=int(self.wgcl9lcq.width*0.9+hcxhgnze*6)
  yx4w6xlp=int(50+hcxhgnze*60)
  q7i6yuj7=pygame.Surface((ljk4q5v7*2,ljk4q5v7*2),pygame.SRCALPHA)
  pygame.draw.circle(q7i6yuj7,(255,215,0,yx4w6xlp),(ljk4q5v7,ljk4q5v7),ljk4q5v7,width=4)
  ukshy8nb.blit(q7i6yuj7,(hfb85p86-ljk4q5v7,k7zgf9q5-ljk4q5v7))
  self.t1w1ht7p(ukshy8nb,jslulzfy,zpfb3hn1,hfb85p86,k7zgf9q5)
