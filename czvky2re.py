import os
import pygame
from z4w1arag import gp84dyt9
mvxdp5gj=gp84dyt9('assets/sfx')
u8c2jwoc={}
wrbw2zla=True
try:
 pygame.mixer.init()
except pygame.error:
 wrbw2zla=False
def wa45hvgo(jr5rdnpx,zqcootnj):
 """Load a sound if its file exists; silently does nothing otherwise, so
    the game runs fine with zero sound files and gains sound automatically
    the moment a matching file is dropped into assets/sfx/."""
 if not wrbw2zla:
  return
 ncyh3fvl=os.path.join(mvxdp5gj,zqcootnj)
 if os.path.exists(ncyh3fvl):
  try:
   u8c2jwoc[jr5rdnpx]=pygame.mixer.Sound(ncyh3fvl)
  except pygame.error:
   pass
def gp6orsnc(jr5rdnpx,qxb7gbdg=1.0):
 t54piwzn=u8c2jwoc.get(jr5rdnpx)
 if t54piwzn is None:
  return
 t54piwzn.set_volume(qxb7gbdg)
 t54piwzn.play()
khl1n13j={'az3m55':'hit_player.wav','m44c68':'hit_enemy.wav','e0s41k':'pickup.wav','l4f9ye':'level_up.wav','yl6lgj':'chest_open.wav','fuxk0a':'shoot.wav'}
for(eqrl1n75,wkzorqqf)in khl1n13j.items():
 wa45hvgo(eqrl1n75,wkzorqqf)
