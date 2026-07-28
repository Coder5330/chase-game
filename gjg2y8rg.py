import json
import pickle
import os
from v7bnhjw6 import my6wktak
mvxdp5gj=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def k44nlz15(stv18kgy):
 return os.path.join(mvxdp5gj,f'slot_{stv18kgy}.json')
def eqrl1n75(stv18kgy):
 return os.path.join(mvxdp5gj,f'slot_{stv18kgy}.pkl')
def yuibrsz1():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def f80ebkjf(stv18kgy):
 return os.path.exists(k44nlz15(stv18kgy))or os.path.exists(eqrl1n75(stv18kgy))
def win4olr6(stv18kgy):
 la3kkrzd=eqrl1n75(stv18kgy)
 if not os.path.exists(la3kkrzd):
  return None
 try:
  with open(la3kkrzd,'rb')as nfn1r4kz:
   return pickle.load(nfn1r4kz)
 except Exception:
  return None
def zflv1xxl(stv18kgy):
 la3kkrzd=k44nlz15(stv18kgy)
 qtzk3ny9=None
 if os.path.exists(la3kkrzd):
  try:
   with open(la3kkrzd,'r')as nfn1r4kz:
    qtzk3ny9=json.load(nfn1r4kz)
  except Exception:
   qtzk3ny9=None
 else:
  qtzk3ny9=win4olr6(stv18kgy)
 ukshy8nb=yuibrsz1()
 if qtzk3ny9:
  ukshy8nb.update(qtzk3ny9)
  wd6r30oj(stv18kgy,ukshy8nb)
 return ukshy8nb
def wd6r30oj(stv18kgy,qtzk3ny9):
 os.makedirs(mvxdp5gj,exist_ok=True)
 with open(k44nlz15(stv18kgy),'w')as nfn1r4kz:
  json.dump(qtzk3ny9,nfn1r4kz,indent=2)
def uwxrum2l(stv18kgy):
 if not f80ebkjf(stv18kgy):
  return None
 qtzk3ny9=zflv1xxl(stv18kgy)
 return{'resources':qtzk3ny9.get('resources',0),'high_level':qtzk3ny9.get('high_level',0),'runs_played':qtzk3ny9.get('runs_played',0)}
