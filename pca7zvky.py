import json
import pickle
import os
from z1yhxso7 import jsylztgx
ky20479t=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def u8c2jwoc(g1b3d505):
 return os.path.join(ky20479t,f'slot_{g1b3d505}.json')
def zs3kkv9r(g1b3d505):
 return os.path.join(ky20479t,f'slot_{g1b3d505}.pkl')
def qtzk3ny9():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def xxns2zyb(g1b3d505):
 return os.path.exists(u8c2jwoc(g1b3d505))or os.path.exists(zs3kkv9r(g1b3d505))
def eqrl1n75(g1b3d505):
 a2wspofv=zs3kkv9r(g1b3d505)
 if not os.path.exists(a2wspofv):
  return None
 try:
  with open(a2wspofv,'rb')as qhkc856w:
   return pickle.load(qhkc856w)
 except Exception:
  return None
def q5amln4p(g1b3d505):
 a2wspofv=u8c2jwoc(g1b3d505)
 qbbz2sf6=None
 if os.path.exists(a2wspofv):
  try:
   with open(a2wspofv,'r')as qhkc856w:
    qbbz2sf6=json.load(qhkc856w)
  except Exception:
   qbbz2sf6=None
 else:
  qbbz2sf6=eqrl1n75(g1b3d505)
 tbxf445c=qtzk3ny9()
 if qbbz2sf6:
  tbxf445c.update(qbbz2sf6)
  uaobt328(g1b3d505,tbxf445c)
 return tbxf445c
def uaobt328(g1b3d505,qbbz2sf6):
 os.makedirs(ky20479t,exist_ok=True)
 with open(u8c2jwoc(g1b3d505),'w')as qhkc856w:
  json.dump(qbbz2sf6,qhkc856w,indent=2)
def t54piwzn(g1b3d505):
 if not xxns2zyb(g1b3d505):
  return None
 qbbz2sf6=q5amln4p(g1b3d505)
 return{'resources':qbbz2sf6.get('resources',0),'high_level':qbbz2sf6.get('high_level',0),'runs_played':qbbz2sf6.get('runs_played',0)}
