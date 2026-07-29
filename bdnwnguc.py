import pygame
from jggz62fe import*
pygame.init()
class yur7ko64:
 rla5ju9b=46
 def __init__(self,width,height,color,title=None,title_font=None,cknfu84x=(60,60,75)):
  self.xu9ymszd=pygame.Rect((cqoldfor-width)//2,(tp0lvsnu-height)//2,width,height)
  self.color=color
  self.cknfu84x=cknfu84x
  self.title=title
  self.title_font=title_font
  self.arhnuxor=self.rla5ju9b if title else 0
  self.q5amln4p=[]
  self.fo75rh8l=pygame.Surface((cqoldfor,tp0lvsnu),pygame.SRCALPHA)
  self.qcd81twh=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.qcd81twh,(0,0,0,90),self.qcd81twh.get_rect(),border_radius=20)
 def add(self,qhkc856w):
  self.q5amln4p.append(qhkc856w)
 def b36htf4p(self,gxlk8wru):
  self.fo75rh8l.fill((0,0,0,150))
  gxlk8wru.blit(self.fo75rh8l,(0,0))
  gxlk8wru.blit(self.qcd81twh,(self.xu9ymszd.x-12,self.xu9ymszd.y-8))
  pygame.draw.rect(gxlk8wru,self.color,self.xu9ymszd,border_radius=16)
  pygame.draw.rect(gxlk8wru,self.cknfu84x,self.xu9ymszd,width=2,border_radius=16)
  if self.title and self.title_font:
   htgsiwg0=self.title_font.render(self.title,True,(30,30,45))
   gxlk8wru.blit(htgsiwg0,(self.xu9ymszd.centerx-htgsiwg0.get_width()//2,self.xu9ymszd.y+12))
   velos6zl=self.xu9ymszd.y+self.arhnuxor-4
   pygame.draw.line(gxlk8wru,self.cknfu84x,(self.xu9ymszd.x+18,velos6zl),(self.xu9ymszd.right-18,velos6zl),1)
  for qhkc856w in self.q5amln4p:
   qhkc856w.b36htf4p(gxlk8wru)
ibps3y70={'n5nhqr':(46,160,67),'sce4qg':(230,126,34),'ujqigy':(52,120,200)}
class hc58drc1:
 def __init__(self,x,y,width,height,i01nouht,cknfu84x,zmybd2qe,fpa8hyex,cjn2fomd,gsrtwlxd,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.xu9ymszd=pygame.Rect(x,y,width,height)
  self.i01nouht=i01nouht
  self.cknfu84x=cknfu84x
  self.zmybd2qe=zmybd2qe
  self.fpa8hyex=fpa8hyex
  self.cjn2fomd=cjn2fomd
  self.gsrtwlxd=gsrtwlxd
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.f55dmcxx=False
  self.bfoqmf5l=False
  self.kind=kind
  self.key=key
  self.qcd81twh=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.qcd81twh,(0,0,0,55),self.qcd81twh.get_rect(),border_radius=border_radius)
 def update(self,s4rxyj38):
  (oc4kl8cg,mfc79m96)=pygame.mouse.get_pos()
  self.f55dmcxx=self.xu9ymszd.collidepoint(oc4kl8cg,mfc79m96)
  self.bfoqmf5l=False
  if self.f55dmcxx:
   for eatvzkhi in s4rxyj38:
    if eatvzkhi.type==pygame.MOUSEBUTTONUP and eatvzkhi.button==1:
     self.bfoqmf5l=True
 def b36htf4p(self,gxlk8wru):
  if self.f55dmcxx:
   i01nouht=self.zmybd2qe
   cknfu84x=self.fpa8hyex
  else:
   i01nouht=self.i01nouht
   cknfu84x=self.cknfu84x
  gxlk8wru.blit(self.qcd81twh,(self.xu9ymszd.x,self.xu9ymszd.y+3))
  pygame.draw.rect(gxlk8wru,i01nouht,self.xu9ymszd,border_radius=self.border_radius)
  zfb7r31q=3 if self.f55dmcxx else 1
  pygame.draw.rect(gxlk8wru,cknfu84x,self.xu9ymszd,border_radius=self.border_radius,width=zfb7r31q)
  d0r2sds8=ibps3y70.get(self.kind)
  bu4xszjn=0
  if d0r2sds8:
   b06xkxb9=pygame.Rect(self.xu9ymszd.x,self.xu9ymszd.y,7,self.xu9ymszd.height)
   pygame.draw.rect(gxlk8wru,d0r2sds8,b06xkxb9,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   bu4xszjn=4
  qxb7gbdg=self.xu9ymszd.centerx+bu4xszjn
  if self.subtitle and self.sub_font:
   htgsiwg0=self.cjn2fomd.render(self.gsrtwlxd,True,(15,15,20))
   rr9u1oe5=self.sub_font.render(self.subtitle,True,(50,50,55))
   hjkuuhcl=htgsiwg0.get_height()+rr9u1oe5.get_height()+2
   n01uyzpd=self.xu9ymszd.centery-hjkuuhcl//2
   d0qzfhom=n01uyzpd+htgsiwg0.get_height()+2
   gxlk8wru.blit(htgsiwg0,(qxb7gbdg-htgsiwg0.get_width()//2,n01uyzpd))
   gxlk8wru.blit(rr9u1oe5,(qxb7gbdg-rr9u1oe5.get_width()//2,d0qzfhom))
  else:
   p7pchcbn=self.cjn2fomd.render(self.gsrtwlxd,True,(15,15,20))
   width=p7pchcbn.get_width()
   height=p7pchcbn.get_height()
   gxlk8wru.blit(p7pchcbn,(qxb7gbdg-width//2,self.xu9ymszd.centery-height//2))
