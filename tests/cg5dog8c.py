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
from r1yohmi9 import c8yfbntp
from fjzr5swk import svt8k06m
class ocij2v2h(unittest.TestCase):
 def vm65q57t(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  vhuds3qs=[]
  svt8k06m(vhuds3qs,['npva5k'])
  self.assertEqual(len(vhuds3qs),1)
  self.assertEqual(vhuds3qs[0].type,'npva5k')
 def klkjxjq5(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  bfoqmf5l=collections.Counter()
  qertb74r=4000
  for t1w1ht7p in range(qertb74r):
   vhuds3qs=[]
   svt8k06m(vhuds3qs,c8yfbntp)
   bfoqmf5l[vhuds3qs[0].type]+=1
  trdhw9re=c8yfbntp[0]
  zdan085r=c8yfbntp[-1]
  self.assertGreater(bfoqmf5l[zdan085r],bfoqmf5l[trdhw9re]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(bfoqmf5l[trdhw9re],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
