import pygame
from e87f8tsx import*
pygame.init()
class oohp6vz4:
 rla5ju9b=46
 def __init__(self,width,height,color,title=None,title_font=None,exvaj2k8=(60,60,75)):
  self.pllkstn3=pygame.Rect((ygspk9p3-width)//2,(tp0lvsnu-height)//2,width,height)
  self.color=color
  self.exvaj2k8=exvaj2k8
  self.title=title
  self.title_font=title_font
  self.nvuprt77=self.rla5ju9b if title else 0
  self.wa45hvgo=[]
  self.wc7x0h3j=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
  self.yp3cyazb=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.yp3cyazb,(0,0,0,90),self.yp3cyazb.get_rect(),border_radius=20)
 def add(self,aicvqy5i):
  self.wa45hvgo.append(aicvqy5i)
 def dw7nh8rq(self,byl68ntk):
  self.wc7x0h3j.fill((0,0,0,150))
  byl68ntk.blit(self.wc7x0h3j,(0,0))
  byl68ntk.blit(self.yp3cyazb,(self.pllkstn3.j1kfk7y6-12,self.pllkstn3.f1bl08kg-8))
  pygame.draw.rect(byl68ntk,self.color,self.pllkstn3,border_radius=16)
  pygame.draw.rect(byl68ntk,self.exvaj2k8,self.pllkstn3,width=2,border_radius=16)
  if self.title and self.title_font:
   htgsiwg0=self.title_font.render(self.title,True,(30,30,45))
   byl68ntk.blit(htgsiwg0,(self.pllkstn3.centerx-htgsiwg0.get_width()//2,self.pllkstn3.f1bl08kg+12))
   sygvwopl=self.pllkstn3.f1bl08kg+self.nvuprt77-4
   pygame.draw.line(byl68ntk,self.exvaj2k8,(self.pllkstn3.j1kfk7y6+18,sygvwopl),(self.pllkstn3.right-18,sygvwopl),1)
  for aicvqy5i in self.wa45hvgo:
   aicvqy5i.dw7nh8rq(byl68ntk)
ibps3y70={'khkf28':(46,160,67),'hipi78':(230,126,34),'vhbef4':(52,120,200)}
class hc58drc1:
 def __init__(self,j1kfk7y6,f1bl08kg,width,height,hfb85p86,exvaj2k8,xk7n8la1,xd8wz42o,m8lw2qit,gsrtwlxd,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.pllkstn3=pygame.Rect(j1kfk7y6,f1bl08kg,width,height)
  self.hfb85p86=hfb85p86
  self.exvaj2k8=exvaj2k8
  self.xk7n8la1=xk7n8la1
  self.xd8wz42o=xd8wz42o
  self.m8lw2qit=m8lw2qit
  self.gsrtwlxd=gsrtwlxd
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.n3rlkte4=False
  self.iektsg7f=False
  self.kind=kind
  self.key=key
  self.yp3cyazb=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.yp3cyazb,(0,0,0,55),self.yp3cyazb.get_rect(),border_radius=border_radius)
 def update(self,xq46nouh):
  (oc4kl8cg,mfc79m96)=pygame.mouse.get_pos()
  self.n3rlkte4=self.pllkstn3.collidepoint(oc4kl8cg,mfc79m96)
  self.iektsg7f=False
  if self.n3rlkte4:
   for mqxlm5q2 in xq46nouh:
    if mqxlm5q2.type==pygame.MOUSEBUTTONUP and mqxlm5q2.button==1:
     self.iektsg7f=True
 def dw7nh8rq(self,byl68ntk):
  if self.n3rlkte4:
   hfb85p86=self.xk7n8la1
   exvaj2k8=self.xd8wz42o
  else:
   hfb85p86=self.hfb85p86
   exvaj2k8=self.exvaj2k8
  byl68ntk.blit(self.yp3cyazb,(self.pllkstn3.j1kfk7y6,self.pllkstn3.f1bl08kg+3))
  pygame.draw.rect(byl68ntk,hfb85p86,self.pllkstn3,border_radius=self.border_radius)
  tk0qtl3q=3 if self.n3rlkte4 else 1
  pygame.draw.rect(byl68ntk,exvaj2k8,self.pllkstn3,border_radius=self.border_radius,width=tk0qtl3q)
  e5x4w7ky=ibps3y70.get(self.kind)
  bu4xszjn=0
  if e5x4w7ky:
   gp84dyt9=pygame.Rect(self.pllkstn3.j1kfk7y6,self.pllkstn3.f1bl08kg,7,self.pllkstn3.height)
   pygame.draw.rect(byl68ntk,e5x4w7ky,gp84dyt9,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   bu4xszjn=4
  qxb7gbdg=self.pllkstn3.centerx+bu4xszjn
  if self.subtitle and self.sub_font:
   htgsiwg0=self.m8lw2qit.render(self.gsrtwlxd,True,(15,15,20))
   oa47sh2s=self.sub_font.render(self.subtitle,True,(50,50,55))
   x3n27m5p=htgsiwg0.get_height()+oa47sh2s.get_height()+2
   n01uyzpd=self.pllkstn3.centery-x3n27m5p//2
   wigbiaf9=n01uyzpd+htgsiwg0.get_height()+2
   byl68ntk.blit(htgsiwg0,(qxb7gbdg-htgsiwg0.get_width()//2,n01uyzpd))
   byl68ntk.blit(oa47sh2s,(qxb7gbdg-oa47sh2s.get_width()//2,wigbiaf9))
  else:
   rk36m8jv=self.m8lw2qit.render(self.gsrtwlxd,True,(15,15,20))
   width=rk36m8jv.get_width()
   height=rk36m8jv.get_height()
   byl68ntk.blit(rk36m8jv,(qxb7gbdg-width//2,self.pllkstn3.centery-height//2))
