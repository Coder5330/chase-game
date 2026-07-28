import pygame
import math
from z4w1arag import*
from.bohxs75t import f935a0l7
class spbhsahx(f935a0l7):
 def __init__(self,b36htf4p,d5ixva1n,nngmx1gm):
  super().__init__(b36htf4p,d5ixva1n,nngmx1gm)
  self.qhkc856w=(0,1)
  self.amcixdu1=False
  self.z9toqw9j=0
  self.hugysm8t=18
 def ywcxz2ei(self,player):
  fo75rh8l=player.cqheyto5.centerx-self.cqheyto5.centerx
  uc1xi04b=player.cqheyto5.centery-self.cqheyto5.centery
  f55dmcxx=math.hypot(fo75rh8l,uc1xi04b)or 1
  self.qhkc856w=(fo75rh8l/f55dmcxx,uc1xi04b/f55dmcxx)
  if self.amcixdu1:
   self.z9toqw9j-=1
   if self.z9toqw9j<=0:
    self.amcixdu1=False
    self.vvbc2vyh(player)
   return True
  if abs(player.cqheyto5.d5ixva1n-self.cqheyto5.d5ixva1n)<b8cgvyie and abs(player.cqheyto5.nngmx1gm-self.cqheyto5.nngmx1gm)<b8cgvyie:
   if self.uva2ieuc>0:
    self.uva2ieuc-=1
    return True
   self.amcixdu1=True
   self.z9toqw9j=self.hugysm8t
   return True
  return False
 def vvbc2vyh(self,player):
  self.uva2ieuc=self.nrpj1epk
  from kyow8dt8 import rpqk51fp
  kz1uu7zy=uqjiujv6['t753ay']['pcs4ke']
  (fo75rh8l,uc1xi04b)=(player.cqheyto5.centerx-self.cqheyto5.centerx,player.cqheyto5.centery-self.cqheyto5.centery)
  pa5u6hc3=rpqk51fp('t753ay',self.cqheyto5.centerx-kz1uu7zy//2,self.cqheyto5.centery-kz1uu7zy//2,kz1uu7zy,kz1uu7zy,fo75rh8l,uc1xi04b)
  pa5u6hc3.k7zgf9q5=self.eohswq40
  self.reqy08p0.append(pa5u6hc3)
 def g8kk791z(self,cq2q4qer,f32ejx5t,dzsedfqs):
  d5ixva1n=self.cqheyto5.d5ixva1n-f32ejx5t
  nngmx1gm=self.cqheyto5.nngmx1gm-dzsedfqs
  l9enulqj=self.cqheyto5.centerx-f32ejx5t
  hfb85p86=self.cqheyto5.centery-dzsedfqs
  self.t1w1ht7p(cq2q4qer,d5ixva1n,nngmx1gm,l9enulqj,hfb85p86)
  (ao4izasn,tw76xato)=self.qhkc856w
  (todsx4nx,tkyrmjlj)=(-tw76xato,ao4izasn)
  (uww5wfcp,j2vmcqbn)=(l9enulqj+ao4izasn*14,hfb85p86+tw76xato*14)
  rb1s9dwd=(uww5wfcp+todsx4nx*13-ao4izasn*6,j2vmcqbn+tkyrmjlj*13-tw76xato*6)
  mlikwe4b=(uww5wfcp-todsx4nx*13-ao4izasn*6,j2vmcqbn-tkyrmjlj*13-tw76xato*6)
  i0x65muf=(uww5wfcp+ao4izasn*6,j2vmcqbn+tw76xato*6)
  pygame.draw.lines(cq2q4qer,(110,70,30),False,[rb1s9dwd,i0x65muf,mlikwe4b],3)
  wzlm72je=1-self.z9toqw9j/self.hugysm8t if self.amcixdu1 else 0
  s8438tgb=(uww5wfcp-ao4izasn*(3+wzlm72je*10),j2vmcqbn-tw76xato*(3+wzlm72je*10))
  pygame.draw.line(cq2q4qer,(225,225,215),rb1s9dwd,s8438tgb,2)
  pygame.draw.line(cq2q4qer,(225,225,215),mlikwe4b,s8438tgb,2)
  if self.amcixdu1:
   wkof8krd=(uww5wfcp+ao4izasn*8,j2vmcqbn+tw76xato*8)
   pygame.draw.line(cq2q4qer,iq5c34dx['rsjr0f'],s8438tgb,wkof8krd,3)
