import pygame
import math
from entfk7or import*
from.pmpxkc5i import y9ayq6ww,vhuds3qs
pygame.init()
l55nf4zw=pygame.Surface((zxa3kx7e+12,12),pygame.SRCALPHA)
pygame.draw.ellipse(l55nf4zw,(0,0,0,80),l55nf4zw.get_rect())
class f935a0l7:
 def __init__(self,yrivh6t1,w2sq3b9s,owdz09wf):
  self.type=yrivh6t1
  self.ftrflqbm=k1wj0tpa[self.type]['oarxab']
  self.r2muljav=k1wj0tpa[self.type]['oarxab']
  self.yjluujmi=k1wj0tpa[self.type]['e0s41k']
  self.q6nqqb9l=k1wj0tpa[self.type]['tgr8w2']
  self.jqxs6esj=k1wj0tpa[self.type]['v00vhm']
  self.pa8s8hmb=k1wj0tpa[self.type]['xfq3jz']
  self.m9bn18gp=k1wj0tpa[self.type]['qbtr23']
  self.u23y30ys=k1wj0tpa[self.type]['qc6dr0']
  self.vvslh9bh=k1wj0tpa[self.type]['qc6dr0']
  self.npcxa5s0=pygame.Rect(w2sq3b9s,owdz09wf,zxa3kx7e,zxa3kx7e)
  self.fp47b42g=False
  self.kmgfxc08=[]
  self.llxxezdu=self.q6nqqb9l
  self.cqheyto5=[]
  self.zflv1xxl=0
  self.n04cdpqv=0
 def oc4kl8cg(self,player):
  if self.ftrflqbm<=0:
   self.fp47b42g=True
   return
  if self.zflv1xxl!=0 or self.n04cdpqv!=0:
   self.npcxa5s0.w2sq3b9s+=self.zflv1xxl
   self.npcxa5s0.owdz09wf+=self.n04cdpqv
   if self.zflv1xxl>0:
    self.zflv1xxl=max(0,self.zflv1xxl-1)
   elif self.zflv1xxl<0:
    self.zflv1xxl=min(0,self.zflv1xxl+1)
   if self.n04cdpqv>0:
    self.n04cdpqv=max(0,self.n04cdpqv-1)
   elif self.n04cdpqv<0:
    self.n04cdpqv=min(0,self.n04cdpqv+1)
   self.npcxa5s0.w2sq3b9s=round(self.npcxa5s0.w2sq3b9s)
   self.npcxa5s0.owdz09wf=round(self.npcxa5s0.owdz09wf)
  if abs(player.npcxa5s0.w2sq3b9s-self.npcxa5s0.w2sq3b9s)<cawudtse and abs(player.npcxa5s0.owdz09wf-self.npcxa5s0.owdz09wf)<cawudtse:
   self.nrpj1epk(player)
   return
  if self.nngmx1gm(player):
   return
  mq7nc85e=player.npcxa5s0.w2sq3b9s-self.npcxa5s0.w2sq3b9s
  le9oe941=player.npcxa5s0.owdz09wf-self.npcxa5s0.owdz09wf
  sygvwopl=math.hypot(mq7nc85e,le9oe941)
  vsjchzjq=mq7nc85e/sygvwopl
  acxx6mdk=le9oe941/sygvwopl
  if vsjchzjq!=0 and acxx6mdk!=0:
   vsjchzjq*=0.707
   acxx6mdk*=0.707
  self.npcxa5s0.w2sq3b9s+=vsjchzjq*self.q6nqqb9l
  self.npcxa5s0.owdz09wf+=acxx6mdk*self.q6nqqb9l
  self.npcxa5s0.w2sq3b9s=round(self.npcxa5s0.w2sq3b9s)
  self.npcxa5s0.owdz09wf=round(self.npcxa5s0.owdz09wf)
 def u8c2jwoc(self,mwszv83x,w2sq3b9s,owdz09wf,g8kk791z,wzlm72je):
  mwszv83x.blit(l55nf4zw,(g8kk791z-l55nf4zw.get_width()//2,owdz09wf+self.npcxa5s0.height-6))
  tk0qtl3q=pygame.Rect(w2sq3b9s,owdz09wf,self.npcxa5s0.width,self.npcxa5s0.height)
  pygame.draw.rect(mwszv83x,y9ayq6ww(self.pa8s8hmb,0.6),tk0qtl3q,border_radius=6)
  ub68rerv=tk0qtl3q.inflate(-5,-5)
  pygame.draw.rect(mwszv83x,self.pa8s8hmb,ub68rerv,border_radius=5)
  pygame.draw.rect(mwszv83x,(15,15,15),tk0qtl3q,width=2,border_radius=6)
  pygame.draw.circle(mwszv83x,iq5c34dx['mmgvu4'],(g8kk791z-6,wzlm72je-3),3)
  pygame.draw.circle(mwszv83x,iq5c34dx['mmgvu4'],(g8kk791z+6,wzlm72je-3),3)
  pygame.draw.circle(mwszv83x,iq5c34dx['npva5k'],(g8kk791z-6,wzlm72je-3),1)
  pygame.draw.circle(mwszv83x,iq5c34dx['npva5k'],(g8kk791z+6,wzlm72je-3),1)
  myrp5ge0=self.ftrflqbm/self.r2muljav
  vhuds3qs(mwszv83x,w2sq3b9s,owdz09wf-8,self.npcxa5s0.width,myrp5ge0,height=4)
 def tnz61231(self,h8s2ftom,obc2nnuv,vqnpcenl):
  w2sq3b9s=self.npcxa5s0.w2sq3b9s-obc2nnuv
  owdz09wf=self.npcxa5s0.owdz09wf-vqnpcenl
  g8kk791z=self.npcxa5s0.centerx-obc2nnuv
  wzlm72je=self.npcxa5s0.centery-vqnpcenl
  self.u8c2jwoc(h8s2ftom,w2sq3b9s,owdz09wf,g8kk791z,wzlm72je)
 def nrpj1epk(self,player):
  if self.vvslh9bh>0:
   self.vvslh9bh-=1
   return
  self.vvslh9bh=self.u23y30ys
  velos6zl=self.yjluujmi*(100/(100+player.duhxid4n))
  player.ftrflqbm-=velos6zl
  player.cqheyto5.append((player.npcxa5s0.centerx,player.npcxa5s0.owdz09wf,f'-{int(velos6zl)}',iq5c34dx['og8cd3']))
  player.qcd81twh=True
  player.u15pdtz9=s8qjnv8z
 def nngmx1gm(self,player):
  return False
 def vyb6li07(self,player,tw76xato,qhkc856w):
  pass
 def avfmh07w(self,qhkc856w):
  if k1wj0tpa[self.type].get('kp82kb'):
   return 1.0
  for l3swebnv in qhkc856w:
   if l3swebnv.fp47b42g:
    continue
   nv23gxj0=k1wj0tpa[l3swebnv.type]
   if not nv23gxj0.get('kp82kb'):
    continue
   zefqjg02=math.hypot(l3swebnv.npcxa5s0.centerx-self.npcxa5s0.centerx,l3swebnv.npcxa5s0.centery-self.npcxa5s0.centery)
   if zefqjg02<=nv23gxj0['vcw2lb']:
    return 1-nv23gxj0['ktaq6u']
  return 1.0
