import os
import sys
import pathlib
import unittest
import math
os.environ.setdefault('SDL_VIDEODRIVER','dummy')
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import pygame
pygame.init()
pygame.display.set_mode((1,1))
from jggz62fe import y38daly8,iq5c34dx,k1wj0tpa
from entities import ky20479t,eohswq40
from mg5wzawn import mvxdp5gj
from zywm7s6n import w89uzfk8
from x50opf06 import cq2q4qer
class pecruyf3(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def njka34mq(self):
  player=ky20479t()
  jo8e7flq=eohswq40('xytaul',player.xu9ymszd.centerx,player.xu9ymszd.centery)
  jo8e7flq.rzs43c5b=0
  self.assertEqual(player.eehou6ql,[])
  jo8e7flq.g11kerpe(player)
  self.assertEqual(len(player.eehou6ql),1)
  (x,y,gsrtwlxd,color)=player.eehou6ql[0]
  self.assertEqual(color,iq5c34dx['cm3v2p'])
  self.assertTrue(gsrtwlxd.startswith('-'))
 def bsp7bm41(self):
  player=ky20479t()
  kmgfxc08=mvxdp5gj('x2s8nn',player.xu9ymszd.centerx,player.xu9ymszd.centery,6,6,1,0)
  kmgfxc08.rzewviyt=12
  kmgfxc08.g11kerpe([],[],[],player=player,target='player')
  self.assertEqual(len(player.eehou6ql),1)
  self.assertEqual(player.eehou6ql[0][3],iq5c34dx['cm3v2p'])
 def frhzn4kg(self):
  player=ky20479t()
  pvasifpw=eohswq40('vuvldd',player.xu9ymszd.centerx+5,player.xu9ymszd.centery)
  pvasifpw.rzs43c5b=0
  pvasifpw.g11kerpe(player)
  for wrbw2zla in range(pvasifpw.n8sa3idy-1):
   pvasifpw.g11kerpe(player)
  self.assertEqual(player.eehou6ql,[])
  pvasifpw.g11kerpe(player)
  self.assertEqual(len(player.eehou6ql),1)
  self.assertEqual(player.eehou6ql[0][3],iq5c34dx['cm3v2p'])
 def kn5gjj8m(self):
  player=ky20479t()
  nd6357oo=eohswq40('pivroc',player.xu9ymszd.centerx+5,player.xu9ymszd.centery)
  nd6357oo.w4rcb1kj=0
  nd6357oo.move(player)
  cq2q4qer([nd6357oo],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.eehou6ql),1)
  self.assertEqual(player.eehou6ql[0][3],iq5c34dx['cm3v2p'])
 def rm0j36tc(self):
  player=ky20479t()
  jo8e7flq=eohswq40('xytaul',player.xu9ymszd.centerx,player.xu9ymszd.centery)
  jo8e7flq.rzs43c5b=0
  bokzixza=player.w4rcb1kj
  jo8e7flq.g11kerpe(player)
  tnz61231=bokzixza-player.w4rcb1kj
  (wrbw2zla,wrbw2zla,gsrtwlxd,wrbw2zla)=player.eehou6ql[0]
  self.assertEqual(gsrtwlxd,f'-{int(tnz61231)}')
 def vm65q57t(self):
  jo8e7flq=eohswq40('xytaul',100,100)
  bllo3rbx=mvxdp5gj('oud2zd',jo8e7flq.xu9ymszd.centerx,jo8e7flq.xu9ymszd.centery,6,6,1,0)
  nfn1r4kz=[jo8e7flq]
  self.assertEqual(jo8e7flq.eehou6ql,[])
  bllo3rbx.g11kerpe(nfn1r4kz,[],[])
  self.assertEqual(len(jo8e7flq.eehou6ql),1)
  (x,y,gsrtwlxd,color)=jo8e7flq.eehou6ql[0]
  self.assertEqual(color,iq5c34dx['cxf5x9'])
  self.assertTrue(gsrtwlxd.startswith('-'))
 def l0sqg4ei(self):
  ytb9xxay=eohswq40('xytaul',100,100)
  mnx4sn6s=eohswq40('xytaul',120,100)
  nfn1r4kz=[ytb9xxay,mnx4sn6s]
  dzsedfqs=mvxdp5gj('vlou83',ytb9xxay.xu9ymszd.centerx,ytb9xxay.xu9ymszd.centery,10,10,1,0)
  dzsedfqs.g11kerpe(nfn1r4kz,[],[])
  self.assertEqual(len(mnx4sn6s.eehou6ql),1)
  self.assertEqual(mnx4sn6s.eehou6ql[0][3],iq5c34dx['cxf5x9'])
class jdiuovw1(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def y06nkwfg(self):
  kx74d0gj=eohswq40('az3m55',100,100)
  kx74d0gj.xu9ymszd.width=kx74d0gj.xu9ymszd.height=60
  bllo3rbx=mvxdp5gj('fkmuso',kx74d0gj.xu9ymszd.centerx,kx74d0gj.xu9ymszd.centery,4,4,0.01,0)
  n3rlkte4=0
  for wrbw2zla in range(10):
   bllo3rbx.move(kx74d0gj)
   bokzixza=kx74d0gj.w4rcb1kj
   bllo3rbx.g11kerpe([kx74d0gj],[],[])
   if kx74d0gj.w4rcb1kj<bokzixza:
    n3rlkte4+=1
   if bllo3rbx.jqxs6esj:
    break
  self.assertEqual(n3rlkte4,1)
  self.assertEqual(bllo3rbx.zqcootnj,1)
 def ejbzutru(self):
  nfn1r4kz=[eohswq40('xytaul',100+je11e9ft*5,100)for je11e9ft in range(4)]
  bllo3rbx=mvxdp5gj('fkmuso',100,100,30,30,1,0)
  bllo3rbx.g11kerpe(nfn1r4kz,[],[])
  self.assertEqual(len(bllo3rbx.xk7n8la1),bllo3rbx.g1g1r1dw,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(bllo3rbx.jqxs6esj)
class xd1wjcit(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def ayr1k12v(self):
  player=ky20479t()
  jo8e7flq=eohswq40('xytaul',player.xu9ymszd.centerx,player.xu9ymszd.centery)
  jo8e7flq.rzs43c5b=0
  self.assertFalse(player.u15pdtz9)
  jo8e7flq.g11kerpe(player)
  self.assertTrue(player.u15pdtz9)
  self.assertEqual(player.yp3cyazb,y38daly8)
 def o9zqyahu(self):
  player=ky20479t()
  kmgfxc08=mvxdp5gj('x2s8nn',player.xu9ymszd.centerx,player.xu9ymszd.centery,6,6,1,0)
  self.assertFalse(player.u15pdtz9)
  kmgfxc08.g11kerpe([],[],[],player=player,target='player')
  self.assertTrue(player.u15pdtz9)
class yr5uqpgb(unittest.TestCase):
 def wvndfdw7(self):
  player=ky20479t()
  wehlxslg=w89uzfk8(player.xu9ymszd.x,player.xu9ymszd.y,50)
  m9bn18gp=player.w2sq3b9s
  wehlxslg.move(player)
  self.assertTrue(wehlxslg.jqxs6esj)
  self.assertEqual(player.w2sq3b9s,m9bn18gp+50)
class s9skdgig(unittest.TestCase):
 def usz2kuuo(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=ky20479t()
  li9nb74x=mvxdp5gj('ta5kw3',player.xu9ymszd.centerx-250,player.xu9ymszd.centery,20,27,1,0)
  li9nb74x.jslulzfy=True
  li9nb74x.wzlm72je=li9nb74x.mpyxdw2z+1
  d1hm38ks=None
  for fekrcppr in range(li9nb74x.mcup8ijl):
   player.xu9ymszd.x+=player.q6nqqb9l
   li9nb74x.move(player)
   if li9nb74x.jqxs6esj:
    d1hm38ks=fekrcppr
    break
  self.assertIsNotNone(d1hm38ks,'boomerang never caught up to the player')
  self.assertLess(d1hm38ks,li9nb74x.mcup8ijl-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
