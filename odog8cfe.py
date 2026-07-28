import pygame
from omerbyea import*
pygame.init()
class oohp6vz4:
 rla5ju9b=46
 def __init__(self,width,height,color,title=None,title_font=None,uj64qhks=(60,60,75)):
  self.cq2q4qer=pygame.Rect((cqoldfor-width)//2,(tp0lvsnu-height)//2,width,height)
  self.color=color
  self.uj64qhks=uj64qhks
  self.title=title
  self.title_font=title_font
  self.ftrflqbm=self.rla5ju9b if title else 0
  self.ub68rerv=[]
  self.rzewviyt=pygame.Surface((cqoldfor,tp0lvsnu),pygame.SRCALPHA)
  self.cb2uuijn=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.cb2uuijn,(0,0,0,90),self.cb2uuijn.get_rect(),border_radius=20)
 def add(self,boih5csk):
  self.ub68rerv.append(boih5csk)
 def tnz61231(self,q3n2qb6g):
  self.rzewviyt.fill((0,0,0,150))
  q3n2qb6g.blit(self.rzewviyt,(0,0))
  q3n2qb6g.blit(self.cb2uuijn,(self.cq2q4qer.eolaq665-12,self.cq2q4qer.t5ivrocv-8))
  pygame.draw.rect(q3n2qb6g,self.color,self.cq2q4qer,border_radius=16)
  pygame.draw.rect(q3n2qb6g,self.uj64qhks,self.cq2q4qer,width=2,border_radius=16)
  if self.title and self.title_font:
   zgomf9pm=self.title_font.render(self.title,True,(30,30,45))
   q3n2qb6g.blit(zgomf9pm,(self.cq2q4qer.centerx-zgomf9pm.get_width()//2,self.cq2q4qer.t5ivrocv+12))
   mygfliji=self.cq2q4qer.t5ivrocv+self.ftrflqbm-4
   pygame.draw.line(q3n2qb6g,self.uj64qhks,(self.cq2q4qer.eolaq665+18,mygfliji),(self.cq2q4qer.right-18,mygfliji),1)
  for boih5csk in self.ub68rerv:
   boih5csk.tnz61231(q3n2qb6g)
ibps3y70={'hipi78':(46,160,67),'orc1yo':(230,126,34),'xbtfbs':(52,120,200)}
class hc58drc1:
 def __init__(self,eolaq665,t5ivrocv,width,height,k7zgf9q5,uj64qhks,xd8wz42o,n3rlkte4,mpyxdw2z,bu4xszjn,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.cq2q4qer=pygame.Rect(eolaq665,t5ivrocv,width,height)
  self.k7zgf9q5=k7zgf9q5
  self.uj64qhks=uj64qhks
  self.xd8wz42o=xd8wz42o
  self.n3rlkte4=n3rlkte4
  self.mpyxdw2z=mpyxdw2z
  self.bu4xszjn=bu4xszjn
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.zmybd2qe=False
  self.vw6m7b5c=False
  self.kind=kind
  self.key=key
  self.cb2uuijn=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.cb2uuijn,(0,0,0,55),self.cb2uuijn.get_rect(),border_radius=border_radius)
 def update(self,eatvzkhi):
  (mfc79m96,wb7f6fdh)=pygame.mouse.get_pos()
  self.zmybd2qe=self.cq2q4qer.collidepoint(mfc79m96,wb7f6fdh)
  self.vw6m7b5c=False
  if self.zmybd2qe:
   for xq46nouh in eatvzkhi:
    if xq46nouh.type==pygame.MOUSEBUTTONUP and xq46nouh.button==1:
     self.vw6m7b5c=True
 def tnz61231(self,q3n2qb6g):
  if self.zmybd2qe:
   k7zgf9q5=self.xd8wz42o
   uj64qhks=self.n3rlkte4
  else:
   k7zgf9q5=self.k7zgf9q5
   uj64qhks=self.uj64qhks
  q3n2qb6g.blit(self.cb2uuijn,(self.cq2q4qer.eolaq665,self.cq2q4qer.t5ivrocv+3))
  pygame.draw.rect(q3n2qb6g,k7zgf9q5,self.cq2q4qer,border_radius=self.border_radius)
  gn89qkns=3 if self.zmybd2qe else 1
  pygame.draw.rect(q3n2qb6g,uj64qhks,self.cq2q4qer,border_radius=self.border_radius,width=gn89qkns)
  gp84dyt9=ibps3y70.get(self.kind)
  ucu7onz3=0
  if gp84dyt9:
   lcj883dh=pygame.Rect(self.cq2q4qer.eolaq665,self.cq2q4qer.t5ivrocv,7,self.cq2q4qer.height)
   pygame.draw.rect(q3n2qb6g,gp84dyt9,lcj883dh,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   ucu7onz3=4
  tza7x73q=self.cq2q4qer.centerx+ucu7onz3
  if self.subtitle and self.sub_font:
   zgomf9pm=self.mpyxdw2z.render(self.bu4xszjn,True,(15,15,20))
   wigbiaf9=self.sub_font.render(self.subtitle,True,(50,50,55))
   jslulzfy=zgomf9pm.get_height()+wigbiaf9.get_height()+2
   kt94ow3l=self.cq2q4qer.centery-jslulzfy//2
   yoyohaz7=kt94ow3l+zgomf9pm.get_height()+2
   q3n2qb6g.blit(zgomf9pm,(tza7x73q-zgomf9pm.get_width()//2,kt94ow3l))
   q3n2qb6g.blit(wigbiaf9,(tza7x73q-wigbiaf9.get_width()//2,yoyohaz7))
  else:
   gqoagsus=self.mpyxdw2z.render(self.bu4xszjn,True,(15,15,20))
   width=gqoagsus.get_width()
   height=gqoagsus.get_height()
   q3n2qb6g.blit(gqoagsus,(tza7x73q-width//2,self.cq2q4qer.centery-height//2))
