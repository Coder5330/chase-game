import pygame
from r1yohmi9 import*
pygame.init()
class oohp6vz4:
 rla5ju9b=46
 def __init__(self,width,height,color,title=None,title_font=None,a2wspofv=(60,60,75)):
  self.nxxjve3d=pygame.Rect((ygspk9p3-width)//2,(tp0lvsnu-height)//2,width,height)
  self.color=color
  self.a2wspofv=a2wspofv
  self.title=title
  self.title_font=title_font
  self.vmxb9yo1=self.rla5ju9b if title else 0
  self.xd8wz42o=[]
  self.qtzk3ny9=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
  self.g1b3d505=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.g1b3d505,(0,0,0,90),self.g1b3d505.get_rect(),border_radius=20)
 def add(self,v15cqzcu):
  self.xd8wz42o.append(v15cqzcu)
 def fo75rh8l(self,vmy9x8sy):
  self.qtzk3ny9.fill((0,0,0,150))
  vmy9x8sy.blit(self.qtzk3ny9,(0,0))
  vmy9x8sy.blit(self.g1b3d505,(self.nxxjve3d.un9sz6rv-12,self.nxxjve3d.ehet25lz-8))
  pygame.draw.rect(vmy9x8sy,self.color,self.nxxjve3d,border_radius=16)
  pygame.draw.rect(vmy9x8sy,self.a2wspofv,self.nxxjve3d,width=2,border_radius=16)
  if self.title and self.title_font:
   x9h0dxho=self.title_font.render(self.title,True,(30,30,45))
   vmy9x8sy.blit(x9h0dxho,(self.nxxjve3d.centerx-x9h0dxho.get_width()//2,self.nxxjve3d.ehet25lz+12))
   vt6om1fb=self.nxxjve3d.ehet25lz+self.vmxb9yo1-4
   pygame.draw.line(vmy9x8sy,self.a2wspofv,(self.nxxjve3d.un9sz6rv+18,vt6om1fb),(self.nxxjve3d.right-18,vt6om1fb),1)
  for v15cqzcu in self.xd8wz42o:
   v15cqzcu.fo75rh8l(vmy9x8sy)
ibps3y70={'bohxs7':(46,160,67),'agbl2q':(230,126,34),'mjz6us':(52,120,200)}
class hc58drc1:
 def __init__(self,un9sz6rv,ehet25lz,width,height,wzs13c9x,a2wspofv,ftrflqbm,arhnuxor,ao4izasn,wyk03o4g,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.nxxjve3d=pygame.Rect(un9sz6rv,ehet25lz,width,height)
  self.wzs13c9x=wzs13c9x
  self.a2wspofv=a2wspofv
  self.ftrflqbm=ftrflqbm
  self.arhnuxor=arhnuxor
  self.ao4izasn=ao4izasn
  self.wyk03o4g=wyk03o4g
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.w4rcb1kj=False
  self.iie0rnuj=False
  self.kind=kind
  self.key=key
  self.g1b3d505=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.g1b3d505,(0,0,0,55),self.g1b3d505.get_rect(),border_radius=border_radius)
 def update(self,aicvqy5i):
  (k3z6bz8u,s8438tgb)=pygame.mouse.get_pos()
  self.w4rcb1kj=self.nxxjve3d.collidepoint(k3z6bz8u,s8438tgb)
  self.iie0rnuj=False
  if self.w4rcb1kj:
   for g70e3p15 in aicvqy5i:
    if g70e3p15.type==pygame.MOUSEBUTTONUP and g70e3p15.button==1:
     self.iie0rnuj=True
 def fo75rh8l(self,vmy9x8sy):
  if self.w4rcb1kj:
   wzs13c9x=self.ftrflqbm
   a2wspofv=self.arhnuxor
  else:
   wzs13c9x=self.wzs13c9x
   a2wspofv=self.a2wspofv
  vmy9x8sy.blit(self.g1b3d505,(self.nxxjve3d.un9sz6rv,self.nxxjve3d.ehet25lz+3))
  pygame.draw.rect(vmy9x8sy,wzs13c9x,self.nxxjve3d,border_radius=self.border_radius)
  bq349dxb=3 if self.w4rcb1kj else 1
  pygame.draw.rect(vmy9x8sy,a2wspofv,self.nxxjve3d,border_radius=self.border_radius,width=bq349dxb)
  j1i2hgj1=ibps3y70.get(self.kind)
  ra9kepad=0
  if j1i2hgj1:
   yx4w6xlp=pygame.Rect(self.nxxjve3d.un9sz6rv,self.nxxjve3d.ehet25lz,7,self.nxxjve3d.height)
   pygame.draw.rect(vmy9x8sy,j1i2hgj1,yx4w6xlp,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   ra9kepad=4
  jdqqzrlf=self.nxxjve3d.centerx+ra9kepad
  if self.subtitle and self.sub_font:
   x9h0dxho=self.ao4izasn.render(self.wyk03o4g,True,(15,15,20))
   nv23gxj0=self.sub_font.render(self.subtitle,True,(50,50,55))
   awnwlc83=x9h0dxho.get_height()+nv23gxj0.get_height()+2
   j7f00ter=self.nxxjve3d.centery-awnwlc83//2
   k7vcneas=j7f00ter+x9h0dxho.get_height()+2
   vmy9x8sy.blit(x9h0dxho,(jdqqzrlf-x9h0dxho.get_width()//2,j7f00ter))
   vmy9x8sy.blit(nv23gxj0,(jdqqzrlf-nv23gxj0.get_width()//2,k7vcneas))
  else:
   rserev36=self.ao4izasn.render(self.wyk03o4g,True,(15,15,20))
   width=rserev36.get_width()
   height=rserev36.get_height()
   vmy9x8sy.blit(rserev36,(jdqqzrlf-width//2,self.nxxjve3d.centery-height//2))
