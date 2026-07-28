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
from e87f8tsx import y38daly8,iq5c34dx,k1wj0tpa
from entities import ky20479t,qtzk3ny9
from bdnwnguc import mvxdp5gj
from wh0imjyj import w89uzfk8
from j4kuqaaj import h4l1vznq
class pecruyf3(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def zanouof0(self):
  player=ky20479t()
  zpajssuu=qtzk3ny9('l226pa',player.pllkstn3.centerx,player.pllkstn3.centery)
  zpajssuu.ra73jgzl=0
  self.assertEqual(player.g1g1r1dw,[])
  zpajssuu.ykipu1wy(player)
  self.assertEqual(len(player.g1g1r1dw),1)
  (j1kfk7y6,f1bl08kg,gsrtwlxd,color)=player.g1g1r1dw[0]
  self.assertEqual(color,iq5c34dx['y3lxch'])
  self.assertTrue(gsrtwlxd.startswith('-'))
 def frhzn4kg(self):
  player=ky20479t()
  nqimqodp=mvxdp5gj('pqpva5',player.pllkstn3.centerx,player.pllkstn3.centery,6,6,1,0)
  nqimqodp.wzlm72je=12
  nqimqodp.ykipu1wy([],[],[],player=player,target='player')
  self.assertEqual(len(player.g1g1r1dw),1)
  self.assertEqual(player.g1g1r1dw[0][3],iq5c34dx['y3lxch'])
 def usz2kuuo(self):
  player=ky20479t()
  dzsedfqs=qtzk3ny9('tcu9td',player.pllkstn3.centerx+5,player.pllkstn3.centery)
  dzsedfqs.ra73jgzl=0
  dzsedfqs.ykipu1wy(player)
  for t1w1ht7p in range(dzsedfqs.s5r96khu-1):
   dzsedfqs.ykipu1wy(player)
  self.assertEqual(player.g1g1r1dw,[])
  dzsedfqs.ykipu1wy(player)
  self.assertEqual(len(player.g1g1r1dw),1)
  self.assertEqual(player.g1g1r1dw[0][3],iq5c34dx['y3lxch'])
 def gf8f3gr9(self):
  player=ky20479t()
  qbm1enf3=qtzk3ny9('xu7dkn',player.pllkstn3.centerx+5,player.pllkstn3.centery)
  qbm1enf3.ftrflqbm=0
  qbm1enf3.wb7f6fdh(player)
  h4l1vznq([qbm1enf3],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.g1g1r1dw),1)
  self.assertEqual(player.g1g1r1dw[0][3],iq5c34dx['y3lxch'])
 def awnwlc83(self):
  player=ky20479t()
  zpajssuu=qtzk3ny9('l226pa',player.pllkstn3.centerx,player.pllkstn3.centery)
  zpajssuu.ra73jgzl=0
  zmybd2qe=player.ftrflqbm
  zpajssuu.ykipu1wy(player)
  yjluujmi=zmybd2qe-player.ftrflqbm
  (t1w1ht7p,t1w1ht7p,gsrtwlxd,t1w1ht7p)=player.g1g1r1dw[0]
  self.assertEqual(gsrtwlxd,f'-{int(yjluujmi)}')
 def njka34mq(self):
  zpajssuu=qtzk3ny9('l226pa',100,100)
  pvasifpw=mvxdp5gj('fkmuso',zpajssuu.pllkstn3.centerx,zpajssuu.pllkstn3.centery,6,6,1,0)
  qhkc856w=[zpajssuu]
  self.assertEqual(zpajssuu.g1g1r1dw,[])
  pvasifpw.ykipu1wy(qhkc856w,[],[])
  self.assertEqual(len(zpajssuu.g1g1r1dw),1)
  (j1kfk7y6,f1bl08kg,gsrtwlxd,color)=zpajssuu.g1g1r1dw[0]
  self.assertEqual(color,iq5c34dx['hzj7ub'])
  self.assertTrue(gsrtwlxd.startswith('-'))
 def mlikwe4b(self):
  nxxjve3d=qtzk3ny9('l226pa',100,100)
  nabufwbu=qtzk3ny9('l226pa',120,100)
  qhkc856w=[nxxjve3d,nabufwbu]
  giec4d14=mvxdp5gj('lcf4mn',nxxjve3d.pllkstn3.centerx,nxxjve3d.pllkstn3.centery,10,10,1,0)
  giec4d14.ykipu1wy(qhkc856w,[],[])
  self.assertEqual(len(nabufwbu.g1g1r1dw),1)
  self.assertEqual(nabufwbu.g1g1r1dw[0][3],iq5c34dx['hzj7ub'])
class jdiuovw1(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def l0sqg4ei(self):
  nfn1r4kz=qtzk3ny9('cxf5x9',100,100)
  nfn1r4kz.pllkstn3.width=nfn1r4kz.pllkstn3.height=60
  pvasifpw=mvxdp5gj('zmygy0',nfn1r4kz.pllkstn3.centerx,nfn1r4kz.pllkstn3.centery,4,4,0.01,0)
  swwnc21o=0
  for t1w1ht7p in range(10):
   pvasifpw.wb7f6fdh(nfn1r4kz)
   zmybd2qe=nfn1r4kz.ftrflqbm
   pvasifpw.ykipu1wy([nfn1r4kz],[],[])
   if nfn1r4kz.ftrflqbm<zmybd2qe:
    swwnc21o+=1
   if pvasifpw.uc1xi04b:
    break
  self.assertEqual(swwnc21o,1)
  self.assertEqual(pvasifpw.nubmxnsz,1)
 def eq3tq1s0(self):
  qhkc856w=[qtzk3ny9('l226pa',100+bokzixza*5,100)for bokzixza in range(4)]
  pvasifpw=mvxdp5gj('zmygy0',100,100,30,30,1,0)
  pvasifpw.ykipu1wy(qhkc856w,[],[])
  self.assertEqual(len(pvasifpw.v3e1ocjx),pvasifpw.k1taa0i5,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(pvasifpw.uc1xi04b)
class xd1wjcit(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def m3hcws2w(self):
  player=ky20479t()
  zpajssuu=qtzk3ny9('l226pa',player.pllkstn3.centerx,player.pllkstn3.centery)
  zpajssuu.ra73jgzl=0
  self.assertFalse(player.cb2uuijn)
  zpajssuu.ykipu1wy(player)
  self.assertTrue(player.cb2uuijn)
  self.assertEqual(player.uoloeazc,y38daly8)
 def e9y3z2t4(self):
  player=ky20479t()
  nqimqodp=mvxdp5gj('pqpva5',player.pllkstn3.centerx,player.pllkstn3.centery,6,6,1,0)
  self.assertFalse(player.cb2uuijn)
  nqimqodp.ykipu1wy([],[],[],player=player,target='player')
  self.assertTrue(player.cb2uuijn)
class yr5uqpgb(unittest.TestCase):
 def r212pgym(self):
  player=ky20479t()
  sl65wvjx=w89uzfk8(player.pllkstn3.j1kfk7y6,player.pllkstn3.f1bl08kg,50)
  eolaq665=player.o3q0e27z
  sl65wvjx.wb7f6fdh(player)
  self.assertTrue(sl65wvjx.uc1xi04b)
  self.assertEqual(player.o3q0e27z,eolaq665+50)
class s9skdgig(unittest.TestCase):
 def guxt9kls(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=ky20479t()
  yw6zbnz8=mvxdp5gj('m314cq',player.pllkstn3.centerx-250,player.pllkstn3.centery,20,27,1,0)
  yw6zbnz8.kcubods1=True
  yw6zbnz8.wehlxslg=yw6zbnz8.x9bp4m18+1
  nbwye6qv=None
  for damdvlnk in range(yw6zbnz8.hp89fkbi):
   player.pllkstn3.j1kfk7y6+=player.hcxhgnze
   yw6zbnz8.wb7f6fdh(player)
   if yw6zbnz8.uc1xi04b:
    nbwye6qv=damdvlnk
    break
  self.assertIsNotNone(nbwye6qv,'boomerang never caught up to the player')
  self.assertLess(nbwye6qv,yw6zbnz8.hp89fkbi-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
