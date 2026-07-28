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
from r1yohmi9 import y38daly8,iq5c34dx,k1wj0tpa
from entities import ky20479t,l9enulqj
from cw2maiet import mvxdp5gj
from bg2y8rgy import w89uzfk8
from fjzr5swk import qc06xq9j
class pecruyf3(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def gf8f3gr9(self):
  player=ky20479t()
  m20u9isy=l9enulqj('npva5k',player.nxxjve3d.centerx,player.nxxjve3d.centery)
  m20u9isy.b06xkxb9=0
  self.assertEqual(player.exvaj2k8,[])
  m20u9isy.d0r2sds8(player)
  self.assertEqual(len(player.exvaj2k8),1)
  (un9sz6rv,ehet25lz,wyk03o4g,color)=player.exvaj2k8[0]
  self.assertEqual(color,iq5c34dx['cparsg'])
  self.assertTrue(wyk03o4g.startswith('-'))
 def yoyohaz7(self):
  player=ky20479t()
  lcj883dh=mvxdp5gj('k4fbl9',player.nxxjve3d.centerx,player.nxxjve3d.centery,6,6,1,0)
  lcj883dh.qbbz2sf6=12
  lcj883dh.d0r2sds8([],[],[],player=player,target='player')
  self.assertEqual(len(player.exvaj2k8),1)
  self.assertEqual(player.exvaj2k8[0][3],iq5c34dx['cparsg'])
 def k82853uy(self):
  player=ky20479t()
  i0x65muf=l9enulqj('py55p1',player.nxxjve3d.centerx+5,player.nxxjve3d.centery)
  i0x65muf.b06xkxb9=0
  i0x65muf.d0r2sds8(player)
  for t1w1ht7p in range(i0x65muf.p7pchcbn-1):
   i0x65muf.d0r2sds8(player)
  self.assertEqual(player.exvaj2k8,[])
  i0x65muf.d0r2sds8(player)
  self.assertEqual(len(player.exvaj2k8),1)
  self.assertEqual(player.exvaj2k8[0][3],iq5c34dx['cparsg'])
 def gqoagsus(self):
  player=ky20479t()
  jc54wsqt=l9enulqj('lgnrfi',player.nxxjve3d.centerx+5,player.nxxjve3d.centery)
  jc54wsqt.zpajssuu=0
  jc54wsqt.bihsa7he(player)
  qc06xq9j([jc54wsqt],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.exvaj2k8),1)
  self.assertEqual(player.exvaj2k8[0][3],iq5c34dx['cparsg'])
 def m3hcws2w(self):
  player=ky20479t()
  m20u9isy=l9enulqj('npva5k',player.nxxjve3d.centerx,player.nxxjve3d.centery)
  m20u9isy.b06xkxb9=0
  rk2u1rsu=player.zpajssuu
  m20u9isy.d0r2sds8(player)
  rzewviyt=rk2u1rsu-player.zpajssuu
  (t1w1ht7p,t1w1ht7p,wyk03o4g,t1w1ht7p)=player.exvaj2k8[0]
  self.assertEqual(wyk03o4g,f'-{int(rzewviyt)}')
 def e9y3z2t4(self):
  m20u9isy=l9enulqj('npva5k',100,100)
  yw6zbnz8=mvxdp5gj('r6q37c',m20u9isy.nxxjve3d.centerx,m20u9isy.nxxjve3d.centery,6,6,1,0)
  vhuds3qs=[m20u9isy]
  self.assertEqual(m20u9isy.exvaj2k8,[])
  yw6zbnz8.d0r2sds8(vhuds3qs,[],[])
  self.assertEqual(len(m20u9isy.exvaj2k8),1)
  (un9sz6rv,ehet25lz,wyk03o4g,color)=m20u9isy.exvaj2k8[0]
  self.assertEqual(color,iq5c34dx['jyzqii'])
  self.assertTrue(wyk03o4g.startswith('-'))
 def o9zqyahu(self):
  v6xii5p5=l9enulqj('npva5k',100,100)
  sfu38gl2=l9enulqj('npva5k',120,100)
  vhuds3qs=[v6xii5p5,sfu38gl2]
  j2vmcqbn=mvxdp5gj('eff1bl',v6xii5p5.nxxjve3d.centerx,v6xii5p5.nxxjve3d.centery,10,10,1,0)
  j2vmcqbn.d0r2sds8(vhuds3qs,[],[])
  self.assertEqual(len(sfu38gl2.exvaj2k8),1)
  self.assertEqual(sfu38gl2.exvaj2k8[0][3],iq5c34dx['jyzqii'])
class jdiuovw1(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def a1tbrwr9(self):
  gubmc97c=l9enulqj('bdbpgv',100,100)
  gubmc97c.nxxjve3d.width=gubmc97c.nxxjve3d.height=60
  yw6zbnz8=mvxdp5gj('fv51zl',gubmc97c.nxxjve3d.centerx,gubmc97c.nxxjve3d.centery,4,4,0.01,0)
  nvuprt77=0
  for t1w1ht7p in range(10):
   yw6zbnz8.bihsa7he(gubmc97c)
   rk2u1rsu=gubmc97c.zpajssuu
   yw6zbnz8.d0r2sds8([gubmc97c],[],[])
   if gubmc97c.zpajssuu<rk2u1rsu:
    nvuprt77+=1
   if yw6zbnz8.eohswq40:
    break
  self.assertEqual(nvuprt77,1)
  self.assertEqual(yw6zbnz8.ouuylaja,1)
 def zanouof0(self):
  vhuds3qs=[l9enulqj('npva5k',100+cp91i3vm*5,100)for cp91i3vm in range(4)]
  yw6zbnz8=mvxdp5gj('fv51zl',100,100,30,30,1,0)
  yw6zbnz8.d0r2sds8(vhuds3qs,[],[])
  self.assertEqual(len(yw6zbnz8.semqgy27),yw6zbnz8.todsx4nx,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(yw6zbnz8.eohswq40)
class xd1wjcit(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def usz2kuuo(self):
  player=ky20479t()
  m20u9isy=l9enulqj('npva5k',player.nxxjve3d.centerx,player.nxxjve3d.centery)
  m20u9isy.b06xkxb9=0
  self.assertFalse(player.xxns2zyb)
  m20u9isy.d0r2sds8(player)
  self.assertTrue(player.xxns2zyb)
  self.assertEqual(player.mn89ltaj,y38daly8)
 def rk36m8jv(self):
  player=ky20479t()
  lcj883dh=mvxdp5gj('k4fbl9',player.nxxjve3d.centerx,player.nxxjve3d.centery,6,6,1,0)
  self.assertFalse(player.xxns2zyb)
  lcj883dh.d0r2sds8([],[],[],player=player,target='player')
  self.assertTrue(player.xxns2zyb)
class yr5uqpgb(unittest.TestCase):
 def qxt6ridl(self):
  player=ky20479t()
  hfb85p86=w89uzfk8(player.nxxjve3d.un9sz6rv,player.nxxjve3d.ehet25lz,50)
  kr0aymk9=player.cgsq7ait
  hfb85p86.bihsa7he(player)
  self.assertTrue(hfb85p86.eohswq40)
  self.assertEqual(player.cgsq7ait,kr0aymk9+50)
class s9skdgig(unittest.TestCase):
 def n8sa3idy(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=ky20479t()
  z0b6ugvs=mvxdp5gj('n1ajo0',player.nxxjve3d.centerx-250,player.nxxjve3d.centery,20,27,1,0)
  z0b6ugvs.tza7x73q=True
  z0b6ugvs.i01nouht=z0b6ugvs.r98s4c3b+1
  myrp5ge0=None
  for mc8qizk3 in range(z0b6ugvs.n04cdpqv):
   player.nxxjve3d.un9sz6rv+=player.jyjhu8my
   z0b6ugvs.bihsa7he(player)
   if z0b6ugvs.eohswq40:
    myrp5ge0=mc8qizk3
    break
  self.assertIsNotNone(myrp5ge0,'boomerang never caught up to the player')
  self.assertLess(myrp5ge0,z0b6ugvs.n04cdpqv-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
