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
  k7zgf9q5=player.mu4fmpkx.centerx-self.mu4fmpkx.centerx
  pa8s8hmb=player.mu4fmpkx.centery-self.mu4fmpkx.centery
  onqyyf9r=math.hypot(k7zgf9q5,pa8s8hmb)or 1
  self.fo75rh8l=(k7zgf9q5/onqyyf9r,pa8s8hmb/onqyyf9r)
  if self.i0x65muf:
   self.kybwmlun-=1
   if self.kybwmlun<=0:
    self.i0x65muf=False
    self.jqxs6esj(player)
   return True
  if abs(player.mu4fmpkx.kn5gjj8m-self.mu4fmpkx.kn5gjj8m)<s0clbr7t and abs(player.mu4fmpkx.lu7jae58-self.mu4fmpkx.lu7jae58)<s0clbr7t:
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
  xsspye9r=mjh75lxo['jq85x7']['uq0e27']
  (k7zgf9q5,pa8s8hmb)=(player.mu4fmpkx.centerx-self.mu4fmpkx.centerx,player.mu4fmpkx.centery-self.mu4fmpkx.centery)
  u8c2jwoc=rpqk51fp('jq85x7',self.mu4fmpkx.centerx-xsspye9r//2,self.mu4fmpkx.centery-xsspye9r//2,xsspye9r,xsspye9r,k7zgf9q5,pa8s8hmb)
  u8c2jwoc.obc2nnuv=self.iektsg7f
  self.bwiykid9.append(u8c2jwoc)
 def u1jhuwb6(self,uz6kf162,u3ifhv1x,f8wquuy5):
  kn5gjj8m=self.mu4fmpkx.kn5gjj8m-u3ifhv1x
  lu7jae58=self.mu4fmpkx.lu7jae58-f8wquuy5
  x5m9j98c=self.mu4fmpkx.centerx-u3ifhv1x
  uos0fb4y=self.mu4fmpkx.centery-f8wquuy5
  self.xd1wjcit(uz6kf162,kn5gjj8m,lu7jae58,x5m9j98c,uos0fb4y)
  (b36htf4p,vhuds3qs)=self.fo75rh8l
  (y8bv78hu,pf0i9g5d)=(-vhuds3qs,b36htf4p)
  (x03uvule,l57p6bkl)=(x5m9j98c+b36htf4p*14,uos0fb4y+vhuds3qs*14)
  holeyrvx=(x03uvule+y8bv78hu*13-b36htf4p*6,l57p6bkl+pf0i9g5d*13-vhuds3qs*6)
  nabufwbu=(x03uvule-y8bv78hu*13-b36htf4p*6,l57p6bkl-pf0i9g5d*13-vhuds3qs*6)
  sv5f1bcp=(x03uvule+b36htf4p*6,l57p6bkl+vhuds3qs*6)
  pygame.draw.lines(uz6kf162,(110,70,30),False,[holeyrvx,sv5f1bcp,nabufwbu],3)
  rk8r2ykc=1-self.kybwmlun/self.wppsfnko if self.i0x65muf else 0
  crsb4gf1=(x03uvule-b36htf4p*(3+rk8r2ykc*10),l57p6bkl-vhuds3qs*(3+rk8r2ykc*10))
  pygame.draw.line(uz6kf162,(225,225,215),holeyrvx,crsb4gf1,2)
  pygame.draw.line(uz6kf162,(225,225,215),nabufwbu,crsb4gf1,2)
  if self.i0x65muf:
   k44nlz15=(x03uvule+b36htf4p*8,l57p6bkl+vhuds3qs*8)
   pygame.draw.line(uz6kf162,bom5igqp['hlxzvo'],crsb4gf1,k44nlz15,3)
