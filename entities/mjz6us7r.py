import pygame
import math
from z1yhxso7 import*
from.pxq7bzeg import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,vhuds3qs,jslulzfy,zpfb3hn1):
  super().__init__(vhuds3qs,jslulzfy,zpfb3hn1)
  self.nubmxnsz=(0,1)
  self.ebt3g2qz=False
  self.amcixdu1=0
  self.z9toqw9j=18
 def ejbzutru(self,player):
  uc1xi04b=player.wgcl9lcq.centerx-self.wgcl9lcq.centerx
  fp47b42g=player.wgcl9lcq.centery-self.wgcl9lcq.centery
  bokzixza=math.hypot(uc1xi04b,fp47b42g)or 1
  self.nubmxnsz=(uc1xi04b/bokzixza,fp47b42g/bokzixza)
  if self.ebt3g2qz:
   self.amcixdu1-=1
   if self.amcixdu1<=0:
    self.ebt3g2qz=False
    self.g5l8a78e(player)
   return True
  if abs(player.wgcl9lcq.jslulzfy-self.wgcl9lcq.jslulzfy)<b8cgvyie and abs(player.wgcl9lcq.zpfb3hn1-self.wgcl9lcq.zpfb3hn1)<b8cgvyie:
   if self.ytv3i12v>0:
    self.ytv3i12v-=1
    return True
   self.ebt3g2qz=True
   self.amcixdu1=self.z9toqw9j
   return True
  return False
 def g5l8a78e(self,player):
  self.ytv3i12v=self.vvslh9bh
  from ft8xkody import rpqk51fp
  gj29yfc2=uqjiujv6['g0ht1t']['xfq3jz']
  (uc1xi04b,fp47b42g)=(player.wgcl9lcq.centerx-self.wgcl9lcq.centerx,player.wgcl9lcq.centery-self.wgcl9lcq.centery)
  wkof8krd=rpqk51fp('g0ht1t',self.wgcl9lcq.centerx-gj29yfc2//2,self.wgcl9lcq.centery-gj29yfc2//2,gj29yfc2,gj29yfc2,uc1xi04b,fp47b42g)
  wkof8krd.pa8s8hmb=self.wehlxslg
  self.e5x4w7ky.append(wkof8krd)
 def wzlm72je(self,ukshy8nb,dzsedfqs,nd6357oo):
  jslulzfy=self.wgcl9lcq.jslulzfy-dzsedfqs
  zpfb3hn1=self.wgcl9lcq.zpfb3hn1-nd6357oo
  hfb85p86=self.wgcl9lcq.centerx-dzsedfqs
  k7zgf9q5=self.wgcl9lcq.centery-nd6357oo
  self.t1w1ht7p(ukshy8nb,jslulzfy,zpfb3hn1,hfb85p86,k7zgf9q5)
  (tw76xato,atj9a3y3)=self.nubmxnsz
  (uz6kf162,z3olfark)=(-atj9a3y3,tw76xato)
  (j2vmcqbn,jc54wsqt)=(hfb85p86+tw76xato*14,k7zgf9q5+atj9a3y3*14)
  vm65q57t=(j2vmcqbn+uz6kf162*13-tw76xato*6,jc54wsqt+z3olfark*13-atj9a3y3*6)
  e8zgvwwu=(j2vmcqbn-uz6kf162*13-tw76xato*6,jc54wsqt-z3olfark*13-atj9a3y3*6)
  llxxezdu=(j2vmcqbn+tw76xato*6,jc54wsqt+atj9a3y3*6)
  pygame.draw.lines(ukshy8nb,(110,70,30),False,[vm65q57t,llxxezdu,e8zgvwwu],3)
  vt6om1fb=1-self.amcixdu1/self.z9toqw9j if self.ebt3g2qz else 0
  bihsa7he=(j2vmcqbn-tw76xato*(3+vt6om1fb*10),jc54wsqt-atj9a3y3*(3+vt6om1fb*10))
  pygame.draw.line(ukshy8nb,(225,225,215),vm65q57t,bihsa7he,2)
  pygame.draw.line(ukshy8nb,(225,225,215),e8zgvwwu,bihsa7he,2)
  if self.ebt3g2qz:
   reqy08p0=(j2vmcqbn+tw76xato*8,jc54wsqt+atj9a3y3*8)
   pygame.draw.line(ukshy8nb,iq5c34dx['vsjchz'],bihsa7he,reqy08p0,3)
