import pygame
from rlfzkicw import*
pygame.init()
class cq5uznof:
 pi3qk2ia=46
 def __init__(self,width,height,zfb7r31q,title=None,title_font=None,zo3lqi7e=(60,60,75)):
  self.wb7f6fdh=pygame.Rect((azebbk7w-width)//2,(gokc1msy-height)//2,width,height)
  self.zfb7r31q=zfb7r31q
  self.zo3lqi7e=zo3lqi7e
  self.title=title
  self.title_font=title_font
  self.yrivh6t1=self.pi3qk2ia if title else 0
  self.damdvlnk=[]
  self.iie0rnuj=pygame.Surface((azebbk7w,gokc1msy),pygame.SRCALPHA)
  self.no0u93mz=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.no0u93mz,(0,0,0,90),self.no0u93mz.get_rect(),border_radius=20)
 def add(self,cnqt3wve):
  self.damdvlnk.append(cnqt3wve)
 def u1jhuwb6(self,todsx4nx):
  self.iie0rnuj.fill((0,0,0,150))
  todsx4nx.blit(self.iie0rnuj,(0,0))
  todsx4nx.blit(self.no0u93mz,(self.wb7f6fdh.kn5gjj8m-12,self.wb7f6fdh.lu7jae58-8))
  pygame.draw.rect(todsx4nx,self.zfb7r31q,self.wb7f6fdh,border_radius=16)
  pygame.draw.rect(todsx4nx,self.zo3lqi7e,self.wb7f6fdh,width=2,border_radius=16)
  if self.title and self.title_font:
   nabufwbu=self.title_font.render(self.title,True,(30,30,45))
   todsx4nx.blit(nabufwbu,(self.wb7f6fdh.centerx-nabufwbu.get_width()//2,self.wb7f6fdh.lu7jae58+12))
   wi8skch8=self.wb7f6fdh.lu7jae58+self.yrivh6t1-4
   pygame.draw.line(todsx4nx,self.zo3lqi7e,(self.wb7f6fdh.kn5gjj8m+18,wi8skch8),(self.wb7f6fdh.right-18,wi8skch8),1)
  for cnqt3wve in self.damdvlnk:
   cnqt3wve.u1jhuwb6(todsx4nx)
rla5ju9b={'txzuu8':(46,160,67),'dzjssz':(230,126,34),'fnn16u':(52,120,200)}
class q7vren93:
 def __init__(self,kn5gjj8m,lu7jae58,width,height,li9nb74x,zo3lqi7e,mc8qizk3,cx41dntc,sygvwopl,q6nqqb9l,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.wb7f6fdh=pygame.Rect(kn5gjj8m,lu7jae58,width,height)
  self.li9nb74x=li9nb74x
  self.zo3lqi7e=zo3lqi7e
  self.mc8qizk3=mc8qizk3
  self.cx41dntc=cx41dntc
  self.sygvwopl=sygvwopl
  self.q6nqqb9l=q6nqqb9l
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.azc4xl99=False
  self.yw6zbnz8=False
  self.kind=kind
  self.key=key
  self.no0u93mz=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.no0u93mz,(0,0,0,55),self.no0u93mz.get_rect(),border_radius=border_radius)
 def update(self,wehlxslg):
  (avfmh07w,o4dd1vn8)=pygame.mouse.get_pos()
  self.azc4xl99=self.wb7f6fdh.collidepoint(avfmh07w,o4dd1vn8)
  self.yw6zbnz8=False
  if self.azc4xl99:
   for eohswq40 in wehlxslg:
    if eohswq40.type==pygame.MOUSEBUTTONUP and eohswq40.button==1:
     self.yw6zbnz8=True
 def u1jhuwb6(self,todsx4nx):
  if self.azc4xl99:
   li9nb74x=self.mc8qizk3
   zo3lqi7e=self.cx41dntc
  else:
   li9nb74x=self.li9nb74x
   zo3lqi7e=self.zo3lqi7e
  todsx4nx.blit(self.no0u93mz,(self.wb7f6fdh.kn5gjj8m,self.wb7f6fdh.lu7jae58+3))
  pygame.draw.rect(todsx4nx,li9nb74x,self.wb7f6fdh,border_radius=self.border_radius)
  vj8yrddp=3 if self.azc4xl99 else 1
  pygame.draw.rect(todsx4nx,zo3lqi7e,self.wb7f6fdh,border_radius=self.border_radius,width=vj8yrddp)
  v83tqll8=rla5ju9b.get(self.kind)
  mnx4sn6s=0
  if v83tqll8:
   m53a5qbs=pygame.Rect(self.wb7f6fdh.kn5gjj8m,self.wb7f6fdh.lu7jae58,7,self.wb7f6fdh.height)
   pygame.draw.rect(todsx4nx,v83tqll8,m53a5qbs,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   mnx4sn6s=4
  w8wj0uun=self.wb7f6fdh.centerx+mnx4sn6s
  if self.subtitle and self.sub_font:
   nabufwbu=self.sygvwopl.render(self.q6nqqb9l,True,(15,15,20))
   t5sn961j=self.sub_font.render(self.subtitle,True,(50,50,55))
   rserev36=nabufwbu.get_height()+t5sn961j.get_height()+2
   bf7so8w5=self.wb7f6fdh.centery-rserev36//2
   k8qeoz0k=bf7so8w5+nabufwbu.get_height()+2
   todsx4nx.blit(nabufwbu,(w8wj0uun-nabufwbu.get_width()//2,bf7so8w5))
   todsx4nx.blit(t5sn961j,(w8wj0uun-t5sn961j.get_width()//2,k8qeoz0k))
  else:
   vmy9x8sy=self.sygvwopl.render(self.q6nqqb9l,True,(15,15,20))
   width=vmy9x8sy.get_width()
   height=vmy9x8sy.get_height()
   todsx4nx.blit(vmy9x8sy,(w8wj0uun-width//2,self.wb7f6fdh.centery-height//2))
