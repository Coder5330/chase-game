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
from en1x2gdg import c8yfbntp
from jxgbngz6 import k8qeoz0k
class s9skdgig(unittest.TestCase):
 def rk36m8jv(self):
  """Start-of-run edge case: only GRUNT unlocked."""
  wc7x0h3j=[]
  k8qeoz0k(wc7x0h3j,['wyn6sj'])
  self.assertEqual(len(wc7x0h3j),1)
  self.assertEqual(wc7x0h3j[0].type,'wyn6sj')
 def p7pchcbn(self):
  """Regression: spawn_enemy used to use random.choice(), giving every
        unlocked archetype an equal chance -- meaning a level-10 run still
        mostly spawned trivial GRUNTs. Weighting should make the most
        recently unlocked archetype (last in the list) clearly favoured
        over the first, without the first dropping to zero."""
  random.seed(1234)
  obc2nnuv=collections.Counter()
  xasez2nx=4000
  for dtx63cfl in range(xasez2nx):
   wc7x0h3j=[]
   k8qeoz0k(wc7x0h3j,c8yfbntp)
   obc2nnuv[wc7x0h3j[0].type]+=1
  jr5rdnpx=c8yfbntp[0]
  vk3g84ut=c8yfbntp[-1]
  self.assertGreater(obc2nnuv[vk3g84ut],obc2nnuv[jr5rdnpx]*5,'most recently unlocked archetype should spawn far more often')
  self.assertGreater(obc2nnuv[jr5rdnpx],0,'oldest archetype should still spawn sometimes, not vanish entirely')
if __name__=='__main__':
 unittest.main()
