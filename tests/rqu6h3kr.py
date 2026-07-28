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
from omerbyea import c8yfbntp,k1wj0tpa
from entities import ky20479t,f935a0l7,sl65wvjx,sivwpvs7
from hb1r8vnr import d1hm38ks
oiqvnb4g=pygame.font.SysFont('arial',15)
class zakoixnt(unittest.TestCase):
 def rb1s9dwd(self):
  """Every name in ENEMY_UNLOCK_ORDER must produce a working enemy --
        catches typos in ENEMY_CLASSES keys (e.g. the old "ASSASIN" bug)."""
  for zorxdtg5 in c8yfbntp:
   with self.subTest(archetype=zorxdtg5):
    zqcootnj=sl65wvjx(zorxdtg5,0,0)
    self.assertEqual(zqcootnj.type,zorxdtg5)
 def e8zgvwwu(self):
  self.assertNotIn('v9hbn5',sivwpvs7)
  self.assertIs(type(sl65wvjx('v9hbn5',0,0)),f935a0l7)
 def jh55hewl(self):
  for(zorxdtg5,cls)in sivwpvs7.items():
   with self.subTest(archetype=zorxdtg5):
    self.assertIs(type(sl65wvjx(zorxdtg5,0,0)),cls)
 def kn5gjj8m(self):
  player=ky20479t()
  gqoagsus=pygame.Surface((200,200))
  for zorxdtg5 in c8yfbntp:
   with self.subTest(archetype=zorxdtg5):
    zqcootnj=sl65wvjx(zorxdtg5,100,100)
    for wrbw2zla in range(20):
     zqcootnj.got7txkd(player)
     zqcootnj.tnz61231(gqoagsus,0,0)
class gdzr1yxr(unittest.TestCase):
 def guxt9kls(self):
  player=ky20479t()
  tp2ex5t5=sl65wvjx('h5kw3h',player.cq2q4qer.centerx+100,player.cq2q4qer.centery)
  tp2ex5t5.kmgfxc08=0
  tp2ex5t5.got7txkd(player)
  self.assertTrue(tp2ex5t5.ruq9e5co)
  self.assertEqual(len(tp2ex5t5.l57p6bkl),0)
  for wrbw2zla in range(tp2ex5t5.lztkkfzz):
   tp2ex5t5.got7txkd(player)
  self.assertFalse(tp2ex5t5.ruq9e5co)
  self.assertEqual(len(tp2ex5t5.l57p6bkl),1)
 def frhzn4kg(self):
  player=ky20479t()
  tp2ex5t5=sl65wvjx('h5kw3h',player.cq2q4qer.centerx+100,player.cq2q4qer.centery)
  tp2ex5t5.kmgfxc08=0
  tp2ex5t5.got7txkd(player)
  for wrbw2zla in range(tp2ex5t5.lztkkfzz):
   tp2ex5t5.got7txkd(player)
  self.assertEqual(tp2ex5t5.l57p6bkl[0].vt6om1fb,tp2ex5t5.yjluujmi)
class dtx63cfl(unittest.TestCase):
 def klkjxjq5(self):
  player=ky20479t()
  nabufwbu=sl65wvjx('cxf5x9',player.cq2q4qer.centerx+100,player.cq2q4qer.centery)
  wppsfnko=nabufwbu.holeyrvx
  nabufwbu.yjr0fzau(player)
  self.assertGreater(nabufwbu.holeyrvx,wppsfnko)
  for wrbw2zla in range(nabufwbu.fo75rh8l):
   nabufwbu.yjr0fzau(player)
  self.assertEqual(nabufwbu.holeyrvx,wppsfnko)
 def l0sqg4ei(self):
  player=ky20479t()
  nabufwbu=sl65wvjx('cxf5x9',player.cq2q4qer.centerx+100,player.cq2q4qer.centery)
  nabufwbu.yjr0fzau(player)
  self.assertGreater(nabufwbu.uidlrye8,0)
class rrcbpljd(unittest.TestCase):
 def njka34mq(self):
  player=ky20479t()
  kc7rm6j8=sl65wvjx('mmgvu4',0,0)
  uww5wfcp=kc7rm6j8.jqxs6esj
  p2nv01zd=k1wj0tpa['mmgvu4']
  for wrbw2zla in range(p2nv01zd['mjz6us']*(p2nv01zd['yrp422']+5)):
   kc7rm6j8.yjr0fzau(player)
  self.assertEqual(kc7rm6j8.jqxs6esj-uww5wfcp,p2nv01zd['yrp422'])
class azebbk7w(unittest.TestCase):
 def ra9kepad(self):
  player=ky20479t()
  nd6357oo=sl65wvjx('pswrgv',player.cq2q4qer.centerx+5,player.cq2q4qer.centery)
  nd6357oo.kmgfxc08=0
  fpa8hyex=player.arhnuxor
  nd6357oo.ra73jgzl(player)
  self.assertTrue(nd6357oo.o3q0e27z)
  for wrbw2zla in range(nd6357oo.bsp7bm41-1):
   nd6357oo.ra73jgzl(player)
  self.assertEqual(player.arhnuxor,fpa8hyex,'no damage should land before the windup finishes')
  nd6357oo.ra73jgzl(player)
  self.assertFalse(nd6357oo.o3q0e27z)
  self.assertLess(player.arhnuxor,fpa8hyex)
class lp0lzjje(unittest.TestCase):
 def eq3tq1s0(self):
  """Regression: hidden assassins skip the melee-attack early-return,
        so they used to fall into the chase code with distance == 0."""
  player=ky20479t()
  duhxid4n=sl65wvjx('vkxzuu',player.cq2q4qer.eolaq665,player.cq2q4qer.t5ivrocv)
  duhxid4n.rserev36='hidden'
  duhxid4n.got7txkd(player)
 def lu7jae58(self):
  player=ky20479t()
  duhxid4n=sl65wvjx('vkxzuu',player.cq2q4qer.centerx,player.cq2q4qer.centery)
  fpa8hyex=player.arhnuxor
  for wrbw2zla in range(duhxid4n.ej16dvtj+duhxid4n.k8qeoz0k):
   duhxid4n.got7txkd(player)
  self.assertEqual(player.arhnuxor,fpa8hyex)
  self.assertEqual(duhxid4n.rserev36,'visible')
 def kc1fjotg(self):
  player=ky20479t()
  duhxid4n=sl65wvjx('vkxzuu',500,500)
  self.assertEqual(duhxid4n.rserev36,'hidden')
  self.assertLess(duhxid4n.zflse45b,255)
class gl08yg0j(unittest.TestCase):
 def mlikwe4b(self):
  player=ky20479t()
  yw6zbnz8=sl65wvjx('tcu9td',player.cq2q4qer.centerx+5,player.cq2q4qer.centery)
  yw6zbnz8.arhnuxor=0
  yw6zbnz8.got7txkd(player)
  nubmxnsz=[yw6zbnz8]
  atj9a3y3=[]
  fpa8hyex=player.arhnuxor
  d1hm38ks(nubmxnsz,[],[],player,atj9a3y3,[],oiqvnb4g)
  self.assertEqual(len(nubmxnsz),0)
  self.assertEqual(len(atj9a3y3),1)
  self.assertLess(player.arhnuxor,fpa8hyex)
 def arml29q2(self):
  player=ky20479t()
  p2nv01zd=k1wj0tpa['tcu9td']
  yw6zbnz8=sl65wvjx('tcu9td',player.cq2q4qer.centerx+p2nv01zd['urf1hx']+200,player.cq2q4qer.centery)
  yw6zbnz8.arhnuxor=0
  yw6zbnz8.got7txkd(player)
  fpa8hyex=player.arhnuxor
  d1hm38ks([yw6zbnz8],[],[],player,[],[],oiqvnb4g)
  self.assertEqual(player.arhnuxor,fpa8hyex)
class x37pqkoj(unittest.TestCase):
 def rm0j36tc(self):
  """Children must be plain Enemy, not Swarm -- otherwise splitting
        recurses forever."""
  player=ky20479t()
  mu118qqv=sl65wvjx('t7wqp3',200,200)
  mu118qqv.arhnuxor=0
  mu118qqv.got7txkd(player)
  nubmxnsz=[mu118qqv]
  d1hm38ks(nubmxnsz,[],[],player,[],[],oiqvnb4g)
  r98s4c3b=k1wj0tpa['t7wqp3']['tn1th1']
  self.assertEqual(len(nubmxnsz),r98s4c3b)
  for ep6beffl in nubmxnsz:
   self.assertIs(type(ep6beffl),f935a0l7)
   self.assertLess(ep6beffl.arhnuxor,k1wj0tpa['t7wqp3']['r7myow'])
class faqvkizz(unittest.TestCase):
 def j7f00ter(self):
  m3pt5r5r=sl65wvjx('v9hbn5',100,100)
  v76ub7l8=sl65wvjx('v9hbn5',5000,5000)
  z5x8a5fb=sl65wvjx('az3m55',105,100)
  nubmxnsz=[m3pt5r5r,v76ub7l8,z5x8a5fb]
  self.assertLess(m3pt5r5r.o4dd1vn8(nubmxnsz),v76ub7l8.o4dd1vn8(nubmxnsz))
  self.assertEqual(v76ub7l8.o4dd1vn8(nubmxnsz),1.0)
 def wvndfdw7(self):
  svt8k06m=sl65wvjx('az3m55',100,100)
  n64fgwje=sl65wvjx('az3m55',105,100)
  nubmxnsz=[svt8k06m,n64fgwje]
  self.assertEqual(svt8k06m.o4dd1vn8(nubmxnsz),1.0)
  self.assertEqual(n64fgwje.o4dd1vn8(nubmxnsz),1.0)
 def i33e1i1p(self):
  """Regression: an earlier version used `return 1.0` on hitting self
        mid-loop, which meant protection depended on iteration order."""
  onqyyf9r=sl65wvjx('v9hbn5',100,100)
  z5x8a5fb=sl65wvjx('az3m55',105,100)
  mu4fmpkx=onqyyf9r.o4dd1vn8([onqyyf9r,z5x8a5fb])
  trdhw9re=onqyyf9r.o4dd1vn8([z5x8a5fb,onqyyf9r])
  self.assertEqual(mu4fmpkx,trdhw9re)
  self.assertLess(mu4fmpkx,1.0)
if __name__=='__main__':
 unittest.main()
