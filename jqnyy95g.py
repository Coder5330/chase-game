import pygame
import time
from jggz62fe import*
from x50opf06 import*
from entities import*
from mg5wzawn import mvxdp5gj
from bdnwnguc import hc58drc1,yur7ko64
from wlbpj8t2 import u1ni10kq
from kupnhzx9 import jenvg3kk
from erp0aga2 import mq7nc85e
class gokc1msy:
 def __init__(self,uwxrum2l):
  self.cjn2fomd=pygame.font.SysFont('arial',28)
  self.yw6zbnz8=pygame.font.SysFont('arial',48)
  self.sfu38gl2=pygame.font.SysFont('arial',16)
  self.title_font=pygame.font.SysFont('arial',20,bold=True)
  self.no0u93mz=pygame.font.SysFont('arial',24,bold=True)
  self.clkqzfpq=pygame.font.SysFont('arial',22,bold=True)
  self.kt94ow3l=pygame.font.SysFont('arial',16,bold=True)
  self.player=ky20479t(meta_upgrades=uwxrum2l.get('meta_upgrades',{}))
  self.nfn1r4kz=[]
  self.i20cv3tl=[]
  self.vt26ys44=[]
  self.vw6m7b5c=[]
  self.rmm1zxyv=[]
  self.fddfgs3j=[]
  self.mabkae6a=[]
  self.e1rhouu9=[c8yfbntp[0]]
  self.qic1l7dy=['oud2zd']
  self.player.hiac2e4q['oud2zd']=1
  self.nyfkjfpn=False
  self.v6xii5p5=False
  self.yuibrsz1=False
  self.f2sehe2a=3
  self.nabufwbu=time.time()
  self.xasez2nx=self.player.a8ax40dt
  self.gg7oq2zd=0
  self.q6p61xuf=bom5igqp*pi3qk2ia
  self.jm25len6=dict(mjh75lxo)
  self.z3olfark=None
  self.wzs13c9x=False
  self.s4rxyj38=[]
  self.ljk4q5v7=hc58drc1(cqoldfor-40,tp0lvsnu-40,30,30,cq5uznof,rv86wzs3,wa11dpg8,qqu7eeqt,self.sfu38gl2,'| |',15)
 def hhl1737s(self):
  if self.v6xii5p5:
   self.ljk4q5v7.gsrtwlxd='| |'
  else:
   self.ljk4q5v7.gsrtwlxd='X'
  if self.v6xii5p5:
   self.yuibrsz1=True
   self.f2sehe2a=3
   self.nabufwbu=time.time()
  self.v6xii5p5=not self.v6xii5p5
 def vpbwhvnz(self):
  self.s4rxyj38=pygame.event.get()
  for eatvzkhi in self.s4rxyj38:
   if eatvzkhi.type==pygame.QUIT:
    return'quit'
   if self.nyfkjfpn and eatvzkhi.type==pygame.KEYDOWN and(eatvzkhi.key in(pygame.K_RETURN,pygame.K_SPACE)):
    return'restart'
   if eatvzkhi.type==pygame.KEYDOWN:
    if eatvzkhi.key==pygame.K_p and(not self.yuibrsz1):
     self.hhl1737s()
  return None
 def update(self):
  self.wzs13c9x=False
  if self.yuibrsz1:
   if time.time()-self.nabufwbu>=1:
    self.nabufwbu=time.time()
    self.f2sehe2a-=1
    if self.f2sehe2a<=0:
     self.yuibrsz1=False
     self.f2sehe2a=3
  if not self.player.zpfb3hn1 and(not self.nyfkjfpn)and(not self.v6xii5p5)and(not self.yuibrsz1):
   self.ytv3i12v()
  if self.player.zpfb3hn1 and(not self.nyfkjfpn):
   self.uva2ieuc()
  h4l1vznq(self.nfn1r4kz)
  self.ljk4q5v7.update(self.s4rxyj38)
  if self.ljk4q5v7.bfoqmf5l and(not self.yuibrsz1):
   self.hhl1737s()
  (self.nfn1r4kz,self.i20cv3tl,self.rmm1zxyv)=cq2q4qer(self.nfn1r4kz,self.i20cv3tl,self.rmm1zxyv,self.player,self.fddfgs3j,self.mabkae6a,self.kt94ow3l)
  for(m81udp2f,kcubods1,x3n27m5p,k82853uy)in self.player.eehou6ql:
   self.mabkae6a.append(zgomf9pm(m81udp2f,kcubods1,x3n27m5p,self.kt94ow3l,color=k82853uy))
   jenvg3kk('oarxab')
  self.player.eehou6ql.clear()
 def ytv3i12v(self):
  for iektsg7f in self.vw6m7b5c[:]:
   o4dd1vn8=iektsg7f.update(self.player)
   if o4dd1vn8:
    self.wzs13c9x=True
   if iektsg7f.gp6orsnc:
    jenvg3kk('kp82kb')
    q26yg3dx=random.randint(re7ur23g,uccblskr)
    self.gg7oq2zd+=q26yg3dx
    for wrbw2zla in range(10):
     self.vt26ys44.append(ysqg8x80([iq5c34dx['glmy62'],iq5c34dx['t7wqp3']],2,4,-3,3,iektsg7f.xu9ymszd.centerx,iektsg7f.xu9ymszd.centery,life=30))
    self.vw6m7b5c.remove(iektsg7f)
  self.q6p61xuf-=1
  if self.q6p61xuf<=0:
   self.q6p61xuf=bom5igqp*pi3qk2ia
   if len(self.vw6m7b5c)<r1yzoyn6:
    self.vw6m7b5c.append(u1ni10kq(self.player))
  if not self.wzs13c9x:
   for cu8el501 in self.qic1l7dy:
    self.jm25len6[cu8el501]-=1
    if self.jm25len6[cu8el501]<=0:
     un4regb1=self.player.hiac2e4q.get(cu8el501,1)
     lztkkfzz=mjh75lxo[cu8el501]*self.player.elwf90km*n8k03w0f(un4regb1)
     self.jm25len6[cu8el501]=max(4,int(lztkkfzz))
     size=uqjiujv6[cu8el501]['zhbgcj']
     v15cqzcu=self.player.uidlrye8*gdg1wjui(un4regb1)
     self.i20cv3tl.append(mvxdp5gj(cu8el501,self.player.xu9ymszd.centerx-size//2,self.player.xu9ymszd.centery-size//2,size,size,self.player.crsb4gf1['kj2jvq'],self.player.crsb4gf1['v00vhm'],v15cqzcu))
     jenvg3kk('th2p39',volume=0.5,min_interval_ms=90)
  su1hbj6t=min(isj6bw3b,d60fkhmy*(1+0.12*(self.player.a8ax40dt-1)))
  if random.random()<su1hbj6t:
   qdnai89y(self.nfn1r4kz,self.e1rhouu9)
  self.player.move()
  if self.player.a8ax40dt>self.xasez2nx:
   jenvg3kk('riny2e')
   if self.player.a8ax40dt<=len(c8yfbntp):
    wydmt8vt=c8yfbntp[self.player.a8ax40dt-1]
    if wydmt8vt not in self.e1rhouu9:
     self.e1rhouu9.append(wydmt8vt)
   self.xasez2nx=self.player.a8ax40dt
  if self.player.w4rcb1kj<=0:
   self.nyfkjfpn=True
  for kx74d0gj in self.nfn1r4kz:
   kx74d0gj.move(self.player)
   for kmgfxc08 in kx74d0gj.sv5f1bcp:
    kmgfxc08.move(self.player)
    kmgfxc08.g11kerpe(self.nfn1r4kz,self.vt26ys44,self.i20cv3tl,player=self.player,target='player')
   kx74d0gj.sv5f1bcp=[am2vajep for am2vajep in kx74d0gj.sv5f1bcp if not am2vajep.jqxs6esj]
  for wehlxslg in self.rmm1zxyv:
   wehlxslg.move(self.player)
  for bllo3rbx in self.i20cv3tl:
   bllo3rbx.move(self.player,o9ros7yt(self.nfn1r4kz,bllo3rbx))
   bllo3rbx.g11kerpe(self.nfn1r4kz,self.vt26ys44,self.i20cv3tl)
  for kx74d0gj in self.nfn1r4kz:
   for(r98s4c3b,cx41dntc,mqxlm5q2,xuu13i59)in kx74d0gj.eehou6ql:
    self.mabkae6a.append(zgomf9pm(r98s4c3b,cx41dntc,mqxlm5q2,self.kt94ow3l,color=xuu13i59))
    jenvg3kk('ozdcuj',volume=0.4,min_interval_ms=60)
   kx74d0gj.eehou6ql.clear()
  for uz6kf162 in self.vt26ys44[:]:
   uz6kf162['futios']+=uz6kf162['kj2jvq']
   uz6kf162['hipi78']+=uz6kf162['v00vhm']
   uz6kf162['r7myow']-=1
   if uz6kf162['r7myow']<=0:
    self.vt26ys44.remove(uz6kf162)
  for wigbiaf9 in self.mabkae6a[:]:
   wigbiaf9['r7myow']-=1
   if wigbiaf9['r7myow']<=0:
    self.mabkae6a.remove(wigbiaf9)
  for u0q0mftg in self.fddfgs3j[:]:
   u0q0mftg.update()
   if u0q0mftg.jqxs6esj():
    self.fddfgs3j.remove(u0q0mftg)
 def uva2ieuc(self):
  if self.z3olfark is None:
   zflse45b=[]
   for qjcjn997 in uqjiujv6:
    if qjcjn997=='x2s8nn':
     continue
    if qjcjn997 not in self.qic1l7dy:
     zflse45b.append(('n5nhqr',qjcjn997))
   for qjcjn997 in self.qic1l7dy:
    if self.player.hiac2e4q.get(qjcjn997,1)<ygspk9p3:
     zflse45b.append(('sce4qg',qjcjn997))
   for k in oohp6vz4:
    if self.player.w2kql0ht.get(k,0)<oohp6vz4[k]['ykht8x']:
     zflse45b.append(('ujqigy',k))
   if not zflse45b:
    self.player.zpfb3hn1=False
   else:
    random.shuffle(zflse45b)
    rk8r2ykc=zflse45b[:3]
    do2m71hs=120*len(rk8r2ykc)+20
    self.z3olfark=yur7ko64(400,do2m71hs+yur7ko64.rla5ju9b,hyihair4,title='LEVEL UP! Choose an upgrade',title_font=self.no0u93mz)
    z9toqw9j=do2m71hs//len(rk8r2ykc)
    qbbz2sf6=self.z3olfark.xu9ymszd.y+self.z3olfark.arhnuxor
    for(je11e9ft,(kind,key))in enumerate(rk8r2ykc):
     if kind=='n5nhqr':
      title=f'NEW WEAPON: {uyhl1c32[key]}'
      subtitle='Unlock this weapon'
     elif kind=='sce4qg':
      vk3g84ut=self.player.hiac2e4q.get(key,1)
      title=f'{uyhl1c32[key]}  Lv.{vk3g84ut} -> {vk3g84ut + 1}'
      subtitle='+12% damage, faster cooldown'
     else:
      vk3g84ut=self.player.w2kql0ht.get(key,0)
      title=f"{oohp6vz4[key]['yrp422']}  Lv.{vk3g84ut} -> {vk3g84ut + 1}"
      subtitle=oohp6vz4[key]['rw8p74']
     hugysm8t=hc58drc1(self.z3olfark.xu9ymszd.x+12,qbbz2sf6+je11e9ft*z9toqw9j+6,self.z3olfark.xu9ymszd.width-24,z9toqw9j-12,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,self.clkqzfpq,title,12,subtitle=subtitle,sub_font=self.sfu38gl2,kind=kind,key=key)
     self.z3olfark.add(hugysm8t)
  if self.z3olfark is not None:
   for qhkc856w in self.z3olfark.q5amln4p:
    qhkc856w.update(self.s4rxyj38)
    if qhkc856w.bfoqmf5l:
     if qhkc856w.kind=='n5nhqr':
      self.qic1l7dy.append(qhkc856w.key)
      self.player.hiac2e4q[qhkc856w.key]=1
      self.jm25len6[qhkc856w.key]=mjh75lxo[qhkc856w.key]
     elif qhkc856w.kind=='sce4qg':
      self.player.qo6q0usw(qhkc856w.key)
     elif qhkc856w.kind=='ujqigy':
      self.player.duhxid4n(qhkc856w.key)
     self.player.zpfb3hn1=False
     self.z3olfark=None
 def b36htf4p(self,gxlk8wru):
  mq7nc85e(gxlk8wru,self)
 def rk43safy(self,gxlk8wru,l9enulqj):
  while True:
   mpdzp6lf=self.vpbwhvnz()
   if mpdzp6lf=='quit':
    return(self.gg7oq2zd,self.player.a8ax40dt,True)
   if mpdzp6lf=='restart':
    return(self.gg7oq2zd,self.player.a8ax40dt,False)
   self.update()
   self.b36htf4p(gxlk8wru)
   pygame.display.flip()
   l9enulqj.tick(pi3qk2ia)
def gj29yfc2(uwxrum2l,gxlk8wru,l9enulqj):
 return gokc1msy(uwxrum2l).rk43safy(gxlk8wru,l9enulqj)
