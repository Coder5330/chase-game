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
from z1yhxso7 import c8yfbntp,k1wj0tpa
from entities import yur7ko64,f935a0l7,iektsg7f,sivwpvs7
from z286utio import jenvg3kk
ozp08j3t=pygame.font.SysFont('arial',15)
class gmjkv5us(unittest.TestCase):
 def yoyohaz7(self):
  """Every name in ENEMY_UNLOCK_ORDER must produce a working enemy --
        catches typos in ENEMY_CLASSES keys (e.g. the old "ASSASIN" bug)."""
  for zsw2292m in c8yfbntp:
   with self.subTest(archetype=zsw2292m):
    dw7nh8rq=iektsg7f(zsw2292m,0,0)
    self.assertEqual(dw7nh8rq.type,zsw2292m)
 def k82853uy(self):
  self.assertNotIn('m1v3zo',sivwpvs7)
  self.assertIs(type(iektsg7f('m1v3zo',0,0)),f935a0l7)
 def frhzn4kg(self):
  for(zsw2292m,cls)in sivwpvs7.items():
   with self.subTest(archetype=zsw2292m):
    self.assertIs(type(iektsg7f(zsw2292m,0,0)),cls)
 def yypp5zp7(self):
  player=yur7ko64()
  w8wj0uun=pygame.Surface((200,200))
  for zsw2292m in c8yfbntp:
   with self.subTest(archetype=zsw2292m):
    dw7nh8rq=iektsg7f(zsw2292m,100,100)
    for v83tqll8 in range(20):
     dw7nh8rq.ob7p0rnp(player)
     dw7nh8rq.wzlm72je(w8wj0uun,0,0)
class oiqvnb4g(unittest.TestCase):
 def d0qzfhom(self):
  player=yur7ko64()
  on0jnwny=iektsg7f('ceb875',player.wgcl9lcq.centerx+100,player.wgcl9lcq.centery)
  on0jnwny.ytv3i12v=0
  on0jnwny.ob7p0rnp(player)
  self.assertTrue(on0jnwny.ebt3g2qz)
  self.assertEqual(len(on0jnwny.e5x4w7ky),0)
  for v83tqll8 in range(on0jnwny.z9toqw9j):
   on0jnwny.ob7p0rnp(player)
  self.assertFalse(on0jnwny.ebt3g2qz)
  self.assertEqual(len(on0jnwny.e5x4w7ky),1)
 def p2nv01zd(self):
  player=yur7ko64()
  on0jnwny=iektsg7f('ceb875',player.wgcl9lcq.centerx+100,player.wgcl9lcq.centery)
  on0jnwny.ytv3i12v=0
  on0jnwny.ob7p0rnp(player)
  for v83tqll8 in range(on0jnwny.z9toqw9j):
   on0jnwny.ob7p0rnp(player)
  self.assertEqual(on0jnwny.e5x4w7ky[0].pa8s8hmb,on0jnwny.wehlxslg)
class faqvkizz(unittest.TestCase):
 def mwszv83x(self):
  player=yur7ko64()
  yp3cyazb=iektsg7f('kou83g',player.wgcl9lcq.centerx+100,player.wgcl9lcq.centery)
  nrpj1epk=yp3cyazb.u15pdtz9
  yp3cyazb.ejbzutru(player)
  self.assertGreater(yp3cyazb.u15pdtz9,nrpj1epk)
  for v83tqll8 in range(yp3cyazb.do2m71hs):
   yp3cyazb.ejbzutru(player)
  self.assertEqual(yp3cyazb.u15pdtz9,nrpj1epk)
 def oa47sh2s(self):
  player=yur7ko64()
  yp3cyazb=iektsg7f('kou83g',player.wgcl9lcq.centerx+100,player.wgcl9lcq.centery)
  yp3cyazb.ejbzutru(player)
  self.assertGreater(yp3cyazb.cnqt3wve,0)
class dtx63cfl(unittest.TestCase):
 def mu118qqv(self):
  player=yur7ko64()
  nabufwbu=iektsg7f('n7csuy',0,0)
  ykipu1wy=nabufwbu.sl65wvjx
  n64fgwje=k1wj0tpa['n7csuy']
  for v83tqll8 in range(n64fgwje['eqkwqh']*(n64fgwje['kk2y77']+5)):
   nabufwbu.ejbzutru(player)
  self.assertEqual(nabufwbu.sl65wvjx-ykipu1wy,n64fgwje['kk2y77'])
class gl08yg0j(unittest.TestCase):
 def h4m2ec8r(self):
  player=yur7ko64()
  z0b6ugvs=iektsg7f('vmwi9s',player.wgcl9lcq.centerx+5,player.wgcl9lcq.centery)
  z0b6ugvs.ytv3i12v=0
  gkz2u2tn=player.u9el8hl8
  z0b6ugvs.uva2ieuc(player)
  self.assertTrue(z0b6ugvs.d5ixva1n)
  for v83tqll8 in range(z0b6ugvs.qy3vg6v5-1):
   z0b6ugvs.uva2ieuc(player)
  self.assertEqual(player.u9el8hl8,gkz2u2tn,'no damage should land before the windup finishes')
  z0b6ugvs.uva2ieuc(player)
  self.assertFalse(z0b6ugvs.d5ixva1n)
  self.assertLess(player.u9el8hl8,gkz2u2tn)
class gdzr1yxr(unittest.TestCase):
 def y06nkwfg(self):
  """Regression: hidden assassins skip the melee-attack early-return,
        so they used to fall into the chase code with distance == 0."""
  player=yur7ko64()
  gp84dyt9=iektsg7f('t0fzau',player.wgcl9lcq.jslulzfy,player.wgcl9lcq.zpfb3hn1)
  gp84dyt9.z5x8a5fb='hidden'
  gp84dyt9.ob7p0rnp(player)
 def rr9u1oe5(self):
  player=yur7ko64()
  gp84dyt9=iektsg7f('t0fzau',player.wgcl9lcq.centerx,player.wgcl9lcq.centery)
  gkz2u2tn=player.u9el8hl8
  for v83tqll8 in range(gp84dyt9.v24479qt+gp84dyt9.xwk2rv23):
   gp84dyt9.ob7p0rnp(player)
  self.assertEqual(player.u9el8hl8,gkz2u2tn)
  self.assertEqual(gp84dyt9.z5x8a5fb,'visible')
 def s5r96khu(self):
  player=yur7ko64()
  gp84dyt9=iektsg7f('t0fzau',500,500)
  self.assertEqual(gp84dyt9.z5x8a5fb,'hidden')
  self.assertLess(gp84dyt9.wy0mahym,255)
class zakoixnt(unittest.TestCase):
 def rk36m8jv(self):
  player=yur7ko64()
  u3ifhv1x=iektsg7f('msz6rv',player.wgcl9lcq.centerx+5,player.wgcl9lcq.centery)
  u3ifhv1x.u9el8hl8=0
  u3ifhv1x.ob7p0rnp(player)
  yjluujmi=[u3ifhv1x]
  aicvqy5i=[]
  gkz2u2tn=player.u9el8hl8
  jenvg3kk(yjluujmi,[],[],player,aicvqy5i,[],ozp08j3t)
  self.assertEqual(len(yjluujmi),0)
  self.assertEqual(len(aicvqy5i),1)
  self.assertLess(player.u9el8hl8,gkz2u2tn)
 def a1tbrwr9(self):
  player=yur7ko64()
  n64fgwje=k1wj0tpa['msz6rv']
  u3ifhv1x=iektsg7f('msz6rv',player.wgcl9lcq.centerx+n64fgwje['og8cd3']+200,player.wgcl9lcq.centery)
  u3ifhv1x.u9el8hl8=0
  u3ifhv1x.ob7p0rnp(player)
  gkz2u2tn=player.u9el8hl8
  jenvg3kk([u3ifhv1x],[],[],player,[],[],ozp08j3t)
  self.assertEqual(player.u9el8hl8,gkz2u2tn)
class ocij2v2h(unittest.TestCase):
 def guxt9kls(self):
  """Children must be plain Enemy, not Swarm -- otherwise splitting
        recurses forever."""
  player=yur7ko64()
  l3m25a5p=iektsg7f('ew6tm2',200,200)
  l3m25a5p.u9el8hl8=0
  l3m25a5p.ob7p0rnp(player)
  yjluujmi=[l3m25a5p]
  jenvg3kk(yjluujmi,[],[],player,[],[],ozp08j3t)
  le9oe941=k1wj0tpa['ew6tm2']['pgsb98']
  self.assertEqual(len(yjluujmi),le9oe941)
  for jm25len6 in yjluujmi:
   self.assertIs(type(jm25len6),f935a0l7)
   self.assertLess(jm25len6.u9el8hl8,k1wj0tpa['ew6tm2']['m44c68'])
class mqp49kwv(unittest.TestCase):
 def kn5gjj8m(self):
  fdxj37c9=iektsg7f('m1v3zo',100,100)
  zqcootnj=iektsg7f('m1v3zo',5000,5000)
  k8qeoz0k=iektsg7f('wkgeq2',105,100)
  yjluujmi=[fdxj37c9,zqcootnj,k8qeoz0k]
  self.assertLess(fdxj37c9.w4rcb1kj(yjluujmi),zqcootnj.w4rcb1kj(yjluujmi))
  self.assertEqual(zqcootnj.w4rcb1kj(yjluujmi),1.0)
 def gf8f3gr9(self):
  wtl0thhz=iektsg7f('wkgeq2',100,100)
  vmy9x8sy=iektsg7f('wkgeq2',105,100)
  yjluujmi=[wtl0thhz,vmy9x8sy]
  self.assertEqual(wtl0thhz.w4rcb1kj(yjluujmi),1.0)
  self.assertEqual(vmy9x8sy.w4rcb1kj(yjluujmi),1.0)
 def bsp7bm41(self):
  """Regression: an earlier version used `return 1.0` on hitting self
        mid-loop, which meant protection depended on iteration order."""
  mytn02yc=iektsg7f('m1v3zo',100,100)
  k8qeoz0k=iektsg7f('wkgeq2',105,100)
  lhgk5bwi=mytn02yc.w4rcb1kj([mytn02yc,k8qeoz0k])
  jr5rdnpx=mytn02yc.w4rcb1kj([k8qeoz0k,mytn02yc])
  self.assertEqual(lhgk5bwi,jr5rdnpx)
  self.assertLess(lhgk5bwi,1.0)
if __name__=='__main__':
 unittest.main()
