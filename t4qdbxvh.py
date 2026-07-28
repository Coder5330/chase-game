import os
import pygame
from omerbyea import ykipu1wy
cq0b8ic8=ykipu1wy('assets/sfx')
lt63j3r3={}
mnx39rbs=True
try:
 pygame.mixer.init()
except pygame.error:
 mnx39rbs=False
def gqq4d3kz(zorxdtg5,sf337kuu):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not mnx39rbs:
  return
 cqheyto5=os.path.join(cq0b8ic8,sf337kuu)
 if os.path.exists(cqheyto5):
  try:
   lt63j3r3[zorxdtg5]=pygame.mixer.Sound(cqheyto5)
  except pygame.error:
   pass
k44nlz15={}
def xasez2nx(zorxdtg5,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 u1ni10kq=lt63j3r3.get(zorxdtg5)
 if u1ni10kq is None:
  return
 if min_interval_ms>0:
  a2wspofv=pygame.time.get_ticks()
  d1b3jczu=k44nlz15.get(zorxdtg5,-min_interval_ms)
  if a2wspofv-d1b3jczu<min_interval_ms:
   return
  k44nlz15[zorxdtg5]=a2wspofv
 u1ni10kq.set_volume(volume)
 u1ni10kq.play()
b18hafey={'jz6wmd':'hit_player.wav','ykht8x':'hit_enemy.wav','voeytl':'pickup.wav','zq9bc2':'level_up.wav','t7fr91':'chest_open.wav','ujqigy':'shoot.wav','igc9ho':'explosion.wav'}
for(iy6qktc8,u8c2jwoc)in b18hafey.items():
 gqq4d3kz(iy6qktc8,u8c2jwoc)
