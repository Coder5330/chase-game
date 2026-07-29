import pygame
def y9ayq6ww(color,q7i6yuj7):
 return tuple((max(0,min(255,int(obc2nnuv*q7i6yuj7)))for obc2nnuv in color[:3]))
def w4rcb1kj(myrp5ge0):
 if myrp5ge0>0.6:
  return(60,200,80)
 if myrp5ge0>0.3:
  return(230,200,40)
 return(220,60,60)
def ouuylaja(h8s2ftom,x,y,width,myrp5ge0,height=6,fg=None,bg=(45,45,50)):
 myrp5ge0=max(0.0,min(1.0,myrp5ge0))
 if fg is None:
  fg=w4rcb1kj(myrp5ge0)
 tj0nmeoq=height//2
 giec4d14=pygame.Rect(x,y,width,height)
 pygame.draw.rect(h8s2ftom,bg,giec4d14,border_radius=tj0nmeoq)
 if myrp5ge0>0:
  mytn02yc=max(height,int(width*myrp5ge0))
  pygame.draw.rect(h8s2ftom,fg,(x,y,mytn02yc,height),border_radius=tj0nmeoq)
 pygame.draw.rect(h8s2ftom,(20,20,20),giec4d14,width=1,border_radius=tj0nmeoq)
