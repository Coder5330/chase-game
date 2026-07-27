import pygame
from c8v341on import*
from entities import ytb9xxay
from sn9uzery import wa11dpg8,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.la3kkrzd=pygame.Rect(jdiuovw1//2-z0xkxwd8//2,rla5ju9b-90,z0xkxwd8,z0xkxwd8)
  self.qertb74r=hyihair4
  self.amcixdu1=iq5c34dx['msz6rv']
  self.gkz2u2tn={'tcu9td':0,'xy79kv':-1}
 def lnf74t60(self):
  we4xyf9i=pygame.key.get_pressed()
  qtzk3ny9=sl65wvjx=0
  if we4xyf9i[pygame.K_UP]:
   sl65wvjx-=self.qertb74r
  if we4xyf9i[pygame.K_DOWN]:
   sl65wvjx+=self.qertb74r
  if we4xyf9i[pygame.K_LEFT]:
   qtzk3ny9-=self.qertb74r
  if we4xyf9i[pygame.K_RIGHT]:
   qtzk3ny9+=self.qertb74r
  if qtzk3ny9!=0 and sl65wvjx!=0:
   qtzk3ny9*=0.707
   sl65wvjx*=0.707
  if qtzk3ny9!=0 or sl65wvjx!=0:
   self.gkz2u2tn['tcu9td']=qtzk3ny9
   self.gkz2u2tn['xy79kv']=sl65wvjx
  self.la3kkrzd.jh55hewl+=qtzk3ny9
  self.la3kkrzd.rm0j36tc+=sl65wvjx
  self.la3kkrzd.jh55hewl=max(0,min(self.la3kkrzd.jh55hewl,jdiuovw1-self.la3kkrzd.width))
  self.la3kkrzd.rm0j36tc=max(60,min(self.la3kkrzd.rm0j36tc,rla5ju9b-self.la3kkrzd.height))
 def pv4ykade(self,yg87oi0e):
  (jh55hewl,rm0j36tc)=(self.la3kkrzd.jh55hewl,self.la3kkrzd.rm0j36tc)
  (cq6qdy4l,lztkkfzz)=(self.la3kkrzd.centerx,self.la3kkrzd.centery)
  npejzhya=pygame.Surface((self.la3kkrzd.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(npejzhya,(0,0,0,80),npejzhya.get_rect())
  yg87oi0e.blit(npejzhya,(cq6qdy4l-npejzhya.get_width()//2,rm0j36tc+self.la3kkrzd.height-6))
  l57p6bkl=pygame.Rect(jh55hewl,rm0j36tc,self.la3kkrzd.width,self.la3kkrzd.height)
  pygame.draw.rect(yg87oi0e,ytb9xxay(self.amcixdu1,0.55),l57p6bkl,border_radius=10)
  vmxb9yo1=l57p6bkl.inflate(-5,-5)
  pygame.draw.rect(yg87oi0e,self.amcixdu1,vmxb9yo1,border_radius=8)
  sf337kuu=pygame.Rect(vmxb9yo1.jh55hewl+3,vmxb9yo1.rm0j36tc+3,vmxb9yo1.width//2,vmxb9yo1.height//3)
  pygame.draw.rect(yg87oi0e,ytb9xxay(self.amcixdu1,2.0),sf337kuu,border_radius=4)
  pygame.draw.rect(yg87oi0e,(15,15,30),l57p6bkl,width=2,border_radius=10)
class gncxll4z:
 def __init__(self,j1ldqnk2,i0x65muf,color,jh55hewl,rm0j36tc):
  self.j1ldqnk2=j1ldqnk2
  self.i0x65muf=i0x65muf
  self.amcixdu1=color
  self.la3kkrzd=pygame.Rect(jh55hewl,rm0j36tc,34,34)
  self.jo8e7flq=False
 def pv4ykade(self,yg87oi0e,mq7nc85e):
  npejzhya=pygame.Surface((self.la3kkrzd.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(npejzhya,(0,0,0,70),npejzhya.get_rect())
  yg87oi0e.blit(npejzhya,(self.la3kkrzd.centerx-npejzhya.get_width()//2,self.la3kkrzd.bottom-4))
  l57p6bkl=pygame.Rect(self.la3kkrzd.jh55hewl,self.la3kkrzd.rm0j36tc,self.la3kkrzd.width,self.la3kkrzd.height)
  pygame.draw.rect(yg87oi0e,ytb9xxay(self.amcixdu1,0.6),l57p6bkl,border_radius=8)
  vmxb9yo1=l57p6bkl.inflate(-5,-5)
  pygame.draw.rect(yg87oi0e,self.amcixdu1,vmxb9yo1,border_radius=6)
  pygame.draw.rect(yg87oi0e,(15,15,15),l57p6bkl,width=2,border_radius=8)
  (cq6qdy4l,lztkkfzz)=(self.la3kkrzd.centerx,self.la3kkrzd.centery)
  pygame.draw.circle(yg87oi0e,iq5c34dx['dq3b9s'],(cq6qdy4l-6,lztkkfzz-3),3)
  pygame.draw.circle(yg87oi0e,iq5c34dx['dq3b9s'],(cq6qdy4l+6,lztkkfzz-3),3)
  pygame.draw.circle(yg87oi0e,iq5c34dx['bhrdu4'],(cq6qdy4l-6,lztkkfzz-3),1)
  pygame.draw.circle(yg87oi0e,iq5c34dx['bhrdu4'],(cq6qdy4l+6,lztkkfzz-3),1)
  vpbwhvnz=mq7nc85e.render(self.j1ldqnk2,True,(20,20,20))
  yg87oi0e.blit(vpbwhvnz,(cq6qdy4l-vpbwhvnz.get_width()//2,self.la3kkrzd.rm0j36tc-20))
def zmybd2qe():
 return[gncxll4z('Vera','og8cd3',iq5c34dx['jgm32w'],120,140),gncxll4z('Duncan','e8a1ar',iq5c34dx['jayeqa'],383,110),gncxll4z('Mira','l226pa',iq5c34dx['g0ht1t'],650,140)]
yex8fsv8={'og8cd3':'Vitality Shop - Vera','e8a1ar':'Combat Shop - Duncan','l226pa':'Mobility Shop - Mira'}
def klkjxjq5(key,w4rcb1kj):
 z8z3v6di=ibps3y70[key]
 return int(z8z3v6di['ldz09w']*z8z3v6di['pta5iv']**w4rcb1kj)
def mal2w37d(jenvg3kk,i0x65muf,le9oe941):
 (mq7nc85e,pllkstn3,w8y72ivg,uww5wfcp)=le9oe941
 we4xyf9i=[k for(k,mlikwe4b)in ibps3y70.items()if mlikwe4b['fnn16u']==i0x65muf]
 ugez7bh2=110*len(we4xyf9i)+20
 jl90pxrl=wa11dpg8(420,ugez7bh2+wa11dpg8.gokc1msy+60,my6wktak,title=yex8fsv8.get(i0x65muf,'Shop'),title_font=w8y72ivg)
 bllo3rbx=jl90pxrl.la3kkrzd.rm0j36tc+jl90pxrl.cx41dntc
 rzs43c5b=ugez7bh2//len(we4xyf9i)
 for(kkzruin3,key)in enumerate(we4xyf9i):
  z8z3v6di=ibps3y70[key]
  swwnc21o=jenvg3kk['meta_upgrades'].get(key,0)
  nyrid3dn=swwnc21o>=z8z3v6di['yl4zjd']
  if nyrid3dn:
   title=f"{z8z3v6di['rthy25']}  MAX LEVEL"
  else:
   xp8mgyn2=klkjxjq5(key,swwnc21o)
   title=f"{z8z3v6di['rthy25']}  Lv.{swwnc21o} -> {swwnc21o + 1}   [{xp8mgyn2} res]"
  g11kerpe=hc58drc1(jl90pxrl.la3kkrzd.jh55hewl+12,bllo3rbx+kkzruin3*rzs43c5b+6,jl90pxrl.la3kkrzd.width-24,rzs43c5b-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,uww5wfcp,title,12,subtitle=z8z3v6di['dzjssz'],sub_font=pllkstn3,kind='meta',key=key)
  g11kerpe.maxed=nyrid3dn
  jl90pxrl.add(g11kerpe)
 pvasifpw=bllo3rbx+len(we4xyf9i)*rzs43c5b+12
 d1ieixwc=hc58drc1(jl90pxrl.la3kkrzd.jh55hewl+12,pvasifpw,jl90pxrl.la3kkrzd.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),uww5wfcp,'Close (ESC)',10,kind='close',key=None)
 jl90pxrl.add(d1ieixwc)
 return jl90pxrl
def cqheyto5(yg87oi0e,tacj4t0s,jenvg3kk,k1taa0i5):
 mq7nc85e=pygame.font.SysFont('arial',22)
 pllkstn3=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 w8y72ivg=pygame.font.SysFont('arial',22,bold=True)
 uww5wfcp=pygame.font.SysFont('arial',20,bold=True)
 m8lw2qit=pygame.font.SysFont('arial',15)
 le9oe941=(mq7nc85e,pllkstn3,w8y72ivg,uww5wfcp)
 x52qc1iy=zbqe7ckw()
 gqq4d3kz=zmybd2qe()
 wb7f6fdh=pygame.Rect(jdiuovw1//2-70,rla5ju9b-60,140,44)
 mnx39rbs=None
 win4olr6=None
 while True:
  fp47b42g=pygame.event.get()
  for uc1xi04b in fp47b42g:
   if uc1xi04b.type==pygame.QUIT:
    return'quit'
   if uc1xi04b.type==pygame.KEYDOWN and uc1xi04b.key==pygame.K_ESCAPE and mnx39rbs:
    mnx39rbs=None
    win4olr6=None
  if mnx39rbs is None:
   x52qc1iy.lnf74t60()
   kn5gjj8m=None
   for yvffqot8 in gqq4d3kz:
    if x52qc1iy.la3kkrzd.colliderect(yvffqot8.la3kkrzd.inflate(24,24)):
     if not yvffqot8.jo8e7flq:
      kn5gjj8m=yvffqot8
      yvffqot8.jo8e7flq=True
      break
    else:
     yvffqot8.jo8e7flq=False
   if kn5gjj8m:
    win4olr6=kn5gjj8m.i0x65muf
    mnx39rbs=mal2w37d(jenvg3kk,win4olr6,le9oe941)
   if x52qc1iy.la3kkrzd.colliderect(wb7f6fdh):
    return'start_game'
  else:
   for wehlxslg in mnx39rbs.zpajssuu:
    wehlxslg.update(fp47b42g)
   zfb7r31q=next((yuibrsz1 for yuibrsz1 in mnx39rbs.zpajssuu if yuibrsz1.zfb7r31q),None)
   if zfb7r31q is not None:
    if zfb7r31q.kind=='close':
     mnx39rbs=None
     win4olr6=None
    elif zfb7r31q.kind=='meta'and(not getattr(zfb7r31q,'maxed',False)):
     key=zfb7r31q.key
     swwnc21o=jenvg3kk['meta_upgrades'].get(key,0)
     xp8mgyn2=klkjxjq5(key,swwnc21o)
     if jenvg3kk['resources']>=xp8mgyn2:
      jenvg3kk['resources']-=xp8mgyn2
      jenvg3kk['meta_upgrades'][key]=swwnc21o+1
      k1taa0i5(jenvg3kk)
      mnx39rbs=mal2w37d(jenvg3kk,win4olr6,le9oe941)
  yg87oi0e.fill((190,225,190))
  for eatvzkhi in range(0,jdiuovw1,ky20479t):
   pygame.draw.line(yg87oi0e,(160,205,160),(eatvzkhi,0),(eatvzkhi,rla5ju9b),1)
  for s4rxyj38 in range(0,rla5ju9b,ky20479t):
   pygame.draw.line(yg87oi0e,(160,205,160),(0,s4rxyj38),(jdiuovw1,s4rxyj38),1)
  pygame.draw.rect(yg87oi0e,iq5c34dx['txb3n2'],wb7f6fdh,border_radius=10)
  pygame.draw.rect(yg87oi0e,(150,110,0),wb7f6fdh,width=3,border_radius=10)
  mfc79m96=pllkstn3.render('ENTER RUN',True,(40,30,0))
  yg87oi0e.blit(mfc79m96,(wb7f6fdh.centerx-mfc79m96.get_width()//2,wb7f6fdh.centery-mfc79m96.get_height()//2))
  for yvffqot8 in gqq4d3kz:
   yvffqot8.pv4ykade(yg87oi0e,pllkstn3)
  x52qc1iy.pv4ykade(yg87oi0e)
  a8lw2lm3=pygame.Rect(12,12,220,40)
  u9el8hl8=pygame.Surface((a8lw2lm3.width,a8lw2lm3.height),pygame.SRCALPHA)
  pygame.draw.rect(u9el8hl8,(255,255,255,160),u9el8hl8.get_rect(),border_radius=10)
  yg87oi0e.blit(u9el8hl8,a8lw2lm3.topleft)
  f8rtm4j3=mq7nc85e.render(f"Resources: {jenvg3kk['resources']}",True,(20,20,20))
  yg87oi0e.blit(f8rtm4j3,(20,22))
  arjn2hz2=title_font.render('HOMEBASE',True,(20,40,20))
  yg87oi0e.blit(arjn2hz2,(jdiuovw1//2-arjn2hz2.get_width()//2,12))
  x9bp4m18=m8lw2qit.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  yg87oi0e.blit(x9bp4m18,(jdiuovw1//2-x9bp4m18.get_width()//2,rla5ju9b-105))
  if mnx39rbs:
   mnx39rbs.pv4ykade(yg87oi0e)
  pygame.display.flip()
  tacj4t0s.tick(pi3qk2ia)
