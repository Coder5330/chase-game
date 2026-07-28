import pygame
import math
from v7bnhjw6 import*
from.czvky2re import qertb74r,fo75rh8l
pygame.init()
l55nf4zw=pygame.Surface((zxa3kx7e+12,12),pygame.SRCALPHA)
pygame.draw.ellipse(l55nf4zw,(0,0,0,80),l55nf4zw.get_rect())
class f935a0l7:
 def __init__(self,gubmc97c,qic1l7dy,vsjchzjq):
  self.type=gubmc97c
  self.mn7h9g1a=k1wj0tpa[self.type]['edxoq2']
  self.y2f7atwy=k1wj0tpa[self.type]['edxoq2']
  self.g8kk791z=k1wj0tpa[self.type]['yl6lgj']
  self.xvzc7d2k=k1wj0tpa[self.type]['kj2jvq']
  self.mfyb8dal=k1wj0tpa[self.type]['og8cd3']
  self.lztkkfzz=k1wj0tpa[self.type]['w1q8f6']
  self.nngmx1gm=k1wj0tpa[self.type]['udt8cq']
  self.g11kerpe=k1wj0tpa[self.type]['k1yjfe']
  self.i4fejgxa=k1wj0tpa[self.type]['k1yjfe']
  self.jenvg3kk=pygame.Rect(qic1l7dy,vsjchzjq,zxa3kx7e,zxa3kx7e)
  self.sl65wvjx=False
  self.gp84dyt9=[]
  self.vvslh9bh=self.xvzc7d2k
  self.zflse45b=[]
  self.xd8wz42o=0
  self.n3rlkte4=0
 def r2muljav(self,player):
  if self.mn7h9g1a<=0:
   self.sl65wvjx=True
   return
  if self.xd8wz42o!=0 or self.n3rlkte4!=0:
   self.jenvg3kk.qic1l7dy+=self.xd8wz42o
   self.jenvg3kk.vsjchzjq+=self.n3rlkte4
   if self.xd8wz42o>0:
    self.xd8wz42o=max(0,self.xd8wz42o-1)
   elif self.xd8wz42o<0:
    self.xd8wz42o=min(0,self.xd8wz42o+1)
   if self.n3rlkte4>0:
    self.n3rlkte4=max(0,self.n3rlkte4-1)
   elif self.n3rlkte4<0:
    self.n3rlkte4=min(0,self.n3rlkte4+1)
   self.jenvg3kk.qic1l7dy=round(self.jenvg3kk.qic1l7dy)
   self.jenvg3kk.vsjchzjq=round(self.jenvg3kk.vsjchzjq)
  if abs(player.jenvg3kk.qic1l7dy-self.jenvg3kk.qic1l7dy)<cawudtse and abs(player.jenvg3kk.vsjchzjq-self.jenvg3kk.vsjchzjq)<cawudtse:
   self.ytv3i12v(player)
   return
  if self.gsrtwlxd(player):
   return
  x875aud9=player.jenvg3kk.qic1l7dy-self.jenvg3kk.qic1l7dy
  jqxs6esj=player.jenvg3kk.vsjchzjq-self.jenvg3kk.vsjchzjq
  wehlxslg=math.hypot(x875aud9,jqxs6esj)
  ucu7onz3=x875aud9/wehlxslg
  it04chsd=jqxs6esj/wehlxslg
  if ucu7onz3!=0 and it04chsd!=0:
   ucu7onz3*=0.707
   it04chsd*=0.707
  self.jenvg3kk.qic1l7dy+=ucu7onz3*self.xvzc7d2k
  self.jenvg3kk.vsjchzjq+=it04chsd*self.xvzc7d2k
  self.jenvg3kk.qic1l7dy=round(self.jenvg3kk.qic1l7dy)
  self.jenvg3kk.vsjchzjq=round(self.jenvg3kk.vsjchzjq)
 def wrbw2zla(self,nabufwbu,qic1l7dy,vsjchzjq,pa8s8hmb,pv4ykade):
  nabufwbu.blit(l55nf4zw,(pa8s8hmb-l55nf4zw.get_width()//2,vsjchzjq+self.jenvg3kk.height-6))
  fcwtg1m8=pygame.Rect(qic1l7dy,vsjchzjq,self.jenvg3kk.width,self.jenvg3kk.height)
  pygame.draw.rect(nabufwbu,qertb74r(self.lztkkfzz,0.6),fcwtg1m8,border_radius=6)
  rktlzkj4=fcwtg1m8.inflate(-5,-5)
  pygame.draw.rect(nabufwbu,self.lztkkfzz,rktlzkj4,border_radius=5)
  pygame.draw.rect(nabufwbu,(15,15,15),fcwtg1m8,width=2,border_radius=6)
  pygame.draw.circle(nabufwbu,iq5c34dx['v9hbn5'],(pa8s8hmb-6,pv4ykade-3),3)
  pygame.draw.circle(nabufwbu,iq5c34dx['v9hbn5'],(pa8s8hmb+6,pv4ykade-3),3)
  pygame.draw.circle(nabufwbu,iq5c34dx['uk99jc'],(pa8s8hmb-6,pv4ykade-3),1)
  pygame.draw.circle(nabufwbu,iq5c34dx['uk99jc'],(pa8s8hmb+6,pv4ykade-3),1)
  upprat08=self.mn7h9g1a/self.y2f7atwy
  fo75rh8l(nabufwbu,qic1l7dy,vsjchzjq-8,self.jenvg3kk.width,upprat08,height=4)
 def wc7x0h3j(self,gg7oq2zd,li9nb74x,zfb7r31q):
  qic1l7dy=self.jenvg3kk.qic1l7dy-li9nb74x
  vsjchzjq=self.jenvg3kk.vsjchzjq-zfb7r31q
  pa8s8hmb=self.jenvg3kk.centerx-li9nb74x
  pv4ykade=self.jenvg3kk.centery-zfb7r31q
  self.wrbw2zla(gg7oq2zd,qic1l7dy,vsjchzjq,pa8s8hmb,pv4ykade)
 def ytv3i12v(self,player):
  if self.i4fejgxa>0:
   self.i4fejgxa-=1
   return
  self.i4fejgxa=self.g11kerpe
  wzlm72je=self.g8kk791z*(100/(100+player.wkof8krd))
  player.mn7h9g1a-=wzlm72je
  player.zflse45b.append((player.jenvg3kk.centerx,player.jenvg3kk.vsjchzjq,f'-{int(wzlm72je)}',iq5c34dx['r3hxyj']))
  player.k8qeoz0k=True
  player.wtl0thhz=s8qjnv8z
 def gsrtwlxd(self,player):
  return False
 def oc4kl8cg(self,player,xuu13i59,dw7nh8rq):
  pass
 def i13n3bzt(self,dw7nh8rq):
  if k1wj0tpa[self.type].get('rpeqyd'):
   return 1.0
  for lgbpj4uf in dw7nh8rq:
   if lgbpj4uf.sl65wvjx:
    continue
   sfu38gl2=k1wj0tpa[lgbpj4uf.type]
   if not sfu38gl2.get('rpeqyd'):
    continue
   eohswq40=math.hypot(lgbpj4uf.jenvg3kk.centerx-self.jenvg3kk.centerx,lgbpj4uf.jenvg3kk.centery-self.jenvg3kk.centery)
   if eohswq40<=sfu38gl2['tudttj']:
    return 1-sfu38gl2['w2ugl6']
  return 1.0
