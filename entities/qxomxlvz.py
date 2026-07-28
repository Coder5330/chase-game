import pygame
def qcd81twh(color,azc4xl99):
 return tuple((max(0,min(255,int(xp8mgyn2*azc4xl99)))for xp8mgyn2 in color[:3]))
def arhnuxor(xu9ymszd):
 if xu9ymszd>0.6:
  return(60,200,80)
 if xu9ymszd>0.3:
  return(230,200,40)
 return(220,60,60)
def b36htf4p(byl68ntk,j1kfk7y6,f1bl08kg,width,xu9ymszd,height=6,fg=None,bg=(45,45,50)):
 xu9ymszd=max(0.0,min(1.0,xu9ymszd))
 if fg is None:
  fg=arhnuxor(xu9ymszd)
 npcxa5s0=height//2
 kybwmlun=pygame.Rect(j1kfk7y6,f1bl08kg,width,height)
 pygame.draw.rect(byl68ntk,bg,kybwmlun,border_radius=npcxa5s0)
 if xu9ymszd>0:
  sf337kuu=max(height,int(width*xu9ymszd))
  pygame.draw.rect(byl68ntk,fg,(j1kfk7y6,f1bl08kg,sf337kuu,height),border_radius=npcxa5s0)
 pygame.draw.rect(byl68ntk,(20,20,20),kybwmlun,width=1,border_radius=npcxa5s0)
