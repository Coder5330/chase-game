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
from v7bnhjw6 import s8qjnv8z,iq5c34dx,k1wj0tpa
from entities import r0tvhhpb,u1jhuwb6
from xu7bfxq7 import ky20479t
from tgv3dr2h import w89uzfk8
from piua08ek import ytb9xxay
class yr5uqpgb(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def a1tbrwr9(self):
  player=r0tvhhpb()
  m8lw2qit=u1jhuwb6('nk7y6q',player.jenvg3kk.centerx,player.jenvg3kk.centery)
  m8lw2qit.i4fejgxa=0
  self.assertEqual(player.zflse45b,[])
  m8lw2qit.ytv3i12v(player)
  self.assertEqual(len(player.zflse45b),1)
  (qic1l7dy,vsjchzjq,vm65q57t,color)=player.zflse45b[0]
  self.assertEqual(color,iq5c34dx['r3hxyj'])
  self.assertTrue(vm65q57t.startswith('-'))
 def rr9u1oe5(self):
  player=r0tvhhpb()
  reqy08p0=ky20479t('wdl5tg',player.jenvg3kk.centerx,player.jenvg3kk.centery,6,6,1,0)
  reqy08p0.i01nouht=12
  reqy08p0.ytv3i12v([],[],[],player=player,target='player')
  self.assertEqual(len(player.zflse45b),1)
  self.assertEqual(player.zflse45b[0][3],iq5c34dx['r3hxyj'])
 def p7pchcbn(self):
  player=r0tvhhpb()
  bq349dxb=u1jhuwb6('uet25l',player.jenvg3kk.centerx+5,player.jenvg3kk.centery)
  bq349dxb.i4fejgxa=0
  bq349dxb.ytv3i12v(player)
  for m53a5qbs in range(bq349dxb.ej16dvtj-1):
   bq349dxb.ytv3i12v(player)
  self.assertEqual(player.zflse45b,[])
  bq349dxb.ytv3i12v(player)
  self.assertEqual(len(player.zflse45b),1)
  self.assertEqual(player.zflse45b[0][3],iq5c34dx['r3hxyj'])
 def rwybow23(self):
  player=r0tvhhpb()
  f8wquuy5=u1jhuwb6('iimoe0',player.jenvg3kk.centerx+5,player.jenvg3kk.centery)
  f8wquuy5.mn7h9g1a=0
  f8wquuy5.r2muljav(player)
  ytb9xxay([f8wquuy5],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.zflse45b),1)
  self.assertEqual(player.zflse45b[0][3],iq5c34dx['r3hxyj'])
 def mlikwe4b(self):
  player=r0tvhhpb()
  m8lw2qit=u1jhuwb6('nk7y6q',player.jenvg3kk.centerx,player.jenvg3kk.centery)
  m8lw2qit.i4fejgxa=0
  semqgy27=player.mn7h9g1a
  m8lw2qit.ytv3i12v(player)
  wzlm72je=semqgy27-player.mn7h9g1a
  (m53a5qbs,m53a5qbs,vm65q57t,m53a5qbs)=player.zflse45b[0]
  self.assertEqual(vm65q57t,f'-{int(wzlm72je)}')
 def h4m2ec8r(self):
  m8lw2qit=u1jhuwb6('nk7y6q',100,100)
  uysal8m1=ky20479t('dzjssz',m8lw2qit.jenvg3kk.centerx,m8lw2qit.jenvg3kk.centery,6,6,1,0)
  dw7nh8rq=[m8lw2qit]
  self.assertEqual(m8lw2qit.zflse45b,[])
  uysal8m1.ytv3i12v(dw7nh8rq,[],[])
  self.assertEqual(len(m8lw2qit.zflse45b),1)
  (qic1l7dy,vsjchzjq,vm65q57t,color)=m8lw2qit.zflse45b[0]
  self.assertEqual(color,iq5c34dx['v9hbn5'])
  self.assertTrue(vm65q57t.startswith('-'))
 def n8sa3idy(self):
  tkyrmjlj=u1jhuwb6('nk7y6q',100,100)
  xo2t8fy6=u1jhuwb6('nk7y6q',120,100)
  dw7nh8rq=[tkyrmjlj,xo2t8fy6]
  u3ifhv1x=ky20479t('xutxzb',tkyrmjlj.jenvg3kk.centerx,tkyrmjlj.jenvg3kk.centery,10,10,1,0)
  u3ifhv1x.ytv3i12v(dw7nh8rq,[],[])
  self.assertEqual(len(xo2t8fy6.zflse45b),1)
  self.assertEqual(xo2t8fy6.zflse45b[0][3],iq5c34dx['v9hbn5'])
class pecruyf3(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def k82853uy(self):
  v15cqzcu=u1jhuwb6('hn3ksg',100,100)
  v15cqzcu.jenvg3kk.width=v15cqzcu.jenvg3kk.height=60
  uysal8m1=ky20479t('pswrgv',v15cqzcu.jenvg3kk.centerx,v15cqzcu.jenvg3kk.centery,4,4,0.01,0)
  ftlpq2wg=0
  for m53a5qbs in range(10):
   uysal8m1.r2muljav(v15cqzcu)
   semqgy27=v15cqzcu.mn7h9g1a
   uysal8m1.ytv3i12v([v15cqzcu],[],[])
   if v15cqzcu.mn7h9g1a<semqgy27:
    ftlpq2wg+=1
   if uysal8m1.sl65wvjx:
    break
  self.assertEqual(ftlpq2wg,1)
  self.assertEqual(uysal8m1.tnz61231,1)
 def rb1s9dwd(self):
  dw7nh8rq=[u1jhuwb6('nk7y6q',100+ftrflqbm*5,100)for ftrflqbm in range(4)]
  uysal8m1=ky20479t('pswrgv',100,100,30,30,1,0)
  uysal8m1.ytv3i12v(dw7nh8rq,[],[])
  self.assertEqual(len(uysal8m1.gsmdzqcb),uysal8m1.l3swebnv,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(uysal8m1.sl65wvjx)
class mqp49kwv(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def s5r96khu(self):
  player=r0tvhhpb()
  m8lw2qit=u1jhuwb6('nk7y6q',player.jenvg3kk.centerx,player.jenvg3kk.centery)
  m8lw2qit.i4fejgxa=0
  self.assertFalse(player.k8qeoz0k)
  m8lw2qit.ytv3i12v(player)
  self.assertTrue(player.k8qeoz0k)
  self.assertEqual(player.wtl0thhz,s8qjnv8z)
 def d0qzfhom(self):
  player=r0tvhhpb()
  reqy08p0=ky20479t('wdl5tg',player.jenvg3kk.centerx,player.jenvg3kk.centery,6,6,1,0)
  self.assertFalse(player.k8qeoz0k)
  reqy08p0.ytv3i12v([],[],[],player=player,target='player')
  self.assertTrue(player.k8qeoz0k)
class azebbk7w(unittest.TestCase):
 def klkjxjq5(self):
  player=r0tvhhpb()
  rk8r2ykc=w89uzfk8(player.jenvg3kk.qic1l7dy,player.jenvg3kk.vsjchzjq,50)
  zpfb3hn1=player.nngmx1gm
  rk8r2ykc.r2muljav(player)
  self.assertTrue(rk8r2ykc.sl65wvjx)
  self.assertEqual(player.nngmx1gm,zpfb3hn1+50)
class gl08yg0j(unittest.TestCase):
 def wigbiaf9(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=r0tvhhpb()
  uww5wfcp=ky20479t('q8wwii',player.jenvg3kk.centerx-250,player.jenvg3kk.centery,20,27,1,0)
  uww5wfcp.r212pgym=True
  uww5wfcp.k7zgf9q5=uww5wfcp.xq46nouh+1
  gmoft6yr=None
  for ao4izasn in range(uww5wfcp.ub68rerv):
   player.jenvg3kk.qic1l7dy+=player.xvzc7d2k
   uww5wfcp.r2muljav(player)
   if uww5wfcp.sl65wvjx:
    gmoft6yr=ao4izasn
    break
  self.assertIsNotNone(gmoft6yr,'boomerang never caught up to the player')
  self.assertLess(gmoft6yr,uww5wfcp.ub68rerv-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
