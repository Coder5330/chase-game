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
from c8v341on import c8yfbntp
from uu86zjq7 import wd6r30oj
class gl08yg0j(unittest.TestCase):
 def rr9u1oe5(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  g8kk791z=[]
  wd6r30oj(g8kk791z,['mbslul'])
  self.assertEqual(len(g8kk791z),1)
  self.assertEqual(g8kk791z[0].type,'mbslul')
 def p2nv01zd(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  clkqzfpq=collections.Counter()
  g1g1r1dw=4000
  for ocij2v2h in range(g1g1r1dw):
   g8kk791z=[]
   wd6r30oj(g8kk791z,c8yfbntp)
   clkqzfpq[g8kk791z[0].type]+=1
  dq2fa39e=c8yfbntp[0]
  mcup8ijl=c8yfbntp[-1]
  self.assertGreater(clkqzfpq[mcup8ijl],clkqzfpq[dq2fa39e]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(clkqzfpq[dq2fa39e],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
