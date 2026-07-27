import pygame
import math
from c8v341on import*
from.tdr08cw2 import f935a0l7
class ukxvf1t2(f935a0l7):
 def __init__(self,fo75rh8l,jh55hewl,rm0j36tc):
  super().__init__(fo75rh8l,jh55hewl,rm0j36tc)
  self.zorxdtg5=0
 def y06nkwfg(self,player):
  self.zorxdtg5+=1
  return False
 def mnwxuj3a(self,player,yjluujmi,g8kk791z):
  from jw6taq6u import zy0ifznb
  yjluujmi.append(zy0ifznb(self.la3kkrzd.center))
  gj29yfc2=k1wj0tpa[self.type]
  rk8r2ykc=math.hypot(player.la3kkrzd.centerx-self.la3kkrzd.centerx,player.la3kkrzd.centery-self.la3kkrzd.centery)
  if rk8r2ykc<=gj29yfc2['pswrgv']:
   k7zgf9q5=self.hfb85p86*(100/(100+player.t5wi6fqj))
   player.azc4xl99-=k7zgf9q5
   player.pf0i9g5d.append((player.la3kkrzd.centerx,player.la3kkrzd.rm0j36tc,f'-{int(k7zgf9q5)}',iq5c34dx['ehet25']))
 def pv4ykade(self,yg87oi0e,wppsfnko,kybwmlun):
  cq6qdy4l=self.la3kkrzd.centerx-wppsfnko
  lztkkfzz=self.la3kkrzd.centery-kybwmlun
  cb2uuijn=(math.sin(self.zorxdtg5*0.15)+1)/2
  y8dd2255=int(self.la3kkrzd.width*0.6+cb2uuijn*6)
  sld4d6af=int(70+cb2uuijn*90)
  g5l8a78e=pygame.Surface((y8dd2255*2,y8dd2255*2),pygame.SRCALPHA)
  pygame.draw.circle(g5l8a78e,(200,30,20,sld4d6af),(y8dd2255,y8dd2255),y8dd2255)
  yg87oi0e.blit(g5l8a78e,(cq6qdy4l-y8dd2255,lztkkfzz-y8dd2255))
  jh55hewl=self.la3kkrzd.jh55hewl-wppsfnko
  rm0j36tc=self.la3kkrzd.rm0j36tc-kybwmlun
  self.x37pqkoj(yg87oi0e,jh55hewl,rm0j36tc,cq6qdy4l,lztkkfzz)
  (iaq7b7v1,stv18kgy)=(8,12)
  f80ebkjf=pygame.Rect(cq6qdy4l-iaq7b7v1//2,rm0j36tc-stv18kgy+2,iaq7b7v1,stv18kgy)
  pygame.draw.rect(yg87oi0e,(180,30,20),f80ebkjf,border_radius=1)
  pygame.draw.rect(yg87oi0e,(20,20,20),f80ebkjf,width=1,border_radius=1)
  for h8s2ftom in(f80ebkjf.top+3,f80ebkjf.top+8):
   pygame.draw.line(yg87oi0e,(240,240,230),(f80ebkjf.left,h8s2ftom),(f80ebkjf.right,h8s2ftom),1)
  xuu13i59=(f80ebkjf.centerx,f80ebkjf.top)
  boih5csk=(f80ebkjf.centerx+4,f80ebkjf.top-6)
  pygame.draw.line(yg87oi0e,(90,60,30),xuu13i59,boih5csk,1)
  ukshy8nb=(math.sin(self.zorxdtg5*0.4)+1)/2
  uaobt328=(255,int(150+ukshy8nb*100),40)
  pygame.draw.circle(yg87oi0e,uaobt328,boih5csk,2+int(ukshy8nb))
