import pygame
from en1x2gdg import*
pygame.init()
class wa11dpg8:
 gokc1msy=46
 def __init__(self,width,height,color,title=None,title_font=None,wg25cfzf=(60,60,75)):
  self.f8rtm4j3=pygame.Rect((mqp49kwv-width)//2,(rla5ju9b-height)//2,width,height)
  self.color=color
  self.wg25cfzf=wg25cfzf
  self.title=title
  self.title_font=title_font
  self.v76ub7l8=self.gokc1msy if title else 0
  self.ftlpq2wg=[]
  self.wi8skch8=pygame.Surface((mqp49kwv,rla5ju9b),pygame.SRCALPHA)
  self.d46aexl6=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.d46aexl6,(0,0,0,90),self.d46aexl6.get_rect(),border_radius=20)
 def add(self,wzlm72je):
  self.ftlpq2wg.append(wzlm72je)
 def do2m71hs(self,gmoft6yr):
  self.wi8skch8.fill((0,0,0,150))
  gmoft6yr.blit(self.wi8skch8,(0,0))
  gmoft6yr.blit(self.d46aexl6,(self.f8rtm4j3.qxb7gbdg-12,self.f8rtm4j3.n01uyzpd-8))
  pygame.draw.rect(gmoft6yr,self.color,self.f8rtm4j3,border_radius=16)
  pygame.draw.rect(gmoft6yr,self.wg25cfzf,self.f8rtm4j3,width=2,border_radius=16)
  if self.title and self.title_font:
   kn5gjj8m=self.title_font.render(self.title,True,(30,30,45))
   gmoft6yr.blit(kn5gjj8m,(self.f8rtm4j3.centerx-kn5gjj8m.get_width()//2,self.f8rtm4j3.n01uyzpd+12))
   pa8s8hmb=self.f8rtm4j3.n01uyzpd+self.v76ub7l8-4
   pygame.draw.line(gmoft6yr,self.wg25cfzf,(self.f8rtm4j3.qxb7gbdg+18,pa8s8hmb),(self.f8rtm4j3.right-18,pa8s8hmb),1)
  for wzlm72je in self.ftlpq2wg:
   wzlm72je.do2m71hs(gmoft6yr)
tp0lvsnu={'cxf5x9':(46,160,67),'mmgvu4':(230,126,34),'y3lxch':(52,120,200)}
class hc58drc1:
 def __init__(self,qxb7gbdg,n01uyzpd,width,height,ugez7bh2,wg25cfzf,u9el8hl8,kkzruin3,g70e3p15,v7g0iiji,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.f8rtm4j3=pygame.Rect(qxb7gbdg,n01uyzpd,width,height)
  self.ugez7bh2=ugez7bh2
  self.wg25cfzf=wg25cfzf
  self.u9el8hl8=u9el8hl8
  self.kkzruin3=kkzruin3
  self.g70e3p15=g70e3p15
  self.v7g0iiji=v7g0iiji
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.mn7h9g1a=False
  self.d1ieixwc=False
  self.kind=kind
  self.key=key
  self.d46aexl6=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.d46aexl6,(0,0,0,55),self.d46aexl6.get_rect(),border_radius=border_radius)
 def update(self,zefqjg02):
  (j1ldqnk2,xwqvr1h6)=pygame.mouse.get_pos()
  self.mn7h9g1a=self.f8rtm4j3.collidepoint(j1ldqnk2,xwqvr1h6)
  self.d1ieixwc=False
  if self.mn7h9g1a:
   for jqxs6esj in zefqjg02:
    if jqxs6esj.type==pygame.MOUSEBUTTONUP and jqxs6esj.button==1:
     self.d1ieixwc=True
 def do2m71hs(self,gmoft6yr):
  if self.mn7h9g1a:
   ugez7bh2=self.u9el8hl8
   wg25cfzf=self.kkzruin3
  else:
   ugez7bh2=self.ugez7bh2
   wg25cfzf=self.wg25cfzf
  gmoft6yr.blit(self.d46aexl6,(self.f8rtm4j3.qxb7gbdg,self.f8rtm4j3.n01uyzpd+3))
  pygame.draw.rect(gmoft6yr,ugez7bh2,self.f8rtm4j3,border_radius=self.border_radius)
  sv5f1bcp=3 if self.mn7h9g1a else 1
  pygame.draw.rect(gmoft6yr,wg25cfzf,self.f8rtm4j3,border_radius=self.border_radius,width=sv5f1bcp)
  zs3kkv9r=tp0lvsnu.get(self.kind)
  a1tbrwr9=0
  if zs3kkv9r:
   eqrl1n75=pygame.Rect(self.f8rtm4j3.qxb7gbdg,self.f8rtm4j3.n01uyzpd,7,self.f8rtm4j3.height)
   pygame.draw.rect(gmoft6yr,zs3kkv9r,eqrl1n75,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   a1tbrwr9=4
  h4m2ec8r=self.f8rtm4j3.centerx+a1tbrwr9
  if self.subtitle and self.sub_font:
   kn5gjj8m=self.g70e3p15.render(self.v7g0iiji,True,(15,15,20))
   uoloeazc=self.sub_font.render(self.subtitle,True,(50,50,55))
   z7pwo6cm=kn5gjj8m.get_height()+uoloeazc.get_height()+2
   frhzn4kg=self.f8rtm4j3.centery-z7pwo6cm//2
   xvzc7d2k=frhzn4kg+kn5gjj8m.get_height()+2
   gmoft6yr.blit(kn5gjj8m,(h4m2ec8r-kn5gjj8m.get_width()//2,frhzn4kg))
   gmoft6yr.blit(uoloeazc,(h4m2ec8r-uoloeazc.get_width()//2,xvzc7d2k))
  else:
   xo2t8fy6=self.g70e3p15.render(self.v7g0iiji,True,(15,15,20))
   width=xo2t8fy6.get_width()
   height=xo2t8fy6.get_height()
   gmoft6yr.blit(xo2t8fy6,(h4m2ec8r-width//2,self.f8rtm4j3.centery-height//2))
