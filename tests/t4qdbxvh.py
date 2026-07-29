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
from j1bmqf7z import c8yfbntp,k1wj0tpa
from entities import r0tvhhpb,f935a0l7,mfyb8dal,sivwpvs7
from nnnkm95d import pllkstn3
pq3vli7k=pygame.font.SysFont('arial',15)
class gdzr1yxr(unittest.TestCase):
 def y06nkwfg(self):
  """Every name in ENEMY_UNLOCK_ORDER must produce a working enemy --
        catches typos in ENEMY_CLASSES keys (e.g. the old "ASSASIN" bug)."""
  for got7txkd in c8yfbntp:
   with self.subTest(archetype=got7txkd):
    zqcootnj=mfyb8dal(got7txkd,0,0)
    self.assertEqual(zqcootnj.type,got7txkd)
 def l0sqg4ei(self):
  self.assertNotIn('r6q37c',sivwpvs7)
  self.assertIs(type(mfyb8dal('r6q37c',0,0)),f935a0l7)
 def kc1fjotg(self):
  for(got7txkd,cls)in sivwpvs7.items():
   with self.subTest(archetype=got7txkd):
    self.assertIs(type(mfyb8dal(got7txkd,0,0)),cls)
 def h4m2ec8r(self):
  player=r0tvhhpb()
  rwybow23=pygame.Surface((200,200))
  for got7txkd in c8yfbntp:
   with self.subTest(archetype=got7txkd):
    zqcootnj=mfyb8dal(got7txkd,100,100)
    for t1w1ht7p in range(20):
     zqcootnj.move(player)
     zqcootnj.v15cqzcu(rwybow23,0,0)
class gmjkv5us(unittest.TestCase):
 def e9y3z2t4(self):
  player=r0tvhhpb()
  duhxid4n=mfyb8dal('eolaq6',player.npcxa5s0.centerx+100,player.npcxa5s0.centery)
  duhxid4n.g11kerpe=0
  duhxid4n.move(player)
  self.assertTrue(duhxid4n.ep6beffl)
  self.assertEqual(len(duhxid4n.c0hpmnz1),0)
  for t1w1ht7p in range(duhxid4n.wzs13c9x):
   duhxid4n.move(player)
  self.assertFalse(duhxid4n.ep6beffl)
  self.assertEqual(len(duhxid4n.c0hpmnz1),1)
 def a1tbrwr9(self):
  player=r0tvhhpb()
  duhxid4n=mfyb8dal('eolaq6',player.npcxa5s0.centerx+100,player.npcxa5s0.centery)
  duhxid4n.g11kerpe=0
  duhxid4n.move(player)
  for t1w1ht7p in range(duhxid4n.wzs13c9x):
   duhxid4n.move(player)
  self.assertEqual(duhxid4n.c0hpmnz1[0].wc7x0h3j,duhxid4n.velos6zl)
class ocij2v2h(unittest.TestCase):
 def wfhj4d0j(self):
  player=r0tvhhpb()
  q6nqqb9l=mfyb8dal('eqkwqh',player.npcxa5s0.centerx+100,player.npcxa5s0.centery)
  u23y30ys=q6nqqb9l.p7b1ijiy
  q6nqqb9l.qic1l7dy(player)
  self.assertGreater(q6nqqb9l.p7b1ijiy,u23y30ys)
  for t1w1ht7p in range(q6nqqb9l.uc1xi04b):
   q6nqqb9l.qic1l7dy(player)
  self.assertEqual(q6nqqb9l.p7b1ijiy,u23y30ys)
 def lu7jae58(self):
  player=r0tvhhpb()
  q6nqqb9l=mfyb8dal('eqkwqh',player.npcxa5s0.centerx+100,player.npcxa5s0.centery)
  q6nqqb9l.qic1l7dy(player)
  self.assertGreater(q6nqqb9l.fo75rh8l,0)
class x37pqkoj(unittest.TestCase):
 def rb1s9dwd(self):
  player=r0tvhhpb()
  yoyohaz7=mfyb8dal('m44c68',0,0)
  bq349dxb=yoyohaz7.zefqjg02
  xxkdq95g=k1wj0tpa['m44c68']
  for t1w1ht7p in range(xxkdq95g['en1x2g']*(xxkdq95g['dzjq7w']+5)):
   yoyohaz7.qic1l7dy(player)
  self.assertEqual(yoyohaz7.zefqjg02-bq349dxb,xxkdq95g['dzjq7w'])
class s9skdgig(unittest.TestCase):
 def zanouof0(self):
  player=r0tvhhpb()
  d1ieixwc=mfyb8dal('uu3bfx',player.npcxa5s0.centerx+5,player.npcxa5s0.centery)
  d1ieixwc.g11kerpe=0
  f55dmcxx=player.arhnuxor
  d1ieixwc.vvslh9bh(player)
  self.assertTrue(d1ieixwc.o5rlqiob)
  for t1w1ht7p in range(d1ieixwc.arjn2hz2-1):
   d1ieixwc.vvslh9bh(player)
  self.assertEqual(player.arhnuxor,f55dmcxx,'no damage should land before the windup finishes')
  d1ieixwc.vvslh9bh(player)
  self.assertFalse(d1ieixwc.o5rlqiob)
  self.assertLess(player.arhnuxor,f55dmcxx)
class zakoixnt(unittest.TestCase):
 def ywcxz2ei(self):
  """Regression: hidden assassins skip the melee-attack early-return,
        so they used to fall into the chase code with distance == 0."""
  player=r0tvhhpb()
  sv5f1bcp=mfyb8dal('qz09wf',player.npcxa5s0.x,player.npcxa5s0.y)
  sv5f1bcp.nabufwbu='hidden'
  sv5f1bcp.move(player)
 def frhzn4kg(self):
  player=r0tvhhpb()
  sv5f1bcp=mfyb8dal('qz09wf',player.npcxa5s0.centerx,player.npcxa5s0.centery)
  f55dmcxx=player.arhnuxor
  for t1w1ht7p in range(sv5f1bcp.nv23gxj0+sv5f1bcp.nbwye6qv):
   sv5f1bcp.move(player)
  self.assertEqual(player.arhnuxor,f55dmcxx)
  self.assertEqual(sv5f1bcp.nabufwbu,'visible')
 def wyk03o4g(self):
  player=r0tvhhpb()
  sv5f1bcp=mfyb8dal('qz09wf',500,500)
  self.assertEqual(sv5f1bcp.nabufwbu,'hidden')
  self.assertLess(sv5f1bcp.la3kkrzd,255)
class lp0lzjje(unittest.TestCase):
 def z7pwo6cm(self):
  player=r0tvhhpb()
  dzsedfqs=mfyb8dal('ga1arr',player.npcxa5s0.centerx+5,player.npcxa5s0.centery)
  dzsedfqs.arhnuxor=0
  dzsedfqs.move(player)
  nubmxnsz=[dzsedfqs]
  atj9a3y3=[]
  f55dmcxx=player.arhnuxor
  pllkstn3(nubmxnsz,[],[],player,atj9a3y3,[],pq3vli7k)
  self.assertEqual(len(nubmxnsz),0)
  self.assertEqual(len(atj9a3y3),1)
  self.assertLess(player.arhnuxor,f55dmcxx)
 def m3hcws2w(self):
  player=r0tvhhpb()
  xxkdq95g=k1wj0tpa['ga1arr']
  dzsedfqs=mfyb8dal('ga1arr',player.npcxa5s0.centerx+xxkdq95g['nddqhk']+200,player.npcxa5s0.centery)
  dzsedfqs.arhnuxor=0
  dzsedfqs.move(player)
  f55dmcxx=player.arhnuxor
  pllkstn3([dzsedfqs],[],[],player,[],[],pq3vli7k)
  self.assertEqual(player.arhnuxor,f55dmcxx)
class dtx63cfl(unittest.TestCase):
 def wvndfdw7(self):
  """Children must be plain Enemy, not Swarm -- otherwise splitting
        recurses forever."""
  player=r0tvhhpb()
  mwszv83x=mfyb8dal('w9mda9',200,200)
  mwszv83x.arhnuxor=0
  mwszv83x.move(player)
  nubmxnsz=[mwszv83x]
  pllkstn3(nubmxnsz,[],[],player,[],[],pq3vli7k)
  r98s4c3b=k1wj0tpa['w9mda9']['zhbgcj']
  self.assertEqual(len(nubmxnsz),r98s4c3b)
  for vw6m7b5c in nubmxnsz:
   self.assertIs(type(vw6m7b5c),f935a0l7)
   self.assertLess(vw6m7b5c.arhnuxor,k1wj0tpa['w9mda9']['yc1nlc'])
class xd1wjcit(unittest.TestCase):
 def arml29q2(self):
  zorxdtg5=mfyb8dal('r6q37c',100,100)
  v76ub7l8=mfyb8dal('r6q37c',5000,5000)
  uoloeazc=mfyb8dal('wurvqt',105,100)
  nubmxnsz=[zorxdtg5,v76ub7l8,uoloeazc]
  self.assertLess(zorxdtg5.o4dd1vn8(nubmxnsz),v76ub7l8.o4dd1vn8(nubmxnsz))
  self.assertEqual(v76ub7l8.o4dd1vn8(nubmxnsz),1.0)
 def x9h0dxho(self):
  xvzc7d2k=mfyb8dal('wurvqt',100,100)
  ck7n3bfh=mfyb8dal('wurvqt',105,100)
  nubmxnsz=[xvzc7d2k,ck7n3bfh]
  self.assertEqual(xvzc7d2k.o4dd1vn8(nubmxnsz),1.0)
  self.assertEqual(ck7n3bfh.o4dd1vn8(nubmxnsz),1.0)
 def jdqqzrlf(self):
  """Regression: an earlier version used `return 1.0` on hitting self
        mid-loop, which meant protection depended on iteration order."""
  onqyyf9r=mfyb8dal('r6q37c',100,100)
  uoloeazc=mfyb8dal('wurvqt',105,100)
  mfc79m96=onqyyf9r.o4dd1vn8([onqyyf9r,uoloeazc])
  wb7f6fdh=onqyyf9r.o4dd1vn8([uoloeazc,onqyyf9r])
  self.assertEqual(mfc79m96,wb7f6fdh)
  self.assertLess(mfc79m96,1.0)
if __name__=='__main__':
 unittest.main()
