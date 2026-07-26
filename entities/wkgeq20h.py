import pygame
import math
from rlfzkicw import*
from.o3ksgnbh import dmu5907i
class spbhsahx(dmu5907i):
 def __init__(self,mfyb8dal,kn5gjj8m,lu7jae58):
  super().__init__(mfyb8dal,kn5gjj8m,lu7jae58)
  self.fo75rh8l=(0,1)
  self.i0x65muf=False
  self.kybwmlun=0
  self.wppsfnko=18
 def tjy1o2rn(self,player):
  k7zgf9q5=player.wb7f6fdh.centerx-self.wb7f6fdh.centerx
  pa8s8hmb=player.wb7f6fdh.centery-self.wb7f6fdh.centery
  zpajssuu=math.hypot(k7zgf9q5,pa8s8hmb)or 1
  self.fo75rh8l=(k7zgf9q5/zpajssuu,pa8s8hmb/zpajssuu)
  if self.i0x65muf:
   self.kybwmlun-=1
   if self.kybwmlun<=0:
    self.i0x65muf=False
    self.jqxs6esj(player)
   return True
  if abs(player.wb7f6fdh.kn5gjj8m-self.wb7f6fdh.kn5gjj8m)<s0clbr7t and abs(player.wb7f6fdh.lu7jae58-self.wb7f6fdh.lu7jae58)<s0clbr7t:
   if self.iy6qktc8>0:
    self.iy6qktc8-=1
    return True
   self.i0x65muf=True
   self.kybwmlun=self.wppsfnko
   return True
  return False
 def jqxs6esj(self,player):
  self.iy6qktc8=self.i4fejgxa
  from p2xrw6tm import rpqk51fp
  k1taa0i5=mjh75lxo['jq85x7']['uq0e27']
  (k7zgf9q5,pa8s8hmb)=(player.wb7f6fdh.centerx-self.wb7f6fdh.centerx,player.wb7f6fdh.centery-self.wb7f6fdh.centery)
  u8c2jwoc=rpqk51fp('jq85x7',self.wb7f6fdh.centerx-k1taa0i5//2,self.wb7f6fdh.centery-k1taa0i5//2,k1taa0i5,k1taa0i5,k7zgf9q5,pa8s8hmb)
  u8c2jwoc.obc2nnuv=self.iektsg7f
  self.bwiykid9.append(u8c2jwoc)
 def u1jhuwb6(self,todsx4nx,u3ifhv1x,f8wquuy5):
  kn5gjj8m=self.wb7f6fdh.kn5gjj8m-u3ifhv1x
  lu7jae58=self.wb7f6fdh.lu7jae58-f8wquuy5
  x5m9j98c=self.wb7f6fdh.centerx-u3ifhv1x
  uos0fb4y=self.wb7f6fdh.centery-f8wquuy5
  self.xd1wjcit(todsx4nx,kn5gjj8m,lu7jae58,x5m9j98c,uos0fb4y)
  (b36htf4p,vhuds3qs)=self.fo75rh8l
  (w8y72ivg,j0kgazu4)=(-vhuds3qs,b36htf4p)
  (x03uvule,l57p6bkl)=(x5m9j98c+b36htf4p*14,uos0fb4y+vhuds3qs*14)
  hcxhgnze=(x03uvule+w8y72ivg*13-b36htf4p*6,l57p6bkl+j0kgazu4*13-vhuds3qs*6)
  holeyrvx=(x03uvule-w8y72ivg*13-b36htf4p*6,l57p6bkl-j0kgazu4*13-vhuds3qs*6)
  sv5f1bcp=(x03uvule+b36htf4p*6,l57p6bkl+vhuds3qs*6)
  pygame.draw.lines(todsx4nx,(110,70,30),False,[hcxhgnze,sv5f1bcp,holeyrvx],3)
  rk8r2ykc=1-self.kybwmlun/self.wppsfnko if self.i0x65muf else 0
  ls2zge2j=(x03uvule-b36htf4p*(3+rk8r2ykc*10),l57p6bkl-vhuds3qs*(3+rk8r2ykc*10))
  pygame.draw.line(todsx4nx,(225,225,215),hcxhgnze,ls2zge2j,2)
  pygame.draw.line(todsx4nx,(225,225,215),holeyrvx,ls2zge2j,2)
  if self.i0x65muf:
   k44nlz15=(x03uvule+b36htf4p*8,l57p6bkl+vhuds3qs*8)
   pygame.draw.line(todsx4nx,bom5igqp['hlxzvo'],ls2zge2j,k44nlz15,3)
