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
from ykatqyds import c8yfbntp,k1wj0tpa
from entities import ky20479t,f935a0l7,yuibrsz1,sivwpvs7
from ifcl5efj import wd6r30oj
oiqvnb4g=pygame.font.SysFont('arial',15)
class zakoixnt(unittest.TestCase):
 def vm65q57t(self):
  """Every name in ENEMY_UNLOCK_ORDER must produce a working enemy --
        catches typos in ENEMY_CLASSES keys (e.g. the old "ASSASIN" bug)."""
  for lgbpj4uf in c8yfbntp:
   with self.subTest(archetype=lgbpj4uf):
    kx74d0gj=yuibrsz1(lgbpj4uf,0,0)
    self.assertEqual(kx74d0gj.type,lgbpj4uf)
 def njka34mq(self):
  self.assertNotIn('s1whhk',sivwpvs7)
  self.assertIs(type(yuibrsz1('s1whhk',0,0)),f935a0l7)
 def wvndfdw7(self):
  for(lgbpj4uf,cls)in sivwpvs7.items():
   with self.subTest(archetype=lgbpj4uf):
    self.assertIs(type(yuibrsz1(lgbpj4uf,0,0)),cls)
 def e9y3z2t4(self):
  player=ky20479t()
  mu118qqv=pygame.Surface((200,200))
  for lgbpj4uf in c8yfbntp:
   with self.subTest(archetype=lgbpj4uf):
    kx74d0gj=yuibrsz1(lgbpj4uf,100,100)
    for wrbw2zla in range(20):
     kx74d0gj.mu4fmpkx(player)
     kx74d0gj.v15cqzcu(mu118qqv,0,0)
class gdzr1yxr(unittest.TestCase):
 def z7pwo6cm(self):
  player=ky20479t()
  tp2ex5t5=yuibrsz1('n9fkxz',player.uaobt328.centerx+100,player.uaobt328.centery)
  tp2ex5t5.kmgfxc08=0
  tp2ex5t5.mu4fmpkx(player)
  self.assertTrue(tp2ex5t5.ruq9e5co)
  self.assertEqual(len(tp2ex5t5.l57p6bkl),0)
  for wrbw2zla in range(tp2ex5t5.lztkkfzz):
   tp2ex5t5.mu4fmpkx(player)
  self.assertFalse(tp2ex5t5.ruq9e5co)
  self.assertEqual(len(tp2ex5t5.l57p6bkl),1)
 def gf8f3gr9(self):
  player=ky20479t()
  tp2ex5t5=yuibrsz1('n9fkxz',player.uaobt328.centerx+100,player.uaobt328.centery)
  tp2ex5t5.kmgfxc08=0
  tp2ex5t5.mu4fmpkx(player)
  for wrbw2zla in range(tp2ex5t5.lztkkfzz):
   tp2ex5t5.mu4fmpkx(player)
  self.assertEqual(tp2ex5t5.l57p6bkl[0].wc7x0h3j,tp2ex5t5.velos6zl)
class dtx63cfl(unittest.TestCase):
 def i7zcgdc5(self):
  player=ky20479t()
  xxkdq95g=yuibrsz1('mmgvu4',player.uaobt328.centerx+100,player.uaobt328.centery)
  wppsfnko=xxkdq95g.bf7so8w5
  xxkdq95g.acxx6mdk(player)
  self.assertGreater(xxkdq95g.bf7so8w5,wppsfnko)
  for wrbw2zla in range(xxkdq95g.uc1xi04b):
   xxkdq95g.acxx6mdk(player)
  self.assertEqual(xxkdq95g.bf7so8w5,wppsfnko)
 def rb1s9dwd(self):
  player=ky20479t()
  xxkdq95g=yuibrsz1('mmgvu4',player.uaobt328.centerx+100,player.uaobt328.centery)
  xxkdq95g.acxx6mdk(player)
  self.assertGreater(xxkdq95g.fo75rh8l,0)
class rrcbpljd(unittest.TestCase):
 def zanouof0(self):
  player=ky20479t()
  h4m2ec8r=yuibrsz1('e0s41k',0,0)
  uww5wfcp=h4m2ec8r.zefqjg02
  az2ueaxy=k1wj0tpa['e0s41k']
  for wrbw2zla in range(az2ueaxy['r7myow']*(az2ueaxy['udt8cq']+5)):
   h4m2ec8r.acxx6mdk(player)
  self.assertEqual(h4m2ec8r.zefqjg02-uww5wfcp,az2ueaxy['udt8cq'])
class azebbk7w(unittest.TestCase):
 def kc1fjotg(self):
  player=ky20479t()
  nd6357oo=yuibrsz1('nomuwa',player.uaobt328.centerx+5,player.uaobt328.centery)
  nd6357oo.kmgfxc08=0
  f55dmcxx=player.w4rcb1kj
  nd6357oo.ra73jgzl(player)
  self.assertTrue(nd6357oo.cjy62zee)
  for wrbw2zla in range(nd6357oo.kn5gjj8m-1):
   nd6357oo.ra73jgzl(player)
  self.assertEqual(player.w4rcb1kj,f55dmcxx,'no damage should land before the windup finishes')
  nd6357oo.ra73jgzl(player)
  self.assertFalse(nd6357oo.cjy62zee)
  self.assertLess(player.w4rcb1kj,f55dmcxx)
class lp0lzjje(unittest.TestCase):
 def gsrtwlxd(self):
  """Regression: hidden assassins skip the melee-attack early-return,
        so they used to fall into the chase code with distance == 0."""
  player=ky20479t()
  duhxid4n=yuibrsz1('rcqe4l',player.uaobt328.owdz09wf,player.uaobt328.lb4y4k7b)
  duhxid4n.p2nv01zd='hidden'
  duhxid4n.mu4fmpkx(player)
 def y06nkwfg(self):
  player=ky20479t()
  duhxid4n=yuibrsz1('rcqe4l',player.uaobt328.centerx,player.uaobt328.centery)
  f55dmcxx=player.w4rcb1kj
  for wrbw2zla in range(duhxid4n.kodpvjtu+duhxid4n.vmy9x8sy):
   duhxid4n.mu4fmpkx(player)
  self.assertEqual(player.w4rcb1kj,f55dmcxx)
  self.assertEqual(duhxid4n.p2nv01zd,'visible')
 def x9h0dxho(self):
  player=ky20479t()
  duhxid4n=yuibrsz1('rcqe4l',500,500)
  self.assertEqual(duhxid4n.p2nv01zd,'hidden')
  self.assertLess(duhxid4n.g5hcbbmh,255)
class gl08yg0j(unittest.TestCase):
 def e8zgvwwu(self):
  player=ky20479t()
  yw6zbnz8=yuibrsz1('l7wr0r',player.uaobt328.centerx+5,player.uaobt328.centery)
  yw6zbnz8.w4rcb1kj=0
  yw6zbnz8.mu4fmpkx(player)
  nfn1r4kz=[yw6zbnz8]
  fddfgs3j=[]
  f55dmcxx=player.w4rcb1kj
  wd6r30oj(nfn1r4kz,[],[],player,fddfgs3j,[],oiqvnb4g)
  self.assertEqual(len(nfn1r4kz),0)
  self.assertEqual(len(fddfgs3j),1)
  self.assertLess(player.w4rcb1kj,f55dmcxx)
 def i33e1i1p(self):
  player=ky20479t()
  az2ueaxy=k1wj0tpa['l7wr0r']
  yw6zbnz8=yuibrsz1('l7wr0r',player.uaobt328.centerx+az2ueaxy['mjz6us']+200,player.uaobt328.centery)
  yw6zbnz8.w4rcb1kj=0
  yw6zbnz8.mu4fmpkx(player)
  f55dmcxx=player.w4rcb1kj
  wd6r30oj([yw6zbnz8],[],[],player,[],[],oiqvnb4g)
  self.assertEqual(player.w4rcb1kj,f55dmcxx)
class x37pqkoj(unittest.TestCase):
 def awnwlc83(self):
  """Children must be plain Enemy, not Swarm -- otherwise splitting
        recurses forever."""
  player=ky20479t()
  n8sa3idy=yuibrsz1('buzery',200,200)
  n8sa3idy.w4rcb1kj=0
  n8sa3idy.mu4fmpkx(player)
  nfn1r4kz=[n8sa3idy]
  wd6r30oj(nfn1r4kz,[],[],player,[],[],oiqvnb4g)
  ao4izasn=k1wj0tpa['buzery']['gpm21b']
  self.assertEqual(len(nfn1r4kz),ao4izasn)
  for ep6beffl in nfn1r4kz:
   self.assertIs(type(ep6beffl),f935a0l7)
   self.assertLess(ep6beffl.w4rcb1kj,k1wj0tpa['buzery']['jz6wmd'])
class faqvkizz(unittest.TestCase):
 def f2voi8uy(self):
  co4busu9=yuibrsz1('s1whhk',100,100)
  sf337kuu=yuibrsz1('s1whhk',5000,5000)
  n64fgwje=yuibrsz1('l4f9ye',105,100)
  nfn1r4kz=[co4busu9,sf337kuu,n64fgwje]
  self.assertLess(co4busu9.k2ixivzk(nfn1r4kz),sf337kuu.k2ixivzk(nfn1r4kz))
  self.assertEqual(sf337kuu.k2ixivzk(nfn1r4kz),1.0)
 def r212pgym(self):
  v24479qt=yuibrsz1('l4f9ye',100,100)
  jyjhu8my=yuibrsz1('l4f9ye',105,100)
  nfn1r4kz=[v24479qt,jyjhu8my]
  self.assertEqual(v24479qt.k2ixivzk(nfn1r4kz),1.0)
  self.assertEqual(jyjhu8my.k2ixivzk(nfn1r4kz),1.0)
 def j7f00ter(self):
  """Regression: an earlier version used `return 1.0` on hitting self
        mid-loop, which meant protection depended on iteration order."""
  jo8e7flq=yuibrsz1('s1whhk',100,100)
  n64fgwje=yuibrsz1('l4f9ye',105,100)
  trdhw9re=jo8e7flq.k2ixivzk([jo8e7flq,n64fgwje])
  zorxdtg5=jo8e7flq.k2ixivzk([n64fgwje,jo8e7flq])
  self.assertEqual(trdhw9re,zorxdtg5)
  self.assertLess(trdhw9re,1.0)
if __name__=='__main__':
 unittest.main()
