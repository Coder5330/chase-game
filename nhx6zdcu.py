import json
import pickle
import os
from i1arxabo import jsylztgx
ky20479t=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def g7s55j2o(gg7oq2zd):
 return os.path.join(ky20479t,f'slot_{gg7oq2zd}.json')
def t1w1ht7p(gg7oq2zd):
 return os.path.join(ky20479t,f'slot_{gg7oq2zd}.pkl')
def pa8s8hmb():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def nbwye6qv(gg7oq2zd):
 return os.path.exists(g7s55j2o(gg7oq2zd))or os.path.exists(t1w1ht7p(gg7oq2zd))
def wrbw2zla(gg7oq2zd):
 mu4fmpkx=t1w1ht7p(gg7oq2zd)
 if not os.path.exists(mu4fmpkx):
  return None
 try:
  with open(mu4fmpkx,'rb')as mq7nc85e:
   return pickle.load(mq7nc85e)
 except Exception:
  return None
def bokzixza(gg7oq2zd):
 mu4fmpkx=g7s55j2o(gg7oq2zd)
 hfb85p86=None
 if os.path.exists(mu4fmpkx):
  try:
   with open(mu4fmpkx,'r')as mq7nc85e:
    hfb85p86=json.load(mq7nc85e)
  except Exception:
   hfb85p86=None
 else:
  hfb85p86=wrbw2zla(gg7oq2zd)
 hay64yfd=pa8s8hmb()
 if hfb85p86:
  hay64yfd.update(hfb85p86)
  d46aexl6(gg7oq2zd,hay64yfd)
 return hay64yfd
def d46aexl6(gg7oq2zd,hfb85p86):
 os.makedirs(ky20479t,exist_ok=True)
 with open(g7s55j2o(gg7oq2zd),'w')as mq7nc85e:
  json.dump(hfb85p86,mq7nc85e,indent=2)
def q26yg3dx(gg7oq2zd):
 if not nbwye6qv(gg7oq2zd):
  return None
 hfb85p86=bokzixza(gg7oq2zd)
 return{'resources':hfb85p86.get('resources',0),'high_level':hfb85p86.get('high_level',0),'runs_played':hfb85p86.get('runs_played',0)}
