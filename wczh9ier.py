import os
import pygame
from vnbnqbnx import duhxid4n
khl1n13j=duhxid4n('assets/sfx')
sne6loh2={}
win4olr6=True
try:
 pygame.mixer.init()
except pygame.error:
 win4olr6=False
def j1ldqnk2(wy0mahym,fddfgs3j):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not win4olr6:
  return
 uj64qhks=os.path.join(khl1n13j,fddfgs3j)
 if os.path.exists(uj64qhks):
  try:
   sne6loh2[wy0mahym]=pygame.mixer.Sound(uj64qhks)
  except pygame.error:
   pass
u8c2jwoc={}
def ljk4q5v7(wy0mahym,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 xo2t8fy6=sne6loh2.get(wy0mahym)
 if xo2t8fy6 is None:
  return
 if min_interval_ms>0:
  trdhw9re=pygame.time.get_ticks()
  ry181acj=u8c2jwoc.get(wy0mahym,-min_interval_ms)
  if trdhw9re-ry181acj<min_interval_ms:
   return
  u8c2jwoc[wy0mahym]=trdhw9re
 xo2t8fy6.set_volume(volume)
 xo2t8fy6.play()
cq0b8ic8={'onlt8d':'hit_player.wav','mrf5a7':'hit_enemy.wav','i1yy1j':'pickup.wav','v00vhm':'level_up.wav','m44c68':'chest_open.wav','mjz6us':'shoot.wav','fuxk0a':'explosion.wav'}
for(t5wi6fqj,sld4d6af)in cq0b8ic8.items():
 j1ldqnk2(t5wi6fqj,sld4d6af)
