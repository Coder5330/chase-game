import pygame
import math
from zfiblejg import*
from.fjzr5swk import gxlk8wru,b36htf4p
pygame.init()
l55nf4zw=pygame.Surface((zxa3kx7e+12,12),pygame.SRCALPHA)
pygame.draw.ellipse(l55nf4zw,(0,0,0,80),l55nf4zw.get_rect())
class f935a0l7:
 def __init__(self,g5l8a78e,x3zo7utx,cjy62zee):
  self.type=g5l8a78e
  self.nvuprt77=k1wj0tpa[self.type]['urf1hx']
  self.zsw2292m=k1wj0tpa[self.type]['urf1hx']
  self.mygfliji=k1wj0tpa[self.type]['hzj7ub']
  self.p7b1ijiy=k1wj0tpa[self.type]['jo31yh']
  self.x875aud9=k1wj0tpa[self.type]['rw8p74']
  self.k7zgf9q5=k1wj0tpa[self.type]['pcs4ke']
  self.w2sq3b9s=k1wj0tpa[self.type]['hipi78']
  self.llxxezdu=k1wj0tpa[self.type]['buzery']
  self.nrpj1epk=k1wj0tpa[self.type]['buzery']
  self.tby49e7e=pygame.Rect(x3zo7utx,cjy62zee,zxa3kx7e,zxa3kx7e)
  self.uc1xi04b=False
  self.ra73jgzl=[]
  self.i0x65muf=self.p7b1ijiy
  self.ljk4q5v7=[]
  self.mctwjlsh=0
  self.zflv1xxl=0
 def mmn32u1i(self,player):
  if self.nvuprt77<=0:
   self.uc1xi04b=True
   return
  if self.mctwjlsh!=0 or self.zflv1xxl!=0:
   self.tby49e7e.x3zo7utx+=self.mctwjlsh
   self.tby49e7e.cjy62zee+=self.zflv1xxl
   if self.mctwjlsh>0:
    self.mctwjlsh=max(0,self.mctwjlsh-1)
   elif self.mctwjlsh<0:
    self.mctwjlsh=min(0,self.mctwjlsh+1)
   if self.zflv1xxl>0:
    self.zflv1xxl=max(0,self.zflv1xxl-1)
   elif self.zflv1xxl<0:
    self.zflv1xxl=min(0,self.zflv1xxl+1)
   self.tby49e7e.x3zo7utx=round(self.tby49e7e.x3zo7utx)
   self.tby49e7e.cjy62zee=round(self.tby49e7e.cjy62zee)
  if abs(player.tby49e7e.x3zo7utx-self.tby49e7e.x3zo7utx)<cawudtse and abs(player.tby49e7e.cjy62zee-self.tby49e7e.cjy62zee)<cawudtse:
   self.sv5f1bcp(player)
   return
  if self.qic1l7dy(player):
   return
  pbo119xp=player.tby49e7e.x3zo7utx-self.tby49e7e.x3zo7utx
  mq7nc85e=player.tby49e7e.cjy62zee-self.tby49e7e.cjy62zee
  zefqjg02=math.hypot(pbo119xp,mq7nc85e)
  yjr0fzau=pbo119xp/zefqjg02
  vsjchzjq=mq7nc85e/zefqjg02
  if yjr0fzau!=0 and vsjchzjq!=0:
   yjr0fzau*=0.707
   vsjchzjq*=0.707
  self.tby49e7e.x3zo7utx+=yjr0fzau*self.p7b1ijiy
  self.tby49e7e.cjy62zee+=vsjchzjq*self.p7b1ijiy
  self.tby49e7e.x3zo7utx=round(self.tby49e7e.x3zo7utx)
  self.tby49e7e.cjy62zee=round(self.tby49e7e.cjy62zee)
 def sld4d6af(self,p7pchcbn,x3zo7utx,cjy62zee,rmm1zxyv,g8kk791z):
  p7pchcbn.blit(l55nf4zw,(rmm1zxyv-l55nf4zw.get_width()//2,cjy62zee+self.tby49e7e.height-6))
  yw6zbnz8=pygame.Rect(x3zo7utx,cjy62zee,self.tby49e7e.width,self.tby49e7e.height)
  pygame.draw.rect(p7pchcbn,gxlk8wru(self.k7zgf9q5,0.6),yw6zbnz8,border_radius=6)
  wa45hvgo=yw6zbnz8.inflate(-5,-5)
  pygame.draw.rect(p7pchcbn,self.k7zgf9q5,wa45hvgo,border_radius=5)
  pygame.draw.rect(p7pchcbn,(15,15,15),yw6zbnz8,width=2,border_radius=6)
  pygame.draw.circle(p7pchcbn,iq5c34dx['edxoq2'],(rmm1zxyv-6,g8kk791z-3),3)
  pygame.draw.circle(p7pchcbn,iq5c34dx['edxoq2'],(rmm1zxyv+6,g8kk791z-3),3)
  pygame.draw.circle(p7pchcbn,iq5c34dx['p4ta5i'],(rmm1zxyv-6,g8kk791z-3),1)
  pygame.draw.circle(p7pchcbn,iq5c34dx['p4ta5i'],(rmm1zxyv+6,g8kk791z-3),1)
  tj0nmeoq=self.nvuprt77/self.zsw2292m
  b36htf4p(p7pchcbn,x3zo7utx,cjy62zee-8,self.tby49e7e.width,tj0nmeoq,height=4)
 def dw7nh8rq(self,uwxrum2l,uos0fb4y,obc2nnuv):
  x3zo7utx=self.tby49e7e.x3zo7utx-uos0fb4y
  cjy62zee=self.tby49e7e.cjy62zee-obc2nnuv
  rmm1zxyv=self.tby49e7e.centerx-uos0fb4y
  g8kk791z=self.tby49e7e.centery-obc2nnuv
  self.sld4d6af(uwxrum2l,x3zo7utx,cjy62zee,rmm1zxyv,g8kk791z)
 def sv5f1bcp(self,player):
  if self.nrpj1epk>0:
   self.nrpj1epk-=1
   return
  self.nrpj1epk=self.llxxezdu
  yjluujmi=self.mygfliji*(100/(100+player.l57p6bkl))
  player.nvuprt77-=yjluujmi
  player.ljk4q5v7.append((player.tby49e7e.centerx,player.tby49e7e.cjy62zee,f'-{int(yjluujmi)}',iq5c34dx['zmygy0']))
  player.q3n2qb6g=True
  player.qcd81twh=s8qjnv8z
 def qic1l7dy(self,player):
  return False
 def njxurgow(self,player,ao4izasn,xuu13i59):
  pass
 def je11e9ft(self,xuu13i59):
  if k1wj0tpa[self.type].get('vcw2lb'):
   return 1.0
  for g5hcbbmh in xuu13i59:
   if g5hcbbmh.uc1xi04b:
    continue
   xxkdq95g=k1wj0tpa[g5hcbbmh.type]
   if not xxkdq95g.get('vcw2lb'):
    continue
   jqxs6esj=math.hypot(g5hcbbmh.tby49e7e.centerx-self.tby49e7e.centerx,g5hcbbmh.tby49e7e.centery-self.tby49e7e.centery)
   if jqxs6esj<=xxkdq95g['e0s41k']:
    return 1-xxkdq95g['qc6dr0']
  return 1.0
