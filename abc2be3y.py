import pygame
from z1yhxso7 import*
pygame.init()
class yswjckjl:
 gokc1msy=46
 def __init__(self,width,height,color,title=None,title_font=None,mu4fmpkx=(60,60,75)):
  self.wgcl9lcq=pygame.Rect((rrcbpljd-width)//2,(rla5ju9b-height)//2,width,height)
  self.color=color
  self.mu4fmpkx=mu4fmpkx
  self.title=title
  self.title_font=title_font
  self.a8lw2lm3=self.gokc1msy if title else 0
  self.nd31k9qm=[]
  self.i01nouht=pygame.Surface((rrcbpljd,rla5ju9b),pygame.SRCALPHA)
  self.gg7oq2zd=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.gg7oq2zd,(0,0,0,90),self.gg7oq2zd.get_rect(),border_radius=20)
 def add(self,sygvwopl):
  self.nd31k9qm.append(sygvwopl)
 def wzlm72je(self,ukshy8nb):
  self.i01nouht.fill((0,0,0,150))
  ukshy8nb.blit(self.i01nouht,(0,0))
  ukshy8nb.blit(self.gg7oq2zd,(self.wgcl9lcq.jslulzfy-12,self.wgcl9lcq.zpfb3hn1-8))
  pygame.draw.rect(ukshy8nb,self.color,self.wgcl9lcq,border_radius=16)
  pygame.draw.rect(ukshy8nb,self.mu4fmpkx,self.wgcl9lcq,width=2,border_radius=16)
  if self.title and self.title_font:
   qxt6ridl=self.title_font.render(self.title,True,(30,30,45))
   ukshy8nb.blit(qxt6ridl,(self.wgcl9lcq.centerx-qxt6ridl.get_width()//2,self.wgcl9lcq.zpfb3hn1+12))
   eohswq40=self.wgcl9lcq.zpfb3hn1+self.a8lw2lm3-4
   pygame.draw.line(ukshy8nb,self.mu4fmpkx,(self.wgcl9lcq.jslulzfy+18,eohswq40),(self.wgcl9lcq.right-18,eohswq40),1)
  for sygvwopl in self.nd31k9qm:
   sygvwopl.wzlm72je(ukshy8nb)
tp0lvsnu={'en1x2g':(46,160,67),'yc1nlc':(230,126,34),'jr87iy':(52,120,200)}
class hc58drc1:
 def __init__(self,jslulzfy,zpfb3hn1,width,height,izhwy9he,mu4fmpkx,we4xyf9i,ftlpq2wg,mqxlm5q2,l0sqg4ei,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.wgcl9lcq=pygame.Rect(jslulzfy,zpfb3hn1,width,height)
  self.izhwy9he=izhwy9he
  self.mu4fmpkx=mu4fmpkx
  self.we4xyf9i=we4xyf9i
  self.ftlpq2wg=ftlpq2wg
  self.mqxlm5q2=mqxlm5q2
  self.l0sqg4ei=l0sqg4ei
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.vpbwhvnz=False
  self.clkqzfpq=False
  self.kind=kind
  self.key=key
  self.gg7oq2zd=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.gg7oq2zd,(0,0,0,55),self.gg7oq2zd.get_rect(),border_radius=border_radius)
 def update(self,gubmc97c):
  (mnwxuj3a,chx3d43e)=pygame.mouse.get_pos()
  self.vpbwhvnz=self.wgcl9lcq.collidepoint(mnwxuj3a,chx3d43e)
  self.clkqzfpq=False
  if self.vpbwhvnz:
   for ouuylaja in gubmc97c:
    if ouuylaja.type==pygame.MOUSEBUTTONUP and ouuylaja.button==1:
     self.clkqzfpq=True
 def wzlm72je(self,ukshy8nb):
  if self.vpbwhvnz:
   izhwy9he=self.we4xyf9i
   mu4fmpkx=self.ftlpq2wg
  else:
   izhwy9he=self.izhwy9he
   mu4fmpkx=self.mu4fmpkx
  ukshy8nb.blit(self.gg7oq2zd,(self.wgcl9lcq.jslulzfy,self.wgcl9lcq.zpfb3hn1+3))
  pygame.draw.rect(ukshy8nb,izhwy9he,self.wgcl9lcq,border_radius=self.border_radius)
  uww5wfcp=3 if self.vpbwhvnz else 1
  pygame.draw.rect(ukshy8nb,mu4fmpkx,self.wgcl9lcq,border_radius=self.border_radius,width=uww5wfcp)
  iy6qktc8=tp0lvsnu.get(self.kind)
  rb1s9dwd=0
  if iy6qktc8:
   sk8yqk94=pygame.Rect(self.wgcl9lcq.jslulzfy,self.wgcl9lcq.zpfb3hn1,7,self.wgcl9lcq.height)
   pygame.draw.rect(ukshy8nb,iy6qktc8,sk8yqk94,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   rb1s9dwd=4
  i7zcgdc5=self.wgcl9lcq.centerx+rb1s9dwd
  if self.subtitle and self.sub_font:
   qxt6ridl=self.mqxlm5q2.render(self.l0sqg4ei,True,(15,15,20))
   ysqg8x80=self.sub_font.render(self.subtitle,True,(50,50,55))
   kc1fjotg=qxt6ridl.get_height()+ysqg8x80.get_height()+2
   njka34mq=self.wgcl9lcq.centery-kc1fjotg//2
   p7b1ijiy=njka34mq+qxt6ridl.get_height()+2
   ukshy8nb.blit(qxt6ridl,(i7zcgdc5-qxt6ridl.get_width()//2,njka34mq))
   ukshy8nb.blit(ysqg8x80,(i7zcgdc5-ysqg8x80.get_width()//2,p7b1ijiy))
  else:
   w8wj0uun=self.mqxlm5q2.render(self.l0sqg4ei,True,(15,15,20))
   width=w8wj0uun.get_width()
   height=w8wj0uun.get_height()
   ukshy8nb.blit(w8wj0uun,(i7zcgdc5-width//2,self.wgcl9lcq.centery-height//2))
