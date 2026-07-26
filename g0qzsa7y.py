import pygame
from rlfzkicw import*
from entities import no0u93mz
from amntfvge import cq5uznof,q7vren93
class zbqe7ckw:
 def __init__(self):
  self.mu4fmpkx=pygame.Rect(azebbk7w//2-n2vlpys2//2,gokc1msy-90,n2vlpys2,n2vlpys2)
  self.fd6rupw2=z0xkxwd8
  self.li9nb74x=bom5igqp['qy1fko']
  self.xqzpky32={'vmwi9s':0,'zcjn99':-1}
 def ub68rerv(self):
  u9el8hl8=pygame.key.get_pressed()
  k7zgf9q5=pa8s8hmb=0
  if u9el8hl8[pygame.K_UP]:
   pa8s8hmb-=self.fd6rupw2
  if u9el8hl8[pygame.K_DOWN]:
   pa8s8hmb+=self.fd6rupw2
  if u9el8hl8[pygame.K_LEFT]:
   k7zgf9q5-=self.fd6rupw2
  if u9el8hl8[pygame.K_RIGHT]:
   k7zgf9q5+=self.fd6rupw2
  if k7zgf9q5!=0 and pa8s8hmb!=0:
   k7zgf9q5*=0.707
   pa8s8hmb*=0.707
  if k7zgf9q5!=0 or pa8s8hmb!=0:
   self.xqzpky32['vmwi9s']=k7zgf9q5
   self.xqzpky32['zcjn99']=pa8s8hmb
  self.mu4fmpkx.kn5gjj8m+=k7zgf9q5
  self.mu4fmpkx.lu7jae58+=pa8s8hmb
  self.mu4fmpkx.kn5gjj8m=max(0,min(self.mu4fmpkx.kn5gjj8m,azebbk7w-self.mu4fmpkx.width))
  self.mu4fmpkx.lu7jae58=max(60,min(self.mu4fmpkx.lu7jae58,gokc1msy-self.mu4fmpkx.height))
 def u1jhuwb6(self,uz6kf162):
  (kn5gjj8m,lu7jae58)=(self.mu4fmpkx.kn5gjj8m,self.mu4fmpkx.lu7jae58)
  (x5m9j98c,uos0fb4y)=(self.mu4fmpkx.centerx,self.mu4fmpkx.centery)
  vt26ys44=pygame.Surface((self.mu4fmpkx.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(vt26ys44,(0,0,0,80),vt26ys44.get_rect())
  uz6kf162.blit(vt26ys44,(x5m9j98c-vt26ys44.get_width()//2,lu7jae58+self.mu4fmpkx.height-6))
  mpdzp6lf=pygame.Rect(kn5gjj8m,lu7jae58,self.mu4fmpkx.width,self.mu4fmpkx.height)
  pygame.draw.rect(uz6kf162,no0u93mz(self.li9nb74x,0.55),mpdzp6lf,border_radius=10)
  damdvlnk=mpdzp6lf.inflate(-5,-5)
  pygame.draw.rect(uz6kf162,self.li9nb74x,damdvlnk,border_radius=8)
  s4rxyj38=pygame.Rect(damdvlnk.kn5gjj8m+3,damdvlnk.lu7jae58+3,damdvlnk.width//2,damdvlnk.height//3)
  pygame.draw.rect(uz6kf162,no0u93mz(self.li9nb74x,2.0),s4rxyj38,border_radius=4)
  pygame.draw.rect(uz6kf162,(15,15,30),mpdzp6lf,width=2,border_radius=10)
class ibps3y70:
 def __init__(self,b78okz1p,uww5wfcp,zfb7r31q,kn5gjj8m,lu7jae58):
  self.b78okz1p=b78okz1p
  self.uww5wfcp=uww5wfcp
  self.li9nb74x=zfb7r31q
  self.mu4fmpkx=pygame.Rect(kn5gjj8m,lu7jae58,34,34)
  self.cn7zrwqe=False
 def u1jhuwb6(self,uz6kf162,sygvwopl):
  vt26ys44=pygame.Surface((self.mu4fmpkx.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(vt26ys44,(0,0,0,70),vt26ys44.get_rect())
  uz6kf162.blit(vt26ys44,(self.mu4fmpkx.centerx-vt26ys44.get_width()//2,self.mu4fmpkx.bottom-4))
  mpdzp6lf=pygame.Rect(self.mu4fmpkx.kn5gjj8m,self.mu4fmpkx.lu7jae58,self.mu4fmpkx.width,self.mu4fmpkx.height)
  pygame.draw.rect(uz6kf162,no0u93mz(self.li9nb74x,0.6),mpdzp6lf,border_radius=8)
  damdvlnk=mpdzp6lf.inflate(-5,-5)
  pygame.draw.rect(uz6kf162,self.li9nb74x,damdvlnk,border_radius=6)
  pygame.draw.rect(uz6kf162,(15,15,15),mpdzp6lf,width=2,border_radius=8)
  (x5m9j98c,uos0fb4y)=(self.mu4fmpkx.centerx,self.mu4fmpkx.centery)
  pygame.draw.circle(uz6kf162,bom5igqp['ym5p7e'],(x5m9j98c-6,uos0fb4y-3),3)
  pygame.draw.circle(uz6kf162,bom5igqp['ym5p7e'],(x5m9j98c+6,uos0fb4y-3),3)
  pygame.draw.circle(uz6kf162,bom5igqp['o270sq'],(x5m9j98c-6,uos0fb4y-3),1)
  pygame.draw.circle(uz6kf162,bom5igqp['o270sq'],(x5m9j98c+6,uos0fb4y-3),1)
  mn7h9g1a=sygvwopl.render(self.b78okz1p,True,(20,20,20))
  uz6kf162.blit(mn7h9g1a,(x5m9j98c-mn7h9g1a.get_width()//2,self.mu4fmpkx.lu7jae58-20))
def rk2u1rsu():
 return[ibps3y70('Vera','m314cq',bom5igqp['cym81c'],120,140),ibps3y70('Duncan','ceb875',bom5igqp['wn0jbz'],383,110),ibps3y70('Mira','o5rlqi',bom5igqp['rkzggm'],650,140)]
hc58drc1={'m314cq':'Vitality Shop - Vera','ceb875':'Combat Shop - Duncan','o5rlqi':'Mobility Shop - Mira'}
def d0qzfhom(key,jo8e7flq):
 jq1ddpus=tp0lvsnu[key]
 return int(jq1ddpus['cjpyue']*jq1ddpus['jayeqa']**jo8e7flq)
def c0hpmnz1(todsx4nx,uww5wfcp,mygfliji):
 (sygvwopl,nxxjve3d,jr5rdnpx,rzs43c5b)=mygfliji
 u9el8hl8=[k for(k,oa47sh2s)in tp0lvsnu.items()if oa47sh2s['npmlva']==uww5wfcp]
 d1ieixwc=110*len(u9el8hl8)+20
 lhgk5bwi=cq5uznof(420,d1ieixwc+cq5uznof.pi3qk2ia+60,jsylztgx,title=hc58drc1.get(uww5wfcp,'Shop'),title_font=jr5rdnpx)
 pvasifpw=lhgk5bwi.mu4fmpkx.lu7jae58+lhgk5bwi.yrivh6t1
 ra73jgzl=d1ieixwc//len(u9el8hl8)
 for(mytn02yc,key)in enumerate(u9el8hl8):
  jq1ddpus=tp0lvsnu[key]
  nvuprt77=todsx4nx['meta_upgrades'].get(key,0)
  rktlzkj4=nvuprt77>=jq1ddpus['xyhhg8']
  if rktlzkj4:
   title=f"{jq1ddpus['amyrsv']}  MAX LEVEL"
  else:
   z9toqw9j=d0qzfhom(key,nvuprt77)
   title=f"{jq1ddpus['amyrsv']}  Lv.{nvuprt77} -> {nvuprt77 + 1}   [{z9toqw9j} res]"
  ykipu1wy=q7vren93(lhgk5bwi.mu4fmpkx.kn5gjj8m+12,pvasifpw+mytn02yc*ra73jgzl+6,lhgk5bwi.mu4fmpkx.width-24,ra73jgzl-10,uqjiujv6,aye511mk,mn9er14f,f2pcn9t8,rzs43c5b,title,12,subtitle=jq1ddpus['h7kr0a'],sub_font=nxxjve3d,kind='meta',key=key)
  ykipu1wy.maxed=rktlzkj4
  lhgk5bwi.add(ykipu1wy)
 f32ejx5t=pvasifpw+len(u9el8hl8)*ra73jgzl+12
 gn89qkns=q7vren93(lhgk5bwi.mu4fmpkx.kn5gjj8m+12,f32ejx5t,lhgk5bwi.mu4fmpkx.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),rzs43c5b,'Close (ESC)',10,kind='close',key=None)
 lhgk5bwi.add(gn89qkns)
 return lhgk5bwi
def l3swebnv(uz6kf162,tk0qtl3q,todsx4nx,uj64qhks):
 sygvwopl=pygame.font.SysFont('arial',22)
 nxxjve3d=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 jr5rdnpx=pygame.font.SysFont('arial',22,bold=True)
 rzs43c5b=pygame.font.SysFont('arial',20,bold=True)
 ao4izasn=pygame.font.SysFont('arial',15)
 mygfliji=(sygvwopl,nxxjve3d,jr5rdnpx,rzs43c5b)
 diuu9k9x=zbqe7ckw()
 lnf74t60=rk2u1rsu()
 bihsa7he=pygame.Rect(azebbk7w//2-70,gokc1msy-60,140,44)
 nd96qe3r=None
 wrbw2zla=None
 while True:
  wehlxslg=pygame.event.get()
  for eohswq40 in wehlxslg:
   if eohswq40.type==pygame.QUIT:
    return'quit'
   if eohswq40.type==pygame.KEYDOWN and eohswq40.key==pygame.K_ESCAPE and nd96qe3r:
    nd96qe3r=None
    wrbw2zla=None
  if nd96qe3r is None:
   diuu9k9x.ub68rerv()
   yypp5zp7=None
   for sye0a4ab in lnf74t60:
    if diuu9k9x.mu4fmpkx.colliderect(sye0a4ab.mu4fmpkx.inflate(24,24)):
     if not sye0a4ab.cn7zrwqe:
      yypp5zp7=sye0a4ab
      sye0a4ab.cn7zrwqe=True
      break
    else:
     sye0a4ab.cn7zrwqe=False
   if yypp5zp7:
    wrbw2zla=yypp5zp7.uww5wfcp
    nd96qe3r=c0hpmnz1(todsx4nx,wrbw2zla,mygfliji)
   if diuu9k9x.mu4fmpkx.colliderect(bihsa7he):
    return'start_game'
  else:
   for cnqt3wve in nd96qe3r.m20u9isy:
    cnqt3wve.update(wehlxslg)
   yw6zbnz8=next((pv4ykade for pv4ykade in nd96qe3r.m20u9isy if pv4ykade.yw6zbnz8),None)
   if yw6zbnz8 is not None:
    if yw6zbnz8.kind=='close':
     nd96qe3r=None
     wrbw2zla=None
    elif yw6zbnz8.kind=='meta'and(not getattr(yw6zbnz8,'maxed',False)):
     key=yw6zbnz8.key
     nvuprt77=todsx4nx['meta_upgrades'].get(key,0)
     z9toqw9j=d0qzfhom(key,nvuprt77)
     if todsx4nx['resources']>=z9toqw9j:
      todsx4nx['resources']-=z9toqw9j
      todsx4nx['meta_upgrades'][key]=nvuprt77+1
      uj64qhks(todsx4nx)
      nd96qe3r=c0hpmnz1(todsx4nx,wrbw2zla,mygfliji)
  uz6kf162.fill((190,225,190))
  for boih5csk in range(0,azebbk7w,r0tvhhpb):
   pygame.draw.line(uz6kf162,(160,205,160),(boih5csk,0),(boih5csk,gokc1msy),1)
  for xuu13i59 in range(0,gokc1msy,r0tvhhpb):
   pygame.draw.line(uz6kf162,(160,205,160),(0,xuu13i59),(azebbk7w,xuu13i59),1)
  pygame.draw.rect(uz6kf162,bom5igqp['wpadah'],bihsa7he,border_radius=10)
  pygame.draw.rect(uz6kf162,(150,110,0),bihsa7he,width=3,border_radius=10)
  s8438tgb=nxxjve3d.render('ENTER RUN',True,(40,30,0))
  uz6kf162.blit(s8438tgb,(bihsa7he.centerx-s8438tgb.get_width()//2,bihsa7he.centery-s8438tgb.get_height()//2))
  for sye0a4ab in lnf74t60:
   sye0a4ab.u1jhuwb6(uz6kf162,nxxjve3d)
  diuu9k9x.u1jhuwb6(uz6kf162)
  v76ub7l8=pygame.Rect(12,12,220,40)
  sf337kuu=pygame.Surface((v76ub7l8.width,v76ub7l8.height),pygame.SRCALPHA)
  pygame.draw.rect(sf337kuu,(255,255,255,160),sf337kuu.get_rect(),border_radius=10)
  uz6kf162.blit(sf337kuu,v76ub7l8.topleft)
  co4busu9=sygvwopl.render(f"Resources: {todsx4nx['resources']}",True,(20,20,20))
  uz6kf162.blit(co4busu9,(20,22))
  bf7so8w5=title_font.render('HOMEBASE',True,(20,40,20))
  uz6kf162.blit(bf7so8w5,(azebbk7w//2-bf7so8w5.get_width()//2,12))
  r98s4c3b=ao4izasn.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  uz6kf162.blit(r98s4c3b,(azebbk7w//2-r98s4c3b.get_width()//2,gokc1msy-105))
  if nd96qe3r:
   nd96qe3r.u1jhuwb6(uz6kf162)
  pygame.display.flip()
  tk0qtl3q.tick(zy0ifznb)
