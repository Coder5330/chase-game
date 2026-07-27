import pygame
import math
from c8v341on import*
from.tdr08cw2 import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,fo75rh8l,jh55hewl,rm0j36tc):
  super().__init__(fo75rh8l,jh55hewl,rm0j36tc)
  self.v15cqzcu=(0,1)
  self.tk0qtl3q=False
  self.yw6zbnz8=0
  self.qbm1enf3=18
 def y06nkwfg(self,player):
  qtzk3ny9=player.la3kkrzd.centerx-self.la3kkrzd.centerx
  sl65wvjx=player.la3kkrzd.centery-self.la3kkrzd.centery
  arhnuxor=math.hypot(qtzk3ny9,sl65wvjx)or 1
  self.v15cqzcu=(qtzk3ny9/arhnuxor,sl65wvjx/arhnuxor)
  if self.tk0qtl3q:
   self.yw6zbnz8-=1
   if self.yw6zbnz8<=0:
    self.tk0qtl3q=False
    self.gubmc97c(player)
   return True
  if abs(player.la3kkrzd.jh55hewl-self.la3kkrzd.jh55hewl)<b8cgvyie and abs(player.la3kkrzd.rm0j36tc-self.la3kkrzd.rm0j36tc)<b8cgvyie:
   if self.sne6loh2>0:
    self.sne6loh2-=1
    return True
   self.tk0qtl3q=True
   self.yw6zbnz8=self.qbm1enf3
   return True
  return False
 def gubmc97c(self,player):
  self.sne6loh2=self.tp2ex5t5
  from px9ee346 import rpqk51fp
  tby49e7e=uqjiujv6['hlc83g']['k1yjfe']
  (qtzk3ny9,sl65wvjx)=(player.la3kkrzd.centerx-self.la3kkrzd.centerx,player.la3kkrzd.centery-self.la3kkrzd.centery)
  iy6qktc8=rpqk51fp('hlc83g',self.la3kkrzd.centerx-tby49e7e//2,self.la3kkrzd.centery-tby49e7e//2,tby49e7e,tby49e7e,qtzk3ny9,sl65wvjx)
  iy6qktc8.f2sehe2a=self.hfb85p86
  self.diuu9k9x.append(iy6qktc8)
 def pv4ykade(self,yg87oi0e,wppsfnko,kybwmlun):
  jh55hewl=self.la3kkrzd.jh55hewl-wppsfnko
  rm0j36tc=self.la3kkrzd.rm0j36tc-kybwmlun
  cq6qdy4l=self.la3kkrzd.centerx-wppsfnko
  lztkkfzz=self.la3kkrzd.centery-kybwmlun
  self.x37pqkoj(yg87oi0e,jh55hewl,rm0j36tc,cq6qdy4l,lztkkfzz)
  (qhkc856w,nubmxnsz)=self.v15cqzcu
  (m3pt5r5r,co4busu9)=(-nubmxnsz,qhkc856w)
  (sv5f1bcp,nrpj1epk)=(cq6qdy4l+qhkc856w*14,lztkkfzz+nubmxnsz*14)
  k82853uy=(sv5f1bcp+m3pt5r5r*13-qhkc856w*6,nrpj1epk+co4busu9*13-nubmxnsz*6)
  mu118qqv=(sv5f1bcp-m3pt5r5r*13-qhkc856w*6,nrpj1epk-co4busu9*13-nubmxnsz*6)
  divsolml=(sv5f1bcp+qhkc856w*6,nrpj1epk+nubmxnsz*6)
  pygame.draw.lines(yg87oi0e,(110,70,30),False,[k82853uy,divsolml,mu118qqv],3)
  i01nouht=1-self.yw6zbnz8/self.qbm1enf3 if self.tk0qtl3q else 0
  zo3lqi7e=(sv5f1bcp-qhkc856w*(3+i01nouht*10),nrpj1epk-nubmxnsz*(3+i01nouht*10))
  pygame.draw.line(yg87oi0e,(225,225,215),k82853uy,zo3lqi7e,2)
  pygame.draw.line(yg87oi0e,(225,225,215),mu118qqv,zo3lqi7e,2)
  if self.tk0qtl3q:
   sk8yqk94=(sv5f1bcp+qhkc856w*8,nrpj1epk+nubmxnsz*8)
   pygame.draw.line(yg87oi0e,iq5c34dx['ddxb7g'],zo3lqi7e,sk8yqk94,3)
