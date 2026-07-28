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
from v7bnhjw6 import c8yfbntp
from piua08ek import yp3cyazb
class faqvkizz(unittest.TestCase):
 def y06nkwfg(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  dw7nh8rq=[]
  yp3cyazb(dw7nh8rq,['nk7y6q'])
  self.assertEqual(len(dw7nh8rq),1)
  self.assertEqual(dw7nh8rq[0].type,'nk7y6q')
 def gf8f3gr9(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  vw6m7b5c=collections.Counter()
  uaobt328=4000
  for m53a5qbs in range(uaobt328):
   dw7nh8rq=[]
   yp3cyazb(dw7nh8rq,c8yfbntp)
   vw6m7b5c[dw7nh8rq[0].type]+=1
  mmn32u1i=c8yfbntp[0]
  jl90pxrl=c8yfbntp[-1]
  self.assertGreater(vw6m7b5c[jl90pxrl],vw6m7b5c[mmn32u1i]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(vw6m7b5c[mmn32u1i],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
