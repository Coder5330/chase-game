import pygame
from z4w1arag import*
pygame.init()
class yswjckjl:
 gokc1msy=46
 def __init__(self,width,height,color,title=None,title_font=None,wb7f6fdh=(60,60,75)):
  self.cqheyto5=pygame.Rect((rrcbpljd-width)//2,(rla5ju9b-height)//2,width,height)
  self.color=color
  self.wb7f6fdh=wb7f6fdh
  self.title=title
  self.title_font=title_font
  self.cn7zrwqe=self.gokc1msy if title else 0
  self.i13n3bzt=[]
  self.pv4ykade=pygame.Surface((rrcbpljd,rla5ju9b),pygame.SRCALPHA)
  self.d1hm38ks=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.d1hm38ks,(0,0,0,90),self.d1hm38ks.get_rect(),border_radius=20)
 def add(self,zefqjg02):
  self.i13n3bzt.append(zefqjg02)
 def g8kk791z(self,cq2q4qer):
  self.pv4ykade.fill((0,0,0,150))
  cq2q4qer.blit(self.pv4ykade,(0,0))
  cq2q4qer.blit(self.d1hm38ks,(self.cqheyto5.d5ixva1n-12,self.cqheyto5.nngmx1gm-8))
  pygame.draw.rect(cq2q4qer,self.color,self.cqheyto5,border_radius=16)
  pygame.draw.rect(cq2q4qer,self.wb7f6fdh,self.cqheyto5,width=2,border_radius=16)
  if self.title and self.title_font:
   vm65q57t=self.title_font.render(self.title,True,(30,30,45))
   cq2q4qer.blit(vm65q57t,(self.cqheyto5.centerx-vm65q57t.get_width()//2,self.cqheyto5.nngmx1gm+12))
   mfyb8dal=self.cqheyto5.nngmx1gm+self.cn7zrwqe-4
   pygame.draw.line(cq2q4qer,self.wb7f6fdh,(self.cqheyto5.d5ixva1n+18,mfyb8dal),(self.cqheyto5.right-18,mfyb8dal),1)
  for zefqjg02 in self.i13n3bzt:
   zefqjg02.g8kk791z(cq2q4qer)
tp0lvsnu={'gbwcv6':(46,160,67),'dzjq7w':(230,126,34),'hx0gu4':(52,120,200)}
class hc58drc1:
 def __init__(self,d5ixva1n,nngmx1gm,width,height,iie0rnuj,wb7f6fdh,gsmdzqcb,we4xyf9i,yrivh6t1,z7pwo6cm,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.cqheyto5=pygame.Rect(d5ixva1n,nngmx1gm,width,height)
  self.iie0rnuj=iie0rnuj
  self.wb7f6fdh=wb7f6fdh
  self.gsmdzqcb=gsmdzqcb
  self.we4xyf9i=we4xyf9i
  self.yrivh6t1=yrivh6t1
  self.z7pwo6cm=z7pwo6cm
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.ftlpq2wg=False
  self.i20cv3tl=False
  self.kind=kind
  self.key=key
  self.d1hm38ks=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.d1hm38ks,(0,0,0,55),self.d1hm38ks.get_rect(),border_radius=border_radius)
 def update(self,ouuylaja):
  (dq2fa39e,mnwxuj3a)=pygame.mouse.get_pos()
  self.ftlpq2wg=self.cqheyto5.collidepoint(dq2fa39e,mnwxuj3a)
  self.i20cv3tl=False
  if self.ftlpq2wg:
   for vhuds3qs in ouuylaja:
    if vhuds3qs.type==pygame.MOUSEBUTTONUP and vhuds3qs.button==1:
     self.i20cv3tl=True
 def g8kk791z(self,cq2q4qer):
  if self.ftlpq2wg:
   iie0rnuj=self.gsmdzqcb
   wb7f6fdh=self.we4xyf9i
  else:
   iie0rnuj=self.iie0rnuj
   wb7f6fdh=self.wb7f6fdh
  cq2q4qer.blit(self.d1hm38ks,(self.cqheyto5.d5ixva1n,self.cqheyto5.nngmx1gm+3))
  pygame.draw.rect(cq2q4qer,iie0rnuj,self.cqheyto5,border_radius=self.border_radius)
  f8wquuy5=3 if self.ftlpq2wg else 1
  pygame.draw.rect(cq2q4qer,wb7f6fdh,self.cqheyto5,border_radius=self.border_radius,width=f8wquuy5)
  t5wi6fqj=tp0lvsnu.get(self.kind)
  l0sqg4ei=0
  if t5wi6fqj:
   iy6qktc8=pygame.Rect(self.cqheyto5.d5ixva1n,self.cqheyto5.nngmx1gm,7,self.cqheyto5.height)
   pygame.draw.rect(cq2q4qer,t5wi6fqj,iy6qktc8,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   l0sqg4ei=4
  klkjxjq5=self.cqheyto5.centerx+l0sqg4ei
  if self.subtitle and self.sub_font:
   vm65q57t=self.yrivh6t1.render(self.z7pwo6cm,True,(15,15,20))
   u1ni10kq=self.sub_font.render(self.subtitle,True,(50,50,55))
   ra9kepad=vm65q57t.get_height()+u1ni10kq.get_height()+2
   e8zgvwwu=self.cqheyto5.centery-ra9kepad//2
   qdnai89y=e8zgvwwu+vm65q57t.get_height()+2
   cq2q4qer.blit(vm65q57t,(klkjxjq5-vm65q57t.get_width()//2,e8zgvwwu))
   cq2q4qer.blit(u1ni10kq,(klkjxjq5-u1ni10kq.get_width()//2,qdnai89y))
  else:
   p7b1ijiy=self.yrivh6t1.render(self.z7pwo6cm,True,(15,15,20))
   width=p7b1ijiy.get_width()
   height=p7b1ijiy.get_height()
   cq2q4qer.blit(p7b1ijiy,(klkjxjq5-width//2,self.cqheyto5.centery-height//2))
