import pygame
import math
from vnbnqbnx import*
from.qbtr23qi import mn89ltaj,velos6zl
pygame.init()
rv86wzs3=pygame.Surface((rqf5q14j+16,14),pygame.SRCALPHA)
pygame.draw.ellipse(rv86wzs3,(0,0,0,90),rv86wzs3.get_rect())
def dw7nh8rq(g1b3d505,bdgbk2l0,i4fejgxa=120,xwk2rv23=10):
 p2nv01zd=pygame.Surface((bdgbk2l0.width,bdgbk2l0.height),pygame.SRCALPHA)
 pygame.draw.rect(p2nv01zd,(255,255,255,i4fejgxa),p2nv01zd.get_rect(),border_radius=xwk2rv23)
 g1b3d505.blit(p2nv01zd,bdgbk2l0.topleft)
class r0tvhhpb:
 def __init__(self,meta_upgrades=None):
  meta_upgrades=meta_upgrades or{}
  a62c9t19=meta_upgrades.get('START_HEALTH',0)
  s8438tgb=meta_upgrades.get('START_SPEED',0)
  zsw2292m=meta_upgrades.get('START_DAMAGE',0)
  lhgk5bwi=meta_upgrades.get('START_COOLDOWN',0)
  ob7p0rnp=meta_upgrades.get('START_ARMOR',0)
  k3z6bz8u=meta_upgrades.get('START_REGEN',0)
  self.z0b6ugvs=yswjckjl*bihsa7he(s8438tgb)
  self.w0p4e05q=self.z0b6ugvs
  self.bdgbk2l0=pygame.Rect((v83tqll8-rqf5q14j)//2,(cqoldfor-rqf5q14j)//2,rqf5q14j,rqf5q14j)
  self.rk8r2ykc=iq5c34dx['yl4zjd']
  self.uww5wfcp=int(1000*fdxj37c9(a62c9t19))
  self.mnwxuj3a=self.uww5wfcp
  self.gkz2u2tn=self.uww5wfcp
  self.uypuplvq=0
  self.crsb4gf1=1
  self.hhl1737s=False
  self.ry181acj={'ktaq6u':0,'kp82kb':self.w0p4e05q}
  self.acxx6mdk={}
  self.hjkuuhcl={key:0 for key in rcfnfhol}
  self.fcwtg1m8=r2muljav(zsw2292m)
  self.divsolml=jr5rdnpx(lhgk5bwi)
  self.aqclpoxk=chx3d43e(ob7p0rnp)
  self.jc54wsqt=hu9n79gi(k3z6bz8u)
  self.wehlxslg=self.fcwtg1m8
  self.k7zgf9q5=self.divsolml
  self.q6p61xuf=1.0
  self.tp2ex5t5=self.aqclpoxk
  self.d46aexl6=self.jc54wsqt
  self.tj0nmeoq=pi3qk2ia
  self.f80ebkjf=False
  self.iaq7b7v1=0
  self.z3olfark=[]
  self.wa45hvgo=0
  self.ub68rerv=0
  self.q7i6yuj7=pygame.font.SysFont('arial',20,bold=True)
 def mpdzp6lf(self,key):
  self.hjkuuhcl[key]+=1
  a8ax40dt=self.hjkuuhcl[key]
  if key=='r4uov5':
   wb7f6fdh=int(self.uww5wfcp*(1+0.2*a8ax40dt))
   self.gkz2u2tn+=wb7f6fdh-self.mnwxuj3a
   self.mnwxuj3a=wb7f6fdh
  elif key=='wzwl3z':
   self.w0p4e05q=self.z0b6ugvs*(1+0.08*a8ax40dt)
  elif key=='k1yjfe':
   self.d46aexl6=self.jc54wsqt+a8ax40dt
  elif key=='w2zeeq':
   self.wehlxslg=self.fcwtg1m8*(1+0.06*a8ax40dt)
  elif key=='uq0e27':
   self.k7zgf9q5=self.divsolml*max(0.6,1-0.05*a8ax40dt)
  elif key=='tqxgnr':
   self.tp2ex5t5=self.aqclpoxk+a8ax40dt*5
  elif key=='cm3v2p':
   self.q6p61xuf=1+0.15*a8ax40dt
 def lnf74t60(self,w2kql0ht):
  self.acxx6mdk[w2kql0ht]=self.acxx6mdk.get(w2kql0ht,1)+1
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
  self.bdgbk2l0.iimoe0sy+=b36htf4p+self.wa45hvgo
  self.bdgbk2l0.gdg1wjui+=vhuds3qs+self.ub68rerv
  if self.wa45hvgo>0:
   self.wa45hvgo=max(0,self.wa45hvgo-1)
  elif self.wa45hvgo<0:
   self.wa45hvgo=min(0,self.wa45hvgo+1)
  if self.ub68rerv>0:
   self.ub68rerv=max(0,self.ub68rerv-1)
  elif self.ub68rerv<0:
   self.ub68rerv=min(0,self.ub68rerv+1)
  self.bdgbk2l0.iimoe0sy=max(min(self.bdgbk2l0.iimoe0sy,v83tqll8-self.bdgbk2l0.width),0)
  self.bdgbk2l0.gdg1wjui=max(min(self.bdgbk2l0.gdg1wjui,cqoldfor-self.bdgbk2l0.height),0)
  if self.d46aexl6>0 and self.gkz2u2tn<self.mnwxuj3a:
   self.tj0nmeoq-=1
   if self.tj0nmeoq<=0:
    self.tj0nmeoq=pi3qk2ia
    self.gkz2u2tn=min(self.mnwxuj3a,self.gkz2u2tn+self.d46aexl6)
  if self.uypuplvq>=m53a5qbs[min(self.crsb4gf1,len(m53a5qbs)-1)]:
   self.hhl1737s=True
   self.uypuplvq=0
   self.crsb4gf1+=1
 def sygvwopl(self,g1b3d505,xp8mgyn2,i20cv3tl):
  iimoe0sy=self.bdgbk2l0.iimoe0sy-xp8mgyn2
  gdg1wjui=self.bdgbk2l0.gdg1wjui-i20cv3tl
  yuibrsz1=self.bdgbk2l0.centerx-xp8mgyn2
  mfyb8dal=self.bdgbk2l0.centery-i20cv3tl
  g1b3d505.blit(rv86wzs3,(yuibrsz1-rv86wzs3.get_width()//2,gdg1wjui+self.bdgbk2l0.height-8))
  u23y30ys=pygame.Rect(iimoe0sy,gdg1wjui,self.bdgbk2l0.width,self.bdgbk2l0.height)
  pygame.draw.rect(g1b3d505,mn89ltaj(self.rk8r2ykc,0.55),u23y30ys,border_radius=10)
  nyrid3dn=u23y30ys.inflate(-5,-5)
  pygame.draw.rect(g1b3d505,self.rk8r2ykc,nyrid3dn,border_radius=8)
  nvuprt77=pygame.Rect(nyrid3dn.iimoe0sy+3,nyrid3dn.gdg1wjui+3,nyrid3dn.width//2,nyrid3dn.height//3)
  pygame.draw.rect(g1b3d505,mn89ltaj(self.rk8r2ykc,2.0),nvuprt77,border_radius=4)
  pygame.draw.rect(g1b3d505,(15,15,30),u23y30ys,width=2,border_radius=10)
  d1b3jczu=math.hypot(self.ry181acj['ktaq6u'],self.ry181acj['kp82kb'])or 1
  (zdan085r,mmn32u1i)=(self.ry181acj['ktaq6u']/d1b3jczu,self.ry181acj['kp82kb']/d1b3jczu)
  jh55hewl=(yuibrsz1+zdan085r*20,mfyb8dal+mmn32u1i*20)
  zflv1xxl=(yuibrsz1-mmn32u1i*7+zdan085r*4,mfyb8dal+zdan085r*7+mmn32u1i*4)
  ukshy8nb=(yuibrsz1+mmn32u1i*7+zdan085r*4,mfyb8dal-zdan085r*7+mmn32u1i*4)
  pygame.draw.polygon(g1b3d505,iq5c34dx['mviifr'],[jh55hewl,zflv1xxl,ukshy8nb])
  pygame.draw.polygon(g1b3d505,(15,15,30),[jh55hewl,zflv1xxl,ukshy8nb],width=1)
  gmoft6yr=self.gkz2u2tn/self.mnwxuj3a
  velos6zl(g1b3d505,iimoe0sy,gdg1wjui-10,self.bdgbk2l0.width,gmoft6yr,height=6)
  dw7nh8rq(g1b3d505,pygame.Rect(225,12,372,40))
  p2nv01zd=self.q7i6yuj7.render('Hp.',True,(20,20,20))
  g1b3d505.blit(p2nv01zd,(233,23))
  velos6zl(g1b3d505,297,25,290,gmoft6yr,height=19)
  p2nv01zd=self.q7i6yuj7.render(f'{round(self.gkz2u2tn)}/{self.mnwxuj3a}',True,(20,20,20))
  width=p2nv01zd.get_width()
  height=p2nv01zd.get_height()
  g1b3d505.blit(p2nv01zd,(442-width//2,34.5-height//2))
