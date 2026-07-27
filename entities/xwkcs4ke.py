import pygame
import math
from c8v341on import*
from.kp82kb70 import ytb9xxay,do2m71hs
pygame.init()
n2vlpys2=pygame.Surface((z0xkxwd8+16,14),pygame.SRCALPHA)
pygame.draw.ellipse(n2vlpys2,(0,0,0,90),n2vlpys2.get_rect())
class rqf5q14j:
 def __init__(self,meta_upgrades=None):
  meta_upgrades=meta_upgrades or{}
  ry181acj=meta_upgrades.get('START_HEALTH',0)
  n04cdpqv=meta_upgrades.get('START_SPEED',0)
  ub68rerv=meta_upgrades.get('START_DAMAGE',0)
  k2ixivzk=meta_upgrades.get('START_COOLDOWN',0)
  o4dd1vn8=meta_upgrades.get('START_ARMOR',0)
  zflv1xxl=meta_upgrades.get('START_REGEN',0)
  self.ejwtl9tq=hyihair4*jxxgaear(n04cdpqv)
  self.qertb74r=self.ejwtl9tq
  self.la3kkrzd=pygame.Rect((xd1wjcit-z0xkxwd8)//2,(mqp49kwv-z0xkxwd8)//2,z0xkxwd8,z0xkxwd8)
  self.amcixdu1=iq5c34dx['msz6rv']
  self.d0r2sds8=int(1000*b78okz1p(ry181acj))
  self.je11e9ft=self.d0r2sds8
  self.azc4xl99=self.d0r2sds8
  self.f2voi8uy=0
  self.w4rcb1kj=1
  self.z7pwo6cm=False
  self.gkz2u2tn={'tcu9td':0,'xy79kv':self.qertb74r}
  self.arml29q2={}
  self.l0sqg4ei={key:0 for key in cq5uznof}
  self.ytv3i12v=q5amln4p(ub68rerv)
  self.uva2ieuc=wa45hvgo(k2ixivzk)
  self.gp84dyt9=avfmh07w(o4dd1vn8)
  self.mpdzp6lf=mctwjlsh(zflv1xxl)
  self.ruq9e5co=self.ytv3i12v
  self.jm25len6=self.uva2ieuc
  self.ywcxz2ei=1.0
  self.t5wi6fqj=self.gp84dyt9
  self.he9p3jpx=self.mpdzp6lf
  self.gp6orsnc=pi3qk2ia
  self.xwk2rv23=False
  self.gmoft6yr=0
  self.pf0i9g5d=[]
 def yw5py6b2(self,key):
  self.l0sqg4ei[key]+=1
  swwnc21o=self.l0sqg4ei[key]
  if key=='vmdk5n':
   qo6q0usw=int(self.d0r2sds8*(1+0.2*swwnc21o))
   self.azc4xl99+=qo6q0usw-self.je11e9ft
   self.je11e9ft=qo6q0usw
  elif key=='twvwvi':
   self.qertb74r=self.ejwtl9tq*(1+0.08*swwnc21o)
  elif key=='jy66p6':
   self.he9p3jpx=self.mpdzp6lf+swwnc21o
  elif key=='kxtv76':
   self.ruq9e5co=self.ytv3i12v*(1+0.06*swwnc21o)
  elif key=='mgsiwg':
   self.jm25len6=self.uva2ieuc*max(0.6,1-0.05*swwnc21o)
  elif key=='qnga41':
   self.t5wi6fqj=self.gp84dyt9+swwnc21o*5
  elif key=='m9bn18':
   self.ywcxz2ei=1+0.15*swwnc21o
 def i13n3bzt(self,wyk03o4g):
  self.arml29q2[wyk03o4g]=self.arml29q2.get(wyk03o4g,1)+1
 def lnf74t60(self):
  we4xyf9i=pygame.key.get_pressed()
  qtzk3ny9=sl65wvjx=0
  if we4xyf9i[pygame.K_UP]:
   sl65wvjx-=self.qertb74r
  if we4xyf9i[pygame.K_DOWN]:
   sl65wvjx+=self.qertb74r
  if we4xyf9i[pygame.K_LEFT]:
   qtzk3ny9-=self.qertb74r
  if we4xyf9i[pygame.K_RIGHT]:
   qtzk3ny9+=self.qertb74r
  if qtzk3ny9!=0 and sl65wvjx!=0:
   qtzk3ny9*=0.707
   sl65wvjx*=0.707
  if qtzk3ny9!=0 or sl65wvjx!=0:
   self.gkz2u2tn['tcu9td']=qtzk3ny9
   self.gkz2u2tn['xy79kv']=sl65wvjx
  self.la3kkrzd.jh55hewl+=qtzk3ny9
  self.la3kkrzd.rm0j36tc+=sl65wvjx
  self.la3kkrzd.jh55hewl=max(min(self.la3kkrzd.jh55hewl,xd1wjcit-self.la3kkrzd.width),0)
  self.la3kkrzd.rm0j36tc=max(min(self.la3kkrzd.rm0j36tc,mqp49kwv-self.la3kkrzd.height),0)
  if self.he9p3jpx>0 and self.azc4xl99<self.je11e9ft:
   self.gp6orsnc-=1
   if self.gp6orsnc<=0:
    self.gp6orsnc=pi3qk2ia
    self.azc4xl99=min(self.je11e9ft,self.azc4xl99+self.he9p3jpx)
  if self.f2voi8uy>=faqvkizz[min(self.w4rcb1kj,len(faqvkizz)-1)]:
   self.z7pwo6cm=True
   self.f2voi8uy=0
   self.w4rcb1kj+=1
 def pv4ykade(self,yg87oi0e,wppsfnko,kybwmlun):
  jh55hewl=self.la3kkrzd.jh55hewl-wppsfnko
  rm0j36tc=self.la3kkrzd.rm0j36tc-kybwmlun
  cq6qdy4l=self.la3kkrzd.centerx-wppsfnko
  lztkkfzz=self.la3kkrzd.centery-kybwmlun
  yg87oi0e.blit(n2vlpys2,(cq6qdy4l-n2vlpys2.get_width()//2,rm0j36tc+self.la3kkrzd.height-8))
  duhxid4n=pygame.Rect(jh55hewl,rm0j36tc,self.la3kkrzd.width,self.la3kkrzd.height)
  pygame.draw.rect(yg87oi0e,ytb9xxay(self.amcixdu1,0.55),duhxid4n,border_radius=10)
  onqyyf9r=duhxid4n.inflate(-5,-5)
  pygame.draw.rect(yg87oi0e,self.amcixdu1,onqyyf9r,border_radius=8)
  mytn02yc=pygame.Rect(onqyyf9r.jh55hewl+3,onqyyf9r.rm0j36tc+3,onqyyf9r.width//2,onqyyf9r.height//3)
  pygame.draw.rect(yg87oi0e,ytb9xxay(self.amcixdu1,2.0),mytn02yc,border_radius=4)
  pygame.draw.rect(yg87oi0e,(15,15,30),duhxid4n,width=2,border_radius=10)
  arhnuxor=math.hypot(self.gkz2u2tn['tcu9td'],self.gkz2u2tn['xy79kv'])or 1
  (xwqvr1h6,y2f7atwy)=(self.gkz2u2tn['tcu9td']/arhnuxor,self.gkz2u2tn['xy79kv']/arhnuxor)
  gqoagsus=(cq6qdy4l+xwqvr1h6*20,lztkkfzz+y2f7atwy*20)
  sdeekgys=(cq6qdy4l-y2f7atwy*7+xwqvr1h6*4,lztkkfzz+xwqvr1h6*7+y2f7atwy*4)
  uz6kf162=(cq6qdy4l+y2f7atwy*7+xwqvr1h6*4,lztkkfzz-xwqvr1h6*7+y2f7atwy*4)
  pygame.draw.polygon(yg87oi0e,iq5c34dx['dq3b9s'],[gqoagsus,sdeekgys,uz6kf162])
  pygame.draw.polygon(yg87oi0e,(15,15,30),[gqoagsus,sdeekgys,uz6kf162],width=1)
  njxurgow=self.azc4xl99/self.je11e9ft
  do2m71hs(yg87oi0e,jh55hewl,rm0j36tc-10,self.la3kkrzd.width,njxurgow,height=6)
