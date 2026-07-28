import pygame
import math
from z1yhxso7 import*
from.pxq7bzeg import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,vhuds3qs,jslulzfy,zpfb3hn1):
  super().__init__(vhuds3qs,jslulzfy,zpfb3hn1)
  n64fgwje=k1wj0tpa[vhuds3qs]
  self.hdw6lqwl=n64fgwje['kj2jvq']
  self.v24479qt=n64fgwje['onlt8d']
  self.jyjhu8my=n64fgwje['rw8p74']
  self.xwk2rv23=n64fgwje['pcs4ke']
  self.wy0mahym=n64fgwje['kj2jvq']
  self.z5x8a5fb='hidden'
  self.svt8k06m=self.v24479qt
 def jmpioygg(self):
  self.svt8k06m-=1
  if self.svt8k06m<=0:
   if self.z5x8a5fb=='hidden':
    self.z5x8a5fb='revealing'
    self.svt8k06m=self.xwk2rv23
   elif self.z5x8a5fb=='revealing':
    self.z5x8a5fb='visible'
    self.svt8k06m=self.jyjhu8my
   else:
    self.z5x8a5fb='hidden'
    self.svt8k06m=self.v24479qt
  self.wy0mahym=self.hdw6lqwl if self.z5x8a5fb=='hidden'else 255
 def ob7p0rnp(self,player):
  if self.u9el8hl8<=0:
   self.elwf90km=True
   return
  self.jmpioygg()
  if self.z5x8a5fb=='visible'and abs(player.wgcl9lcq.jslulzfy-self.wgcl9lcq.jslulzfy)<cawudtse and(abs(player.wgcl9lcq.zpfb3hn1-self.wgcl9lcq.zpfb3hn1)<cawudtse):
   self.uva2ieuc(player)
   return
  uc1xi04b=player.wgcl9lcq.jslulzfy-self.wgcl9lcq.jslulzfy
  fp47b42g=player.wgcl9lcq.zpfb3hn1-self.wgcl9lcq.zpfb3hn1
  mfyb8dal=math.hypot(uc1xi04b,fp47b42g)
  if mfyb8dal==0:
   return
  gsrtwlxd=uc1xi04b/mfyb8dal
  qxb7gbdg=fp47b42g/mfyb8dal
  if gsrtwlxd!=0 and qxb7gbdg!=0:
   gsrtwlxd*=0.707
   qxb7gbdg*=0.707
  self.wgcl9lcq.jslulzfy+=gsrtwlxd*self.u15pdtz9
  self.wgcl9lcq.zpfb3hn1+=qxb7gbdg*self.u15pdtz9
  self.wgcl9lcq.jslulzfy=round(self.wgcl9lcq.jslulzfy)
  self.wgcl9lcq.zpfb3hn1=round(self.wgcl9lcq.zpfb3hn1)
 def wzlm72je(self,ukshy8nb,dzsedfqs,nd6357oo):
  jslulzfy=self.wgcl9lcq.jslulzfy-dzsedfqs
  zpfb3hn1=self.wgcl9lcq.zpfb3hn1-nd6357oo
  hfb85p86=self.wgcl9lcq.centerx-dzsedfqs
  k7zgf9q5=self.wgcl9lcq.centery-nd6357oo
  if self.wy0mahym>=255:
   self.t1w1ht7p(ukshy8nb,jslulzfy,zpfb3hn1,hfb85p86,k7zgf9q5)
   return
  ls2zge2j=24
  rserev36=pygame.Surface((self.wgcl9lcq.width+ls2zge2j*2,self.wgcl9lcq.height+ls2zge2j*2),pygame.SRCALPHA)
  (mctwjlsh,zflv1xxl)=(ls2zge2j,ls2zge2j)
  (xd8wz42o,n3rlkte4)=(mctwjlsh+self.wgcl9lcq.width//2,zflv1xxl+self.wgcl9lcq.height//2)
  self.t1w1ht7p(rserev36,mctwjlsh,zflv1xxl,xd8wz42o,n3rlkte4)
  rserev36.set_alpha(self.wy0mahym)
  ukshy8nb.blit(rserev36,(jslulzfy-ls2zge2j,zpfb3hn1-ls2zge2j))
