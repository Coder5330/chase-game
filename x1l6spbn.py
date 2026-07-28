import pygame
from entfk7or import*
pygame.init()
class oohp6vz4:
 rla5ju9b=46
 def __init__(self,width,height,color,title=None,title_font=None,f8rtm4j3=(60,60,75)):
  self.npcxa5s0=pygame.Rect((ygspk9p3-width)//2,(tp0lvsnu-height)//2,width,height)
  self.color=color
  self.f8rtm4j3=f8rtm4j3
  self.title=title
  self.title_font=title_font
  self.nvuprt77=self.rla5ju9b if title else 0
  self.wa45hvgo=[]
  self.rzewviyt=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
  self.q3n2qb6g=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.q3n2qb6g,(0,0,0,90),self.q3n2qb6g.get_rect(),border_radius=20)
 def add(self,boih5csk):
  self.wa45hvgo.append(boih5csk)
 def tnz61231(self,h8s2ftom):
  self.rzewviyt.fill((0,0,0,150))
  h8s2ftom.blit(self.rzewviyt,(0,0))
  h8s2ftom.blit(self.q3n2qb6g,(self.npcxa5s0.w2sq3b9s-12,self.npcxa5s0.owdz09wf-8))
  pygame.draw.rect(h8s2ftom,self.color,self.npcxa5s0,border_radius=16)
  pygame.draw.rect(h8s2ftom,self.f8rtm4j3,self.npcxa5s0,width=2,border_radius=16)
  if self.title and self.title_font:
   htgsiwg0=self.title_font.render(self.title,True,(30,30,45))
   h8s2ftom.blit(htgsiwg0,(self.npcxa5s0.centerx-htgsiwg0.get_width()//2,self.npcxa5s0.owdz09wf+12))
   mygfliji=self.npcxa5s0.owdz09wf+self.nvuprt77-4
   pygame.draw.line(h8s2ftom,self.f8rtm4j3,(self.npcxa5s0.w2sq3b9s+18,mygfliji),(self.npcxa5s0.right-18,mygfliji),1)
  for boih5csk in self.wa45hvgo:
   boih5csk.tnz61231(h8s2ftom)
ibps3y70={'sce4qg':(46,160,67),'gv4k00':(230,126,34),'tn1th1':(52,120,200)}
class hc58drc1:
 def __init__(self,w2sq3b9s,owdz09wf,width,height,pa8s8hmb,f8rtm4j3,xd8wz42o,n3rlkte4,m8lw2qit,gsrtwlxd,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.npcxa5s0=pygame.Rect(w2sq3b9s,owdz09wf,width,height)
  self.pa8s8hmb=pa8s8hmb
  self.f8rtm4j3=f8rtm4j3
  self.xd8wz42o=xd8wz42o
  self.n3rlkte4=n3rlkte4
  self.m8lw2qit=m8lw2qit
  self.gsrtwlxd=gsrtwlxd
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.zmybd2qe=False
  self.u1jhuwb6=False
  self.kind=kind
  self.key=key
  self.q3n2qb6g=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.q3n2qb6g,(0,0,0,55),self.q3n2qb6g.get_rect(),border_radius=border_radius)
 def update(self,xq46nouh):
  (zdan085r,mmn32u1i)=pygame.mouse.get_pos()
  self.zmybd2qe=self.npcxa5s0.collidepoint(zdan085r,mmn32u1i)
  self.u1jhuwb6=False
  if self.zmybd2qe:
   for mqxlm5q2 in xq46nouh:
    if mqxlm5q2.type==pygame.MOUSEBUTTONUP and mqxlm5q2.button==1:
     self.u1jhuwb6=True
 def tnz61231(self,h8s2ftom):
  if self.zmybd2qe:
   pa8s8hmb=self.xd8wz42o
   f8rtm4j3=self.n3rlkte4
  else:
   pa8s8hmb=self.pa8s8hmb
   f8rtm4j3=self.f8rtm4j3
  h8s2ftom.blit(self.q3n2qb6g,(self.npcxa5s0.w2sq3b9s,self.npcxa5s0.owdz09wf+3))
  pygame.draw.rect(h8s2ftom,pa8s8hmb,self.npcxa5s0,border_radius=self.border_radius)
  nd6357oo=3 if self.zmybd2qe else 1
  pygame.draw.rect(h8s2ftom,f8rtm4j3,self.npcxa5s0,border_radius=self.border_radius,width=nd6357oo)
  i4fejgxa=ibps3y70.get(self.kind)
  bu4xszjn=0
  if i4fejgxa:
   am2vajep=pygame.Rect(self.npcxa5s0.w2sq3b9s,self.npcxa5s0.owdz09wf,7,self.npcxa5s0.height)
   pygame.draw.rect(h8s2ftom,i4fejgxa,am2vajep,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   bu4xszjn=4
  qxb7gbdg=self.npcxa5s0.centerx+bu4xszjn
  if self.subtitle and self.sub_font:
   htgsiwg0=self.m8lw2qit.render(self.gsrtwlxd,True,(15,15,20))
   rr9u1oe5=self.sub_font.render(self.subtitle,True,(50,50,55))
   hjkuuhcl=htgsiwg0.get_height()+rr9u1oe5.get_height()+2
   n01uyzpd=self.npcxa5s0.centery-hjkuuhcl//2
   d0qzfhom=n01uyzpd+htgsiwg0.get_height()+2
   h8s2ftom.blit(htgsiwg0,(qxb7gbdg-htgsiwg0.get_width()//2,n01uyzpd))
   h8s2ftom.blit(rr9u1oe5,(qxb7gbdg-rr9u1oe5.get_width()//2,d0qzfhom))
  else:
   p7pchcbn=self.m8lw2qit.render(self.gsrtwlxd,True,(15,15,20))
   width=p7pchcbn.get_width()
   height=p7pchcbn.get_height()
   h8s2ftom.blit(p7pchcbn,(qxb7gbdg-width//2,self.npcxa5s0.centery-height//2))
