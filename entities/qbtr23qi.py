import pygame
def mn89ltaj(color,tw76xato):
 return tuple((max(0,min(255,int(jm25len6*tw76xato)))for jm25len6 in color[:3]))
def gqj5sxvw(gmoft6yr):
 if gmoft6yr>0.6:
  return(60,200,80)
 if gmoft6yr>0.3:
  return(230,200,40)
 return(220,60,60)
def velos6zl(g1b3d505,iimoe0sy,gdg1wjui,width,gmoft6yr,height=6,fg=None,bg=(45,45,50)):
 gmoft6yr=max(0.0,min(1.0,gmoft6yr))
 if fg is None:
  fg=gqj5sxvw(gmoft6yr)
 xwk2rv23=height//2
 wppsfnko=pygame.Rect(iimoe0sy,gdg1wjui,width,height)
 pygame.draw.rect(g1b3d505,bg,wppsfnko,border_radius=xwk2rv23)
 if gmoft6yr>0:
  mc8qizk3=max(height,int(width*gmoft6yr))
  pygame.draw.rect(g1b3d505,fg,(iimoe0sy,gdg1wjui,mc8qizk3,height),border_radius=xwk2rv23)
 pygame.draw.rect(g1b3d505,(20,20,20),wppsfnko,width=1,border_radius=xwk2rv23)
