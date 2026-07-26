import pygame
from ygm55ff1 import*
pygame.init()
class rv86wzs3:
 tp0lvsnu=46
 def __init__(self,width,height,kybwmlun,title=None,title_font=None,j1ldqnk2=(60,60,75)):
  self.zdan085r=pygame.Rect((qxaprpn6-width)//2,(ibps3y70-height)//2,width,height)
  self.kybwmlun=kybwmlun
  self.j1ldqnk2=j1ldqnk2
  self.title=title
  self.title_font=title_font
  self.xuu13i59=self.tp0lvsnu if title else 0
  self.mytn02yc=[]
  self.pvasifpw=pygame.Surface((qxaprpn6,ibps3y70),pygame.SRCALPHA)
  self.vt26ys44=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.vt26ys44,(0,0,0,90),self.vt26ys44.get_rect(),border_radius=20)
 def add(self,l9enulqj):
  self.mytn02yc.append(l9enulqj)
 def izhwy9he(self,uj64qhks):
  self.pvasifpw.fill((0,0,0,150))
  uj64qhks.blit(self.pvasifpw,(0,0))
  uj64qhks.blit(self.vt26ys44,(self.zdan085r.yypp5zp7-12,self.zdan085r.tjy1o2rn-8))
  pygame.draw.rect(uj64qhks,self.kybwmlun,self.zdan085r,border_radius=16)
  pygame.draw.rect(uj64qhks,self.j1ldqnk2,self.zdan085r,width=2,border_radius=16)
  if self.title and self.title_font:
   y9ayq6ww=self.title_font.render(self.title,True,(30,30,45))
   uj64qhks.blit(y9ayq6ww,(self.zdan085r.centerx-y9ayq6ww.get_width()//2,self.zdan085r.tjy1o2rn+12))
   clkqzfpq=self.zdan085r.tjy1o2rn+self.xuu13i59-4
   pygame.draw.line(uj64qhks,self.j1ldqnk2,(self.zdan085r.yypp5zp7+18,clkqzfpq),(self.zdan085r.right-18,clkqzfpq),1)
  for l9enulqj in self.mytn02yc:
   l9enulqj.izhwy9he(uj64qhks)
gncxll4z={'h7kr0a':(46,160,67),'r8imoe':(230,126,34),'ceb875':(52,120,200)}
class hc58drc1:
 def __init__(self,yypp5zp7,tjy1o2rn,width,height,wppsfnko,j1ldqnk2,u0q0mftg,r98s4c3b,rzewviyt,stv18kgy,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.zdan085r=pygame.Rect(yypp5zp7,tjy1o2rn,width,height)
  self.wppsfnko=wppsfnko
  self.j1ldqnk2=j1ldqnk2
  self.u0q0mftg=u0q0mftg
  self.r98s4c3b=r98s4c3b
  self.rzewviyt=rzewviyt
  self.stv18kgy=stv18kgy
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.ao4izasn=False
  self.f8wquuy5=False
  self.kind=kind
  self.key=key
  self.vt26ys44=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.vt26ys44,(0,0,0,55),self.vt26ys44.get_rect(),border_radius=border_radius)
 def update(self,qbbz2sf6):
  (je11e9ft,avfmh07w)=pygame.mouse.get_pos()
  self.ao4izasn=self.zdan085r.collidepoint(je11e9ft,avfmh07w)
  self.f8wquuy5=False
  if self.ao4izasn:
   for do2m71hs in qbbz2sf6:
    if do2m71hs.type==pygame.MOUSEBUTTONUP and do2m71hs.button==1:
     self.f8wquuy5=True
 def izhwy9he(self,uj64qhks):
  if self.ao4izasn:
   wppsfnko=self.u0q0mftg
   j1ldqnk2=self.r98s4c3b
  else:
   wppsfnko=self.wppsfnko
   j1ldqnk2=self.j1ldqnk2
  uj64qhks.blit(self.vt26ys44,(self.zdan085r.yypp5zp7,self.zdan085r.tjy1o2rn+3))
  pygame.draw.rect(uj64qhks,wppsfnko,self.zdan085r,border_radius=self.border_radius)
  e5x4w7ky=3 if self.ao4izasn else 1
  pygame.draw.rect(uj64qhks,j1ldqnk2,self.zdan085r,border_radius=self.border_radius,width=e5x4w7ky)
  jdiuovw1=gncxll4z.get(self.kind)
  iaq7b7v1=0
  if jdiuovw1:
   mqp49kwv=pygame.Rect(self.zdan085r.yypp5zp7,self.zdan085r.tjy1o2rn,7,self.zdan085r.height)
   pygame.draw.rect(uj64qhks,jdiuovw1,mqp49kwv,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   iaq7b7v1=4
  f80ebkjf=self.zdan085r.centerx+iaq7b7v1
  if self.subtitle and self.sub_font:
   y9ayq6ww=self.rzewviyt.render(self.stv18kgy,True,(15,15,20))
   d1hm38ks=self.sub_font.render(self.subtitle,True,(50,50,55))
   yp3cyazb=y9ayq6ww.get_height()+d1hm38ks.get_height()+2
   byl68ntk=self.zdan085r.centery-yp3cyazb//2
   wd6r30oj=byl68ntk+y9ayq6ww.get_height()+2
   uj64qhks.blit(y9ayq6ww,(f80ebkjf-y9ayq6ww.get_width()//2,byl68ntk))
   uj64qhks.blit(d1hm38ks,(f80ebkjf-d1hm38ks.get_width()//2,wd6r30oj))
  else:
   nbwye6qv=self.rzewviyt.render(self.stv18kgy,True,(15,15,20))
   width=nbwye6qv.get_width()
   height=nbwye6qv.get_height()
   uj64qhks.blit(nbwye6qv,(f80ebkjf-width//2,self.zdan085r.centery-height//2))
