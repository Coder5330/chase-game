import pygame
import math
from i1arxabo import*
from.uu86zjq7 import fd6rupw2,eohswq40
pygame.init()
wa11dpg8=pygame.Surface((qqu7eeqt+16,14),pygame.SRCALPHA)
pygame.draw.ellipse(wa11dpg8,(0,0,0,90),wa11dpg8.get_rect())
class yur7ko64:
 def __init__(self,meta_upgrades=None):
  meta_upgrades=meta_upgrades or{}
  sye0a4ab=meta_upgrades.get('START_HEALTH',0)
  j1ldqnk2=meta_upgrades.get('START_SPEED',0)
  d1b3jczu=meta_upgrades.get('START_DAMAGE',0)
  jxxgaear=meta_upgrades.get('START_COOLDOWN',0)
  n04cdpqv=meta_upgrades.get('START_ARMOR',0)
  v6g298cq=meta_upgrades.get('START_REGEN',0)
  self.l57p6bkl=rv86wzs3*xwqvr1h6(j1ldqnk2)
  self.mn89ltaj=self.l57p6bkl
  self.todsx4nx=pygame.Rect((rrcbpljd-qqu7eeqt)//2,(x37pqkoj-qqu7eeqt)//2,qqu7eeqt,qqu7eeqt)
  self.i20cv3tl=iq5c34dx['m1v3zo']
  self.nqimqodp=int(1000*lnf74t60(sye0a4ab))
  self.mctwjlsh=self.nqimqodp
  self.mpyxdw2z=self.nqimqodp
  self.n01uyzpd=0
  self.swwnc21o=1
  self.ra9kepad=False
  self.i13n3bzt={'v9hbn5':0,'da7yvd':self.mn89ltaj}
  self.qxb7gbdg={}
  self.kc1fjotg={key:0 for key in rqf5q14j}
  self.mpdzp6lf=crsb4gf1(d1b3jczu)
  self.b06xkxb9=ls2zge2j(jxxgaear)
  self.am2vajep=zflv1xxl(n04cdpqv)
  self.x03uvule=nii6l3ue(v6g298cq)
  self.u1jhuwb6=self.mpdzp6lf
  self.obc2nnuv=self.b06xkxb9
  self.kt94ow3l=1.0
  self.j1i2hgj1=self.am2vajep
  self.tkyrmjlj=self.x03uvule
  self.uz6kf162=pi3qk2ia
  self.xu9ymszd=False
  self.v0rxxf36=0
  self.lgbpj4uf=[]
 def diuu9k9x(self,key):
  self.kc1fjotg[key]+=1
  nyrid3dn=self.kc1fjotg[key]
  if key=='o5rlqi':
   chx3d43e=int(self.nqimqodp*(1+0.2*nyrid3dn))
   self.mpyxdw2z+=chx3d43e-self.mctwjlsh
   self.mctwjlsh=chx3d43e
  elif key=='e8a1ar':
   self.mn89ltaj=self.l57p6bkl*(1+0.08*nyrid3dn)
  elif key=='w2zeeq':
   self.tkyrmjlj=self.x03uvule+nyrid3dn
  elif key=='kmx1gm':
   self.u1jhuwb6=self.mpdzp6lf*(1+0.06*nyrid3dn)
  elif key=='yeurxh':
   self.obc2nnuv=self.b06xkxb9*max(0.6,1-0.05*nyrid3dn)
  elif key=='l6ijku':
   self.j1i2hgj1=self.am2vajep+nyrid3dn*5
  elif key=='dzjssz':
   self.kt94ow3l=1+0.15*nyrid3dn
 def xd8wz42o(self,eq3tq1s0):
  self.qxb7gbdg[eq3tq1s0]=self.qxb7gbdg.get(eq3tq1s0,1)+1
 def mcup8ijl(self):
  arhnuxor=pygame.key.get_pressed()
  g8kk791z=wzlm72je=0
  if arhnuxor[pygame.K_UP]:
   wzlm72je-=self.mn89ltaj
  if arhnuxor[pygame.K_DOWN]:
   wzlm72je+=self.mn89ltaj
  if arhnuxor[pygame.K_LEFT]:
   g8kk791z-=self.mn89ltaj
  if arhnuxor[pygame.K_RIGHT]:
   g8kk791z+=self.mn89ltaj
  if g8kk791z!=0 and wzlm72je!=0:
   g8kk791z*=0.707
   wzlm72je*=0.707
  if g8kk791z!=0 or wzlm72je!=0:
   self.i13n3bzt['v9hbn5']=g8kk791z
   self.i13n3bzt['da7yvd']=wzlm72je
  self.todsx4nx.htgsiwg0+=g8kk791z
  self.todsx4nx.hhl1737s+=wzlm72je
  self.todsx4nx.htgsiwg0=max(min(self.todsx4nx.htgsiwg0,rrcbpljd-self.todsx4nx.width),0)
  self.todsx4nx.hhl1737s=max(min(self.todsx4nx.hhl1737s,x37pqkoj-self.todsx4nx.height),0)
  if self.tkyrmjlj>0 and self.mpyxdw2z<self.mctwjlsh:
   self.uz6kf162-=1
   if self.uz6kf162<=0:
    self.uz6kf162=pi3qk2ia
    self.mpyxdw2z=min(self.mctwjlsh,self.mpyxdw2z+self.tkyrmjlj)
  if self.n01uyzpd>=v4u89yjb[min(self.swwnc21o,len(v4u89yjb)-1)]:
   self.ra9kepad=True
   self.n01uyzpd=0
   self.swwnc21o+=1
 def sl65wvjx(self,tj0nmeoq,uysal8m1,giec4d14):
  htgsiwg0=self.todsx4nx.htgsiwg0-uysal8m1
  hhl1737s=self.todsx4nx.hhl1737s-giec4d14
  wi8skch8=self.todsx4nx.centerx-uysal8m1
  iektsg7f=self.todsx4nx.centery-giec4d14
  tj0nmeoq.blit(wa11dpg8,(wi8skch8-wa11dpg8.get_width()//2,hhl1737s+self.todsx4nx.height-8))
  sv5f1bcp=pygame.Rect(htgsiwg0,hhl1737s,self.todsx4nx.width,self.todsx4nx.height)
  pygame.draw.rect(tj0nmeoq,fd6rupw2(self.i20cv3tl,0.55),sv5f1bcp,border_radius=10)
  sdeekgys=sv5f1bcp.inflate(-5,-5)
  pygame.draw.rect(tj0nmeoq,self.i20cv3tl,sdeekgys,border_radius=8)
  m20u9isy=pygame.Rect(sdeekgys.htgsiwg0+3,sdeekgys.hhl1737s+3,sdeekgys.width//2,sdeekgys.height//3)
  pygame.draw.rect(tj0nmeoq,fd6rupw2(self.i20cv3tl,2.0),m20u9isy,border_radius=4)
  pygame.draw.rect(tj0nmeoq,(15,15,30),sv5f1bcp,width=2,border_radius=10)
  w5iz31yr=math.hypot(self.i13n3bzt['v9hbn5'],self.i13n3bzt['da7yvd'])or 1
  (tb4ldims,vk3g84ut)=(self.i13n3bzt['v9hbn5']/w5iz31yr,self.i13n3bzt['da7yvd']/w5iz31yr)
  e9y3z2t4=(wi8skch8+tb4ldims*20,iektsg7f+vk3g84ut*20)
  wvpw232u=(wi8skch8-vk3g84ut*7+tb4ldims*4,iektsg7f+tb4ldims*7+vk3g84ut*4)
  upprat08=(wi8skch8+vk3g84ut*7+tb4ldims*4,iektsg7f-tb4ldims*7+vk3g84ut*4)
  pygame.draw.polygon(tj0nmeoq,iq5c34dx['m314cq'],[e9y3z2t4,wvpw232u,upprat08])
  pygame.draw.polygon(tj0nmeoq,(15,15,30),[e9y3z2t4,wvpw232u,upprat08],width=1)
  exvaj2k8=self.mpyxdw2z/self.mctwjlsh
  eohswq40(tj0nmeoq,htgsiwg0,hhl1737s-10,self.todsx4nx.width,exvaj2k8,height=6)
