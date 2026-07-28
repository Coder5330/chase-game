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
from z1yhxso7 import b18hafey,iq5c34dx,k1wj0tpa
from entities import yur7ko64,iektsg7f
from ft8xkody import r0tvhhpb
from pn2xr838 import w89uzfk8
from z286utio import jenvg3kk
class azebbk7w(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def n8sa3idy(self):
  player=yur7ko64()
  mytn02yc=iektsg7f('m1v3zo',player.wgcl9lcq.centerx,player.wgcl9lcq.centery)
  mytn02yc.ytv3i12v=0
  self.assertEqual(player.vyb6li07,[])
  mytn02yc.uva2ieuc(player)
  self.assertEqual(len(player.vyb6li07),1)
  (jslulzfy,zpfb3hn1,l0sqg4ei,color)=player.vyb6li07[0]
  self.assertEqual(color,iq5c34dx['xy79kv'])
  self.assertTrue(l0sqg4ei.startswith('-'))
 def ej16dvtj(self):
  player=yur7ko64()
  wkof8krd=r0tvhhpb('g0ht1t',player.wgcl9lcq.centerx,player.wgcl9lcq.centery,6,6,1,0)
  wkof8krd.pa8s8hmb=12
  wkof8krd.uva2ieuc([],[],[],player=player,target='player')
  self.assertEqual(len(player.vyb6li07),1)
  self.assertEqual(player.vyb6li07[0][3],iq5c34dx['xy79kv'])
 def tjy1o2rn(self):
  player=yur7ko64()
  z0b6ugvs=iektsg7f('vmwi9s',player.wgcl9lcq.centerx+5,player.wgcl9lcq.centery)
  z0b6ugvs.ytv3i12v=0
  z0b6ugvs.uva2ieuc(player)
  for v83tqll8 in range(z0b6ugvs.qy3vg6v5-1):
   z0b6ugvs.uva2ieuc(player)
  self.assertEqual(player.vyb6li07,[])
  z0b6ugvs.uva2ieuc(player)
  self.assertEqual(len(player.vyb6li07),1)
  self.assertEqual(player.vyb6li07[0][3],iq5c34dx['xy79kv'])
 def kodpvjtu(self):
  player=yur7ko64()
  u3ifhv1x=iektsg7f('msz6rv',player.wgcl9lcq.centerx+5,player.wgcl9lcq.centery)
  u3ifhv1x.u9el8hl8=0
  u3ifhv1x.ob7p0rnp(player)
  jenvg3kk([u3ifhv1x],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.vyb6li07),1)
  self.assertEqual(player.vyb6li07[0][3],iq5c34dx['xy79kv'])
 def klkjxjq5(self):
  player=yur7ko64()
  mytn02yc=iektsg7f('m1v3zo',player.wgcl9lcq.centerx,player.wgcl9lcq.centery)
  mytn02yc.ytv3i12v=0
  gkz2u2tn=player.u9el8hl8
  mytn02yc.uva2ieuc(player)
  rmm1zxyv=gkz2u2tn-player.u9el8hl8
  (v83tqll8,v83tqll8,l0sqg4ei,v83tqll8)=player.vyb6li07[0]
  self.assertEqual(l0sqg4ei,f'-{int(rmm1zxyv)}')
 def arjn2hz2(self):
  mytn02yc=iektsg7f('m1v3zo',100,100)
  u23y30ys=r0tvhhpb('umfbuv',mytn02yc.wgcl9lcq.centerx,mytn02yc.wgcl9lcq.centery,6,6,1,0)
  yjluujmi=[mytn02yc]
  self.assertEqual(mytn02yc.vyb6li07,[])
  u23y30ys.uva2ieuc(yjluujmi,[],[])
  self.assertEqual(len(mytn02yc.vyb6li07),1)
  (jslulzfy,zpfb3hn1,l0sqg4ei,color)=mytn02yc.vyb6li07[0]
  self.assertEqual(color,iq5c34dx['yl4zjd'])
  self.assertTrue(l0sqg4ei.startswith('-'))
 def gqoagsus(self):
  vhxs58yr=iektsg7f('m1v3zo',100,100)
  cb2uuijn=iektsg7f('m1v3zo',120,100)
  yjluujmi=[vhxs58yr,cb2uuijn]
  fcwtg1m8=r0tvhhpb('wxgnrf',vhxs58yr.wgcl9lcq.centerx,vhxs58yr.wgcl9lcq.centery,10,10,1,0)
  fcwtg1m8.uva2ieuc(yjluujmi,[],[])
  self.assertEqual(len(cb2uuijn.vyb6li07),1)
  self.assertEqual(cb2uuijn.vyb6li07[0][3],iq5c34dx['yl4zjd'])
class yr5uqpgb(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def wigbiaf9(self):
  dw7nh8rq=iektsg7f('n7csuy',100,100)
  dw7nh8rq.wgcl9lcq.width=dw7nh8rq.wgcl9lcq.height=60
  u23y30ys=r0tvhhpb('m314cq',dw7nh8rq.wgcl9lcq.centerx,dw7nh8rq.wgcl9lcq.centery,4,4,0.01,0)
  gsmdzqcb=0
  for v83tqll8 in range(10):
   u23y30ys.ob7p0rnp(dw7nh8rq)
   gkz2u2tn=dw7nh8rq.u9el8hl8
   u23y30ys.uva2ieuc([dw7nh8rq],[],[])
   if dw7nh8rq.u9el8hl8<gkz2u2tn:
    gsmdzqcb+=1
   if u23y30ys.elwf90km:
    break
  self.assertEqual(gsmdzqcb,1)
  self.assertEqual(u23y30ys.velos6zl,1)
 def z7pwo6cm(self):
  yjluujmi=[iektsg7f('m1v3zo',100+sdeekgys*5,100)for sdeekgys in range(4)]
  u23y30ys=r0tvhhpb('m314cq',100,100,30,30,1,0)
  u23y30ys.uva2ieuc(yjluujmi,[],[])
  self.assertEqual(len(u23y30ys.onqyyf9r),u23y30ys.he9p3jpx,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(u23y30ys.elwf90km)
class jdiuovw1(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def kc7rm6j8(self):
  player=yur7ko64()
  mytn02yc=iektsg7f('m1v3zo',player.wgcl9lcq.centerx,player.wgcl9lcq.centery)
  mytn02yc.ytv3i12v=0
  self.assertFalse(player.nbwye6qv)
  mytn02yc.uva2ieuc(player)
  self.assertTrue(player.nbwye6qv)
  self.assertEqual(player.qertb74r,b18hafey)
 def az2ueaxy(self):
  player=yur7ko64()
  wkof8krd=r0tvhhpb('g0ht1t',player.wgcl9lcq.centerx,player.wgcl9lcq.centery,6,6,1,0)
  self.assertFalse(player.nbwye6qv)
  wkof8krd.uva2ieuc([],[],[],player=player,target='player')
  self.assertTrue(player.nbwye6qv)
class s9skdgig(unittest.TestCase):
 def lu7jae58(self):
  player=yur7ko64()
  vw6m7b5c=w89uzfk8(player.wgcl9lcq.jslulzfy,player.wgcl9lcq.zpfb3hn1,50)
  kcubods1=player.m81udp2f
  vw6m7b5c.ob7p0rnp(player)
  self.assertTrue(vw6m7b5c.elwf90km)
  self.assertEqual(player.m81udp2f,kcubods1+50)
class lp0lzjje(unittest.TestCase):
 def rwybow23(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=yur7ko64()
  f8wquuy5=r0tvhhpb('cgsq7a',player.wgcl9lcq.centerx-250,player.wgcl9lcq.centery,20,27,1,0)
  f8wquuy5.jh55hewl=True
  f8wquuy5.l9enulqj=f8wquuy5.yrivh6t1+1
  ytb9xxay=None
  for u0q0mftg in range(f8wquuy5.avfmh07w):
   player.wgcl9lcq.jslulzfy+=player.u15pdtz9
   f8wquuy5.ob7p0rnp(player)
   if f8wquuy5.elwf90km:
    ytb9xxay=u0q0mftg
    break
  self.assertIsNotNone(ytb9xxay,'boomerang never caught up to the player')
  self.assertLess(ytb9xxay,f8wquuy5.avfmh07w-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
