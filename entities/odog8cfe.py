import pygame
def byl68ntk(color,v76ub7l8):
 return tuple((max(0,min(255,int(vqnpcenl*v76ub7l8)))for vqnpcenl in color[:3]))
def rk2u1rsu(fd6rupw2):
 if fd6rupw2>0.6:
  return(60,200,80)
 if fd6rupw2>0.3:
  return(230,200,40)
 return(220,60,60)
def gubmc97c(gxlk8wru,x,y,width,fd6rupw2,height=6,fg=None,bg=(45,45,50)):
 fd6rupw2=max(0.0,min(1.0,fd6rupw2))
 if fg is None:
  fg=rk2u1rsu(fd6rupw2)
 myrp5ge0=height//2
 qbm1enf3=pygame.Rect(x,y,width,height)
 pygame.draw.rect(gxlk8wru,bg,qbm1enf3,border_radius=myrp5ge0)
 if fd6rupw2>0:
  x9bp4m18=max(height,int(width*fd6rupw2))
  pygame.draw.rect(gxlk8wru,fg,(x,y,x9bp4m18,height),border_radius=myrp5ge0)
 pygame.draw.rect(gxlk8wru,(20,20,20),qbm1enf3,width=1,border_radius=myrp5ge0)
