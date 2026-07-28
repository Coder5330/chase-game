import pygame
from r1yohmi9 import*
from entities import rk43safy
from bbnhjw6q import oohp6vz4,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.nxxjve3d=pygame.Rect(ygspk9p3//2-rqf5q14j//2,tp0lvsnu-90,rqf5q14j,rqf5q14j)
  self.jyjhu8my=yswjckjl
  self.wzs13c9x=iq5c34dx['p2xrw6']
  self.avfmh07w={'mmgvu4':0,'hzj7ub':-1}
 def bihsa7he(self):
  f55dmcxx=pygame.key.get_pressed()
  mygfliji=yjluujmi=0
  if f55dmcxx[pygame.K_UP]:
   yjluujmi-=self.jyjhu8my
  if f55dmcxx[pygame.K_DOWN]:
   yjluujmi+=self.jyjhu8my
  if f55dmcxx[pygame.K_LEFT]:
   mygfliji-=self.jyjhu8my
  if f55dmcxx[pygame.K_RIGHT]:
   mygfliji+=self.jyjhu8my
  if mygfliji!=0 and yjluujmi!=0:
   mygfliji*=0.707
   yjluujmi*=0.707
  if mygfliji!=0 or yjluujmi!=0:
   self.avfmh07w['mmgvu4']=mygfliji
   self.avfmh07w['hzj7ub']=yjluujmi
  self.nxxjve3d.un9sz6rv+=mygfliji
  self.nxxjve3d.ehet25lz+=yjluujmi
  self.nxxjve3d.un9sz6rv=max(0,min(self.nxxjve3d.un9sz6rv,ygspk9p3-self.nxxjve3d.width))
  self.nxxjve3d.ehet25lz=max(60,min(self.nxxjve3d.ehet25lz,tp0lvsnu-self.nxxjve3d.height))
 def fo75rh8l(self,vmy9x8sy):
  (un9sz6rv,ehet25lz)=(self.nxxjve3d.un9sz6rv,self.nxxjve3d.ehet25lz)
  (cnqt3wve,do2m71hs)=(self.nxxjve3d.centerx,self.nxxjve3d.centery)
  gj29yfc2=pygame.Surface((self.nxxjve3d.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(gj29yfc2,(0,0,0,80),gj29yfc2.get_rect())
  vmy9x8sy.blit(gj29yfc2,(cnqt3wve-gj29yfc2.get_width()//2,ehet25lz+self.nxxjve3d.height-6))
  f8wquuy5=pygame.Rect(un9sz6rv,ehet25lz,self.nxxjve3d.width,self.nxxjve3d.height)
  pygame.draw.rect(vmy9x8sy,rk43safy(self.wzs13c9x,0.55),f8wquuy5,border_radius=10)
  xk7n8la1=f8wquuy5.inflate(-5,-5)
  pygame.draw.rect(vmy9x8sy,self.wzs13c9x,xk7n8la1,border_radius=8)
  gsmdzqcb=pygame.Rect(xk7n8la1.un9sz6rv+3,xk7n8la1.ehet25lz+3,xk7n8la1.width//2,xk7n8la1.height//3)
  pygame.draw.rect(vmy9x8sy,rk43safy(self.wzs13c9x,2.0),gsmdzqcb,border_radius=4)
  pygame.draw.rect(vmy9x8sy,(15,15,30),f8wquuy5,width=2,border_radius=10)
class my6wktak:
 def __init__(self,jl90pxrl,hugysm8t,color,un9sz6rv,ehet25lz):
  self.jl90pxrl=jl90pxrl
  self.hugysm8t=hugysm8t
  self.wzs13c9x=color
  self.nxxjve3d=pygame.Rect(un9sz6rv,ehet25lz,34,34)
  self.zmybd2qe=False
 def fo75rh8l(self,vmy9x8sy,ao4izasn):
  gj29yfc2=pygame.Surface((self.nxxjve3d.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(gj29yfc2,(0,0,0,70),gj29yfc2.get_rect())
  vmy9x8sy.blit(gj29yfc2,(self.nxxjve3d.centerx-gj29yfc2.get_width()//2,self.nxxjve3d.bottom-4))
  f8wquuy5=pygame.Rect(self.nxxjve3d.un9sz6rv,self.nxxjve3d.ehet25lz,self.nxxjve3d.width,self.nxxjve3d.height)
  pygame.draw.rect(vmy9x8sy,rk43safy(self.wzs13c9x,0.6),f8wquuy5,border_radius=8)
  xk7n8la1=f8wquuy5.inflate(-5,-5)
  pygame.draw.rect(vmy9x8sy,self.wzs13c9x,xk7n8la1,border_radius=6)
  pygame.draw.rect(vmy9x8sy,(15,15,15),f8wquuy5,width=2,border_radius=8)
  (cnqt3wve,do2m71hs)=(self.nxxjve3d.centerx,self.nxxjve3d.centery)
  pygame.draw.circle(vmy9x8sy,iq5c34dx['jyzqii'],(cnqt3wve-6,do2m71hs-3),3)
  pygame.draw.circle(vmy9x8sy,iq5c34dx['jyzqii'],(cnqt3wve+6,do2m71hs-3),3)
  pygame.draw.circle(vmy9x8sy,iq5c34dx['ivwvia'],(cnqt3wve-6,do2m71hs-3),1)
  pygame.draw.circle(vmy9x8sy,iq5c34dx['ivwvia'],(cnqt3wve+6,do2m71hs-3),1)
  je11e9ft=ao4izasn.render(self.jl90pxrl,True,(20,20,20))
  vmy9x8sy.blit(je11e9ft,(cnqt3wve-je11e9ft.get_width()//2,self.nxxjve3d.ehet25lz-20))
def y2f7atwy():
 return[my6wktak('Vera','ua6wix',iq5c34dx['s0w9ry'],120,140),my6wktak('Duncan','kk2y77',iq5c34dx['p35ikg'],383,110),my6wktak('Mira','kj2jvq',iq5c34dx['dawe42'],650,140)]
yex8fsv8={'ua6wix':'Vitality Shop - Vera','kk2y77':'Combat Shop - Duncan','kj2jvq':'Mobility Shop - Mira'}
def huh17j8q(key,b78okz1p):
 swwnc21o=jsylztgx[key]
 return int(swwnc21o['wurvqt']*swwnc21o['w9mda9']**b78okz1p)
def giec4d14(k8qeoz0k,hugysm8t,tw76xato):
 (ao4izasn,yp3cyazb,g5hcbbmh,dzsedfqs)=tw76xato
 f55dmcxx=[k for(k,hjkuuhcl)in jsylztgx.items()if hjkuuhcl['og8cd3']==hugysm8t]
 ep6beffl=110*len(f55dmcxx)+20
 zflse45b=oohp6vz4(420,ep6beffl+oohp6vz4.rla5ju9b+60,z0xkxwd8,title=yex8fsv8.get(hugysm8t,'Shop'),title_font=g5hcbbmh)
 wi8skch8=zflse45b.nxxjve3d.ehet25lz+zflse45b.vmxb9yo1
 u23y30ys=ep6beffl//len(f55dmcxx)
 for(cp91i3vm,key)in enumerate(f55dmcxx):
  swwnc21o=jsylztgx[key]
  nii6l3ue=k8qeoz0k['meta_upgrades'].get(key,0)
  zo3lqi7e=nii6l3ue>=swwnc21o['onlt8d']
  if zo3lqi7e:
   title=f"{swwnc21o['hx0gu4']}  MAX LEVEL"
  else:
   vw6m7b5c=huh17j8q(key,nii6l3ue)
   title=f"{swwnc21o['hx0gu4']}  Lv.{nii6l3ue} -> {nii6l3ue + 1}   [{vw6m7b5c} res]"
  llxxezdu=hc58drc1(zflse45b.nxxjve3d.un9sz6rv+12,wi8skch8+cp91i3vm*u23y30ys+6,zflse45b.nxxjve3d.width-24,u23y30ys-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,dzsedfqs,title,12,subtitle=swwnc21o['t7wqp3'],sub_font=yp3cyazb,kind='meta',key=key)
  llxxezdu.maxed=zo3lqi7e
  zflse45b.add(llxxezdu)
 lztkkfzz=wi8skch8+len(f55dmcxx)*u23y30ys+12
 cq6qdy4l=hc58drc1(zflse45b.nxxjve3d.un9sz6rv+12,lztkkfzz,zflse45b.nxxjve3d.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),dzsedfqs,'Close (ESC)',10,kind='close',key=None)
 zflse45b.add(cq6qdy4l)
 return zflse45b
def wd6r30oj(vmy9x8sy,izhwy9he,k8qeoz0k,t5sn961j):
 ao4izasn=pygame.font.SysFont('arial',22)
 yp3cyazb=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 g5hcbbmh=pygame.font.SysFont('arial',22,bold=True)
 dzsedfqs=pygame.font.SysFont('arial',20,bold=True)
 vpbwhvnz=pygame.font.SysFont('arial',15)
 tw76xato=(ao4izasn,yp3cyazb,g5hcbbmh,dzsedfqs)
 ejwtl9tq=zbqe7ckw()
 wb7f6fdh=y2f7atwy()
 vt26ys44=pygame.Rect(ygspk9p3//2-70,tp0lvsnu-60,140,44)
 x52qc1iy=None
 lt63j3r3=None
 while True:
  aicvqy5i=pygame.event.get()
  for g70e3p15 in aicvqy5i:
   if g70e3p15.type==pygame.QUIT:
    return'quit'
   if g70e3p15.type==pygame.KEYDOWN and g70e3p15.key==pygame.K_ESCAPE and x52qc1iy:
    x52qc1iy=None
    lt63j3r3=None
  if x52qc1iy is None:
   ejwtl9tq.bihsa7he()
   gsrtwlxd=None
   for mfc79m96 in wb7f6fdh:
    if ejwtl9tq.nxxjve3d.colliderect(mfc79m96.nxxjve3d.inflate(24,24)):
     if not mfc79m96.zmybd2qe:
      gsrtwlxd=mfc79m96
      mfc79m96.zmybd2qe=True
      break
    else:
     mfc79m96.zmybd2qe=False
   if gsrtwlxd:
    lt63j3r3=gsrtwlxd.hugysm8t
    x52qc1iy=giec4d14(k8qeoz0k,lt63j3r3,tw76xato)
   if ejwtl9tq.nxxjve3d.colliderect(vt26ys44):
    return'start_game'
  else:
   for v15cqzcu in x52qc1iy.xd8wz42o:
    v15cqzcu.update(aicvqy5i)
   iie0rnuj=next((velos6zl for velos6zl in x52qc1iy.xd8wz42o if velos6zl.iie0rnuj),None)
   if iie0rnuj is not None:
    if iie0rnuj.kind=='close':
     x52qc1iy=None
     lt63j3r3=None
    elif iie0rnuj.kind=='meta'and(not getattr(iie0rnuj,'maxed',False)):
     key=iie0rnuj.key
     nii6l3ue=k8qeoz0k['meta_upgrades'].get(key,0)
     vw6m7b5c=huh17j8q(key,nii6l3ue)
     if k8qeoz0k['resources']>=vw6m7b5c:
      k8qeoz0k['resources']-=vw6m7b5c
      k8qeoz0k['meta_upgrades'][key]=nii6l3ue+1
      t5sn961j(k8qeoz0k)
      x52qc1iy=giec4d14(k8qeoz0k,lt63j3r3,tw76xato)
  vmy9x8sy.fill((190,225,190))
  for fekrcppr in range(0,ygspk9p3,vve92mpn):
   pygame.draw.line(vmy9x8sy,(160,205,160),(fekrcppr,0),(fekrcppr,tp0lvsnu),1)
  for cn7zrwqe in range(0,tp0lvsnu,vve92mpn):
   pygame.draw.line(vmy9x8sy,(160,205,160),(0,cn7zrwqe),(ygspk9p3,cn7zrwqe),1)
  pygame.draw.rect(vmy9x8sy,iq5c34dx['x1qwee'],vt26ys44,border_radius=10)
  pygame.draw.rect(vmy9x8sy,(150,110,0),vt26ys44,width=3,border_radius=10)
  no0u93mz=yp3cyazb.render('ENTER RUN',True,(40,30,0))
  vmy9x8sy.blit(no0u93mz,(vt26ys44.centerx-no0u93mz.get_width()//2,vt26ys44.centery-no0u93mz.get_height()//2))
  for mfc79m96 in wb7f6fdh:
   mfc79m96.fo75rh8l(vmy9x8sy,yp3cyazb)
  ejwtl9tq.fo75rh8l(vmy9x8sy)
  i13n3bzt=pygame.Rect(12,12,220,40)
  nd31k9qm=pygame.Surface((i13n3bzt.width,i13n3bzt.height),pygame.SRCALPHA)
  pygame.draw.rect(nd31k9qm,(255,255,255,160),nd31k9qm.get_rect(),border_radius=10)
  vmy9x8sy.blit(nd31k9qm,i13n3bzt.topleft)
  d46aexl6=ao4izasn.render(f"Resources: {k8qeoz0k['resources']}",True,(20,20,20))
  vmy9x8sy.blit(d46aexl6,(20,22))
  x9h0dxho=title_font.render('HOMEBASE',True,(20,40,20))
  vmy9x8sy.blit(x9h0dxho,(ygspk9p3//2-x9h0dxho.get_width()//2,12))
  ftlpq2wg=vpbwhvnz.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  vmy9x8sy.blit(ftlpq2wg,(ygspk9p3//2-ftlpq2wg.get_width()//2,tp0lvsnu-105))
  if x52qc1iy:
   x52qc1iy.fo75rh8l(vmy9x8sy)
  pygame.display.flip()
  izhwy9he.tick(pi3qk2ia)
