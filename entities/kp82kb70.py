import pygame
def ytb9xxay(color,b36htf4p):
 return tuple((max(0,min(255,int(bq349dxb*b36htf4p)))for bq349dxb in color[:3]))
def q7i6yuj7(njxurgow):
 if njxurgow>0.6:
  return(60,200,80)
 if njxurgow>0.3:
  return(230,200,40)
 return(220,60,60)
def do2m71hs(yg87oi0e,jh55hewl,rm0j36tc,width,njxurgow,height=6,fg=None,bg=(45,45,50)):
 njxurgow=max(0.0,min(1.0,njxurgow))
 if fg is None:
  fg=q7i6yuj7(njxurgow)
 y8dd2255=height//2
 nqimqodp=pygame.Rect(jh55hewl,rm0j36tc,width,height)
 pygame.draw.rect(yg87oi0e,bg,nqimqodp,border_radius=y8dd2255)
 if njxurgow>0:
  ouuylaja=max(height,int(width*njxurgow))
  pygame.draw.rect(yg87oi0e,fg,(jh55hewl,rm0j36tc,ouuylaja,height),border_radius=y8dd2255)
 pygame.draw.rect(yg87oi0e,(20,20,20),nqimqodp,width=1,border_radius=y8dd2255)
