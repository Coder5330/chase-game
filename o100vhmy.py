import pygame
from i1arxabo import*
pygame.init()
class yswjckjl:
 gokc1msy=46
 def __init__(self,width,height,color,title=None,title_font=None,j0kgazu4=(60,60,75)):
  self.todsx4nx=pygame.Rect((dtx63cfl-width)//2,(rla5ju9b-height)//2,width,height)
  self.color=color
  self.j0kgazu4=j0kgazu4
  self.title=title
  self.title_font=title_font
  self.m8lw2qit=self.gokc1msy if title else 0
  self.semqgy27=[]
  self.rk8r2ykc=pygame.Surface((dtx63cfl,rla5ju9b),pygame.SRCALPHA)
  self.npcxa5s0=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.npcxa5s0,(0,0,0,90),self.npcxa5s0.get_rect(),border_radius=20)
 def add(self,uidlrye8):
  self.semqgy27.append(uidlrye8)
 def sl65wvjx(self,tj0nmeoq):
  self.rk8r2ykc.fill((0,0,0,150))
  tj0nmeoq.blit(self.rk8r2ykc,(0,0))
  tj0nmeoq.blit(self.npcxa5s0,(self.todsx4nx.htgsiwg0-12,self.todsx4nx.hhl1737s-8))
  pygame.draw.rect(tj0nmeoq,self.color,self.todsx4nx,border_radius=16)
  pygame.draw.rect(tj0nmeoq,self.j0kgazu4,self.todsx4nx,width=2,border_radius=16)
  if self.title and self.title_font:
   wfhj4d0j=self.title_font.render(self.title,True,(30,30,45))
   tj0nmeoq.blit(wfhj4d0j,(self.todsx4nx.centerx-wfhj4d0j.get_width()//2,self.todsx4nx.hhl1737s+12))
   do2m71hs=self.todsx4nx.hhl1737s+self.m8lw2qit-4
   pygame.draw.line(tj0nmeoq,self.j0kgazu4,(self.todsx4nx.htgsiwg0+18,do2m71hs),(self.todsx4nx.right-18,do2m71hs),1)
  for uidlrye8 in self.semqgy27:
   uidlrye8.sl65wvjx(tj0nmeoq)
tp0lvsnu={'qc6dr0':(46,160,67),'kp82kb':(230,126,34),'hpvwzo':(52,120,200)}
class hc58drc1:
 def __init__(self,htgsiwg0,hhl1737s,width,height,i20cv3tl,j0kgazu4,nyfkjfpn,o9ros7yt,qhkc856w,o9zqyahu,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.todsx4nx=pygame.Rect(htgsiwg0,hhl1737s,width,height)
  self.i20cv3tl=i20cv3tl
  self.j0kgazu4=j0kgazu4
  self.nyfkjfpn=nyfkjfpn
  self.o9ros7yt=o9ros7yt
  self.qhkc856w=qhkc856w
  self.o9zqyahu=o9zqyahu
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.z8z3v6di=False
  self.amcixdu1=False
  self.kind=kind
  self.key=key
  self.npcxa5s0=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.npcxa5s0,(0,0,0,55),self.npcxa5s0.get_rect(),border_radius=border_radius)
 def update(self,velos6zl):
  (hp89fkbi,qo6q0usw)=pygame.mouse.get_pos()
  self.z8z3v6di=self.todsx4nx.collidepoint(hp89fkbi,qo6q0usw)
  self.amcixdu1=False
  if self.z8z3v6di:
   for yjluujmi in velos6zl:
    if yjluujmi.type==pygame.MOUSEBUTTONUP and yjluujmi.button==1:
     self.amcixdu1=True
 def sl65wvjx(self,tj0nmeoq):
  if self.z8z3v6di:
   i20cv3tl=self.nyfkjfpn
   j0kgazu4=self.o9ros7yt
  else:
   i20cv3tl=self.i20cv3tl
   j0kgazu4=self.j0kgazu4
  tj0nmeoq.blit(self.npcxa5s0,(self.todsx4nx.htgsiwg0,self.todsx4nx.hhl1737s+3))
  pygame.draw.rect(tj0nmeoq,i20cv3tl,self.todsx4nx,border_radius=self.border_radius)
  rzs43c5b=3 if self.z8z3v6di else 1
  pygame.draw.rect(tj0nmeoq,j0kgazu4,self.todsx4nx,border_radius=self.border_radius,width=rzs43c5b)
  sld4d6af=tp0lvsnu.get(self.kind)
  frhzn4kg=0
  if sld4d6af:
   u8c2jwoc=pygame.Rect(self.todsx4nx.htgsiwg0,self.todsx4nx.hhl1737s,7,self.todsx4nx.height)
   pygame.draw.rect(tj0nmeoq,sld4d6af,u8c2jwoc,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   frhzn4kg=4
  kn5gjj8m=self.todsx4nx.centerx+frhzn4kg
  if self.subtitle and self.sub_font:
   wfhj4d0j=self.qhkc856w.render(self.o9zqyahu,True,(15,15,20))
   svt8k06m=self.sub_font.render(self.subtitle,True,(50,50,55))
   mlikwe4b=wfhj4d0j.get_height()+svt8k06m.get_height()+2
   lu7jae58=self.todsx4nx.centery-mlikwe4b//2
   n64fgwje=lu7jae58+wfhj4d0j.get_height()+2
   tj0nmeoq.blit(wfhj4d0j,(kn5gjj8m-wfhj4d0j.get_width()//2,lu7jae58))
   tj0nmeoq.blit(svt8k06m,(kn5gjj8m-svt8k06m.get_width()//2,n64fgwje))
  else:
   jyjhu8my=self.qhkc856w.render(self.o9zqyahu,True,(15,15,20))
   width=jyjhu8my.get_width()
   height=jyjhu8my.get_height()
   tj0nmeoq.blit(jyjhu8my,(kn5gjj8m-width//2,self.todsx4nx.centery-height//2))
