import pygame
from o100vhmy import*
pygame.init()
class wa11dpg8:
 gokc1msy=46
 def __init__(self,width,height,color,title=None,title_font=None,s8438tgb=(60,60,75)):
  self.zflse45b=pygame.Rect((mqp49kwv-width)//2,(rla5ju9b-height)//2,width,height)
  self.color=color
  self.s8438tgb=s8438tgb
  self.title=title
  self.title_font=title_font
  self.azc4xl99=self.gokc1msy if title else 0
  self.gsmdzqcb=[]
  self.oqse3tv1=pygame.Surface((mqp49kwv,rla5ju9b),pygame.SRCALPHA)
  self.hay64yfd=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.hay64yfd,(0,0,0,90),self.hay64yfd.get_rect(),border_radius=20)
 def add(self,rmm1zxyv):
  self.gsmdzqcb.append(rmm1zxyv)
 def i01nouht(self,npejzhya):
  self.oqse3tv1.fill((0,0,0,150))
  npejzhya.blit(self.oqse3tv1,(0,0))
  npejzhya.blit(self.hay64yfd,(self.zflse45b.rm0j36tc-12,self.zflse45b.tza7x73q-8))
  pygame.draw.rect(npejzhya,self.color,self.zflse45b,border_radius=16)
  pygame.draw.rect(npejzhya,self.s8438tgb,self.zflse45b,width=2,border_radius=16)
  if self.title and self.title_font:
   a1tbrwr9=self.title_font.render(self.title,True,(30,30,45))
   npejzhya.blit(a1tbrwr9,(self.zflse45b.centerx-a1tbrwr9.get_width()//2,self.zflse45b.tza7x73q+12))
   hfb85p86=self.zflse45b.tza7x73q+self.azc4xl99-4
   pygame.draw.line(npejzhya,self.s8438tgb,(self.zflse45b.rm0j36tc+18,hfb85p86),(self.zflse45b.right-18,hfb85p86),1)
  for rmm1zxyv in self.gsmdzqcb:
   rmm1zxyv.i01nouht(npejzhya)
tp0lvsnu={'m44c68':(46,160,67),'ntxrgn':(230,126,34),'mviifr':(52,120,200)}
class hc58drc1:
 def __init__(self,rm0j36tc,tza7x73q,width,height,ebt3g2qz,s8438tgb,cn7zrwqe,a8lw2lm3,le9oe941,mu118qqv,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.zflse45b=pygame.Rect(rm0j36tc,tza7x73q,width,height)
  self.ebt3g2qz=ebt3g2qz
  self.s8438tgb=s8438tgb
  self.cn7zrwqe=cn7zrwqe
  self.a8lw2lm3=a8lw2lm3
  self.le9oe941=le9oe941
  self.mu118qqv=mu118qqv
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.u9el8hl8=False
  self.tacj4t0s=False
  self.kind=kind
  self.key=key
  self.hay64yfd=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.hay64yfd,(0,0,0,55),self.hay64yfd.get_rect(),border_radius=border_radius)
 def update(self,x875aud9):
  (nii6l3ue,v6g298cq)=pygame.mouse.get_pos()
  self.u9el8hl8=self.zflse45b.collidepoint(nii6l3ue,v6g298cq)
  self.tacj4t0s=False
  if self.u9el8hl8:
   for fp47b42g in x875aud9:
    if fp47b42g.type==pygame.MOUSEBUTTONUP and fp47b42g.button==1:
     self.tacj4t0s=True
 def i01nouht(self,npejzhya):
  if self.u9el8hl8:
   ebt3g2qz=self.cn7zrwqe
   s8438tgb=self.a8lw2lm3
  else:
   ebt3g2qz=self.ebt3g2qz
   s8438tgb=self.s8438tgb
  npejzhya.blit(self.hay64yfd,(self.zflse45b.rm0j36tc,self.zflse45b.tza7x73q+3))
  pygame.draw.rect(npejzhya,ebt3g2qz,self.zflse45b,border_radius=self.border_radius)
  sv5f1bcp=3 if self.u9el8hl8 else 1
  pygame.draw.rect(npejzhya,s8438tgb,self.zflse45b,border_radius=self.border_radius,width=sv5f1bcp)
  zs3kkv9r=tp0lvsnu.get(self.kind)
  n8sa3idy=0
  if zs3kkv9r:
   eqrl1n75=pygame.Rect(self.zflse45b.rm0j36tc,self.zflse45b.tza7x73q,7,self.zflse45b.height)
   pygame.draw.rect(npejzhya,zs3kkv9r,eqrl1n75,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   n8sa3idy=4
  arjn2hz2=self.zflse45b.centerx+n8sa3idy
  if self.subtitle and self.sub_font:
   a1tbrwr9=self.le9oe941.render(self.mu118qqv,True,(15,15,20))
   qcd81twh=self.sub_font.render(self.subtitle,True,(50,50,55))
   wfhj4d0j=a1tbrwr9.get_height()+qcd81twh.get_height()+2
   s5r96khu=self.zflse45b.centery-wfhj4d0j//2
   u15pdtz9=s5r96khu+a1tbrwr9.get_height()+2
   npejzhya.blit(a1tbrwr9,(arjn2hz2-a1tbrwr9.get_width()//2,s5r96khu))
   npejzhya.blit(qcd81twh,(arjn2hz2-qcd81twh.get_width()//2,u15pdtz9))
  else:
   cb2uuijn=self.le9oe941.render(self.mu118qqv,True,(15,15,20))
   width=cb2uuijn.get_width()
   height=cb2uuijn.get_height()
   npejzhya.blit(cb2uuijn,(arjn2hz2-width//2,self.zflse45b.centery-height//2))
