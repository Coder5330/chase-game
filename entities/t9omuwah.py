import pygame
import math
from rlfzkicw import*
from.o3ksgnbh import dmu5907i
class if8mdd4v(dmu5907i):
 def __init__(self,mfyb8dal,kn5gjj8m,lu7jae58):
  super().__init__(mfyb8dal,kn5gjj8m,lu7jae58)
  pllkstn3=isj6bw3b[mfyb8dal]
  self.ukshy8nb=pllkstn3['pta5iv']
  self.cq2q4qer=pllkstn3['jl1qwe']
  self.uaobt328=pllkstn3['e8a1ar']
  self.a2wspofv=pllkstn3['nk7y6q']
  self.j1ldqnk2=pllkstn3['pta5iv']
  self.v0rxxf36='hidden'
  self.tbxf445c=self.cq2q4qer
 def ygspk9p3(self):
  self.tbxf445c-=1
  if self.tbxf445c<=0:
   if self.v0rxxf36=='hidden':
    self.v0rxxf36='revealing'
    self.tbxf445c=self.a2wspofv
   elif self.v0rxxf36=='revealing':
    self.v0rxxf36='visible'
    self.tbxf445c=self.uaobt328
   else:
    self.v0rxxf36='hidden'
    self.tbxf445c=self.cq2q4qer
  self.j1ldqnk2=self.ukshy8nb if self.v0rxxf36=='hidden'else 255
 def k2ixivzk(self,player):
  if self.mqxlm5q2<=0:
   self.f2sehe2a=True
   return
  self.ygspk9p3()
  if self.v0rxxf36=='visible'and abs(player.wb7f6fdh.kn5gjj8m-self.wb7f6fdh.kn5gjj8m)<gyljexq7 and(abs(player.wb7f6fdh.lu7jae58-self.wb7f6fdh.lu7jae58)<gyljexq7):
   self.t5wi6fqj(player)
   return
  k7zgf9q5=player.wb7f6fdh.kn5gjj8m-self.wb7f6fdh.kn5gjj8m
  pa8s8hmb=player.wb7f6fdh.lu7jae58-self.wb7f6fdh.lu7jae58
  ep6beffl=math.hypot(k7zgf9q5,pa8s8hmb)
  if ep6beffl==0:
   return
  p7pchcbn=k7zgf9q5/ep6beffl
  mwszv83x=pa8s8hmb/ep6beffl
  if p7pchcbn!=0 and mwszv83x!=0:
   p7pchcbn*=0.707
   mwszv83x*=0.707
  self.wb7f6fdh.kn5gjj8m+=p7pchcbn*self.tj0nmeoq
  self.wb7f6fdh.lu7jae58+=mwszv83x*self.tj0nmeoq
  self.wb7f6fdh.kn5gjj8m=round(self.wb7f6fdh.kn5gjj8m)
  self.wb7f6fdh.lu7jae58=round(self.wb7f6fdh.lu7jae58)
 def u1jhuwb6(self,todsx4nx,u3ifhv1x,f8wquuy5):
  kn5gjj8m=self.wb7f6fdh.kn5gjj8m-u3ifhv1x
  lu7jae58=self.wb7f6fdh.lu7jae58-f8wquuy5
  x5m9j98c=self.wb7f6fdh.centerx-u3ifhv1x
  uos0fb4y=self.wb7f6fdh.centery-f8wquuy5
  if self.j1ldqnk2>=255:
   self.xd1wjcit(todsx4nx,kn5gjj8m,lu7jae58,x5m9j98c,uos0fb4y)
   return
  w4rcb1kj=24
  iaq7b7v1=pygame.Surface((self.wb7f6fdh.width+w4rcb1kj*2,self.wb7f6fdh.height+w4rcb1kj*2),pygame.SRCALPHA)
  (sdeekgys,nvuprt77)=(w4rcb1kj,w4rcb1kj)
  (xqzpky32,nyfkjfpn)=(sdeekgys+self.wb7f6fdh.width//2,nvuprt77+self.wb7f6fdh.height//2)
  self.xd1wjcit(iaq7b7v1,sdeekgys,nvuprt77,xqzpky32,nyfkjfpn)
  iaq7b7v1.set_alpha(self.j1ldqnk2)
  todsx4nx.blit(iaq7b7v1,(kn5gjj8m-w4rcb1kj,lu7jae58-w4rcb1kj))
