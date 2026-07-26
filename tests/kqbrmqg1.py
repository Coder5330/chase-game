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
from rlfzkicw import oohp6vz4
from entities import rv86wzs3,ugez7bh2
from p2xrw6tm import rqf5q14j
from ahy25m8k import m6fao72k
class oiqvnb4g(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def xo2t8fy6(self):
  player=rv86wzs3()
  aicvqy5i=ugez7bh2('rqg433',player.wb7f6fdh.centerx,player.wb7f6fdh.centery)
  aicvqy5i.iy6qktc8=0
  self.assertFalse(player.vt26ys44)
  aicvqy5i.t5wi6fqj(player)
  self.assertTrue(player.vt26ys44)
  self.assertEqual(player.rgdej31g,oohp6vz4)
 def gxlk8wru(self):
  player=rv86wzs3()
  u8c2jwoc=rqf5q14j('jq85x7',player.wb7f6fdh.centerx,player.wb7f6fdh.centery,6,6,1,0)
  self.assertFalse(player.vt26ys44)
  u8c2jwoc.t5wi6fqj([],[],[],player=player,target='player')
  self.assertTrue(player.vt26ys44)
class ozp08j3t(unittest.TestCase):
 def qdnai89y(self):
  player=rv86wzs3()
  bllo3rbx=m6fao72k(player.wb7f6fdh.kn5gjj8m,player.wb7f6fdh.lu7jae58,50)
  e9y3z2t4=player.frhzn4kg
  bllo3rbx.k2ixivzk(player)
  self.assertTrue(bllo3rbx.f2sehe2a)
  self.assertEqual(player.frhzn4kg,e9y3z2t4+50)
class vve92mpn(unittest.TestCase):
 def q3n2qb6g(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=rv86wzs3()
  nqimqodp=rqf5q14j('ptao1c',player.wb7f6fdh.centerx-250,player.wb7f6fdh.centery,20,27,1,0)
  nqimqodp.ej16dvtj=True
  nqimqodp.clkqzfpq=nqimqodp.zefqjg02+1
  co4busu9=None
  for dw7nh8rq in range(nqimqodp.we4xyf9i):
   player.wb7f6fdh.kn5gjj8m+=player.tj0nmeoq
   nqimqodp.k2ixivzk(player)
   if nqimqodp.f2sehe2a:
    co4busu9=dw7nh8rq
    break
  self.assertIsNotNone(co4busu9,'boomerang never caught up to the player')
  self.assertLess(co4busu9,nqimqodp.we4xyf9i-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
