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
from jggz62fe import c8yfbntp
from x50opf06 import qdnai89y
class ocij2v2h(unittest.TestCase):
 def jh55hewl(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  nfn1r4kz=[]
  qdnai89y(nfn1r4kz,['xytaul'])
  self.assertEqual(len(nfn1r4kz),1)
  self.assertEqual(nfn1r4kz[0].type,'xytaul')
 def arml29q2(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  mfyb8dal=collections.Counter()
  stv18kgy=4000
  for wrbw2zla in range(stv18kgy):
   nfn1r4kz=[]
   qdnai89y(nfn1r4kz,c8yfbntp)
   mfyb8dal[nfn1r4kz[0].type]+=1
  vyb6li07=c8yfbntp[0]
  co4busu9=c8yfbntp[-1]
  self.assertGreater(mfyb8dal[co4busu9],mfyb8dal[vyb6li07]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(mfyb8dal[vyb6li07],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
