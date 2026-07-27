import json
import pickle
import os
from en1x2gdg import jsylztgx
rcfnfhol=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def t1w1ht7p(uaobt328):
 return os.path.join(rcfnfhol,f'slot_{uaobt328}.json')
def ygspk9p3(uaobt328):
 return os.path.join(rcfnfhol,f'slot_{uaobt328}.pkl')
def bfoqmf5l():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def ukshy8nb(uaobt328):
 return os.path.exists(t1w1ht7p(uaobt328))or os.path.exists(ygspk9p3(uaobt328))
def cqoldfor(uaobt328):
 oc4kl8cg=ygspk9p3(uaobt328)
 if not os.path.exists(oc4kl8cg):
  return None
 try:
  with open(oc4kl8cg,'rb')as vhuds3qs:
   return pickle.load(vhuds3qs)
 except Exception:
  return None
def n3rlkte4(uaobt328):
 oc4kl8cg=t1w1ht7p(uaobt328)
 u1jhuwb6=None
 if os.path.exists(oc4kl8cg):
  try:
   with open(oc4kl8cg,'r')as vhuds3qs:
    u1jhuwb6=json.load(vhuds3qs)
  except Exception:
   u1jhuwb6=None
 else:
  u1jhuwb6=cqoldfor(uaobt328)
 ytb9xxay=bfoqmf5l()
 if u1jhuwb6:
  ytb9xxay.update(u1jhuwb6)
  xwk2rv23(uaobt328,ytb9xxay)
 return ytb9xxay
def xwk2rv23(uaobt328,u1jhuwb6):
 os.makedirs(rcfnfhol,exist_ok=True)
 with open(t1w1ht7p(uaobt328),'w')as vhuds3qs:
  json.dump(u1jhuwb6,vhuds3qs,indent=2)
def d1hm38ks(uaobt328):
 if not ukshy8nb(uaobt328):
  return None
 u1jhuwb6=n3rlkte4(uaobt328)
 return{'resources':u1jhuwb6.get('resources',0),'high_level':u1jhuwb6.get('high_level',0),'runs_played':u1jhuwb6.get('runs_played',0)}
