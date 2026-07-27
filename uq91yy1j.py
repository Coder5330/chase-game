import pygame
from i1arxabo import*
from entities import fd6rupw2
from o100vhmy import yswjckjl,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.todsx4nx=pygame.Rect(dtx63cfl//2-qqu7eeqt//2,rla5ju9b-90,qqu7eeqt,qqu7eeqt)
  self.mn89ltaj=rv86wzs3
  self.i20cv3tl=iq5c34dx['m1v3zo']
  self.i13n3bzt={'v9hbn5':0,'da7yvd':-1}
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
  self.todsx4nx.htgsiwg0=max(0,min(self.todsx4nx.htgsiwg0,dtx63cfl-self.todsx4nx.width))
  self.todsx4nx.hhl1737s=max(60,min(self.todsx4nx.hhl1737s,rla5ju9b-self.todsx4nx.height))
 def sl65wvjx(self,tj0nmeoq):
  (htgsiwg0,hhl1737s)=(self.todsx4nx.htgsiwg0,self.todsx4nx.hhl1737s)
  (wi8skch8,iektsg7f)=(self.todsx4nx.centerx,self.todsx4nx.centery)
  tby49e7e=pygame.Surface((self.todsx4nx.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(tby49e7e,(0,0,0,80),tby49e7e.get_rect())
  tj0nmeoq.blit(tby49e7e,(wi8skch8-tby49e7e.get_width()//2,hhl1737s+self.todsx4nx.height-6))
  c0hpmnz1=pygame.Rect(htgsiwg0,hhl1737s,self.todsx4nx.width,self.todsx4nx.height)
  pygame.draw.rect(tj0nmeoq,fd6rupw2(self.i20cv3tl,0.55),c0hpmnz1,border_radius=10)
  gqj5sxvw=c0hpmnz1.inflate(-5,-5)
  pygame.draw.rect(tj0nmeoq,self.i20cv3tl,gqj5sxvw,border_radius=8)
  damdvlnk=pygame.Rect(gqj5sxvw.htgsiwg0+3,gqj5sxvw.hhl1737s+3,gqj5sxvw.width//2,gqj5sxvw.height//3)
  pygame.draw.rect(tj0nmeoq,fd6rupw2(self.i20cv3tl,2.0),damdvlnk,border_radius=4)
  pygame.draw.rect(tj0nmeoq,(15,15,30),c0hpmnz1,width=2,border_radius=10)
class gncxll4z:
 def __init__(self,gqq4d3kz,qbm1enf3,color,htgsiwg0,hhl1737s):
  self.gqq4d3kz=gqq4d3kz
  self.qbm1enf3=qbm1enf3
  self.i20cv3tl=color
  self.todsx4nx=pygame.Rect(htgsiwg0,hhl1737s,34,34)
  self.nvuprt77=False
 def sl65wvjx(self,tj0nmeoq,qhkc856w):
  tby49e7e=pygame.Surface((self.todsx4nx.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(tby49e7e,(0,0,0,70),tby49e7e.get_rect())
  tj0nmeoq.blit(tby49e7e,(self.todsx4nx.centerx-tby49e7e.get_width()//2,self.todsx4nx.bottom-4))
  c0hpmnz1=pygame.Rect(self.todsx4nx.htgsiwg0,self.todsx4nx.hhl1737s,self.todsx4nx.width,self.todsx4nx.height)
  pygame.draw.rect(tj0nmeoq,fd6rupw2(self.i20cv3tl,0.6),c0hpmnz1,border_radius=8)
  gqj5sxvw=c0hpmnz1.inflate(-5,-5)
  pygame.draw.rect(tj0nmeoq,self.i20cv3tl,gqj5sxvw,border_radius=6)
  pygame.draw.rect(tj0nmeoq,(15,15,15),c0hpmnz1,width=2,border_radius=8)
  (wi8skch8,iektsg7f)=(self.todsx4nx.centerx,self.todsx4nx.centery)
  pygame.draw.circle(tj0nmeoq,iq5c34dx['m314cq'],(wi8skch8-6,iektsg7f-3),3)
  pygame.draw.circle(tj0nmeoq,iq5c34dx['m314cq'],(wi8skch8+6,iektsg7f-3),3)
  pygame.draw.circle(tj0nmeoq,iq5c34dx['no55ix'],(wi8skch8-6,iektsg7f-3),1)
  pygame.draw.circle(tj0nmeoq,iq5c34dx['no55ix'],(wi8skch8+6,iektsg7f-3),1)
  rk2u1rsu=qhkc856w.render(self.gqq4d3kz,True,(20,20,20))
  tj0nmeoq.blit(rk2u1rsu,(wi8skch8-rk2u1rsu.get_width()//2,self.todsx4nx.hhl1737s-20))
def k2ixivzk():
 return[gncxll4z('Vera','ktaq6u',iq5c34dx['dg4fbl'],120,140),gncxll4z('Duncan','ew6tm2',iq5c34dx['twvwvi'],383,110),gncxll4z('Mira','mviifr',iq5c34dx['amyrsv'],650,140)]
yex8fsv8={'ktaq6u':'Vitality Shop - Vera','ew6tm2':'Combat Shop - Duncan','mviifr':'Mobility Shop - Mira'}
def arml29q2(key,swwnc21o):
 gkz2u2tn=ibps3y70[key]
 return int(gkz2u2tn['r3hxyj']*gkz2u2tn['n7csuy']**swwnc21o)
def uww5wfcp(bdgbk2l0,qbm1enf3,nubmxnsz):
 (qhkc856w,t5sn961j,wb7f6fdh,wppsfnko)=nubmxnsz
 arhnuxor=[k for(k,j7f00ter)in ibps3y70.items()if j7f00ter['clslay']==qbm1enf3]
 x5m9j98c=110*len(arhnuxor)+20
 mfc79m96=yswjckjl(420,x5m9j98c+yswjckjl.gokc1msy+60,my6wktak,title=yex8fsv8.get(qbm1enf3,'Shop'),title_font=wb7f6fdh)
 uos0fb4y=mfc79m96.todsx4nx.hhl1737s+mfc79m96.m8lw2qit
 u3ifhv1x=x5m9j98c//len(arhnuxor)
 for(jo8e7flq,key)in enumerate(arhnuxor):
  gkz2u2tn=ibps3y70[key]
  nyrid3dn=bdgbk2l0['meta_upgrades'].get(key,0)
  b78okz1p=nyrid3dn>=gkz2u2tn['fkmuso']
  if b78okz1p:
   title=f"{gkz2u2tn['w1q8f6']}  MAX LEVEL"
  else:
   vqnpcenl=arml29q2(key,nyrid3dn)
   title=f"{gkz2u2tn['w1q8f6']}  Lv.{nyrid3dn} -> {nyrid3dn + 1}   [{vqnpcenl} res]"
  fcwtg1m8=hc58drc1(mfc79m96.todsx4nx.htgsiwg0+12,uos0fb4y+jo8e7flq*u3ifhv1x+6,mfc79m96.todsx4nx.width-24,u3ifhv1x-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,wppsfnko,title,12,subtitle=gkz2u2tn['j1f537'],sub_font=t5sn961j,kind='meta',key=key)
  fcwtg1m8.maxed=b78okz1p
  mfc79m96.add(fcwtg1m8)
 bllo3rbx=uos0fb4y+len(arhnuxor)*u3ifhv1x+12
 ugez7bh2=hc58drc1(mfc79m96.todsx4nx.htgsiwg0+12,bllo3rbx,mfc79m96.todsx4nx.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),wppsfnko,'Close (ESC)',10,kind='close',key=None)
 mfc79m96.add(ugez7bh2)
 return mfc79m96
def npejzhya(tj0nmeoq,ebt3g2qz,bdgbk2l0,qc06xq9j):
 qhkc856w=pygame.font.SysFont('arial',22)
 t5sn961j=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 wb7f6fdh=pygame.font.SysFont('arial',22,bold=True)
 wppsfnko=pygame.font.SysFont('arial',20,bold=True)
 cn7zrwqe=pygame.font.SysFont('arial',15)
 nubmxnsz=(qhkc856w,t5sn961j,wb7f6fdh,wppsfnko)
 reqy08p0=zbqe7ckw()
 zsw2292m=k2ixivzk()
 x6cnoljq=pygame.Rect(dtx63cfl//2-70,rla5ju9b-60,140,44)
 yw5py6b2=None
 bwiykid9=None
 while True:
  velos6zl=pygame.event.get()
  for yjluujmi in velos6zl:
   if yjluujmi.type==pygame.QUIT:
    return'quit'
   if yjluujmi.type==pygame.KEYDOWN and yjluujmi.key==pygame.K_ESCAPE and yw5py6b2:
    yw5py6b2=None
    bwiykid9=None
  if yw5py6b2 is None:
   reqy08p0.mcup8ijl()
   vm65q57t=None
   for jr5rdnpx in zsw2292m:
    if reqy08p0.todsx4nx.colliderect(jr5rdnpx.todsx4nx.inflate(24,24)):
     if not jr5rdnpx.nvuprt77:
      vm65q57t=jr5rdnpx
      jr5rdnpx.nvuprt77=True
      break
    else:
     jr5rdnpx.nvuprt77=False
   if vm65q57t:
    bwiykid9=vm65q57t.qbm1enf3
    yw5py6b2=uww5wfcp(bdgbk2l0,bwiykid9,nubmxnsz)
   if reqy08p0.todsx4nx.colliderect(x6cnoljq):
    return'start_game'
  else:
   for uidlrye8 in yw5py6b2.semqgy27:
    uidlrye8.update(velos6zl)
   amcixdu1=next((vt6om1fb for vt6om1fb in yw5py6b2.semqgy27 if vt6om1fb.amcixdu1),None)
   if amcixdu1 is not None:
    if amcixdu1.kind=='close':
     yw5py6b2=None
     bwiykid9=None
    elif amcixdu1.kind=='meta'and(not getattr(amcixdu1,'maxed',False)):
     key=amcixdu1.key
     nyrid3dn=bdgbk2l0['meta_upgrades'].get(key,0)
     vqnpcenl=arml29q2(key,nyrid3dn)
     if bdgbk2l0['resources']>=vqnpcenl:
      bdgbk2l0['resources']-=vqnpcenl
      bdgbk2l0['meta_upgrades'][key]=nyrid3dn+1
      qc06xq9j(bdgbk2l0)
      yw5py6b2=uww5wfcp(bdgbk2l0,bwiykid9,nubmxnsz)
  tj0nmeoq.fill((190,225,190))
  for fddfgs3j in range(0,dtx63cfl,b18hafey):
   pygame.draw.line(tj0nmeoq,(160,205,160),(fddfgs3j,0),(fddfgs3j,rla5ju9b),1)
  for mc8qizk3 in range(0,rla5ju9b,b18hafey):
   pygame.draw.line(tj0nmeoq,(160,205,160),(0,mc8qizk3),(dtx63cfl,mc8qizk3),1)
  pygame.draw.rect(tj0nmeoq,iq5c34dx['wdl5tg'],x6cnoljq,border_radius=10)
  pygame.draw.rect(tj0nmeoq,(150,110,0),x6cnoljq,width=3,border_radius=10)
  ncyh3fvl=t5sn961j.render('ENTER RUN',True,(40,30,0))
  tj0nmeoq.blit(ncyh3fvl,(x6cnoljq.centerx-ncyh3fvl.get_width()//2,x6cnoljq.centery-ncyh3fvl.get_height()//2))
  for jr5rdnpx in zsw2292m:
   jr5rdnpx.sl65wvjx(tj0nmeoq,t5sn961j)
  reqy08p0.sl65wvjx(tj0nmeoq)
  zpajssuu=pygame.Rect(12,12,220,40)
  onqyyf9r=pygame.Surface((zpajssuu.width,zpajssuu.height),pygame.SRCALPHA)
  pygame.draw.rect(onqyyf9r,(255,255,255,160),onqyyf9r.get_rect(),border_radius=10)
  tj0nmeoq.blit(onqyyf9r,zpajssuu.topleft)
  rgdej31g=qhkc856w.render(f"Resources: {bdgbk2l0['resources']}",True,(20,20,20))
  tj0nmeoq.blit(rgdej31g,(20,22))
  wfhj4d0j=title_font.render('HOMEBASE',True,(20,40,20))
  tj0nmeoq.blit(wfhj4d0j,(dtx63cfl//2-wfhj4d0j.get_width()//2,12))
  fekrcppr=cn7zrwqe.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  tj0nmeoq.blit(fekrcppr,(dtx63cfl//2-fekrcppr.get_width()//2,rla5ju9b-105))
  if yw5py6b2:
   yw5py6b2.sl65wvjx(tj0nmeoq)
  pygame.display.flip()
  ebt3g2qz.tick(pi3qk2ia)
