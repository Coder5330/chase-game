import json
import pickle
import os
import sys
import hmac
import hashlib
import base64
from j1bmqf7z import n2vlpys2,jsylztgx
if getattr(sys,'frozen',False):
 win4olr6=os.path.dirname(sys.executable)
else:
 win4olr6=os.path.dirname(os.path.abspath(__file__))
mvxdp5gj=os.path.join(win4olr6,'saves')
g7s55j2o=1000000
wkzorqqf=1000
zs3kkv9r=100000
def j1i2hgj1(fp47b42g):
 if not isinstance(fp47b42g,dict):
  return False
 d1hm38ks=fp47b42g.get('resources',0)
 if isinstance(d1hm38ks,bool)or not isinstance(d1hm38ks,(int,float)):
  return False
 if not 0<=d1hm38ks<=g7s55j2o:
  return False
 i13n3bzt=fp47b42g.get('high_level',0)
 if isinstance(i13n3bzt,bool)or not isinstance(i13n3bzt,(int,float)):
  return False
 if not 0<=i13n3bzt<=wkzorqqf:
  return False
 xxns2zyb=fp47b42g.get('runs_played',0)
 if isinstance(xxns2zyb,bool)or not isinstance(xxns2zyb,(int,float)):
  return False
 if not 0<=xxns2zyb<=zs3kkv9r:
  return False
 meta_upgrades=fp47b42g.get('meta_upgrades',{})
 if not isinstance(meta_upgrades,dict):
  return False
 for(key,tb4ldims)in meta_upgrades.items():
  k2ixivzk=jsylztgx.get(key)
  if k2ixivzk is None:
   return False
  if isinstance(tb4ldims,bool)or not isinstance(tb4ldims,(int,float)):
   return False
  if not 0<=tb4ldims<=k2ixivzk['udt8cq']:
   return False
 return True
def ytv3i12v(fp47b42g,key):
 return bytes((mal2w37d^key[nyrid3dn%len(key)]for(nyrid3dn,mal2w37d)in enumerate(fp47b42g)))
nd96qe3r=b'gr8-annoyance-pass!'
eqrl1n75=bytes.fromhex('29376a5c0214021e20360228047a221010426f152b6f552d212a224c32290f0e4e42113f10130b196b412f253428091b0f325810')
def u8c2jwoc():
 qhkc856w=ytv3i12v(eqrl1n75,nd96qe3r)
 return base64.b64decode(qhkc856w)
mnx39rbs=u8c2jwoc()
def sne6loh2(fp47b42g):
 return ytv3i12v(fp47b42g,mnx39rbs)
def on0jnwny(ljk4q5v7):
 return hmac.new(mnx39rbs,ljk4q5v7,hashlib.sha256).hexdigest()
def pa5u6hc3(svt8k06m):
 return os.path.join(mvxdp5gj,f'slot_{svt8k06m}.sav')
def iy6qktc8(svt8k06m):
 return os.path.join(mvxdp5gj,f'slot_{svt8k06m}.json')
def sk8yqk94(svt8k06m):
 return os.path.join(mvxdp5gj,f'slot_{svt8k06m}.pkl')
def jqxs6esj():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def n64fgwje(svt8k06m):
 return os.path.exists(pa5u6hc3(svt8k06m))or os.path.exists(iy6qktc8(svt8k06m))or os.path.exists(sk8yqk94(svt8k06m))
def ia529603(svt8k06m):
 vt26ys44=iy6qktc8(svt8k06m)
 if os.path.exists(vt26ys44):
  try:
   with open(vt26ys44,'r')as cx41dntc:
    fp47b42g=json.load(cx41dntc)
   if isinstance(fp47b42g,dict):
    return fp47b42g
  except Exception:
   pass
  return None
 vt26ys44=sk8yqk94(svt8k06m)
 if os.path.exists(vt26ys44):
  try:
   with open(vt26ys44,'rb')as cx41dntc:
    fp47b42g=pickle.load(cx41dntc)
   if isinstance(fp47b42g,dict):
    return fp47b42g
  except Exception:
   pass
  return None
 return None
def diuu9k9x(svt8k06m):
 vt26ys44=pa5u6hc3(svt8k06m)
 if not os.path.exists(vt26ys44):
  return None
 try:
  with open(vt26ys44,'r')as cx41dntc:
   g5l8a78e=json.load(cx41dntc)
  ljk4q5v7=sne6loh2(base64.b64decode(g5l8a78e['jr87iy']))
  if hmac.compare_digest(on0jnwny(ljk4q5v7),g5l8a78e.get('th2p39','')):
   fp47b42g=json.loads(ljk4q5v7.decode('utf-8'))
   if isinstance(fp47b42g,dict):
    return fp47b42g
 except Exception:
  pass
 return None
def x52qc1iy(svt8k06m):
 for vt26ys44 in(iy6qktc8(svt8k06m),sk8yqk94(svt8k06m)):
  if os.path.exists(vt26ys44):
   try:
    os.remove(vt26ys44)
   except OSError:
    pass
def yvffqot8(svt8k06m):
 try:
  fp47b42g=diuu9k9x(svt8k06m)
  w2kql0ht=False
  if fp47b42g is None:
   fp47b42g=ia529603(svt8k06m)
   w2kql0ht=fp47b42g is not None
  if fp47b42g is not None and(not j1i2hgj1(fp47b42g)):
   fp47b42g=None
  stv18kgy=jqxs6esj()
  if fp47b42g:
   stv18kgy.update(fp47b42g)
   uwxrum2l(svt8k06m,stv18kgy)
   if w2kql0ht:
    x52qc1iy(svt8k06m)
  return stv18kgy
 except Exception:
  return jqxs6esj()
def uwxrum2l(svt8k06m,fp47b42g):
 try:
  os.makedirs(mvxdp5gj,exist_ok=True)
  ljk4q5v7=json.dumps(fp47b42g).encode('utf-8')
  g5l8a78e={'jr87iy':base64.b64encode(sne6loh2(ljk4q5v7)).decode('ascii'),'th2p39':on0jnwny(ljk4q5v7)}
  with open(pa5u6hc3(svt8k06m),'w')as cx41dntc:
   json.dump(g5l8a78e,cx41dntc)
 except Exception:
  pass
def jyjhu8my(svt8k06m):
 if not n64fgwje(svt8k06m):
  return None
 fp47b42g=yvffqot8(svt8k06m)
 return{'resources':fp47b42g.get('resources',0),'high_level':fp47b42g.get('high_level',0),'runs_played':fp47b42g.get('runs_played',0)}
