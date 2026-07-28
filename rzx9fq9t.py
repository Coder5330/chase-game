import os
import pygame
from zfiblejg import c0hpmnz1
khl1n13j=c0hpmnz1('assets/sfx')
on0jnwny={}
u8c2jwoc=True
try:
 pygame.mixer.init()
except pygame.error:
 u8c2jwoc=False
def qo6q0usw(wb7f6fdh,q7i6yuj7):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not u8c2jwoc:
  return
 no0u93mz=os.path.join(khl1n13j,q7i6yuj7)
 if os.path.exists(no0u93mz):
  try:
   on0jnwny[wb7f6fdh]=pygame.mixer.Sound(no0u93mz)
  except pygame.error:
   pass
yw5py6b2={}
def upprat08(wb7f6fdh,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 sfu38gl2=on0jnwny.get(wb7f6fdh)
 if sfu38gl2 is None:
  return
 if min_interval_ms>0:
  co4busu9=pygame.time.get_ticks()
  jxxgaear=yw5py6b2.get(wb7f6fdh,-min_interval_ms)
  if co4busu9-jxxgaear<min_interval_ms:
   return
  yw5py6b2[wb7f6fdh]=co4busu9
 sfu38gl2.set_volume(volume)
 sfu38gl2.play()
cq0b8ic8={'mjz6us':'hit_player.wav','oarxab':'hit_enemy.wav','bohxs7':'pickup.wav','r7myow':'level_up.wav','t00ucr':'chest_open.wav','voeytl':'shoot.wav','gbwcv6':'explosion.wav'}
for(ia529603,bwiykid9)in cq0b8ic8.items():
 qo6q0usw(ia529603,bwiykid9)
