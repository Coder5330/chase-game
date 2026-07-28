import pygame
from v7bnhjw6 import*
pygame.init()
class rcfnfhol:
 gokc1msy=46
 def __init__(self,width,height,color,title=None,title_font=None,wydmt8vt=(60,60,75)):
  self.jenvg3kk=pygame.Rect((v4u89yjb-width)//2,(rla5ju9b-height)//2,width,height)
  self.color=color
  self.wydmt8vt=wydmt8vt
  self.title=title
  self.title_font=title_font
  self.kkzruin3=self.gokc1msy if title else 0
  self.wvpw232u=[]
  self.do2m71hs=pygame.Surface((v4u89yjb,rla5ju9b),pygame.SRCALPHA)
  self.t5sn961j=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.t5sn961j,(0,0,0,90),self.t5sn961j.get_rect(),border_radius=20)
 def add(self,yjluujmi):
  self.wvpw232u.append(yjluujmi)
 def wc7x0h3j(self,gg7oq2zd):
  self.do2m71hs.fill((0,0,0,150))
  gg7oq2zd.blit(self.do2m71hs,(0,0))
  gg7oq2zd.blit(self.t5sn961j,(self.jenvg3kk.qic1l7dy-12,self.jenvg3kk.vsjchzjq-8))
  pygame.draw.rect(gg7oq2zd,self.color,self.jenvg3kk,border_radius=16)
  pygame.draw.rect(gg7oq2zd,self.wydmt8vt,self.jenvg3kk,width=2,border_radius=16)
  if self.title and self.title_font:
   m3hcws2w=self.title_font.render(self.title,True,(30,30,45))
   gg7oq2zd.blit(m3hcws2w,(self.jenvg3kk.centerx-m3hcws2w.get_width()//2,self.jenvg3kk.vsjchzjq+12))
   rmm1zxyv=self.jenvg3kk.vsjchzjq+self.kkzruin3-4
   pygame.draw.line(gg7oq2zd,self.wydmt8vt,(self.jenvg3kk.qic1l7dy+18,rmm1zxyv),(self.jenvg3kk.right-18,rmm1zxyv),1)
  for yjluujmi in self.wvpw232u:
   yjluujmi.wc7x0h3j(gg7oq2zd)
tp0lvsnu={'ozdcuj':(46,160,67),'yrp422':(230,126,34),'w9laac':(52,120,200)}
class hc58drc1:
 def __init__(self,qic1l7dy,vsjchzjq,width,height,lztkkfzz,wydmt8vt,vpbwhvnz,gkz2u2tn,eatvzkhi,vm65q57t,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.jenvg3kk=pygame.Rect(qic1l7dy,vsjchzjq,width,height)
  self.lztkkfzz=lztkkfzz
  self.wydmt8vt=wydmt8vt
  self.vpbwhvnz=vpbwhvnz
  self.gkz2u2tn=gkz2u2tn
  self.eatvzkhi=eatvzkhi
  self.vm65q57t=vm65q57t
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.gqj5sxvw=False
  self.uos0fb4y=False
  self.kind=kind
  self.key=key
  self.t5sn961j=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.t5sn961j,(0,0,0,55),self.t5sn961j.get_rect(),border_radius=border_radius)
 def update(self,mq7nc85e):
  (jr5rdnpx,zsw2292m)=pygame.mouse.get_pos()
  self.gqj5sxvw=self.jenvg3kk.collidepoint(jr5rdnpx,zsw2292m)
  self.uos0fb4y=False
  if self.gqj5sxvw:
   for pbo119xp in mq7nc85e:
    if pbo119xp.type==pygame.MOUSEBUTTONUP and pbo119xp.button==1:
     self.uos0fb4y=True
 def wc7x0h3j(self,gg7oq2zd):
  if self.gqj5sxvw:
   lztkkfzz=self.vpbwhvnz
   wydmt8vt=self.gkz2u2tn
  else:
   lztkkfzz=self.lztkkfzz
   wydmt8vt=self.wydmt8vt
  gg7oq2zd.blit(self.t5sn961j,(self.jenvg3kk.qic1l7dy,self.jenvg3kk.vsjchzjq+3))
  pygame.draw.rect(gg7oq2zd,lztkkfzz,self.jenvg3kk,border_radius=self.border_radius)
  j2vmcqbn=3 if self.gqj5sxvw else 1
  pygame.draw.rect(gg7oq2zd,wydmt8vt,self.jenvg3kk,border_radius=self.border_radius,width=j2vmcqbn)
  sk8yqk94=tp0lvsnu.get(self.kind)
  qxt6ridl=0
  if sk8yqk94:
   diuu9k9x=pygame.Rect(self.jenvg3kk.qic1l7dy,self.jenvg3kk.vsjchzjq,7,self.jenvg3kk.height)
   pygame.draw.rect(gg7oq2zd,sk8yqk94,diuu9k9x,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   qxt6ridl=4
  e8zgvwwu=self.jenvg3kk.centerx+qxt6ridl
  if self.subtitle and self.sub_font:
   m3hcws2w=self.eatvzkhi.render(self.vm65q57t,True,(15,15,20))
   mnx4sn6s=self.sub_font.render(self.subtitle,True,(50,50,55))
   jh55hewl=m3hcws2w.get_height()+mnx4sn6s.get_height()+2
   wyk03o4g=self.jenvg3kk.centery-jh55hewl//2
   l3m25a5p=wyk03o4g+m3hcws2w.get_height()+2
   gg7oq2zd.blit(m3hcws2w,(e8zgvwwu-m3hcws2w.get_width()//2,wyk03o4g))
   gg7oq2zd.blit(mnx4sn6s,(e8zgvwwu-mnx4sn6s.get_width()//2,l3m25a5p))
  else:
   holeyrvx=self.eatvzkhi.render(self.vm65q57t,True,(15,15,20))
   width=holeyrvx.get_width()
   height=holeyrvx.get_height()
   gg7oq2zd.blit(holeyrvx,(e8zgvwwu-width//2,self.jenvg3kk.centery-height//2))
