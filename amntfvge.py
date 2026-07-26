import pygame
from rlfzkicw import*
pygame.init()
class cq5uznof:
 pi3qk2ia=46
 def __init__(self,width,height,zfb7r31q,title=None,title_font=None,gqq4d3kz=(60,60,75)):
  self.mu4fmpkx=pygame.Rect((azebbk7w-width)//2,(gokc1msy-height)//2,width,height)
  self.zfb7r31q=zfb7r31q
  self.gqq4d3kz=gqq4d3kz
  self.title=title
  self.title_font=title_font
  self.yrivh6t1=self.pi3qk2ia if title else 0
  self.m20u9isy=[]
  self.iie0rnuj=pygame.Surface((azebbk7w,gokc1msy),pygame.SRCALPHA)
  self.rgdej31g=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.rgdej31g,(0,0,0,90),self.rgdej31g.get_rect(),border_radius=20)
 def add(self,cnqt3wve):
  self.m20u9isy.append(cnqt3wve)
 def u1jhuwb6(self,uz6kf162):
  self.iie0rnuj.fill((0,0,0,150))
  uz6kf162.blit(self.iie0rnuj,(0,0))
  uz6kf162.blit(self.rgdej31g,(self.mu4fmpkx.kn5gjj8m-12,self.mu4fmpkx.lu7jae58-8))
  pygame.draw.rect(uz6kf162,self.zfb7r31q,self.mu4fmpkx,border_radius=16)
  pygame.draw.rect(uz6kf162,self.gqq4d3kz,self.mu4fmpkx,width=2,border_radius=16)
  if self.title and self.title_font:
   bf7so8w5=self.title_font.render(self.title,True,(30,30,45))
   uz6kf162.blit(bf7so8w5,(self.mu4fmpkx.centerx-bf7so8w5.get_width()//2,self.mu4fmpkx.lu7jae58+12))
   wi8skch8=self.mu4fmpkx.lu7jae58+self.yrivh6t1-4
   pygame.draw.line(uz6kf162,self.gqq4d3kz,(self.mu4fmpkx.kn5gjj8m+18,wi8skch8),(self.mu4fmpkx.right-18,wi8skch8),1)
  for cnqt3wve in self.m20u9isy:
   cnqt3wve.u1jhuwb6(uz6kf162)
rla5ju9b={'txzuu8':(46,160,67),'dzjssz':(230,126,34),'fnn16u':(52,120,200)}
class q7vren93:
 def __init__(self,kn5gjj8m,lu7jae58,width,height,li9nb74x,gqq4d3kz,mc8qizk3,cx41dntc,sygvwopl,w8wj0uun,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.mu4fmpkx=pygame.Rect(kn5gjj8m,lu7jae58,width,height)
  self.li9nb74x=li9nb74x
  self.gqq4d3kz=gqq4d3kz
  self.mc8qizk3=mc8qizk3
  self.cx41dntc=cx41dntc
  self.sygvwopl=sygvwopl
  self.w8wj0uun=w8wj0uun
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.azc4xl99=False
  self.yw6zbnz8=False
  self.kind=kind
  self.key=key
  self.rgdej31g=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.rgdej31g,(0,0,0,55),self.rgdej31g.get_rect(),border_radius=border_radius)
 def update(self,wehlxslg):
  (k2ixivzk,wa45hvgo)=pygame.mouse.get_pos()
  self.azc4xl99=self.mu4fmpkx.collidepoint(k2ixivzk,wa45hvgo)
  self.yw6zbnz8=False
  if self.azc4xl99:
   for eohswq40 in wehlxslg:
    if eohswq40.type==pygame.MOUSEBUTTONUP and eohswq40.button==1:
     self.yw6zbnz8=True
 def u1jhuwb6(self,uz6kf162):
  if self.azc4xl99:
   li9nb74x=self.mc8qizk3
   gqq4d3kz=self.cx41dntc
  else:
   li9nb74x=self.li9nb74x
   gqq4d3kz=self.gqq4d3kz
  uz6kf162.blit(self.rgdej31g,(self.mu4fmpkx.kn5gjj8m,self.mu4fmpkx.lu7jae58+3))
  pygame.draw.rect(uz6kf162,li9nb74x,self.mu4fmpkx,border_radius=self.border_radius)
  vj8yrddp=3 if self.azc4xl99 else 1
  pygame.draw.rect(uz6kf162,gqq4d3kz,self.mu4fmpkx,border_radius=self.border_radius,width=vj8yrddp)
  v83tqll8=rla5ju9b.get(self.kind)
  l3m25a5p=0
  if v83tqll8:
   m53a5qbs=pygame.Rect(self.mu4fmpkx.kn5gjj8m,self.mu4fmpkx.lu7jae58,7,self.mu4fmpkx.height)
   pygame.draw.rect(uz6kf162,v83tqll8,m53a5qbs,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   l3m25a5p=4
  mnx4sn6s=self.mu4fmpkx.centerx+l3m25a5p
  if self.subtitle and self.sub_font:
   bf7so8w5=self.sygvwopl.render(self.w8wj0uun,True,(15,15,20))
   k8qeoz0k=self.sub_font.render(self.subtitle,True,(50,50,55))
   rserev36=bf7so8w5.get_height()+k8qeoz0k.get_height()+2
   xxkdq95g=self.mu4fmpkx.centery-rserev36//2
   wtl0thhz=xxkdq95g+bf7so8w5.get_height()+2
   uz6kf162.blit(bf7so8w5,(mnx4sn6s-bf7so8w5.get_width()//2,xxkdq95g))
   uz6kf162.blit(k8qeoz0k,(mnx4sn6s-k8qeoz0k.get_width()//2,wtl0thhz))
  else:
   kz1uu7zy=self.sygvwopl.render(self.w8wj0uun,True,(15,15,20))
   width=kz1uu7zy.get_width()
   height=kz1uu7zy.get_height()
   uz6kf162.blit(kz1uu7zy,(mnx4sn6s-width//2,self.mu4fmpkx.centery-height//2))
