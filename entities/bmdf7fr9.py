import pygame
import math
from i1arxabo import*
from.lhkgad7x import f935a0l7
class if8mdd4v(f935a0l7):
 def __init__(self,mygfliji,htgsiwg0,hhl1737s):
  super().__init__(mygfliji,htgsiwg0,hhl1737s)
  byl68ntk=k1wj0tpa[mygfliji]
  self.u15pdtz9=byl68ntk['edxoq2']
  self.q3n2qb6g=byl68ntk['l4f9ye']
  self.qcd81twh=byl68ntk['cxf5x9']
  self.wgcl9lcq=byl68ntk['e56waf']
  self.k3z6bz8u=byl68ntk['edxoq2']
  self.gxlk8wru='hidden'
  self.y9ayq6ww=self.q3n2qb6g
 def win4olr6(self):
  self.y9ayq6ww-=1
  if self.y9ayq6ww<=0:
   if self.gxlk8wru=='hidden':
    self.gxlk8wru='revealing'
    self.y9ayq6ww=self.wgcl9lcq
   elif self.gxlk8wru=='revealing':
    self.gxlk8wru='visible'
    self.y9ayq6ww=self.qcd81twh
   else:
    self.gxlk8wru='hidden'
    self.y9ayq6ww=self.q3n2qb6g
  self.k3z6bz8u=self.u15pdtz9 if self.gxlk8wru=='hidden'else 255
 def mcup8ijl(self,player):
  if self.mpyxdw2z<=0:
   self.k7zgf9q5=True
   return
  self.win4olr6()
  if self.gxlk8wru=='visible'and abs(player.todsx4nx.htgsiwg0-self.todsx4nx.htgsiwg0)<cawudtse and(abs(player.todsx4nx.hhl1737s-self.todsx4nx.hhl1737s)<cawudtse):
   self.on0jnwny(player)
   return
  g8kk791z=player.todsx4nx.htgsiwg0-self.todsx4nx.htgsiwg0
  wzlm72je=player.todsx4nx.hhl1737s-self.todsx4nx.hhl1737s
  cnqt3wve=math.hypot(g8kk791z,wzlm72je)
  if cnqt3wve==0:
   return
  i33e1i1p=g8kk791z/cnqt3wve
  x9h0dxho=wzlm72je/cnqt3wve
  if i33e1i1p!=0 and x9h0dxho!=0:
   i33e1i1p*=0.707
   x9h0dxho*=0.707
  self.todsx4nx.htgsiwg0+=i33e1i1p*self.mn89ltaj
  self.todsx4nx.hhl1737s+=x9h0dxho*self.mn89ltaj
  self.todsx4nx.htgsiwg0=round(self.todsx4nx.htgsiwg0)
  self.todsx4nx.hhl1737s=round(self.todsx4nx.hhl1737s)
 def sl65wvjx(self,tj0nmeoq,uysal8m1,giec4d14):
  htgsiwg0=self.todsx4nx.htgsiwg0-uysal8m1
  hhl1737s=self.todsx4nx.hhl1737s-giec4d14
  wi8skch8=self.todsx4nx.centerx-uysal8m1
  iektsg7f=self.todsx4nx.centery-giec4d14
  if self.k3z6bz8u>=255:
   self.v83tqll8(tj0nmeoq,htgsiwg0,hhl1737s,wi8skch8,iektsg7f)
   return
  wa45hvgo=24
  q6nqqb9l=pygame.Surface((self.todsx4nx.width+wa45hvgo*2,self.todsx4nx.height+wa45hvgo*2),pygame.SRCALPHA)
  (je11e9ft,avfmh07w)=(wa45hvgo,wa45hvgo)
  (nd31k9qm,cp91i3vm)=(je11e9ft+self.todsx4nx.width//2,avfmh07w+self.todsx4nx.height//2)
  self.v83tqll8(q6nqqb9l,je11e9ft,avfmh07w,nd31k9qm,cp91i3vm)
  q6nqqb9l.set_alpha(self.k3z6bz8u)
  tj0nmeoq.blit(q6nqqb9l,(htgsiwg0-wa45hvgo,hhl1737s-wa45hvgo))
