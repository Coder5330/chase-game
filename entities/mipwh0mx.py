import pygame
def xwk2rv23(color,vhuds3qs):
 return tuple((max(0,min(255,int(wppsfnko*vhuds3qs)))for wppsfnko in color[:3]))
def v76ub7l8(he9p3jpx):
 if he9p3jpx>0.6:
  return(60,200,80)
 if he9p3jpx>0.3:
  return(230,200,40)
 return(220,60,60)
def qbbz2sf6(npejzhya,rm0j36tc,tza7x73q,width,he9p3jpx,height=6,fg=None,bg=(45,45,50)):
 he9p3jpx=max(0.0,min(1.0,he9p3jpx))
 if fg is None:
  fg=v76ub7l8(he9p3jpx)
 la3kkrzd=height//2
 vj8yrddp=pygame.Rect(rm0j36tc,tza7x73q,width,height)
 pygame.draw.rect(npejzhya,bg,vj8yrddp,border_radius=la3kkrzd)
 if he9p3jpx>0:
  gubmc97c=max(height,int(width*he9p3jpx))
  pygame.draw.rect(npejzhya,fg,(rm0j36tc,tza7x73q,gubmc97c,height),border_radius=la3kkrzd)
 pygame.draw.rect(npejzhya,(20,20,20),vj8yrddp,width=1,border_radius=la3kkrzd)
