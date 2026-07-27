import pygame
import math
from i1arxabo import*
from.lhkgad7x import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,mygfliji,htgsiwg0,hhl1737s):
  super().__init__(mygfliji,htgsiwg0,hhl1737s)
  self.le9oe941=(0,1)
  self.zfb7r31q=False
  self.li9nb74x=0
  self.nd6357oo=18
 def jdqqzrlf(self,player):
  g8kk791z=player.todsx4nx.centerx-self.todsx4nx.centerx
  wzlm72je=player.todsx4nx.centery-self.todsx4nx.centery
  w5iz31yr=math.hypot(g8kk791z,wzlm72je)or 1
  self.le9oe941=(g8kk791z/w5iz31yr,wzlm72je/w5iz31yr)
  if self.zfb7r31q:
   self.li9nb74x-=1
   if self.li9nb74x<=0:
    self.zfb7r31q=False
    self.boih5csk(player)
   return True
  if abs(player.todsx4nx.htgsiwg0-self.todsx4nx.htgsiwg0)<b8cgvyie and abs(player.todsx4nx.hhl1737s-self.todsx4nx.hhl1737s)<b8cgvyie:
   if self.pa5u6hc3>0:
    self.pa5u6hc3-=1
    return True
   self.zfb7r31q=True
   self.li9nb74x=self.nd6357oo
   return True
  return False
 def boih5csk(self,player):
  self.pa5u6hc3=self.duhxid4n
  from riyojtpk import rpqk51fp
  wd6r30oj=uqjiujv6['s7002g']['eqkwqh']
  (g8kk791z,wzlm72je)=(player.todsx4nx.centerx-self.todsx4nx.centerx,player.todsx4nx.centery-self.todsx4nx.centery)
  yx4w6xlp=rpqk51fp('s7002g',self.todsx4nx.centerx-wd6r30oj//2,self.todsx4nx.centery-wd6r30oj//2,wd6r30oj,wd6r30oj,g8kk791z,wzlm72je)
  yx4w6xlp.vw6m7b5c=self.qbbz2sf6
  self.lt63j3r3.append(yx4w6xlp)
 def sl65wvjx(self,tj0nmeoq,uysal8m1,giec4d14):
  htgsiwg0=self.todsx4nx.htgsiwg0-uysal8m1
  hhl1737s=self.todsx4nx.hhl1737s-giec4d14
  wi8skch8=self.todsx4nx.centerx-uysal8m1
  iektsg7f=self.todsx4nx.centery-giec4d14
  self.v83tqll8(tj0nmeoq,htgsiwg0,hhl1737s,wi8skch8,iektsg7f)
  (yrivh6t1,mqxlm5q2)=self.le9oe941
  (gp6orsnc,zflse45b)=(-mqxlm5q2,yrivh6t1)
  (aqclpoxk,mal2w37d)=(wi8skch8+yrivh6t1*14,iektsg7f+mqxlm5q2*14)
  gf8f3gr9=(aqclpoxk+gp6orsnc*13-yrivh6t1*6,mal2w37d+zflse45b*13-mqxlm5q2*6)
  usz2kuuo=(aqclpoxk-gp6orsnc*13-yrivh6t1*6,mal2w37d-zflse45b*13-mqxlm5q2*6)
  j2vmcqbn=(aqclpoxk+yrivh6t1*6,mal2w37d+mqxlm5q2*6)
  pygame.draw.lines(tj0nmeoq,(110,70,30),False,[gf8f3gr9,j2vmcqbn,usz2kuuo],3)
  yuibrsz1=1-self.li9nb74x/self.nd6357oo if self.zfb7r31q else 0
  lhgk5bwi=(aqclpoxk-yrivh6t1*(3+yuibrsz1*10),mal2w37d-mqxlm5q2*(3+yuibrsz1*10))
  pygame.draw.line(tj0nmeoq,(225,225,215),gf8f3gr9,lhgk5bwi,2)
  pygame.draw.line(tj0nmeoq,(225,225,215),usz2kuuo,lhgk5bwi,2)
  if self.zfb7r31q:
   sne6loh2=(aqclpoxk+yrivh6t1*8,mal2w37d+mqxlm5q2*8)
   pygame.draw.line(tj0nmeoq,iq5c34dx['zucc1m'],lhgk5bwi,sne6loh2,3)
