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
from o100vhmy import yur7ko64,iq5c34dx,k1wj0tpa
from entities import rqf5q14j,uos0fb4y
from zuw6taq6 import yswjckjl
from xk2jwuux import w89uzfk8
from ez6us7rp import cknfu84x
class gmjkv5us(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def qy3vg6v5(self):
  player=rqf5q14j()
  eatvzkhi=uos0fb4y('f9w9pf',player.zflse45b.centerx,player.zflse45b.centery)
  eatvzkhi.lt63j3r3=0
  self.assertEqual(player.mmn32u1i,[])
  eatvzkhi.sne6loh2(player)
  self.assertEqual(len(player.mmn32u1i),1)
  (rm0j36tc,tza7x73q,mu118qqv,color)=player.mmn32u1i[0]
  self.assertEqual(color,iq5c34dx['wxgnrf'])
  self.assertTrue(mu118qqv.startswith('-'))
 def rh0w064w(self):
  player=rqf5q14j()
  sk8yqk94=yswjckjl('c88d0t',player.zflse45b.centerx,player.zflse45b.centery,6,6,1,0)
  sk8yqk94.ruq9e5co=12
  sk8yqk94.sne6loh2([],[],[],player=player,target='player')
  self.assertEqual(len(player.mmn32u1i),1)
  self.assertEqual(player.mmn32u1i[0][3],iq5c34dx['wxgnrf'])
 def qdnai89y(self):
  player=rqf5q14j()
  g11kerpe=uos0fb4y('qe6a9h',player.zflse45b.centerx+5,player.zflse45b.centery)
  g11kerpe.lt63j3r3=0
  g11kerpe.sne6loh2(player)
  for dtx63cfl in range(g11kerpe.hdw6lqwl-1):
   g11kerpe.sne6loh2(player)
  self.assertEqual(player.mmn32u1i,[])
  g11kerpe.sne6loh2(player)
  self.assertEqual(len(player.mmn32u1i),1)
  self.assertEqual(player.mmn32u1i[0][3],iq5c34dx['wxgnrf'])
 def u1ni10kq(self):
  player=rqf5q14j()
  kmgfxc08=uos0fb4y('k4ow3l',player.zflse45b.centerx+5,player.zflse45b.centery)
  kmgfxc08.q7i6yuj7=0
  kmgfxc08.j1ldqnk2(player)
  cknfu84x([kmgfxc08],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.mmn32u1i),1)
  self.assertEqual(player.mmn32u1i[0][3],iq5c34dx['wxgnrf'])
 def k82853uy(self):
  player=rqf5q14j()
  eatvzkhi=uos0fb4y('f9w9pf',player.zflse45b.centerx,player.zflse45b.centery)
  eatvzkhi.lt63j3r3=0
  kkzruin3=player.q7i6yuj7
  eatvzkhi.sne6loh2(player)
  pa8s8hmb=kkzruin3-player.q7i6yuj7
  (dtx63cfl,dtx63cfl,mu118qqv,dtx63cfl)=player.mmn32u1i[0]
  self.assertEqual(mu118qqv,f'-{int(pa8s8hmb)}')
 def k7vcneas(self):
  eatvzkhi=uos0fb4y('f9w9pf',100,100)
  u3ifhv1x=yswjckjl('jy66p6',eatvzkhi.zflse45b.centerx,eatvzkhi.zflse45b.centery,6,6,1,0)
  wzlm72je=[eatvzkhi]
  self.assertEqual(eatvzkhi.mmn32u1i,[])
  u3ifhv1x.sne6loh2(wzlm72je,[],[])
  self.assertEqual(len(eatvzkhi.mmn32u1i),1)
  (rm0j36tc,tza7x73q,mu118qqv,color)=eatvzkhi.mmn32u1i[0]
  self.assertEqual(color,iq5c34dx['ldz09w'])
  self.assertTrue(mu118qqv.startswith('-'))
 def bf7so8w5(self):
  lgbpj4uf=uos0fb4y('f9w9pf',100,100)
  vmy9x8sy=uos0fb4y('f9w9pf',120,100)
  wzlm72je=[lgbpj4uf,vmy9x8sy]
  ra73jgzl=yswjckjl('n1eeur',lgbpj4uf.zflse45b.centerx,lgbpj4uf.zflse45b.centery,10,10,1,0)
  ra73jgzl.sne6loh2(wzlm72je,[],[])
  self.assertEqual(len(vmy9x8sy.mmn32u1i),1)
  self.assertEqual(vmy9x8sy.mmn32u1i[0][3],iq5c34dx['ldz09w'])
class gdzr1yxr(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def hcxhgnze(self):
  wc7x0h3j=uos0fb4y('uq0e27',100,100)
  wc7x0h3j.zflse45b.width=wc7x0h3j.zflse45b.height=60
  u3ifhv1x=yswjckjl('xj2dg1',wc7x0h3j.zflse45b.centerx,wc7x0h3j.zflse45b.centery,4,4,0.01,0)
  fekrcppr=0
  for dtx63cfl in range(10):
   u3ifhv1x.j1ldqnk2(wc7x0h3j)
   kkzruin3=wc7x0h3j.q7i6yuj7
   u3ifhv1x.sne6loh2([wc7x0h3j],[],[])
   if wc7x0h3j.q7i6yuj7<kkzruin3:
    fekrcppr+=1
   if u3ifhv1x.vw6m7b5c:
    break
  self.assertEqual(fekrcppr,1)
  self.assertEqual(u3ifhv1x.vt6om1fb,1)
 def gqoagsus(self):
  wzlm72je=[uos0fb4y('f9w9pf',100+nyfkjfpn*5,100)for nyfkjfpn in range(4)]
  u3ifhv1x=yswjckjl('xj2dg1',100,100,30,30,1,0)
  u3ifhv1x.sne6loh2(wzlm72je,[],[])
  self.assertEqual(len(u3ifhv1x.damdvlnk),u3ifhv1x.mfc79m96,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(u3ifhv1x.vw6m7b5c)
class lp0lzjje(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def rserev36(self):
  player=rqf5q14j()
  eatvzkhi=uos0fb4y('f9w9pf',player.zflse45b.centerx,player.zflse45b.centery)
  eatvzkhi.lt63j3r3=0
  self.assertFalse(player.qc06xq9j)
  eatvzkhi.sne6loh2(player)
  self.assertTrue(player.qc06xq9j)
  self.assertEqual(player.bdgbk2l0,yur7ko64)
 def su1hbj6t(self):
  player=rqf5q14j()
  sk8yqk94=yswjckjl('c88d0t',player.zflse45b.centerx,player.zflse45b.centery,6,6,1,0)
  self.assertFalse(player.qc06xq9j)
  sk8yqk94.sne6loh2([],[],[],player=player,target='player')
  self.assertTrue(player.qc06xq9j)
class oiqvnb4g(unittest.TestCase):
 def wigbiaf9(self):
  player=rqf5q14j()
  obc2nnuv=w89uzfk8(player.zflse45b.rm0j36tc,player.zflse45b.tza7x73q,50)
  awnwlc83=player.eq3tq1s0
  obc2nnuv.j1ldqnk2(player)
  self.assertTrue(obc2nnuv.vw6m7b5c)
  self.assertEqual(player.eq3tq1s0,awnwlc83+50)
class ozp08j3t(unittest.TestCase):
 def q6nqqb9l(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=rqf5q14j()
  c0hpmnz1=yswjckjl('huh17j',player.zflse45b.centerx-250,player.zflse45b.centery,20,27,1,0)
  c0hpmnz1.z7pwo6cm=True
  c0hpmnz1.cq6qdy4l=c0hpmnz1.mq7nc85e+1
  todsx4nx=None
  for boih5csk in range(c0hpmnz1.rktlzkj4):
   player.zflse45b.rm0j36tc+=player.k8qeoz0k
   c0hpmnz1.j1ldqnk2(player)
   if c0hpmnz1.vw6m7b5c:
    todsx4nx=boih5csk
    break
  self.assertIsNotNone(todsx4nx,'boomerang never caught up to the player')
  self.assertLess(todsx4nx,c0hpmnz1.rktlzkj4-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
