import pygame
def ukshy8nb(color,nubmxnsz):
 return tuple((max(0,min(255,int(gn89qkns*nubmxnsz)))for gn89qkns in color[:3]))
def u9el8hl8(v6xii5p5):
 if v6xii5p5>0.6:
  return(60,200,80)
 if v6xii5p5>0.3:
  return(230,200,40)
 return(220,60,60)
def wc7x0h3j(cq2q4qer,d5ixva1n,nngmx1gm,width,v6xii5p5,height=6,fg=None,bg=(45,45,50)):
 v6xii5p5=max(0.0,min(1.0,v6xii5p5))
 if fg is None:
  fg=u9el8hl8(v6xii5p5)
 rgdej31g=height//2
 vvslh9bh=pygame.Rect(d5ixva1n,nngmx1gm,width,height)
 pygame.draw.rect(cq2q4qer,bg,vvslh9bh,border_radius=rgdej31g)
 if v6xii5p5>0:
  kx74d0gj=max(height,int(width*v6xii5p5))
  pygame.draw.rect(cq2q4qer,fg,(d5ixva1n,nngmx1gm,kx74d0gj,height),border_radius=rgdej31g)
 pygame.draw.rect(cq2q4qer,(20,20,20),vvslh9bh,width=1,border_radius=rgdej31g)
