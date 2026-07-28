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
from zfiblejg import c8yfbntp
from ok38p6fv import u1ni10kq
class faqvkizz(unittest.TestCase):
 def j7f00ter(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  xuu13i59=[]
  u1ni10kq(xuu13i59,['lcf4mn'])
  self.assertEqual(len(xuu13i59),1)
  self.assertEqual(xuu13i59[0].type,'lcf4mn')
 def ra9kepad(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  qtzk3ny9=collections.Counter()
  mn89ltaj=4000
  for t1w1ht7p in range(mn89ltaj):
   xuu13i59=[]
   u1ni10kq(xuu13i59,c8yfbntp)
   qtzk3ny9[xuu13i59[0].type]+=1
  y8dd2255=c8yfbntp[0]
  wydmt8vt=c8yfbntp[-1]
  self.assertGreater(qtzk3ny9[wydmt8vt],qtzk3ny9[y8dd2255]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(qtzk3ny9[y8dd2255],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
