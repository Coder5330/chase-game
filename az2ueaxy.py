import pygame
from d0qzfhom import*
from entities import avfmh07w
from rserev36 import hyihair4,q7vren93
class zbqe7ckw:
 def __init__(self):
  self.semqgy27=pygame.Rect(khl1n13j//2-my6wktak//2,pi3qk2ia-90,my6wktak,my6wktak)
  self.j1ldqnk2=n2vlpys2
  self.tp2ex5t5=bom5igqp['zp5ge0']
  self.uidlrye8={'qhgcso':0,'rom5xl':-1}
 def s4rxyj38(self):
  wc7x0h3j=pygame.key.get_pressed()
  qbm1enf3=yw6zbnz8=0
  if wc7x0h3j[pygame.K_UP]:
   yw6zbnz8-=self.j1ldqnk2
  if wc7x0h3j[pygame.K_DOWN]:
   yw6zbnz8+=self.j1ldqnk2
  if wc7x0h3j[pygame.K_LEFT]:
   qbm1enf3-=self.j1ldqnk2
  if wc7x0h3j[pygame.K_RIGHT]:
   qbm1enf3+=self.j1ldqnk2
  if qbm1enf3!=0 and yw6zbnz8!=0:
   qbm1enf3*=0.707
   yw6zbnz8*=0.707
  if qbm1enf3!=0 or yw6zbnz8!=0:
   self.uidlrye8['qhgcso']=qbm1enf3
   self.uidlrye8['rom5xl']=yw6zbnz8
  self.semqgy27.gp6orsnc+=qbm1enf3
  self.semqgy27.cknfu84x+=yw6zbnz8
  self.semqgy27.gp6orsnc=max(0,min(self.semqgy27.gp6orsnc,khl1n13j-self.semqgy27.width))
  self.semqgy27.cknfu84x=max(60,min(self.semqgy27.cknfu84x,pi3qk2ia-self.semqgy27.height))
 def llxxezdu(self,je11e9ft):
  (gp6orsnc,cknfu84x)=(self.semqgy27.gp6orsnc,self.semqgy27.cknfu84x)
  (g11kerpe,rzs43c5b)=(self.semqgy27.centerx,self.semqgy27.centery)
  o4dd1vn8=pygame.Surface((self.semqgy27.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(o4dd1vn8,(0,0,0,80),o4dd1vn8.get_rect())
  je11e9ft.blit(o4dd1vn8,(g11kerpe-o4dd1vn8.get_width()//2,cknfu84x+self.semqgy27.height-6))
  bwiykid9=pygame.Rect(gp6orsnc,cknfu84x,self.semqgy27.width,self.semqgy27.height)
  pygame.draw.rect(je11e9ft,avfmh07w(self.tp2ex5t5,0.55),bwiykid9,border_radius=10)
  eohswq40=bwiykid9.inflate(-5,-5)
  pygame.draw.rect(je11e9ft,self.tp2ex5t5,eohswq40,border_radius=8)
  bfoqmf5l=pygame.Rect(eohswq40.gp6orsnc+3,eohswq40.cknfu84x+3,eohswq40.width//2,eohswq40.height//3)
  pygame.draw.rect(je11e9ft,avfmh07w(self.tp2ex5t5,2.0),bfoqmf5l,border_radius=4)
  pygame.draw.rect(je11e9ft,(15,15,30),bwiykid9,width=2,border_radius=10)
class tp0lvsnu:
 def __init__(self,u0q0mftg,pa5u6hc3,nqimqodp,gp6orsnc,cknfu84x):
  self.u0q0mftg=u0q0mftg
  self.pa5u6hc3=pa5u6hc3
  self.tp2ex5t5=nqimqodp
  self.semqgy27=pygame.Rect(gp6orsnc,cknfu84x,34,34)
  self.g8kk791z=False
 def llxxezdu(self,je11e9ft,uos0fb4y):
  o4dd1vn8=pygame.Surface((self.semqgy27.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(o4dd1vn8,(0,0,0,70),o4dd1vn8.get_rect())
  je11e9ft.blit(o4dd1vn8,(self.semqgy27.centerx-o4dd1vn8.get_width()//2,self.semqgy27.bottom-4))
  bwiykid9=pygame.Rect(self.semqgy27.gp6orsnc,self.semqgy27.cknfu84x,self.semqgy27.width,self.semqgy27.height)
  pygame.draw.rect(je11e9ft,avfmh07w(self.tp2ex5t5,0.6),bwiykid9,border_radius=8)
  eohswq40=bwiykid9.inflate(-5,-5)
  pygame.draw.rect(je11e9ft,self.tp2ex5t5,eohswq40,border_radius=6)
  pygame.draw.rect(je11e9ft,(15,15,15),bwiykid9,width=2,border_radius=8)
  (g11kerpe,rzs43c5b)=(self.semqgy27.centerx,self.semqgy27.centery)
  pygame.draw.circle(je11e9ft,bom5igqp['srs7gu'],(g11kerpe-6,rzs43c5b-3),3)
  pygame.draw.circle(je11e9ft,bom5igqp['srs7gu'],(g11kerpe+6,rzs43c5b-3),3)
  pygame.draw.circle(je11e9ft,bom5igqp['luvkyr'],(g11kerpe-6,rzs43c5b-3),1)
  pygame.draw.circle(je11e9ft,bom5igqp['luvkyr'],(g11kerpe+6,rzs43c5b-3),1)
  rzewviyt=uos0fb4y.render(self.u0q0mftg,True,(20,20,20))
  je11e9ft.blit(rzewviyt,(g11kerpe-rzewviyt.get_width()//2,self.semqgy27.cknfu84x-20))
def b36htf4p():
 return[tp0lvsnu('Vera','bbxd8w',bom5igqp['yjshzk'],120,140),tp0lvsnu('Duncan','dwyuix',bom5igqp['c2c06x'],383,110),tp0lvsnu('Mira','rh024k',bom5igqp['o9kqdg'],650,140)]
hc58drc1={'bbxd8w':'Vitality Shop - Vera','dwyuix':'Combat Shop - Duncan','rh024k':'Mobility Shop - Mira'}
def mfc79m96(key,jqxs6esj):
 mfyb8dal=rla5ju9b[key]
 return int(mfyb8dal['vzy6t5']*mfyb8dal['mi22kx']**jqxs6esj)
def diuu9k9x(pcvsqame,pa5u6hc3,obc2nnuv):
 (uos0fb4y,d1b3jczu,kkzruin3,sne6loh2)=obc2nnuv
 wc7x0h3j=[vt6om1fb for(vt6om1fb,trdhw9re)in rla5ju9b.items()if trdhw9re['n3safy']==pa5u6hc3]
 x03uvule=110*len(wc7x0h3j)+20
 u9el8hl8=hyihair4(420,x03uvule+hyihair4.zy0ifznb+60,gncxll4z,title=hc58drc1.get(pa5u6hc3,'Shop'),title_font=kkzruin3)
 l57p6bkl=u9el8hl8.semqgy27.cknfu84x+u9el8hl8.iektsg7f
 iy6qktc8=x03uvule//len(wc7x0h3j)
 for(elwf90km,key)in enumerate(wc7x0h3j):
  mfyb8dal=rla5ju9b[key]
  velos6zl=pcvsqame['meta_upgrades'].get(key,0)
  mq7nc85e=velos6zl>=mfyb8dal['j1poxr']
  if mq7nc85e:
   title=f"{mfyb8dal['nnwpay']}  MAX LEVEL"
  else:
   ykipu1wy=mfc79m96(key,velos6zl)
   title=f"{mfyb8dal['nnwpay']}  Lv.{velos6zl} -> {velos6zl + 1}   [{ykipu1wy} res]"
  t5wi6fqj=q7vren93(u9el8hl8.semqgy27.gp6orsnc+12,l57p6bkl+elwf90km*iy6qktc8+6,u9el8hl8.semqgy27.width-24,iy6qktc8-10,uqjiujv6,aye511mk,mn9er14f,f2pcn9t8,sne6loh2,title,12,subtitle=mfyb8dal['vk2tcz'],sub_font=d1b3jczu,kind='meta',key=key)
  t5wi6fqj.maxed=mq7nc85e
  u9el8hl8.add(t5wi6fqj)
 b06xkxb9=l57p6bkl+len(wc7x0h3j)*iy6qktc8+12
 d0r2sds8=q7vren93(u9el8hl8.semqgy27.gp6orsnc+12,b06xkxb9,u9el8hl8.semqgy27.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),sne6loh2,'Close (ESC)',10,kind='close',key=None)
 u9el8hl8.add(d0r2sds8)
 return u9el8hl8
def n3rlkte4(je11e9ft,am2vajep,pcvsqame,bokzixza):
 uos0fb4y=pygame.font.SysFont('arial',22)
 d1b3jczu=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 kkzruin3=pygame.font.SysFont('arial',22,bold=True)
 sne6loh2=pygame.font.SysFont('arial',20,bold=True)
 k7zgf9q5=pygame.font.SysFont('arial',15)
 obc2nnuv=(uos0fb4y,d1b3jczu,kkzruin3,sne6loh2)
 ygspk9p3=zbqe7ckw()
 mc8qizk3=b36htf4p()
 z8z3v6di=pygame.Rect(khl1n13j//2-70,pi3qk2ia-60,140,44)
 s9skdgig=None
 gl08yg0j=None
 while True:
  hugysm8t=pygame.event.get()
  for pvasifpw in hugysm8t:
   if pvasifpw.type==pygame.QUIT:
    return'quit'
   if pvasifpw.type==pygame.KEYDOWN and pvasifpw.key==pygame.K_ESCAPE and s9skdgig:
    s9skdgig=None
    gl08yg0j=None
  if s9skdgig is None:
   ygspk9p3.s4rxyj38()
   j0kgazu4=None
   for fddfgs3j in mc8qizk3:
    if ygspk9p3.semqgy27.colliderect(fddfgs3j.semqgy27.inflate(24,24)):
     if not fddfgs3j.g8kk791z:
      j0kgazu4=fddfgs3j
      fddfgs3j.g8kk791z=True
      break
    else:
     fddfgs3j.g8kk791z=False
   if j0kgazu4:
    gl08yg0j=j0kgazu4.pa5u6hc3
    s9skdgig=diuu9k9x(pcvsqame,gl08yg0j,obc2nnuv)
   if ygspk9p3.semqgy27.colliderect(z8z3v6di):
    return'start_game'
  else:
   for f32ejx5t in s9skdgig.wehlxslg:
    f32ejx5t.update(hugysm8t)
   i4fejgxa=next((tk0qtl3q for tk0qtl3q in s9skdgig.wehlxslg if tk0qtl3q.i4fejgxa),None)
   if i4fejgxa is not None:
    if i4fejgxa.kind=='close':
     s9skdgig=None
     gl08yg0j=None
    elif i4fejgxa.kind=='meta'and(not getattr(i4fejgxa,'maxed',False)):
     key=i4fejgxa.key
     velos6zl=pcvsqame['meta_upgrades'].get(key,0)
     ykipu1wy=mfc79m96(key,velos6zl)
     if pcvsqame['resources']>=ykipu1wy:
      pcvsqame['resources']-=ykipu1wy
      pcvsqame['meta_upgrades'][key]=velos6zl+1
      bokzixza(pcvsqame)
      s9skdgig=diuu9k9x(pcvsqame,gl08yg0j,obc2nnuv)
  je11e9ft.fill((190,225,190))
  for lztkkfzz in range(0,khl1n13j,rcfnfhol):
   pygame.draw.line(je11e9ft,(160,205,160),(lztkkfzz,0),(lztkkfzz,pi3qk2ia),1)
  for f2sehe2a in range(0,pi3qk2ia,rcfnfhol):
   pygame.draw.line(je11e9ft,(160,205,160),(0,f2sehe2a),(khl1n13j,f2sehe2a),1)
  pygame.draw.rect(je11e9ft,bom5igqp['xiymen'],z8z3v6di,border_radius=10)
  pygame.draw.rect(je11e9ft,(150,110,0),z8z3v6di,width=3,border_radius=10)
  o9ros7yt=d1b3jczu.render('ENTER RUN',True,(40,30,0))
  je11e9ft.blit(o9ros7yt,(z8z3v6di.centerx-o9ros7yt.get_width()//2,z8z3v6di.centery-o9ros7yt.get_height()//2))
  for fddfgs3j in mc8qizk3:
   fddfgs3j.llxxezdu(je11e9ft,d1b3jczu)
  ygspk9p3.llxxezdu(je11e9ft)
  do2m71hs=pygame.Rect(12,12,220,40)
  qbbz2sf6=pygame.Surface((do2m71hs.width,do2m71hs.height),pygame.SRCALPHA)
  pygame.draw.rect(qbbz2sf6,(255,255,255,160),qbbz2sf6.get_rect(),border_radius=10)
  je11e9ft.blit(qbbz2sf6,do2m71hs.topleft)
  rk2u1rsu=uos0fb4y.render(f"Resources: {pcvsqame['resources']}",True,(20,20,20))
  je11e9ft.blit(rk2u1rsu,(20,22))
  wg25cfzf=title_font.render('HOMEBASE',True,(20,40,20))
  je11e9ft.blit(wg25cfzf,(khl1n13j//2-wg25cfzf.get_width()//2,12))
  hfb85p86=k7zgf9q5.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  je11e9ft.blit(hfb85p86,(khl1n13j//2-hfb85p86.get_width()//2,pi3qk2ia-105))
  if s9skdgig:
   s9skdgig.llxxezdu(je11e9ft)
  pygame.display.flip()
  am2vajep.tick(f935a0l7)
