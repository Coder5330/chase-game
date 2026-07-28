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
from entfk7or import s8qjnv8z,iq5c34dx,k1wj0tpa
from entities import r0tvhhpb,yuibrsz1
from k0b8y5dn import ky20479t
from kier7u8h import w89uzfk8
from kc81do6o import pllkstn3
class yr5uqpgb(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def njka34mq(self):
  player=r0tvhhpb()
  zpajssuu=yuibrsz1('fv51zl',player.npcxa5s0.centerx,player.npcxa5s0.centery)
  zpajssuu.vvslh9bh=0
  self.assertEqual(player.cqheyto5,[])
  zpajssuu.nrpj1epk(player)
  self.assertEqual(len(player.cqheyto5),1)
  (w2sq3b9s,owdz09wf,gsrtwlxd,color)=player.cqheyto5[0]
  self.assertEqual(color,iq5c34dx['og8cd3'])
  self.assertTrue(gsrtwlxd.startswith('-'))
 def bsp7bm41(self):
  player=r0tvhhpb()
  ykipu1wy=ky20479t('x1qwee',player.npcxa5s0.centerx,player.npcxa5s0.centery,6,6,1,0)
  ykipu1wy.vt6om1fb=12
  ykipu1wy.nrpj1epk([],[],[],player=player,target='player')
  self.assertEqual(len(player.cqheyto5),1)
  self.assertEqual(player.cqheyto5[0][3],iq5c34dx['og8cd3'])
 def frhzn4kg(self):
  player=r0tvhhpb()
  tacj4t0s=yuibrsz1('l7dknn',player.npcxa5s0.centerx+5,player.npcxa5s0.centery)
  tacj4t0s.vvslh9bh=0
  tacj4t0s.nrpj1epk(player)
  for t1w1ht7p in range(tacj4t0s.n8sa3idy-1):
   tacj4t0s.nrpj1epk(player)
  self.assertEqual(player.cqheyto5,[])
  tacj4t0s.nrpj1epk(player)
  self.assertEqual(len(player.cqheyto5),1)
  self.assertEqual(player.cqheyto5[0][3],iq5c34dx['og8cd3'])
 def kn5gjj8m(self):
  player=r0tvhhpb()
  f32ejx5t=yuibrsz1('bfbuvl',player.npcxa5s0.centerx+5,player.npcxa5s0.centery)
  f32ejx5t.ftrflqbm=0
  f32ejx5t.oc4kl8cg(player)
  pllkstn3([f32ejx5t],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.cqheyto5),1)
  self.assertEqual(player.cqheyto5[0][3],iq5c34dx['og8cd3'])
 def rm0j36tc(self):
  player=r0tvhhpb()
  zpajssuu=yuibrsz1('fv51zl',player.npcxa5s0.centerx,player.npcxa5s0.centery)
  zpajssuu.vvslh9bh=0
  fpa8hyex=player.ftrflqbm
  zpajssuu.nrpj1epk(player)
  velos6zl=fpa8hyex-player.ftrflqbm
  (t1w1ht7p,t1w1ht7p,gsrtwlxd,t1w1ht7p)=player.cqheyto5[0]
  self.assertEqual(gsrtwlxd,f'-{int(velos6zl)}')
 def vm65q57t(self):
  zpajssuu=yuibrsz1('fv51zl',100,100)
  ebt3g2qz=ky20479t('kqbrmq',zpajssuu.npcxa5s0.centerx,zpajssuu.npcxa5s0.centery,6,6,1,0)
  qhkc856w=[zpajssuu]
  self.assertEqual(zpajssuu.cqheyto5,[])
  ebt3g2qz.nrpj1epk(qhkc856w,[],[])
  self.assertEqual(len(zpajssuu.cqheyto5),1)
  (w2sq3b9s,owdz09wf,gsrtwlxd,color)=zpajssuu.cqheyto5[0]
  self.assertEqual(color,iq5c34dx['mmgvu4'])
  self.assertTrue(gsrtwlxd.startswith('-'))
 def l0sqg4ei(self):
  xasez2nx=yuibrsz1('fv51zl',100,100)
  mnx4sn6s=yuibrsz1('fv51zl',120,100)
  qhkc856w=[xasez2nx,mnx4sn6s]
  gn89qkns=ky20479t('r6q37c',xasez2nx.npcxa5s0.centerx,xasez2nx.npcxa5s0.centery,10,10,1,0)
  gn89qkns.nrpj1epk(qhkc856w,[],[])
  self.assertEqual(len(mnx4sn6s.cqheyto5),1)
  self.assertEqual(mnx4sn6s.cqheyto5[0][3],iq5c34dx['mmgvu4'])
class pecruyf3(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def y06nkwfg(self):
  nfn1r4kz=yuibrsz1('l4f9ye',100,100)
  nfn1r4kz.npcxa5s0.width=nfn1r4kz.npcxa5s0.height=60
  ebt3g2qz=ky20479t('cm3v2p',nfn1r4kz.npcxa5s0.centerx,nfn1r4kz.npcxa5s0.centery,4,4,0.01,0)
  xk7n8la1=0
  for t1w1ht7p in range(10):
   ebt3g2qz.oc4kl8cg(nfn1r4kz)
   fpa8hyex=nfn1r4kz.ftrflqbm
   ebt3g2qz.nrpj1epk([nfn1r4kz],[],[])
   if nfn1r4kz.ftrflqbm<fpa8hyex:
    xk7n8la1+=1
   if ebt3g2qz.fp47b42g:
    break
  self.assertEqual(xk7n8la1,1)
  self.assertEqual(ebt3g2qz.nubmxnsz,1)
 def ejbzutru(self):
  qhkc856w=[yuibrsz1('fv51zl',100+pcvsqame*5,100)for pcvsqame in range(4)]
  ebt3g2qz=ky20479t('cm3v2p',100,100,30,30,1,0)
  ebt3g2qz.nrpj1epk(qhkc856w,[],[])
  self.assertEqual(len(ebt3g2qz.w5iz31yr),ebt3g2qz.wgcl9lcq,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(ebt3g2qz.fp47b42g)
class mqp49kwv(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def ayr1k12v(self):
  player=r0tvhhpb()
  zpajssuu=yuibrsz1('fv51zl',player.npcxa5s0.centerx,player.npcxa5s0.centery)
  zpajssuu.vvslh9bh=0
  self.assertFalse(player.qcd81twh)
  zpajssuu.nrpj1epk(player)
  self.assertTrue(player.qcd81twh)
  self.assertEqual(player.u15pdtz9,s8qjnv8z)
 def o9zqyahu(self):
  player=r0tvhhpb()
  ykipu1wy=ky20479t('x1qwee',player.npcxa5s0.centerx,player.npcxa5s0.centery,6,6,1,0)
  self.assertFalse(player.qcd81twh)
  ykipu1wy.nrpj1epk([],[],[],player=player,target='player')
  self.assertTrue(player.qcd81twh)
class azebbk7w(unittest.TestCase):
 def wvndfdw7(self):
  player=r0tvhhpb()
  mfyb8dal=w89uzfk8(player.npcxa5s0.w2sq3b9s,player.npcxa5s0.owdz09wf,50)
  j1kfk7y6=player.m9bn18gp
  mfyb8dal.oc4kl8cg(player)
  self.assertTrue(mfyb8dal.fp47b42g)
  self.assertEqual(player.m9bn18gp,j1kfk7y6+50)
class gl08yg0j(unittest.TestCase):
 def usz2kuuo(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=r0tvhhpb()
  dzsedfqs=ky20479t('cbpgyv',player.npcxa5s0.centerx-250,player.npcxa5s0.centery,20,27,1,0)
  dzsedfqs.jslulzfy=True
  dzsedfqs.rmm1zxyv=dzsedfqs.x9bp4m18+1
  h4l1vznq=None
  for damdvlnk in range(dzsedfqs.hp89fkbi):
   player.npcxa5s0.w2sq3b9s+=player.q6nqqb9l
   dzsedfqs.oc4kl8cg(player)
   if dzsedfqs.fp47b42g:
    h4l1vznq=damdvlnk
    break
  self.assertIsNotNone(h4l1vznq,'boomerang never caught up to the player')
  self.assertLess(h4l1vznq,dzsedfqs.hp89fkbi-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
