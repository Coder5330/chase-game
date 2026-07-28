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
from zfiblejg import s8qjnv8z,iq5c34dx,k1wj0tpa
from entities import r0tvhhpb,sl65wvjx
from uc6lbpj8 import ky20479t
from vnbnqbnx import w89uzfk8
from ok38p6fv import tbxf445c
class yr5uqpgb(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def qxt6ridl(self):
  player=r0tvhhpb()
  vmxb9yo1=sl65wvjx('lcf4mn',player.tby49e7e.centerx,player.tby49e7e.centery)
  vmxb9yo1.nrpj1epk=0
  self.assertEqual(player.ljk4q5v7,[])
  vmxb9yo1.sv5f1bcp(player)
  self.assertEqual(len(player.ljk4q5v7),1)
  (x3zo7utx,cjy62zee,awnwlc83,color)=player.ljk4q5v7[0]
  self.assertEqual(color,iq5c34dx['zmygy0'])
  self.assertTrue(awnwlc83.startswith('-'))
 def s5r96khu(self):
  player=r0tvhhpb()
  duhxid4n=ky20479t('s55ff1',player.tby49e7e.centerx,player.tby49e7e.centery,6,6,1,0)
  duhxid4n.wzlm72je=12
  duhxid4n.sv5f1bcp([],[],[],player=player,target='player')
  self.assertEqual(len(player.ljk4q5v7),1)
  self.assertEqual(player.ljk4q5v7[0][3],iq5c34dx['zmygy0'])
 def kn5gjj8m(self):
  player=r0tvhhpb()
  zfb7r31q=sl65wvjx('jvyv2g',player.tby49e7e.centerx+5,player.tby49e7e.centery)
  zfb7r31q.nrpj1epk=0
  zfb7r31q.sv5f1bcp(player)
  for t1w1ht7p in range(zfb7r31q.arjn2hz2-1):
   zfb7r31q.sv5f1bcp(player)
  self.assertEqual(player.ljk4q5v7,[])
  zfb7r31q.sv5f1bcp(player)
  self.assertEqual(len(player.ljk4q5v7),1)
  self.assertEqual(player.ljk4q5v7[0][3],iq5c34dx['zmygy0'])
 def o9zqyahu(self):
  player=r0tvhhpb()
  gn89qkns=sl65wvjx('rkw3hg',player.tby49e7e.centerx+5,player.tby49e7e.centery)
  gn89qkns.nvuprt77=0
  gn89qkns.mmn32u1i(player)
  tbxf445c([gn89qkns],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.ljk4q5v7),1)
  self.assertEqual(player.ljk4q5v7[0][3],iq5c34dx['zmygy0'])
 def ejbzutru(self):
  player=r0tvhhpb()
  vmxb9yo1=sl65wvjx('lcf4mn',player.tby49e7e.centerx,player.tby49e7e.centery)
  vmxb9yo1.nrpj1epk=0
  zmybd2qe=player.nvuprt77
  vmxb9yo1.sv5f1bcp(player)
  yjluujmi=zmybd2qe-player.nvuprt77
  (t1w1ht7p,t1w1ht7p,awnwlc83,t1w1ht7p)=player.ljk4q5v7[0]
  self.assertEqual(awnwlc83,f'-{int(yjluujmi)}')
 def mlikwe4b(self):
  vmxb9yo1=sl65wvjx('lcf4mn',100,100)
  amcixdu1=ky20479t('w1q8f6',vmxb9yo1.tby49e7e.centerx,vmxb9yo1.tby49e7e.centery,6,6,1,0)
  xuu13i59=[vmxb9yo1]
  self.assertEqual(vmxb9yo1.ljk4q5v7,[])
  amcixdu1.sv5f1bcp(xuu13i59,[],[])
  self.assertEqual(len(vmxb9yo1.ljk4q5v7),1)
  (x3zo7utx,cjy62zee,awnwlc83,color)=vmxb9yo1.ljk4q5v7[0]
  self.assertEqual(color,iq5c34dx['edxoq2'])
  self.assertTrue(awnwlc83.startswith('-'))
 def klkjxjq5(self):
  yg87oi0e=sl65wvjx('lcf4mn',100,100)
  w8wj0uun=sl65wvjx('lcf4mn',120,100)
  xuu13i59=[yg87oi0e,w8wj0uun]
  tk0qtl3q=ky20479t('k7rrbe',yg87oi0e.tby49e7e.centerx,yg87oi0e.tby49e7e.centery,10,10,1,0)
  tk0qtl3q.sv5f1bcp(xuu13i59,[],[])
  self.assertEqual(len(w8wj0uun.ljk4q5v7),1)
  self.assertEqual(w8wj0uun.ljk4q5v7[0][3],iq5c34dx['edxoq2'])
class pecruyf3(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def guxt9kls(self):
  nubmxnsz=sl65wvjx('hpvwzo',100,100)
  nubmxnsz.tby49e7e.width=nubmxnsz.tby49e7e.height=60
  amcixdu1=ky20479t('w2lx2t',nubmxnsz.tby49e7e.centerx,nubmxnsz.tby49e7e.centery,4,4,0.01,0)
  swwnc21o=0
  for t1w1ht7p in range(10):
   amcixdu1.mmn32u1i(nubmxnsz)
   zmybd2qe=nubmxnsz.nvuprt77
   amcixdu1.sv5f1bcp([nubmxnsz],[],[])
   if nubmxnsz.nvuprt77<zmybd2qe:
    swwnc21o+=1
   if amcixdu1.uc1xi04b:
    break
  self.assertEqual(swwnc21o,1)
  self.assertEqual(amcixdu1.qhkc856w,1)
 def r212pgym(self):
  xuu13i59=[sl65wvjx('lcf4mn',100+bokzixza*5,100)for bokzixza in range(4)]
  amcixdu1=ky20479t('w2lx2t',100,100,30,30,1,0)
  amcixdu1.sv5f1bcp(xuu13i59,[],[])
  self.assertEqual(len(amcixdu1.v3e1ocjx),amcixdu1.eehou6ql,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(amcixdu1.uc1xi04b)
class mqp49kwv(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def njka34mq(self):
  player=r0tvhhpb()
  vmxb9yo1=sl65wvjx('lcf4mn',player.tby49e7e.centerx,player.tby49e7e.centery)
  vmxb9yo1.nrpj1epk=0
  self.assertFalse(player.q3n2qb6g)
  vmxb9yo1.sv5f1bcp(player)
  self.assertTrue(player.q3n2qb6g)
  self.assertEqual(player.qcd81twh,s8qjnv8z)
 def bsp7bm41(self):
  player=r0tvhhpb()
  duhxid4n=ky20479t('s55ff1',player.tby49e7e.centerx,player.tby49e7e.centery,6,6,1,0)
  self.assertFalse(player.q3n2qb6g)
  duhxid4n.sv5f1bcp([],[],[],player=player,target='player')
  self.assertTrue(player.q3n2qb6g)
class azebbk7w(unittest.TestCase):
 def f2voi8uy(self):
  player=r0tvhhpb()
  yuibrsz1=w89uzfk8(player.tby49e7e.x3zo7utx,player.tby49e7e.cjy62zee,50)
  m9bn18gp=player.w2sq3b9s
  yuibrsz1.mmn32u1i(player)
  self.assertTrue(yuibrsz1.uc1xi04b)
  self.assertEqual(player.w2sq3b9s,m9bn18gp+50)
class gl08yg0j(unittest.TestCase):
 def gf8f3gr9(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=r0tvhhpb()
  f32ejx5t=ky20479t('bxb4y4',player.tby49e7e.centerx-250,player.tby49e7e.centery,20,27,1,0)
  f32ejx5t.d5ixva1n=True
  f32ejx5t.wehlxslg=f32ejx5t.mytn02yc+1
  ukshy8nb=None
  for jq1ddpus in range(f32ejx5t.a8ax40dt):
   player.tby49e7e.x3zo7utx+=player.p7b1ijiy
   f32ejx5t.mmn32u1i(player)
   if f32ejx5t.uc1xi04b:
    ukshy8nb=jq1ddpus
    break
  self.assertIsNotNone(ukshy8nb,'boomerang never caught up to the player')
  self.assertLess(ukshy8nb,f32ejx5t.a8ax40dt-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
