import json
import pickle
import os
from rlfzkicw import gncxll4z
yswjckjl=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def rrcbpljd(yg87oi0e):
 return os.path.join(yswjckjl,f'slot_{yg87oi0e}.json')
def ocij2v2h(yg87oi0e):
 return os.path.join(yswjckjl,f'slot_{yg87oi0e}.pkl')
def ruq9e5co():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def xasez2nx(yg87oi0e):
 return os.path.exists(rrcbpljd(yg87oi0e))or os.path.exists(ocij2v2h(yg87oi0e))
def dtx63cfl(yg87oi0e):
 r2muljav=ocij2v2h(yg87oi0e)
 if not os.path.exists(r2muljav):
  return None
 try:
  with open(r2muljav,'rb')as uidlrye8:
   return pickle.load(uidlrye8)
 except Exception:
  return None
def semqgy27(yg87oi0e):
 r2muljav=rrcbpljd(yg87oi0e)
 lztkkfzz=None
 if os.path.exists(r2muljav):
  try:
   with open(r2muljav,'r')as uidlrye8:
    lztkkfzz=json.load(uidlrye8)
  except Exception:
   lztkkfzz=None
 else:
  lztkkfzz=dtx63cfl(yg87oi0e)
 exvaj2k8=ruq9e5co()
 if lztkkfzz:
  exvaj2k8.update(lztkkfzz)
  tkyrmjlj(yg87oi0e,exvaj2k8)
 return exvaj2k8
def tkyrmjlj(yg87oi0e,lztkkfzz):
 os.makedirs(yswjckjl,exist_ok=True)
 with open(rrcbpljd(yg87oi0e),'w')as uidlrye8:
  json.dump(lztkkfzz,uidlrye8,indent=2)
def npejzhya(yg87oi0e):
 if not xasez2nx(yg87oi0e):
  return None
 lztkkfzz=semqgy27(yg87oi0e)
 return{'resources':lztkkfzz.get('resources',0),'high_level':lztkkfzz.get('high_level',0),'runs_played':lztkkfzz.get('runs_played',0)}
