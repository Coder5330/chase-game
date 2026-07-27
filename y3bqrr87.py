import pygame
from o100vhmy import*
from entities import xwk2rv23
from j3wkcs4k import wa11dpg8,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.zflse45b=pygame.Rect(mqp49kwv//2-z0xkxwd8//2,rla5ju9b-90,z0xkxwd8,z0xkxwd8)
  self.k8qeoz0k=hyihair4
  self.ebt3g2qz=iq5c34dx['ehet25']
  self.sdeekgys={'kou83g':0,'k7rrbe':-1}
 def j1ldqnk2(self):
  gkz2u2tn=pygame.key.get_pressed()
  sl65wvjx=yuibrsz1=0
  if gkz2u2tn[pygame.K_UP]:
   yuibrsz1-=self.k8qeoz0k
  if gkz2u2tn[pygame.K_DOWN]:
   yuibrsz1+=self.k8qeoz0k
  if gkz2u2tn[pygame.K_LEFT]:
   sl65wvjx-=self.k8qeoz0k
  if gkz2u2tn[pygame.K_RIGHT]:
   sl65wvjx+=self.k8qeoz0k
  if sl65wvjx!=0 and yuibrsz1!=0:
   sl65wvjx*=0.707
   yuibrsz1*=0.707
  if sl65wvjx!=0 or yuibrsz1!=0:
   self.sdeekgys['kou83g']=sl65wvjx
   self.sdeekgys['k7rrbe']=yuibrsz1
  self.zflse45b.rm0j36tc+=sl65wvjx
  self.zflse45b.tza7x73q+=yuibrsz1
  self.zflse45b.rm0j36tc=max(0,min(self.zflse45b.rm0j36tc,mqp49kwv-self.zflse45b.width))
  self.zflse45b.tza7x73q=max(60,min(self.zflse45b.tza7x73q,rla5ju9b-self.zflse45b.height))
 def i01nouht(self,npejzhya):
  (rm0j36tc,tza7x73q)=(self.zflse45b.rm0j36tc,self.zflse45b.tza7x73q)
  (lztkkfzz,f2sehe2a)=(self.zflse45b.centerx,self.zflse45b.centery)
  gmoft6yr=pygame.Surface((self.zflse45b.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(gmoft6yr,(0,0,0,80),gmoft6yr.get_rect())
  npejzhya.blit(gmoft6yr,(lztkkfzz-gmoft6yr.get_width()//2,tza7x73q+self.zflse45b.height-6))
  duhxid4n=pygame.Rect(rm0j36tc,tza7x73q,self.zflse45b.width,self.zflse45b.height)
  pygame.draw.rect(npejzhya,xwk2rv23(self.ebt3g2qz,0.55),duhxid4n,border_radius=10)
  jo8e7flq=duhxid4n.inflate(-5,-5)
  pygame.draw.rect(npejzhya,self.ebt3g2qz,jo8e7flq,border_radius=8)
  mytn02yc=pygame.Rect(jo8e7flq.rm0j36tc+3,jo8e7flq.tza7x73q+3,jo8e7flq.width//2,jo8e7flq.height//3)
  pygame.draw.rect(npejzhya,xwk2rv23(self.ebt3g2qz,2.0),mytn02yc,border_radius=4)
  pygame.draw.rect(npejzhya,(15,15,30),duhxid4n,width=2,border_radius=10)
class gncxll4z:
 def __init__(self,a8ax40dt,llxxezdu,color,rm0j36tc,tza7x73q):
  self.a8ax40dt=a8ax40dt
  self.llxxezdu=llxxezdu
  self.ebt3g2qz=color
  self.zflse45b=pygame.Rect(rm0j36tc,tza7x73q,34,34)
  self.ftlpq2wg=False
 def i01nouht(self,npejzhya,le9oe941):
  gmoft6yr=pygame.Surface((self.zflse45b.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(gmoft6yr,(0,0,0,70),gmoft6yr.get_rect())
  npejzhya.blit(gmoft6yr,(self.zflse45b.centerx-gmoft6yr.get_width()//2,self.zflse45b.bottom-4))
  duhxid4n=pygame.Rect(self.zflse45b.rm0j36tc,self.zflse45b.tza7x73q,self.zflse45b.width,self.zflse45b.height)
  pygame.draw.rect(npejzhya,xwk2rv23(self.ebt3g2qz,0.6),duhxid4n,border_radius=8)
  jo8e7flq=duhxid4n.inflate(-5,-5)
  pygame.draw.rect(npejzhya,self.ebt3g2qz,jo8e7flq,border_radius=6)
  pygame.draw.rect(npejzhya,(15,15,15),duhxid4n,width=2,border_radius=8)
  (lztkkfzz,f2sehe2a)=(self.zflse45b.centerx,self.zflse45b.centery)
  pygame.draw.circle(npejzhya,iq5c34dx['ldz09w'],(lztkkfzz-6,f2sehe2a-3),3)
  pygame.draw.circle(npejzhya,iq5c34dx['ldz09w'],(lztkkfzz+6,f2sehe2a-3),3)
  pygame.draw.circle(npejzhya,iq5c34dx['vpd2ts'],(lztkkfzz-6,f2sehe2a-3),1)
  pygame.draw.circle(npejzhya,iq5c34dx['vpd2ts'],(lztkkfzz+6,f2sehe2a-3),1)
  semqgy27=le9oe941.render(self.a8ax40dt,True,(20,20,20))
  npejzhya.blit(semqgy27,(lztkkfzz-semqgy27.get_width()//2,self.zflse45b.tza7x73q-20))
def bokzixza():
 return[gncxll4z('Vera','hpvwzo',iq5c34dx['vmdk5n'],120,140),gncxll4z('Duncan','m314cq',iq5c34dx['h7kr0a'],383,110),gncxll4z('Mira','tudttj',iq5c34dx['vmwi9s'],650,140)]
yex8fsv8={'hpvwzo':'Vitality Shop - Vera','m314cq':'Combat Shop - Duncan','tudttj':'Mobility Shop - Mira'}
def e8zgvwwu(key,nd31k9qm):
 onqyyf9r=ibps3y70[key]
 return int(onqyyf9r['umfbuv']*onqyyf9r['dzjssz']**nd31k9qm)
def divsolml(xasez2nx,llxxezdu,jqzpniqf):
 (le9oe941,ukshy8nb,pf0i9g5d,j2vmcqbn)=jqzpniqf
 gkz2u2tn=[k for(k,zanouof0)in ibps3y70.items()if zanouof0['k7bpgy']==llxxezdu]
 bllo3rbx=110*len(gkz2u2tn)+20
 y8bv78hu=wa11dpg8(420,bllo3rbx+wa11dpg8.gokc1msy+60,my6wktak,title=yex8fsv8.get(llxxezdu,'Shop'),title_font=pf0i9g5d)
 jm25len6=y8bv78hu.zflse45b.tza7x73q+y8bv78hu.azc4xl99
 aqclpoxk=bllo3rbx//len(gkz2u2tn)
 for(nyfkjfpn,key)in enumerate(gkz2u2tn):
  onqyyf9r=ibps3y70[key]
  n3rlkte4=xasez2nx['meta_upgrades'].get(key,0)
  o4dd1vn8=n3rlkte4>=onqyyf9r['yl6lgj']
  if o4dd1vn8:
   title=f"{onqyyf9r['v9hbn5']}  MAX LEVEL"
  else:
   i20cv3tl=e8zgvwwu(key,n3rlkte4)
   title=f"{onqyyf9r['v9hbn5']}  Lv.{n3rlkte4} -> {n3rlkte4 + 1}   [{i20cv3tl} res]"
  rzs43c5b=hc58drc1(y8bv78hu.zflse45b.rm0j36tc+12,jm25len6+nyfkjfpn*aqclpoxk+6,y8bv78hu.zflse45b.width-24,aqclpoxk-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,j2vmcqbn,title,12,subtitle=onqyyf9r['clslay'],sub_font=ukshy8nb,kind='meta',key=key)
  rzs43c5b.maxed=o4dd1vn8
  y8bv78hu.add(rzs43c5b)
 hugysm8t=jm25len6+len(gkz2u2tn)*aqclpoxk+12
 pvasifpw=hc58drc1(y8bv78hu.zflse45b.rm0j36tc+12,hugysm8t,y8bv78hu.zflse45b.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),j2vmcqbn,'Close (ESC)',10,kind='close',key=None)
 y8bv78hu.add(pvasifpw)
 return y8bv78hu
def g1g1r1dw(npejzhya,d1ieixwc,xasez2nx,yg87oi0e):
 le9oe941=pygame.font.SysFont('arial',22)
 ukshy8nb=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 pf0i9g5d=pygame.font.SysFont('arial',22,bold=True)
 j2vmcqbn=pygame.font.SysFont('arial',20,bold=True)
 mpyxdw2z=pygame.font.SysFont('arial',15)
 jqzpniqf=(le9oe941,ukshy8nb,pf0i9g5d,j2vmcqbn)
 v982n2at=zbqe7ckw()
 dq2fa39e=bokzixza()
 trdhw9re=pygame.Rect(mqp49kwv//2-70,rla5ju9b-60,140,44)
 sld4d6af=None
 mnx39rbs=None
 while True:
  x875aud9=pygame.event.get()
  for fp47b42g in x875aud9:
   if fp47b42g.type==pygame.QUIT:
    return'quit'
   if fp47b42g.type==pygame.KEYDOWN and fp47b42g.key==pygame.K_ESCAPE and sld4d6af:
    sld4d6af=None
    mnx39rbs=None
  if sld4d6af is None:
   v982n2at.j1ldqnk2()
   lu7jae58=None
   for vk3g84ut in dq2fa39e:
    if v982n2at.zflse45b.colliderect(vk3g84ut.zflse45b.inflate(24,24)):
     if not vk3g84ut.ftlpq2wg:
      lu7jae58=vk3g84ut
      vk3g84ut.ftlpq2wg=True
      break
    else:
     vk3g84ut.ftlpq2wg=False
   if lu7jae58:
    mnx39rbs=lu7jae58.llxxezdu
    sld4d6af=divsolml(xasez2nx,mnx39rbs,jqzpniqf)
   if v982n2at.zflse45b.colliderect(trdhw9re):
    return'start_game'
  else:
   for rmm1zxyv in sld4d6af.gsmdzqcb:
    rmm1zxyv.update(x875aud9)
   tacj4t0s=next((mfyb8dal for mfyb8dal in sld4d6af.gsmdzqcb if mfyb8dal.tacj4t0s),None)
   if tacj4t0s is not None:
    if tacj4t0s.kind=='close':
     sld4d6af=None
     mnx39rbs=None
    elif tacj4t0s.kind=='meta'and(not getattr(tacj4t0s,'maxed',False)):
     key=tacj4t0s.key
     n3rlkte4=xasez2nx['meta_upgrades'].get(key,0)
     i20cv3tl=e8zgvwwu(key,n3rlkte4)
     if xasez2nx['resources']>=i20cv3tl:
      xasez2nx['resources']-=i20cv3tl
      xasez2nx['meta_upgrades'][key]=n3rlkte4+1
      yg87oi0e(xasez2nx)
      sld4d6af=divsolml(xasez2nx,mnx39rbs,jqzpniqf)
  npejzhya.fill((190,225,190))
  for s4rxyj38 in range(0,mqp49kwv,ky20479t):
   pygame.draw.line(npejzhya,(160,205,160),(s4rxyj38,0),(s4rxyj38,rla5ju9b),1)
  for u0q0mftg in range(0,rla5ju9b,ky20479t):
   pygame.draw.line(npejzhya,(160,205,160),(0,u0q0mftg),(mqp49kwv,u0q0mftg),1)
  pygame.draw.rect(npejzhya,iq5c34dx['uuu9si'],trdhw9re,border_radius=10)
  pygame.draw.rect(npejzhya,(150,110,0),trdhw9re,width=3,border_radius=10)
  mu4fmpkx=ukshy8nb.render('ENTER RUN',True,(40,30,0))
  npejzhya.blit(mu4fmpkx,(trdhw9re.centerx-mu4fmpkx.get_width()//2,trdhw9re.centery-mu4fmpkx.get_height()//2))
  for vk3g84ut in dq2fa39e:
   vk3g84ut.i01nouht(npejzhya,ukshy8nb)
  v982n2at.i01nouht(npejzhya)
  mn7h9g1a=pygame.Rect(12,12,220,40)
  xqzpky32=pygame.Surface((mn7h9g1a.width,mn7h9g1a.height),pygame.SRCALPHA)
  pygame.draw.rect(xqzpky32,(255,255,255,160),xqzpky32.get_rect(),border_radius=10)
  npejzhya.blit(xqzpky32,mn7h9g1a.topleft)
  exvaj2k8=le9oe941.render(f"Resources: {xasez2nx['resources']}",True,(20,20,20))
  npejzhya.blit(exvaj2k8,(20,22))
  a1tbrwr9=title_font.render('HOMEBASE',True,(20,40,20))
  npejzhya.blit(a1tbrwr9,(mqp49kwv//2-a1tbrwr9.get_width()//2,12))
  m8lw2qit=mpyxdw2z.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  npejzhya.blit(m8lw2qit,(mqp49kwv//2-m8lw2qit.get_width()//2,rla5ju9b-105))
  if sld4d6af:
   sld4d6af.i01nouht(npejzhya)
  pygame.display.flip()
  d1ieixwc.tick(pi3qk2ia)
