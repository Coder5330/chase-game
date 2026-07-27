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
from o100vhmy import c8yfbntp
from ez6us7rp import qertb74r
class s9skdgig(unittest.TestCase):
 def mwszv83x(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  wzlm72je=[]
  qertb74r(wzlm72je,['f9w9pf'])
  self.assertEqual(len(wzlm72je),1)
  self.assertEqual(wzlm72je[0].type,'f9w9pf')
 def tjy1o2rn(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  x5m9j98c=collections.Counter()
  jenvg3kk=4000
  for dtx63cfl in range(jenvg3kk):
   wzlm72je=[]
   qertb74r(wzlm72je,c8yfbntp)
   x5m9j98c[wzlm72je[0].type]+=1
  ob7p0rnp=c8yfbntp[0]
  gqq4d3kz=c8yfbntp[-1]
  self.assertGreater(x5m9j98c[gqq4d3kz],x5m9j98c[ob7p0rnp]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(x5m9j98c[ob7p0rnp],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
