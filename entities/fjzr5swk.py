import pygame
def gxlk8wru(color,cx41dntc):
 return tuple((max(0,min(255,int(x5m9j98c*cx41dntc)))for x5m9j98c in color[:3]))
def ftrflqbm(tj0nmeoq):
 if tj0nmeoq>0.6:
  return(60,200,80)
 if tj0nmeoq>0.3:
  return(230,200,40)
 return(220,60,60)
def b36htf4p(uwxrum2l,x3zo7utx,cjy62zee,width,tj0nmeoq,height=6,fg=None,bg=(45,45,50)):
 tj0nmeoq=max(0.0,min(1.0,tj0nmeoq))
 if fg is None:
  fg=ftrflqbm(tj0nmeoq)
 d46aexl6=height//2
 u23y30ys=pygame.Rect(x3zo7utx,cjy62zee,width,height)
 pygame.draw.rect(uwxrum2l,bg,u23y30ys,border_radius=d46aexl6)
 if tj0nmeoq>0:
  v76ub7l8=max(height,int(width*tj0nmeoq))
  pygame.draw.rect(uwxrum2l,fg,(x3zo7utx,cjy62zee,v76ub7l8,height),border_radius=d46aexl6)
 pygame.draw.rect(uwxrum2l,(20,20,20),u23y30ys,width=1,border_radius=d46aexl6)
