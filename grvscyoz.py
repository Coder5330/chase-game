import os
import pygame
from ykatqyds import ykipu1wy
cq0b8ic8=ykipu1wy('assets/sfx')
lt63j3r3={}
mnx39rbs=True
try:
 pygame.mixer.init()
except pygame.error:
 mnx39rbs=False
def tb4ldims(lgbpj4uf,mytn02yc):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not mnx39rbs:
  return
 eehou6ql=os.path.join(cq0b8ic8,mytn02yc)
 if os.path.exists(eehou6ql):
  try:
   lt63j3r3[lgbpj4uf]=pygame.mixer.Sound(eehou6ql)
  except pygame.error:
   pass
k44nlz15={}
def ytb9xxay(lgbpj4uf,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 ysqg8x80=lt63j3r3.get(lgbpj4uf)
 if ysqg8x80 is None:
  return
 if min_interval_ms>0:
  y8dd2255=pygame.time.get_ticks()
  crsb4gf1=k44nlz15.get(lgbpj4uf,-min_interval_ms)
  if y8dd2255-crsb4gf1<min_interval_ms:
   return
  k44nlz15[lgbpj4uf]=y8dd2255
 ysqg8x80.set_volume(volume)
 ysqg8x80.play()
b18hafey={'zq9bc2':'hit_player.wav','hrctlt':'hit_enemy.wav','be2wnf':'pickup.wav','ua6wix':'level_up.wav','jr87iy':'chest_open.wav','tn1th1':'shoot.wav','oarxab':'explosion.wav'}
for(iy6qktc8,u8c2jwoc)in b18hafey.items():
 tb4ldims(iy6qktc8,u8c2jwoc)
