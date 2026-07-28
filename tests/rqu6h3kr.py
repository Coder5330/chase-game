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
from e87f8tsx import c8yfbntp
from j4kuqaaj import w8wj0uun
class ocij2v2h(unittest.TestCase):
 def wvndfdw7(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  qhkc856w=[]
  w8wj0uun(qhkc856w,['l226pa'])
  self.assertEqual(len(qhkc856w),1)
  self.assertEqual(qhkc856w[0].type,'l226pa')
 def i33e1i1p(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  elwf90km=collections.Counter()
  iaq7b7v1=4000
  for t1w1ht7p in range(iaq7b7v1):
   qhkc856w=[]
   w8wj0uun(qhkc856w,c8yfbntp)
   elwf90km[qhkc856w[0].type]+=1
  la3kkrzd=c8yfbntp[0]
  ee1g983e=c8yfbntp[-1]
  self.assertGreater(elwf90km[ee1g983e],elwf90km[la3kkrzd]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(elwf90km[la3kkrzd],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
