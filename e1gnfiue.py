import json
import pickle
import os
from z4w1arag import jsylztgx
ky20479t=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def sld4d6af(rk43safy):
 return os.path.join(ky20479t,f'slot_{rk43safy}.json')
def g7s55j2o(rk43safy):
 return os.path.join(ky20479t,f'slot_{rk43safy}.pkl')
def elwf90km():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def gj29yfc2(rk43safy):
 return os.path.exists(sld4d6af(rk43safy))or os.path.exists(g7s55j2o(rk43safy))
def zs3kkv9r(rk43safy):
 ncyh3fvl=g7s55j2o(rk43safy)
 if not os.path.exists(ncyh3fvl):
  return None
 try:
  with open(ncyh3fvl,'rb')as xuu13i59:
   return pickle.load(xuu13i59)
 except Exception:
  return None
def ub68rerv(rk43safy):
 ncyh3fvl=sld4d6af(rk43safy)
 do2m71hs=None
 if os.path.exists(ncyh3fvl):
  try:
   with open(ncyh3fvl,'r')as xuu13i59:
    do2m71hs=json.load(xuu13i59)
  except Exception:
   do2m71hs=None
 else:
  do2m71hs=zs3kkv9r(rk43safy)
 xu9ymszd=elwf90km()
 if do2m71hs:
  xu9ymszd.update(do2m71hs)
  pllkstn3(rk43safy,xu9ymszd)
 return xu9ymszd
def pllkstn3(rk43safy,do2m71hs):
 os.makedirs(ky20479t,exist_ok=True)
 with open(sld4d6af(rk43safy),'w')as xuu13i59:
  json.dump(do2m71hs,xuu13i59,indent=2)
def xxns2zyb(rk43safy):
 if not gj29yfc2(rk43safy):
  return None
 do2m71hs=ub68rerv(rk43safy)
 return{'resources':do2m71hs.get('resources',0),'high_level':do2m71hs.get('high_level',0),'runs_played':do2m71hs.get('runs_played',0)}
