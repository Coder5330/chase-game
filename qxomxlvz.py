import pygame
from entfk7or import*
from entities import y9ayq6ww
from x1l6spbn import oohp6vz4,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.npcxa5s0=pygame.Rect(ygspk9p3//2-rqf5q14j//2,tp0lvsnu-90,rqf5q14j,rqf5q14j)
  self.q6nqqb9l=yswjckjl
  self.pa8s8hmb=iq5c34dx['tjng7l']
  self.ls2zge2j={'nddqhk':0,'gbwcv6':-1}
 def oc4kl8cg(self):
  b78okz1p=pygame.key.get_pressed()
  mq7nc85e=le9oe941=0
  if b78okz1p[pygame.K_UP]:
   le9oe941-=self.q6nqqb9l
  if b78okz1p[pygame.K_DOWN]:
   le9oe941+=self.q6nqqb9l
  if b78okz1p[pygame.K_LEFT]:
   mq7nc85e-=self.q6nqqb9l
  if b78okz1p[pygame.K_RIGHT]:
   mq7nc85e+=self.q6nqqb9l
  if mq7nc85e!=0 and le9oe941!=0:
   mq7nc85e*=0.707
   le9oe941*=0.707
  if mq7nc85e!=0 or le9oe941!=0:
   self.ls2zge2j['nddqhk']=mq7nc85e
   self.ls2zge2j['gbwcv6']=le9oe941
  self.npcxa5s0.w2sq3b9s+=mq7nc85e
  self.npcxa5s0.owdz09wf+=le9oe941
  self.npcxa5s0.w2sq3b9s=max(0,min(self.npcxa5s0.w2sq3b9s,ygspk9p3-self.npcxa5s0.width))
  self.npcxa5s0.owdz09wf=max(60,min(self.npcxa5s0.owdz09wf,tp0lvsnu-self.npcxa5s0.height))
 def tnz61231(self,h8s2ftom):
  (w2sq3b9s,owdz09wf)=(self.npcxa5s0.w2sq3b9s,self.npcxa5s0.owdz09wf)
  (g8kk791z,wzlm72je)=(self.npcxa5s0.centerx,self.npcxa5s0.centery)
  byl68ntk=pygame.Surface((self.npcxa5s0.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(byl68ntk,(0,0,0,80),byl68ntk.get_rect())
  h8s2ftom.blit(byl68ntk,(g8kk791z-byl68ntk.get_width()//2,owdz09wf+self.npcxa5s0.height-6))
  yw6zbnz8=pygame.Rect(w2sq3b9s,owdz09wf,self.npcxa5s0.width,self.npcxa5s0.height)
  pygame.draw.rect(h8s2ftom,y9ayq6ww(self.pa8s8hmb,0.55),yw6zbnz8,border_radius=10)
  k2ixivzk=yw6zbnz8.inflate(-5,-5)
  pygame.draw.rect(h8s2ftom,self.pa8s8hmb,k2ixivzk,border_radius=8)
  i13n3bzt=pygame.Rect(k2ixivzk.w2sq3b9s+3,k2ixivzk.owdz09wf+3,k2ixivzk.width//2,k2ixivzk.height//3)
  pygame.draw.rect(h8s2ftom,y9ayq6ww(self.pa8s8hmb,2.0),i13n3bzt,border_radius=4)
  pygame.draw.rect(h8s2ftom,(15,15,30),yw6zbnz8,width=2,border_radius=10)
class my6wktak:
 def __init__(self,got7txkd,iie0rnuj,color,w2sq3b9s,owdz09wf):
  self.got7txkd=got7txkd
  self.iie0rnuj=iie0rnuj
  self.pa8s8hmb=color
  self.npcxa5s0=pygame.Rect(w2sq3b9s,owdz09wf,34,34)
  self.q5amln4p=False
 def tnz61231(self,h8s2ftom,m8lw2qit):
  byl68ntk=pygame.Surface((self.npcxa5s0.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(byl68ntk,(0,0,0,70),byl68ntk.get_rect())
  h8s2ftom.blit(byl68ntk,(self.npcxa5s0.centerx-byl68ntk.get_width()//2,self.npcxa5s0.bottom-4))
  yw6zbnz8=pygame.Rect(self.npcxa5s0.w2sq3b9s,self.npcxa5s0.owdz09wf,self.npcxa5s0.width,self.npcxa5s0.height)
  pygame.draw.rect(h8s2ftom,y9ayq6ww(self.pa8s8hmb,0.6),yw6zbnz8,border_radius=8)
  k2ixivzk=yw6zbnz8.inflate(-5,-5)
  pygame.draw.rect(h8s2ftom,self.pa8s8hmb,k2ixivzk,border_radius=6)
  pygame.draw.rect(h8s2ftom,(15,15,15),yw6zbnz8,width=2,border_radius=8)
  (g8kk791z,wzlm72je)=(self.npcxa5s0.centerx,self.npcxa5s0.centery)
  pygame.draw.circle(h8s2ftom,iq5c34dx['mmgvu4'],(g8kk791z-6,wzlm72je-3),3)
  pygame.draw.circle(h8s2ftom,iq5c34dx['mmgvu4'],(g8kk791z+6,wzlm72je-3),3)
  pygame.draw.circle(h8s2ftom,iq5c34dx['npva5k'],(g8kk791z-6,wzlm72je-3),1)
  pygame.draw.circle(h8s2ftom,iq5c34dx['npva5k'],(g8kk791z+6,wzlm72je-3),1)
  jxxgaear=m8lw2qit.render(self.got7txkd,True,(20,20,20))
  h8s2ftom.blit(jxxgaear,(g8kk791z-jxxgaear.get_width()//2,self.npcxa5s0.owdz09wf-20))
def mnwxuj3a():
 return[my6wktak('Vera','futios',iq5c34dx['s1whhk'],120,140),my6wktak('Duncan','pgsb98',iq5c34dx['ifzkic'],383,110),my6wktak('Mira','bohxs7',iq5c34dx['t6tbb6'],650,140)]
yex8fsv8={'futios':'Vitality Shop - Vera','pgsb98':'Combat Shop - Duncan','bohxs7':'Mobility Shop - Mira'}
def ceb8753a(key,xwqvr1h6):
 o4dd1vn8=jsylztgx[key]
 return int(o4dd1vn8['t00ucr']*o4dd1vn8['t7fr91']**xwqvr1h6)
def z9toqw9j(iaq7b7v1,iie0rnuj,mpyxdw2z):
 (m8lw2qit,sfu38gl2,z3olfark,xp8mgyn2)=mpyxdw2z
 b78okz1p=[k for(k,un9sz6rv)in jsylztgx.items()if un9sz6rv['fuxk0a']==iie0rnuj]
 i01nouht=110*len(b78okz1p)+20
 uz6kf162=oohp6vz4(420,i01nouht+oohp6vz4.rla5ju9b+60,z0xkxwd8,title=yex8fsv8.get(iie0rnuj,'Shop'),title_font=z3olfark)
 cnqt3wve=uz6kf162.npcxa5s0.owdz09wf+uz6kf162.nvuprt77
 pvasifpw=i01nouht//len(b78okz1p)
 for(pcvsqame,key)in enumerate(b78okz1p):
  o4dd1vn8=jsylztgx[key]
  gqq4d3kz=iaq7b7v1['meta_upgrades'].get(key,0)
  zsw2292m=gqq4d3kz>=o4dd1vn8['hrctlt']
  if zsw2292m:
   title=f"{o4dd1vn8['udt8cq']}  MAX LEVEL"
  else:
   qbbz2sf6=ceb8753a(key,gqq4d3kz)
   title=f"{o4dd1vn8['udt8cq']}  Lv.{gqq4d3kz} -> {gqq4d3kz + 1}   [{qbbz2sf6} res]"
  d1ieixwc=hc58drc1(uz6kf162.npcxa5s0.w2sq3b9s+12,cnqt3wve+pcvsqame*pvasifpw+6,uz6kf162.npcxa5s0.width-24,pvasifpw-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,xp8mgyn2,title,12,subtitle=o4dd1vn8['w9laac'],sub_font=sfu38gl2,kind='meta',key=key)
  d1ieixwc.maxed=zsw2292m
  uz6kf162.add(d1ieixwc)
 l9enulqj=cnqt3wve+len(b78okz1p)*pvasifpw+12
 bfoqmf5l=hc58drc1(uz6kf162.npcxa5s0.w2sq3b9s+12,l9enulqj,uz6kf162.npcxa5s0.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),xp8mgyn2,'Close (ESC)',10,kind='close',key=None)
 uz6kf162.add(bfoqmf5l)
 return uz6kf162
def gj29yfc2(h8s2ftom,rk8r2ykc,iaq7b7v1,f80ebkjf):
 m8lw2qit=pygame.font.SysFont('arial',22)
 sfu38gl2=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 z3olfark=pygame.font.SysFont('arial',22,bold=True)
 xp8mgyn2=pygame.font.SysFont('arial',20,bold=True)
 wvpw232u=pygame.font.SysFont('arial',15)
 mpyxdw2z=(m8lw2qit,sfu38gl2,z3olfark,xp8mgyn2)
 rzs43c5b=zbqe7ckw()
 x6cnoljq=mnwxuj3a()
 xsspye9r=pygame.Rect(ygspk9p3//2-70,tp0lvsnu-60,140,44)
 mpdzp6lf=None
 b06xkxb9=None
 while True:
  xq46nouh=pygame.event.get()
  for mqxlm5q2 in xq46nouh:
   if mqxlm5q2.type==pygame.QUIT:
    return'quit'
   if mqxlm5q2.type==pygame.KEYDOWN and mqxlm5q2.key==pygame.K_ESCAPE and mpdzp6lf:
    mpdzp6lf=None
    b06xkxb9=None
  if mpdzp6lf is None:
   rzs43c5b.oc4kl8cg()
   pg3yu6vk=None
   for ncyh3fvl in x6cnoljq:
    if rzs43c5b.npcxa5s0.colliderect(ncyh3fvl.npcxa5s0.inflate(24,24)):
     if not ncyh3fvl.q5amln4p:
      pg3yu6vk=ncyh3fvl
      ncyh3fvl.q5amln4p=True
      break
    else:
     ncyh3fvl.q5amln4p=False
   if pg3yu6vk:
    b06xkxb9=pg3yu6vk.iie0rnuj
    mpdzp6lf=z9toqw9j(iaq7b7v1,b06xkxb9,mpyxdw2z)
   if rzs43c5b.npcxa5s0.colliderect(xsspye9r):
    return'start_game'
  else:
   for boih5csk in mpdzp6lf.wa45hvgo:
    boih5csk.update(xq46nouh)
   u1jhuwb6=next((jqzpniqf for jqzpniqf in mpdzp6lf.wa45hvgo if jqzpniqf.u1jhuwb6),None)
   if u1jhuwb6 is not None:
    if u1jhuwb6.kind=='close':
     mpdzp6lf=None
     b06xkxb9=None
    elif u1jhuwb6.kind=='meta'and(not getattr(u1jhuwb6,'maxed',False)):
     key=u1jhuwb6.key
     gqq4d3kz=iaq7b7v1['meta_upgrades'].get(key,0)
     qbbz2sf6=ceb8753a(key,gqq4d3kz)
     if iaq7b7v1['resources']>=qbbz2sf6:
      iaq7b7v1['resources']-=qbbz2sf6
      iaq7b7v1['meta_upgrades'][key]=gqq4d3kz+1
      f80ebkjf(iaq7b7v1)
      mpdzp6lf=z9toqw9j(iaq7b7v1,b06xkxb9,mpyxdw2z)
  h8s2ftom.fill((190,225,190))
  for onqyyf9r in range(0,ygspk9p3,m7hv3izk):
   pygame.draw.line(h8s2ftom,(160,205,160),(onqyyf9r,0),(onqyyf9r,tp0lvsnu),1)
  for jo8e7flq in range(0,tp0lvsnu,m7hv3izk):
   pygame.draw.line(h8s2ftom,(160,205,160),(0,jo8e7flq),(ygspk9p3,jo8e7flq),1)
  pygame.draw.rect(h8s2ftom,iq5c34dx['qk0lth'],xsspye9r,border_radius=10)
  pygame.draw.rect(h8s2ftom,(150,110,0),xsspye9r,width=3,border_radius=10)
  jenvg3kk=sfu38gl2.render('ENTER RUN',True,(40,30,0))
  h8s2ftom.blit(jenvg3kk,(xsspye9r.centerx-jenvg3kk.get_width()//2,xsspye9r.centery-jenvg3kk.get_height()//2))
  for ncyh3fvl in x6cnoljq:
   ncyh3fvl.tnz61231(h8s2ftom,sfu38gl2)
  rzs43c5b.tnz61231(h8s2ftom)
  f55dmcxx=pygame.Rect(12,12,220,40)
  bokzixza=pygame.Surface((f55dmcxx.width,f55dmcxx.height),pygame.SRCALPHA)
  pygame.draw.rect(bokzixza,(255,255,255,160),bokzixza.get_rect(),border_radius=10)
  h8s2ftom.blit(bokzixza,f55dmcxx.topleft)
  uaobt328=m8lw2qit.render(f"Resources: {iaq7b7v1['resources']}",True,(20,20,20))
  h8s2ftom.blit(uaobt328,(20,22))
  htgsiwg0=title_font.render('HOMEBASE',True,(20,40,20))
  h8s2ftom.blit(htgsiwg0,(ygspk9p3//2-htgsiwg0.get_width()//2,12))
  cp91i3vm=wvpw232u.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  h8s2ftom.blit(cp91i3vm,(ygspk9p3//2-cp91i3vm.get_width()//2,tp0lvsnu-105))
  if mpdzp6lf:
   mpdzp6lf.tnz61231(h8s2ftom)
  pygame.display.flip()
  rk8r2ykc.tick(pi3qk2ia)
