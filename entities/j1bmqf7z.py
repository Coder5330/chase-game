import pygame
def u15pdtz9(color,q7i6yuj7):
 return tuple((max(0,min(255,int(i20cv3tl*q7i6yuj7)))for i20cv3tl in color[:3]))
def w4rcb1kj(v0rxxf36):
 if v0rxxf36>0.6:
  return(60,200,80)
 if v0rxxf36>0.3:
  return(230,200,40)
 return(220,60,60)
def vhuds3qs(q3n2qb6g,eolaq665,t5ivrocv,width,v0rxxf36,height=6,fg=None,bg=(45,45,50)):
 v0rxxf36=max(0.0,min(1.0,v0rxxf36))
 if fg is None:
  fg=w4rcb1kj(v0rxxf36)
 xu9ymszd=height//2
 i0x65muf=pygame.Rect(eolaq665,t5ivrocv,width,height)
 pygame.draw.rect(q3n2qb6g,bg,i0x65muf,border_radius=xu9ymszd)
 if v0rxxf36>0:
  mytn02yc=max(height,int(width*v0rxxf36))
  pygame.draw.rect(q3n2qb6g,fg,(eolaq665,t5ivrocv,mytn02yc,height),border_radius=xu9ymszd)
 pygame.draw.rect(q3n2qb6g,(20,20,20),i0x65muf,width=1,border_radius=xu9ymszd)
