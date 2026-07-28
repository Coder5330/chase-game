import json
import pickle
import os
import hmac
import hashlib
import base64
from ykatqyds import n2vlpys2
khl1n13j=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def reqy08p0(fp47b42g,key):
 return bytes((nrpj1epk^key[nyrid3dn%len(key)]for(nyrid3dn,nrpj1epk)in enumerate(fp47b42g)))
nd96qe3r=b'gr8-annoyance-pass!'
wkzorqqf=bytes.fromhex('29376a5c0214021e20360228047a221010426f152b6f552d212a224c32290f0e4e42113f10130b196b412f253428091b0f325810')
def eqrl1n75():
 qhkc856w=reqy08p0(wkzorqqf,nd96qe3r)
 return base64.b64decode(qhkc856w)
g7s55j2o=eqrl1n75()
def sk8yqk94(fp47b42g):
 return reqy08p0(fp47b42g,g7s55j2o)
def yx4w6xlp(upprat08):
 return hmac.new(g7s55j2o,upprat08,hashlib.sha256).hexdigest()
def sne6loh2(l1rdxck3):
 return os.path.join(khl1n13j,f'slot_{l1rdxck3}.sav')
def bwiykid9(l1rdxck3):
 return os.path.join(khl1n13j,f'slot_{l1rdxck3}.json')
def yw5py6b2(l1rdxck3):
 return os.path.join(khl1n13j,f'slot_{l1rdxck3}.pkl')
def jqxs6esj():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def rh0w064w(l1rdxck3):
 return os.path.exists(sne6loh2(l1rdxck3))or os.path.exists(bwiykid9(l1rdxck3))or os.path.exists(yw5py6b2(l1rdxck3))
def t5wi6fqj(l1rdxck3):
 eehou6ql=bwiykid9(l1rdxck3)
 if os.path.exists(eehou6ql):
  try:
   with open(eehou6ql,'r')as azc4xl99:
    fp47b42g=json.load(azc4xl99)
   if isinstance(fp47b42g,dict):
    return fp47b42g
  except Exception:
   pass
  return None
 eehou6ql=yw5py6b2(l1rdxck3)
 if os.path.exists(eehou6ql):
  try:
   with open(eehou6ql,'rb')as azc4xl99:
    fp47b42g=pickle.load(azc4xl99)
   if isinstance(fp47b42g,dict):
    return fp47b42g
  except Exception:
   pass
  return None
 return None
def jmpioygg(l1rdxck3):
 eehou6ql=sne6loh2(l1rdxck3)
 if not os.path.exists(eehou6ql):
  return None
 try:
  with open(eehou6ql,'r')as azc4xl99:
   yrivh6t1=json.load(azc4xl99)
  upprat08=sk8yqk94(base64.b64decode(yrivh6t1['dzjq7w']))
  if hmac.compare_digest(yx4w6xlp(upprat08),yrivh6t1.get('vhbef4','')):
   fp47b42g=json.loads(upprat08.decode('utf-8'))
   if isinstance(fp47b42g,dict):
    return fp47b42g
 except Exception:
  pass
 return None
def ia529603(l1rdxck3):
 for eehou6ql in(bwiykid9(l1rdxck3),yw5py6b2(l1rdxck3)):
  if os.path.exists(eehou6ql):
   try:
    os.remove(eehou6ql)
   except OSError:
    pass
def vk3g84ut(l1rdxck3):
 try:
  fp47b42g=jmpioygg(l1rdxck3)
  qjcjn997=False
  if fp47b42g is None:
   fp47b42g=t5wi6fqj(l1rdxck3)
   qjcjn997=fp47b42g is not None
  y9ayq6ww=jqxs6esj()
  if fp47b42g:
   y9ayq6ww.update(fp47b42g)
   qcd81twh(l1rdxck3,y9ayq6ww)
   if qjcjn997:
    ia529603(l1rdxck3)
  return y9ayq6ww
 except Exception:
  return jqxs6esj()
def qcd81twh(l1rdxck3,fp47b42g):
 try:
  os.makedirs(khl1n13j,exist_ok=True)
  upprat08=json.dumps(fp47b42g).encode('utf-8')
  yrivh6t1={'dzjq7w':base64.b64encode(sk8yqk94(upprat08)).decode('ascii'),'vhbef4':yx4w6xlp(upprat08)}
  with open(sne6loh2(l1rdxck3),'w')as azc4xl99:
   json.dump(yrivh6t1,azc4xl99)
 except Exception:
  pass
def u1ni10kq(l1rdxck3):
 if not rh0w064w(l1rdxck3):
  return None
 fp47b42g=vk3g84ut(l1rdxck3)
 return{'resources':fp47b42g.get('resources',0),'high_level':fp47b42g.get('high_level',0),'runs_played':fp47b42g.get('runs_played',0)}
