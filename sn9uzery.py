import pygame
from c8v341on import*
pygame.init()
class wa11dpg8:
 gokc1msy=46
 def __init__(self,width,height,color,title=None,title_font=None,fdxj37c9=(60,60,75)):
  self.la3kkrzd=pygame.Rect((jdiuovw1-width)//2,(rla5ju9b-height)//2,width,height)
  self.color=color
  self.fdxj37c9=fdxj37c9
  self.title=title
  self.title_font=title_font
  self.cx41dntc=self.gokc1msy if title else 0
  self.zpajssuu=[]
  self.wzs13c9x=pygame.Surface((jdiuovw1,rla5ju9b),pygame.SRCALPHA)
  self.nxxjve3d=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.nxxjve3d,(0,0,0,90),self.nxxjve3d.get_rect(),border_radius=20)
 def add(self,wehlxslg):
  self.zpajssuu.append(wehlxslg)
 def pv4ykade(self,yg87oi0e):
  self.wzs13c9x.fill((0,0,0,150))
  yg87oi0e.blit(self.wzs13c9x,(0,0))
  yg87oi0e.blit(self.nxxjve3d,(self.la3kkrzd.jh55hewl-12,self.la3kkrzd.rm0j36tc-8))
  pygame.draw.rect(yg87oi0e,self.color,self.la3kkrzd,border_radius=16)
  pygame.draw.rect(yg87oi0e,self.fdxj37c9,self.la3kkrzd,width=2,border_radius=16)
  if self.title and self.title_font:
   arjn2hz2=self.title_font.render(self.title,True,(30,30,45))
   yg87oi0e.blit(arjn2hz2,(self.la3kkrzd.centerx-arjn2hz2.get_width()//2,self.la3kkrzd.rm0j36tc+12))
   l9enulqj=self.la3kkrzd.rm0j36tc+self.cx41dntc-4
   pygame.draw.line(yg87oi0e,self.fdxj37c9,(self.la3kkrzd.jh55hewl+18,l9enulqj),(self.la3kkrzd.right-18,l9enulqj),1)
  for wehlxslg in self.zpajssuu:
   wehlxslg.pv4ykade(yg87oi0e)
tp0lvsnu={'zmygy0':(46,160,67),'y3lxch':(230,126,34),'wzwl3z':(52,120,200)}
class hc58drc1:
 def __init__(self,jh55hewl,rm0j36tc,width,height,amcixdu1,fdxj37c9,damdvlnk,m20u9isy,mq7nc85e,wigbiaf9,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.la3kkrzd=pygame.Rect(jh55hewl,rm0j36tc,width,height)
  self.amcixdu1=amcixdu1
  self.fdxj37c9=fdxj37c9
  self.damdvlnk=damdvlnk
  self.m20u9isy=m20u9isy
  self.mq7nc85e=mq7nc85e
  self.wigbiaf9=wigbiaf9
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.fekrcppr=False
  self.zfb7r31q=False
  self.kind=kind
  self.key=key
  self.nxxjve3d=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.nxxjve3d,(0,0,0,55),self.nxxjve3d.get_rect(),border_radius=border_radius)
 def update(self,fp47b42g):
  (crsb4gf1,sye0a4ab)=pygame.mouse.get_pos()
  self.fekrcppr=self.la3kkrzd.collidepoint(crsb4gf1,sye0a4ab)
  self.zfb7r31q=False
  if self.fekrcppr:
   for uc1xi04b in fp47b42g:
    if uc1xi04b.type==pygame.MOUSEBUTTONUP and uc1xi04b.button==1:
     self.zfb7r31q=True
 def pv4ykade(self,yg87oi0e):
  if self.fekrcppr:
   amcixdu1=self.damdvlnk
   fdxj37c9=self.m20u9isy
  else:
   amcixdu1=self.amcixdu1
   fdxj37c9=self.fdxj37c9
  yg87oi0e.blit(self.nxxjve3d,(self.la3kkrzd.jh55hewl,self.la3kkrzd.rm0j36tc+3))
  pygame.draw.rect(yg87oi0e,amcixdu1,self.la3kkrzd,border_radius=self.border_radius)
  c0hpmnz1=3 if self.fekrcppr else 1
  pygame.draw.rect(yg87oi0e,fdxj37c9,self.la3kkrzd,border_radius=self.border_radius,width=c0hpmnz1)
  g7s55j2o=tp0lvsnu.get(self.kind)
  rk36m8jv=0
  if g7s55j2o:
   zs3kkv9r=pygame.Rect(self.la3kkrzd.jh55hewl,self.la3kkrzd.rm0j36tc,7,self.la3kkrzd.height)
   pygame.draw.rect(yg87oi0e,g7s55j2o,zs3kkv9r,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   rk36m8jv=4
  yoyohaz7=self.la3kkrzd.centerx+rk36m8jv
  if self.subtitle and self.sub_font:
   arjn2hz2=self.mq7nc85e.render(self.wigbiaf9,True,(15,15,20))
   y9ayq6ww=self.sub_font.render(self.subtitle,True,(50,50,55))
   o9zqyahu=arjn2hz2.get_height()+y9ayq6ww.get_height()+2
   n8sa3idy=self.la3kkrzd.centery-o9zqyahu//2
   byl68ntk=n8sa3idy+arjn2hz2.get_height()+2
   yg87oi0e.blit(arjn2hz2,(yoyohaz7-arjn2hz2.get_width()//2,n8sa3idy))
   yg87oi0e.blit(y9ayq6ww,(yoyohaz7-y9ayq6ww.get_width()//2,byl68ntk))
  else:
   qcd81twh=self.mq7nc85e.render(self.wigbiaf9,True,(15,15,20))
   width=qcd81twh.get_width()
   height=qcd81twh.get_height()
   yg87oi0e.blit(qcd81twh,(yoyohaz7-width//2,self.la3kkrzd.centery-height//2))
