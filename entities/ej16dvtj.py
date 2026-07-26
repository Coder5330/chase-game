import pygame
def avfmh07w(nqimqodp,xp8mgyn2):
 return tuple((max(0,min(255,int(x52qc1iy*xp8mgyn2)))for x52qc1iy in nqimqodp[:3]))
def u1jhuwb6(gkz2u2tn):
 if gkz2u2tn>0.6:
  return(60,200,80)
 if gkz2u2tn>0.3:
  return(230,200,40)
 return(220,60,60)
def uysal8m1(je11e9ft,gp6orsnc,cknfu84x,width,gkz2u2tn,height=6,fg=None,bg=(45,45,50)):
 gkz2u2tn=max(0.0,min(1.0,gkz2u2tn))
 if fg is None:
  fg=u1jhuwb6(gkz2u2tn)
 vpbwhvnz=height//2
 u8c2jwoc=pygame.Rect(gp6orsnc,cknfu84x,width,height)
 pygame.draw.rect(je11e9ft,bg,u8c2jwoc,border_radius=vpbwhvnz)
 if gkz2u2tn>0:
  i20cv3tl=max(height,int(width*gkz2u2tn))
  pygame.draw.rect(je11e9ft,fg,(gp6orsnc,cknfu84x,i20cv3tl,height),border_radius=vpbwhvnz)
 pygame.draw.rect(je11e9ft,(20,20,20),u8c2jwoc,width=1,border_radius=vpbwhvnz)
