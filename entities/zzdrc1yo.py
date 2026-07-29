import pygame
import math
from j1bmqf7z import*
from.kier7u8h import f935a0l7
class ukxvf1t2(f935a0l7):
 def __init__(self,mqxlm5q2,x,y):
  super().__init__(mqxlm5q2,x,y)
  self.npejzhya=0
 def qic1l7dy(self,player):
  self.npejzhya+=1
  return False
 def vyb6li07(self,player,atj9a3y3,nubmxnsz):
  from x1l6spbn import zy0ifznb
  from jggz62fe import k1taa0i5
  atj9a3y3.append(zy0ifznb(self.npcxa5s0.center))
  k1taa0i5('w9laac')
  xxkdq95g=k1wj0tpa[self.type]
  sygvwopl=math.hypot(player.npcxa5s0.centerx-self.npcxa5s0.centerx,player.npcxa5s0.centery-self.npcxa5s0.centery)
  if sygvwopl<=xxkdq95g['nddqhk']:
   dw7nh8rq=self.velos6zl*(100/(100+player.ykipu1wy))
   player.arhnuxor-=dw7nh8rq
   player.cqheyto5.append((player.npcxa5s0.centerx,player.npcxa5s0.y,f'-{int(dw7nh8rq)}',iq5c34dx['mviifr']))
 def v15cqzcu(self,h8s2ftom,vqnpcenl,iie0rnuj):
  wzlm72je=self.npcxa5s0.centerx-vqnpcenl
  vt6om1fb=self.npcxa5s0.centery-iie0rnuj
  oa47sh2s=(math.sin(self.npejzhya*0.15)+1)/2
  tj0nmeoq=int(self.npcxa5s0.width*0.6+oa47sh2s*6)
  tp2ex5t5=int(70+oa47sh2s*90)
  z8z3v6di=pygame.Surface((tj0nmeoq*2,tj0nmeoq*2),pygame.SRCALPHA)
  pygame.draw.circle(z8z3v6di,(200,30,20,tp2ex5t5),(tj0nmeoq,tj0nmeoq),tj0nmeoq)
  h8s2ftom.blit(z8z3v6di,(wzlm72je-tj0nmeoq,vt6om1fb-tj0nmeoq))
  x=self.npcxa5s0.x-vqnpcenl
  y=self.npcxa5s0.y-iie0rnuj
  self.k44nlz15(h8s2ftom,x,y,wzlm72je,vt6om1fb)
  (ej16dvtj,yypp5zp7)=(8,12)
  p2nv01zd=pygame.Rect(wzlm72je-ej16dvtj//2,y-yypp5zp7+2,ej16dvtj,yypp5zp7)
  pygame.draw.rect(h8s2ftom,(180,30,20),p2nv01zd,border_radius=1)
  pygame.draw.rect(h8s2ftom,(20,20,20),p2nv01zd,width=1,border_radius=1)
  for az2ueaxy in(p2nv01zd.top+3,p2nv01zd.top+8):
   pygame.draw.line(h8s2ftom,(240,240,230),(p2nv01zd.left,az2ueaxy),(p2nv01zd.right,az2ueaxy),1)
  cn7zrwqe=(p2nv01zd.centerx,p2nv01zd.top)
  fekrcppr=(p2nv01zd.centerx+4,p2nv01zd.top-6)
  pygame.draw.line(h8s2ftom,(90,60,30),cn7zrwqe,fekrcppr,1)
  l1rdxck3=(math.sin(self.npejzhya*0.4)+1)/2
  w0p4e05q=(255,int(150+l1rdxck3*100),40)
  pygame.draw.circle(h8s2ftom,w0p4e05q,fekrcppr,2+int(l1rdxck3))
