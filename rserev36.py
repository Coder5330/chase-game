import pygame
from d0qzfhom import*
pygame.init()
class hyihair4:
 zy0ifznb=46
 def __init__(self,width,height,nqimqodp,title=None,title_font=None,cjn2fomd=(60,60,75)):
  self.semqgy27=pygame.Rect((khl1n13j-width)//2,(pi3qk2ia-height)//2,width,height)
  self.nqimqodp=nqimqodp
  self.cjn2fomd=cjn2fomd
  self.title=title
  self.title_font=title_font
  self.iektsg7f=self.zy0ifznb if title else 0
  self.wehlxslg=[]
  self.divsolml=pygame.Surface((khl1n13j,pi3qk2ia),pygame.SRCALPHA)
  self.k2ixivzk=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.k2ixivzk,(0,0,0,90),self.k2ixivzk.get_rect(),border_radius=20)
 def add(self,f32ejx5t):
  self.wehlxslg.append(f32ejx5t)
 def llxxezdu(self,je11e9ft):
  self.divsolml.fill((0,0,0,150))
  je11e9ft.blit(self.divsolml,(0,0))
  je11e9ft.blit(self.k2ixivzk,(self.semqgy27.gp6orsnc-12,self.semqgy27.cknfu84x-8))
  pygame.draw.rect(je11e9ft,self.nqimqodp,self.semqgy27,border_radius=16)
  pygame.draw.rect(je11e9ft,self.cjn2fomd,self.semqgy27,width=2,border_radius=16)
  if self.title and self.title_font:
   wg25cfzf=self.title_font.render(self.title,True,(30,30,45))
   je11e9ft.blit(wg25cfzf,(self.semqgy27.centerx-wg25cfzf.get_width()//2,self.semqgy27.cknfu84x+12))
   wppsfnko=self.semqgy27.cknfu84x+self.iektsg7f-4
   pygame.draw.line(je11e9ft,self.cjn2fomd,(self.semqgy27.gp6orsnc+18,wppsfnko),(self.semqgy27.right-18,wppsfnko),1)
  for f32ejx5t in self.wehlxslg:
   f32ejx5t.llxxezdu(je11e9ft)
gokc1msy={'lb1iji':(46,160,67),'i4jtgx':(230,126,34),'k5qmkt':(52,120,200)}
class q7vren93:
 def __init__(self,gp6orsnc,cknfu84x,width,height,tp2ex5t5,cjn2fomd,pv4ykade,i01nouht,uos0fb4y,hu9n79gi,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.semqgy27=pygame.Rect(gp6orsnc,cknfu84x,width,height)
  self.tp2ex5t5=tp2ex5t5
  self.cjn2fomd=cjn2fomd
  self.pv4ykade=pv4ykade
  self.i01nouht=i01nouht
  self.uos0fb4y=uos0fb4y
  self.hu9n79gi=hu9n79gi
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.cnqt3wve=False
  self.i4fejgxa=False
  self.kind=kind
  self.key=key
  self.k2ixivzk=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.k2ixivzk,(0,0,0,55),self.k2ixivzk.get_rect(),border_radius=border_radius)
 def update(self,hugysm8t):
  (xq46nouh,eatvzkhi)=pygame.mouse.get_pos()
  self.cnqt3wve=self.semqgy27.collidepoint(xq46nouh,eatvzkhi)
  self.i4fejgxa=False
  if self.cnqt3wve:
   for pvasifpw in hugysm8t:
    if pvasifpw.type==pygame.MOUSEBUTTONUP and pvasifpw.button==1:
     self.i4fejgxa=True
 def llxxezdu(self,je11e9ft):
  if self.cnqt3wve:
   tp2ex5t5=self.pv4ykade
   cjn2fomd=self.i01nouht
  else:
   tp2ex5t5=self.tp2ex5t5
   cjn2fomd=self.cjn2fomd
  je11e9ft.blit(self.k2ixivzk,(self.semqgy27.gp6orsnc,self.semqgy27.cknfu84x+3))
  pygame.draw.rect(je11e9ft,tp2ex5t5,self.semqgy27,border_radius=self.border_radius)
  jmpioygg=3 if self.cnqt3wve else 1
  pygame.draw.rect(je11e9ft,cjn2fomd,self.semqgy27,border_radius=self.border_radius,width=jmpioygg)
  gdzr1yxr=gokc1msy.get(self.kind)
  s8438tgb=0
  if gdzr1yxr:
   zakoixnt=pygame.Rect(self.semqgy27.gp6orsnc,self.semqgy27.cknfu84x,7,self.semqgy27.height)
   pygame.draw.rect(je11e9ft,gdzr1yxr,zakoixnt,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   s8438tgb=4
  k3z6bz8u=self.semqgy27.centerx+s8438tgb
  if self.subtitle and self.sub_font:
   wg25cfzf=self.uos0fb4y.render(self.hu9n79gi,True,(15,15,20))
   vk3g84ut=self.sub_font.render(self.subtitle,True,(50,50,55))
   w8y72ivg=wg25cfzf.get_height()+vk3g84ut.get_height()+2
   d448n7od=self.semqgy27.centery-w8y72ivg//2
   dq2fa39e=d448n7od+wg25cfzf.get_height()+2
   je11e9ft.blit(wg25cfzf,(k3z6bz8u-wg25cfzf.get_width()//2,d448n7od))
   je11e9ft.blit(vk3g84ut,(k3z6bz8u-vk3g84ut.get_width()//2,dq2fa39e))
  else:
   chx3d43e=self.uos0fb4y.render(self.hu9n79gi,True,(15,15,20))
   width=chx3d43e.get_width()
   height=chx3d43e.get_height()
   je11e9ft.blit(chx3d43e,(k3z6bz8u-width//2,self.semqgy27.centery-height//2))
