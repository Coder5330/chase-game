import os
import pygame
from v7bnhjw6 import uva2ieuc
khl1n13j=uva2ieuc('assets/sfx')
bwiykid9={}
nd96qe3r=True
try:
 pygame.mixer.init()
except pygame.error:
 nd96qe3r=False
def mctwjlsh(hu9n79gi,g5l8a78e):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not nd96qe3r:
  return
 la3kkrzd=os.path.join(khl1n13j,g5l8a78e)
 if os.path.exists(la3kkrzd):
  try:
   bwiykid9[hu9n79gi]=pygame.mixer.Sound(la3kkrzd)
  except pygame.error:
   pass
zs3kkv9r={}
def vhxs58yr(hu9n79gi,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 gxlk8wru=bwiykid9.get(hu9n79gi)
 if gxlk8wru is None:
  return
 if min_interval_ms>0:
  j0kgazu4=pygame.time.get_ticks()
  fpa8hyex=zs3kkv9r.get(hu9n79gi,-min_interval_ms)
  if j0kgazu4-fpa8hyex<min_interval_ms:
   return
  zs3kkv9r[hu9n79gi]=j0kgazu4
 gxlk8wru.set_volume(volume)
 gxlk8wru.play()
cq0b8ic8={'hzj7ub':'hit_player.wav','mmgvu4':'hit_enemy.wav','ijj0v6':'pickup.wav','qc6dr0':'level_up.wav','v3c71u':'chest_open.wav','jr87iy':'shoot.wav','w9mda9':'explosion.wav'}
for(mnx39rbs,g7s55j2o)in cq0b8ic8.items():
 mctwjlsh(mnx39rbs,g7s55j2o)
