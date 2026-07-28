import os
import pygame
from z1yhxso7 import lcj883dh
mvxdp5gj=lcj883dh('assets/sfx')
k44nlz15={}
wrbw2zla=True
try:
 pygame.mixer.init()
except pygame.error:
 wrbw2zla=False
def ub68rerv(zsw2292m,kx74d0gj):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not wrbw2zla:
  return
 a2wspofv=os.path.join(mvxdp5gj,kx74d0gj)
 if os.path.exists(a2wspofv):
  try:
   k44nlz15[zsw2292m]=pygame.mixer.Sound(a2wspofv)
  except pygame.error:
   pass
g7s55j2o={}
def g5hcbbmh(zsw2292m,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 f80ebkjf=k44nlz15.get(zsw2292m)
 if f80ebkjf is None:
  return
 if min_interval_ms>0:
  wg25cfzf=pygame.time.get_ticks()
  xk7n8la1=g7s55j2o.get(zsw2292m,-min_interval_ms)
  if wg25cfzf-xk7n8la1<min_interval_ms:
   return
  g7s55j2o[zsw2292m]=wg25cfzf
 f80ebkjf.set_volume(volume)
 f80ebkjf.play()
khl1n13j={'ntxrgn':'hit_player.wav','hpvwzo':'hit_enemy.wav','vcw2lb':'pickup.wav','edxoq2':'level_up.wav','tudttj':'chest_open.wav','ijj0v6':'shoot.wav'}
for(win4olr6,wkzorqqf)in khl1n13j.items():
 ub68rerv(win4olr6,wkzorqqf)
