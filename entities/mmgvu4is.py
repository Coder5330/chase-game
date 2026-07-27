import pygame
import math
from o100vhmy import*
from.vq3jzr25 import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,uc1xi04b,rm0j36tc,tza7x73q):
  super().__init__(uc1xi04b,rm0j36tc,tza7x73q)
  self.b36htf4p=(0,1)
  self.gn89qkns=False
  self.tk0qtl3q=0
  self.yw6zbnz8=18
 def mlikwe4b(self,player):
  sl65wvjx=player.zflse45b.centerx-self.zflse45b.centerx
  yuibrsz1=player.zflse45b.centery-self.zflse45b.centery
  i13n3bzt=math.hypot(sl65wvjx,yuibrsz1)or 1
  self.b36htf4p=(sl65wvjx/i13n3bzt,yuibrsz1/i13n3bzt)
  if self.gn89qkns:
   self.tk0qtl3q-=1
   if self.tk0qtl3q<=0:
    self.gn89qkns=False
    self.pbo119xp(player)
   return True
  if abs(player.zflse45b.rm0j36tc-self.zflse45b.rm0j36tc)<b8cgvyie and abs(player.zflse45b.tza7x73q-self.zflse45b.tza7x73q)<b8cgvyie:
   if self.lt63j3r3>0:
    self.lt63j3r3-=1
    return True
   self.gn89qkns=True
   self.tk0qtl3q=self.yw6zbnz8
   return True
  return False
 def pbo119xp(self,player):
  self.lt63j3r3=self.nqimqodp
  from zuw6taq6 import rpqk51fp
  v0rxxf36=uqjiujv6['c88d0t']['w1q8f6']
  (sl65wvjx,yuibrsz1)=(player.zflse45b.centerx-self.zflse45b.centerx,player.zflse45b.centery-self.zflse45b.centery)
  sk8yqk94=rpqk51fp('c88d0t',self.zflse45b.centerx-v0rxxf36//2,self.zflse45b.centery-v0rxxf36//2,v0rxxf36,v0rxxf36,sl65wvjx,yuibrsz1)
  sk8yqk94.ruq9e5co=self.k7zgf9q5
  self.ia529603.append(sk8yqk94)
 def i01nouht(self,npejzhya,kybwmlun,i0x65muf):
  rm0j36tc=self.zflse45b.rm0j36tc-kybwmlun
  tza7x73q=self.zflse45b.tza7x73q-i0x65muf
  lztkkfzz=self.zflse45b.centerx-kybwmlun
  f2sehe2a=self.zflse45b.centery-i0x65muf
  self.rrcbpljd(npejzhya,rm0j36tc,tza7x73q,lztkkfzz,f2sehe2a)
  (nubmxnsz,nfn1r4kz)=self.b36htf4p
  (ncyh3fvl,x6cnoljq)=(-nfn1r4kz,nubmxnsz)
  (nrpj1epk,vvslh9bh)=(lztkkfzz+nubmxnsz*14,f2sehe2a+nfn1r4kz*14)
  v7g0iiji=(nrpj1epk+ncyh3fvl*13-nubmxnsz*6,vvslh9bh+x6cnoljq*13-nfn1r4kz*6)
  h4m2ec8r=(nrpj1epk-ncyh3fvl*13-nubmxnsz*6,vvslh9bh-x6cnoljq*13-nfn1r4kz*6)
  fcwtg1m8=(nrpj1epk+nubmxnsz*6,vvslh9bh+nfn1r4kz*6)
  pygame.draw.lines(npejzhya,(110,70,30),False,[v7g0iiji,fcwtg1m8,h4m2ec8r],3)
  cnqt3wve=1-self.tk0qtl3q/self.yw6zbnz8 if self.gn89qkns else 0
  tb4ldims=(nrpj1epk-nubmxnsz*(3+cnqt3wve*10),vvslh9bh-nfn1r4kz*(3+cnqt3wve*10))
  pygame.draw.line(npejzhya,(225,225,215),v7g0iiji,tb4ldims,2)
  pygame.draw.line(npejzhya,(225,225,215),h4m2ec8r,tb4ldims,2)
  if self.gn89qkns:
   diuu9k9x=(nrpj1epk+nubmxnsz*8,vvslh9bh+nfn1r4kz*8)
   pygame.draw.line(npejzhya,iq5c34dx['rodwmq'],tb4ldims,diuu9k9x,3)
