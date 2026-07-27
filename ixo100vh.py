import pygame
from en1x2gdg import*
from entities import qc06xq9j
from p1onx0gu import wa11dpg8,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.f8rtm4j3=pygame.Rect(mqp49kwv//2-z0xkxwd8//2,rla5ju9b-90,z0xkxwd8,z0xkxwd8)
  self.kz1uu7zy=hyihair4
  self.ugez7bh2=iq5c34dx['xj2dg1']
  self.ftrflqbm={'lcf4mn':0,'r4uov5':-1}
 def y2f7atwy(self):
  semqgy27=pygame.key.get_pressed()
  mfyb8dal=eohswq40=0
  if semqgy27[pygame.K_UP]:
   eohswq40-=self.kz1uu7zy
  if semqgy27[pygame.K_DOWN]:
   eohswq40+=self.kz1uu7zy
  if semqgy27[pygame.K_LEFT]:
   mfyb8dal-=self.kz1uu7zy
  if semqgy27[pygame.K_RIGHT]:
   mfyb8dal+=self.kz1uu7zy
  if mfyb8dal!=0 and eohswq40!=0:
   mfyb8dal*=0.707
   eohswq40*=0.707
  if mfyb8dal!=0 or eohswq40!=0:
   self.ftrflqbm['lcf4mn']=mfyb8dal
   self.ftrflqbm['r4uov5']=eohswq40
  self.f8rtm4j3.qxb7gbdg+=mfyb8dal
  self.f8rtm4j3.n01uyzpd+=eohswq40
  self.f8rtm4j3.qxb7gbdg=max(0,min(self.f8rtm4j3.qxb7gbdg,mqp49kwv-self.f8rtm4j3.width))
  self.f8rtm4j3.n01uyzpd=max(60,min(self.f8rtm4j3.n01uyzpd,rla5ju9b-self.f8rtm4j3.height))
 def do2m71hs(self,gmoft6yr):
  (qxb7gbdg,n01uyzpd)=(self.f8rtm4j3.qxb7gbdg,self.f8rtm4j3.n01uyzpd)
  (ruq9e5co,wzs13c9x)=(self.f8rtm4j3.centerx,self.f8rtm4j3.centery)
  bdgbk2l0=pygame.Surface((self.f8rtm4j3.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(bdgbk2l0,(0,0,0,80),bdgbk2l0.get_rect())
  gmoft6yr.blit(bdgbk2l0,(ruq9e5co-bdgbk2l0.get_width()//2,n01uyzpd+self.f8rtm4j3.height-6))
  duhxid4n=pygame.Rect(qxb7gbdg,n01uyzpd,self.f8rtm4j3.width,self.f8rtm4j3.height)
  pygame.draw.rect(gmoft6yr,qc06xq9j(self.ugez7bh2,0.55),duhxid4n,border_radius=10)
  we4xyf9i=duhxid4n.inflate(-5,-5)
  pygame.draw.rect(gmoft6yr,self.ugez7bh2,we4xyf9i,border_radius=8)
  m8lw2qit=pygame.Rect(we4xyf9i.qxb7gbdg+3,we4xyf9i.n01uyzpd+3,we4xyf9i.width//2,we4xyf9i.height//3)
  pygame.draw.rect(gmoft6yr,qc06xq9j(self.ugez7bh2,2.0),m8lw2qit,border_radius=4)
  pygame.draw.rect(gmoft6yr,(15,15,30),duhxid4n,width=2,border_radius=10)
class gncxll4z:
 def __init__(self,qo6q0usw,llxxezdu,color,qxb7gbdg,n01uyzpd):
  self.qo6q0usw=qo6q0usw
  self.llxxezdu=llxxezdu
  self.ugez7bh2=color
  self.f8rtm4j3=pygame.Rect(qxb7gbdg,n01uyzpd,34,34)
  self.gkz2u2tn=False
 def do2m71hs(self,gmoft6yr,g70e3p15):
  bdgbk2l0=pygame.Surface((self.f8rtm4j3.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(bdgbk2l0,(0,0,0,70),bdgbk2l0.get_rect())
  gmoft6yr.blit(bdgbk2l0,(self.f8rtm4j3.centerx-bdgbk2l0.get_width()//2,self.f8rtm4j3.bottom-4))
  duhxid4n=pygame.Rect(self.f8rtm4j3.qxb7gbdg,self.f8rtm4j3.n01uyzpd,self.f8rtm4j3.width,self.f8rtm4j3.height)
  pygame.draw.rect(gmoft6yr,qc06xq9j(self.ugez7bh2,0.6),duhxid4n,border_radius=8)
  we4xyf9i=duhxid4n.inflate(-5,-5)
  pygame.draw.rect(gmoft6yr,self.ugez7bh2,we4xyf9i,border_radius=6)
  pygame.draw.rect(gmoft6yr,(15,15,15),duhxid4n,width=2,border_radius=8)
  (ruq9e5co,wzs13c9x)=(self.f8rtm4j3.centerx,self.f8rtm4j3.centery)
  pygame.draw.circle(gmoft6yr,iq5c34dx['pta5iv'],(ruq9e5co-6,wzs13c9x-3),3)
  pygame.draw.circle(gmoft6yr,iq5c34dx['pta5iv'],(ruq9e5co+6,wzs13c9x-3),3)
  pygame.draw.circle(gmoft6yr,iq5c34dx['ja9hl1'],(ruq9e5co-6,wzs13c9x-3),1)
  pygame.draw.circle(gmoft6yr,iq5c34dx['ja9hl1'],(ruq9e5co+6,wzs13c9x-3),1)
  nvuprt77=g70e3p15.render(self.qo6q0usw,True,(20,20,20))
  gmoft6yr.blit(nvuprt77,(ruq9e5co-nvuprt77.get_width()//2,self.f8rtm4j3.n01uyzpd-20))
def nyrid3dn():
 return[gncxll4z('Vera','t7wqp3',iq5c34dx['i563bt'],120,140),gncxll4z('Duncan','pswrgv',iq5c34dx['eplvqe'],383,110),gncxll4z('Mira','v3c71u',iq5c34dx['uet25l'],650,140)]
yex8fsv8={'t7wqp3':'Vitality Shop - Vera','pswrgv':'Combat Shop - Duncan','v3c71u':'Mobility Shop - Mira'}
def zanouof0(key,wvpw232u):
 gsmdzqcb=ibps3y70[key]
 return int(gsmdzqcb['dzjssz']*gsmdzqcb['wkgeq2']**wvpw232u)
def divsolml(nxxjve3d,llxxezdu,aicvqy5i):
 (g70e3p15,wd6r30oj,zdan085r,j2vmcqbn)=aicvqy5i
 semqgy27=[k for(k,ra9kepad)in ibps3y70.items()if ra9kepad['tcu9td']==llxxezdu]
 jm25len6=110*len(semqgy27)+20
 wy0mahym=wa11dpg8(420,jm25len6+wa11dpg8.gokc1msy+60,my6wktak,title=yex8fsv8.get(llxxezdu,'Shop'),title_font=zdan085r)
 xp8mgyn2=wy0mahym.f8rtm4j3.n01uyzpd+wy0mahym.v76ub7l8
 aqclpoxk=jm25len6//len(semqgy27)
 for(z8z3v6di,key)in enumerate(semqgy27):
  gsmdzqcb=ibps3y70[key]
  fpa8hyex=nxxjve3d['meta_upgrades'].get(key,0)
  wa45hvgo=fpa8hyex>=gsmdzqcb['bdoz6w']
  if wa45hvgo:
   title=f"{gsmdzqcb['tudttj']}  MAX LEVEL"
  else:
   clkqzfpq=zanouof0(key,fpa8hyex)
   title=f"{gsmdzqcb['tudttj']}  Lv.{fpa8hyex} -> {fpa8hyex + 1}   [{clkqzfpq} res]"
  rzs43c5b=hc58drc1(wy0mahym.f8rtm4j3.qxb7gbdg+12,xp8mgyn2+z8z3v6di*aqclpoxk+6,wy0mahym.f8rtm4j3.width-24,aqclpoxk-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,j2vmcqbn,title,12,subtitle=gsmdzqcb['rthy25'],sub_font=wd6r30oj,kind='meta',key=key)
  rzs43c5b.maxed=wa45hvgo
  wy0mahym.add(rzs43c5b)
 z9toqw9j=xp8mgyn2+len(semqgy27)*aqclpoxk+12
 hugysm8t=hc58drc1(wy0mahym.f8rtm4j3.qxb7gbdg+12,z9toqw9j,wy0mahym.f8rtm4j3.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),j2vmcqbn,'Close (ESC)',10,kind='close',key=None)
 wy0mahym.add(hugysm8t)
 return wy0mahym
def jenvg3kk(gmoft6yr,pvasifpw,nxxjve3d,npejzhya):
 g70e3p15=pygame.font.SysFont('arial',22)
 wd6r30oj=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 zdan085r=pygame.font.SysFont('arial',22,bold=True)
 j2vmcqbn=pygame.font.SysFont('arial',20,bold=True)
 jq1ddpus=pygame.font.SysFont('arial',15)
 aicvqy5i=(g70e3p15,wd6r30oj,zdan085r,j2vmcqbn)
 v982n2at=zbqe7ckw()
 chx3d43e=nyrid3dn()
 wydmt8vt=pygame.Rect(mqp49kwv//2-70,rla5ju9b-60,140,44)
 sld4d6af=None
 mnx39rbs=None
 while True:
  zefqjg02=pygame.event.get()
  for jqxs6esj in zefqjg02:
   if jqxs6esj.type==pygame.QUIT:
    return'quit'
   if jqxs6esj.type==pygame.KEYDOWN and jqxs6esj.key==pygame.K_ESCAPE and sld4d6af:
    sld4d6af=None
    mnx39rbs=None
  if sld4d6af is None:
   v982n2at.y2f7atwy()
   klkjxjq5=None
   for mnwxuj3a in chx3d43e:
    if v982n2at.f8rtm4j3.colliderect(mnwxuj3a.f8rtm4j3.inflate(24,24)):
     if not mnwxuj3a.gkz2u2tn:
      klkjxjq5=mnwxuj3a
      mnwxuj3a.gkz2u2tn=True
      break
    else:
     mnwxuj3a.gkz2u2tn=False
   if klkjxjq5:
    mnx39rbs=klkjxjq5.llxxezdu
    sld4d6af=divsolml(nxxjve3d,mnx39rbs,aicvqy5i)
   if v982n2at.f8rtm4j3.colliderect(wydmt8vt):
    return'start_game'
  else:
   for wzlm72je in sld4d6af.ftlpq2wg:
    wzlm72je.update(zefqjg02)
   d1ieixwc=next((wehlxslg for wehlxslg in sld4d6af.ftlpq2wg if wehlxslg.d1ieixwc),None)
   if d1ieixwc is not None:
    if d1ieixwc.kind=='close':
     sld4d6af=None
     mnx39rbs=None
    elif d1ieixwc.kind=='meta'and(not getattr(d1ieixwc,'maxed',False)):
     key=d1ieixwc.key
     fpa8hyex=nxxjve3d['meta_upgrades'].get(key,0)
     clkqzfpq=zanouof0(key,fpa8hyex)
     if nxxjve3d['resources']>=clkqzfpq:
      nxxjve3d['resources']-=clkqzfpq
      nxxjve3d['meta_upgrades'][key]=fpa8hyex+1
      npejzhya(nxxjve3d)
      sld4d6af=divsolml(nxxjve3d,mnx39rbs,aicvqy5i)
  gmoft6yr.fill((190,225,190))
  for r98s4c3b in range(0,mqp49kwv,ky20479t):
   pygame.draw.line(gmoft6yr,(160,205,160),(r98s4c3b,0),(r98s4c3b,rla5ju9b),1)
  for ao4izasn in range(0,rla5ju9b,ky20479t):
   pygame.draw.line(gmoft6yr,(160,205,160),(0,ao4izasn),(mqp49kwv,ao4izasn),1)
  pygame.draw.rect(gmoft6yr,iq5c34dx['t753ay'],wydmt8vt,border_radius=10)
  pygame.draw.rect(gmoft6yr,(150,110,0),wydmt8vt,width=3,border_radius=10)
  lgbpj4uf=wd6r30oj.render('ENTER RUN',True,(40,30,0))
  gmoft6yr.blit(lgbpj4uf,(wydmt8vt.centerx-lgbpj4uf.get_width()//2,wydmt8vt.centery-lgbpj4uf.get_height()//2))
  for mnwxuj3a in chx3d43e:
   mnwxuj3a.do2m71hs(gmoft6yr,wd6r30oj)
  v982n2at.do2m71hs(gmoft6yr)
  nyfkjfpn=pygame.Rect(12,12,220,40)
  o9ros7yt=pygame.Surface((nyfkjfpn.width,nyfkjfpn.height),pygame.SRCALPHA)
  pygame.draw.rect(o9ros7yt,(255,255,255,160),o9ros7yt.get_rect(),border_radius=10)
  gmoft6yr.blit(o9ros7yt,nyfkjfpn.topleft)
  tkyrmjlj=g70e3p15.render(f"Resources: {nxxjve3d['resources']}",True,(20,20,20))
  gmoft6yr.blit(tkyrmjlj,(20,22))
  kn5gjj8m=title_font.render('HOMEBASE',True,(20,40,20))
  gmoft6yr.blit(kn5gjj8m,(mqp49kwv//2-kn5gjj8m.get_width()//2,12))
  cjn2fomd=jq1ddpus.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  gmoft6yr.blit(cjn2fomd,(mqp49kwv//2-cjn2fomd.get_width()//2,rla5ju9b-105))
  if sld4d6af:
   sld4d6af.do2m71hs(gmoft6yr)
  pygame.display.flip()
  pvasifpw.tick(pi3qk2ia)
