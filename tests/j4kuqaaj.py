import os
import sys
import pathlib
import unittest
import math
os.environ.setdefault('SDL_VIDEODRIVER','dummy')
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import pygame
pygame.init()
pygame.display.set_mode((1,1))
from ykatqyds import y38daly8,iq5c34dx,k1wj0tpa
from entities import ky20479t,yuibrsz1
from tnyy95g5 import mvxdp5gj
from pfh8aoy7 import w89uzfk8
from ifcl5efj import wd6r30oj
class pecruyf3(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def jdqqzrlf(self):
  player=ky20479t()
  jo8e7flq=yuibrsz1('s1whhk',player.uaobt328.centerx,player.uaobt328.centery)
  jo8e7flq.kmgfxc08=0
  self.assertEqual(player.k1taa0i5,[])
  jo8e7flq.ra73jgzl(player)
  self.assertEqual(len(player.k1taa0i5),1)
  (owdz09wf,lb4y4k7b,ucu7onz3,color)=player.k1taa0i5[0]
  self.assertEqual(color,iq5c34dx['az3m55'])
  self.assertTrue(ucu7onz3.startswith('-'))
 def usz2kuuo(self):
  player=ky20479t()
  vj8yrddp=mvxdp5gj('c1l631',player.uaobt328.centerx,player.uaobt328.centery,6,6,1,0)
  vj8yrddp.wc7x0h3j=12
  vj8yrddp.ra73jgzl([],[],[],player=player,target='player')
  self.assertEqual(len(player.k1taa0i5),1)
  self.assertEqual(player.k1taa0i5[0][3],iq5c34dx['az3m55'])
 def guxt9kls(self):
  player=ky20479t()
  nd6357oo=yuibrsz1('nomuwa',player.uaobt328.centerx+5,player.uaobt328.centery)
  nd6357oo.kmgfxc08=0
  nd6357oo.ra73jgzl(player)
  for wrbw2zla in range(nd6357oo.kn5gjj8m-1):
   nd6357oo.ra73jgzl(player)
  self.assertEqual(player.k1taa0i5,[])
  nd6357oo.ra73jgzl(player)
  self.assertEqual(len(player.k1taa0i5),1)
  self.assertEqual(player.k1taa0i5[0][3],iq5c34dx['az3m55'])
 def lu7jae58(self):
  player=ky20479t()
  yw6zbnz8=yuibrsz1('l7wr0r',player.uaobt328.centerx+5,player.uaobt328.centery)
  yw6zbnz8.w4rcb1kj=0
  yw6zbnz8.mu4fmpkx(player)
  wd6r30oj([yw6zbnz8],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.k1taa0i5),1)
  self.assertEqual(player.k1taa0i5[0][3],iq5c34dx['az3m55'])
 def bu4xszjn(self):
  player=ky20479t()
  jo8e7flq=yuibrsz1('s1whhk',player.uaobt328.centerx,player.uaobt328.centery)
  jo8e7flq.kmgfxc08=0
  f55dmcxx=player.w4rcb1kj
  jo8e7flq.ra73jgzl(player)
  dw7nh8rq=f55dmcxx-player.w4rcb1kj
  (wrbw2zla,wrbw2zla,ucu7onz3,wrbw2zla)=player.k1taa0i5[0]
  self.assertEqual(ucu7onz3,f'-{int(dw7nh8rq)}')
 def m3hcws2w(self):
  jo8e7flq=yuibrsz1('s1whhk',100,100)
  hugysm8t=mvxdp5gj('og8cd3',jo8e7flq.uaobt328.centerx,jo8e7flq.uaobt328.centery,6,6,1,0)
  nfn1r4kz=[jo8e7flq]
  self.assertEqual(jo8e7flq.k1taa0i5,[])
  hugysm8t.ra73jgzl(nfn1r4kz,[],[])
  self.assertEqual(len(jo8e7flq.k1taa0i5),1)
  (owdz09wf,lb4y4k7b,ucu7onz3,color)=jo8e7flq.k1taa0i5[0]
  self.assertEqual(color,iq5c34dx['kp82kb'])
  self.assertTrue(ucu7onz3.startswith('-'))
 def qxt6ridl(self):
  gmoft6yr=yuibrsz1('s1whhk',100,100)
  nv23gxj0=yuibrsz1('s1whhk',120,100)
  nfn1r4kz=[gmoft6yr,nv23gxj0]
  qbm1enf3=mvxdp5gj('p0s1f5',gmoft6yr.uaobt328.centerx,gmoft6yr.uaobt328.centery,10,10,1,0)
  qbm1enf3.ra73jgzl(nfn1r4kz,[],[])
  self.assertEqual(len(nv23gxj0.k1taa0i5),1)
  self.assertEqual(nv23gxj0.k1taa0i5[0][3],iq5c34dx['kp82kb'])
class jdiuovw1(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def mlikwe4b(self):
  kx74d0gj=yuibrsz1('e0s41k',100,100)
  kx74d0gj.uaobt328.width=kx74d0gj.uaobt328.height=60
  hugysm8t=mvxdp5gj('kk2y77',kx74d0gj.uaobt328.centerx,kx74d0gj.uaobt328.centery,4,4,0.01,0)
  xd8wz42o=0
  for wrbw2zla in range(10):
   hugysm8t.mu4fmpkx(kx74d0gj)
   f55dmcxx=kx74d0gj.w4rcb1kj
   hugysm8t.ra73jgzl([kx74d0gj],[],[])
   if kx74d0gj.w4rcb1kj<f55dmcxx:
    xd8wz42o+=1
   if hugysm8t.x875aud9:
    break
  self.assertEqual(xd8wz42o,1)
  self.assertEqual(hugysm8t.zqcootnj,1)
 def qxb7gbdg(self):
  nfn1r4kz=[yuibrsz1('s1whhk',100+nyrid3dn*5,100)for nyrid3dn in range(4)]
  hugysm8t=mvxdp5gj('kk2y77',100,100,30,30,1,0)
  hugysm8t.ra73jgzl(nfn1r4kz,[],[])
  self.assertEqual(len(hugysm8t.swwnc21o),hugysm8t.xsspye9r,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(hugysm8t.x875aud9)
class xd1wjcit(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def ra9kepad(self):
  player=ky20479t()
  jo8e7flq=yuibrsz1('s1whhk',player.uaobt328.centerx,player.uaobt328.centery)
  jo8e7flq.kmgfxc08=0
  self.assertFalse(player.ck7n3bfh)
  jo8e7flq.ra73jgzl(player)
  self.assertTrue(player.ck7n3bfh)
  self.assertEqual(player.xo2t8fy6,y38daly8)
 def wfhj4d0j(self):
  player=ky20479t()
  vj8yrddp=mvxdp5gj('c1l631',player.uaobt328.centerx,player.uaobt328.centery,6,6,1,0)
  self.assertFalse(player.ck7n3bfh)
  vj8yrddp.ra73jgzl([],[],[],player=player,target='player')
  self.assertTrue(player.ck7n3bfh)
class yr5uqpgb(unittest.TestCase):
 def eq3tq1s0(self):
  player=ky20479t()
  mfyb8dal=w89uzfk8(player.uaobt328.owdz09wf,player.uaobt328.lb4y4k7b,50)
  f1bl08kg=player.rn16uxf5
  mfyb8dal.mu4fmpkx(player)
  self.assertTrue(mfyb8dal.x875aud9)
  self.assertEqual(player.rn16uxf5,f1bl08kg+50)
class s9skdgig(unittest.TestCase):
 def klkjxjq5(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=ky20479t()
  tk0qtl3q=mvxdp5gj('zgvz9a',player.uaobt328.centerx-250,player.uaobt328.centery,20,27,1,0)
  tk0qtl3q.zpfb3hn1=True
  tk0qtl3q.g8kk791z=tk0qtl3q.mpyxdw2z+1
  t5sn961j=None
  for fekrcppr in range(tk0qtl3q.mcup8ijl):
   player.uaobt328.owdz09wf+=player.bf7so8w5
   tk0qtl3q.mu4fmpkx(player)
   if tk0qtl3q.x875aud9:
    t5sn961j=fekrcppr
    break
  self.assertIsNotNone(t5sn961j,'boomerang never caught up to the player')
  self.assertLess(t5sn961j,tk0qtl3q.mcup8ijl-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
