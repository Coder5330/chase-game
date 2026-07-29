import os
import pygame
from jggz62fe import vvslh9bh
cq0b8ic8=vvslh9bh('assets/sfx')
reqy08p0={}
yw5py6b2=True
try:
 pygame.mixer.init()
except pygame.error:
 yw5py6b2=False
def yvffqot8(mu4fmpkx,mytn02yc):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not yw5py6b2:
  return
 rgdej31g=os.path.join(cq0b8ic8,mytn02yc)
 if os.path.exists(rgdej31g):
  try:
   reqy08p0[mu4fmpkx]=pygame.mixer.Sound(rgdej31g)
  except pygame.error:
   pass
iy6qktc8={}
def jenvg3kk(mu4fmpkx,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 w0p4e05q=reqy08p0.get(mu4fmpkx)
 if w0p4e05q is None:
  return
 if min_interval_ms>0:
  ncyh3fvl=pygame.time.get_ticks()
  crsb4gf1=iy6qktc8.get(mu4fmpkx,-min_interval_ms)
  if ncyh3fvl-crsb4gf1<min_interval_ms:
   return
  iy6qktc8[mu4fmpkx]=ncyh3fvl
 w0p4e05q.set_volume(volume)
 w0p4e05q.play()
b18hafey={'oarxab':'hit_player.wav','ozdcuj':'hit_enemy.wav','zq9bc2':'pickup.wav','riny2e':'level_up.wav','kp82kb':'chest_open.wav','th2p39':'shoot.wav','nddqhk':'explosion.wav'}
for(sne6loh2,t5wi6fqj)in b18hafey.items():
 yvffqot8(sne6loh2,t5wi6fqj)
