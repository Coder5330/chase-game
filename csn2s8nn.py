import json
import pickle
import os
from ygm55ff1 import n2vlpys2
oohp6vz4=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def azebbk7w(upprat08):
 return os.path.join(oohp6vz4,f'slot_{upprat08}.json')
def gl08yg0j(upprat08):
 return os.path.join(oohp6vz4,f'slot_{upprat08}.pkl')
def ugez7bh2():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def k1taa0i5(upprat08):
 return os.path.exists(azebbk7w(upprat08))or os.path.exists(gl08yg0j(upprat08))
def s9skdgig(upprat08):
 dq2fa39e=gl08yg0j(upprat08)
 if not os.path.exists(dq2fa39e):
  return None
 try:
  with open(dq2fa39e,'rb')as eohswq40:
   return pickle.load(eohswq40)
 except Exception:
  return None
def ftlpq2wg(upprat08):
 dq2fa39e=azebbk7w(upprat08)
 amcixdu1=None
 if os.path.exists(dq2fa39e):
  try:
   with open(dq2fa39e,'r')as eohswq40:
    amcixdu1=json.load(eohswq40)
  except Exception:
   amcixdu1=None
 else:
  amcixdu1=s9skdgig(upprat08)
 f8rtm4j3=ugez7bh2()
 if amcixdu1:
  f8rtm4j3.update(amcixdu1)
  exvaj2k8(upprat08,f8rtm4j3)
 return f8rtm4j3
def exvaj2k8(upprat08,amcixdu1):
 os.makedirs(oohp6vz4,exist_ok=True)
 with open(azebbk7w(upprat08),'w')as eohswq40:
  json.dump(amcixdu1,eohswq40,indent=2)
def xsspye9r(upprat08):
 if not k1taa0i5(upprat08):
  return None
 amcixdu1=ftlpq2wg(upprat08)
 return{'resources':amcixdu1.get('resources',0),'high_level':amcixdu1.get('high_level',0),'runs_played':amcixdu1.get('runs_played',0)}
