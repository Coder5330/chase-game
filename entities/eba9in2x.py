import pygame
import math
from v7bnhjw6 import*
from.e1gnfiue import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,gubmc97c,qic1l7dy,vsjchzjq):
  super().__init__(gubmc97c,qic1l7dy,vsjchzjq)
  sfu38gl2=k1wj0tpa[gubmc97c]
  self.rh0w064w=sfu38gl2['en1x2g']
  self.w0p4e05q=sfu38gl2['gbwcv6']
  self.l1rdxck3=sfu38gl2['g8wze4']
  self.bdgbk2l0=sfu38gl2['bx1ego']
  self.mfc79m96=sfu38gl2['en1x2g']
  self.jyjhu8my='hidden'
  self.hdw6lqwl=self.w0p4e05q
 def t5wi6fqj(self):
  self.hdw6lqwl-=1
  if self.hdw6lqwl<=0:
   if self.jyjhu8my=='hidden':
    self.jyjhu8my='revealing'
    self.hdw6lqwl=self.bdgbk2l0
   elif self.jyjhu8my=='revealing':
    self.jyjhu8my='visible'
    self.hdw6lqwl=self.l1rdxck3
   else:
    self.jyjhu8my='hidden'
    self.hdw6lqwl=self.w0p4e05q
  self.mfc79m96=self.rh0w064w if self.jyjhu8my=='hidden'else 255
 def r2muljav(self,player):
  if self.mn7h9g1a<=0:
   self.sl65wvjx=True
   return
  self.t5wi6fqj()
  if self.jyjhu8my=='visible'and abs(player.jenvg3kk.qic1l7dy-self.jenvg3kk.qic1l7dy)<cawudtse and(abs(player.jenvg3kk.vsjchzjq-self.jenvg3kk.vsjchzjq)<cawudtse):
   self.ytv3i12v(player)
   return
  x875aud9=player.jenvg3kk.qic1l7dy-self.jenvg3kk.qic1l7dy
  jqxs6esj=player.jenvg3kk.vsjchzjq-self.jenvg3kk.vsjchzjq
  wehlxslg=math.hypot(x875aud9,jqxs6esj)
  if wehlxslg==0:
   return
  ucu7onz3=x875aud9/wehlxslg
  it04chsd=jqxs6esj/wehlxslg
  if ucu7onz3!=0 and it04chsd!=0:
   ucu7onz3*=0.707
   it04chsd*=0.707
  self.jenvg3kk.qic1l7dy+=ucu7onz3*self.xvzc7d2k
  self.jenvg3kk.vsjchzjq+=it04chsd*self.xvzc7d2k
  self.jenvg3kk.qic1l7dy=round(self.jenvg3kk.qic1l7dy)
  self.jenvg3kk.vsjchzjq=round(self.jenvg3kk.vsjchzjq)
 def wc7x0h3j(self,gg7oq2zd,li9nb74x,zfb7r31q):
  qic1l7dy=self.jenvg3kk.qic1l7dy-li9nb74x
  vsjchzjq=self.jenvg3kk.vsjchzjq-zfb7r31q
  pa8s8hmb=self.jenvg3kk.centerx-li9nb74x
  pv4ykade=self.jenvg3kk.centery-zfb7r31q
  if self.mfc79m96>=255:
   self.wrbw2zla(gg7oq2zd,qic1l7dy,vsjchzjq,pa8s8hmb,pv4ykade)
   return
  lnf74t60=24
  az2ueaxy=pygame.Surface((self.jenvg3kk.width+lnf74t60*2,self.jenvg3kk.height+lnf74t60*2),pygame.SRCALPHA)
  (ls2zge2j,d1b3jczu)=(lnf74t60,lnf74t60)
  (f55dmcxx,bokzixza)=(ls2zge2j+self.jenvg3kk.width//2,d1b3jczu+self.jenvg3kk.height//2)
  self.wrbw2zla(az2ueaxy,ls2zge2j,d1b3jczu,f55dmcxx,bokzixza)
  az2ueaxy.set_alpha(self.mfc79m96)
  gg7oq2zd.blit(az2ueaxy,(qic1l7dy-lnf74t60,vsjchzjq-lnf74t60))
