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
from en1x2gdg import yur7ko64,iq5c34dx,k1wj0tpa
from entities import rqf5q14j,vqnpcenl
from c4kek4ae import yswjckjl
from f25mdf7f import w89uzfk8
from jxgbngz6 import uj64qhks
class gmjkv5us(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def ej16dvtj(self):
  player=rqf5q14j()
  u0q0mftg=vqnpcenl('wyn6sj',player.f8rtm4j3.centerx,player.f8rtm4j3.centery)
  u0q0mftg.lt63j3r3=0
  self.assertEqual(player.wb7f6fdh,[])
  u0q0mftg.sne6loh2(player)
  self.assertEqual(len(player.wb7f6fdh),1)
  (qxb7gbdg,n01uyzpd,v7g0iiji,color)=player.wb7f6fdh[0]
  self.assertEqual(color,iq5c34dx['xutxzb'])
  self.assertTrue(v7g0iiji.startswith('-'))
 def ysqg8x80(self):
  player=rqf5q14j()
  sk8yqk94=yswjckjl('n1p0vu',player.f8rtm4j3.centerx,player.f8rtm4j3.centery,6,6,1,0)
  sk8yqk94.oqse3tv1=12
  sk8yqk94.sne6loh2([],[],[],player=player,target='player')
  self.assertEqual(len(player.wb7f6fdh),1)
  self.assertEqual(player.wb7f6fdh[0][3],iq5c34dx['xutxzb'])
 def w8wj0uun(self):
  player=rqf5q14j()
  g11kerpe=vqnpcenl('s3dxb3',player.f8rtm4j3.centerx+5,player.f8rtm4j3.centery)
  g11kerpe.lt63j3r3=0
  g11kerpe.sne6loh2(player)
  for dtx63cfl in range(g11kerpe.rh0w064w-1):
   g11kerpe.sne6loh2(player)
  self.assertEqual(player.wb7f6fdh,[])
  g11kerpe.sne6loh2(player)
  self.assertEqual(len(player.wb7f6fdh),1)
  self.assertEqual(player.wb7f6fdh[0][3],iq5c34dx['xutxzb'])
 def q6nqqb9l(self):
  player=rqf5q14j()
  kmgfxc08=vqnpcenl('dbmenu',player.f8rtm4j3.centerx+5,player.f8rtm4j3.centery)
  kmgfxc08.sf337kuu=0
  kmgfxc08.y2f7atwy(player)
  uj64qhks([kmgfxc08],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.wb7f6fdh),1)
  self.assertEqual(player.wb7f6fdh[0][3],iq5c34dx['xutxzb'])
 def kc7rm6j8(self):
  player=rqf5q14j()
  u0q0mftg=vqnpcenl('wyn6sj',player.f8rtm4j3.centerx,player.f8rtm4j3.centery)
  u0q0mftg.lt63j3r3=0
  xqzpky32=player.sf337kuu
  u0q0mftg.sne6loh2(player)
  i01nouht=xqzpky32-player.sf337kuu
  (dtx63cfl,dtx63cfl,v7g0iiji,dtx63cfl)=player.wb7f6fdh[0]
  self.assertEqual(v7g0iiji,f'-{int(i01nouht)}')
 def p2nv01zd(self):
  u0q0mftg=vqnpcenl('wyn6sj',100,100)
  u3ifhv1x=yswjckjl('twvwvi',u0q0mftg.f8rtm4j3.centerx,u0q0mftg.f8rtm4j3.centery,6,6,1,0)
  wc7x0h3j=[u0q0mftg]
  self.assertEqual(u0q0mftg.wb7f6fdh,[])
  u3ifhv1x.sne6loh2(wc7x0h3j,[],[])
  self.assertEqual(len(u0q0mftg.wb7f6fdh),1)
  (qxb7gbdg,n01uyzpd,v7g0iiji,color)=u0q0mftg.wb7f6fdh[0]
  self.assertEqual(color,iq5c34dx['pta5iv'])
  self.assertTrue(v7g0iiji.startswith('-'))
 def qy3vg6v5(self):
  co4busu9=vqnpcenl('wyn6sj',100,100)
  gj29yfc2=vqnpcenl('wyn6sj',120,100)
  wc7x0h3j=[co4busu9,gj29yfc2]
  ra73jgzl=yswjckjl('lf0d0i',co4busu9.f8rtm4j3.centerx,co4busu9.f8rtm4j3.centery,10,10,1,0)
  ra73jgzl.sne6loh2(wc7x0h3j,[],[])
  self.assertEqual(len(gj29yfc2.wb7f6fdh),1)
  self.assertEqual(gj29yfc2.wb7f6fdh[0][3],iq5c34dx['pta5iv'])
class gdzr1yxr(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def xxkdq95g(self):
  uidlrye8=vqnpcenl('fnn16u',100,100)
  uidlrye8.f8rtm4j3.width=uidlrye8.f8rtm4j3.height=60
  u3ifhv1x=yswjckjl('xyhhg8',uidlrye8.f8rtm4j3.centerx,uidlrye8.f8rtm4j3.centery,4,4,0.01,0)
  a8lw2lm3=0
  for dtx63cfl in range(10):
   u3ifhv1x.y2f7atwy(uidlrye8)
   xqzpky32=uidlrye8.sf337kuu
   u3ifhv1x.sne6loh2([uidlrye8],[],[])
   if uidlrye8.sf337kuu<xqzpky32:
    a8lw2lm3+=1
   if u3ifhv1x.rk8r2ykc:
    break
  self.assertEqual(a8lw2lm3,1)
  self.assertEqual(u3ifhv1x.rzewviyt,1)
 def n8sa3idy(self):
  wc7x0h3j=[vqnpcenl('wyn6sj',100+z8z3v6di*5,100)for z8z3v6di in range(4)]
  u3ifhv1x=yswjckjl('xyhhg8',100,100,30,30,1,0)
  u3ifhv1x.sne6loh2(wc7x0h3j,[],[])
  self.assertEqual(len(u3ifhv1x.fekrcppr),u3ifhv1x.mu4fmpkx,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(u3ifhv1x.rk8r2ykc)
class lp0lzjje(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def az2ueaxy(self):
  player=rqf5q14j()
  u0q0mftg=vqnpcenl('wyn6sj',player.f8rtm4j3.centerx,player.f8rtm4j3.centery)
  u0q0mftg.lt63j3r3=0
  self.assertFalse(player.tj0nmeoq)
  u0q0mftg.sne6loh2(player)
  self.assertTrue(player.tj0nmeoq)
  self.assertEqual(player.myrp5ge0,yur7ko64)
 def p7b1ijiy(self):
  player=rqf5q14j()
  sk8yqk94=yswjckjl('n1p0vu',player.f8rtm4j3.centerx,player.f8rtm4j3.centery,6,6,1,0)
  self.assertFalse(player.tj0nmeoq)
  sk8yqk94.sne6loh2([],[],[],player=player,target='player')
  self.assertTrue(player.tj0nmeoq)
class oiqvnb4g(unittest.TestCase):
 def k82853uy(self):
  player=rqf5q14j()
  iie0rnuj=w89uzfk8(player.f8rtm4j3.qxb7gbdg,player.f8rtm4j3.n01uyzpd,50)
  tza7x73q=player.bu4xszjn
  iie0rnuj.y2f7atwy(player)
  self.assertTrue(iie0rnuj.rk8r2ykc)
  self.assertEqual(player.bu4xszjn,tza7x73q+50)
class ozp08j3t(unittest.TestCase):
 def hcxhgnze(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=rqf5q14j()
  c0hpmnz1=yswjckjl('hjkuuh',player.f8rtm4j3.centerx-250,player.f8rtm4j3.centery,20,27,1,0)
  c0hpmnz1.rb1s9dwd=True
  c0hpmnz1.f2sehe2a=c0hpmnz1.jqzpniqf+1
  z3olfark=None
  for qhkc856w in range(c0hpmnz1.w5iz31yr):
   player.f8rtm4j3.qxb7gbdg+=player.kz1uu7zy
   c0hpmnz1.y2f7atwy(player)
   if c0hpmnz1.rk8r2ykc:
    z3olfark=qhkc856w
    break
  self.assertIsNotNone(z3olfark,'boomerang never caught up to the player')
  self.assertLess(z3olfark,c0hpmnz1.w5iz31yr-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
