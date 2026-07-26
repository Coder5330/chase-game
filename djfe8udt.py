import json
import pickle
import os
from rlfzkicw import gncxll4z
yswjckjl=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def rrcbpljd(jenvg3kk):
 return os.path.join(yswjckjl,f'slot_{jenvg3kk}.json')
def ocij2v2h(jenvg3kk):
 return os.path.join(yswjckjl,f'slot_{jenvg3kk}.pkl')
def ruq9e5co():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def xsspye9r(jenvg3kk):
 return os.path.exists(rrcbpljd(jenvg3kk))or os.path.exists(ocij2v2h(jenvg3kk))
def dtx63cfl(jenvg3kk):
 jr5rdnpx=ocij2v2h(jenvg3kk)
 if not os.path.exists(jr5rdnpx):
  return None
 try:
  with open(jr5rdnpx,'rb')as uidlrye8:
   return pickle.load(uidlrye8)
 except Exception:
  return None
def gkz2u2tn(jenvg3kk):
 jr5rdnpx=rrcbpljd(jenvg3kk)
 lztkkfzz=None
 if os.path.exists(jr5rdnpx):
  try:
   with open(jr5rdnpx,'r')as uidlrye8:
    lztkkfzz=json.load(uidlrye8)
  except Exception:
   lztkkfzz=None
 else:
  lztkkfzz=dtx63cfl(jenvg3kk)
 cknfu84x=ruq9e5co()
 if lztkkfzz:
  cknfu84x.update(lztkkfzz)
  uj64qhks(jenvg3kk,cknfu84x)
 return cknfu84x
def uj64qhks(jenvg3kk,lztkkfzz):
 os.makedirs(yswjckjl,exist_ok=True)
 with open(rrcbpljd(jenvg3kk),'w')as uidlrye8:
  json.dump(lztkkfzz,uidlrye8,indent=2)
def xasez2nx(jenvg3kk):
 if not xsspye9r(jenvg3kk):
  return None
 lztkkfzz=gkz2u2tn(jenvg3kk)
 return{'resources':lztkkfzz.get('resources',0),'high_level':lztkkfzz.get('high_level',0),'runs_played':lztkkfzz.get('runs_played',0)}
