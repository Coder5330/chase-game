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
from z1yhxso7 import c8yfbntp
from z286utio import byl68ntk
class xd1wjcit(unittest.TestCase):
 def usz2kuuo(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  yjluujmi=[]
  byl68ntk(yjluujmi,['m1v3zo'])
  self.assertEqual(len(yjluujmi),1)
  self.assertEqual(yjluujmi[0].type,'m1v3zo')
 def o9zqyahu(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  wi8skch8=collections.Counter()
  v0rxxf36=4000
  for v83tqll8 in range(v0rxxf36):
   yjluujmi=[]
   byl68ntk(yjluujmi,c8yfbntp)
   wi8skch8[yjluujmi[0].type]+=1
  y8bv78hu=c8yfbntp[0]
  s8438tgb=c8yfbntp[-1]
  self.assertGreater(wi8skch8[s8438tgb],wi8skch8[y8bv78hu]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(wi8skch8[y8bv78hu],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
