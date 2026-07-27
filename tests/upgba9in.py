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
from i1arxabo import khl1n13j,iq5c34dx,k1wj0tpa
from entities import yur7ko64,lztkkfzz
from riyojtpk import r0tvhhpb
from nvxjj2jv import w89uzfk8
from tbzegbl2 import no0u93mz
class gl08yg0j(unittest.TestCase):
 """Same pattern as TestScreenShake: damage-dealing code can't reach a
    `toasts` list directly without threading it through every attack()/
    on_death() signature, so pending entries are queued on `player` (which
    every attacker already has) and drained once per frame in main.py."""
 def d0qzfhom(self):
  player=yur7ko64()
  atj9a3y3=lztkkfzz('uk99jc',player.todsx4nx.centerx,player.todsx4nx.centery)
  atj9a3y3.pa5u6hc3=0
  self.assertEqual(player.lgbpj4uf,[])
  atj9a3y3.on0jnwny(player)
  self.assertEqual(len(player.lgbpj4uf),1)
  (htgsiwg0,hhl1737s,o9zqyahu,color)=player.lgbpj4uf[0]
  self.assertEqual(color,iq5c34dx['w65dlx'])
  self.assertTrue(o9zqyahu.startswith('-'))
 def l3m25a5p(self):
  player=yur7ko64()
  yx4w6xlp=r0tvhhpb('s7002g',player.todsx4nx.centerx,player.todsx4nx.centery,6,6,1,0)
  yx4w6xlp.vw6m7b5c=12
  yx4w6xlp.on0jnwny([],[],[],player=player,target='player')
  self.assertEqual(len(player.lgbpj4uf),1)
  self.assertEqual(player.lgbpj4uf[0][3],iq5c34dx['w65dlx'])
 def nabufwbu(self):
  player=yur7ko64()
  divsolml=lztkkfzz('btjopz',player.todsx4nx.centerx+5,player.todsx4nx.centery)
  divsolml.pa5u6hc3=0
  divsolml.on0jnwny(player)
  for ygspk9p3 in range(divsolml.p7b1ijiy-1):
   divsolml.on0jnwny(player)
  self.assertEqual(player.lgbpj4uf,[])
  divsolml.on0jnwny(player)
  self.assertEqual(len(player.lgbpj4uf),1)
  self.assertEqual(player.lgbpj4uf[0][3],iq5c34dx['w65dlx'])
 def holeyrvx(self):
  player=yur7ko64()
  vvslh9bh=lztkkfzz('ktfshb',player.todsx4nx.centerx+5,player.todsx4nx.centery)
  vvslh9bh.mpyxdw2z=0
  vvslh9bh.mcup8ijl(player)
  no0u93mz([vvslh9bh],[],[],player,[],[],pygame.font.SysFont('arial',15))
  self.assertEqual(len(player.lgbpj4uf),1)
  self.assertEqual(player.lgbpj4uf[0][3],iq5c34dx['w65dlx'])
 def bsp7bm41(self):
  player=yur7ko64()
  atj9a3y3=lztkkfzz('uk99jc',player.todsx4nx.centerx,player.todsx4nx.centery)
  atj9a3y3.pa5u6hc3=0
  vmxb9yo1=player.mpyxdw2z
  atj9a3y3.on0jnwny(player)
  elwf90km=vmxb9yo1-player.mpyxdw2z
  (ygspk9p3,ygspk9p3,o9zqyahu,ygspk9p3)=player.lgbpj4uf[0]
  self.assertEqual(o9zqyahu,f'-{int(elwf90km)}')
 def rr9u1oe5(self):
  atj9a3y3=lztkkfzz('uk99jc',100,100)
  jc54wsqt=r0tvhhpb('xutxzb',atj9a3y3.todsx4nx.centerx,atj9a3y3.todsx4nx.centery,6,6,1,0)
  uc1xi04b=[atj9a3y3]
  self.assertEqual(atj9a3y3.lgbpj4uf,[])
  jc54wsqt.on0jnwny(uc1xi04b,[],[])
  self.assertEqual(len(atj9a3y3.lgbpj4uf),1)
  (htgsiwg0,hhl1737s,o9zqyahu,color)=atj9a3y3.lgbpj4uf[0]
  self.assertEqual(color,iq5c34dx['m314cq'])
  self.assertTrue(o9zqyahu.startswith('-'))
 def az2ueaxy(self):
  y8dd2255=lztkkfzz('uk99jc',100,100)
  stv18kgy=lztkkfzz('uk99jc',120,100)
  uc1xi04b=[y8dd2255,stv18kgy]
  nrpj1epk=r0tvhhpb('da5xin',y8dd2255.todsx4nx.centerx,y8dd2255.todsx4nx.centery,10,10,1,0)
  nrpj1epk.on0jnwny(uc1xi04b,[],[])
  self.assertEqual(len(stv18kgy.lgbpj4uf),1)
  self.assertEqual(stv18kgy.lgbpj4uf[0][3],iq5c34dx['m314cq'])
class s9skdgig(unittest.TestCase):
 """Regression: the enemy-collision loop had no memory of who it had
    already hit, so a bullet that stayed overlapping one enemy across
    several frames (slow relative to the target, or an oversized target)
    burned its whole pierce allowance on that single enemy instead of
    passing through to new ones."""
 def yypp5zp7(self):
  x875aud9=lztkkfzz('umfbuv',100,100)
  x875aud9.todsx4nx.width=x875aud9.todsx4nx.height=60
  jc54wsqt=r0tvhhpb('nk7y6q',x875aud9.todsx4nx.centerx,x875aud9.todsx4nx.centery,4,4,0.01,0)
  xqzpky32=0
  for ygspk9p3 in range(10):
   jc54wsqt.mcup8ijl(x875aud9)
   vmxb9yo1=x875aud9.mpyxdw2z
   jc54wsqt.on0jnwny([x875aud9],[],[])
   if x875aud9.mpyxdw2z<vmxb9yo1:
    xqzpky32+=1
   if jc54wsqt.k7zgf9q5:
    break
  self.assertEqual(xqzpky32,1)
  self.assertEqual(jc54wsqt.fp47b42g,1)
 def s5r96khu(self):
  uc1xi04b=[lztkkfzz('uk99jc',100+jo8e7flq*5,100)for jo8e7flq in range(4)]
  jc54wsqt=r0tvhhpb('nk7y6q',100,100,30,30,1,0)
  jc54wsqt.on0jnwny(uc1xi04b,[],[])
  self.assertEqual(len(jc54wsqt.kkzruin3),jc54wsqt.m3pt5r5r,'should stop exactly at its pierce limit, even with more targets overlapping in one frame')
  self.assertTrue(jc54wsqt.k7zgf9q5)
class yr5uqpgb(unittest.TestCase):
 """Regression: `global shake, shakecd` inside Enemy.attack()/Projectile.attack()
    used to write to entities.py's/bullets.py's own module namespace, not
    main.py's local run_game() variables -- so shake never actually fired.
    State now lives on `player` instead, which every attacker already has."""
 def rwybow23(self):
  player=yur7ko64()
  atj9a3y3=lztkkfzz('uk99jc',player.todsx4nx.centerx,player.todsx4nx.centery)
  atj9a3y3.pa5u6hc3=0
  self.assertFalse(player.xu9ymszd)
  atj9a3y3.on0jnwny(player)
  self.assertTrue(player.xu9ymszd)
  self.assertEqual(player.v0rxxf36,khl1n13j)
 def hcxhgnze(self):
  player=yur7ko64()
  yx4w6xlp=r0tvhhpb('s7002g',player.todsx4nx.centerx,player.todsx4nx.centery,6,6,1,0)
  self.assertFalse(player.xu9ymszd)
  yx4w6xlp.on0jnwny([],[],[],player=player,target='player')
  self.assertTrue(player.xu9ymszd)
class lp0lzjje(unittest.TestCase):
 def v7g0iiji(self):
  player=yur7ko64()
  f2sehe2a=w89uzfk8(player.todsx4nx.htgsiwg0,player.todsx4nx.hhl1737s,50)
  zgomf9pm=player.n01uyzpd
  f2sehe2a.mcup8ijl(player)
  self.assertTrue(f2sehe2a.k7zgf9q5)
  self.assertEqual(player.n01uyzpd,zgomf9pm+50)
class gdzr1yxr(unittest.TestCase):
 def nv23gxj0(self):
  """Regression: the old return logic moved at a fixed world-space
        speed and composed movement before checking distance, so a player
        moving at a comparable speed could never actually be caught --
        the boomerang only ever 'died' when its lifetime ran out."""
  player=yur7ko64()
  g11kerpe=r0tvhhpb('x981ud',player.todsx4nx.centerx-250,player.todsx4nx.centery,20,27,1,0)
  g11kerpe.njka34mq=True
  g11kerpe.ep6beffl=g11kerpe.xuu13i59+1
  ljk4q5v7=None
  for kx74d0gj in range(g11kerpe.n3rlkte4):
   player.todsx4nx.htgsiwg0+=player.mn89ltaj
   g11kerpe.mcup8ijl(player)
   if g11kerpe.k7zgf9q5:
    ljk4q5v7=kx74d0gj
    break
  self.assertIsNotNone(ljk4q5v7,'boomerang never caught up to the player')
  self.assertLess(ljk4q5v7,g11kerpe.n3rlkte4-5,'boomerang only died from lifetime expiry, not from actually catching up')
if __name__=='__main__':
 unittest.main()
