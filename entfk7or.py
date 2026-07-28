import json
import pickle
import os
import hmac
import hashlib
import base64
from e87f8tsx import n2vlpys2
khl1n13j=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def wkof8krd(fo75rh8l,key):
 return bytes((sv5f1bcp^key[bokzixza%len(key)]for(bokzixza,sv5f1bcp)in enumerate(fo75rh8l)))
wrbw2zla=b'gr8-annoyance-pass!'
nd96qe3r=bytes.fromhex('29376a5c0214021e20360228047a221010426f152b6f552d212a224c32290f0e4e42113f10130b196b412f253428091b0f325810')
def zs3kkv9r():
 boih5csk=wkof8krd(nd96qe3r,wrbw2zla)
 return base64.b64decode(boih5csk)
wkzorqqf=zs3kkv9r()
def iy6qktc8(fo75rh8l):
 return wkof8krd(fo75rh8l,wkzorqqf)
def j1i2hgj1(wgcl9lcq):
 return hmac.new(wkzorqqf,wgcl9lcq,hashlib.sha256).hexdigest()
def yx4w6xlp(hdw6lqwl):
 return os.path.join(khl1n13j,f'slot_{hdw6lqwl}.sav')
def k44nlz15(hdw6lqwl):
 return os.path.join(khl1n13j,f'slot_{hdw6lqwl}.json')
def bwiykid9(hdw6lqwl):
 return os.path.join(khl1n13j,f'slot_{hdw6lqwl}.pkl')
def fp47b42g():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def sfu38gl2(hdw6lqwl):
 return os.path.exists(yx4w6xlp(hdw6lqwl))or os.path.exists(k44nlz15(hdw6lqwl))or os.path.exists(bwiykid9(hdw6lqwl))
def jmpioygg(hdw6lqwl):
 ljk4q5v7=k44nlz15(hdw6lqwl)
 if os.path.exists(ljk4q5v7):
  try:
   with open(ljk4q5v7,'r')as mc8qizk3:
    return json.load(mc8qizk3)
  except Exception:
   return None
 ljk4q5v7=bwiykid9(hdw6lqwl)
 if os.path.exists(ljk4q5v7):
  try:
   with open(ljk4q5v7,'rb')as mc8qizk3:
    return pickle.load(mc8qizk3)
  except Exception:
   return None
 return None
def yw5py6b2(hdw6lqwl):
 ljk4q5v7=yx4w6xlp(hdw6lqwl)
 if not os.path.exists(ljk4q5v7):
  return None
 try:
  with open(ljk4q5v7,'r')as mc8qizk3:
   vvbc2vyh=json.load(mc8qizk3)
  wgcl9lcq=iy6qktc8(base64.b64decode(vvbc2vyh['v00vhm']))
  if hmac.compare_digest(j1i2hgj1(wgcl9lcq),vvbc2vyh.get('pca7zv','')):
   return json.loads(wgcl9lcq.decode('utf-8'))
 except Exception:
  pass
 return None
def diuu9k9x(hdw6lqwl):
 for ljk4q5v7 in(k44nlz15(hdw6lqwl),bwiykid9(hdw6lqwl)):
  if os.path.exists(ljk4q5v7):
   try:
    os.remove(ljk4q5v7)
   except OSError:
    pass
def gqq4d3kz(hdw6lqwl):
 fo75rh8l=yw5py6b2(hdw6lqwl)
 acxx6mdk=False
 if fo75rh8l is None:
  fo75rh8l=jmpioygg(hdw6lqwl)
  acxx6mdk=fo75rh8l is not None
 uwxrum2l=fp47b42g()
 if fo75rh8l:
  uwxrum2l.update(fo75rh8l)
  y9ayq6ww(hdw6lqwl,uwxrum2l)
  if acxx6mdk:
   diuu9k9x(hdw6lqwl)
 return uwxrum2l
def y9ayq6ww(hdw6lqwl,fo75rh8l):
 os.makedirs(khl1n13j,exist_ok=True)
 wgcl9lcq=json.dumps(fo75rh8l).encode('utf-8')
 vvbc2vyh={'v00vhm':base64.b64encode(iy6qktc8(wgcl9lcq)).decode('ascii'),'pca7zv':j1i2hgj1(wgcl9lcq)}
 with open(yx4w6xlp(hdw6lqwl),'w')as mc8qizk3:
  json.dump(vvbc2vyh,mc8qizk3)
def l1rdxck3(hdw6lqwl):
 if not sfu38gl2(hdw6lqwl):
  return None
 fo75rh8l=gqq4d3kz(hdw6lqwl)
 return{'resources':fo75rh8l.get('resources',0),'high_level':fo75rh8l.get('high_level',0),'runs_played':fo75rh8l.get('runs_played',0)}
