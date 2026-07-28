import pygame
from vnbnqbnx import*
pygame.init()
class oohp6vz4:
 rla5ju9b=46
 def __init__(self,width,height,color,title=None,title_font=None,la3kkrzd=(60,60,75)):
  self.bdgbk2l0=pygame.Rect((ygspk9p3-width)//2,(tp0lvsnu-height)//2,width,height)
  self.color=color
  self.la3kkrzd=la3kkrzd
  self.title=title
  self.title_font=title_font
  self.vpbwhvnz=self.rla5ju9b if title else 0
  self.pcvsqame=[]
  self.rmm1zxyv=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
  self.stv18kgy=pygame.Surface((width+24,height+24),pygame.SRCALPHA)
  pygame.draw.rect(self.stv18kgy,(0,0,0,90),self.stv18kgy.get_rect(),border_radius=20)
 def add(self,mq7nc85e):
  self.pcvsqame.append(mq7nc85e)
 def sygvwopl(self,g1b3d505):
  self.rmm1zxyv.fill((0,0,0,150))
  g1b3d505.blit(self.rmm1zxyv,(0,0))
  g1b3d505.blit(self.stv18kgy,(self.bdgbk2l0.iimoe0sy-12,self.bdgbk2l0.gdg1wjui-8))
  pygame.draw.rect(g1b3d505,self.color,self.bdgbk2l0,border_radius=16)
  pygame.draw.rect(g1b3d505,self.la3kkrzd,self.bdgbk2l0,width=2,border_radius=16)
  if self.title and self.title_font:
   ywcxz2ei=self.title_font.render(self.title,True,(30,30,45))
   g1b3d505.blit(ywcxz2ei,(self.bdgbk2l0.centerx-ywcxz2ei.get_width()//2,self.bdgbk2l0.gdg1wjui+12))
   fp47b42g=self.bdgbk2l0.gdg1wjui+self.vpbwhvnz-4
   pygame.draw.line(g1b3d505,self.la3kkrzd,(self.bdgbk2l0.iimoe0sy+18,fp47b42g),(self.bdgbk2l0.right-18,fp47b42g),1)
  for mq7nc85e in self.pcvsqame:
   mq7nc85e.sygvwopl(g1b3d505)
ibps3y70={'zhbgcj':(46,160,67),'pca7zv':(230,126,34),'upgba9':(52,120,200)}
class hc58drc1:
 def __init__(self,iimoe0sy,gdg1wjui,width,height,rk8r2ykc,la3kkrzd,wvpw232u,rktlzkj4,q7i6yuj7,i33e1i1p,border_radius,subtitle=None,sub_font=None,kind=None,key=None):
  self.bdgbk2l0=pygame.Rect(iimoe0sy,gdg1wjui,width,height)
  self.rk8r2ykc=rk8r2ykc
  self.la3kkrzd=la3kkrzd
  self.wvpw232u=wvpw232u
  self.rktlzkj4=rktlzkj4
  self.q7i6yuj7=q7i6yuj7
  self.i33e1i1p=i33e1i1p
  self.subtitle=subtitle
  self.sub_font=sub_font
  self.border_radius=border_radius
  self.v3e1ocjx=False
  self.oqse3tv1=False
  self.kind=kind
  self.key=key
  self.stv18kgy=pygame.Surface((width,height),pygame.SRCALPHA)
  pygame.draw.rect(self.stv18kgy,(0,0,0,55),self.stv18kgy.get_rect(),border_radius=border_radius)
 def update(self,kx74d0gj):
  (jl90pxrl,w8y72ivg)=pygame.mouse.get_pos()
  self.v3e1ocjx=self.bdgbk2l0.collidepoint(jl90pxrl,w8y72ivg)
  self.oqse3tv1=False
  if self.v3e1ocjx:
   for zqcootnj in kx74d0gj:
    if zqcootnj.type==pygame.MOUSEBUTTONUP and zqcootnj.button==1:
     self.oqse3tv1=True
 def sygvwopl(self,g1b3d505):
  if self.v3e1ocjx:
   rk8r2ykc=self.wvpw232u
   la3kkrzd=self.rktlzkj4
  else:
   rk8r2ykc=self.rk8r2ykc
   la3kkrzd=self.la3kkrzd
  g1b3d505.blit(self.stv18kgy,(self.bdgbk2l0.iimoe0sy,self.bdgbk2l0.gdg1wjui+3))
  pygame.draw.rect(g1b3d505,rk8r2ykc,self.bdgbk2l0,border_radius=self.border_radius)
  yw6zbnz8=3 if self.v3e1ocjx else 1
  pygame.draw.rect(g1b3d505,la3kkrzd,self.bdgbk2l0,border_radius=self.border_radius,width=yw6zbnz8)
  e5x4w7ky=ibps3y70.get(self.kind)
  j7f00ter=0
  if e5x4w7ky:
   gp84dyt9=pygame.Rect(self.bdgbk2l0.iimoe0sy,self.bdgbk2l0.gdg1wjui,7,self.bdgbk2l0.height)
   pygame.draw.rect(g1b3d505,e5x4w7ky,gp84dyt9,border_top_left_radius=self.border_radius,border_bottom_left_radius=self.border_radius)
   j7f00ter=4
  x9h0dxho=self.bdgbk2l0.centerx+j7f00ter
  if self.subtitle and self.sub_font:
   ywcxz2ei=self.q7i6yuj7.render(self.i33e1i1p,True,(15,15,20))
   qy3vg6v5=self.sub_font.render(self.subtitle,True,(50,50,55))
   bu4xszjn=ywcxz2ei.get_height()+qy3vg6v5.get_height()+2
   r212pgym=self.bdgbk2l0.centery-bu4xszjn//2
   rserev36=r212pgym+ywcxz2ei.get_height()+2
   g1b3d505.blit(ywcxz2ei,(x9h0dxho-ywcxz2ei.get_width()//2,r212pgym))
   g1b3d505.blit(qy3vg6v5,(x9h0dxho-qy3vg6v5.get_width()//2,rserev36))
  else:
   p2nv01zd=self.q7i6yuj7.render(self.i33e1i1p,True,(15,15,20))
   width=p2nv01zd.get_width()
   height=p2nv01zd.get_height()
   g1b3d505.blit(p2nv01zd,(x9h0dxho-width//2,self.bdgbk2l0.centery-height//2))
