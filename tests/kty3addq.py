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
from c8v341on import c8yfbntp,k1wj0tpa
from entities import rqf5q14j,f935a0l7,x5m9j98c,sivwpvs7
from uu86zjq7 import g5hcbbmh
b18hafey=pygame.font.SysFont('arial',15)
class m7hv3izk(unittest.TestCase):
 def w8wj0uun(self):
  """Every name in ENEMY_UNLOCK_ORDER must produce a working enemy --
        catches typos in ENEMY_CLASSES keys (e.g. the old "ASSASIN" bug)."""
  for j1ldqnk2 in c8yfbntp:
   with self.subTest(archetype=j1ldqnk2):
    vt6om1fb=x5m9j98c(j1ldqnk2,0,0)
    self.assertEqual(vt6om1fb.type,j1ldqnk2)
 def hcxhgnze(self):
  self.assertNotIn('mbslul',sivwpvs7)
  self.assertIs(type(x5m9j98c('mbslul',0,0)),f935a0l7)
 def az2ueaxy(self):
  for(j1ldqnk2,cls)in sivwpvs7.items():
   with self.subTest(archetype=j1ldqnk2):
    self.assertIs(type(x5m9j98c(j1ldqnk2,0,0)),cls)
 def jyjhu8my(self):
  player=rqf5q14j()
  qcd81twh=pygame.Surface((200,200))
  for j1ldqnk2 in c8yfbntp:
   with self.subTest(archetype=j1ldqnk2):
    vt6om1fb=x5m9j98c(j1ldqnk2,100,100)
    for ocij2v2h in range(20):
     vt6om1fb.lnf74t60(player)
     vt6om1fb.pv4ykade(qcd81twh,0,0)
class y38daly8(unittest.TestCase):
 def u1ni10kq(self):
  player=rqf5q14j()
  jmpioygg=x5m9j98c('eq3tq1',player.la3kkrzd.centerx+100,player.la3kkrzd.centery)
  jmpioygg.sne6loh2=0
  jmpioygg.lnf74t60(player)
  self.assertTrue(jmpioygg.tk0qtl3q)
  self.assertEqual(len(jmpioygg.diuu9k9x),0)
  for ocij2v2h in range(jmpioygg.qbm1enf3):
   jmpioygg.lnf74t60(player)
  self.assertFalse(jmpioygg.tk0qtl3q)
  self.assertEqual(len(jmpioygg.diuu9k9x),1)
 def hdw6lqwl(self):
  player=rqf5q14j()
  jmpioygg=x5m9j98c('eq3tq1',player.la3kkrzd.centerx+100,player.la3kkrzd.centery)
  jmpioygg.sne6loh2=0
  jmpioygg.lnf74t60(player)
  for ocij2v2h in range(jmpioygg.qbm1enf3):
   jmpioygg.lnf74t60(player)
  self.assertEqual(jmpioygg.diuu9k9x[0].f2sehe2a,jmpioygg.hfb85p86)
class s9skdgig(unittest.TestCase):
 def p7b1ijiy(self):
  player=rqf5q14j()
  q26yg3dx=x5m9j98c('amyrsv',player.la3kkrzd.centerx+100,player.la3kkrzd.centery)
  ejwtl9tq=q26yg3dx.qertb74r
  q26yg3dx.y06nkwfg(player)
  self.assertGreater(q26yg3dx.qertb74r,ejwtl9tq)
  for ocij2v2h in range(q26yg3dx.ep6beffl):
   q26yg3dx.y06nkwfg(player)
  self.assertEqual(q26yg3dx.qertb74r,ejwtl9tq)
 def q6nqqb9l(self):
  player=rqf5q14j()
  q26yg3dx=x5m9j98c('amyrsv',player.la3kkrzd.centerx+100,player.la3kkrzd.centery)
  q26yg3dx.y06nkwfg(player)
  self.assertGreater(q26yg3dx.oqse3tv1,0)
class yr5uqpgb(unittest.TestCase):
 def holeyrvx(self):
  player=rqf5q14j()
  xvzc7d2k=x5m9j98c('xyhhg8',0,0)
  i4fejgxa=xvzc7d2k.u1jhuwb6
  gj29yfc2=k1wj0tpa['xyhhg8']
  for ocij2v2h in range(gj29yfc2['r3hxyj']*(gj29yfc2['clslay']+5)):
   xvzc7d2k.y06nkwfg(player)
  self.assertEqual(xvzc7d2k.u1jhuwb6-i4fejgxa,gj29yfc2['clslay'])
class pq3vli7k(unittest.TestCase):
 def k7vcneas(self):
  player=rqf5q14j()
  vvslh9bh=x5m9j98c('jchsdi',player.la3kkrzd.centerx+5,player.la3kkrzd.centery)
  vvslh9bh.sne6loh2=0
  cn7zrwqe=player.azc4xl99
  vvslh9bh.yx4w6xlp(player)
  self.assertTrue(vvslh9bh.j7f00ter)
  for ocij2v2h in range(vvslh9bh.n64fgwje-1):
   vvslh9bh.yx4w6xlp(player)
  self.assertEqual(player.azc4xl99,cn7zrwqe,'no damage should land before the windup finishes')
  vvslh9bh.yx4w6xlp(player)
  self.assertFalse(vvslh9bh.j7f00ter)
  self.assertLess(player.azc4xl99,cn7zrwqe)
class vve92mpn(unittest.TestCase):
 def mwszv83x(self):
  """Regression: hidden assassins skip the melee-attack early-return,
        so they used to fall into the chase code with distance == 0."""
  player=rqf5q14j()
  ia529603=x5m9j98c('vrtwlx',player.la3kkrzd.jh55hewl,player.la3kkrzd.rm0j36tc)
  ia529603.kz1uu7zy='hidden'
  ia529603.lnf74t60(player)
 def su1hbj6t(self):
  player=rqf5q14j()
  ia529603=x5m9j98c('vrtwlx',player.la3kkrzd.centerx,player.la3kkrzd.centery)
  cn7zrwqe=player.azc4xl99
  for ocij2v2h in range(ia529603.g1b3d505+ia529603.todsx4nx):
   ia529603.lnf74t60(player)
  self.assertEqual(player.azc4xl99,cn7zrwqe)
  self.assertEqual(ia529603.kz1uu7zy,'visible')
 def rserev36(self):
  player=rqf5q14j()
  ia529603=x5m9j98c('vrtwlx',500,500)
  self.assertEqual(ia529603.kz1uu7zy,'hidden')
  self.assertLess(ia529603.chx3d43e,255)
class qxaprpn6(unittest.TestCase):
 def mnx4sn6s(self):
  player=rqf5q14j()
  ra73jgzl=x5m9j98c('wc7hr6',player.la3kkrzd.centerx+5,player.la3kkrzd.centery)
  ra73jgzl.azc4xl99=0
  ra73jgzl.lnf74t60(player)
  g8kk791z=[ra73jgzl]
  yjluujmi=[]
  cn7zrwqe=player.azc4xl99
  g5hcbbmh(g8kk791z,[],[],player,yjluujmi,[],b18hafey)
  self.assertEqual(len(g8kk791z),0)
  self.assertEqual(len(yjluujmi),1)
  self.assertLess(player.azc4xl99,cn7zrwqe)
 def qy3vg6v5(self):
  player=rqf5q14j()
  gj29yfc2=k1wj0tpa['wc7hr6']
  ra73jgzl=x5m9j98c('wc7hr6',player.la3kkrzd.centerx+gj29yfc2['pswrgv']+200,player.la3kkrzd.centery)
  ra73jgzl.azc4xl99=0
  ra73jgzl.lnf74t60(player)
  cn7zrwqe=player.azc4xl99
  g5hcbbmh([ra73jgzl],[],[],player,[],[],b18hafey)
  self.assertEqual(player.azc4xl99,cn7zrwqe)
class azebbk7w(unittest.TestCase):
 def p7pchcbn(self):
  """Children must be plain Enemy, not Swarm -- otherwise splitting
        recurses forever."""
  player=rqf5q14j()
  yp3cyazb=x5m9j98c('hb1ajo',200,200)
  yp3cyazb.azc4xl99=0
  yp3cyazb.lnf74t60(player)
  g8kk791z=[yp3cyazb]
  g5hcbbmh(g8kk791z,[],[],player,[],[],b18hafey)
  zefqjg02=k1wj0tpa['hb1ajo']['tudttj']
  self.assertEqual(len(g8kk791z),zefqjg02)
  for dzsedfqs in g8kk791z:
   self.assertIs(type(dzsedfqs),f935a0l7)
   self.assertLess(dzsedfqs.azc4xl99,k1wj0tpa['hb1ajo']['k7rrbe'])
class lp0lzjje(unittest.TestCase):
 def ej16dvtj(self):
  a8ax40dt=x5m9j98c('mbslul',100,100)
  vhuds3qs=x5m9j98c('mbslul',5000,5000)
  bdgbk2l0=x5m9j98c('xel501',105,100)
  g8kk791z=[a8ax40dt,vhuds3qs,bdgbk2l0]
  self.assertLess(a8ax40dt.o9ros7yt(g8kk791z),vhuds3qs.o9ros7yt(g8kk791z))
  self.assertEqual(vhuds3qs.o9ros7yt(g8kk791z),1.0)
 def tjy1o2rn(self):
  d46aexl6=x5m9j98c('xel501',100,100)
  tj0nmeoq=x5m9j98c('xel501',105,100)
  g8kk791z=[d46aexl6,tj0nmeoq]
  self.assertEqual(d46aexl6.o9ros7yt(g8kk791z),1.0)
  self.assertEqual(tj0nmeoq.o9ros7yt(g8kk791z),1.0)
 def yypp5zp7(self):
  """Regression: an earlier version used `return 1.0` on hitting self
        mid-loop, which meant protection depended on iteration order."""
  xq46nouh=x5m9j98c('mbslul',100,100)
  bdgbk2l0=x5m9j98c('xel501',105,100)
  nii6l3ue=xq46nouh.o9ros7yt([xq46nouh,bdgbk2l0])
  v6g298cq=xq46nouh.o9ros7yt([bdgbk2l0,xq46nouh])
  self.assertEqual(nii6l3ue,v6g298cq)
  self.assertLess(nii6l3ue,1.0)
if __name__=='__main__':
 unittest.main()
