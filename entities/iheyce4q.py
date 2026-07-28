import pygame
def rk43safy(color,mqxlm5q2):
 return tuple((max(0,min(255,int(tacj4t0s*mqxlm5q2)))for tacj4t0s in color[:3]))
def onqyyf9r(ytb9xxay):
 if ytb9xxay>0.6:
  return(60,200,80)
 if ytb9xxay>0.3:
  return(230,200,40)
 return(220,60,60)
def x875aud9(vmy9x8sy,un9sz6rv,ehet25lz,width,ytb9xxay,height=6,fg=None,bg=(45,45,50)):
 ytb9xxay=max(0.0,min(1.0,ytb9xxay))
 if fg is None:
  fg=onqyyf9r(ytb9xxay)
 xasez2nx=height//2
 divsolml=pygame.Rect(un9sz6rv,ehet25lz,width,height)
 pygame.draw.rect(vmy9x8sy,bg,divsolml,border_radius=xasez2nx)
 if ytb9xxay>0:
  s4rxyj38=max(height,int(width*ytb9xxay))
  pygame.draw.rect(vmy9x8sy,fg,(un9sz6rv,ehet25lz,s4rxyj38,height),border_radius=xasez2nx)
 pygame.draw.rect(vmy9x8sy,(20,20,20),divsolml,width=1,border_radius=xasez2nx)
