import pygame
import math
from z1yhxso7 import*
from.dr2h2p39 import d1hm38ks,rzewviyt
pygame.init()
wa11dpg8=pygame.Surface((qqu7eeqt+16,14),pygame.SRCALPHA)
pygame.draw.ellipse(wa11dpg8,(0,0,0,90),wa11dpg8.get_rect())
def uidlrye8(ukshy8nb,wgcl9lcq,yx4w6xlp=120,ljk4q5v7=10):
 w8wj0uun=pygame.Surface((wgcl9lcq.width,wgcl9lcq.height),pygame.SRCALPHA)
 pygame.draw.rect(w8wj0uun,(255,255,255,yx4w6xlp),w8wj0uun.get_rect(),border_radius=ljk4q5v7)
 ukshy8nb.blit(w8wj0uun,wgcl9lcq.topleft)
class yur7ko64:
 def __init__(self,meta_upgrades=None):
  meta_upgrades=meta_upgrades or{}
  qo6q0usw=meta_upgrades.get('START_HEALTH',0)
  gqq4d3kz=meta_upgrades.get('START_SPEED',0)
  a8ax40dt=meta_upgrades.get('START_DAMAGE',0)
  xwqvr1h6=meta_upgrades.get('START_COOLDOWN',0)
  j1ldqnk2=meta_upgrades.get('START_ARMOR',0)
  yvffqot8=meta_upgrades.get('START_REGEN',0)
  self.nrpj1epk=rv86wzs3*tb4ldims(gqq4d3kz)
  self.u15pdtz9=self.nrpj1epk
  self.wgcl9lcq=pygame.Rect((ygspk9p3-qqu7eeqt)//2,(v4u89yjb-qqu7eeqt)//2,qqu7eeqt,qqu7eeqt)
  self.izhwy9he=iq5c34dx['iwu3bf']
  self.kmgfxc08=int(1000*mcup8ijl(qo6q0usw))
  self.nii6l3ue=self.kmgfxc08
  self.u9el8hl8=self.kmgfxc08
  self.m81udp2f=0
  self.pcvsqame=1
  self.rm0j36tc=False
  self.xk7n8la1={'cm3v2p':0,'zmygy0':self.u15pdtz9}
  self.s7fbmenu={}
  self.awnwlc83={key:0 for key in rqf5q14j}
  self.duhxid4n=hp89fkbi(a8ax40dt)
  self.l57p6bkl=y2f7atwy(xwqvr1h6)
  self.vj8yrddp=v6g298cq(j1ldqnk2)
  self.sv5f1bcp=zo3lqi7e(yvffqot8)
  self.pv4ykade=self.duhxid4n
  self.ruq9e5co=self.l57p6bkl
  self.e1rhouu9=1.0
  self.pa5u6hc3=self.vj8yrddp
  self.g1g1r1dw=self.sv5f1bcp
  self.upprat08=pi3qk2ia
  self.nbwye6qv=False
  self.qertb74r=0
  self.vyb6li07=[]
  self.mqxlm5q2=pygame.font.SysFont('arial',20,bold=True)
 def v982n2at(self,key):
  self.awnwlc83[key]+=1
  b78okz1p=self.awnwlc83[key]
  if key=='pqpva5':
   k3z6bz8u=int(self.kmgfxc08*(1+0.2*b78okz1p))
   self.u9el8hl8+=k3z6bz8u-self.nii6l3ue
   self.nii6l3ue=k3z6bz8u
  elif key=='clslay':
   self.u15pdtz9=self.nrpj1epk*(1+0.08*b78okz1p)
  elif key=='kjuw7w':
   self.g1g1r1dw=self.sv5f1bcp+b78okz1p
  elif key=='huplvq':
   self.pv4ykade=self.duhxid4n*(1+0.06*b78okz1p)
  elif key=='zcjn99':
   self.ruq9e5co=self.l57p6bkl*max(0.6,1-0.05*b78okz1p)
  elif key=='jayeqa':
   self.pa5u6hc3=self.vj8yrddp+b78okz1p*5
  elif key=='hn3ksg':
   self.e1rhouu9=1+0.15*b78okz1p
 def je11e9ft(self,huh17j8q):
  self.s7fbmenu[huh17j8q]=self.s7fbmenu.get(huh17j8q,1)+1
 def ob7p0rnp(self):
  v3e1ocjx=pygame.key.get_pressed()
  uc1xi04b=fp47b42g=0
  if v3e1ocjx[pygame.K_UP]:
   fp47b42g-=self.u15pdtz9
  if v3e1ocjx[pygame.K_DOWN]:
   fp47b42g+=self.u15pdtz9
  if v3e1ocjx[pygame.K_LEFT]:
   uc1xi04b-=self.u15pdtz9
  if v3e1ocjx[pygame.K_RIGHT]:
   uc1xi04b+=self.u15pdtz9
  if uc1xi04b!=0 and fp47b42g!=0:
   uc1xi04b*=0.707
   fp47b42g*=0.707
  if uc1xi04b!=0 or fp47b42g!=0:
   self.xk7n8la1['cm3v2p']=uc1xi04b
   self.xk7n8la1['zmygy0']=fp47b42g
  self.wgcl9lcq.jslulzfy+=uc1xi04b
  self.wgcl9lcq.zpfb3hn1+=fp47b42g
  self.wgcl9lcq.jslulzfy=max(min(self.wgcl9lcq.jslulzfy,ygspk9p3-self.wgcl9lcq.width),0)
  self.wgcl9lcq.zpfb3hn1=max(min(self.wgcl9lcq.zpfb3hn1,v4u89yjb-self.wgcl9lcq.height),0)
  if self.g1g1r1dw>0 and self.u9el8hl8<self.nii6l3ue:
   self.upprat08-=1
   if self.upprat08<=0:
    self.upprat08=pi3qk2ia
    self.u9el8hl8=min(self.nii6l3ue,self.u9el8hl8+self.g1g1r1dw)
  if self.m81udp2f>=cqoldfor[min(self.pcvsqame,len(cqoldfor)-1)]:
   self.rm0j36tc=True
   self.m81udp2f=0
   self.pcvsqame+=1
 def wzlm72je(self,ukshy8nb,dzsedfqs,nd6357oo):
  jslulzfy=self.wgcl9lcq.jslulzfy-dzsedfqs
  zpfb3hn1=self.wgcl9lcq.zpfb3hn1-nd6357oo
  hfb85p86=self.wgcl9lcq.centerx-dzsedfqs
  k7zgf9q5=self.wgcl9lcq.centery-nd6357oo
  ukshy8nb.blit(wa11dpg8,(hfb85p86-wa11dpg8.get_width()//2,zpfb3hn1+self.wgcl9lcq.height-8))
  divsolml=pygame.Rect(jslulzfy,zpfb3hn1,self.wgcl9lcq.width,self.wgcl9lcq.height)
  pygame.draw.rect(ukshy8nb,d1hm38ks(self.izhwy9he,0.55),divsolml,border_radius=10)
  cp91i3vm=divsolml.inflate(-5,-5)
  pygame.draw.rect(ukshy8nb,self.izhwy9he,cp91i3vm,border_radius=8)
  nyfkjfpn=pygame.Rect(cp91i3vm.jslulzfy+3,cp91i3vm.zpfb3hn1+3,cp91i3vm.width//2,cp91i3vm.height//3)
  pygame.draw.rect(ukshy8nb,d1hm38ks(self.izhwy9he,2.0),nyfkjfpn,border_radius=4)
  pygame.draw.rect(ukshy8nb,(15,15,30),divsolml,width=2,border_radius=10)
  bokzixza=math.hypot(self.xk7n8la1['cm3v2p'],self.xk7n8la1['zmygy0'])or 1
  (r2muljav,a62c9t19)=(self.xk7n8la1['cm3v2p']/bokzixza,self.xk7n8la1['zmygy0']/bokzixza)
  mlikwe4b=(hfb85p86+r2muljav*20,k7zgf9q5+a62c9t19*20)
  zmybd2qe=(hfb85p86-a62c9t19*7+r2muljav*4,k7zgf9q5+r2muljav*7+a62c9t19*4)
  hay64yfd=(hfb85p86+a62c9t19*7+r2muljav*4,k7zgf9q5-r2muljav*7+a62c9t19*4)
  pygame.draw.polygon(ukshy8nb,iq5c34dx['yl4zjd'],[mlikwe4b,zmybd2qe,hay64yfd])
  pygame.draw.polygon(ukshy8nb,(15,15,30),[mlikwe4b,zmybd2qe,hay64yfd],width=1)
  cqheyto5=self.u9el8hl8/self.nii6l3ue
  rzewviyt(ukshy8nb,jslulzfy,zpfb3hn1-10,self.wgcl9lcq.width,cqheyto5,height=6)
  uidlrye8(ukshy8nb,pygame.Rect(225,12,372,40))
  w8wj0uun=self.mqxlm5q2.render('Hp.',True,(20,20,20))
  ukshy8nb.blit(w8wj0uun,(233,23))
  rzewviyt(ukshy8nb,297,25,290,cqheyto5,height=19)
  w8wj0uun=self.mqxlm5q2.render(f'{round(self.u9el8hl8)}/{self.nii6l3ue}',True,(20,20,20))
  width=w8wj0uun.get_width()
  height=w8wj0uun.get_height()
  ukshy8nb.blit(w8wj0uun,(442-width//2,34.5-height//2))
