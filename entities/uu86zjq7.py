import pygame
def fd6rupw2(color,jqzpniqf):
 return tuple((max(0,min(255,int(u23y30ys*jqzpniqf)))for u23y30ys in color[:3]))
def cjn2fomd(exvaj2k8):
 if exvaj2k8>0.6:
  return(60,200,80)
 if exvaj2k8>0.3:
  return(230,200,40)
 return(220,60,60)
def eohswq40(tj0nmeoq,htgsiwg0,hhl1737s,width,exvaj2k8,height=6,fg=None,bg=(45,45,50)):
 exvaj2k8=max(0.0,min(1.0,exvaj2k8))
 if fg is None:
  fg=cjn2fomd(exvaj2k8)
 vhxs58yr=height//2
 ykipu1wy=pygame.Rect(htgsiwg0,hhl1737s,width,height)
 pygame.draw.rect(tj0nmeoq,bg,ykipu1wy,border_radius=vhxs58yr)
 if exvaj2k8>0:
  aicvqy5i=max(height,int(width*exvaj2k8))
  pygame.draw.rect(tj0nmeoq,fg,(htgsiwg0,hhl1737s,aicvqy5i,height),border_radius=vhxs58yr)
 pygame.draw.rect(tj0nmeoq,(20,20,20),ykipu1wy,width=1,border_radius=vhxs58yr)
