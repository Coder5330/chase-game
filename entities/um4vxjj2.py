import pygame
def qc06xq9j(color,gubmc97c):
 return tuple((max(0,min(255,int(wppsfnko*gubmc97c)))for wppsfnko in color[:3]))
def mytn02yc(g5hcbbmh):
 if g5hcbbmh>0.6:
  return(60,200,80)
 if g5hcbbmh>0.3:
  return(230,200,40)
 return(220,60,60)
def qtzk3ny9(gmoft6yr,qxb7gbdg,n01uyzpd,width,g5hcbbmh,height=6,fg=None,bg=(45,45,50)):
 g5hcbbmh=max(0.0,min(1.0,g5hcbbmh))
 if fg is None:
  fg=mytn02yc(g5hcbbmh)
 zflse45b=height//2
 vj8yrddp=pygame.Rect(qxb7gbdg,n01uyzpd,width,height)
 pygame.draw.rect(gmoft6yr,bg,vj8yrddp,border_radius=zflse45b)
 if g5hcbbmh>0:
  mq7nc85e=max(height,int(width*g5hcbbmh))
  pygame.draw.rect(gmoft6yr,fg,(qxb7gbdg,n01uyzpd,mq7nc85e,height),border_radius=zflse45b)
 pygame.draw.rect(gmoft6yr,(20,20,20),vj8yrddp,width=1,border_radius=zflse45b)
