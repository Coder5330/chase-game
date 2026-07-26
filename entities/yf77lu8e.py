import pygame
import math
from ygm55ff1 import*
from.qdq55it9 import zy0ifznb
class spbhsahx(zy0ifznb):
 def __init__(self,cnqt3wve,yypp5zp7,tjy1o2rn):
  super().__init__(cnqt3wve,yypp5zp7,tjy1o2rn)
  self.rmm1zxyv=(0,1)
  self.aqclpoxk=False
  self.rzs43c5b=0
  self.g11kerpe=18
 def svt8k06m(self,player):
  vw6m7b5c=player.zdan085r.centerx-self.zdan085r.centerx
  u1jhuwb6=player.zdan085r.centery-self.zdan085r.centery
  vmxb9yo1=math.hypot(vw6m7b5c,u1jhuwb6)or 1
  self.rmm1zxyv=(vw6m7b5c/vmxb9yo1,u1jhuwb6/vmxb9yo1)
  if self.aqclpoxk:
   self.rzs43c5b-=1
   if self.rzs43c5b<=0:
    self.aqclpoxk=False
    self.vt6om1fb(player)
   return True
  if abs(player.zdan085r.yypp5zp7-self.zdan085r.yypp5zp7)<sivwpvs7 and abs(player.zdan085r.tjy1o2rn-self.zdan085r.tjy1o2rn)<sivwpvs7:
   if self.wkzorqqf>0:
    self.wkzorqqf-=1
    return True
   self.aqclpoxk=True
   self.rzs43c5b=self.g11kerpe
   return True
  return False
 def vt6om1fb(self,player):
  self.wkzorqqf=self.x52qc1iy
  from cyrsvzn4 import rpqk51fp
  g1g1r1dw=uqjiujv6['fds22w']['mxhw0i']
  (vw6m7b5c,u1jhuwb6)=(player.zdan085r.centerx-self.zdan085r.centerx,player.zdan085r.centery-self.zdan085r.centery)
  v83tqll8=rpqk51fp('fds22w',self.zdan085r.centerx-g1g1r1dw//2,self.zdan085r.centery-g1g1r1dw//2,g1g1r1dw,g1g1r1dw,vw6m7b5c,u1jhuwb6)
  v83tqll8.tacj4t0s=self.x5m9j98c
  self.t1w1ht7p.append(v83tqll8)
 def izhwy9he(self,uj64qhks,ra73jgzl,kmgfxc08):
  yypp5zp7=self.zdan085r.yypp5zp7-ra73jgzl
  tjy1o2rn=self.zdan085r.tjy1o2rn-kmgfxc08
  nd6357oo=self.zdan085r.centerx-ra73jgzl
  li9nb74x=self.zdan085r.centery-kmgfxc08
  self.zakoixnt(uj64qhks,yypp5zp7,tjy1o2rn,nd6357oo,li9nb74x)
  (jqxs6esj,zefqjg02)=self.rmm1zxyv
  (wg25cfzf,d448n7od)=(-zefqjg02,jqxs6esj)
  (gp84dyt9,lcj883dh)=(nd6357oo+jqxs6esj*14,li9nb74x+zefqjg02*14)
  h8s2ftom=(gp84dyt9+wg25cfzf*13-jqxs6esj*6,lcj883dh+d448n7od*13-zefqjg02*6)
  gxlk8wru=(gp84dyt9-wg25cfzf*13-jqxs6esj*6,lcj883dh-d448n7od*13-zefqjg02*6)
  d0r2sds8=(gp84dyt9+jqxs6esj*6,lcj883dh+zefqjg02*6)
  pygame.draw.lines(uj64qhks,(110,70,30),False,[h8s2ftom,d0r2sds8,gxlk8wru],3)
  f2sehe2a=1-self.rzs43c5b/self.g11kerpe if self.aqclpoxk else 0
  b78okz1p=(gp84dyt9-jqxs6esj*(3+f2sehe2a*10),lcj883dh-zefqjg02*(3+f2sehe2a*10))
  pygame.draw.line(uj64qhks,(225,225,215),h8s2ftom,b78okz1p,2)
  pygame.draw.line(uj64qhks,(225,225,215),gxlk8wru,b78okz1p,2)
  if self.aqclpoxk:
   m53a5qbs=(gp84dyt9+jqxs6esj*8,lcj883dh+zefqjg02*8)
   pygame.draw.line(uj64qhks,iq5c34dx['eqvdjn'],b78okz1p,m53a5qbs,3)
