import pygame
from z4w1arag import*
from entities import ukshy8nb
from eba9in2x import yswjckjl,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.cqheyto5=pygame.Rect(rrcbpljd//2-qqu7eeqt//2,rla5ju9b-90,qqu7eeqt,qqu7eeqt)
  self.q3n2qb6g=rv86wzs3
  self.iie0rnuj=iq5c34dx['pta5iv']
  self.swwnc21o={'w2lx2t':0,'mviifr':-1}
 def chx3d43e(self):
  rktlzkj4=pygame.key.get_pressed()
  fo75rh8l=uc1xi04b=0
  if rktlzkj4[pygame.K_UP]:
   uc1xi04b-=self.q3n2qb6g
  if rktlzkj4[pygame.K_DOWN]:
   uc1xi04b+=self.q3n2qb6g
  if rktlzkj4[pygame.K_LEFT]:
   fo75rh8l-=self.q3n2qb6g
  if rktlzkj4[pygame.K_RIGHT]:
   fo75rh8l+=self.q3n2qb6g
  if fo75rh8l!=0 and uc1xi04b!=0:
   fo75rh8l*=0.707
   uc1xi04b*=0.707
  if fo75rh8l!=0 or uc1xi04b!=0:
   self.swwnc21o['w2lx2t']=fo75rh8l
   self.swwnc21o['mviifr']=uc1xi04b
  self.cqheyto5.d5ixva1n+=fo75rh8l
  self.cqheyto5.nngmx1gm+=uc1xi04b
  self.cqheyto5.d5ixva1n=max(0,min(self.cqheyto5.d5ixva1n,rrcbpljd-self.cqheyto5.width))
  self.cqheyto5.nngmx1gm=max(60,min(self.cqheyto5.nngmx1gm,rla5ju9b-self.cqheyto5.height))
 def g8kk791z(self,cq2q4qer):
  (d5ixva1n,nngmx1gm)=(self.cqheyto5.d5ixva1n,self.cqheyto5.nngmx1gm)
  (l9enulqj,hfb85p86)=(self.cqheyto5.centerx,self.cqheyto5.centery)
  h4l1vznq=pygame.Surface((self.cqheyto5.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(h4l1vznq,(0,0,0,80),h4l1vznq.get_rect())
  cq2q4qer.blit(h4l1vznq,(l9enulqj-h4l1vznq.get_width()//2,nngmx1gm+self.cqheyto5.height-6))
  aqclpoxk=pygame.Rect(d5ixva1n,nngmx1gm,self.cqheyto5.width,self.cqheyto5.height)
  pygame.draw.rect(cq2q4qer,ukshy8nb(self.iie0rnuj,0.55),aqclpoxk,border_radius=10)
  rk2u1rsu=aqclpoxk.inflate(-5,-5)
  pygame.draw.rect(cq2q4qer,self.iie0rnuj,rk2u1rsu,border_radius=8)
  mn7h9g1a=pygame.Rect(rk2u1rsu.d5ixva1n+3,rk2u1rsu.nngmx1gm+3,rk2u1rsu.width//2,rk2u1rsu.height//3)
  pygame.draw.rect(cq2q4qer,ukshy8nb(self.iie0rnuj,2.0),mn7h9g1a,border_radius=4)
  pygame.draw.rect(cq2q4qer,(15,15,30),aqclpoxk,width=2,border_radius=10)
class gncxll4z:
 def __init__(self,jr5rdnpx,nd6357oo,color,d5ixva1n,nngmx1gm):
  self.jr5rdnpx=jr5rdnpx
  self.nd6357oo=nd6357oo
  self.iie0rnuj=color
  self.cqheyto5=pygame.Rect(d5ixva1n,nngmx1gm,34,34)
  self.cp91i3vm=False
 def g8kk791z(self,cq2q4qer,yrivh6t1):
  h4l1vznq=pygame.Surface((self.cqheyto5.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(h4l1vznq,(0,0,0,70),h4l1vznq.get_rect())
  cq2q4qer.blit(h4l1vznq,(self.cqheyto5.centerx-h4l1vznq.get_width()//2,self.cqheyto5.bottom-4))
  aqclpoxk=pygame.Rect(self.cqheyto5.d5ixva1n,self.cqheyto5.nngmx1gm,self.cqheyto5.width,self.cqheyto5.height)
  pygame.draw.rect(cq2q4qer,ukshy8nb(self.iie0rnuj,0.6),aqclpoxk,border_radius=8)
  rk2u1rsu=aqclpoxk.inflate(-5,-5)
  pygame.draw.rect(cq2q4qer,self.iie0rnuj,rk2u1rsu,border_radius=6)
  pygame.draw.rect(cq2q4qer,(15,15,15),aqclpoxk,width=2,border_radius=8)
  (l9enulqj,hfb85p86)=(self.cqheyto5.centerx,self.cqheyto5.centery)
  pygame.draw.circle(cq2q4qer,iq5c34dx['lcf4mn'],(l9enulqj-6,hfb85p86-3),3)
  pygame.draw.circle(cq2q4qer,iq5c34dx['lcf4mn'],(l9enulqj+6,hfb85p86-3),3)
  pygame.draw.circle(cq2q4qer,iq5c34dx['wyn6sj'],(l9enulqj-6,hfb85p86-3),1)
  pygame.draw.circle(cq2q4qer,iq5c34dx['wyn6sj'],(l9enulqj+6,hfb85p86-3),1)
  w5iz31yr=yrivh6t1.render(self.jr5rdnpx,True,(20,20,20))
  cq2q4qer.blit(w5iz31yr,(l9enulqj-w5iz31yr.get_width()//2,self.cqheyto5.nngmx1gm-20))
def n04cdpqv():
 return[gncxll4z('Vera','en1x2g',iq5c34dx['uq0e27'],120,140),gncxll4z('Duncan','w2ugl6',iq5c34dx['w2zeeq'],383,110),gncxll4z('Mira','hzj7ub',iq5c34dx['ldz09w'],650,140)]
yex8fsv8={'en1x2g':'Vitality Shop - Vera','w2ugl6':'Combat Shop - Duncan','hzj7ub':'Mobility Shop - Mira'}
def ejbzutru(key,bokzixza):
 w4rcb1kj=ibps3y70[key]
 return int(w4rcb1kj['da7yvd']*w4rcb1kj['rpeqyd']**bokzixza)
def kybwmlun(tbxf445c,nd6357oo,mqxlm5q2):
 (yrivh6t1,mn89ltaj,co4busu9,giec4d14)=mqxlm5q2
 rktlzkj4=[k for(k,gsrtwlxd)in ibps3y70.items()if gsrtwlxd['o6d10a']==nd6357oo]
 cq6qdy4l=110*len(rktlzkj4)+20
 m3pt5r5r=yswjckjl(420,cq6qdy4l+yswjckjl.gokc1msy+60,my6wktak,title=yex8fsv8.get(nd6357oo,'Shop'),title_font=co4busu9)
 lztkkfzz=m3pt5r5r.cqheyto5.nngmx1gm+m3pt5r5r.cn7zrwqe
 bq349dxb=cq6qdy4l//len(rktlzkj4)
 for(semqgy27,key)in enumerate(rktlzkj4):
  w4rcb1kj=ibps3y70[key]
  ry181acj=tbxf445c['meta_upgrades'].get(key,0)
  sye0a4ab=ry181acj>=w4rcb1kj['t7wqp3']
  if sye0a4ab:
   title=f"{w4rcb1kj['ntxrgn']}  MAX LEVEL"
  else:
   ruq9e5co=ejbzutru(key,ry181acj)
   title=f"{w4rcb1kj['ntxrgn']}  Lv.{ry181acj} -> {ry181acj + 1}   [{ruq9e5co} res]"
  z0b6ugvs=hc58drc1(m3pt5r5r.cqheyto5.d5ixva1n+12,lztkkfzz+semqgy27*bq349dxb+6,m3pt5r5r.cqheyto5.width-24,bq349dxb-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,giec4d14,title,12,subtitle=w4rcb1kj['fkmuso'],sub_font=mn89ltaj,kind='meta',key=key)
  z0b6ugvs.maxed=sye0a4ab
  m3pt5r5r.add(z0b6ugvs)
 uos0fb4y=lztkkfzz+len(rktlzkj4)*bq349dxb+12
 x5m9j98c=hc58drc1(m3pt5r5r.cqheyto5.d5ixva1n+12,uos0fb4y,m3pt5r5r.cqheyto5.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),giec4d14,'Close (ESC)',10,kind='close',key=None)
 m3pt5r5r.add(x5m9j98c)
 return m3pt5r5r
def myrp5ge0(cq2q4qer,clkqzfpq,tbxf445c,v0rxxf36):
 yrivh6t1=pygame.font.SysFont('arial',22)
 mn89ltaj=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 co4busu9=pygame.font.SysFont('arial',22,bold=True)
 giec4d14=pygame.font.SysFont('arial',20,bold=True)
 o9ros7yt=pygame.font.SysFont('arial',15)
 mqxlm5q2=(yrivh6t1,mn89ltaj,co4busu9,giec4d14)
 i4fejgxa=zbqe7ckw()
 wg25cfzf=n04cdpqv()
 g5hcbbmh=pygame.Rect(rrcbpljd//2-70,rla5ju9b-60,140,44)
 ia529603=None
 diuu9k9x=None
 while True:
  ouuylaja=pygame.event.get()
  for vhuds3qs in ouuylaja:
   if vhuds3qs.type==pygame.QUIT:
    return'quit'
   if vhuds3qs.type==pygame.KEYDOWN and vhuds3qs.key==pygame.K_ESCAPE and ia529603:
    ia529603=None
    diuu9k9x=None
  if ia529603 is None:
   i4fejgxa.chx3d43e()
   arml29q2=None
   for bihsa7he in wg25cfzf:
    if i4fejgxa.cqheyto5.colliderect(bihsa7he.cqheyto5.inflate(24,24)):
     if not bihsa7he.cp91i3vm:
      arml29q2=bihsa7he
      bihsa7he.cp91i3vm=True
      break
    else:
     bihsa7he.cp91i3vm=False
   if arml29q2:
    diuu9k9x=arml29q2.nd6357oo
    ia529603=kybwmlun(tbxf445c,diuu9k9x,mqxlm5q2)
   if i4fejgxa.cqheyto5.colliderect(g5hcbbmh):
    return'start_game'
  else:
   for zefqjg02 in ia529603.i13n3bzt:
    zefqjg02.update(ouuylaja)
   i20cv3tl=next((fp47b42g for fp47b42g in ia529603.i13n3bzt if fp47b42g.i20cv3tl),None)
   if i20cv3tl is not None:
    if i20cv3tl.kind=='close':
     ia529603=None
     diuu9k9x=None
    elif i20cv3tl.kind=='meta'and(not getattr(i20cv3tl,'maxed',False)):
     key=i20cv3tl.key
     ry181acj=tbxf445c['meta_upgrades'].get(key,0)
     ruq9e5co=ejbzutru(key,ry181acj)
     if tbxf445c['resources']>=ruq9e5co:
      tbxf445c['resources']-=ruq9e5co
      tbxf445c['meta_upgrades'][key]=ry181acj+1
      v0rxxf36(tbxf445c)
      ia529603=kybwmlun(tbxf445c,diuu9k9x,mqxlm5q2)
  cq2q4qer.fill((190,225,190))
  for mytn02yc in range(0,rrcbpljd,y38daly8):
   pygame.draw.line(cq2q4qer,(160,205,160),(mytn02yc,0),(mytn02yc,rla5ju9b),1)
  for x9bp4m18 in range(0,rla5ju9b,y38daly8):
   pygame.draw.line(cq2q4qer,(160,205,160),(0,x9bp4m18),(rrcbpljd,x9bp4m18),1)
  pygame.draw.rect(cq2q4qer,iq5c34dx['amyrsv'],g5hcbbmh,border_radius=10)
  pygame.draw.rect(cq2q4qer,(150,110,0),g5hcbbmh,width=3,border_radius=10)
  zflse45b=mn89ltaj.render('ENTER RUN',True,(40,30,0))
  cq2q4qer.blit(zflse45b,(g5hcbbmh.centerx-zflse45b.get_width()//2,g5hcbbmh.centery-zflse45b.get_height()//2))
  for bihsa7he in wg25cfzf:
   bihsa7he.g8kk791z(cq2q4qer,mn89ltaj)
  i4fejgxa.g8kk791z(cq2q4qer)
  gkz2u2tn=pygame.Rect(12,12,220,40)
  gqj5sxvw=pygame.Surface((gkz2u2tn.width,gkz2u2tn.height),pygame.SRCALPHA)
  pygame.draw.rect(gqj5sxvw,(255,255,255,160),gqj5sxvw.get_rect(),border_radius=10)
  cq2q4qer.blit(gqj5sxvw,gkz2u2tn.topleft)
  jenvg3kk=yrivh6t1.render(f"Resources: {tbxf445c['resources']}",True,(20,20,20))
  cq2q4qer.blit(jenvg3kk,(20,22))
  vm65q57t=title_font.render('HOMEBASE',True,(20,40,20))
  cq2q4qer.blit(vm65q57t,(rrcbpljd//2-vm65q57t.get_width()//2,12))
  nyfkjfpn=o9ros7yt.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  cq2q4qer.blit(nyfkjfpn,(rrcbpljd//2-nyfkjfpn.get_width()//2,rla5ju9b-105))
  if ia529603:
   ia529603.g8kk791z(cq2q4qer)
  pygame.display.flip()
  clkqzfpq.tick(pi3qk2ia)
