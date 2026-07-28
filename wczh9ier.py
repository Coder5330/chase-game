import pygame
from zfiblejg import*
pygame.init()
class oohp6vz4:
 rla5ju9b=46
 def __init__(self,width,height,color,title=None,title_font=None,l3swebnv=(60,60,75)):
  self.tby49e7e=pygame.Rect((ygspk9p3-width)//2,(tp0lvsnu-height)//2,width,height)
  self.color=color
  self.l3swebnv=l3swebnv
  self.title=title
  self.title_font=title_font
  self.sdeekgys=self.rla5ju9b if title else 0
  self.k2ixivzk=[]
  self.wc7x0h3j=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
  self.byl68ntk=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.byl68ntk,(0,0,0,90),self.byl68ntk.get_rect(),border_radius=20)
 def add(self,aicvqy5i):
  self.k2ixivzk.append(aicvqy5i)
 def dw7nh8rq(self,uwxrum2l):
  self.wc7x0h3j.fill((0,0,0,150))
  uwxrum2l.blit(self.wc7x0h3j,(0,0))
  uwxrum2l.blit(self.byl68ntk,(self.tby49e7e.x3zo7utx-12,self.tby49e7e.cjy62zee-8))
  pygame.draw.rect(uwxrum2l,self.color,self.tby49e7e,border_radius=16)
  pygame.draw.rect(uwxrum2l,self.l3swebnv,self.tby49e7e,width=2,border_radius=16)
  if self.title and self.title_font:
   it04chsd=self.title_font.render(self.title,True,(30,30,45))
   uwxrum2l.blit(it04chsd,(self.tby49e7e.centerx-it04chsd.get_width()//2,self.tby49e7e.cjy62zee+12))
   sygvwopl=self.tby49e7e.cjy62zee+self.sdeekgys-4
   pygame.draw.line(uwxrum2l,self.l3swebnv,(self.tby49e7e.x3zo7utx+18,sygvwopl),(self.tby49e7e.right-18,sygvwopl),1)
  for aicvqy5i in self.k2ixivzk:
   aicvqy5i.dw7nh8rq(uwxrum2l)
ibps3y70={'nf7qne':(46,160,67),'khkf28':(230,126,34),'tgr8w2':(52,120,200)}
class hc58drc1:
 def __init__(self,x3zo7utx,cjy62zee,width,height,k7zgf9q5,l3swebnv,xk7n8la1,xd8wz42o,x9bp4m18,awnwlc83,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.tby49e7e=pygame.Rect(x3zo7utx,cjy62zee,width,height)
  self.k7zgf9q5=k7zgf9q5
  self.l3swebnv=l3swebnv
  self.xk7n8la1=xk7n8la1
  self.xd8wz42o=xd8wz42o
  self.x9bp4m18=x9bp4m18
  self.awnwlc83=awnwlc83
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.n3rlkte4=False
  self.vw6m7b5c=False
  self.kind=kind
  self.key=key
  self.byl68ntk=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.byl68ntk,(0,0,0,55),self.byl68ntk.get_rect(),border_radius=border_radius)
 def update(self,mqxlm5q2):
  (wy0mahym,zdan085r)=pygame.mouse.get_pos()
  self.n3rlkte4=self.tby49e7e.collidepoint(wy0mahym,zdan085r)
  self.vw6m7b5c=False
  if self.n3rlkte4:
   for yrivh6t1 in mqxlm5q2:
    if yrivh6t1.type==pygame.MOUSEBUTTONUP and yrivh6t1.button==1:
     self.vw6m7b5c=True
 def dw7nh8rq(self,uwxrum2l):
  if self.n3rlkte4:
   k7zgf9q5=self.xk7n8la1
   l3swebnv=self.xd8wz42o
  else:
   k7zgf9q5=self.k7zgf9q5
   l3swebnv=self.l3swebnv
  uwxrum2l.blit(self.byl68ntk,(self.tby49e7e.x3zo7utx,self.tby49e7e.cjy62zee+3))
  pygame.draw.rect(uwxrum2l,k7zgf9q5,self.tby49e7e,border_radius=self.border_radius)
  dzsedfqs=3 if self.n3rlkte4 else 1
  pygame.draw.rect(uwxrum2l,l3swebnv,self.tby49e7e,border_radius=self.border_radius,width=dzsedfqs)
  ytv3i12v=ibps3y70.get(self.kind)
  qxb7gbdg=0
  if ytv3i12v:
   i4fejgxa=pygame.Rect(self.tby49e7e.x3zo7utx,self.tby49e7e.cjy62zee,7,self.tby49e7e.height)
   pygame.draw.rect(uwxrum2l,ytv3i12v,i4fejgxa,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   qxb7gbdg=4
  gsrtwlxd=self.tby49e7e.centerx+qxb7gbdg
  if self.subtitle and self.sub_font:
   it04chsd=self.x9bp4m18.render(self.awnwlc83,True,(15,15,20))
   tjy1o2rn=self.sub_font.render(self.subtitle,True,(50,50,55))
   s7fbmenu=it04chsd.get_height()+tjy1o2rn.get_height()+2
   htgsiwg0=self.tby49e7e.centery-s7fbmenu//2
   rr9u1oe5=htgsiwg0+it04chsd.get_height()+2
   uwxrum2l.blit(it04chsd,(gsrtwlxd-it04chsd.get_width()//2,htgsiwg0))
   uwxrum2l.blit(tjy1o2rn,(gsrtwlxd-tjy1o2rn.get_width()//2,rr9u1oe5))
  else:
   rwybow23=self.x9bp4m18.render(self.awnwlc83,True,(15,15,20))
   width=rwybow23.get_width()
   height=rwybow23.get_height()
   uwxrum2l.blit(rwybow23,(gsrtwlxd-width//2,self.tby49e7e.centery-height//2))
