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
from j1bmqf7z import s8qjnv8z,iq5c34dx,k1wj0tpa
from entities import r0tvhhpb,mfyb8dal
from s0aq15o2 import ky20479t
from jpj8t22c import w89uzfk8
from nnnkm95d import pllkstn3
class yr5uqpgb(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def qxt6ridl(self):
  player=r0tvhhpb()
  onqyyf9r=mfyb8dal('r6q37c',player.npcxa5s0.centerx,player.npcxa5s0.centery)
  onqyyf9r.g11kerpe=0
  self.assertEqual(player.cqheyto5,[])
  onqyyf9r.vvslh9bh(player)
  self.assertEqual(len(player.cqheyto5),1)
  (x,y,awnwlc83,color)=player.cqheyto5[0]
  self.assertEqual(color,iq5c34dx['mviifr'])
  self.assertTrue(awnwlc83.startswith('-'))
 def s5r96khu(self):
  player=r0tvhhpb()
  ra73jgzl=ky20479t('fzeeqn',player.npcxa5s0.centerx,player.npcxa5s0.centery,6,6,1,0)
  ra73jgzl.wc7x0h3j=12
  ra73jgzl.vvslh9bh([],[],[],player=player,target='player')
  self.assertEqual(len(player.cqheyto5),1)
  self.assertEqual(player.cqheyto5[0][3],iq5c34dx['mviifr'])
 def kn5gjj8m(self):
  player=r0tvhhpb()
  d1ieixwc=mfyb8dal('uu3bfx',player.npcxa5s0.centerx+5,player.npcxa5s0.centery)
  d1ieixwc.g11kerpe=0
  d1ieixwc.vvslh9bh(player)
  for t1w1ht7p in range(d1ieixwc.arjn2hz2-1):
   d1ieixwc.vvslh9bh(player)
  self.assertEqual(player.cqheyto5,[])
  d1ieixwc.vvslh9bh(player)
  self.assertEqual(len(player.cqheyto5),1)
  self.assertEqual(player.cqheyto5[0][3],iq5c34dx['mviifr'])
 def o9zqyahu(self):
  player=r0tvhhpb()
  dzsedfqs=mfyb8dal('ga1arr',player.npcxa5s0.centerx+5,player.npcxa5s0.centery)
  dzsedfqs.arhnuxor=0
  dzsedfqs.move(player)
  pllkstn3([dzsedfqs],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.cqheyto5),1)
  self.assertEqual(player.cqheyto5[0][3],iq5c34dx['mviifr'])
 def ejbzutru(self):
  player=r0tvhhpb()
  onqyyf9r=mfyb8dal('r6q37c',player.npcxa5s0.centerx,player.npcxa5s0.centery)
  onqyyf9r.g11kerpe=0
  f55dmcxx=player.arhnuxor
  onqyyf9r.vvslh9bh(player)
  dw7nh8rq=f55dmcxx-player.arhnuxor
  (t1w1ht7p,t1w1ht7p,awnwlc83,t1w1ht7p)=player.cqheyto5[0]
  self.assertEqual(awnwlc83,f'-{int(dw7nh8rq)}')
 def mlikwe4b(self):
  onqyyf9r=mfyb8dal('r6q37c',100,100)
  ugez7bh2=ky20479t('gzyt91',onqyyf9r.npcxa5s0.centerx,onqyyf9r.npcxa5s0.centery,6,6,1,0)
  nubmxnsz=[onqyyf9r]
  self.assertEqual(onqyyf9r.cqheyto5,[])
  ugez7bh2.vvslh9bh(nubmxnsz,[],[])
  self.assertEqual(len(onqyyf9r.cqheyto5),1)
  (x,y,awnwlc83,color)=onqyyf9r.cqheyto5[0]
  self.assertEqual(color,iq5c34dx['l4f9ye'])
  self.assertTrue(awnwlc83.startswith('-'))
 def klkjxjq5(self):
  xasez2nx=mfyb8dal('r6q37c',100,100)
  w8wj0uun=mfyb8dal('r6q37c',120,100)
  nubmxnsz=[xasez2nx,w8wj0uun]
  f32ejx5t=ky20479t('gyjckt',xasez2nx.npcxa5s0.centerx,xasez2nx.npcxa5s0.centery,10,10,1,0)
  f32ejx5t.vvslh9bh(nubmxnsz,[],[])
  self.assertEqual(len(w8wj0uun.cqheyto5),1)
  self.assertEqual(w8wj0uun.cqheyto5[0][3],iq5c34dx['l4f9ye'])
class pecruyf3(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def guxt9kls(self):
  zqcootnj=mfyb8dal('m44c68',100,100)
  zqcootnj.npcxa5s0.width=zqcootnj.npcxa5s0.height=60
  ugez7bh2=ky20479t('kqbrmq',zqcootnj.npcxa5s0.centerx,zqcootnj.npcxa5s0.centery,4,4,0.01,0)
  xd8wz42o=0
  for t1w1ht7p in range(10):
   ugez7bh2.move(zqcootnj)
   f55dmcxx=zqcootnj.arhnuxor
   ugez7bh2.vvslh9bh([zqcootnj],[],[])
   if zqcootnj.arhnuxor<f55dmcxx:
    xd8wz42o+=1
   if ugez7bh2.x875aud9:
    break
  self.assertEqual(xd8wz42o,1)
  self.assertEqual(ugez7bh2.nfn1r4kz,1)
 def r212pgym(self):
  nubmxnsz=[mfyb8dal('r6q37c',100+nyrid3dn*5,100)for nyrid3dn in range(4)]
  ugez7bh2=ky20479t('kqbrmq',100,100,30,30,1,0)
  ugez7bh2.vvslh9bh(nubmxnsz,[],[])
  self.assertEqual(len(ugez7bh2.swwnc21o),ugez7bh2.wgcl9lcq,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(ugez7bh2.x875aud9)
class mqp49kwv(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def njka34mq(self):
  player=r0tvhhpb()
  onqyyf9r=mfyb8dal('r6q37c',player.npcxa5s0.centerx,player.npcxa5s0.centery)
  onqyyf9r.g11kerpe=0
  self.assertFalse(player.qcd81twh)
  onqyyf9r.vvslh9bh(player)
  self.assertTrue(player.qcd81twh)
  self.assertEqual(player.u15pdtz9,s8qjnv8z)
 def bsp7bm41(self):
  player=r0tvhhpb()
  ra73jgzl=ky20479t('fzeeqn',player.npcxa5s0.centerx,player.npcxa5s0.centery,6,6,1,0)
  self.assertFalse(player.qcd81twh)
  ra73jgzl.vvslh9bh([],[],[],player=player,target='player')
  self.assertTrue(player.qcd81twh)
class azebbk7w(unittest.TestCase):
 def f2voi8uy(self):
  player=r0tvhhpb()
  eohswq40=w89uzfk8(player.npcxa5s0.x,player.npcxa5s0.y,50)
  w2sq3b9s=player.x3zo7utx
  eohswq40.move(player)
  self.assertTrue(eohswq40.x875aud9)
  self.assertEqual(player.x3zo7utx,w2sq3b9s+50)
class gl08yg0j(unittest.TestCase):
 def gf8f3gr9(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=r0tvhhpb()
  nd6357oo=ky20479t('za5ivr',player.npcxa5s0.centerx-250,player.npcxa5s0.centery,20,27,1,0)
  nd6357oo.d5ixva1n=True
  nd6357oo.g8kk791z=nd6357oo.m8lw2qit+1
  h4l1vznq=None
  for m20u9isy in range(nd6357oo.qo6q0usw):
   player.npcxa5s0.x+=player.p7b1ijiy
   nd6357oo.move(player)
   if nd6357oo.x875aud9:
    h4l1vznq=m20u9isy
    break
  self.assertIsNotNone(h4l1vznq,'boomerang never caught up to the player')
  self.assertLess(h4l1vznq,nd6357oo.qo6q0usw-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
