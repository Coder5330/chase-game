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
from rlfzkicw import k1wj0tpa
from fxc7urvq import qc06xq9j
class gdzr1yxr(unittest.TestCase):
 def su1hbj6t(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  qbbz2sf6=[]
  qc06xq9j(qbbz2sf6,['rqg433'])
  self.assertEqual(len(qbbz2sf6),1)
  self.assertEqual(qbbz2sf6[0].type,'rqg433')
 def hdw6lqwl(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  ebt3g2qz=collections.Counter()
  f8rtm4j3=4000
  for mqp49kwv in range(f8rtm4j3):
   qbbz2sf6=[]
   qc06xq9j(qbbz2sf6,k1wj0tpa)
   ebt3g2qz[qbbz2sf6[0].type]+=1
  nii6l3ue=k1wj0tpa[0]
  jxxgaear=k1wj0tpa[-1]
  self.assertGreater(ebt3g2qz[jxxgaear],ebt3g2qz[nii6l3ue]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(ebt3g2qz[nii6l3ue],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
