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
from j1bmqf7z import c8yfbntp
from nnnkm95d import u1ni10kq
class faqvkizz(unittest.TestCase):
 def j7f00ter(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  nubmxnsz=[]
  u1ni10kq(nubmxnsz,['r6q37c'])
  self.assertEqual(len(nubmxnsz),1)
  self.assertEqual(nubmxnsz[0].type,'r6q37c')
 def ra9kepad(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  yuibrsz1=collections.Counter()
  t54piwzn=4000
  for t1w1ht7p in range(t54piwzn):
   nubmxnsz=[]
   u1ni10kq(nubmxnsz,c8yfbntp)
   yuibrsz1[nubmxnsz[0].type]+=1
  njxurgow=c8yfbntp[0]
  m3pt5r5r=c8yfbntp[-1]
  self.assertGreater(yuibrsz1[m3pt5r5r],yuibrsz1[njxurgow]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(yuibrsz1[njxurgow],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
