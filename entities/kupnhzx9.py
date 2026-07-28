import pygame
def cb2uuijn(color,v76ub7l8):
 return tuple((max(0,min(255,int(i20cv3tl*v76ub7l8)))for i20cv3tl in color[:3]))
def rk2u1rsu(tbxf445c):
 if tbxf445c>0.6:
  return(60,200,80)
 if tbxf445c>0.3:
  return(230,200,40)
 return(220,60,60)
def ouuylaja(u15pdtz9,owdz09wf,lb4y4k7b,width,tbxf445c,height=6,fg=None,bg=(45,45,50)):
 tbxf445c=max(0.0,min(1.0,tbxf445c))
 if fg is None:
  fg=rk2u1rsu(tbxf445c)
 v0rxxf36=height//2
 i0x65muf=pygame.Rect(owdz09wf,lb4y4k7b,width,height)
 pygame.draw.rect(u15pdtz9,bg,i0x65muf,border_radius=v0rxxf36)
 if tbxf445c>0:
  x9bp4m18=max(height,int(width*tbxf445c))
  pygame.draw.rect(u15pdtz9,fg,(owdz09wf,lb4y4k7b,x9bp4m18,height),border_radius=v0rxxf36)
 pygame.draw.rect(u15pdtz9,(20,20,20),i0x65muf,width=1,border_radius=v0rxxf36)
