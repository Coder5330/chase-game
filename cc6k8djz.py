import pygame
from j1bmqf7z import*
from entities import y9ayq6ww
from k0b8y5dn import oohp6vz4,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.npcxa5s0=pygame.Rect(ygspk9p3//2-rqf5q14j//2,tp0lvsnu-90,rqf5q14j,rqf5q14j)
  self.p7b1ijiy=yswjckjl
  self.pv4ykade=iq5c34dx['swyqml']
  self.d1b3jczu={'rw8p74':0,'kj2jvq':-1}
 def move(self):
  mctwjlsh=pygame.key.get_pressed()
  le9oe941=jqzpniqf=0
  if mctwjlsh[pygame.K_UP]:
   jqzpniqf-=self.p7b1ijiy
  if mctwjlsh[pygame.K_DOWN]:
   jqzpniqf+=self.p7b1ijiy
  if mctwjlsh[pygame.K_LEFT]:
   le9oe941-=self.p7b1ijiy
  if mctwjlsh[pygame.K_RIGHT]:
   le9oe941+=self.p7b1ijiy
  if le9oe941!=0 and jqzpniqf!=0:
   le9oe941*=0.707
   jqzpniqf*=0.707
  if le9oe941!=0 or jqzpniqf!=0:
   self.d1b3jczu['rw8p74']=le9oe941
   self.d1b3jczu['kj2jvq']=jqzpniqf
  self.npcxa5s0.x+=le9oe941
  self.npcxa5s0.y+=jqzpniqf
  self.npcxa5s0.x=max(0,min(self.npcxa5s0.x,ygspk9p3-self.npcxa5s0.width))
  self.npcxa5s0.y=max(60,min(self.npcxa5s0.y,tp0lvsnu-self.npcxa5s0.height))
 def v15cqzcu(self,h8s2ftom):
  (x,y)=(self.npcxa5s0.x,self.npcxa5s0.y)
  (wzlm72je,vt6om1fb)=(self.npcxa5s0.centerx,self.npcxa5s0.centery)
  byl68ntk=pygame.Surface((self.npcxa5s0.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(byl68ntk,(0,0,0,80),byl68ntk.get_rect())
  h8s2ftom.blit(byl68ntk,(wzlm72je-byl68ntk.get_width()//2,y+self.npcxa5s0.height-6))
  tk0qtl3q=pygame.Rect(x,y,self.npcxa5s0.width,self.npcxa5s0.height)
  pygame.draw.rect(h8s2ftom,y9ayq6ww(self.pv4ykade,0.55),tk0qtl3q,border_radius=10)
  wa45hvgo=tk0qtl3q.inflate(-5,-5)
  pygame.draw.rect(h8s2ftom,self.pv4ykade,wa45hvgo,border_radius=8)
  nd31k9qm=pygame.Rect(wa45hvgo.x+3,wa45hvgo.y+3,wa45hvgo.width//2,wa45hvgo.height//3)
  pygame.draw.rect(h8s2ftom,y9ayq6ww(self.pv4ykade,2.0),nd31k9qm,border_radius=4)
  pygame.draw.rect(h8s2ftom,(15,15,30),tk0qtl3q,width=2,border_radius=10)
class my6wktak:
 def __init__(self,got7txkd,izhwy9he,color,x,y):
  self.got7txkd=got7txkd
  self.izhwy9he=izhwy9he
  self.pv4ykade=color
  self.npcxa5s0=pygame.Rect(x,y,34,34)
  self.ry181acj=False
 def v15cqzcu(self,h8s2ftom,mpyxdw2z):
  byl68ntk=pygame.Surface((self.npcxa5s0.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(byl68ntk,(0,0,0,70),byl68ntk.get_rect())
  h8s2ftom.blit(byl68ntk,(self.npcxa5s0.centerx-byl68ntk.get_width()//2,self.npcxa5s0.bottom-4))
  tk0qtl3q=pygame.Rect(self.npcxa5s0.x,self.npcxa5s0.y,self.npcxa5s0.width,self.npcxa5s0.height)
  pygame.draw.rect(h8s2ftom,y9ayq6ww(self.pv4ykade,0.6),tk0qtl3q,border_radius=8)
  wa45hvgo=tk0qtl3q.inflate(-5,-5)
  pygame.draw.rect(h8s2ftom,self.pv4ykade,wa45hvgo,border_radius=6)
  pygame.draw.rect(h8s2ftom,(15,15,15),tk0qtl3q,width=2,border_radius=8)
  (wzlm72je,vt6om1fb)=(self.npcxa5s0.centerx,self.npcxa5s0.centery)
  pygame.draw.circle(h8s2ftom,iq5c34dx['l4f9ye'],(wzlm72je-6,vt6om1fb-3),3)
  pygame.draw.circle(h8s2ftom,iq5c34dx['l4f9ye'],(wzlm72je+6,vt6om1fb-3),3)
  pygame.draw.circle(h8s2ftom,iq5c34dx['eff1bl'],(wzlm72je-6,vt6om1fb-3),1)
  pygame.draw.circle(h8s2ftom,iq5c34dx['eff1bl'],(wzlm72je+6,vt6om1fb-3),1)
  ls2zge2j=mpyxdw2z.render(self.got7txkd,True,(20,20,20))
  h8s2ftom.blit(ls2zge2j,(wzlm72je-ls2zge2j.get_width()//2,self.npcxa5s0.y-20))
def chx3d43e():
 return[my6wktak('Vera','nf7qne',iq5c34dx['p0s1f5'],120,140),my6wktak('Duncan','fuxk0a',iq5c34dx['kqbsxl'],383,110),my6wktak('Mira','jz6wmd',iq5c34dx['s1whhk'],650,140)]
yex8fsv8={'nf7qne':'Vitality Shop - Vera','fuxk0a':'Combat Shop - Duncan','jz6wmd':'Mobility Shop - Mira'}
def zpfb3hn1(key,y2f7atwy):
 k2ixivzk=jsylztgx[key]
 return int(k2ixivzk['qc6dr0']*k2ixivzk['pcs4ke']**y2f7atwy)
def amcixdu1(iaq7b7v1,izhwy9he,cjn2fomd):
 (mpyxdw2z,hdw6lqwl,z3olfark,i20cv3tl)=cjn2fomd
 mctwjlsh=[k for(k,acxx6mdk)in jsylztgx.items()if acxx6mdk['vcw2lb']==izhwy9he]
 cnqt3wve=110*len(mctwjlsh)+20
 uz6kf162=oohp6vz4(420,cnqt3wve+oohp6vz4.rla5ju9b+60,z0xkxwd8,title=yex8fsv8.get(izhwy9he,'Shop'),title_font=z3olfark)
 do2m71hs=uz6kf162.npcxa5s0.y+uz6kf162.ftrflqbm
 hugysm8t=cnqt3wve//len(mctwjlsh)
 for(nyrid3dn,key)in enumerate(mctwjlsh):
  k2ixivzk=jsylztgx[key]
  tb4ldims=iaq7b7v1['meta_upgrades'].get(key,0)
  r2muljav=tb4ldims>=k2ixivzk['udt8cq']
  if r2muljav:
   title=f"{k2ixivzk['mjz6us']}  MAX LEVEL"
  else:
   elwf90km=zpfb3hn1(key,tb4ldims)
   title=f"{k2ixivzk['mjz6us']}  Lv.{tb4ldims} -> {tb4ldims + 1}   [{elwf90km} res]"
  pvasifpw=hc58drc1(uz6kf162.npcxa5s0.x+12,do2m71hs+nyrid3dn*hugysm8t+6,uz6kf162.npcxa5s0.width-24,hugysm8t-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,i20cv3tl,title,12,subtitle=k2ixivzk['onlt8d'],sub_font=hdw6lqwl,kind='meta',key=key)
  pvasifpw.maxed=r2muljav
  uz6kf162.add(pvasifpw)
 hfb85p86=do2m71hs+len(mctwjlsh)*hugysm8t+12
 l9enulqj=hc58drc1(uz6kf162.npcxa5s0.x+12,hfb85p86,uz6kf162.npcxa5s0.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),i20cv3tl,'Close (ESC)',10,kind='close',key=None)
 uz6kf162.add(l9enulqj)
 return uz6kf162
def gj29yfc2(h8s2ftom,bfoqmf5l,iaq7b7v1,f80ebkjf):
 mpyxdw2z=pygame.font.SysFont('arial',22)
 hdw6lqwl=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 z3olfark=pygame.font.SysFont('arial',22,bold=True)
 i20cv3tl=pygame.font.SysFont('arial',20,bold=True)
 rktlzkj4=pygame.font.SysFont('arial',15)
 cjn2fomd=(mpyxdw2z,hdw6lqwl,z3olfark,i20cv3tl)
 aqclpoxk=zbqe7ckw()
 x6cnoljq=chx3d43e()
 xsspye9r=pygame.Rect(ygspk9p3//2-70,tp0lvsnu-60,140,44)
 ejwtl9tq=None
 mpdzp6lf=None
 while True:
  eatvzkhi=pygame.event.get()
  for xq46nouh in eatvzkhi:
   if xq46nouh.type==pygame.QUIT:
    return'quit'
   if xq46nouh.type==pygame.KEYDOWN and xq46nouh.key==pygame.K_ESCAPE and ejwtl9tq:
    ejwtl9tq=None
    mpdzp6lf=None
  if ejwtl9tq is None:
   aqclpoxk.move()
   hjkuuhcl=None
   for ncyh3fvl in x6cnoljq:
    if aqclpoxk.npcxa5s0.colliderect(ncyh3fvl.npcxa5s0.inflate(24,24)):
     if not ncyh3fvl.ry181acj:
      hjkuuhcl=ncyh3fvl
      ncyh3fvl.ry181acj=True
      break
    else:
     ncyh3fvl.ry181acj=False
   if hjkuuhcl:
    mpdzp6lf=hjkuuhcl.izhwy9he
    ejwtl9tq=amcixdu1(iaq7b7v1,mpdzp6lf,cjn2fomd)
   if aqclpoxk.npcxa5s0.colliderect(xsspye9r):
    return'start_game'
  else:
   for xuu13i59 in ejwtl9tq.ub68rerv:
    xuu13i59.update(eatvzkhi)
   rk8r2ykc=next((g70e3p15 for g70e3p15 in ejwtl9tq.ub68rerv if g70e3p15.rk8r2ykc),None)
   if rk8r2ykc is not None:
    if rk8r2ykc.kind=='close':
     ejwtl9tq=None
     mpdzp6lf=None
    elif rk8r2ykc.kind=='meta'and(not getattr(rk8r2ykc,'maxed',False)):
     key=rk8r2ykc.key
     tb4ldims=iaq7b7v1['meta_upgrades'].get(key,0)
     elwf90km=zpfb3hn1(key,tb4ldims)
     if iaq7b7v1['resources']>=elwf90km:
      iaq7b7v1['resources']-=elwf90km
      iaq7b7v1['meta_upgrades'][key]=tb4ldims+1
      f80ebkjf(iaq7b7v1)
      ejwtl9tq=amcixdu1(iaq7b7v1,mpdzp6lf,cjn2fomd)
  h8s2ftom.fill((190,225,190))
  for jo8e7flq in range(0,ygspk9p3,m7hv3izk):
   pygame.draw.line(h8s2ftom,(160,205,160),(jo8e7flq,0),(jo8e7flq,tp0lvsnu),1)
  for gsmdzqcb in range(0,tp0lvsnu,m7hv3izk):
   pygame.draw.line(h8s2ftom,(160,205,160),(0,gsmdzqcb),(ygspk9p3,gsmdzqcb),1)
  pygame.draw.rect(h8s2ftom,iq5c34dx['yaym0w'],xsspye9r,border_radius=10)
  pygame.draw.rect(h8s2ftom,(150,110,0),xsspye9r,width=3,border_radius=10)
  jenvg3kk=hdw6lqwl.render('ENTER RUN',True,(40,30,0))
  h8s2ftom.blit(jenvg3kk,(xsspye9r.centerx-jenvg3kk.get_width()//2,xsspye9r.centery-jenvg3kk.get_height()//2))
  for ncyh3fvl in x6cnoljq:
   ncyh3fvl.v15cqzcu(h8s2ftom,hdw6lqwl)
  aqclpoxk.v15cqzcu(h8s2ftom)
  bokzixza=pygame.Rect(12,12,220,40)
  pcvsqame=pygame.Surface((bokzixza.width,bokzixza.height),pygame.SRCALPHA)
  pygame.draw.rect(pcvsqame,(255,255,255,160),pcvsqame.get_rect(),border_radius=10)
  h8s2ftom.blit(pcvsqame,bokzixza.topleft)
  uaobt328=mpyxdw2z.render(f"Resources: {iaq7b7v1['resources']}",True,(20,20,20))
  h8s2ftom.blit(uaobt328,(20,22))
  it04chsd=title_font.render('HOMEBASE',True,(20,40,20))
  h8s2ftom.blit(it04chsd,(ygspk9p3//2-it04chsd.get_width()//2,12))
  wvpw232u=rktlzkj4.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  h8s2ftom.blit(wvpw232u,(ygspk9p3//2-wvpw232u.get_width()//2,tp0lvsnu-105))
  if ejwtl9tq:
   ejwtl9tq.v15cqzcu(h8s2ftom)
  pygame.display.flip()
  bfoqmf5l.tick(pi3qk2ia)
