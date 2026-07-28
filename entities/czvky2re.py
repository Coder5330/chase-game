import pygame
def qertb74r(color,kx74d0gj):
 return tuple((max(0,min(255,int(nd6357oo*kx74d0gj)))for nd6357oo in color[:3]))
def xqzpky32(upprat08):
 if upprat08>0.6:
  return(60,200,80)
 if upprat08>0.3:
  return(230,200,40)
 return(220,60,60)
def fo75rh8l(gg7oq2zd,qic1l7dy,vsjchzjq,width,upprat08,height=6,fg=None,bg=(45,45,50)):
 upprat08=max(0.0,min(1.0,upprat08))
 if fg is None:
  fg=xqzpky32(upprat08)
 g1g1r1dw=height//2
 rzs43c5b=pygame.Rect(qic1l7dy,vsjchzjq,width,height)
 pygame.draw.rect(gg7oq2zd,bg,rzs43c5b,border_radius=g1g1r1dw)
 if upprat08>0:
  yrivh6t1=max(height,int(width*upprat08))
  pygame.draw.rect(gg7oq2zd,fg,(qic1l7dy,vsjchzjq,yrivh6t1,height),border_radius=g1g1r1dw)
 pygame.draw.rect(gg7oq2zd,(20,20,20),rzs43c5b,width=1,border_radius=g1g1r1dw)
