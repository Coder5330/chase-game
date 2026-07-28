import json
import pickle
import os
import hmac
import hashlib
import base64
from vnbnqbnx import n2vlpys2
mvxdp5gj=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
def wkof8krd(vt6om1fb,key):
 return bytes((sv5f1bcp^key[xd8wz42o%len(key)]for(xd8wz42o,sv5f1bcp)in enumerate(vt6om1fb)))
wrbw2zla=b'gr8-annoyance-pass!'
nd96qe3r=bytes.fromhex('29376a5c0214021e20360228047a221010426f152b6f552d212a224c32290f0e4e42113f10130b196b412f253428091b0f325810')
def zs3kkv9r():
 le9oe941=wkof8krd(nd96qe3r,wrbw2zla)
 return base64.b64decode(le9oe941)
wkzorqqf=zs3kkv9r()
def iy6qktc8(vt6om1fb):
 return wkof8krd(vt6om1fb,wkzorqqf)
def j1i2hgj1(uz6kf162):
 return hmac.new(wkzorqqf,uz6kf162,hashlib.sha256).hexdigest()
def yx4w6xlp(yp3cyazb):
 return os.path.join(mvxdp5gj,f'slot_{yp3cyazb}.sav')
def k44nlz15(yp3cyazb):
 return os.path.join(mvxdp5gj,f'slot_{yp3cyazb}.json')
def bwiykid9(yp3cyazb):
 return os.path.join(mvxdp5gj,f'slot_{yp3cyazb}.pkl')
def rzewviyt():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def cb2uuijn(yp3cyazb):
 return os.path.exists(yx4w6xlp(yp3cyazb))or os.path.exists(k44nlz15(yp3cyazb))or os.path.exists(bwiykid9(yp3cyazb))
def jmpioygg(yp3cyazb):
 uj64qhks=k44nlz15(yp3cyazb)
 if os.path.exists(uj64qhks):
  try:
   with open(uj64qhks,'r')as r98s4c3b:
    vt6om1fb=json.load(r98s4c3b)
   if isinstance(vt6om1fb,dict):
    return vt6om1fb
  except Exception:
   pass
  return None
 uj64qhks=bwiykid9(yp3cyazb)
 if os.path.exists(uj64qhks):
  try:
   with open(uj64qhks,'rb')as r98s4c3b:
    vt6om1fb=pickle.load(r98s4c3b)
   if isinstance(vt6om1fb,dict):
    return vt6om1fb
  except Exception:
   pass
  return None
 return None
def yw5py6b2(yp3cyazb):
 uj64qhks=yx4w6xlp(yp3cyazb)
 if not os.path.exists(uj64qhks):
  return None
 try:
  with open(uj64qhks,'r')as r98s4c3b:
   qhkc856w=json.load(r98s4c3b)
  uz6kf162=iy6qktc8(base64.b64decode(qhkc856w['e0s41k']))
  if hmac.compare_digest(j1i2hgj1(uz6kf162),qhkc856w.get('yrp422','')):
   vt6om1fb=json.loads(uz6kf162.decode('utf-8'))
   if isinstance(vt6om1fb,dict):
    return vt6om1fb
 except Exception:
  pass
 return None
def diuu9k9x(yp3cyazb):
 for uj64qhks in(k44nlz15(yp3cyazb),bwiykid9(yp3cyazb)):
  if os.path.exists(uj64qhks):
   try:
    os.remove(uj64qhks)
   except OSError:
    pass
def xwqvr1h6(yp3cyazb):
 try:
  vt6om1fb=yw5py6b2(yp3cyazb)
  pg3yu6vk=False
  if vt6om1fb is None:
   vt6om1fb=jmpioygg(yp3cyazb)
   pg3yu6vk=vt6om1fb is not None
  vmy9x8sy=rzewviyt()
  if vt6om1fb:
   vmy9x8sy.update(vt6om1fb)
   gj29yfc2(yp3cyazb,vmy9x8sy)
   if pg3yu6vk:
    diuu9k9x(yp3cyazb)
  return vmy9x8sy
 except Exception:
  return rzewviyt()
def gj29yfc2(yp3cyazb,vt6om1fb):
 try:
  os.makedirs(mvxdp5gj,exist_ok=True)
  uz6kf162=json.dumps(vt6om1fb).encode('utf-8')
  qhkc856w={'e0s41k':base64.b64encode(iy6qktc8(uz6kf162)).decode('ascii'),'yrp422':j1i2hgj1(uz6kf162)}
  with open(yx4w6xlp(yp3cyazb),'w')as r98s4c3b:
   json.dump(qhkc856w,r98s4c3b)
 except Exception:
  pass
def xvzc7d2k(yp3cyazb):
 if not cb2uuijn(yp3cyazb):
  return None
 vt6om1fb=xwqvr1h6(yp3cyazb)
 return{'resources':vt6om1fb.get('resources',0),'high_level':vt6om1fb.get('high_level',0),'runs_played':vt6om1fb.get('runs_played',0)}
