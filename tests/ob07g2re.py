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
from z4w1arag import b18hafey,iq5c34dx,k1wj0tpa
from entities import yur7ko64,wi8skch8
from kyow8dt8 import r0tvhhpb
from jz6wmdw0 import w89uzfk8
from umjmbukd import upprat08
class azebbk7w(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def mu118qqv(self):
  player=yur7ko64()
  sf337kuu=wi8skch8('xyhhg8',player.cqheyto5.centerx,player.cqheyto5.centery)
  sf337kuu.uva2ieuc=0
  self.assertEqual(player.y8dd2255,[])
  sf337kuu.lcj883dh(player)
  self.assertEqual(len(player.y8dd2255),1)
  (d5ixva1n,nngmx1gm,z7pwo6cm,color)=player.y8dd2255[0]
  self.assertEqual(color,iq5c34dx['dzjssz'])
  self.assertTrue(z7pwo6cm.startswith('-'))
 def yypp5zp7(self):
  player=yur7ko64()
  pa5u6hc3=r0tvhhpb('t753ay',player.cqheyto5.centerx,player.cqheyto5.centery,6,6,1,0)
  pa5u6hc3.k7zgf9q5=12
  pa5u6hc3.lcj883dh([],[],[],player=player,target='player')
  self.assertEqual(len(player.y8dd2255),1)
  self.assertEqual(player.y8dd2255[0][3],iq5c34dx['dzjssz'])
 def az2ueaxy(self):
  player=yur7ko64()
  jc54wsqt=wi8skch8('q8uzb7',player.cqheyto5.centerx+5,player.cqheyto5.centery)
  jc54wsqt.uva2ieuc=0
  jc54wsqt.lcj883dh(player)
  for v83tqll8 in range(jc54wsqt.nv23gxj0-1):
   jc54wsqt.lcj883dh(player)
  self.assertEqual(player.y8dd2255,[])
  jc54wsqt.lcj883dh(player)
  self.assertEqual(len(player.y8dd2255),1)
  self.assertEqual(player.y8dd2255[0][3],iq5c34dx['dzjssz'])
 def ej16dvtj(self):
  player=yur7ko64()
  fcwtg1m8=wi8skch8('acxx6m',player.cqheyto5.centerx+5,player.cqheyto5.centery)
  fcwtg1m8.a8lw2lm3=0
  fcwtg1m8.chx3d43e(player)
  upprat08([fcwtg1m8],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.y8dd2255),1)
  self.assertEqual(player.y8dd2255[0][3],iq5c34dx['dzjssz'])
 def y06nkwfg(self):
  player=yur7ko64()
  sf337kuu=wi8skch8('xyhhg8',player.cqheyto5.centerx,player.cqheyto5.centery)
  sf337kuu.uva2ieuc=0
  vpbwhvnz=player.a8lw2lm3
  sf337kuu.lcj883dh(player)
  wehlxslg=vpbwhvnz-player.a8lw2lm3
  (v83tqll8,v83tqll8,z7pwo6cm,v83tqll8)=player.y8dd2255[0]
  self.assertEqual(z7pwo6cm,f'-{int(wehlxslg)}')
 def k82853uy(self):
  sf337kuu=wi8skch8('xyhhg8',100,100)
  llxxezdu=r0tvhhpb('pqpva5',sf337kuu.cqheyto5.centerx,sf337kuu.cqheyto5.centery,6,6,1,0)
  mygfliji=[sf337kuu]
  self.assertEqual(sf337kuu.y8dd2255,[])
  llxxezdu.lcj883dh(mygfliji,[],[])
  self.assertEqual(len(sf337kuu.y8dd2255),1)
  (d5ixva1n,nngmx1gm,z7pwo6cm,color)=sf337kuu.y8dd2255[0]
  self.assertEqual(color,iq5c34dx['lcf4mn'])
  self.assertTrue(z7pwo6cm.startswith('-'))
 def yoyohaz7(self):
  f8rtm4j3=wi8skch8('xyhhg8',100,100)
  u15pdtz9=wi8skch8('xyhhg8',120,100)
  mygfliji=[f8rtm4j3,u15pdtz9]
  divsolml=r0tvhhpb('twvwvi',f8rtm4j3.cqheyto5.centerx,f8rtm4j3.cqheyto5.centery,10,10,1,0)
  divsolml.lcj883dh(mygfliji,[],[])
  self.assertEqual(len(u15pdtz9.y8dd2255),1)
  self.assertEqual(u15pdtz9.y8dd2255[0][3],iq5c34dx['lcf4mn'])
class yr5uqpgb(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def mwszv83x(self):
  velos6zl=wi8skch8('k7rrbe',100,100)
  velos6zl.cqheyto5.width=velos6zl.cqheyto5.height=60
  llxxezdu=r0tvhhpb('txzuu8',velos6zl.cqheyto5.centerx,velos6zl.cqheyto5.centery,4,4,0.01,0)
  jo8e7flq=0
  for v83tqll8 in range(10):
   llxxezdu.chx3d43e(velos6zl)
   vpbwhvnz=velos6zl.a8lw2lm3
   llxxezdu.lcj883dh([velos6zl],[],[])
   if velos6zl.a8lw2lm3<vpbwhvnz:
    jo8e7flq+=1
   if llxxezdu.qbbz2sf6:
    break
  self.assertEqual(jo8e7flq,1)
  self.assertEqual(llxxezdu.yjluujmi,1)
 def guxt9kls(self):
  mygfliji=[wi8skch8('xyhhg8',100+semqgy27*5,100)for semqgy27 in range(4)]
  llxxezdu=r0tvhhpb('txzuu8',100,100,30,30,1,0)
  llxxezdu.lcj883dh(mygfliji,[],[])
  self.assertEqual(len(llxxezdu.zpajssuu),llxxezdu.vyb6li07,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(llxxezdu.qbbz2sf6)
class jdiuovw1(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def arjn2hz2(self):
  player=yur7ko64()
  sf337kuu=wi8skch8('xyhhg8',player.cqheyto5.centerx,player.cqheyto5.centery)
  sf337kuu.uva2ieuc=0
  self.assertFalse(player.wd6r30oj)
  sf337kuu.lcj883dh(player)
  self.assertTrue(player.wd6r30oj)
  self.assertEqual(player.gg7oq2zd,b18hafey)
 def p2nv01zd(self):
  player=yur7ko64()
  pa5u6hc3=r0tvhhpb('t753ay',player.cqheyto5.centerx,player.cqheyto5.centery,6,6,1,0)
  self.assertFalse(player.wd6r30oj)
  pa5u6hc3.lcj883dh([],[],[],player=player,target='player')
  self.assertTrue(player.wd6r30oj)
class s9skdgig(unittest.TestCase):
 def usz2kuuo(self):
  player=yur7ko64()
  iektsg7f=w89uzfk8(player.cqheyto5.d5ixva1n,player.cqheyto5.nngmx1gm,50)
  m81udp2f=player.jslulzfy
  iektsg7f.chx3d43e(player)
  self.assertTrue(iektsg7f.qbbz2sf6)
  self.assertEqual(player.jslulzfy,m81udp2f+50)
class lp0lzjje(unittest.TestCase):
 def rr9u1oe5(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=yur7ko64()
  u3ifhv1x=r0tvhhpb('da5xin',player.cqheyto5.centerx-250,player.cqheyto5.centery,20,27,1,0)
  u3ifhv1x.x9h0dxho=True
  u3ifhv1x.bfoqmf5l=u3ifhv1x.g5l8a78e+1
  yg87oi0e=None
  for s4rxyj38 in range(u3ifhv1x.je11e9ft):
   player.cqheyto5.d5ixva1n+=player.q3n2qb6g
   u3ifhv1x.chx3d43e(player)
   if u3ifhv1x.qbbz2sf6:
    yg87oi0e=s4rxyj38
    break
  self.assertIsNotNone(yg87oi0e,'boomerang never caught up to the player')
  self.assertLess(yg87oi0e,u3ifhv1x.je11e9ft-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
