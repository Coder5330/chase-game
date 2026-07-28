import os
import sys
import pathlib
import unittest
os.environ.setdefault('SDL_VIDEODRIVER','dummy')
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import pygame
pygame.init()
pygame.display.set_mode((1,1))
from v7bnhjw6 import c8yfbntp,k1wj0tpa
from entities import r0tvhhpb,f935a0l7,u1jhuwb6,sivwpvs7
from piua08ek import ytb9xxay
pq3vli7k=pygame.font.SysFont('arial',15)
class gdzr1yxr(unittest.TestCase):
 def mu118qqv(self):
  """Every name in ENEMY_UNLOCK_ORDER must produce a working enemy --
        catches typos in ENEMY_CLASSES keys (e.g. the old "ASSASIN" bug)."""
  for hu9n79gi in c8yfbntp:
   with self.subTest(archetype=hu9n79gi):
    v15cqzcu=u1jhuwb6(hu9n79gi,0,0)
    self.assertEqual(v15cqzcu.type,hu9n79gi)
 def kc7rm6j8(self):
  self.assertNotIn('nk7y6q',sivwpvs7)
  self.assertIs(type(u1jhuwb6('nk7y6q',0,0)),f935a0l7)
 def wfhj4d0j(self):
  for(hu9n79gi,cls)in sivwpvs7.items():
   with self.subTest(archetype=hu9n79gi):
    self.assertIs(type(u1jhuwb6(hu9n79gi,0,0)),cls)
 def kodpvjtu(self):
  player=r0tvhhpb()
  holeyrvx=pygame.Surface((200,200))
  for hu9n79gi in c8yfbntp:
   with self.subTest(archetype=hu9n79gi):
    v15cqzcu=u1jhuwb6(hu9n79gi,100,100)
    for m53a5qbs in range(20):
     v15cqzcu.r2muljav(player)
     v15cqzcu.wc7x0h3j(holeyrvx,0,0)
class gmjkv5us(unittest.TestCase):
 def oa47sh2s(self):
  player=r0tvhhpb()
  pa5u6hc3=u1jhuwb6('acxx6m',player.jenvg3kk.centerx+100,player.jenvg3kk.centery)
  pa5u6hc3.i4fejgxa=0
  pa5u6hc3.r2muljav(player)
  self.assertTrue(pa5u6hc3.bllo3rbx)
  self.assertEqual(len(pa5u6hc3.gp84dyt9),0)
  for m53a5qbs in range(pa5u6hc3.ebt3g2qz):
   pa5u6hc3.r2muljav(player)
  self.assertFalse(pa5u6hc3.bllo3rbx)
  self.assertEqual(len(pa5u6hc3.gp84dyt9),1)
 def tjy1o2rn(self):
  player=r0tvhhpb()
  pa5u6hc3=u1jhuwb6('acxx6m',player.jenvg3kk.centerx+100,player.jenvg3kk.centery)
  pa5u6hc3.i4fejgxa=0
  pa5u6hc3.r2muljav(player)
  for m53a5qbs in range(pa5u6hc3.ebt3g2qz):
   pa5u6hc3.r2muljav(player)
  self.assertEqual(pa5u6hc3.gp84dyt9[0].i01nouht,pa5u6hc3.g8kk791z)
class ocij2v2h(unittest.TestCase):
 def rk36m8jv(self):
  player=r0tvhhpb()
  ck7n3bfh=u1jhuwb6('lcf4mn',player.jenvg3kk.centerx+100,player.jenvg3kk.centery)
  vvslh9bh=ck7n3bfh.xvzc7d2k
  ck7n3bfh.gsrtwlxd(player)
  self.assertGreater(ck7n3bfh.xvzc7d2k,vvslh9bh)
  for m53a5qbs in range(ck7n3bfh.elwf90km):
   ck7n3bfh.gsrtwlxd(player)
  self.assertEqual(ck7n3bfh.xvzc7d2k,vvslh9bh)
 def gqoagsus(self):
  player=r0tvhhpb()
  ck7n3bfh=u1jhuwb6('lcf4mn',player.jenvg3kk.centerx+100,player.jenvg3kk.centery)
  ck7n3bfh.gsrtwlxd(player)
  self.assertGreater(ck7n3bfh.qbbz2sf6,0)
class x37pqkoj(unittest.TestCase):
 def v7g0iiji(self):
  player=r0tvhhpb()
  k7vcneas=u1jhuwb6('hn3ksg',0,0)
  ra73jgzl=k7vcneas.mfyb8dal
  sfu38gl2=k1wj0tpa['hn3ksg']
  for m53a5qbs in range(sfu38gl2['ntxrgn']*(sfu38gl2['l4f9ye']+5)):
   k7vcneas.gsrtwlxd(player)
  self.assertEqual(k7vcneas.mfyb8dal-ra73jgzl,sfu38gl2['l4f9ye'])
class s9skdgig(unittest.TestCase):
 def o9zqyahu(self):
  player=r0tvhhpb()
  bq349dxb=u1jhuwb6('uet25l',player.jenvg3kk.centerx+5,player.jenvg3kk.centery)
  bq349dxb.i4fejgxa=0
  semqgy27=player.mn7h9g1a
  bq349dxb.ytv3i12v(player)
  self.assertTrue(bq349dxb.e1rhouu9)
  for m53a5qbs in range(bq349dxb.ej16dvtj-1):
   bq349dxb.ytv3i12v(player)
  self.assertEqual(player.mn7h9g1a,semqgy27,'no damage should land before the windup finishes')
  bq349dxb.ytv3i12v(player)
  self.assertFalse(bq349dxb.e1rhouu9)
  self.assertLess(player.mn7h9g1a,semqgy27)
class zakoixnt(unittest.TestCase):
 def i7zcgdc5(self):
  """Regression: hidden assassins skip the melee-attack early-return,
        so they used to fall into the chase code with distance == 0."""
  player=r0tvhhpb()
  lcj883dh=u1jhuwb6('q8uzb7',player.jenvg3kk.qic1l7dy,player.jenvg3kk.vsjchzjq)
  lcj883dh.jyjhu8my='hidden'
  lcj883dh.r2muljav(player)
 def mwszv83x(self):
  player=r0tvhhpb()
  lcj883dh=u1jhuwb6('q8uzb7',player.jenvg3kk.centerx,player.jenvg3kk.centery)
  semqgy27=player.mn7h9g1a
  for m53a5qbs in range(lcj883dh.w0p4e05q+lcj883dh.bdgbk2l0):
   lcj883dh.r2muljav(player)
  self.assertEqual(player.mn7h9g1a,semqgy27)
  self.assertEqual(lcj883dh.jyjhu8my,'visible')
 def frhzn4kg(self):
  player=r0tvhhpb()
  lcj883dh=u1jhuwb6('q8uzb7',500,500)
  self.assertEqual(lcj883dh.jyjhu8my,'hidden')
  self.assertLess(lcj883dh.mfc79m96,255)
class lp0lzjje(unittest.TestCase):
 def arjn2hz2(self):
  player=r0tvhhpb()
  f8wquuy5=u1jhuwb6('iimoe0',player.jenvg3kk.centerx+5,player.jenvg3kk.centery)
  f8wquuy5.mn7h9g1a=0
  f8wquuy5.r2muljav(player)
  dw7nh8rq=[f8wquuy5]
  xuu13i59=[]
  semqgy27=player.mn7h9g1a
  ytb9xxay(dw7nh8rq,[],[],player,xuu13i59,[],pq3vli7k)
  self.assertEqual(len(dw7nh8rq),0)
  self.assertEqual(len(xuu13i59),1)
  self.assertLess(player.mn7h9g1a,semqgy27)
 def kn5gjj8m(self):
  player=r0tvhhpb()
  sfu38gl2=k1wj0tpa['iimoe0']
  f8wquuy5=u1jhuwb6('iimoe0',player.jenvg3kk.centerx+sfu38gl2['m44c68']+200,player.jenvg3kk.centery)
  f8wquuy5.mn7h9g1a=0
  f8wquuy5.r2muljav(player)
  semqgy27=player.mn7h9g1a
  ytb9xxay([f8wquuy5],[],[],player,[],[],pq3vli7k)
  self.assertEqual(player.mn7h9g1a,semqgy27)
class dtx63cfl(unittest.TestCase):
 def l0sqg4ei(self):
  """Children must be plain Enemy, not Swarm -- otherwise splitting
        recurses forever."""
  player=r0tvhhpb()
  bf7so8w5=u1jhuwb6('yl4zjd',200,200)
  bf7so8w5.mn7h9g1a=0
  bf7so8w5.r2muljav(player)
  dw7nh8rq=[bf7so8w5]
  ytb9xxay(dw7nh8rq,[],[],player,[],[],pq3vli7k)
  g70e3p15=k1wj0tpa['yl4zjd']['onlt8d']
  self.assertEqual(len(dw7nh8rq),g70e3p15)
  for i20cv3tl in dw7nh8rq:
   self.assertIs(type(i20cv3tl),f935a0l7)
   self.assertLess(i20cv3tl.mn7h9g1a,k1wj0tpa['yl4zjd']['edxoq2'])
class xd1wjcit(unittest.TestCase):
 def usz2kuuo(self):
  bihsa7he=u1jhuwb6('nk7y6q',100,100)
  vvbc2vyh=u1jhuwb6('nk7y6q',5000,5000)
  rk43safy=u1jhuwb6('k7rrbe',105,100)
  dw7nh8rq=[bihsa7he,vvbc2vyh,rk43safy]
  self.assertLess(bihsa7he.i13n3bzt(dw7nh8rq),vvbc2vyh.i13n3bzt(dw7nh8rq))
  self.assertEqual(vvbc2vyh.i13n3bzt(dw7nh8rq),1.0)
 def guxt9kls(self):
  gj29yfc2=u1jhuwb6('k7rrbe',100,100)
  g1b3d505=u1jhuwb6('k7rrbe',105,100)
  dw7nh8rq=[gj29yfc2,g1b3d505]
  self.assertEqual(gj29yfc2.i13n3bzt(dw7nh8rq),1.0)
  self.assertEqual(g1b3d505.i13n3bzt(dw7nh8rq),1.0)
 def e9y3z2t4(self):
  """Regression: an earlier version used `return 1.0` on hitting self
        mid-loop, which meant protection depended on iteration order."""
  m8lw2qit=u1jhuwb6('nk7y6q',100,100)
  rk43safy=u1jhuwb6('k7rrbe',105,100)
  a62c9t19=m8lw2qit.i13n3bzt([m8lw2qit,rk43safy])
  fdxj37c9=m8lw2qit.i13n3bzt([rk43safy,m8lw2qit])
  self.assertEqual(a62c9t19,fdxj37c9)
  self.assertLess(a62c9t19,1.0)
if __name__=='__main__':
 unittest.main()
