import pygame
import math
from c8v341on import*
from.tdr08cw2 import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,fo75rh8l,jh55hewl,rm0j36tc):
  super().__init__(fo75rh8l,jh55hewl,rm0j36tc)
  gj29yfc2=k1wj0tpa[fo75rh8l]
  self.mn89ltaj=gj29yfc2['i6ozx2']
  self.g1b3d505=gj29yfc2['c37qqy']
  self.xxns2zyb=gj29yfc2['w1q8f6']
  self.todsx4nx=gj29yfc2['yl6lgj']
  self.chx3d43e=gj29yfc2['i6ozx2']
  self.kz1uu7zy='hidden'
  self.rk43safy=self.g1b3d505
 def nd96qe3r(self):
  self.rk43safy-=1
  if self.rk43safy<=0:
   if self.kz1uu7zy=='hidden':
    self.kz1uu7zy='revealing'
    self.rk43safy=self.todsx4nx
   elif self.kz1uu7zy=='revealing':
    self.kz1uu7zy='visible'
    self.rk43safy=self.xxns2zyb
   else:
    self.kz1uu7zy='hidden'
    self.rk43safy=self.g1b3d505
  self.chx3d43e=self.mn89ltaj if self.kz1uu7zy=='hidden'else 255
 def lnf74t60(self,player):
  if self.azc4xl99<=0:
   self.iektsg7f=True
   return
  self.nd96qe3r()
  if self.kz1uu7zy=='visible'and abs(player.la3kkrzd.jh55hewl-self.la3kkrzd.jh55hewl)<cawudtse and(abs(player.la3kkrzd.rm0j36tc-self.la3kkrzd.rm0j36tc)<cawudtse):
   self.yx4w6xlp(player)
   return
  qtzk3ny9=player.la3kkrzd.jh55hewl-self.la3kkrzd.jh55hewl
  sl65wvjx=player.la3kkrzd.rm0j36tc-self.la3kkrzd.rm0j36tc
  bfoqmf5l=math.hypot(qtzk3ny9,sl65wvjx)
  if bfoqmf5l==0:
   return
  i7zcgdc5=qtzk3ny9/bfoqmf5l
  rb1s9dwd=sl65wvjx/bfoqmf5l
  if i7zcgdc5!=0 and rb1s9dwd!=0:
   i7zcgdc5*=0.707
   rb1s9dwd*=0.707
  self.la3kkrzd.jh55hewl+=i7zcgdc5*self.qertb74r
  self.la3kkrzd.rm0j36tc+=rb1s9dwd*self.qertb74r
  self.la3kkrzd.jh55hewl=round(self.la3kkrzd.jh55hewl)
  self.la3kkrzd.rm0j36tc=round(self.la3kkrzd.rm0j36tc)
 def pv4ykade(self,yg87oi0e,wppsfnko,kybwmlun):
  jh55hewl=self.la3kkrzd.jh55hewl-wppsfnko
  rm0j36tc=self.la3kkrzd.rm0j36tc-kybwmlun
  cq6qdy4l=self.la3kkrzd.centerx-wppsfnko
  lztkkfzz=self.la3kkrzd.centery-kybwmlun
  if self.chx3d43e>=255:
   self.x37pqkoj(yg87oi0e,jh55hewl,rm0j36tc,cq6qdy4l,lztkkfzz)
   return
  fpa8hyex=24
  v24479qt=pygame.Surface((self.la3kkrzd.width+fpa8hyex*2,self.la3kkrzd.height+fpa8hyex*2),pygame.SRCALPHA)
  (xk7n8la1,xd8wz42o)=(fpa8hyex,fpa8hyex)
  (gqj5sxvw,semqgy27)=(xk7n8la1+self.la3kkrzd.width//2,xd8wz42o+self.la3kkrzd.height//2)
  self.x37pqkoj(v24479qt,xk7n8la1,xd8wz42o,gqj5sxvw,semqgy27)
  v24479qt.set_alpha(self.chx3d43e)
  yg87oi0e.blit(v24479qt,(jh55hewl-fpa8hyex,rm0j36tc-fpa8hyex))
