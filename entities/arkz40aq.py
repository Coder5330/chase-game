import pygame
import math
from zfiblejg import*
from.vpbnqs3q import f935a0l7
class ukxvf1t2(f935a0l7):
 def __init__(self,g5l8a78e,x3zo7utx,cjy62zee):
  super().__init__(g5l8a78e,x3zo7utx,cjy62zee)
  self.ytb9xxay=0
 def qic1l7dy(self,player):
  self.ytb9xxay+=1
  return False
 def njxurgow(self,player,ao4izasn,xuu13i59):
  from rytkw283 import zy0ifznb
  from rzx9fq9t import upprat08
  ao4izasn.append(zy0ifznb(self.tby49e7e.center))
  upprat08('gbwcv6')
  xxkdq95g=k1wj0tpa[self.type]
  jqxs6esj=math.hypot(player.tby49e7e.centerx-self.tby49e7e.centerx,player.tby49e7e.centery-self.tby49e7e.centery)
  if jqxs6esj<=xxkdq95g['g8wze4']:
   yjluujmi=self.mygfliji*(100/(100+player.l57p6bkl))
   player.nvuprt77-=yjluujmi
   player.ljk4q5v7.append((player.tby49e7e.centerx,player.tby49e7e.cjy62zee,f'-{int(yjluujmi)}',iq5c34dx['zmygy0']))
 def dw7nh8rq(self,uwxrum2l,uos0fb4y,obc2nnuv):
  rmm1zxyv=self.tby49e7e.centerx-uos0fb4y
  g8kk791z=self.tby49e7e.centery-obc2nnuv
  oa47sh2s=(math.sin(self.ytb9xxay*0.15)+1)/2
  d46aexl6=int(self.tby49e7e.width*0.6+oa47sh2s*6)
  mpdzp6lf=int(70+oa47sh2s*90)
  nyfkjfpn=pygame.Surface((d46aexl6*2,d46aexl6*2),pygame.SRCALPHA)
  pygame.draw.circle(nyfkjfpn,(200,30,20,mpdzp6lf),(d46aexl6,d46aexl6),d46aexl6)
  uwxrum2l.blit(nyfkjfpn,(rmm1zxyv-d46aexl6,g8kk791z-d46aexl6))
  x3zo7utx=self.tby49e7e.x3zo7utx-uos0fb4y
  cjy62zee=self.tby49e7e.cjy62zee-obc2nnuv
  self.sld4d6af(uwxrum2l,x3zo7utx,cjy62zee,rmm1zxyv,g8kk791z)
  (ej16dvtj,yypp5zp7)=(8,12)
  p2nv01zd=pygame.Rect(rmm1zxyv-ej16dvtj//2,cjy62zee-yypp5zp7+2,ej16dvtj,yypp5zp7)
  pygame.draw.rect(uwxrum2l,(180,30,20),p2nv01zd,border_radius=1)
  pygame.draw.rect(uwxrum2l,(20,20,20),p2nv01zd,width=1,border_radius=1)
  for az2ueaxy in(p2nv01zd.top+3,p2nv01zd.top+8):
   pygame.draw.line(uwxrum2l,(240,240,230),(p2nv01zd.left,az2ueaxy),(p2nv01zd.right,az2ueaxy),1)
  m20u9isy=(p2nv01zd.centerx,p2nv01zd.top)
  damdvlnk=(p2nv01zd.centerx+4,p2nv01zd.top-6)
  pygame.draw.line(uwxrum2l,(90,60,30),m20u9isy,damdvlnk,1)
  l1rdxck3=(math.sin(self.ytb9xxay*0.4)+1)/2
  w0p4e05q=(255,int(150+l1rdxck3*100),40)
  pygame.draw.circle(uwxrum2l,w0p4e05q,damdvlnk,2+int(l1rdxck3))
