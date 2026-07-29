import pygame
from jggz62fe import*
from entities import byl68ntk
from bdnwnguc import yur7ko64,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.xu9ymszd=pygame.Rect(cqoldfor//2-yswjckjl//2,tp0lvsnu-90,yswjckjl,yswjckjl)
  self.q6nqqb9l=rcfnfhol
  self.i01nouht=iq5c34dx['gzyt91']
  self.crsb4gf1={'kj2jvq':0,'v00vhm':-1}
 def move(self):
  zflv1xxl=pygame.key.get_pressed()
  jqzpniqf=g70e3p15=0
  if zflv1xxl[pygame.K_UP]:
   g70e3p15-=self.q6nqqb9l
  if zflv1xxl[pygame.K_DOWN]:
   g70e3p15+=self.q6nqqb9l
  if zflv1xxl[pygame.K_LEFT]:
   jqzpniqf-=self.q6nqqb9l
  if zflv1xxl[pygame.K_RIGHT]:
   jqzpniqf+=self.q6nqqb9l
  if jqzpniqf!=0 and g70e3p15!=0:
   jqzpniqf*=0.707
   g70e3p15*=0.707
  if jqzpniqf!=0 or g70e3p15!=0:
   self.crsb4gf1['kj2jvq']=jqzpniqf
   self.crsb4gf1['v00vhm']=g70e3p15
  self.xu9ymszd.x+=jqzpniqf
  self.xu9ymszd.y+=g70e3p15
  self.xu9ymszd.x=max(0,min(self.xu9ymszd.x,cqoldfor-self.xu9ymszd.width))
  self.xu9ymszd.y=max(60,min(self.xu9ymszd.y,tp0lvsnu-self.xu9ymszd.height))
 def b36htf4p(self,gxlk8wru):
  (x,y)=(self.xu9ymszd.x,self.xu9ymszd.y)
  (vt6om1fb,wc7x0h3j)=(self.xu9ymszd.centerx,self.xu9ymszd.centery)
  q3n2qb6g=pygame.Surface((self.xu9ymszd.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(q3n2qb6g,(0,0,0,80),q3n2qb6g.get_rect())
  gxlk8wru.blit(q3n2qb6g,(vt6om1fb-q3n2qb6g.get_width()//2,y+self.xu9ymszd.height-6))
  gn89qkns=pygame.Rect(x,y,self.xu9ymszd.width,self.xu9ymszd.height)
  pygame.draw.rect(gxlk8wru,byl68ntk(self.i01nouht,0.55),gn89qkns,border_radius=10)
  ub68rerv=gn89qkns.inflate(-5,-5)
  pygame.draw.rect(gxlk8wru,self.i01nouht,ub68rerv,border_radius=8)
  cp91i3vm=pygame.Rect(ub68rerv.x+3,ub68rerv.y+3,ub68rerv.width//2,ub68rerv.height//3)
  pygame.draw.rect(gxlk8wru,byl68ntk(self.i01nouht,2.0),cp91i3vm,border_radius=4)
  pygame.draw.rect(gxlk8wru,(15,15,30),gn89qkns,width=2,border_radius=10)
class n2vlpys2:
 def __init__(self,mu4fmpkx,cq6qdy4l,color,x,y):
  self.mu4fmpkx=mu4fmpkx
  self.cq6qdy4l=cq6qdy4l
  self.i01nouht=color
  self.xu9ymszd=pygame.Rect(x,y,34,34)
  self.b78okz1p=False
 def b36htf4p(self,gxlk8wru,cjn2fomd):
  q3n2qb6g=pygame.Surface((self.xu9ymszd.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(q3n2qb6g,(0,0,0,70),q3n2qb6g.get_rect())
  gxlk8wru.blit(q3n2qb6g,(self.xu9ymszd.centerx-q3n2qb6g.get_width()//2,self.xu9ymszd.bottom-4))
  gn89qkns=pygame.Rect(self.xu9ymszd.x,self.xu9ymszd.y,self.xu9ymszd.width,self.xu9ymszd.height)
  pygame.draw.rect(gxlk8wru,byl68ntk(self.i01nouht,0.6),gn89qkns,border_radius=8)
  ub68rerv=gn89qkns.inflate(-5,-5)
  pygame.draw.rect(gxlk8wru,self.i01nouht,ub68rerv,border_radius=6)
  pygame.draw.rect(gxlk8wru,(15,15,15),gn89qkns,width=2,border_radius=8)
  (vt6om1fb,wc7x0h3j)=(self.xu9ymszd.centerx,self.xu9ymszd.centery)
  pygame.draw.circle(gxlk8wru,iq5c34dx['cxf5x9'],(vt6om1fb-6,wc7x0h3j-3),3)
  pygame.draw.circle(gxlk8wru,iq5c34dx['cxf5x9'],(vt6om1fb+6,wc7x0h3j-3),3)
  pygame.draw.circle(gxlk8wru,iq5c34dx['okg68a'],(vt6om1fb-6,wc7x0h3j-3),1)
  pygame.draw.circle(gxlk8wru,iq5c34dx['okg68a'],(vt6om1fb+6,wc7x0h3j-3),1)
  d1b3jczu=cjn2fomd.render(self.mu4fmpkx,True,(20,20,20))
  gxlk8wru.blit(d1b3jczu,(vt6om1fb-d1b3jczu.get_width()//2,self.xu9ymszd.y-20))
def ob7p0rnp():
 return[n2vlpys2('Vera','xgmjmb',iq5c34dx['qye0qz'],120,140),n2vlpys2('Duncan','pcs4ke',iq5c34dx['s1whhk'],383,110),n2vlpys2('Mira','upgba9',iq5c34dx['rlpefj'],650,140)]
yex8fsv8={'xgmjmb':'Vitality Shop - Vera','pcs4ke':'Combat Shop - Duncan','upgba9':'Mobility Shop - Mira'}
def ceb8753a(key,a8ax40dt):
 wa45hvgo=my6wktak[key]
 return int(wa45hvgo['vcw2lb']*wa45hvgo['ijj0v6']**a8ax40dt)
def ebt3g2qz(uwxrum2l,cq6qdy4l,jq1ddpus):
 (cjn2fomd,sfu38gl2,no0u93mz,clkqzfpq)=jq1ddpus
 zflv1xxl=[k for(k,un9sz6rv)in my6wktak.items()if un9sz6rv['ktaq6u']==cq6qdy4l]
 do2m71hs=110*len(zflv1xxl)+20
 z3olfark=yur7ko64(420,do2m71hs+yur7ko64.rla5ju9b+60,hyihair4,title=yex8fsv8.get(cq6qdy4l,'Shop'),title_font=no0u93mz)
 qbbz2sf6=z3olfark.xu9ymszd.y+z3olfark.arhnuxor
 z9toqw9j=do2m71hs//len(zflv1xxl)
 for(je11e9ft,key)in enumerate(zflv1xxl):
  wa45hvgo=my6wktak[key]
  vk3g84ut=uwxrum2l['meta_upgrades'].get(key,0)
  a62c9t19=vk3g84ut>=wa45hvgo['ykht8x']
  if a62c9t19:
   title=f"{wa45hvgo['yrp422']}  MAX LEVEL"
  else:
   qtzk3ny9=ceb8753a(key,vk3g84ut)
   title=f"{wa45hvgo['yrp422']}  Lv.{vk3g84ut} -> {vk3g84ut + 1}   [{qtzk3ny9} res]"
  hugysm8t=hc58drc1(z3olfark.xu9ymszd.x+12,qbbz2sf6+je11e9ft*z9toqw9j+6,z3olfark.xu9ymszd.width-24,z9toqw9j-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,clkqzfpq,title,12,subtitle=wa45hvgo['rw8p74'],sub_font=sfu38gl2,kind='meta',key=key)
  hugysm8t.maxed=a62c9t19
  z3olfark.add(hugysm8t)
 k7zgf9q5=qbbz2sf6+len(zflv1xxl)*z9toqw9j+12
 hfb85p86=hc58drc1(z3olfark.xu9ymszd.x+12,k7zgf9q5,z3olfark.xu9ymszd.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),clkqzfpq,'Close (ESC)',10,kind='close',key=None)
 z3olfark.add(hfb85p86)
 return z3olfark
def g1b3d505(gxlk8wru,l9enulqj,uwxrum2l,iaq7b7v1):
 cjn2fomd=pygame.font.SysFont('arial',22)
 sfu38gl2=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 no0u93mz=pygame.font.SysFont('arial',22,bold=True)
 clkqzfpq=pygame.font.SysFont('arial',20,bold=True)
 v3e1ocjx=pygame.font.SysFont('arial',15)
 jq1ddpus=(cjn2fomd,sfu38gl2,no0u93mz,clkqzfpq)
 mal2w37d=zbqe7ckw()
 a2wspofv=ob7p0rnp()
 yg87oi0e=pygame.Rect(cqoldfor//2-70,tp0lvsnu-60,140,44)
 tp2ex5t5=None
 ejwtl9tq=None
 while True:
  s4rxyj38=pygame.event.get()
  for eatvzkhi in s4rxyj38:
   if eatvzkhi.type==pygame.QUIT:
    return'quit'
   if eatvzkhi.type==pygame.KEYDOWN and eatvzkhi.key==pygame.K_ESCAPE and tp2ex5t5:
    tp2ex5t5=None
    ejwtl9tq=None
  if tp2ex5t5 is None:
   mal2w37d.move()
   pg3yu6vk=None
   for x6cnoljq in a2wspofv:
    if mal2w37d.xu9ymszd.colliderect(x6cnoljq.xu9ymszd.inflate(24,24)):
     if not x6cnoljq.b78okz1p:
      pg3yu6vk=x6cnoljq
      x6cnoljq.b78okz1p=True
      break
    else:
     x6cnoljq.b78okz1p=False
   if pg3yu6vk:
    ejwtl9tq=pg3yu6vk.cq6qdy4l
    tp2ex5t5=ebt3g2qz(uwxrum2l,ejwtl9tq,jq1ddpus)
   if mal2w37d.xu9ymszd.colliderect(yg87oi0e):
    return'start_game'
  else:
   for qhkc856w in tp2ex5t5.q5amln4p:
    qhkc856w.update(s4rxyj38)
   bfoqmf5l=next((aicvqy5i for aicvqy5i in tp2ex5t5.q5amln4p if aicvqy5i.bfoqmf5l),None)
   if bfoqmf5l is not None:
    if bfoqmf5l.kind=='close':
     tp2ex5t5=None
     ejwtl9tq=None
    elif bfoqmf5l.kind=='meta'and(not getattr(bfoqmf5l,'maxed',False)):
     key=bfoqmf5l.key
     vk3g84ut=uwxrum2l['meta_upgrades'].get(key,0)
     qtzk3ny9=ceb8753a(key,vk3g84ut)
     if uwxrum2l['resources']>=qtzk3ny9:
      uwxrum2l['resources']-=qtzk3ny9
      uwxrum2l['meta_upgrades'][key]=vk3g84ut+1
      iaq7b7v1(uwxrum2l)
      tp2ex5t5=ebt3g2qz(uwxrum2l,ejwtl9tq,jq1ddpus)
  gxlk8wru.fill((190,225,190))
  for gsmdzqcb in range(0,cqoldfor,vve92mpn):
   pygame.draw.line(gxlk8wru,(160,205,160),(gsmdzqcb,0),(gsmdzqcb,tp0lvsnu),1)
  for we4xyf9i in range(0,tp0lvsnu,vve92mpn):
   pygame.draw.line(gxlk8wru,(160,205,160),(0,we4xyf9i),(cqoldfor,we4xyf9i),1)
  pygame.draw.rect(gxlk8wru,iq5c34dx['glmy62'],yg87oi0e,border_radius=10)
  pygame.draw.rect(gxlk8wru,(150,110,0),yg87oi0e,width=3,border_radius=10)
  xsspye9r=sfu38gl2.render('ENTER RUN',True,(40,30,0))
  gxlk8wru.blit(xsspye9r,(yg87oi0e.centerx-xsspye9r.get_width()//2,yg87oi0e.centery-xsspye9r.get_height()//2))
  for x6cnoljq in a2wspofv:
   x6cnoljq.b36htf4p(gxlk8wru,sfu38gl2)
  mal2w37d.b36htf4p(gxlk8wru)
  pcvsqame=pygame.Rect(12,12,220,40)
  nyrid3dn=pygame.Surface((pcvsqame.width,pcvsqame.height),pygame.SRCALPHA)
  pygame.draw.rect(nyrid3dn,(255,255,255,160),nyrid3dn.get_rect(),border_radius=10)
  gxlk8wru.blit(nyrid3dn,pcvsqame.topleft)
  ukshy8nb=cjn2fomd.render(f"Resources: {uwxrum2l['resources']}",True,(20,20,20))
  gxlk8wru.blit(ukshy8nb,(20,22))
  htgsiwg0=title_font.render('HOMEBASE',True,(20,40,20))
  gxlk8wru.blit(htgsiwg0,(cqoldfor//2-htgsiwg0.get_width()//2,12))
  rktlzkj4=v3e1ocjx.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  gxlk8wru.blit(rktlzkj4,(cqoldfor//2-rktlzkj4.get_width()//2,tp0lvsnu-105))
  if tp2ex5t5:
   tp2ex5t5.b36htf4p(gxlk8wru)
  pygame.display.flip()
  l9enulqj.tick(pi3qk2ia)
