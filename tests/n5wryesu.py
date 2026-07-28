import os
import sys
import pathlib
import random
import unittest
import collections
os.environ.setdefault('SDL_VIDEODRIVER','dummy')
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import pygame
pygame.init()
pygame.display.set_mode((1,1))
from ykatqyds import c8yfbntp
from ifcl5efj import hcxhgnze
class ocij2v2h(unittest.TestCase):
 def ejbzutru(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  nfn1r4kz=[]
  hcxhgnze(nfn1r4kz,['s1whhk'])
  self.assertEqual(len(nfn1r4kz),1)
  self.assertEqual(nfn1r4kz[0].type,'s1whhk')
 def jh55hewl(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  sl65wvjx=collections.Counter()
  gxlk8wru=4000
  for wrbw2zla in range(gxlk8wru):
   nfn1r4kz=[]
   hcxhgnze(nfn1r4kz,c8yfbntp)
   sl65wvjx[nfn1r4kz[0].type]+=1
  gp6orsnc=c8yfbntp[0]
  x6cnoljq=c8yfbntp[-1]
  self.assertGreater(sl65wvjx[x6cnoljq],sl65wvjx[gp6orsnc]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(sl65wvjx[gp6orsnc],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
