import pygame
from ykatqyds import*
pygame.init()
class oohp6vz4:
 rla5ju9b=46
 def __init__(self,width,height,color,title=None,title_font=None,todsx4nx=(60,60,75)):
  self.uaobt328=pygame.Rect((cqoldfor-width)//2,(tp0lvsnu-height)//2,width,height)
  self.color=color
  self.todsx4nx=todsx4nx
  self.title=title
  self.title_font=title_font
  self.arhnuxor=self.rla5ju9b if title else 0
  self.q5amln4p=[]
  self.uidlrye8=pygame.Surface((cqoldfor,tp0lvsnu),pygame.SRCALPHA)
  self.xvzc7d2k=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.xvzc7d2k,(0,0,0,90),self.xvzc7d2k.get_rect(),border_radius=20)
 def add(self,xuu13i59):
  self.q5amln4p.append(xuu13i59)
 def v15cqzcu(self,u15pdtz9):
  self.uidlrye8.fill((0,0,0,150))
  u15pdtz9.blit(self.uidlrye8,(0,0))
  u15pdtz9.blit(self.xvzc7d2k,(self.uaobt328.owdz09wf-12,self.uaobt328.lb4y4k7b-8))
  pygame.draw.rect(u15pdtz9,self.color,self.uaobt328,border_radius=16)
  pygame.draw.rect(u15pdtz9,self.todsx4nx,self.uaobt328,width=2,border_radius=16)
  if self.title and self.title_font:
   huh17j8q=self.title_font.render(self.title,True,(30,30,45))
   u15pdtz9.blit(huh17j8q,(self.uaobt328.centerx-huh17j8q.get_width()//2,self.uaobt328.lb4y4k7b+12))
   yjluujmi=self.uaobt328.lb4y4k7b+self.arhnuxor-4
   pygame.draw.line(u15pdtz9,self.todsx4nx,(self.uaobt328.owdz09wf+18,yjluujmi),(self.uaobt328.right-18,yjluujmi),1)
  for xuu13i59 in self.q5amln4p:
   xuu13i59.v15cqzcu(u15pdtz9)
ibps3y70={'orc1yo':(46,160,67),'o15o2n':(230,126,34),'n5nhqr':(52,120,200)}
class hc58drc1:
 def __init__(self,owdz09wf,lb4y4k7b,width,height,pa8s8hmb,todsx4nx,n3rlkte4,zmybd2qe,cjn2fomd,ucu7onz3,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.uaobt328=pygame.Rect(owdz09wf,lb4y4k7b,width,height)
  self.pa8s8hmb=pa8s8hmb
  self.todsx4nx=todsx4nx
  self.n3rlkte4=n3rlkte4
  self.zmybd2qe=zmybd2qe
  self.cjn2fomd=cjn2fomd
  self.ucu7onz3=ucu7onz3
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.fpa8hyex=False
  self.vw6m7b5c=False
  self.kind=kind
  self.key=key
  self.xvzc7d2k=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.xvzc7d2k,(0,0,0,55),self.xvzc7d2k.get_rect(),border_radius=border_radius)
 def update(self,s4rxyj38):
  (wb7f6fdh,got7txkd)=pygame.mouse.get_pos()
  self.fpa8hyex=self.uaobt328.collidepoint(wb7f6fdh,got7txkd)
  self.vw6m7b5c=False
  if self.fpa8hyex:
   for eatvzkhi in s4rxyj38:
    if eatvzkhi.type==pygame.MOUSEBUTTONUP and eatvzkhi.button==1:
     self.vw6m7b5c=True
 def v15cqzcu(self,u15pdtz9):
  if self.fpa8hyex:
   pa8s8hmb=self.n3rlkte4
   todsx4nx=self.zmybd2qe
  else:
   pa8s8hmb=self.pa8s8hmb
   todsx4nx=self.todsx4nx
  u15pdtz9.blit(self.xvzc7d2k,(self.uaobt328.owdz09wf,self.uaobt328.lb4y4k7b+3))
  pygame.draw.rect(u15pdtz9,pa8s8hmb,self.uaobt328,border_radius=self.border_radius)
  gn89qkns=3 if self.fpa8hyex else 1
  pygame.draw.rect(u15pdtz9,todsx4nx,self.uaobt328,border_radius=self.border_radius,width=gn89qkns)
  gp84dyt9=ibps3y70.get(self.kind)
  htgsiwg0=0
  if gp84dyt9:
   lcj883dh=pygame.Rect(self.uaobt328.owdz09wf,self.uaobt328.lb4y4k7b,7,self.uaobt328.height)
   pygame.draw.rect(u15pdtz9,gp84dyt9,lcj883dh,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   htgsiwg0=4
  it04chsd=self.uaobt328.centerx+htgsiwg0
  if self.subtitle and self.sub_font:
   huh17j8q=self.cjn2fomd.render(self.ucu7onz3,True,(15,15,20))
   rk36m8jv=self.sub_font.render(self.subtitle,True,(50,50,55))
   kcubods1=huh17j8q.get_height()+rk36m8jv.get_height()+2
   mabkae6a=self.uaobt328.centery-kcubods1//2
   gqoagsus=mabkae6a+huh17j8q.get_height()+2
   u15pdtz9.blit(huh17j8q,(it04chsd-huh17j8q.get_width()//2,mabkae6a))
   u15pdtz9.blit(rk36m8jv,(it04chsd-rk36m8jv.get_width()//2,gqoagsus))
  else:
   mu118qqv=self.cjn2fomd.render(self.ucu7onz3,True,(15,15,20))
   width=mu118qqv.get_width()
   height=mu118qqv.get_height()
   u15pdtz9.blit(mu118qqv,(it04chsd-width//2,self.uaobt328.centery-height//2))
