import pygame
import math
from omerbyea import*
from.j1bmqf7z import u15pdtz9,vhuds3qs
pygame.init()
rv86wzs3=pygame.Surface((rqf5q14j+16,14),pygame.SRCALPHA)
pygame.draw.ellipse(rv86wzs3,(0,0,0,90),rv86wzs3.get_rect())
def ouuylaja(q3n2qb6g,cq2q4qer,am2vajep=120,xu9ymszd=10):
 gqoagsus=pygame.Surface((cq2q4qer.width,cq2q4qer.height),pygame.SRCALPHA)
 pygame.draw.rect(gqoagsus,(255,255,255,am2vajep),gqoagsus.get_rect(),border_radius=xu9ymszd)
 q3n2qb6g.blit(gqoagsus,cq2q4qer.topleft)
class ky20479t:
 def __init__(self,meta_upgrades=None):
  meta_upgrades=meta_upgrades or{}
  w8y72ivg=meta_upgrades.get('START_HEALTH',0)
  wy0mahym=meta_upgrades.get('START_SPEED',0)
  d448n7od=meta_upgrades.get('START_DAMAGE',0)
  bihsa7he=meta_upgrades.get('START_COOLDOWN',0)
  s8438tgb=meta_upgrades.get('START_ARMOR',0)
  pf0i9g5d=meta_upgrades.get('START_REGEN',0)
  self.wppsfnko=yswjckjl*zdan085r(wy0mahym)
  self.holeyrvx=self.wppsfnko
  self.cq2q4qer=pygame.Rect((m53a5qbs-rqf5q14j)//2,(v83tqll8-rqf5q14j)//2,rqf5q14j,rqf5q14j)
  self.k7zgf9q5=iq5c34dx['mviifr']
  self.jc54wsqt=int(1000*j0kgazu4(w8y72ivg))
  self.hu9n79gi=self.jc54wsqt
  self.arhnuxor=self.jc54wsqt
  self.cjy62zee=0
  self.y2f7atwy=1
  self.vsjchzjq=False
  self.d1b3jczu={'dzjq7w':0,'i1yy1j':self.holeyrvx}
  self.x3zo7utx={}
  self.un9sz6rv={key:0 for key in rcfnfhol}
  self.f8wquuy5=jl90pxrl(d448n7od)
  self.u3ifhv1x=wg25cfzf(bihsa7he)
  self.divsolml=k3z6bz8u(s8438tgb)
  self.bq349dxb=y8bv78hu(pf0i9g5d)
  self.wc7x0h3j=self.f8wquuy5
  self.cnqt3wve=self.u3ifhv1x
  self.rn16uxf5=1.0
  self.nqimqodp=self.divsolml
  self.uaobt328=self.bq349dxb
  self.ukshy8nb=pi3qk2ia
  self.uoloeazc=False
  self.xvzc7d2k=0
  self.upprat08=[]
  self.n04cdpqv=0
  self.jxxgaear=0
  self.mpyxdw2z=pygame.font.SysFont('arial',20,bold=True)
 def ejwtl9tq(self,key):
  self.un9sz6rv[key]+=1
  dq2fa39e=self.un9sz6rv[key]
  if key=='w2lx2t':
   ee1g983e=int(self.jc54wsqt*(1+0.2*dq2fa39e))
   self.arhnuxor+=ee1g983e-self.hu9n79gi
   self.hu9n79gi=ee1g983e
  elif key=='l4f9ye':
   self.holeyrvx=self.wppsfnko*(1+0.08*dq2fa39e)
  elif key=='w9mda9':
   self.uaobt328=self.bq349dxb+dq2fa39e
  elif key=='clslay':
   self.wc7x0h3j=self.f8wquuy5*(1+0.06*dq2fa39e)
  elif key=='wkgeq2':
   self.cnqt3wve=self.u3ifhv1x*max(0.6,1-0.05*dq2fa39e)
  elif key=='ffxb4y':
   self.nqimqodp=self.divsolml+dq2fa39e*5
  elif key=='vcw2lb':
   self.rn16uxf5=1+0.15*dq2fa39e
 def hp89fkbi(self,un4regb1):
  self.x3zo7utx[un4regb1]=self.x3zo7utx.get(un4regb1,1)+1
 def got7txkd(self):
  mctwjlsh=pygame.key.get_pressed()
  mq7nc85e=le9oe941=0
  if mctwjlsh[pygame.K_UP]:
   le9oe941-=self.holeyrvx
  if mctwjlsh[pygame.K_DOWN]:
   le9oe941+=self.holeyrvx
  if mctwjlsh[pygame.K_LEFT]:
   mq7nc85e-=self.holeyrvx
  if mctwjlsh[pygame.K_RIGHT]:
   mq7nc85e+=self.holeyrvx
  if mq7nc85e!=0 and le9oe941!=0:
   mq7nc85e*=0.707
   le9oe941*=0.707
  if mq7nc85e!=0 or le9oe941!=0:
   self.d1b3jczu['dzjq7w']=mq7nc85e
   self.d1b3jczu['i1yy1j']=le9oe941
  self.cq2q4qer.eolaq665+=mq7nc85e+self.n04cdpqv
  self.cq2q4qer.t5ivrocv+=le9oe941+self.jxxgaear
  if self.n04cdpqv>0:
   self.n04cdpqv=max(0,self.n04cdpqv-1)
  elif self.n04cdpqv<0:
   self.n04cdpqv=min(0,self.n04cdpqv+1)
  if self.jxxgaear>0:
   self.jxxgaear=max(0,self.jxxgaear-1)
  elif self.jxxgaear<0:
   self.jxxgaear=min(0,self.jxxgaear+1)
  self.cq2q4qer.eolaq665=max(min(self.cq2q4qer.eolaq665,m53a5qbs-self.cq2q4qer.width),0)
  self.cq2q4qer.t5ivrocv=max(min(self.cq2q4qer.t5ivrocv,v83tqll8-self.cq2q4qer.height),0)
  if self.uaobt328>0 and self.arhnuxor<self.hu9n79gi:
   self.ukshy8nb-=1
   if self.ukshy8nb<=0:
    self.ukshy8nb=pi3qk2ia
    self.arhnuxor=min(self.hu9n79gi,self.arhnuxor+self.uaobt328)
  if self.cjy62zee>=t1w1ht7p[min(self.y2f7atwy,len(t1w1ht7p)-1)]:
   self.vsjchzjq=True
   self.cjy62zee=0
   self.y2f7atwy+=1
 def tnz61231(self,q3n2qb6g,clkqzfpq,x5m9j98c):
  eolaq665=self.cq2q4qer.eolaq665-clkqzfpq
  t5ivrocv=self.cq2q4qer.t5ivrocv-x5m9j98c
  g8kk791z=self.cq2q4qer.centerx-clkqzfpq
  wzlm72je=self.cq2q4qer.centery-x5m9j98c
  q3n2qb6g.blit(rv86wzs3,(g8kk791z-rv86wzs3.get_width()//2,t5ivrocv+self.cq2q4qer.height-8))
  giec4d14=pygame.Rect(eolaq665,t5ivrocv,self.cq2q4qer.width,self.cq2q4qer.height)
  pygame.draw.rect(q3n2qb6g,u15pdtz9(self.k7zgf9q5,0.55),giec4d14,border_radius=10)
  q5amln4p=giec4d14.inflate(-5,-5)
  pygame.draw.rect(q3n2qb6g,self.k7zgf9q5,q5amln4p,border_radius=8)
  nd31k9qm=pygame.Rect(q5amln4p.eolaq665+3,q5amln4p.t5ivrocv+3,q5amln4p.width//2,q5amln4p.height//3)
  pygame.draw.rect(q3n2qb6g,u15pdtz9(self.k7zgf9q5,2.0),nd31k9qm,border_radius=4)
  pygame.draw.rect(q3n2qb6g,(15,15,30),giec4d14,width=2,border_radius=10)
  xwqvr1h6=math.hypot(self.d1b3jczu['dzjq7w'],self.d1b3jczu['i1yy1j'])or 1
  (lgbpj4uf,wydmt8vt)=(self.d1b3jczu['dzjq7w']/xwqvr1h6,self.d1b3jczu['i1yy1j']/xwqvr1h6)
  it04chsd=(g8kk791z+lgbpj4uf*20,wzlm72je+wydmt8vt*20)
  lnf74t60=(g8kk791z-wydmt8vt*7+lgbpj4uf*4,wzlm72je+lgbpj4uf*7+wydmt8vt*4)
  vmy9x8sy=(g8kk791z+wydmt8vt*7+lgbpj4uf*4,wzlm72je-lgbpj4uf*7+wydmt8vt*4)
  pygame.draw.polygon(q3n2qb6g,iq5c34dx['qc6dr0'],[it04chsd,lnf74t60,vmy9x8sy])
  pygame.draw.polygon(q3n2qb6g,(15,15,30),[it04chsd,lnf74t60,vmy9x8sy],width=1)
  v0rxxf36=self.arhnuxor/self.hu9n79gi
  vhuds3qs(q3n2qb6g,eolaq665,t5ivrocv-10,self.cq2q4qer.width,v0rxxf36,height=6)
  ouuylaja(q3n2qb6g,pygame.Rect(225,12,372,40))
  gqoagsus=self.mpyxdw2z.render('Hp.',True,(20,20,20))
  q3n2qb6g.blit(gqoagsus,(233,23))
  vhuds3qs(q3n2qb6g,297,25,290,v0rxxf36,height=19)
  gqoagsus=self.mpyxdw2z.render(f'{round(self.arhnuxor)}/{self.hu9n79gi}',True,(20,20,20))
  width=gqoagsus.get_width()
  height=gqoagsus.get_height()
  q3n2qb6g.blit(gqoagsus,(442-width//2,34.5-height//2))
