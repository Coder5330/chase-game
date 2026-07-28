import pygame
import math
from v7bnhjw6 import*
from.czvky2re import qertb74r,fo75rh8l
pygame.init()
qqu7eeqt=pygame.Surface((rv86wzs3+16,14),pygame.SRCALPHA)
pygame.draw.ellipse(qqu7eeqt,(0,0,0,90),qqu7eeqt.get_rect())
def uc1xi04b(gg7oq2zd,jenvg3kk,sne6loh2=120,g1g1r1dw=10):
 holeyrvx=pygame.Surface((jenvg3kk.width,jenvg3kk.height),pygame.SRCALPHA)
 pygame.draw.rect(holeyrvx,(255,255,255,sne6loh2),holeyrvx.get_rect(),border_radius=g1g1r1dw)
 gg7oq2zd.blit(holeyrvx,jenvg3kk.topleft)
class r0tvhhpb:
 def __init__(self,meta_upgrades=None):
  meta_upgrades=meta_upgrades or{}
  gqq4d3kz=meta_upgrades.get('START_HEALTH',0)
  mnwxuj3a=meta_upgrades.get('START_SPEED',0)
  zo3lqi7e=meta_upgrades.get('START_DAMAGE',0)
  qo6q0usw=meta_upgrades.get('START_COOLDOWN',0)
  hp89fkbi=meta_upgrades.get('START_ARMOR',0)
  dq2fa39e=meta_upgrades.get('START_REGEN',0)
  self.vvslh9bh=rqf5q14j*chx3d43e(mnwxuj3a)
  self.xvzc7d2k=self.vvslh9bh
  self.jenvg3kk=pygame.Rect((cqoldfor-rv86wzs3)//2,(ygspk9p3-rv86wzs3)//2,rv86wzs3,rv86wzs3)
  self.lztkkfzz=iq5c34dx['m314cq']
  self.c0hpmnz1=int(1000*tb4ldims(gqq4d3kz))
  self.y2f7atwy=self.c0hpmnz1
  self.mn7h9g1a=self.c0hpmnz1
  self.nngmx1gm=0
  self.o4dd1vn8=1
  self.qxb7gbdg=False
  self.fpa8hyex={'e56waf':0,'eqkwqh':self.xvzc7d2k}
  self.d5ixva1n={}
  self.tza7x73q={key:0 for key in yswjckjl}
  self.ykipu1wy=yvffqot8(zo3lqi7e)
  self.duhxid4n=mcup8ijl(qo6q0usw)
  self.x03uvule=a8ax40dt(hp89fkbi)
  self.nrpj1epk=vk3g84ut(dq2fa39e)
  self.cnqt3wve=self.ykipu1wy
  self.oqse3tv1=self.duhxid4n
  self.ceb8753a=1.0
  self.wkof8krd=self.x03uvule
  self.xsspye9r=self.nrpj1epk
  self.yg87oi0e=pi3qk2ia
  self.k8qeoz0k=False
  self.wtl0thhz=0
  self.zflse45b=[]
  self.xd8wz42o=0
  self.n3rlkte4=0
  self.eatvzkhi=pygame.font.SysFont('arial',20,bold=True)
 def on0jnwny(self,key):
  self.tza7x73q[key]+=1
  jxxgaear=self.tza7x73q[key]
  if key=='xu7dkn':
   d448n7od=int(self.c0hpmnz1*(1+0.2*jxxgaear))
   self.mn7h9g1a+=d448n7od-self.y2f7atwy
   self.y2f7atwy=d448n7od
  elif key=='rthy25':
   self.xvzc7d2k=self.vvslh9bh*(1+0.08*jxxgaear)
  elif key=='clslay':
   self.xsspye9r=self.nrpj1epk+jxxgaear
  elif key=='n8k03w':
   self.cnqt3wve=self.ykipu1wy*(1+0.06*jxxgaear)
  elif key=='w66p61':
   self.oqse3tv1=self.duhxid4n*max(0.6,1-0.05*jxxgaear)
  elif key=='da5xin':
   self.wkof8krd=self.x03uvule+jxxgaear*5
  elif key=='da7yvd':
   self.ceb8753a=1+0.15*jxxgaear
 def wa45hvgo(self,hjkuuhcl):
  self.d5ixva1n[hjkuuhcl]=self.d5ixva1n.get(hjkuuhcl,1)+1
 def r2muljav(self):
  swwnc21o=pygame.key.get_pressed()
  x875aud9=jqxs6esj=0
  if swwnc21o[pygame.K_UP]:
   jqxs6esj-=self.xvzc7d2k
  if swwnc21o[pygame.K_DOWN]:
   jqxs6esj+=self.xvzc7d2k
  if swwnc21o[pygame.K_LEFT]:
   x875aud9-=self.xvzc7d2k
  if swwnc21o[pygame.K_RIGHT]:
   x875aud9+=self.xvzc7d2k
  if x875aud9!=0 and jqxs6esj!=0:
   x875aud9*=0.707
   jqxs6esj*=0.707
  if x875aud9!=0 or jqxs6esj!=0:
   self.fpa8hyex['e56waf']=x875aud9
   self.fpa8hyex['eqkwqh']=jqxs6esj
  self.jenvg3kk.qic1l7dy+=x875aud9+self.xd8wz42o
  self.jenvg3kk.vsjchzjq+=jqxs6esj+self.n3rlkte4
  if self.xd8wz42o>0:
   self.xd8wz42o=max(0,self.xd8wz42o-1)
  elif self.xd8wz42o<0:
   self.xd8wz42o=min(0,self.xd8wz42o+1)
  if self.n3rlkte4>0:
   self.n3rlkte4=max(0,self.n3rlkte4-1)
  elif self.n3rlkte4<0:
   self.n3rlkte4=min(0,self.n3rlkte4+1)
  self.jenvg3kk.qic1l7dy=max(min(self.jenvg3kk.qic1l7dy,cqoldfor-self.jenvg3kk.width),0)
  self.jenvg3kk.vsjchzjq=max(min(self.jenvg3kk.vsjchzjq,ygspk9p3-self.jenvg3kk.height),0)
  if self.xsspye9r>0 and self.mn7h9g1a<self.y2f7atwy:
   self.yg87oi0e-=1
   if self.yg87oi0e<=0:
    self.yg87oi0e=pi3qk2ia
    self.mn7h9g1a=min(self.y2f7atwy,self.mn7h9g1a+self.xsspye9r)
  if self.nngmx1gm>=v83tqll8[min(self.o4dd1vn8,len(v83tqll8)-1)]:
   self.qxb7gbdg=True
   self.nngmx1gm=0
   self.o4dd1vn8+=1
 def wc7x0h3j(self,gg7oq2zd,li9nb74x,zfb7r31q):
  qic1l7dy=self.jenvg3kk.qic1l7dy-li9nb74x
  vsjchzjq=self.jenvg3kk.vsjchzjq-zfb7r31q
  pa8s8hmb=self.jenvg3kk.centerx-li9nb74x
  pv4ykade=self.jenvg3kk.centery-zfb7r31q
  gg7oq2zd.blit(qqu7eeqt,(pa8s8hmb-qqu7eeqt.get_width()//2,vsjchzjq+self.jenvg3kk.height-8))
  fcwtg1m8=pygame.Rect(qic1l7dy,vsjchzjq,self.jenvg3kk.width,self.jenvg3kk.height)
  pygame.draw.rect(gg7oq2zd,qertb74r(self.lztkkfzz,0.55),fcwtg1m8,border_radius=10)
  rktlzkj4=fcwtg1m8.inflate(-5,-5)
  pygame.draw.rect(gg7oq2zd,self.lztkkfzz,rktlzkj4,border_radius=8)
  z8z3v6di=pygame.Rect(rktlzkj4.qic1l7dy+3,rktlzkj4.vsjchzjq+3,rktlzkj4.width//2,rktlzkj4.height//3)
  pygame.draw.rect(gg7oq2zd,qertb74r(self.lztkkfzz,2.0),z8z3v6di,border_radius=4)
  pygame.draw.rect(gg7oq2zd,(15,15,30),fcwtg1m8,width=2,border_radius=10)
  avfmh07w=math.hypot(self.fpa8hyex['e56waf'],self.fpa8hyex['eqkwqh'])or 1
  (k3z6bz8u,s8438tgb)=(self.fpa8hyex['e56waf']/avfmh07w,self.fpa8hyex['eqkwqh']/avfmh07w)
  njka34mq=(pa8s8hmb+k3z6bz8u*20,pv4ykade+s8438tgb*20)
  pcvsqame=(pa8s8hmb-s8438tgb*7+k3z6bz8u*4,pv4ykade+k3z6bz8u*7+s8438tgb*4)
  tj0nmeoq=(pa8s8hmb+s8438tgb*7+k3z6bz8u*4,pv4ykade-k3z6bz8u*7+s8438tgb*4)
  pygame.draw.polygon(gg7oq2zd,iq5c34dx['v9hbn5'],[njka34mq,pcvsqame,tj0nmeoq])
  pygame.draw.polygon(gg7oq2zd,(15,15,30),[njka34mq,pcvsqame,tj0nmeoq],width=1)
  upprat08=self.mn7h9g1a/self.y2f7atwy
  fo75rh8l(gg7oq2zd,qic1l7dy,vsjchzjq-10,self.jenvg3kk.width,upprat08,height=6)
  uc1xi04b(gg7oq2zd,pygame.Rect(225,12,372,40))
  holeyrvx=self.eatvzkhi.render('Hp.',True,(20,20,20))
  gg7oq2zd.blit(holeyrvx,(233,23))
  fo75rh8l(gg7oq2zd,297,25,290,upprat08,height=19)
  holeyrvx=self.eatvzkhi.render(f'{round(self.mn7h9g1a)}/{self.y2f7atwy}',True,(20,20,20))
  width=holeyrvx.get_width()
  height=holeyrvx.get_height()
  gg7oq2zd.blit(holeyrvx,(442-width//2,34.5-height//2))
