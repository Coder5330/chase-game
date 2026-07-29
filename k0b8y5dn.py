import pygame
from j1bmqf7z import*
pygame.init()
class oohp6vz4:
 rla5ju9b=46
 def __init__(self,width,height,color,title=None,title_font=None,f8rtm4j3=(60,60,75)):
  self.npcxa5s0=pygame.Rect((ygspk9p3-width)//2,(tp0lvsnu-height)//2,width,height)
  self.color=color
  self.f8rtm4j3=f8rtm4j3
  self.title=title
  self.title_font=title_font
  self.ftrflqbm=self.rla5ju9b if title else 0
  self.ub68rerv=[]
  self.uidlrye8=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
  self.q3n2qb6g=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.q3n2qb6g,(0,0,0,90),self.q3n2qb6g.get_rect(),border_radius=20)
 def add(self,xuu13i59):
  self.ub68rerv.append(xuu13i59)
 def v15cqzcu(self,h8s2ftom):
  self.uidlrye8.fill((0,0,0,150))
  h8s2ftom.blit(self.uidlrye8,(0,0))
  h8s2ftom.blit(self.q3n2qb6g,(self.npcxa5s0.x-12,self.npcxa5s0.y-8))
  pygame.draw.rect(h8s2ftom,self.color,self.npcxa5s0,border_radius=16)
  pygame.draw.rect(h8s2ftom,self.f8rtm4j3,self.npcxa5s0,width=2,border_radius=16)
  if self.title and self.title_font:
   it04chsd=self.title_font.render(self.title,True,(30,30,45))
   h8s2ftom.blit(it04chsd,(self.npcxa5s0.centerx-it04chsd.get_width()//2,self.npcxa5s0.y+12))
   yjluujmi=self.npcxa5s0.y+self.ftrflqbm-4
   pygame.draw.line(h8s2ftom,self.f8rtm4j3,(self.npcxa5s0.x+18,yjluujmi),(self.npcxa5s0.right-18,yjluujmi),1)
  for xuu13i59 in self.ub68rerv:
   xuu13i59.v15cqzcu(h8s2ftom)
ibps3y70={'v6idii':(46,160,67),'xgmjmb':(230,126,34),'jo31yh':(52,120,200)}
class hc58drc1:
 def __init__(self,x,y,width,height,pv4ykade,f8rtm4j3,n3rlkte4,zmybd2qe,mpyxdw2z,awnwlc83,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.npcxa5s0=pygame.Rect(x,y,width,height)
  self.pv4ykade=pv4ykade
  self.f8rtm4j3=f8rtm4j3
  self.n3rlkte4=n3rlkte4
  self.zmybd2qe=zmybd2qe
  self.mpyxdw2z=mpyxdw2z
  self.awnwlc83=awnwlc83
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.fpa8hyex=False
  self.rk8r2ykc=False
  self.kind=kind
  self.key=key
  self.q3n2qb6g=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.q3n2qb6g,(0,0,0,55),self.q3n2qb6g.get_rect(),border_radius=border_radius)
 def update(self,eatvzkhi):
  (mmn32u1i,oc4kl8cg)=pygame.mouse.get_pos()
  self.fpa8hyex=self.npcxa5s0.collidepoint(mmn32u1i,oc4kl8cg)
  self.rk8r2ykc=False
  if self.fpa8hyex:
   for xq46nouh in eatvzkhi:
    if xq46nouh.type==pygame.MOUSEBUTTONUP and xq46nouh.button==1:
     self.rk8r2ykc=True
 def v15cqzcu(self,h8s2ftom):
  if self.fpa8hyex:
   pv4ykade=self.n3rlkte4
   f8rtm4j3=self.zmybd2qe
  else:
   pv4ykade=self.pv4ykade
   f8rtm4j3=self.f8rtm4j3
  h8s2ftom.blit(self.q3n2qb6g,(self.npcxa5s0.x,self.npcxa5s0.y+3))
  pygame.draw.rect(h8s2ftom,pv4ykade,self.npcxa5s0,border_radius=self.border_radius)
  li9nb74x=3 if self.fpa8hyex else 1
  pygame.draw.rect(h8s2ftom,f8rtm4j3,self.npcxa5s0,border_radius=self.border_radius,width=li9nb74x)
  am2vajep=ibps3y70.get(self.kind)
  qxb7gbdg=0
  if am2vajep:
   d0r2sds8=pygame.Rect(self.npcxa5s0.x,self.npcxa5s0.y,7,self.npcxa5s0.height)
   pygame.draw.rect(h8s2ftom,am2vajep,d0r2sds8,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   qxb7gbdg=4
  gsrtwlxd=self.npcxa5s0.centerx+qxb7gbdg
  if self.subtitle and self.sub_font:
   it04chsd=self.mpyxdw2z.render(self.awnwlc83,True,(15,15,20))
   tjy1o2rn=self.sub_font.render(self.subtitle,True,(50,50,55))
   s7fbmenu=it04chsd.get_height()+tjy1o2rn.get_height()+2
   htgsiwg0=self.npcxa5s0.centery-s7fbmenu//2
   rr9u1oe5=htgsiwg0+it04chsd.get_height()+2
   h8s2ftom.blit(it04chsd,(gsrtwlxd-it04chsd.get_width()//2,htgsiwg0))
   h8s2ftom.blit(tjy1o2rn,(gsrtwlxd-tjy1o2rn.get_width()//2,rr9u1oe5))
  else:
   rwybow23=self.mpyxdw2z.render(self.awnwlc83,True,(15,15,20))
   width=rwybow23.get_width()
   height=rwybow23.get_height()
   h8s2ftom.blit(rwybow23,(gsrtwlxd-width//2,self.npcxa5s0.centery-height//2))
