import os
import pygame
from r1yohmi9 import am2vajep
cq0b8ic8=am2vajep('assets/sfx')
yw5py6b2={}
wkzorqqf=True
try:
 pygame.mixer.init()
except pygame.error:
 wkzorqqf=False
def crsb4gf1(jl90pxrl,eatvzkhi):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not wkzorqqf:
  return
 f8rtm4j3=os.path.join(cq0b8ic8,eatvzkhi)
 if os.path.exists(f8rtm4j3):
  try:
   yw5py6b2[jl90pxrl]=pygame.mixer.Sound(f8rtm4j3)
  except pygame.error:
   pass
eqrl1n75={}
def z3olfark(jl90pxrl,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 cb2uuijn=yw5py6b2.get(jl90pxrl)
 if cb2uuijn is None:
  return
 if min_interval_ms>0:
  oc4kl8cg=pygame.time.get_ticks()
  avfmh07w=eqrl1n75.get(jl90pxrl,-min_interval_ms)
  if oc4kl8cg-avfmh07w<min_interval_ms:
   return
  eqrl1n75[jl90pxrl]=oc4kl8cg
 cb2uuijn.set_volume(volume)
 cb2uuijn.play()
b18hafey={'pgsb98':'hit_player.wav','xfq3jz':'hit_enemy.wav','w9laac':'pickup.wav','bx1ego':'level_up.wav','y3lxch':'chest_open.wav','i1yy1j':'shoot.wav','e0s41k':'explosion.wav'}
for(sld4d6af,zs3kkv9r)in b18hafey.items():
 crsb4gf1(sld4d6af,zs3kkv9r)
