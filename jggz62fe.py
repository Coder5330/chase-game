import os
import pygame
from j1bmqf7z import nrpj1epk
khl1n13j=nrpj1epk('assets/sfx')
wkof8krd={}
bwiykid9=True
try:
 pygame.mixer.init()
except pygame.error:
 bwiykid9=False
def zo3lqi7e(got7txkd,sf337kuu):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not bwiykid9:
  return
 vt26ys44=os.path.join(khl1n13j,sf337kuu)
 if os.path.exists(vt26ys44):
  try:
   wkof8krd[got7txkd]=pygame.mixer.Sound(vt26ys44)
  except pygame.error:
   pass
t5wi6fqj={}
def k1taa0i5(got7txkd,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 sfu38gl2=wkof8krd.get(got7txkd)
 if sfu38gl2 is None:
  return
 if min_interval_ms>0:
  ee1g983e=pygame.time.get_ticks()
  d1b3jczu=t5wi6fqj.get(got7txkd,-min_interval_ms)
  if ee1g983e-d1b3jczu<min_interval_ms:
   return
  t5wi6fqj[got7txkd]=ee1g983e
 sfu38gl2.set_volume(volume)
 sfu38gl2.play()
cq0b8ic8={'ozdcuj':'hit_player.wav','urf1hx':'hit_enemy.wav','hrctlt':'pickup.wav','yrp422':'level_up.wav','ktaq6u':'chest_open.wav','f4c3ev':'shoot.wav','w9laac':'explosion.wav'}
for(yx4w6xlp,jmpioygg)in cq0b8ic8.items():
 zo3lqi7e(yx4w6xlp,jmpioygg)
