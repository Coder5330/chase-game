import pygame
def uz6kf162(zfb7r31q,uc1xi04b):
 return tuple((max(0,min(255,int(fcwtg1m8*uc1xi04b)))for fcwtg1m8 in zfb7r31q[:3]))
def xq46nouh(oc4kl8cg):
 if oc4kl8cg>0.6:
  return(60,200,80)
 if oc4kl8cg>0.3:
  return(230,200,40)
 return(220,60,60)
def l9enulqj(todsx4nx,kn5gjj8m,lu7jae58,width,oc4kl8cg,height=6,fg=None,bg=(45,45,50)):
 oc4kl8cg=max(0.0,min(1.0,oc4kl8cg))
 if fg is None:
  fg=xq46nouh(oc4kl8cg)
 mmn32u1i=height//2
 am2vajep=pygame.Rect(kn5gjj8m,lu7jae58,width,height)
 pygame.draw.rect(todsx4nx,bg,am2vajep,border_radius=mmn32u1i)
 if oc4kl8cg>0:
  x875aud9=max(height,int(width*oc4kl8cg))
  pygame.draw.rect(todsx4nx,fg,(kn5gjj8m,lu7jae58,x875aud9,height),border_radius=mmn32u1i)
 pygame.draw.rect(todsx4nx,(20,20,20),am2vajep,width=1,border_radius=mmn32u1i)
