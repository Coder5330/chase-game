import pygame
def z3olfark(kybwmlun,g8kk791z):
 return tuple((max(0,min(255,int(l57p6bkl*g8kk791z)))for l57p6bkl in kybwmlun[:3]))
def nubmxnsz(pf0i9g5d):
 if pf0i9g5d>0.6:
  return(60,200,80)
 if pf0i9g5d>0.3:
  return(230,200,40)
 return(220,60,60)
def ep6beffl(uj64qhks,yypp5zp7,tjy1o2rn,width,pf0i9g5d,height=6,fg=None,bg=(45,45,50)):
 pf0i9g5d=max(0.0,min(1.0,pf0i9g5d))
 if fg is None:
  fg=nubmxnsz(pf0i9g5d)
 y8bv78hu=height//2
 v982n2at=pygame.Rect(yypp5zp7,tjy1o2rn,width,height)
 pygame.draw.rect(uj64qhks,bg,v982n2at,border_radius=y8bv78hu)
 if pf0i9g5d>0:
  wzlm72je=max(height,int(width*pf0i9g5d))
  pygame.draw.rect(uj64qhks,fg,(yypp5zp7,tjy1o2rn,wzlm72je,height),border_radius=y8bv78hu)
 pygame.draw.rect(uj64qhks,(20,20,20),v982n2at,width=1,border_radius=y8bv78hu)
