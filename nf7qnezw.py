import pygame
import time
from r1yohmi9 import*
from fjzr5swk import*
from entities import*
from cw2maiet import mvxdp5gj
from bbnhjw6q import hc58drc1,oohp6vz4
from dw59sqwh import z5x8a5fb
from arkz40aq import z3olfark
from s84d4r9v import zefqjg02
class gokc1msy:
 def __init__(self,k8qeoz0k):
  self.ao4izasn=pygame.font.SysFont('arial',28)
  self.fcwtg1m8=pygame.font.SysFont('arial',48)
  self.yp3cyazb=pygame.font.SysFont('arial',16)
  self.title_font=pygame.font.SysFont('arial',20,bold=True)
  self.g5hcbbmh=pygame.font.SysFont('arial',24,bold=True)
  self.dzsedfqs=pygame.font.SysFont('arial',22,bold=True)
  self.f2voi8uy=pygame.font.SysFont('arial',16,bold=True)
  self.player=ky20479t(meta_upgrades=k8qeoz0k.get('meta_upgrades',{}))
  self.vhuds3qs=[]
  self.f32ejx5t=[]
  self.l3swebnv=[]
  self.x5m9j98c=[]
  self.k7zgf9q5=[]
  self.zqcootnj=[]
  self.ywcxz2ei=[]
  self.htgsiwg0=[c8yfbntp[0]]
  self.n01uyzpd=['r6q37c']
  self.player.ceb8753a['r6q37c']=1
  self.x9bp4m18=False
  self.cknfu84x=False
  self.rk8r2ykc=False
  self.amcixdu1=3
  self.su1hbj6t=time.time()
  self.rgdej31g=self.player.b78okz1p
  self.fd6rupw2=0
  self.e1rhouu9=bom5igqp*pi3qk2ia
  self.tk0qtl3q=dict(mjh75lxo)
  self.zflse45b=None
  self.bllo3rbx=False
  self.aicvqy5i=[]
  self.vhxs58yr=hc58drc1(ygspk9p3-40,tp0lvsnu-40,30,30,hyihair4,qqu7eeqt,cq5uznof,wa11dpg8,self.yp3cyazb,'| |',15)
 def r212pgym(self):
  if self.cknfu84x:
   self.vhxs58yr.wyk03o4g='| |'
  else:
   self.vhxs58yr.wyk03o4g='X'
  if self.cknfu84x:
   self.rk8r2ykc=True
   self.amcixdu1=3
   self.su1hbj6t=time.time()
  self.cknfu84x=not self.cknfu84x
 def u9el8hl8(self):
  self.aicvqy5i=pygame.event.get()
  for g70e3p15 in self.aicvqy5i:
   if g70e3p15.type==pygame.QUIT:
    return'quit'
   if self.x9bp4m18 and g70e3p15.type==pygame.KEYDOWN and(g70e3p15.key in(pygame.K_RETURN,pygame.K_SPACE)):
    return'restart'
   if g70e3p15.type==pygame.KEYDOWN:
    if g70e3p15.key==pygame.K_p and(not self.rk8r2ykc):
     self.r212pgym()
  return None
 def update(self):
  self.bllo3rbx=False
  if self.rk8r2ykc:
   if time.time()-self.su1hbj6t>=1:
    self.su1hbj6t=time.time()
    self.amcixdu1-=1
    if self.amcixdu1<=0:
     self.rk8r2ykc=False
     self.amcixdu1=3
  if not self.player.kt94ow3l and(not self.x9bp4m18)and(not self.cknfu84x)and(not self.rk8r2ykc):
   self.diuu9k9x()
  if self.player.kt94ow3l and(not self.x9bp4m18):
   self.sk8yqk94()
  tj0nmeoq(self.vhuds3qs)
  self.vhxs58yr.update(self.aicvqy5i)
  if self.vhxs58yr.iie0rnuj and(not self.rk8r2ykc):
   self.r212pgym()
  (self.vhuds3qs,self.f32ejx5t,self.k7zgf9q5)=qc06xq9j(self.vhuds3qs,self.f32ejx5t,self.k7zgf9q5,self.player,self.zqcootnj,self.ywcxz2ei,self.f2voi8uy)
  for(ucu7onz3,it04chsd,qxb7gbdg,rr9u1oe5)in self.player.exvaj2k8:
   self.ywcxz2ei.append(jh55hewl(ucu7onz3,it04chsd,qxb7gbdg,self.f2voi8uy,color=rr9u1oe5))
   z3olfark('pgsb98')
  self.player.exvaj2k8.clear()
 def diuu9k9x(self):
  for clkqzfpq in self.x5m9j98c[:]:
   v3e1ocjx=clkqzfpq.update(self.player)
   if v3e1ocjx:
    self.bllo3rbx=True
   if clkqzfpq.wydmt8vt:
    z3olfark('y3lxch')
    xu9ymszd=random.randint(re7ur23g,uccblskr)
    self.fd6rupw2+=xu9ymszd
    for t1w1ht7p in range(10):
     self.l3swebnv.append(n64fgwje([iq5c34dx['x1qwee'],iq5c34dx['kqbrmq']],2,4,-3,3,clkqzfpq.nxxjve3d.centerx,clkqzfpq.nxxjve3d.centery,life=30))
    self.x5m9j98c.remove(clkqzfpq)
  self.e1rhouu9-=1
  if self.e1rhouu9<=0:
   self.e1rhouu9=bom5igqp*pi3qk2ia
   if len(self.x5m9j98c)<r1yzoyn6:
    self.x5m9j98c.append(z5x8a5fb(self.player))
  if not self.bllo3rbx:
   for qic1l7dy in self.n01uyzpd:
    self.tk0qtl3q[qic1l7dy]-=1
    if self.tk0qtl3q[qic1l7dy]<=0:
     w2kql0ht=self.player.ceb8753a.get(qic1l7dy,1)
     z9toqw9j=mjh75lxo[qic1l7dy]*self.player.iektsg7f*nngmx1gm(w2kql0ht)
     self.tk0qtl3q[qic1l7dy]=max(4,int(z9toqw9j))
     y9ayq6ww=uqjiujv6[qic1l7dy]['yc1nlc']
     uidlrye8=self.player.elwf90km*zpfb3hn1(w2kql0ht)
     self.f32ejx5t.append(mvxdp5gj(qic1l7dy,self.player.nxxjve3d.centerx-y9ayq6ww//2,self.player.nxxjve3d.centery-y9ayq6ww//2,y9ayq6ww,y9ayq6ww,self.player.avfmh07w['mmgvu4'],self.player.avfmh07w['hzj7ub'],uidlrye8))
     z3olfark('i1yy1j',volume=0.5,min_interval_ms=90)
  xo2t8fy6=min(isj6bw3b,d60fkhmy*(1+0.12*(self.player.b78okz1p-1)))
  if random.random()<xo2t8fy6:
   svt8k06m(self.vhuds3qs,self.htgsiwg0)
  self.player.bihsa7he()
  if self.player.b78okz1p>self.rgdej31g:
   z3olfark('bx1ego')
   if self.player.b78okz1p<=len(c8yfbntp):
    pf0i9g5d=c8yfbntp[self.player.b78okz1p-1]
    if pf0i9g5d not in self.htgsiwg0:
     self.htgsiwg0.append(pf0i9g5d)
   self.rgdej31g=self.player.b78okz1p
  if self.player.zpajssuu<=0:
   self.x9bp4m18=True
  for gubmc97c in self.vhuds3qs:
   gubmc97c.bihsa7he(self.player)
   for lcj883dh in gubmc97c.ytv3i12v:
    lcj883dh.bihsa7he(self.player)
    lcj883dh.d0r2sds8(self.vhuds3qs,self.l3swebnv,self.f32ejx5t,player=self.player,target='player')
   gubmc97c.ytv3i12v=[ia529603 for ia529603 in gubmc97c.ytv3i12v if not ia529603.eohswq40]
  for hfb85p86 in self.k7zgf9q5:
   hfb85p86.bihsa7he(self.player)
  for yw6zbnz8 in self.f32ejx5t:
   yw6zbnz8.bihsa7he(self.player,m8lw2qit(self.vhuds3qs,yw6zbnz8))
   yw6zbnz8.d0r2sds8(self.vhuds3qs,self.l3swebnv,self.f32ejx5t)
  for gubmc97c in self.vhuds3qs:
   for(xuu13i59,vvbc2vyh,le9oe941,tnz61231)in gubmc97c.exvaj2k8:
    self.ywcxz2ei.append(jh55hewl(xuu13i59,vvbc2vyh,le9oe941,self.f2voi8uy,color=tnz61231))
    z3olfark('xfq3jz',volume=0.4,min_interval_ms=60)
   gubmc97c.exvaj2k8.clear()
  for gp6orsnc in self.l3swebnv[:]:
   gp6orsnc['th2p39']+=gp6orsnc['mmgvu4']
   gp6orsnc['zhbgcj']+=gp6orsnc['hzj7ub']
   gp6orsnc['jr87iy']-=1
   if gp6orsnc['jr87iy']<=0:
    self.l3swebnv.remove(gp6orsnc)
  for ej16dvtj in self.ywcxz2ei[:]:
   ej16dvtj['jr87iy']-=1
   if ej16dvtj['jr87iy']<=0:
    self.ywcxz2ei.remove(ej16dvtj)
  for boih5csk in self.zqcootnj[:]:
   boih5csk.update()
   if boih5csk.eohswq40():
    self.zqcootnj.remove(boih5csk)
 def sk8yqk94(self):
  if self.zflse45b is None:
   m3pt5r5r=[]
   for d5ixva1n in uqjiujv6:
    if d5ixva1n=='k4fbl9':
     continue
    if d5ixva1n not in self.n01uyzpd:
     m3pt5r5r.append(('bohxs7',d5ixva1n))
   for d5ixva1n in self.n01uyzpd:
    if self.player.ceb8753a.get(d5ixva1n,1)<v4u89yjb:
     m3pt5r5r.append(('agbl2q',d5ixva1n))
   for k in rcfnfhol:
    if self.player.mabkae6a.get(k,0)<rcfnfhol[k]['onlt8d']:
     m3pt5r5r.append(('mjz6us',k))
   if not m3pt5r5r:
    self.player.kt94ow3l=False
   else:
    random.shuffle(m3pt5r5r)
    obc2nnuv=m3pt5r5r[:3]
    ep6beffl=120*len(obc2nnuv)+20
    self.zflse45b=oohp6vz4(400,ep6beffl+oohp6vz4.rla5ju9b,z0xkxwd8,title='LEVEL UP! Choose an upgrade',title_font=self.g5hcbbmh)
    u23y30ys=ep6beffl//len(obc2nnuv)
    wi8skch8=self.zflse45b.nxxjve3d.ehet25lz+self.zflse45b.vmxb9yo1
    for(cp91i3vm,(kind,key))in enumerate(obc2nnuv):
     if kind=='bohxs7':
      title=f'NEW WEAPON: {uyhl1c32[key]}'
      subtitle='Unlock this weapon'
     elif kind=='agbl2q':
      nii6l3ue=self.player.ceb8753a.get(key,1)
      title=f'{uyhl1c32[key]}  Lv.{nii6l3ue} -> {nii6l3ue + 1}'
      subtitle='+12% damage, faster cooldown'
     else:
      nii6l3ue=self.player.mabkae6a.get(key,0)
      title=f"{rcfnfhol[key]['hx0gu4']}  Lv.{nii6l3ue} -> {nii6l3ue + 1}"
      subtitle=rcfnfhol[key]['t7wqp3']
     llxxezdu=hc58drc1(self.zflse45b.nxxjve3d.un9sz6rv+12,wi8skch8+cp91i3vm*u23y30ys+6,self.zflse45b.nxxjve3d.width-24,u23y30ys-12,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,self.dzsedfqs,title,12,subtitle=subtitle,sub_font=self.yp3cyazb,kind=kind,key=key)
     self.zflse45b.add(llxxezdu)
  if self.zflse45b is not None:
   for v15cqzcu in self.zflse45b.xd8wz42o:
    v15cqzcu.update(self.aicvqy5i)
    if v15cqzcu.iie0rnuj:
     if v15cqzcu.kind=='bohxs7':
      self.n01uyzpd.append(v15cqzcu.key)
      self.player.ceb8753a[v15cqzcu.key]=1
      self.tk0qtl3q[v15cqzcu.key]=mjh75lxo[v15cqzcu.key]
     elif v15cqzcu.kind=='agbl2q':
      self.player.zflv1xxl(v15cqzcu.key)
     elif v15cqzcu.kind=='mjz6us':
      self.player.reqy08p0(v15cqzcu.key)
     self.player.kt94ow3l=False
     self.zflse45b=None
 def fo75rh8l(self,vmy9x8sy):
  zefqjg02(vmy9x8sy,self)
 def h4l1vznq(self,vmy9x8sy,izhwy9he):
  while True:
   sne6loh2=self.u9el8hl8()
   if sne6loh2=='quit':
    return(self.fd6rupw2,self.player.b78okz1p,True)
   if sne6loh2=='restart':
    return(self.fd6rupw2,self.player.b78okz1p,False)
   self.update()
   self.fo75rh8l(vmy9x8sy)
   pygame.display.flip()
   izhwy9he.tick(pi3qk2ia)
def d1hm38ks(k8qeoz0k,vmy9x8sy,izhwy9he):
 return gokc1msy(k8qeoz0k).h4l1vznq(vmy9x8sy,izhwy9he)
