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
from i1arxabo import c8yfbntp
from tbzegbl2 import gj29yfc2
class jdiuovw1(unittest.TestCase):
 def n8sa3idy(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  uc1xi04b=[]
  gj29yfc2(uc1xi04b,['uk99jc'])
  self.assertEqual(len(uc1xi04b),1)
  self.assertEqual(uc1xi04b[0].type,'uk99jc')
 def rk36m8jv(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  cq6qdy4l=collections.Counter()
  gmoft6yr=4000
  for ygspk9p3 in range(gmoft6yr):
   uc1xi04b=[]
   gj29yfc2(uc1xi04b,c8yfbntp)
   cq6qdy4l[uc1xi04b[0].type]+=1
  fdxj37c9=c8yfbntp[0]
  ob7p0rnp=c8yfbntp[-1]
  self.assertGreater(cq6qdy4l[ob7p0rnp],cq6qdy4l[fdxj37c9]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(cq6qdy4l[fdxj37c9],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
