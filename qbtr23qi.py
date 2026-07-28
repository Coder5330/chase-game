import json
import pickle
import os
from r1yohmi9 import n2vlpys2
khl1n13j=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def bwiykid9(byl68ntk):
 return os.path.join(khl1n13j,f'slot_{byl68ntk}.json')
def win4olr6(byl68ntk):
 return os.path.join(khl1n13j,f'slot_{byl68ntk}.pkl')
def wehlxslg():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def q3n2qb6g(byl68ntk):
 return os.path.exists(bwiykid9(byl68ntk))or os.path.exists(win4olr6(byl68ntk))
def mnx39rbs(byl68ntk):
 f8rtm4j3=win4olr6(byl68ntk)
 if not os.path.exists(f8rtm4j3):
  return None
 try:
  with open(f8rtm4j3,'rb')as g5l8a78e:
   return pickle.load(g5l8a78e)
 except Exception:
  return None
def sye0a4ab(byl68ntk):
 f8rtm4j3=bwiykid9(byl68ntk)
 mfyb8dal=None
 if os.path.exists(f8rtm4j3):
  try:
   with open(f8rtm4j3,'r')as g5l8a78e:
    mfyb8dal=json.load(g5l8a78e)
  except Exception:
   mfyb8dal=None
 else:
  mfyb8dal=mnx39rbs(byl68ntk)
 q26yg3dx=wehlxslg()
 if mfyb8dal:
  q26yg3dx.update(mfyb8dal)
  wtl0thhz(byl68ntk,q26yg3dx)
 return q26yg3dx
def wtl0thhz(byl68ntk,mfyb8dal):
 os.makedirs(khl1n13j,exist_ok=True)
 with open(bwiykid9(byl68ntk),'w')as g5l8a78e:
  json.dump(mfyb8dal,g5l8a78e,indent=2)
def u15pdtz9(byl68ntk):
 if not q3n2qb6g(byl68ntk):
  return None
 mfyb8dal=sye0a4ab(byl68ntk)
 return{'resources':mfyb8dal.get('resources',0),'high_level':mfyb8dal.get('high_level',0),'runs_played':mfyb8dal.get('runs_played',0)}
