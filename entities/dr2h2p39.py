import pygame
def d1hm38ks(color,nfn1r4kz):
 return tuple((max(0,min(255,int(f32ejx5t*nfn1r4kz)))for f32ejx5t in color[:3]))
def kkzruin3(cqheyto5):
 if cqheyto5>0.6:
  return(60,200,80)
 if cqheyto5>0.3:
  return(230,200,40)
 return(220,60,60)
def rzewviyt(ukshy8nb,jslulzfy,zpfb3hn1,width,cqheyto5,height=6,fg=None,bg=(45,45,50)):
 cqheyto5=max(0.0,min(1.0,cqheyto5))
 if fg is None:
  fg=kkzruin3(cqheyto5)
 ljk4q5v7=height//2
 g11kerpe=pygame.Rect(jslulzfy,zpfb3hn1,width,height)
 pygame.draw.rect(ukshy8nb,bg,g11kerpe,border_radius=ljk4q5v7)
 if cqheyto5>0:
  vvbc2vyh=max(height,int(width*cqheyto5))
  pygame.draw.rect(ukshy8nb,fg,(jslulzfy,zpfb3hn1,vvbc2vyh,height),border_radius=ljk4q5v7)
 pygame.draw.rect(ukshy8nb,(20,20,20),g11kerpe,width=1,border_radius=ljk4q5v7)
