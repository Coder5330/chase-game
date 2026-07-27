import pygame
import math
from o100vhmy import*
from.mipwh0mx import xwk2rv23,qbbz2sf6
pygame.init()
l55nf4zw=pygame.Surface((zxa3kx7e+12,12),pygame.SRCALPHA)
pygame.draw.ellipse(l55nf4zw,(0,0,0,80),l55nf4zw.get_rect())
class f935a0l7:
 def __init__(self,uc1xi04b,rm0j36tc,tza7x73q):
  self.type=uc1xi04b
  self.q7i6yuj7=k1wj0tpa[self.type]['l226pa']
  self.k2ixivzk=k1wj0tpa[self.type]['l226pa']
  self.k7zgf9q5=k1wj0tpa[self.type]['jl1qwe']
  self.k8qeoz0k=k1wj0tpa[self.type]['fkmuso']
  self.rk8r2ykc=k1wj0tpa[self.type]['r3hxyj']
  self.ebt3g2qz=k1wj0tpa[self.type]['xu7dkn']
  self.eq3tq1s0=k1wj0tpa[self.type]['edxoq2']
  self.nqimqodp=k1wj0tpa[self.type]['e8a1ar']
  self.lt63j3r3=k1wj0tpa[self.type]['e8a1ar']
  self.zflse45b=pygame.Rect(rm0j36tc,tza7x73q,zxa3kx7e,zxa3kx7e)
  self.vw6m7b5c=False
  self.ia529603=[]
  self.tp2ex5t5=self.k8qeoz0k
  self.mmn32u1i=[]
 def j1ldqnk2(self,player):
  if self.q7i6yuj7<=0:
   self.vw6m7b5c=True
   return
  if abs(player.zflse45b.rm0j36tc-self.zflse45b.rm0j36tc)<cawudtse and abs(player.zflse45b.tza7x73q-self.zflse45b.tza7x73q)<cawudtse:
   self.sne6loh2(player)
   return
  if self.mlikwe4b(player):
   return
  sl65wvjx=player.zflse45b.rm0j36tc-self.zflse45b.rm0j36tc
  yuibrsz1=player.zflse45b.tza7x73q-self.zflse45b.tza7x73q
  l9enulqj=math.hypot(sl65wvjx,yuibrsz1)
  njka34mq=sl65wvjx/l9enulqj
  ayr1k12v=yuibrsz1/l9enulqj
  if njka34mq!=0 and ayr1k12v!=0:
   njka34mq*=0.707
   ayr1k12v*=0.707
  self.zflse45b.rm0j36tc+=njka34mq*self.k8qeoz0k
  self.zflse45b.tza7x73q+=ayr1k12v*self.k8qeoz0k
  self.zflse45b.rm0j36tc=round(self.zflse45b.rm0j36tc)
  self.zflse45b.tza7x73q=round(self.zflse45b.tza7x73q)
 def rrcbpljd(self,uoloeazc,rm0j36tc,tza7x73q,lztkkfzz,f2sehe2a):
  uoloeazc.blit(l55nf4zw,(lztkkfzz-l55nf4zw.get_width()//2,tza7x73q+self.zflse45b.height-6))
  ykipu1wy=pygame.Rect(rm0j36tc,tza7x73q,self.zflse45b.width,self.zflse45b.height)
  pygame.draw.rect(uoloeazc,xwk2rv23(self.ebt3g2qz,0.6),ykipu1wy,border_radius=6)
  we4xyf9i=ykipu1wy.inflate(-5,-5)
  pygame.draw.rect(uoloeazc,self.ebt3g2qz,we4xyf9i,border_radius=5)
  pygame.draw.rect(uoloeazc,(15,15,15),ykipu1wy,width=2,border_radius=6)
  pygame.draw.circle(uoloeazc,iq5c34dx['ldz09w'],(lztkkfzz-6,f2sehe2a-3),3)
  pygame.draw.circle(uoloeazc,iq5c34dx['ldz09w'],(lztkkfzz+6,f2sehe2a-3),3)
  pygame.draw.circle(uoloeazc,iq5c34dx['vpd2ts'],(lztkkfzz-6,f2sehe2a-3),1)
  pygame.draw.circle(uoloeazc,iq5c34dx['vpd2ts'],(lztkkfzz+6,f2sehe2a-3),1)
  he9p3jpx=self.q7i6yuj7/self.k2ixivzk
  qbbz2sf6(uoloeazc,rm0j36tc,tza7x73q-8,self.zflse45b.width,he9p3jpx,height=4)
 def i01nouht(self,npejzhya,kybwmlun,i0x65muf):
  rm0j36tc=self.zflse45b.rm0j36tc-kybwmlun
  tza7x73q=self.zflse45b.tza7x73q-i0x65muf
  lztkkfzz=self.zflse45b.centerx-kybwmlun
  f2sehe2a=self.zflse45b.centery-i0x65muf
  self.rrcbpljd(npejzhya,rm0j36tc,tza7x73q,lztkkfzz,f2sehe2a)
 def sne6loh2(self,player):
  if self.lt63j3r3>0:
   self.lt63j3r3-=1
   return
  self.lt63j3r3=self.nqimqodp
  pa8s8hmb=self.k7zgf9q5*(100/(100+player.iy6qktc8))
  player.q7i6yuj7-=pa8s8hmb
  player.mmn32u1i.append((player.zflse45b.centerx,player.zflse45b.tza7x73q,f'-{int(pa8s8hmb)}',iq5c34dx['wxgnrf']))
  player.qc06xq9j=True
  player.bdgbk2l0=yur7ko64
 def mlikwe4b(self,player):
  return False
 def lhgk5bwi(self,player,velos6zl,wzlm72je):
  pass
 def zpajssuu(self,wzlm72je):
  if k1wj0tpa[self.type].get('iwu3bf'):
   return 1.0
  for k3z6bz8u in wzlm72je:
   if k3z6bz8u.vw6m7b5c:
    continue
   mn89ltaj=k1wj0tpa[k3z6bz8u.type]
   if not mn89ltaj.get('iwu3bf'):
    continue
   bfoqmf5l=math.hypot(k3z6bz8u.zflse45b.centerx-self.zflse45b.centerx,k3z6bz8u.zflse45b.centery-self.zflse45b.centery)
   if bfoqmf5l<=mn89ltaj['pta5iv']:
    return 1-mn89ltaj['pqpva5']
  return 1.0
