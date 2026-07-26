import pygame
from ygm55ff1 import*
from entities import z3olfark
from py55p1v3 import rv86wzs3,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.zdan085r=pygame.Rect(qxaprpn6//2-cq5uznof//2,ibps3y70-90,cq5uznof,cq5uznof)
  self.qc06xq9j=wa11dpg8
  self.wppsfnko=iq5c34dx['fga0x7']
  self.u9el8hl8={'l2cwt0':0,'jchsdi':-1}
 def o4dd1vn8(self):
  fekrcppr=pygame.key.get_pressed()
  vw6m7b5c=u1jhuwb6=0
  if fekrcppr[pygame.K_UP]:
   u1jhuwb6-=self.qc06xq9j
  if fekrcppr[pygame.K_DOWN]:
   u1jhuwb6+=self.qc06xq9j
  if fekrcppr[pygame.K_LEFT]:
   vw6m7b5c-=self.qc06xq9j
  if fekrcppr[pygame.K_RIGHT]:
   vw6m7b5c+=self.qc06xq9j
  if vw6m7b5c!=0 and u1jhuwb6!=0:
   vw6m7b5c*=0.707
   u1jhuwb6*=0.707
  if vw6m7b5c!=0 or u1jhuwb6!=0:
   self.u9el8hl8['l2cwt0']=vw6m7b5c
   self.u9el8hl8['jchsdi']=u1jhuwb6
  self.zdan085r.yypp5zp7+=vw6m7b5c
  self.zdan085r.tjy1o2rn+=u1jhuwb6
  self.zdan085r.yypp5zp7=max(0,min(self.zdan085r.yypp5zp7,qxaprpn6-self.zdan085r.width))
  self.zdan085r.tjy1o2rn=max(60,min(self.zdan085r.tjy1o2rn,ibps3y70-self.zdan085r.height))
 def izhwy9he(self,uj64qhks):
  (yypp5zp7,tjy1o2rn)=(self.zdan085r.yypp5zp7,self.zdan085r.tjy1o2rn)
  (nd6357oo,li9nb74x)=(self.zdan085r.centerx,self.zdan085r.centery)
  no0u93mz=pygame.Surface((self.zdan085r.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(no0u93mz,(0,0,0,80),no0u93mz.get_rect())
  uj64qhks.blit(no0u93mz,(nd6357oo-no0u93mz.get_width()//2,tjy1o2rn+self.zdan085r.height-6))
  wkof8krd=pygame.Rect(yypp5zp7,tjy1o2rn,self.zdan085r.width,self.zdan085r.height)
  pygame.draw.rect(uj64qhks,z3olfark(self.wppsfnko,0.55),wkof8krd,border_radius=10)
  sf337kuu=wkof8krd.inflate(-5,-5)
  pygame.draw.rect(uj64qhks,self.wppsfnko,sf337kuu,border_radius=8)
  kx74d0gj=pygame.Rect(sf337kuu.yypp5zp7+3,sf337kuu.tjy1o2rn+3,sf337kuu.width//2,sf337kuu.height//3)
  pygame.draw.rect(uj64qhks,z3olfark(self.wppsfnko,2.0),kx74d0gj,border_radius=4)
  pygame.draw.rect(uj64qhks,(15,15,30),wkof8krd,width=2,border_radius=10)
class my6wktak:
 def __init__(self,k2ixivzk,c0hpmnz1,kybwmlun,yypp5zp7,tjy1o2rn):
  self.k2ixivzk=k2ixivzk
  self.c0hpmnz1=c0hpmnz1
  self.wppsfnko=kybwmlun
  self.zdan085r=pygame.Rect(yypp5zp7,tjy1o2rn,34,34)
  self.cjn2fomd=False
 def izhwy9he(self,uj64qhks,rzewviyt):
  no0u93mz=pygame.Surface((self.zdan085r.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(no0u93mz,(0,0,0,70),no0u93mz.get_rect())
  uj64qhks.blit(no0u93mz,(self.zdan085r.centerx-no0u93mz.get_width()//2,self.zdan085r.bottom-4))
  wkof8krd=pygame.Rect(self.zdan085r.yypp5zp7,self.zdan085r.tjy1o2rn,self.zdan085r.width,self.zdan085r.height)
  pygame.draw.rect(uj64qhks,z3olfark(self.wppsfnko,0.6),wkof8krd,border_radius=8)
  sf337kuu=wkof8krd.inflate(-5,-5)
  pygame.draw.rect(uj64qhks,self.wppsfnko,sf337kuu,border_radius=6)
  pygame.draw.rect(uj64qhks,(15,15,15),wkof8krd,width=2,border_radius=8)
  (nd6357oo,li9nb74x)=(self.zdan085r.centerx,self.zdan085r.centery)
  pygame.draw.circle(uj64qhks,iq5c34dx['d9zn9i'],(nd6357oo-6,li9nb74x-3),3)
  pygame.draw.circle(uj64qhks,iq5c34dx['d9zn9i'],(nd6357oo+6,li9nb74x-3),3)
  pygame.draw.circle(uj64qhks,iq5c34dx['tbn9ws'],(nd6357oo-6,li9nb74x-3),1)
  pygame.draw.circle(uj64qhks,iq5c34dx['tbn9ws'],(nd6357oo+6,li9nb74x-3),1)
  a8lw2lm3=rzewviyt.render(self.k2ixivzk,True,(20,20,20))
  uj64qhks.blit(a8lw2lm3,(nd6357oo-a8lw2lm3.get_width()//2,self.zdan085r.tjy1o2rn-20))
def sdeekgys():
 return[my6wktak('Vera','zcjn99',iq5c34dx['sbdfhj'],120,140),my6wktak('Duncan','xq5v4f',iq5c34dx['guxt9k'],383,110),my6wktak('Mira','ym5p7e',iq5c34dx['kyr06n'],650,140)]
yex8fsv8={'zcjn99':'Vitality Shop - Vera','xq5v4f':'Combat Shop - Duncan','ym5p7e':'Mobility Shop - Mira'}
def v24479qt(key,zpajssuu):
 v76ub7l8=jsylztgx[key]
 return int(v76ub7l8['lxz2ei']*v76ub7l8['qfkjna']**zpajssuu)
def am2vajep(vhxs58yr,c0hpmnz1,uidlrye8):
 (rzewviyt,yg87oi0e,tb4ldims,tp2ex5t5)=uidlrye8
 fekrcppr=[m20u9isy for(m20u9isy,w0p4e05q)in jsylztgx.items()if w0p4e05q['r212pg']==c0hpmnz1]
 llxxezdu=110*len(fekrcppr)+20
 gqq4d3kz=rv86wzs3(420,llxxezdu+rv86wzs3.tp0lvsnu+60,z0xkxwd8,title=yex8fsv8.get(c0hpmnz1,'Shop'),title_font=tb4ldims)
 u23y30ys=gqq4d3kz.zdan085r.tjy1o2rn+gqq4d3kz.xuu13i59
 ytv3i12v=llxxezdu//len(fekrcppr)
 for(mc8qizk3,key)in enumerate(fekrcppr):
  v76ub7l8=jsylztgx[key]
  vpbwhvnz=vhxs58yr['meta_upgrades'].get(key,0)
  rk2u1rsu=vpbwhvnz>=v76ub7l8['txb3n2']
  if rk2u1rsu:
   title=f"{v76ub7l8['eenui3']}  MAX LEVEL"
  else:
   giec4d14=v24479qt(key,vpbwhvnz)
   title=f"{v76ub7l8['eenui3']}  Lv.{vpbwhvnz} -> {vpbwhvnz + 1}   [{giec4d14} res]"
  uva2ieuc=hc58drc1(gqq4d3kz.zdan085r.yypp5zp7+12,u23y30ys+mc8qizk3*ytv3i12v+6,gqq4d3kz.zdan085r.width-24,ytv3i12v-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,tp2ex5t5,title,12,subtitle=v76ub7l8['cqxm06'],sub_font=yg87oi0e,kind='meta',key=key)
  uva2ieuc.maxed=rk2u1rsu
  gqq4d3kz.add(uva2ieuc)
 jc54wsqt=u23y30ys+len(fekrcppr)*ytv3i12v+12
 j2vmcqbn=hc58drc1(gqq4d3kz.zdan085r.yypp5zp7+12,jc54wsqt,gqq4d3kz.zdan085r.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),tp2ex5t5,'Close (ESC)',10,kind='close',key=None)
 gqq4d3kz.add(j2vmcqbn)
 return gqq4d3kz
def la3kkrzd(uj64qhks,uww5wfcp,vhxs58yr,cknfu84x):
 rzewviyt=pygame.font.SysFont('arial',22)
 yg87oi0e=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 tb4ldims=pygame.font.SysFont('arial',22,bold=True)
 tp2ex5t5=pygame.font.SysFont('arial',20,bold=True)
 yrivh6t1=pygame.font.SysFont('arial',15)
 uidlrye8=(rzewviyt,yg87oi0e,tb4ldims,tp2ex5t5)
 zs3kkv9r=zbqe7ckw()
 zflv1xxl=sdeekgys()
 a62c9t19=pygame.Rect(qxaprpn6//2-70,ibps3y70-60,140,44)
 ocij2v2h=None
 faqvkizz=None
 while True:
  qbbz2sf6=pygame.event.get()
  for do2m71hs in qbbz2sf6:
   if do2m71hs.type==pygame.QUIT:
    return'quit'
   if do2m71hs.type==pygame.KEYDOWN and do2m71hs.key==pygame.K_ESCAPE and ocij2v2h:
    ocij2v2h=None
    faqvkizz=None
  if ocij2v2h is None:
   zs3kkv9r.o4dd1vn8()
   cb2uuijn=None
   for mctwjlsh in zflv1xxl:
    if zs3kkv9r.zdan085r.colliderect(mctwjlsh.zdan085r.inflate(24,24)):
     if not mctwjlsh.cjn2fomd:
      cb2uuijn=mctwjlsh
      mctwjlsh.cjn2fomd=True
      break
    else:
     mctwjlsh.cjn2fomd=False
   if cb2uuijn:
    faqvkizz=cb2uuijn.c0hpmnz1
    ocij2v2h=am2vajep(vhxs58yr,faqvkizz,uidlrye8)
   if zs3kkv9r.zdan085r.colliderect(a62c9t19):
    return'start_game'
  else:
   for l9enulqj in ocij2v2h.mytn02yc:
    l9enulqj.update(qbbz2sf6)
   f8wquuy5=next((rk8r2ykc for rk8r2ykc in ocij2v2h.mytn02yc if rk8r2ykc.f8wquuy5),None)
   if f8wquuy5 is not None:
    if f8wquuy5.kind=='close':
     ocij2v2h=None
     faqvkizz=None
    elif f8wquuy5.kind=='meta'and(not getattr(f8wquuy5,'maxed',False)):
     key=f8wquuy5.key
     vpbwhvnz=vhxs58yr['meta_upgrades'].get(key,0)
     giec4d14=v24479qt(key,vpbwhvnz)
     if vhxs58yr['resources']>=giec4d14:
      vhxs58yr['resources']-=giec4d14
      vhxs58yr['meta_upgrades'][key]=vpbwhvnz+1
      cknfu84x(vhxs58yr)
      ocij2v2h=am2vajep(vhxs58yr,faqvkizz,uidlrye8)
  uj64qhks.fill((190,225,190))
  for b36htf4p in range(0,qxaprpn6,mvxdp5gj):
   pygame.draw.line(uj64qhks,(160,205,160),(b36htf4p,0),(b36htf4p,ibps3y70),1)
  for ouuylaja in range(0,ibps3y70,mvxdp5gj):
   pygame.draw.line(uj64qhks,(160,205,160),(0,ouuylaja),(qxaprpn6,ouuylaja),1)
  pygame.draw.rect(uj64qhks,iq5c34dx['lwr965'],a62c9t19,border_radius=10)
  pygame.draw.rect(uj64qhks,(150,110,0),a62c9t19,width=3,border_radius=10)
  r2muljav=yg87oi0e.render('ENTER RUN',True,(40,30,0))
  uj64qhks.blit(r2muljav,(a62c9t19.centerx-r2muljav.get_width()//2,a62c9t19.centery-r2muljav.get_height()//2))
  for mctwjlsh in zflv1xxl:
   mctwjlsh.izhwy9he(uj64qhks,yg87oi0e)
  zs3kkv9r.izhwy9he(uj64qhks)
  tw76xato=pygame.Rect(12,12,220,40)
  atj9a3y3=pygame.Surface((tw76xato.width,tw76xato.height),pygame.SRCALPHA)
  pygame.draw.rect(atj9a3y3,(255,255,255,160),atj9a3y3.get_rect(),border_radius=10)
  uj64qhks.blit(atj9a3y3,tw76xato.topleft)
  trdhw9re=rzewviyt.render(f"Resources: {vhxs58yr['resources']}",True,(20,20,20))
  uj64qhks.blit(trdhw9re,(20,22))
  y9ayq6ww=title_font.render('HOMEBASE',True,(20,40,20))
  uj64qhks.blit(y9ayq6ww,(qxaprpn6//2-y9ayq6ww.get_width()//2,12))
  g5l8a78e=yrivh6t1.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  uj64qhks.blit(g5l8a78e,(qxaprpn6//2-g5l8a78e.get_width()//2,ibps3y70-105))
  if ocij2v2h:
   ocij2v2h.izhwy9he(uj64qhks)
  pygame.display.flip()
  uww5wfcp.tick(gokc1msy)
