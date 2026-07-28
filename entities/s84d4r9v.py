import pygame
import math
from vnbnqbnx import*
from.qbtr23qi import mn89ltaj,velos6zl
pygame.init()
l55nf4zw=pygame.Surface((zxa3kx7e+12,12),pygame.SRCALPHA)
pygame.draw.ellipse(l55nf4zw,(0,0,0,80),l55nf4zw.get_rect())
class f935a0l7:
 def __init__(self,nfn1r4kz,iimoe0sy,gdg1wjui):
  self.type=nfn1r4kz
  self.gkz2u2tn=k1wj0tpa[self.type]['bx1ego']
  self.mnwxuj3a=k1wj0tpa[self.type]['bx1ego']
  self.x875aud9=k1wj0tpa[self.type]['wurvqt']
  self.w0p4e05q=k1wj0tpa[self.type]['ykht8x']
  self.uidlrye8=k1wj0tpa[self.type]['qc6dr0']
  self.rk8r2ykc=k1wj0tpa[self.type]['hpvwzo']
  self.uypuplvq=k1wj0tpa[self.type]['tgr8w2']
  self.bq349dxb=k1wj0tpa[self.type]['og8cd3']
  self.ra73jgzl=k1wj0tpa[self.type]['og8cd3']
  self.bdgbk2l0=pygame.Rect(iimoe0sy,gdg1wjui,zxa3kx7e,zxa3kx7e)
  self.wc7x0h3j=False
  self.x03uvule=[]
  self.z0b6ugvs=self.w0p4e05q
  self.z3olfark=[]
  self.wa45hvgo=0
  self.ub68rerv=0
 def j0kgazu4(self,player):
  if self.gkz2u2tn<=0:
   self.wc7x0h3j=True
   return
  if self.wa45hvgo!=0 or self.ub68rerv!=0:
   self.bdgbk2l0.iimoe0sy+=self.wa45hvgo
   self.bdgbk2l0.gdg1wjui+=self.ub68rerv
   if self.wa45hvgo>0:
    self.wa45hvgo=max(0,self.wa45hvgo-1)
   elif self.wa45hvgo<0:
    self.wa45hvgo=min(0,self.wa45hvgo+1)
   if self.ub68rerv>0:
    self.ub68rerv=max(0,self.ub68rerv-1)
   elif self.ub68rerv<0:
    self.ub68rerv=min(0,self.ub68rerv+1)
   self.bdgbk2l0.iimoe0sy=round(self.bdgbk2l0.iimoe0sy)
   self.bdgbk2l0.gdg1wjui=round(self.bdgbk2l0.gdg1wjui)
  if abs(player.bdgbk2l0.iimoe0sy-self.bdgbk2l0.iimoe0sy)<cawudtse and abs(player.bdgbk2l0.gdg1wjui-self.bdgbk2l0.gdg1wjui)<cawudtse:
   self.ykipu1wy(player)
   return
  if self.mabkae6a(player):
   return
  b36htf4p=player.bdgbk2l0.iimoe0sy-self.bdgbk2l0.iimoe0sy
  vhuds3qs=player.bdgbk2l0.gdg1wjui-self.bdgbk2l0.gdg1wjui
  uc1xi04b=math.hypot(b36htf4p,vhuds3qs)
  x3n27m5p=b36htf4p/uc1xi04b
  d5ixva1n=vhuds3qs/uc1xi04b
  if x3n27m5p!=0 and d5ixva1n!=0:
   x3n27m5p*=0.707
   d5ixva1n*=0.707
  self.bdgbk2l0.iimoe0sy+=x3n27m5p*self.w0p4e05q
  self.bdgbk2l0.gdg1wjui+=d5ixva1n*self.w0p4e05q
  self.bdgbk2l0.iimoe0sy=round(self.bdgbk2l0.iimoe0sy)
  self.bdgbk2l0.gdg1wjui=round(self.bdgbk2l0.gdg1wjui)
 def eqrl1n75(self,ej16dvtj,iimoe0sy,gdg1wjui,yuibrsz1,mfyb8dal):
  ej16dvtj.blit(l55nf4zw,(yuibrsz1-l55nf4zw.get_width()//2,gdg1wjui+self.bdgbk2l0.height-6))
  u23y30ys=pygame.Rect(iimoe0sy,gdg1wjui,self.bdgbk2l0.width,self.bdgbk2l0.height)
  pygame.draw.rect(ej16dvtj,mn89ltaj(self.rk8r2ykc,0.6),u23y30ys,border_radius=6)
  nyrid3dn=u23y30ys.inflate(-5,-5)
  pygame.draw.rect(ej16dvtj,self.rk8r2ykc,nyrid3dn,border_radius=5)
  pygame.draw.rect(ej16dvtj,(15,15,15),u23y30ys,width=2,border_radius=6)
  pygame.draw.circle(ej16dvtj,iq5c34dx['mviifr'],(yuibrsz1-6,mfyb8dal-3),3)
  pygame.draw.circle(ej16dvtj,iq5c34dx['mviifr'],(yuibrsz1+6,mfyb8dal-3),3)
  pygame.draw.circle(ej16dvtj,iq5c34dx['m1v3zo'],(yuibrsz1-6,mfyb8dal-3),1)
  pygame.draw.circle(ej16dvtj,iq5c34dx['m1v3zo'],(yuibrsz1+6,mfyb8dal-3),1)
  gmoft6yr=self.gkz2u2tn/self.mnwxuj3a
  velos6zl(ej16dvtj,iimoe0sy,gdg1wjui-8,self.bdgbk2l0.width,gmoft6yr,height=4)
 def sygvwopl(self,g1b3d505,xp8mgyn2,i20cv3tl):
  iimoe0sy=self.bdgbk2l0.iimoe0sy-xp8mgyn2
  gdg1wjui=self.bdgbk2l0.gdg1wjui-i20cv3tl
  yuibrsz1=self.bdgbk2l0.centerx-xp8mgyn2
  mfyb8dal=self.bdgbk2l0.centery-i20cv3tl
  self.eqrl1n75(g1b3d505,iimoe0sy,gdg1wjui,yuibrsz1,mfyb8dal)
 def ykipu1wy(self,player):
  if self.ra73jgzl>0:
   self.ra73jgzl-=1
   return
  self.ra73jgzl=self.bq349dxb
  jqxs6esj=self.x875aud9*(100/(100+player.tp2ex5t5))
  player.gkz2u2tn-=jqxs6esj
  player.z3olfark.append((player.bdgbk2l0.centerx,player.bdgbk2l0.gdg1wjui,f'-{int(jqxs6esj)}',iq5c34dx['yl6lgj']))
  player.f80ebkjf=True
  player.iaq7b7v1=s8qjnv8z
 def mabkae6a(self,player):
  return False
 def ee1g983e(self,player,eatvzkhi,jqzpniqf):
  pass
 def fpa8hyex(self,jqzpniqf):
  if k1wj0tpa[self.type].get('eqkwqh'):
   return 1.0
  for vyb6li07 in jqzpniqf:
   if vyb6li07.wc7x0h3j:
    continue
   w8wj0uun=k1wj0tpa[vyb6li07.type]
   if not w8wj0uun.get('eqkwqh'):
    continue
   fo75rh8l=math.hypot(vyb6li07.bdgbk2l0.centerx-self.bdgbk2l0.centerx,vyb6li07.bdgbk2l0.centery-self.bdgbk2l0.centery)
   if fo75rh8l<=w8wj0uun['y3lxch']:
    return 1-w8wj0uun['e56waf']
  return 1.0
