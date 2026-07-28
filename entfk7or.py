import pygame
from ykatqyds import*
from entities import cb2uuijn
from pmpxkc5i import oohp6vz4,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.uaobt328=pygame.Rect(cqoldfor//2-rqf5q14j//2,tp0lvsnu-90,rqf5q14j,rqf5q14j)
  self.bf7so8w5=yswjckjl
  self.pa8s8hmb=iq5c34dx['wurvqt']
  self.crsb4gf1={'igc9ho':0,'urf1hx':-1}
 def mu4fmpkx(self):
  zflv1xxl=pygame.key.get_pressed()
  le9oe941=jqzpniqf=0
  if zflv1xxl[pygame.K_UP]:
   jqzpniqf-=self.bf7so8w5
  if zflv1xxl[pygame.K_DOWN]:
   jqzpniqf+=self.bf7so8w5
  if zflv1xxl[pygame.K_LEFT]:
   le9oe941-=self.bf7so8w5
  if zflv1xxl[pygame.K_RIGHT]:
   le9oe941+=self.bf7so8w5
  if le9oe941!=0 and jqzpniqf!=0:
   le9oe941*=0.707
   jqzpniqf*=0.707
  if le9oe941!=0 or jqzpniqf!=0:
   self.crsb4gf1['igc9ho']=le9oe941
   self.crsb4gf1['urf1hx']=jqzpniqf
  self.uaobt328.owdz09wf+=le9oe941
  self.uaobt328.lb4y4k7b+=jqzpniqf
  self.uaobt328.owdz09wf=max(0,min(self.uaobt328.owdz09wf,cqoldfor-self.uaobt328.width))
  self.uaobt328.lb4y4k7b=max(60,min(self.uaobt328.lb4y4k7b,tp0lvsnu-self.uaobt328.height))
 def v15cqzcu(self,u15pdtz9):
  (owdz09wf,lb4y4k7b)=(self.uaobt328.owdz09wf,self.uaobt328.lb4y4k7b)
  (wzlm72je,vt6om1fb)=(self.uaobt328.centerx,self.uaobt328.centery)
  uoloeazc=pygame.Surface((self.uaobt328.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(uoloeazc,(0,0,0,80),uoloeazc.get_rect())
  u15pdtz9.blit(uoloeazc,(wzlm72je-uoloeazc.get_width()//2,lb4y4k7b+self.uaobt328.height-6))
  uysal8m1=pygame.Rect(owdz09wf,lb4y4k7b,self.uaobt328.width,self.uaobt328.height)
  pygame.draw.rect(u15pdtz9,cb2uuijn(self.pa8s8hmb,0.55),uysal8m1,border_radius=10)
  ub68rerv=uysal8m1.inflate(-5,-5)
  pygame.draw.rect(u15pdtz9,self.pa8s8hmb,ub68rerv,border_radius=8)
  nd31k9qm=pygame.Rect(ub68rerv.owdz09wf+3,ub68rerv.lb4y4k7b+3,ub68rerv.width//2,ub68rerv.height//3)
  pygame.draw.rect(u15pdtz9,cb2uuijn(self.pa8s8hmb,2.0),nd31k9qm,border_radius=4)
  pygame.draw.rect(u15pdtz9,(15,15,30),uysal8m1,width=2,border_radius=10)
class my6wktak:
 def __init__(self,lgbpj4uf,uos0fb4y,color,owdz09wf,lb4y4k7b):
  self.lgbpj4uf=lgbpj4uf
  self.uos0fb4y=uos0fb4y
  self.pa8s8hmb=color
  self.uaobt328=pygame.Rect(owdz09wf,lb4y4k7b,34,34)
  self.b78okz1p=False
 def v15cqzcu(self,u15pdtz9,cjn2fomd):
  uoloeazc=pygame.Surface((self.uaobt328.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(uoloeazc,(0,0,0,70),uoloeazc.get_rect())
  u15pdtz9.blit(uoloeazc,(self.uaobt328.centerx-uoloeazc.get_width()//2,self.uaobt328.bottom-4))
  uysal8m1=pygame.Rect(self.uaobt328.owdz09wf,self.uaobt328.lb4y4k7b,self.uaobt328.width,self.uaobt328.height)
  pygame.draw.rect(u15pdtz9,cb2uuijn(self.pa8s8hmb,0.6),uysal8m1,border_radius=8)
  ub68rerv=uysal8m1.inflate(-5,-5)
  pygame.draw.rect(u15pdtz9,self.pa8s8hmb,ub68rerv,border_radius=6)
  pygame.draw.rect(u15pdtz9,(15,15,15),uysal8m1,width=2,border_radius=8)
  (wzlm72je,vt6om1fb)=(self.uaobt328.centerx,self.uaobt328.centery)
  pygame.draw.circle(u15pdtz9,iq5c34dx['kp82kb'],(wzlm72je-6,vt6om1fb-3),3)
  pygame.draw.circle(u15pdtz9,iq5c34dx['kp82kb'],(wzlm72je+6,vt6om1fb-3),3)
  pygame.draw.circle(u15pdtz9,iq5c34dx['utd0v2'],(wzlm72je-6,vt6om1fb-3),1)
  pygame.draw.circle(u15pdtz9,iq5c34dx['utd0v2'],(wzlm72je+6,vt6om1fb-3),1)
  d1b3jczu=cjn2fomd.render(self.lgbpj4uf,True,(20,20,20))
  u15pdtz9.blit(d1b3jczu,(wzlm72je-d1b3jczu.get_width()//2,self.uaobt328.lb4y4k7b-20))
def jr5rdnpx():
 return[my6wktak('Vera','jfquv9',iq5c34dx['oud2zd'],120,140),my6wktak('Duncan','rw8p74',iq5c34dx['kqbrmq'],383,110),my6wktak('Mira','zhbgcj',iq5c34dx['fkmuso'],650,140)]
yex8fsv8={'jfquv9':'Vitality Shop - Vera','rw8p74':'Combat Shop - Duncan','zhbgcj':'Mobility Shop - Mira'}
def cgsq7ait(key,a8ax40dt):
 wa45hvgo=jsylztgx[key]
 return int(wa45hvgo['hx0gu4']*wa45hvgo['kj2jvq']**a8ax40dt)
def d1ieixwc(q3n2qb6g,uos0fb4y,jq1ddpus):
 (cjn2fomd,qdnai89y,ljk4q5v7,ugez7bh2)=jq1ddpus
 zflv1xxl=[k for(k,ehet25lz)in jsylztgx.items()if ehet25lz['bx1ego']==uos0fb4y]
 i01nouht=110*len(zflv1xxl)+20
 v6xii5p5=oohp6vz4(420,i01nouht+oohp6vz4.rla5ju9b+60,z0xkxwd8,title=yex8fsv8.get(uos0fb4y,'Shop'),title_font=ljk4q5v7)
 cnqt3wve=v6xii5p5.uaobt328.lb4y4k7b+v6xii5p5.arhnuxor
 zfb7r31q=i01nouht//len(zflv1xxl)
 for(nyrid3dn,key)in enumerate(zflv1xxl):
  wa45hvgo=jsylztgx[key]
  mnwxuj3a=q3n2qb6g['meta_upgrades'].get(key,0)
  hu9n79gi=mnwxuj3a>=wa45hvgo['th2p39']
  if hu9n79gi:
   title=f"{wa45hvgo['rfu7bf']}  MAX LEVEL"
  else:
   qbbz2sf6=cgsq7ait(key,mnwxuj3a)
   title=f"{wa45hvgo['rfu7bf']}  Lv.{mnwxuj3a} -> {mnwxuj3a + 1}   [{qbbz2sf6} res]"
  li9nb74x=hc58drc1(v6xii5p5.uaobt328.owdz09wf+12,cnqt3wve+nyrid3dn*zfb7r31q+6,v6xii5p5.uaobt328.width-24,zfb7r31q-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,ugez7bh2,title,12,subtitle=wa45hvgo['yc1nlc'],sub_font=qdnai89y,kind='meta',key=key)
  li9nb74x.maxed=hu9n79gi
  v6xii5p5.add(li9nb74x)
 bfoqmf5l=cnqt3wve+len(zflv1xxl)*zfb7r31q+12
 rk8r2ykc=hc58drc1(v6xii5p5.uaobt328.owdz09wf+12,bfoqmf5l,v6xii5p5.uaobt328.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),ugez7bh2,'Close (ESC)',10,kind='close',key=None)
 v6xii5p5.add(rk8r2ykc)
 return v6xii5p5
def iaq7b7v1(u15pdtz9,u1jhuwb6,q3n2qb6g,byl68ntk):
 cjn2fomd=pygame.font.SysFont('arial',22)
 qdnai89y=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 ljk4q5v7=pygame.font.SysFont('arial',22,bold=True)
 ugez7bh2=pygame.font.SysFont('arial',20,bold=True)
 rktlzkj4=pygame.font.SysFont('arial',15)
 jq1ddpus=(cjn2fomd,qdnai89y,ljk4q5v7,ugez7bh2)
 sv5f1bcp=zbqe7ckw()
 vyb6li07=jr5rdnpx()
 nxxjve3d=pygame.Rect(cqoldfor//2-70,tp0lvsnu-60,140,44)
 i4fejgxa=None
 ytv3i12v=None
 while True:
  s4rxyj38=pygame.event.get()
  for eatvzkhi in s4rxyj38:
   if eatvzkhi.type==pygame.QUIT:
    return'quit'
   if eatvzkhi.type==pygame.KEYDOWN and eatvzkhi.key==pygame.K_ESCAPE and i4fejgxa:
    i4fejgxa=None
    ytv3i12v=None
  if i4fejgxa is None:
   sv5f1bcp.mu4fmpkx()
   e1rhouu9=None
   for njxurgow in vyb6li07:
    if sv5f1bcp.uaobt328.colliderect(njxurgow.uaobt328.inflate(24,24)):
     if not njxurgow.b78okz1p:
      e1rhouu9=njxurgow
      njxurgow.b78okz1p=True
      break
    else:
     njxurgow.b78okz1p=False
   if e1rhouu9:
    ytv3i12v=e1rhouu9.uos0fb4y
    i4fejgxa=d1ieixwc(q3n2qb6g,ytv3i12v,jq1ddpus)
   if sv5f1bcp.uaobt328.colliderect(nxxjve3d):
    return'start_game'
  else:
   for xuu13i59 in i4fejgxa.q5amln4p:
    xuu13i59.update(s4rxyj38)
   vw6m7b5c=next((g70e3p15 for g70e3p15 in i4fejgxa.q5amln4p if g70e3p15.vw6m7b5c),None)
   if vw6m7b5c is not None:
    if vw6m7b5c.kind=='close':
     i4fejgxa=None
     ytv3i12v=None
    elif vw6m7b5c.kind=='meta'and(not getattr(vw6m7b5c,'maxed',False)):
     key=vw6m7b5c.key
     mnwxuj3a=q3n2qb6g['meta_upgrades'].get(key,0)
     qbbz2sf6=cgsq7ait(key,mnwxuj3a)
     if q3n2qb6g['resources']>=qbbz2sf6:
      q3n2qb6g['resources']-=qbbz2sf6
      q3n2qb6g['meta_upgrades'][key]=mnwxuj3a+1
      byl68ntk(q3n2qb6g)
      i4fejgxa=d1ieixwc(q3n2qb6g,ytv3i12v,jq1ddpus)
  u15pdtz9.fill((190,225,190))
  for gsmdzqcb in range(0,cqoldfor,vve92mpn):
   pygame.draw.line(u15pdtz9,(160,205,160),(gsmdzqcb,0),(gsmdzqcb,tp0lvsnu),1)
  for we4xyf9i in range(0,tp0lvsnu,vve92mpn):
   pygame.draw.line(u15pdtz9,(160,205,160),(0,we4xyf9i),(cqoldfor,we4xyf9i),1)
  pygame.draw.rect(u15pdtz9,iq5c34dx['qye0qz'],nxxjve3d,border_radius=10)
  pygame.draw.rect(u15pdtz9,(150,110,0),nxxjve3d,width=3,border_radius=10)
  npejzhya=qdnai89y.render('ENTER RUN',True,(40,30,0))
  u15pdtz9.blit(npejzhya,(nxxjve3d.centerx-npejzhya.get_width()//2,nxxjve3d.centery-npejzhya.get_height()//2))
  for njxurgow in vyb6li07:
   njxurgow.v15cqzcu(u15pdtz9,qdnai89y)
  sv5f1bcp.v15cqzcu(u15pdtz9)
  bokzixza=pygame.Rect(12,12,220,40)
  pcvsqame=pygame.Surface((bokzixza.width,bokzixza.height),pygame.SRCALPHA)
  pygame.draw.rect(pcvsqame,(255,255,255,160),pcvsqame.get_rect(),border_radius=10)
  u15pdtz9.blit(pcvsqame,bokzixza.topleft)
  qertb74r=cjn2fomd.render(f"Resources: {q3n2qb6g['resources']}",True,(20,20,20))
  u15pdtz9.blit(qertb74r,(20,22))
  huh17j8q=title_font.render('HOMEBASE',True,(20,40,20))
  u15pdtz9.blit(huh17j8q,(cqoldfor//2-huh17j8q.get_width()//2,12))
  wvpw232u=rktlzkj4.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  u15pdtz9.blit(wvpw232u,(cqoldfor//2-wvpw232u.get_width()//2,tp0lvsnu-105))
  if i4fejgxa:
   i4fejgxa.v15cqzcu(u15pdtz9)
  pygame.display.flip()
  u1jhuwb6.tick(pi3qk2ia)
