import os
import pygame
from entfk7or import sv5f1bcp
khl1n13j=sv5f1bcp('assets/sfx')
pa5u6hc3={}
k44nlz15=True
try:
 pygame.mixer.init()
except pygame.error:
 k44nlz15=False
def mcup8ijl(got7txkd,v76ub7l8):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not k44nlz15:
  return
 vt26ys44=os.path.join(khl1n13j,v76ub7l8)
 if os.path.exists(vt26ys44):
  try:
   pa5u6hc3[got7txkd]=pygame.mixer.Sound(vt26ys44)
  except pygame.error:
   pass
jmpioygg={}
def k1taa0i5(got7txkd,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 w0p4e05q=pa5u6hc3.get(got7txkd)
 if w0p4e05q is None:
  return
 if min_interval_ms>0:
  ee1g983e=pygame.time.get_ticks()
  ls2zge2j=jmpioygg.get(got7txkd,-min_interval_ms)
  if ee1g983e-ls2zge2j<min_interval_ms:
   return
  jmpioygg[got7txkd]=ee1g983e
 w0p4e05q.set_volume(volume)
 w0p4e05q.play()
cq0b8ic8={'riny2e':'hit_player.wav','yrp422':'hit_enemy.wav','ua6wix':'pickup.wav','ykht8x':'level_up.wav','pcs4ke':'chest_open.wav','yoztp7':'shoot.wav','en1x2g':'explosion.wav'}
for(j1i2hgj1,yw5py6b2)in cq0b8ic8.items():
 mcup8ijl(j1i2hgj1,yw5py6b2)
