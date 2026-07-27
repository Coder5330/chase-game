import json
import pickle
import os
from o100vhmy import jsylztgx
rcfnfhol=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def t1w1ht7p(tbxf445c):
 return os.path.join(rcfnfhol,f'slot_{tbxf445c}.json')
def ygspk9p3(tbxf445c):
 return os.path.join(rcfnfhol,f'slot_{tbxf445c}.pkl')
def u1jhuwb6():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def pllkstn3(tbxf445c):
 return os.path.exists(t1w1ht7p(tbxf445c))or os.path.exists(ygspk9p3(tbxf445c))
def cqoldfor(tbxf445c):
 zdan085r=ygspk9p3(tbxf445c)
 if not os.path.exists(zdan085r):
  return None
 try:
  with open(zdan085r,'rb')as v15cqzcu:
   return pickle.load(v15cqzcu)
 except Exception:
  return None
def xk7n8la1(tbxf445c):
 zdan085r=t1w1ht7p(tbxf445c)
 iektsg7f=None
 if os.path.exists(zdan085r):
  try:
   with open(zdan085r,'r')as v15cqzcu:
    iektsg7f=json.load(v15cqzcu)
  except Exception:
   iektsg7f=None
 else:
  iektsg7f=cqoldfor(tbxf445c)
 xsspye9r=u1jhuwb6()
 if iektsg7f:
  xsspye9r.update(iektsg7f)
  ytb9xxay(tbxf445c,xsspye9r)
 return xsspye9r
def ytb9xxay(tbxf445c,iektsg7f):
 os.makedirs(rcfnfhol,exist_ok=True)
 with open(t1w1ht7p(tbxf445c),'w')as v15cqzcu:
  json.dump(iektsg7f,v15cqzcu,indent=2)
def uaobt328(tbxf445c):
 if not pllkstn3(tbxf445c):
  return None
 iektsg7f=xk7n8la1(tbxf445c)
 return{'resources':iektsg7f.get('resources',0),'high_level':iektsg7f.get('high_level',0),'runs_played':iektsg7f.get('runs_played',0)}
