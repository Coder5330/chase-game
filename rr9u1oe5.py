import json
import pickle
import os
from d0qzfhom import ibps3y70
rv86wzs3=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def pq3vli7k(zflv1xxl):
 return os.path.join(rv86wzs3,f'slot_{zflv1xxl}.json')
def qxaprpn6(zflv1xxl):
 return os.path.join(rv86wzs3,f'slot_{zflv1xxl}.pkl')
def j2vmcqbn():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def n04cdpqv(zflv1xxl):
 return os.path.exists(pq3vli7k(zflv1xxl))or os.path.exists(qxaprpn6(zflv1xxl))
def ozp08j3t(zflv1xxl):
 xqzpky32=qxaprpn6(zflv1xxl)
 if not os.path.exists(xqzpky32):
  return None
 try:
  with open(xqzpky32,'rb')as jm25len6:
   return pickle.load(jm25len6)
 except Exception:
  return None
def yjluujmi(zflv1xxl):
 xqzpky32=pq3vli7k(zflv1xxl)
 f8wquuy5=None
 if os.path.exists(xqzpky32):
  try:
   with open(xqzpky32,'r')as jm25len6:
    f8wquuy5=json.load(jm25len6)
  except Exception:
   f8wquuy5=None
 else:
  f8wquuy5=ozp08j3t(zflv1xxl)
 f55dmcxx=j2vmcqbn()
 if f8wquuy5:
  f55dmcxx.update(f8wquuy5)
  nyrid3dn(zflv1xxl,f55dmcxx)
 return f55dmcxx
def nyrid3dn(zflv1xxl,f8wquuy5):
 os.makedirs(rv86wzs3,exist_ok=True)
 with open(pq3vli7k(zflv1xxl),'w')as jm25len6:
  json.dump(f8wquuy5,jm25len6,indent=2)
def ls2zge2j(zflv1xxl):
 if not n04cdpqv(zflv1xxl):
  return None
 f8wquuy5=yjluujmi(zflv1xxl)
 return{'resources':f8wquuy5.get('resources',0),'high_level':f8wquuy5.get('high_level',0),'runs_played':f8wquuy5.get('runs_played',0)}
