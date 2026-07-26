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
 def z5x8a5fb(self):
  player=rv86wzs3()
  aicvqy5i=ugez7bh2('rqg433',player.mu4fmpkx.centerx,player.mu4fmpkx.centery)
  aicvqy5i.iy6qktc8=0
  self.assertFalse(player.v6xii5p5)
  aicvqy5i.t5wi6fqj(player)
  self.assertTrue(player.v6xii5p5)
  self.assertEqual(player.ljk4q5v7,oohp6vz4)
 def y9ayq6ww(self):
  player=rv86wzs3()
  u8c2jwoc=rqf5q14j('jq85x7',player.mu4fmpkx.centerx,player.mu4fmpkx.centery,6,6,1,0)
  self.assertFalse(player.v6xii5p5)
  u8c2jwoc.t5wi6fqj([],[],[],player=player,target='player')
  self.assertTrue(player.v6xii5p5)
class ozp08j3t(unittest.TestCase):
 def ysqg8x80(self):
  player=rv86wzs3()
  bllo3rbx=m6fao72k(player.mu4fmpkx.kn5gjj8m,player.mu4fmpkx.lu7jae58,50)
  e9y3z2t4=player.frhzn4kg
  bllo3rbx.ub68rerv(player)
  self.assertTrue(bllo3rbx.f2sehe2a)
  self.assertEqual(player.frhzn4kg,e9y3z2t4+50)
class vve92mpn(unittest.TestCase):
 def qcd81twh(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=rv86wzs3()
  nqimqodp=rqf5q14j('ptao1c',player.mu4fmpkx.centerx-250,player.mu4fmpkx.centery,20,27,1,0)
  nqimqodp.ej16dvtj=True
  nqimqodp.clkqzfpq=nqimqodp.zefqjg02+1
  ncyh3fvl=None
  for dw7nh8rq in range(nqimqodp.ftlpq2wg):
   player.mu4fmpkx.kn5gjj8m+=player.fd6rupw2
   nqimqodp.ub68rerv(player)
   if nqimqodp.f2sehe2a:
    ncyh3fvl=dw7nh8rq
    break
  self.assertIsNotNone(ncyh3fvl,'boomerang never caught up to the player')
  self.assertLess(ncyh3fvl,nqimqodp.ftlpq2wg-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
