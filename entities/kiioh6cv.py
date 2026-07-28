import pygame
import math
from v7bnhjw6 import*
from.e1gnfiue import f935a0l7
class qxaprpn6(f935a0l7):
 def __init__(self,gubmc97c,qic1l7dy,vsjchzjq):
  super().__init__(gubmc97c,qic1l7dy,vsjchzjq)
  self.qbbz2sf6=0
  self.elwf90km=0
  self.mabkae6a=0
 def gsrtwlxd(self,player):
  self.mabkae6a+=0.35*(self.xvzc7d2k/self.vvslh9bh if self.vvslh9bh else 1)
  sfu38gl2=k1wj0tpa[self.type]
  if self.elwf90km>0:
   self.elwf90km-=1
   if self.elwf90km<=0:
    self.xvzc7d2k=self.vvslh9bh
   return False
  if self.qbbz2sf6>0:
   self.qbbz2sf6-=1
   return False
  if abs(player.jenvg3kk.qic1l7dy-self.jenvg3kk.qic1l7dy)<sfu38gl2['zmygy0']and abs(player.jenvg3kk.vsjchzjq-self.jenvg3kk.vsjchzjq)<sfu38gl2['zmygy0']:
   self.xvzc7d2k=self.vvslh9bh*sfu38gl2['wurvqt']
   self.elwf90km=sfu38gl2['cm3v2p']
   self.qbbz2sf6=sfu38gl2['mviifr']
  return False
 def wc7x0h3j(self,gg7oq2zd,li9nb74x,zfb7r31q):
  qic1l7dy=self.jenvg3kk.qic1l7dy-li9nb74x
  vsjchzjq=self.jenvg3kk.vsjchzjq-zfb7r31q
  pa8s8hmb=self.jenvg3kk.centerx-li9nb74x
  pv4ykade=self.jenvg3kk.centery-zfb7r31q
  jq1ddpus=self.jenvg3kk.width//2
  x9bp4m18=vsjchzjq+self.jenvg3kk.height-3
  nyrid3dn=(25,25,25)
  je11e9ft=[(-1,-6,0),(-1,6,math.pi),(1,-6,math.pi),(1,6,0)]
  for(mn89ltaj,jo8e7flq,g5hcbbmh)in je11e9ft:
   su1hbj6t=math.sin(self.mabkae6a+g5hcbbmh)
   q5amln4p=max(0,su1hbj6t)*4
   onqyyf9r=(pa8s8hmb+mn89ltaj*jq1ddpus*0.7,pv4ykade+jo8e7flq)
   u0q0mftg=pa8s8hmb+mn89ltaj*(jq1ddpus+9)+su1hbj6t*3
   r98s4c3b=x9bp4m18-q5amln4p
   xk7n8la1=((onqyyf9r[0]+u0q0mftg)/2,(onqyyf9r[1]+r98s4c3b)/2-2)
   pygame.draw.line(gg7oq2zd,nyrid3dn,onqyyf9r,xk7n8la1,3)
   pygame.draw.line(gg7oq2zd,nyrid3dn,xk7n8la1,(u0q0mftg,r98s4c3b),3)
  self.wrbw2zla(gg7oq2zd,qic1l7dy,vsjchzjq,pa8s8hmb,pv4ykade)
