import pygame
def no0u93mz(zfb7r31q,uc1xi04b):
 return tuple((max(0,min(255,int(fcwtg1m8*uc1xi04b)))for fcwtg1m8 in zfb7r31q[:3]))
def xq46nouh(wb7f6fdh):
 if wb7f6fdh>0.6:
  return(60,200,80)
 if wb7f6fdh>0.3:
  return(230,200,40)
 return(220,60,60)
def l9enulqj(uz6kf162,kn5gjj8m,lu7jae58,width,wb7f6fdh,height=6,fg=None,bg=(45,45,50)):
 wb7f6fdh=max(0.0,min(1.0,wb7f6fdh))
 if fg is None:
  fg=xq46nouh(wb7f6fdh)
 mfc79m96=height//2
 am2vajep=pygame.Rect(kn5gjj8m,lu7jae58,width,height)
 pygame.draw.rect(uz6kf162,bg,am2vajep,border_radius=mfc79m96)
 if wb7f6fdh>0:
  x875aud9=max(height,int(width*wb7f6fdh))
  pygame.draw.rect(uz6kf162,fg,(kn5gjj8m,lu7jae58,x875aud9,height),border_radius=mfc79m96)
 pygame.draw.rect(uz6kf162,(20,20,20),am2vajep,width=1,border_radius=mfc79m96)
