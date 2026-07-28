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
from omerbyea import c8yfbntp
from hb1r8vnr import mnx4sn6s
class ocij2v2h(unittest.TestCase):
 def ywcxz2ei(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  nubmxnsz=[]
  mnx4sn6s(nubmxnsz,['v9hbn5'])
  self.assertEqual(len(nubmxnsz),1)
  self.assertEqual(nubmxnsz[0].type,'v9hbn5')
 def x9h0dxho(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  qtzk3ny9=collections.Counter()
  uwxrum2l=4000
  for wrbw2zla in range(uwxrum2l):
   nubmxnsz=[]
   mnx4sn6s(nubmxnsz,c8yfbntp)
   qtzk3ny9[nubmxnsz[0].type]+=1
  he9p3jpx=c8yfbntp[0]
  ncyh3fvl=c8yfbntp[-1]
  self.assertGreater(qtzk3ny9[ncyh3fvl],qtzk3ny9[he9p3jpx]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(qtzk3ny9[he9p3jpx],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
