import json
import pickle
import os
from c8v341on import jsylztgx
rcfnfhol=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def m53a5qbs(npcxa5s0):
 return os.path.join(rcfnfhol,f'slot_{npcxa5s0}.json')
def v4u89yjb(npcxa5s0):
 return os.path.join(rcfnfhol,f'slot_{npcxa5s0}.pkl')
def vw6m7b5c():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def xu9ymszd(npcxa5s0):
 return os.path.exists(m53a5qbs(npcxa5s0))or os.path.exists(v4u89yjb(npcxa5s0))
def ygspk9p3(npcxa5s0):
 y8bv78hu=v4u89yjb(npcxa5s0)
 if not os.path.exists(y8bv78hu):
  return None
 try:
  with open(y8bv78hu,'rb')as tnz61231:
   return pickle.load(tnz61231)
 except Exception:
  return None
def v3e1ocjx(npcxa5s0):
 y8bv78hu=m53a5qbs(npcxa5s0)
 wi8skch8=None
 if os.path.exists(y8bv78hu):
  try:
   with open(y8bv78hu,'r')as tnz61231:
    wi8skch8=json.load(tnz61231)
  except Exception:
   wi8skch8=None
 else:
  wi8skch8=ygspk9p3(npcxa5s0)
 upprat08=vw6m7b5c()
 if wi8skch8:
  upprat08.update(wi8skch8)
  xsspye9r(npcxa5s0,upprat08)
 return upprat08
def xsspye9r(npcxa5s0,wi8skch8):
 os.makedirs(rcfnfhol,exist_ok=True)
 with open(m53a5qbs(npcxa5s0),'w')as tnz61231:
  json.dump(wi8skch8,tnz61231,indent=2)
def tbxf445c(npcxa5s0):
 if not xu9ymszd(npcxa5s0):
  return None
 wi8skch8=v3e1ocjx(npcxa5s0)
 return{'resources':wi8skch8.get('resources',0),'high_level':wi8skch8.get('high_level',0),'runs_played':wi8skch8.get('runs_played',0)}
