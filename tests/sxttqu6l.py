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
from vnbnqbnx import c8yfbntp
from zjr81bmq import jyjhu8my
class faqvkizz(unittest.TestCase):
 def ayr1k12v(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  jqzpniqf=[]
  jyjhu8my(jqzpniqf,['m314cq'])
  self.assertEqual(len(jqzpniqf),1)
  self.assertEqual(jqzpniqf[0].type,'m314cq')
 def mlikwe4b(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  cnqt3wve=collections.Counter()
  wtl0thhz=4000
  for t1w1ht7p in range(wtl0thhz):
   jqzpniqf=[]
   jyjhu8my(jqzpniqf,c8yfbntp)
   cnqt3wve[jqzpniqf[0].type]+=1
  co4busu9=c8yfbntp[0]
  got7txkd=c8yfbntp[-1]
  self.assertGreater(cnqt3wve[got7txkd],cnqt3wve[co4busu9]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(cnqt3wve[co4busu9],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
