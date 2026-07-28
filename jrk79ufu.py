import json
import pickle
import os
import hmac
import hashlib
import base64
from omerbyea import n2vlpys2
khl1n13j=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def reqy08p0(uc1xi04b,key):
 return bytes((nrpj1epk^key[pcvsqame%len(key)]for(pcvsqame,nrpj1epk)in enumerate(uc1xi04b)))
nd96qe3r=b'gr8-annoyance-pass!'
wkzorqqf=bytes.fromhex('29376a5c0214021e20360228047a221010426f152b6f552d212a224c32290f0e4e42113f10130b196b412f253428091b0f325810')
def eqrl1n75():
 xuu13i59=reqy08p0(wkzorqqf,nd96qe3r)
 return base64.b64decode(xuu13i59)
g7s55j2o=eqrl1n75()
def sk8yqk94(uc1xi04b):
 return reqy08p0(uc1xi04b,g7s55j2o)
def yx4w6xlp(g1g1r1dw):
 return hmac.new(g7s55j2o,g1g1r1dw,hashlib.sha256).hexdigest()
def sne6loh2(sfu38gl2):
 return os.path.join(khl1n13j,f'slot_{sfu38gl2}.sav')
def bwiykid9(sfu38gl2):
 return os.path.join(khl1n13j,f'slot_{sfu38gl2}.json')
def yw5py6b2(sfu38gl2):
 return os.path.join(khl1n13j,f'slot_{sfu38gl2}.pkl')
def x875aud9():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def w0p4e05q(sfu38gl2):
 return os.path.exists(sne6loh2(sfu38gl2))or os.path.exists(bwiykid9(sfu38gl2))or os.path.exists(yw5py6b2(sfu38gl2))
def t5wi6fqj(sfu38gl2):
 cqheyto5=bwiykid9(sfu38gl2)
 if os.path.exists(cqheyto5):
  try:
   with open(cqheyto5,'r')as cx41dntc:
    uc1xi04b=json.load(cx41dntc)
   if isinstance(uc1xi04b,dict):
    return uc1xi04b
  except Exception:
   pass
  return None
 cqheyto5=yw5py6b2(sfu38gl2)
 if os.path.exists(cqheyto5):
  try:
   with open(cqheyto5,'rb')as cx41dntc:
    uc1xi04b=pickle.load(cx41dntc)
   if isinstance(uc1xi04b,dict):
    return uc1xi04b
  except Exception:
   pass
  return None
 return None
def jmpioygg(sfu38gl2):
 cqheyto5=sne6loh2(sfu38gl2)
 if not os.path.exists(cqheyto5):
  return None
 try:
  with open(cqheyto5,'r')as cx41dntc:
   g5l8a78e=json.load(cx41dntc)
  g1g1r1dw=sk8yqk94(base64.b64decode(g5l8a78e['gbwcv6']))
  if hmac.compare_digest(yx4w6xlp(g1g1r1dw),g5l8a78e.get('tgr8w2','')):
   uc1xi04b=json.loads(g1g1r1dw.decode('utf-8'))
   if isinstance(uc1xi04b,dict):
    return uc1xi04b
 except Exception:
  pass
 return None
def ia529603(sfu38gl2):
 for cqheyto5 in(bwiykid9(sfu38gl2),yw5py6b2(sfu38gl2)):
  if os.path.exists(cqheyto5):
   try:
    os.remove(cqheyto5)
   except OSError:
    pass
def tb4ldims(sfu38gl2):
 try:
  uc1xi04b=jmpioygg(sfu38gl2)
  cgsq7ait=False
  if uc1xi04b is None:
   uc1xi04b=t5wi6fqj(sfu38gl2)
   cgsq7ait=uc1xi04b is not None
  h8s2ftom=x875aud9()
  if uc1xi04b:
   h8s2ftom.update(uc1xi04b)
   byl68ntk(sfu38gl2,h8s2ftom)
   if cgsq7ait:
    ia529603(sfu38gl2)
  return h8s2ftom
 except Exception:
  return x875aud9()
def byl68ntk(sfu38gl2,uc1xi04b):
 try:
  os.makedirs(khl1n13j,exist_ok=True)
  g1g1r1dw=json.dumps(uc1xi04b).encode('utf-8')
  g5l8a78e={'gbwcv6':base64.b64encode(sk8yqk94(g1g1r1dw)).decode('ascii'),'tgr8w2':yx4w6xlp(g1g1r1dw)}
  with open(sne6loh2(sfu38gl2),'w')as cx41dntc:
   json.dump(g5l8a78e,cx41dntc)
 except Exception:
  pass
def rh0w064w(sfu38gl2):
 if not w0p4e05q(sfu38gl2):
  return None
 uc1xi04b=tb4ldims(sfu38gl2)
 return{'resources':uc1xi04b.get('resources',0),'high_level':uc1xi04b.get('high_level',0),'runs_played':uc1xi04b.get('runs_played',0)}
