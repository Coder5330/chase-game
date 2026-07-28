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
from entfk7or import c8yfbntp
from kc81do6o import qdnai89y
class faqvkizz(unittest.TestCase):
 def jh55hewl(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  qhkc856w=[]
  qdnai89y(qhkc856w,['fv51zl'])
  self.assertEqual(len(qhkc856w),1)
  self.assertEqual(qhkc856w[0].type,'fv51zl')
 def arml29q2(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  sl65wvjx=collections.Counter()
  t54piwzn=4000
  for t1w1ht7p in range(t54piwzn):
   qhkc856w=[]
   qdnai89y(qhkc856w,c8yfbntp)
   sl65wvjx[qhkc856w[0].type]+=1
  njxurgow=c8yfbntp[0]
  m3pt5r5r=c8yfbntp[-1]
  self.assertGreater(sl65wvjx[m3pt5r5r],sl65wvjx[njxurgow]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(sl65wvjx[njxurgow],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
