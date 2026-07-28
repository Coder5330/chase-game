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
from vnbnqbnx import s8qjnv8z,iq5c34dx,k1wj0tpa
from entities import r0tvhhpb,do2m71hs
from ovlhyl2l import ky20479t
from nf7qnezw import w89uzfk8
from zjr81bmq import fd6rupw2
class yr5uqpgb(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def guxt9kls(self):
  player=r0tvhhpb()
  xqzpky32=do2m71hs('m314cq',player.bdgbk2l0.centerx,player.bdgbk2l0.centery)
  xqzpky32.ra73jgzl=0
  self.assertEqual(player.z3olfark,[])
  xqzpky32.ykipu1wy(player)
  self.assertEqual(len(player.z3olfark),1)
  (iimoe0sy,gdg1wjui,i33e1i1p,color)=player.z3olfark[0]
  self.assertEqual(color,iq5c34dx['yl6lgj'])
  self.assertTrue(i33e1i1p.startswith('-'))
 def gqoagsus(self):
  player=r0tvhhpb()
  nqimqodp=ky20479t('fgb1aj',player.bdgbk2l0.centerx,player.bdgbk2l0.centery,6,6,1,0)
  nqimqodp.eohswq40=12
  nqimqodp.ykipu1wy([],[],[],player=player,target='player')
  self.assertEqual(len(player.z3olfark),1)
  self.assertEqual(player.z3olfark[0][3],iq5c34dx['yl6lgj'])
 def arjn2hz2(self):
  player=r0tvhhpb()
  f32ejx5t=do2m71hs('nk7y6q',player.bdgbk2l0.centerx+5,player.bdgbk2l0.centery)
  f32ejx5t.ra73jgzl=0
  f32ejx5t.ykipu1wy(player)
  for t1w1ht7p in range(f32ejx5t.oa47sh2s-1):
   f32ejx5t.ykipu1wy(player)
  self.assertEqual(player.z3olfark,[])
  f32ejx5t.ykipu1wy(player)
  self.assertEqual(len(player.z3olfark),1)
  self.assertEqual(player.z3olfark[0][3],iq5c34dx['yl6lgj'])
 def mu118qqv(self):
  player=r0tvhhpb()
  giec4d14=do2m71hs('dq3b9s',player.bdgbk2l0.centerx+5,player.bdgbk2l0.centery)
  giec4d14.gkz2u2tn=0
  giec4d14.j0kgazu4(player)
  fd6rupw2([giec4d14],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.z3olfark),1)
  self.assertEqual(player.z3olfark[0][3],iq5c34dx['yl6lgj'])
 def arml29q2(self):
  player=r0tvhhpb()
  xqzpky32=do2m71hs('m314cq',player.bdgbk2l0.centerx,player.bdgbk2l0.centery)
  xqzpky32.ra73jgzl=0
  w5iz31yr=player.gkz2u2tn
  xqzpky32.ykipu1wy(player)
  jqxs6esj=w5iz31yr-player.gkz2u2tn
  (t1w1ht7p,t1w1ht7p,i33e1i1p,t1w1ht7p)=player.z3olfark[0]
  self.assertEqual(i33e1i1p,f'-{int(jqxs6esj)}')
 def wfhj4d0j(self):
  xqzpky32=do2m71hs('m314cq',100,100)
  d1ieixwc=ky20479t('hn3ksg',xqzpky32.bdgbk2l0.centerx,xqzpky32.bdgbk2l0.centery,6,6,1,0)
  jqzpniqf=[xqzpky32]
  self.assertEqual(xqzpky32.z3olfark,[])
  d1ieixwc.ykipu1wy(jqzpniqf,[],[])
  self.assertEqual(len(xqzpky32.z3olfark),1)
  (iimoe0sy,gdg1wjui,i33e1i1p,color)=xqzpky32.z3olfark[0]
  self.assertEqual(color,iq5c34dx['mviifr'])
  self.assertTrue(i33e1i1p.startswith('-'))
 def frhzn4kg(self):
  g1g1r1dw=do2m71hs('m314cq',100,100)
  rh0w064w=do2m71hs('m314cq',120,100)
  jqzpniqf=[g1g1r1dw,rh0w064w]
  uysal8m1=ky20479t('umfbuv',g1g1r1dw.bdgbk2l0.centerx,g1g1r1dw.bdgbk2l0.centery,10,10,1,0)
  uysal8m1.ykipu1wy(jqzpniqf,[],[])
  self.assertEqual(len(rh0w064w.z3olfark),1)
  self.assertEqual(rh0w064w.z3olfark[0][3],iq5c34dx['mviifr'])
class pecruyf3(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def bsp7bm41(self):
  aicvqy5i=do2m71hs('i6ozx2',100,100)
  aicvqy5i.bdgbk2l0.width=aicvqy5i.bdgbk2l0.height=60
  d1ieixwc=ky20479t('v9hbn5',aicvqy5i.bdgbk2l0.centerx,aicvqy5i.bdgbk2l0.centery,4,4,0.01,0)
  cp91i3vm=0
  for t1w1ht7p in range(10):
   d1ieixwc.j0kgazu4(aicvqy5i)
   w5iz31yr=aicvqy5i.gkz2u2tn
   d1ieixwc.ykipu1wy([aicvqy5i],[],[])
   if aicvqy5i.gkz2u2tn<w5iz31yr:
    cp91i3vm+=1
   if d1ieixwc.wc7x0h3j:
    break
  self.assertEqual(cp91i3vm,1)
  self.assertEqual(d1ieixwc.g70e3p15,1)
 def ra9kepad(self):
  jqzpniqf=[do2m71hs('m314cq',100+xd8wz42o*5,100)for xd8wz42o in range(4)]
  d1ieixwc=ky20479t('v9hbn5',100,100,30,30,1,0)
  d1ieixwc.ykipu1wy(jqzpniqf,[],[])
  self.assertEqual(len(d1ieixwc.i13n3bzt),d1ieixwc.vt26ys44,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(d1ieixwc.wc7x0h3j)
class mqp49kwv(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def y06nkwfg(self):
  player=r0tvhhpb()
  xqzpky32=do2m71hs('m314cq',player.bdgbk2l0.centerx,player.bdgbk2l0.centery)
  xqzpky32.ra73jgzl=0
  self.assertFalse(player.f80ebkjf)
  xqzpky32.ykipu1wy(player)
  self.assertTrue(player.f80ebkjf)
  self.assertEqual(player.iaq7b7v1,s8qjnv8z)
 def k82853uy(self):
  player=r0tvhhpb()
  nqimqodp=ky20479t('fgb1aj',player.bdgbk2l0.centerx,player.bdgbk2l0.centery,6,6,1,0)
  self.assertFalse(player.f80ebkjf)
  nqimqodp.ykipu1wy([],[],[],player=player,target='player')
  self.assertTrue(player.f80ebkjf)
class azebbk7w(unittest.TestCase):
 def m3hcws2w(self):
  player=r0tvhhpb()
  qbbz2sf6=w89uzfk8(player.bdgbk2l0.iimoe0sy,player.bdgbk2l0.gdg1wjui,50)
  ehet25lz=player.uypuplvq
  qbbz2sf6.j0kgazu4(player)
  self.assertTrue(qbbz2sf6.wc7x0h3j)
  self.assertEqual(player.uypuplvq,ehet25lz+50)
class gl08yg0j(unittest.TestCase):
 def v7g0iiji(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=r0tvhhpb()
  qbm1enf3=ky20479t('m9bn18',player.bdgbk2l0.centerx-250,player.bdgbk2l0.centery,20,27,1,0)
  qbm1enf3.htgsiwg0=True
  qbm1enf3.sl65wvjx=qbm1enf3.azc4xl99+1
  v0rxxf36=None
  for x9bp4m18 in range(qbm1enf3.nii6l3ue):
   player.bdgbk2l0.iimoe0sy+=player.w0p4e05q
   qbm1enf3.j0kgazu4(player)
   if qbm1enf3.wc7x0h3j:
    v0rxxf36=x9bp4m18
    break
  self.assertIsNotNone(v0rxxf36,'boomerang never caught up to the player')
  self.assertLess(v0rxxf36,qbm1enf3.nii6l3ue-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
