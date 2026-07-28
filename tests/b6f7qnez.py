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
from z4w1arag import c8yfbntp
from umjmbukd import gxlk8wru
class xd1wjcit(unittest.TestCase):
 def e9y3z2t4(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  mygfliji=[]
  gxlk8wru(mygfliji,['xyhhg8'])
  self.assertEqual(len(mygfliji),1)
  self.assertEqual(mygfliji[0].type,'xyhhg8')
 def s5r96khu(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  ep6beffl=collections.Counter()
  npcxa5s0=4000
  for v83tqll8 in range(npcxa5s0):
   mygfliji=[]
   gxlk8wru(mygfliji,c8yfbntp)
   ep6beffl[mygfliji[0].type]+=1
  w8y72ivg=c8yfbntp[0]
  k3z6bz8u=c8yfbntp[-1]
  self.assertGreater(ep6beffl[k3z6bz8u],ep6beffl[w8y72ivg]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(ep6beffl[w8y72ivg],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
