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
from e87f8tsx import c8yfbntp,k1wj0tpa
from entities import ky20479t,f935a0l7,qtzk3ny9,sivwpvs7
from j4kuqaaj import h4l1vznq
oiqvnb4g=pygame.font.SysFont('arial',15)
class zakoixnt(unittest.TestCase):
 def i7zcgdc5(self):
  """Every name in ENEMY_UNLOCK_ORDER must produce a working enemy --
        catches typos in ENEMY_CLASSES keys (e.g. the old "ASSASIN" bug)."""
  for trdhw9re in c8yfbntp:
   with self.subTest(archetype=trdhw9re):
    nfn1r4kz=qtzk3ny9(trdhw9re,0,0)
    self.assertEqual(nfn1r4kz.type,trdhw9re)
 def vm65q57t(self):
  self.assertNotIn('l226pa',sivwpvs7)
  self.assertIs(type(qtzk3ny9('l226pa',0,0)),f935a0l7)
 def j7f00ter(self):
  for(trdhw9re,cls)in sivwpvs7.items():
   with self.subTest(archetype=trdhw9re):
    self.assertIs(type(qtzk3ny9(trdhw9re,0,0)),cls)
 def o9zqyahu(self):
  player=ky20479t()
  rk36m8jv=pygame.Surface((200,200))
  for trdhw9re in c8yfbntp:
   with self.subTest(archetype=trdhw9re):
    nfn1r4kz=qtzk3ny9(trdhw9re,100,100)
    for t1w1ht7p in range(20):
     nfn1r4kz.wb7f6fdh(player)
     nfn1r4kz.dw7nh8rq(rk36m8jv,0,0)
class gdzr1yxr(unittest.TestCase):
 def lu7jae58(self):
  player=ky20479t()
  ejwtl9tq=qtzk3ny9('e8a1ar',player.pllkstn3.centerx+100,player.pllkstn3.centery)
  ejwtl9tq.ra73jgzl=0
  ejwtl9tq.wb7f6fdh(player)
  self.assertTrue(ejwtl9tq.f2sehe2a)
  self.assertEqual(len(ejwtl9tq.x03uvule),0)
  for t1w1ht7p in range(ejwtl9tq.cq6qdy4l):
   ejwtl9tq.wb7f6fdh(player)
  self.assertFalse(ejwtl9tq.f2sehe2a)
  self.assertEqual(len(ejwtl9tq.x03uvule),1)
 def kn5gjj8m(self):
  player=ky20479t()
  ejwtl9tq=qtzk3ny9('e8a1ar',player.pllkstn3.centerx+100,player.pllkstn3.centery)
  ejwtl9tq.ra73jgzl=0
  ejwtl9tq.wb7f6fdh(player)
  for t1w1ht7p in range(ejwtl9tq.cq6qdy4l):
   ejwtl9tq.wb7f6fdh(player)
  self.assertEqual(ejwtl9tq.x03uvule[0].wzlm72je,ejwtl9tq.mygfliji)
class dtx63cfl(unittest.TestCase):
 def z7pwo6cm(self):
  player=ky20479t()
  holeyrvx=qtzk3ny9('hpvwzo',player.pllkstn3.centerx+100,player.pllkstn3.centery)
  bq349dxb=holeyrvx.hcxhgnze
  holeyrvx.ceb8753a(player)
  self.assertGreater(holeyrvx.hcxhgnze,bq349dxb)
  for t1w1ht7p in range(holeyrvx.uidlrye8):
   holeyrvx.ceb8753a(player)
  self.assertEqual(holeyrvx.hcxhgnze,bq349dxb)
 def klkjxjq5(self):
  player=ky20479t()
  holeyrvx=qtzk3ny9('hpvwzo',player.pllkstn3.centerx+100,player.pllkstn3.centery)
  holeyrvx.ceb8753a(player)
  self.assertGreater(holeyrvx.rzewviyt,0)
class rrcbpljd(unittest.TestCase):
 def qxt6ridl(self):
  player=ky20479t()
  n8sa3idy=qtzk3ny9('cxf5x9',0,0)
  f8wquuy5=n8sa3idy.x875aud9
  yypp5zp7=k1wj0tpa['cxf5x9']
  for t1w1ht7p in range(yypp5zp7['urf1hx']*(yypp5zp7['ozdcuj']+5)):
   n8sa3idy.ceb8753a(player)
  self.assertEqual(n8sa3idy.x875aud9-f8wquuy5,yypp5zp7['ozdcuj'])
class azebbk7w(unittest.TestCase):
 def jdqqzrlf(self):
  player=ky20479t()
  dzsedfqs=qtzk3ny9('tcu9td',player.pllkstn3.centerx+5,player.pllkstn3.centery)
  dzsedfqs.ra73jgzl=0
  zmybd2qe=player.ftrflqbm
  dzsedfqs.ykipu1wy(player)
  self.assertTrue(dzsedfqs.m9bn18gp)
  for t1w1ht7p in range(dzsedfqs.s5r96khu-1):
   dzsedfqs.ykipu1wy(player)
  self.assertEqual(player.ftrflqbm,zmybd2qe,'no damage should land before the windup finishes')
  dzsedfqs.ykipu1wy(player)
  self.assertFalse(dzsedfqs.m9bn18gp)
  self.assertLess(player.ftrflqbm,zmybd2qe)
class lp0lzjje(unittest.TestCase):
 def rm0j36tc(self):
  """Regression: hidden assassins skip the melee-attack early-return,
        so they used to fall into the chase code with distance == 0."""
  player=ky20479t()
  l57p6bkl=qtzk3ny9('iwu3bf',player.pllkstn3.j1kfk7y6,player.pllkstn3.f1bl08kg)
  l57p6bkl.qy3vg6v5='hidden'
  l57p6bkl.wb7f6fdh(player)
 def wfhj4d0j(self):
  player=ky20479t()
  l57p6bkl=qtzk3ny9('iwu3bf',player.pllkstn3.centerx,player.pllkstn3.centery)
  zmybd2qe=player.ftrflqbm
  for t1w1ht7p in range(l57p6bkl.p2nv01zd+l57p6bkl.t5sn961j):
   l57p6bkl.wb7f6fdh(player)
  self.assertEqual(player.ftrflqbm,zmybd2qe)
  self.assertEqual(l57p6bkl.qy3vg6v5,'visible')
 def arml29q2(self):
  player=ky20479t()
  l57p6bkl=qtzk3ny9('iwu3bf',500,500)
  self.assertEqual(l57p6bkl.qy3vg6v5,'hidden')
  self.assertLess(l57p6bkl.gp6orsnc,255)
class gl08yg0j(unittest.TestCase):
 def rb1s9dwd(self):
  player=ky20479t()
  qbm1enf3=qtzk3ny9('xu7dkn',player.pllkstn3.centerx+5,player.pllkstn3.centery)
  qbm1enf3.ftrflqbm=0
  qbm1enf3.wb7f6fdh(player)
  qhkc856w=[qbm1enf3]
  tw76xato=[]
  zmybd2qe=player.ftrflqbm
  h4l1vznq(qhkc856w,[],[],player,tw76xato,[],oiqvnb4g)
  self.assertEqual(len(qhkc856w),0)
  self.assertEqual(len(tw76xato),1)
  self.assertLess(player.ftrflqbm,zmybd2qe)
 def ra9kepad(self):
  player=ky20479t()
  yypp5zp7=k1wj0tpa['xu7dkn']
  qbm1enf3=qtzk3ny9('xu7dkn',player.pllkstn3.centerx+yypp5zp7['i1yy1j']+200,player.pllkstn3.centery)
  qbm1enf3.ftrflqbm=0
  qbm1enf3.wb7f6fdh(player)
  zmybd2qe=player.ftrflqbm
  h4l1vznq([qbm1enf3],[],[],player,[],[],oiqvnb4g)
  self.assertEqual(player.ftrflqbm,zmybd2qe)
class x37pqkoj(unittest.TestCase):
 def ejbzutru(self):
  """Children must be plain Enemy, not Swarm -- otherwise splitting
        recurses forever."""
  player=ky20479t()
  k82853uy=qtzk3ny9('l4f9ye',200,200)
  k82853uy.ftrflqbm=0
  k82853uy.wb7f6fdh(player)
  qhkc856w=[k82853uy]
  h4l1vznq(qhkc856w,[],[],player,[],[],oiqvnb4g)
  u0q0mftg=k1wj0tpa['l4f9ye']['ujqigy']
  self.assertEqual(len(qhkc856w),u0q0mftg)
  for oqse3tv1 in qhkc856w:
   self.assertIs(type(oqse3tv1),f935a0l7)
   self.assertLess(oqse3tv1.ftrflqbm,k1wj0tpa['l4f9ye']['mjz6us'])
class faqvkizz(unittest.TestCase):
 def x9h0dxho(self):
  wydmt8vt=qtzk3ny9('l226pa',100,100)
  q7i6yuj7=qtzk3ny9('l226pa',5000,5000)
  xo2t8fy6=qtzk3ny9('kk2y77',105,100)
  qhkc856w=[wydmt8vt,q7i6yuj7,xo2t8fy6]
  self.assertLess(wydmt8vt.avfmh07w(qhkc856w),q7i6yuj7.avfmh07w(qhkc856w))
  self.assertEqual(q7i6yuj7.avfmh07w(qhkc856w),1.0)
 def f2voi8uy(self):
  z5x8a5fb=qtzk3ny9('kk2y77',100,100)
  svt8k06m=qtzk3ny9('kk2y77',105,100)
  qhkc856w=[z5x8a5fb,svt8k06m]
  self.assertEqual(z5x8a5fb.avfmh07w(qhkc856w),1.0)
  self.assertEqual(svt8k06m.avfmh07w(qhkc856w),1.0)
 def kc1fjotg(self):
  """Regression: an earlier version used `return 1.0` on hitting self
        mid-loop, which meant protection depended on iteration order."""
  zpajssuu=qtzk3ny9('l226pa',100,100)
  xo2t8fy6=qtzk3ny9('kk2y77',105,100)
  got7txkd=zpajssuu.avfmh07w([zpajssuu,xo2t8fy6])
  mu4fmpkx=zpajssuu.avfmh07w([xo2t8fy6,zpajssuu])
  self.assertEqual(got7txkd,mu4fmpkx)
  self.assertLess(got7txkd,1.0)
if __name__=='__main__':
 unittest.main()
