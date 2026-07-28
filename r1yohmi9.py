import pygame
from vnbnqbnx import*
from entities import mn89ltaj
from iheyce4q import oohp6vz4,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.bdgbk2l0=pygame.Rect(ygspk9p3//2-rqf5q14j//2,tp0lvsnu-90,rqf5q14j,rqf5q14j)
  self.w0p4e05q=yswjckjl
  self.rk8r2ykc=iq5c34dx['yl4zjd']
  self.ry181acj={'ktaq6u':0,'kp82kb':-1}
 def j0kgazu4(self):
  o4dd1vn8=pygame.key.get_pressed()
  b36htf4p=vhuds3qs=0
  if o4dd1vn8[pygame.K_UP]:
   vhuds3qs-=self.w0p4e05q
  if o4dd1vn8[pygame.K_DOWN]:
   vhuds3qs+=self.w0p4e05q
  if o4dd1vn8[pygame.K_LEFT]:
   b36htf4p-=self.w0p4e05q
  if o4dd1vn8[pygame.K_RIGHT]:
   b36htf4p+=self.w0p4e05q
  if b36htf4p!=0 and vhuds3qs!=0:
   b36htf4p*=0.707
   vhuds3qs*=0.707
  if b36htf4p!=0 or vhuds3qs!=0:
   self.ry181acj['ktaq6u']=b36htf4p
   self.ry181acj['kp82kb']=vhuds3qs
  self.bdgbk2l0.iimoe0sy+=b36htf4p
  self.bdgbk2l0.gdg1wjui+=vhuds3qs
  self.bdgbk2l0.iimoe0sy=max(0,min(self.bdgbk2l0.iimoe0sy,ygspk9p3-self.bdgbk2l0.width))
  self.bdgbk2l0.gdg1wjui=max(60,min(self.bdgbk2l0.gdg1wjui,tp0lvsnu-self.bdgbk2l0.height))
 def sygvwopl(self,g1b3d505):
  (iimoe0sy,gdg1wjui)=(self.bdgbk2l0.iimoe0sy,self.bdgbk2l0.gdg1wjui)
  (yuibrsz1,mfyb8dal)=(self.bdgbk2l0.centerx,self.bdgbk2l0.centery)
  t54piwzn=pygame.Surface((self.bdgbk2l0.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(t54piwzn,(0,0,0,80),t54piwzn.get_rect())
  g1b3d505.blit(t54piwzn,(yuibrsz1-t54piwzn.get_width()//2,gdg1wjui+self.bdgbk2l0.height-6))
  llxxezdu=pygame.Rect(iimoe0sy,gdg1wjui,self.bdgbk2l0.width,self.bdgbk2l0.height)
  pygame.draw.rect(g1b3d505,mn89ltaj(self.rk8r2ykc,0.55),llxxezdu,border_radius=10)
  bokzixza=llxxezdu.inflate(-5,-5)
  pygame.draw.rect(g1b3d505,self.rk8r2ykc,bokzixza,border_radius=8)
  sdeekgys=pygame.Rect(bokzixza.iimoe0sy+3,bokzixza.gdg1wjui+3,bokzixza.width//2,bokzixza.height//3)
  pygame.draw.rect(g1b3d505,mn89ltaj(self.rk8r2ykc,2.0),sdeekgys,border_radius=4)
  pygame.draw.rect(g1b3d505,(15,15,30),llxxezdu,width=2,border_radius=10)
class my6wktak:
 def __init__(self,wy0mahym,clkqzfpq,color,iimoe0sy,gdg1wjui):
  self.wy0mahym=wy0mahym
  self.clkqzfpq=clkqzfpq
  self.rk8r2ykc=color
  self.bdgbk2l0=pygame.Rect(iimoe0sy,gdg1wjui,34,34)
  self.je11e9ft=False
 def sygvwopl(self,g1b3d505,q7i6yuj7):
  t54piwzn=pygame.Surface((self.bdgbk2l0.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(t54piwzn,(0,0,0,70),t54piwzn.get_rect())
  g1b3d505.blit(t54piwzn,(self.bdgbk2l0.centerx-t54piwzn.get_width()//2,self.bdgbk2l0.bottom-4))
  llxxezdu=pygame.Rect(self.bdgbk2l0.iimoe0sy,self.bdgbk2l0.gdg1wjui,self.bdgbk2l0.width,self.bdgbk2l0.height)
  pygame.draw.rect(g1b3d505,mn89ltaj(self.rk8r2ykc,0.6),llxxezdu,border_radius=8)
  bokzixza=llxxezdu.inflate(-5,-5)
  pygame.draw.rect(g1b3d505,self.rk8r2ykc,bokzixza,border_radius=6)
  pygame.draw.rect(g1b3d505,(15,15,15),llxxezdu,width=2,border_radius=8)
  (yuibrsz1,mfyb8dal)=(self.bdgbk2l0.centerx,self.bdgbk2l0.centery)
  pygame.draw.circle(g1b3d505,iq5c34dx['mviifr'],(yuibrsz1-6,mfyb8dal-3),3)
  pygame.draw.circle(g1b3d505,iq5c34dx['mviifr'],(yuibrsz1+6,mfyb8dal-3),3)
  pygame.draw.circle(g1b3d505,iq5c34dx['m1v3zo'],(yuibrsz1-6,mfyb8dal-3),1)
  pygame.draw.circle(g1b3d505,iq5c34dx['m1v3zo'],(yuibrsz1+6,mfyb8dal-3),1)
  q5amln4p=q7i6yuj7.render(self.wy0mahym,True,(20,20,20))
  g1b3d505.blit(q5amln4p,(yuibrsz1-q5amln4p.get_width()//2,self.bdgbk2l0.gdg1wjui-20))
def zo3lqi7e():
 return[my6wktak('Vera','be2wnf',iq5c34dx['r3hxyj'],120,140),my6wktak('Duncan','ntxrgn',iq5c34dx['k7rrbe'],383,110),my6wktak('Mira','en1x2g',iq5c34dx['ew6tm2'],650,140)]
yex8fsv8={'be2wnf':'Vitality Shop - Vera','ntxrgn':'Combat Shop - Duncan','en1x2g':'Mobility Shop - Mira'}
def s7fbmenu(key,crsb4gf1):
 f55dmcxx=jsylztgx[key]
 return int(f55dmcxx['kk2y77']*f55dmcxx['l4f9ye']**crsb4gf1)
def zfb7r31q(rk43safy,clkqzfpq,v76ub7l8):
 (q7i6yuj7,ck7n3bfh,vhxs58yr,amcixdu1)=v76ub7l8
 o4dd1vn8=[k for(k,jslulzfy)in jsylztgx.items()if jslulzfy['w9mda9']==clkqzfpq]
 l9enulqj=110*len(o4dd1vn8)+20
 cknfu84x=oohp6vz4(420,l9enulqj+oohp6vz4.rla5ju9b+60,z0xkxwd8,title=yex8fsv8.get(clkqzfpq,'Shop'),title_font=vhxs58yr)
 hfb85p86=cknfu84x.bdgbk2l0.gdg1wjui+cknfu84x.vpbwhvnz
 nd6357oo=l9enulqj//len(o4dd1vn8)
 for(xd8wz42o,key)in enumerate(o4dd1vn8):
  f55dmcxx=jsylztgx[key]
  a8ax40dt=rk43safy['meta_upgrades'].get(key,0)
  dq2fa39e=a8ax40dt>=f55dmcxx['gbwcv6']
  if dq2fa39e:
   title=f"{f55dmcxx['kj2jvq']}  MAX LEVEL"
  else:
   pa8s8hmb=s7fbmenu(key,a8ax40dt)
   title=f"{f55dmcxx['kj2jvq']}  Lv.{a8ax40dt} -> {a8ax40dt + 1}   [{pa8s8hmb} res]"
  dzsedfqs=hc58drc1(cknfu84x.bdgbk2l0.iimoe0sy+12,hfb85p86+xd8wz42o*nd6357oo+6,cknfu84x.bdgbk2l0.width-24,nd6357oo-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,amcixdu1,title,12,subtitle=f55dmcxx['vcw2lb'],sub_font=ck7n3bfh,kind='meta',key=key)
  dzsedfqs.maxed=dq2fa39e
  cknfu84x.add(dzsedfqs)
 iektsg7f=hfb85p86+len(o4dd1vn8)*nd6357oo+12
 wi8skch8=hc58drc1(cknfu84x.bdgbk2l0.iimoe0sy+12,iektsg7f,cknfu84x.bdgbk2l0.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),amcixdu1,'Close (ESC)',10,kind='close',key=None)
 cknfu84x.add(wi8skch8)
 return cknfu84x
def q26yg3dx(g1b3d505,ep6beffl,rk43safy,kz1uu7zy):
 q7i6yuj7=pygame.font.SysFont('arial',22)
 ck7n3bfh=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 vhxs58yr=pygame.font.SysFont('arial',22,bold=True)
 amcixdu1=pygame.font.SysFont('arial',20,bold=True)
 arhnuxor=pygame.font.SysFont('arial',15)
 v76ub7l8=(q7i6yuj7,ck7n3bfh,vhxs58yr,amcixdu1)
 c0hpmnz1=zbqe7ckw()
 lgbpj4uf=zo3lqi7e()
 eehou6ql=pygame.Rect(ygspk9p3//2-70,tp0lvsnu-60,140,44)
 ytv3i12v=None
 uva2ieuc=None
 while True:
  kx74d0gj=pygame.event.get()
  for zqcootnj in kx74d0gj:
   if zqcootnj.type==pygame.QUIT:
    return'quit'
   if zqcootnj.type==pygame.KEYDOWN and zqcootnj.key==pygame.K_ESCAPE and ytv3i12v:
    ytv3i12v=None
    uva2ieuc=None
  if ytv3i12v is None:
   c0hpmnz1.j0kgazu4()
   tza7x73q=None
   for zorxdtg5 in lgbpj4uf:
    if c0hpmnz1.bdgbk2l0.colliderect(zorxdtg5.bdgbk2l0.inflate(24,24)):
     if not zorxdtg5.je11e9ft:
      tza7x73q=zorxdtg5
      zorxdtg5.je11e9ft=True
      break
    else:
     zorxdtg5.je11e9ft=False
   if tza7x73q:
    uva2ieuc=tza7x73q.clkqzfpq
    ytv3i12v=zfb7r31q(rk43safy,uva2ieuc,v76ub7l8)
   if c0hpmnz1.bdgbk2l0.colliderect(eehou6ql):
    return'start_game'
  else:
   for mq7nc85e in ytv3i12v.pcvsqame:
    mq7nc85e.update(kx74d0gj)
   oqse3tv1=next((ouuylaja for ouuylaja in ytv3i12v.pcvsqame if ouuylaja.oqse3tv1),None)
   if oqse3tv1 is not None:
    if oqse3tv1.kind=='close':
     ytv3i12v=None
     uva2ieuc=None
    elif oqse3tv1.kind=='meta'and(not getattr(oqse3tv1,'maxed',False)):
     key=oqse3tv1.key
     a8ax40dt=rk43safy['meta_upgrades'].get(key,0)
     pa8s8hmb=s7fbmenu(key,a8ax40dt)
     if rk43safy['resources']>=pa8s8hmb:
      rk43safy['resources']-=pa8s8hmb
      rk43safy['meta_upgrades'][key]=a8ax40dt+1
      kz1uu7zy(rk43safy)
      ytv3i12v=zfb7r31q(rk43safy,uva2ieuc,v76ub7l8)
  g1b3d505.fill((190,225,190))
  for nyfkjfpn in range(0,ygspk9p3,m7hv3izk):
   pygame.draw.line(g1b3d505,(160,205,160),(nyfkjfpn,0),(nyfkjfpn,tp0lvsnu),1)
  for o9ros7yt in range(0,tp0lvsnu,m7hv3izk):
   pygame.draw.line(g1b3d505,(160,205,160),(0,o9ros7yt),(ygspk9p3,o9ros7yt),1)
  pygame.draw.rect(g1b3d505,iq5c34dx['k7bpgy'],eehou6ql,border_radius=10)
  pygame.draw.rect(g1b3d505,(150,110,0),eehou6ql,width=3,border_radius=10)
  cqheyto5=ck7n3bfh.render('ENTER RUN',True,(40,30,0))
  g1b3d505.blit(cqheyto5,(eehou6ql.centerx-cqheyto5.get_width()//2,eehou6ql.centery-cqheyto5.get_height()//2))
  for zorxdtg5 in lgbpj4uf:
   zorxdtg5.sygvwopl(g1b3d505,ck7n3bfh)
  c0hpmnz1.sygvwopl(g1b3d505)
  swwnc21o=pygame.Rect(12,12,220,40)
  xk7n8la1=pygame.Surface((swwnc21o.width,swwnc21o.height),pygame.SRCALPHA)
  pygame.draw.rect(xk7n8la1,(255,255,255,160),xk7n8la1.get_rect(),border_radius=10)
  g1b3d505.blit(xk7n8la1,swwnc21o.topleft)
  npcxa5s0=q7i6yuj7.render(f"Resources: {rk43safy['resources']}",True,(20,20,20))
  g1b3d505.blit(npcxa5s0,(20,22))
  ywcxz2ei=title_font.render('HOMEBASE',True,(20,40,20))
  g1b3d505.blit(ywcxz2ei,(ygspk9p3//2-ywcxz2ei.get_width()//2,12))
  ftrflqbm=arhnuxor.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  g1b3d505.blit(ftrflqbm,(ygspk9p3//2-ftrflqbm.get_width()//2,tp0lvsnu-105))
  if ytv3i12v:
   ytv3i12v.sygvwopl(g1b3d505)
  pygame.display.flip()
  ep6beffl.tick(pi3qk2ia)
