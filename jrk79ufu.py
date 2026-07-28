import os
import pygame
from e87f8tsx import duhxid4n
cq0b8ic8=duhxid4n('assets/sfx')
sne6loh2={}
win4olr6=True
try:
 pygame.mixer.init()
except pygame.error:
 win4olr6=False
def yvffqot8(trdhw9re,v76ub7l8):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not win4olr6:
  return
 ljk4q5v7=os.path.join(cq0b8ic8,v76ub7l8)
 if os.path.exists(ljk4q5v7):
  try:
   sne6loh2[trdhw9re]=pygame.mixer.Sound(ljk4q5v7)
  except pygame.error:
   pass
u8c2jwoc={}
def yg87oi0e(trdhw9re,volume=1.0,min_interval_ms=0):
 """min_interval_ms rate-limits a sound against ITSELF -- e.g. rapid-fire
    weapons or an AoE hitting many enemies at once would otherwise stack the
    same sound into an overlapping wall of noise instead of a single hit."""
 su1hbj6t=sne6loh2.get(trdhw9re)
 if su1hbj6t is None:
  return
 if min_interval_ms>0:
  x6cnoljq=pygame.time.get_ticks()
  ls2zge2j=u8c2jwoc.get(trdhw9re,-min_interval_ms)
  if x6cnoljq-ls2zge2j<min_interval_ms:
   return
  u8c2jwoc[trdhw9re]=x6cnoljq
 su1hbj6t.set_volume(volume)
 su1hbj6t.play()
b18hafey={'r7myow':'hit_player.wav','riny2e':'hit_enemy.wav','agbl2q':'pickup.wav','jz6wmd':'level_up.wav','ijj0v6':'chest_open.wav','be2wnf':'shoot.wav','dzjq7w':'explosion.wav'}
for(t5wi6fqj,sld4d6af)in b18hafey.items():
 yvffqot8(t5wi6fqj,sld4d6af)
