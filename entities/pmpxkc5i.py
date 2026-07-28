import pygame
def y9ayq6ww(color,azc4xl99):
 return tuple((max(0,min(255,int(uos0fb4y*azc4xl99)))for uos0fb4y in color[:3]))
def arhnuxor(myrp5ge0):
 if myrp5ge0>0.6:
  return(60,200,80)
 if myrp5ge0>0.3:
  return(230,200,40)
 return(220,60,60)
def vhuds3qs(h8s2ftom,w2sq3b9s,owdz09wf,width,myrp5ge0,height=6,fg=None,bg=(45,45,50)):
 myrp5ge0=max(0.0,min(1.0,myrp5ge0))
 if fg is None:
  fg=arhnuxor(myrp5ge0)
 tj0nmeoq=height//2
 uysal8m1=pygame.Rect(w2sq3b9s,owdz09wf,width,height)
 pygame.draw.rect(h8s2ftom,bg,uysal8m1,border_radius=tj0nmeoq)
 if myrp5ge0>0:
  sf337kuu=max(height,int(width*myrp5ge0))
  pygame.draw.rect(h8s2ftom,fg,(w2sq3b9s,owdz09wf,sf337kuu,height),border_radius=tj0nmeoq)
 pygame.draw.rect(h8s2ftom,(20,20,20),uysal8m1,width=1,border_radius=tj0nmeoq)
