import pygame
import math
from vnbnqbnx import*
from.s84d4r9v import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,nfn1r4kz,iimoe0sy,gdg1wjui):
  super().__init__(nfn1r4kz,iimoe0sy,gdg1wjui)
  self.ao4izasn=(0,1)
  self.cq6qdy4l=False
  self.izhwy9he=0
  self.iie0rnuj=18
 def mabkae6a(self,player):
  b36htf4p=player.bdgbk2l0.centerx-self.bdgbk2l0.centerx
  vhuds3qs=player.bdgbk2l0.centery-self.bdgbk2l0.centery
  d1b3jczu=math.hypot(b36htf4p,vhuds3qs)or 1
  self.ao4izasn=(b36htf4p/d1b3jczu,vhuds3qs/d1b3jczu)
  if self.cq6qdy4l:
   self.izhwy9he-=1
   if self.izhwy9he<=0:
    self.cq6qdy4l=False
    self.cx41dntc(player)
   return True
  if abs(player.bdgbk2l0.iimoe0sy-self.bdgbk2l0.iimoe0sy)<b8cgvyie and abs(player.bdgbk2l0.gdg1wjui-self.bdgbk2l0.gdg1wjui)<b8cgvyie:
   if self.ra73jgzl>0:
    self.ra73jgzl-=1
    return True
   self.cq6qdy4l=True
   self.izhwy9he=self.iie0rnuj
   return True
  return False
 def cx41dntc(self,player):
  self.ra73jgzl=self.bq349dxb
  from ovlhyl2l import rpqk51fp
  u15pdtz9=uqjiujv6['fgb1aj']['riny2e']
  (b36htf4p,vhuds3qs)=(player.bdgbk2l0.centerx-self.bdgbk2l0.centerx,player.bdgbk2l0.centery-self.bdgbk2l0.centery)
  nqimqodp=rpqk51fp('fgb1aj',self.bdgbk2l0.centerx-u15pdtz9//2,self.bdgbk2l0.centery-u15pdtz9//2,u15pdtz9,u15pdtz9,b36htf4p,vhuds3qs)
  nqimqodp.eohswq40=self.x875aud9
  self.x03uvule.append(nqimqodp)
 def sygvwopl(self,g1b3d505,xp8mgyn2,i20cv3tl):
  iimoe0sy=self.bdgbk2l0.iimoe0sy-xp8mgyn2
  gdg1wjui=self.bdgbk2l0.gdg1wjui-i20cv3tl
  yuibrsz1=self.bdgbk2l0.centerx-xp8mgyn2
  mfyb8dal=self.bdgbk2l0.centery-i20cv3tl
  self.eqrl1n75(g1b3d505,iimoe0sy,gdg1wjui,yuibrsz1,mfyb8dal)
  (cjn2fomd,jq1ddpus)=self.ao4izasn
  (yg87oi0e,xasez2nx)=(-jq1ddpus,cjn2fomd)
  (tk0qtl3q,gn89qkns)=(yuibrsz1+cjn2fomd*14,mfyb8dal+jq1ddpus*14)
  f2voi8uy=(tk0qtl3q+yg87oi0e*13-cjn2fomd*6,gn89qkns+xasez2nx*13-jq1ddpus*6)
  wvndfdw7=(tk0qtl3q-yg87oi0e*13-cjn2fomd*6,gn89qkns-xasez2nx*13-jq1ddpus*6)
  tacj4t0s=(tk0qtl3q+cjn2fomd*6,gn89qkns+jq1ddpus*6)
  pygame.draw.lines(g1b3d505,(110,70,30),False,[f2voi8uy,tacj4t0s,wvndfdw7],3)
  mygfliji=1-self.izhwy9he/self.iie0rnuj if self.cq6qdy4l else 0
  mu4fmpkx=(tk0qtl3q-cjn2fomd*(3+mygfliji*10),gn89qkns-jq1ddpus*(3+mygfliji*10))
  pygame.draw.line(g1b3d505,(225,225,215),f2voi8uy,mu4fmpkx,2)
  pygame.draw.line(g1b3d505,(225,225,215),wvndfdw7,mu4fmpkx,2)
  if self.cq6qdy4l:
   vj8yrddp=(tk0qtl3q+cjn2fomd*8,gn89qkns+jq1ddpus*8)
   pygame.draw.line(g1b3d505,iq5c34dx['o5rlqi'],mu4fmpkx,vj8yrddp,3)
