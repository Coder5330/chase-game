import json
import pickle
import os
import sys
import hmac
import hashlib
import base64
from jggz62fe import z0xkxwd8,my6wktak
if getattr(sys,'frozen',False):
 mnx39rbs=os.path.dirname(sys.executable)
else:
 mnx39rbs=os.path.dirname(os.path.abspath(__file__))
khl1n13j=os.path.join(mnx39rbs,'saves')
zs3kkv9r=1000000
g7s55j2o=1000
eqrl1n75=100000
def yx4w6xlp(x875aud9):
 if not isinstance(x875aud9,dict):
  return False
 wd6r30oj=x875aud9.get('resources',0)
 if isinstance(wd6r30oj,bool)or not isinstance(wd6r30oj,(int,float)):
  return False
 if not 0<=wd6r30oj<=zs3kkv9r:
  return False
 nd31k9qm=x875aud9.get('high_level',0)
 if isinstance(nd31k9qm,bool)or not isinstance(nd31k9qm,(int,float)):
  return False
 if not 0<=nd31k9qm<=g7s55j2o:
  return False
 mn89ltaj=x875aud9.get('runs_played',0)
 if isinstance(mn89ltaj,bool)or not isinstance(mn89ltaj,(int,float)):
  return False
 if not 0<=mn89ltaj<=eqrl1n75:
  return False
 meta_upgrades=x875aud9.get('meta_upgrades',{})
 if not isinstance(meta_upgrades,dict):
  return False
 for(key,vk3g84ut)in meta_upgrades.items():
  wa45hvgo=my6wktak.get(key)
  if wa45hvgo is None:
   return False
  if isinstance(vk3g84ut,bool)or not isinstance(vk3g84ut,(int,float)):
   return False
  if not 0<=vk3g84ut<=wa45hvgo['ykht8x']:
   return False
 return True
def i4fejgxa(x875aud9,key):
 return bytes((divsolml^key[je11e9ft%len(key)]for(je11e9ft,divsolml)in enumerate(x875aud9)))
wkzorqqf=b'gr8-annoyance-pass!'
win4olr6=bytes.fromhex('29376a5c0214021e20360228047a221010426f152b6f552d212a224c32290f0e4e42113f10130b196b412f253428091b0f325810')
def k44nlz15():
 nubmxnsz=i4fejgxa(win4olr6,wkzorqqf)
 return base64.b64decode(nubmxnsz)
sld4d6af=k44nlz15()
def lt63j3r3(x875aud9):
 return i4fejgxa(x875aud9,sld4d6af)
def pa5u6hc3(cqheyto5):
 return hmac.new(sld4d6af,cqheyto5,hashlib.sha256).hexdigest()
def wkof8krd(n64fgwje):
 return os.path.join(khl1n13j,f'slot_{n64fgwje}.sav')
def sk8yqk94(n64fgwje):
 return os.path.join(khl1n13j,f'slot_{n64fgwje}.json')
def diuu9k9x(n64fgwje):
 return os.path.join(khl1n13j,f'slot_{n64fgwje}.pkl')
def zefqjg02():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def v24479qt(n64fgwje):
 return os.path.exists(wkof8krd(n64fgwje))or os.path.exists(sk8yqk94(n64fgwje))or os.path.exists(diuu9k9x(n64fgwje))
def j1i2hgj1(n64fgwje):
 rgdej31g=sk8yqk94(n64fgwje)
 if os.path.exists(rgdej31g):
  try:
   with open(rgdej31g,'r')as azc4xl99:
    x875aud9=json.load(azc4xl99)
   if isinstance(x875aud9,dict):
    return x875aud9
  except Exception:
   pass
  return None
 rgdej31g=diuu9k9x(n64fgwje)
 if os.path.exists(rgdej31g):
  try:
   with open(rgdej31g,'rb')as azc4xl99:
    x875aud9=pickle.load(azc4xl99)
   if isinstance(x875aud9,dict):
    return x875aud9
  except Exception:
   pass
  return None
 return None
def ia529603(n64fgwje):
 rgdej31g=wkof8krd(n64fgwje)
 if not os.path.exists(rgdej31g):
  return None
 try:
  with open(rgdej31g,'r')as azc4xl99:
   yrivh6t1=json.load(azc4xl99)
  cqheyto5=lt63j3r3(base64.b64decode(yrivh6t1['mrf5a7']))
  if hmac.compare_digest(pa5u6hc3(cqheyto5),yrivh6t1.get('voeytl','')):
   x875aud9=json.loads(cqheyto5.decode('utf-8'))
   if isinstance(x875aud9,dict):
    return x875aud9
 except Exception:
  pass
 return None
def v982n2at(n64fgwje):
 for rgdej31g in(sk8yqk94(n64fgwje),diuu9k9x(n64fgwje)):
  if os.path.exists(rgdej31g):
   try:
    os.remove(rgdej31g)
   except OSError:
    pass
def gqq4d3kz(n64fgwje):
 try:
  x875aud9=ia529603(n64fgwje)
  yjr0fzau=False
  if x875aud9 is None:
   x875aud9=j1i2hgj1(n64fgwje)
   yjr0fzau=x875aud9 is not None
  if x875aud9 is not None and(not yx4w6xlp(x875aud9)):
   x875aud9=None
  f80ebkjf=zefqjg02()
  if x875aud9:
   f80ebkjf.update(x875aud9)
   h8s2ftom(n64fgwje,f80ebkjf)
   if yjr0fzau:
    v982n2at(n64fgwje)
  return f80ebkjf
 except Exception:
  return zefqjg02()
def h8s2ftom(n64fgwje,x875aud9):
 try:
  os.makedirs(khl1n13j,exist_ok=True)
  cqheyto5=json.dumps(x875aud9).encode('utf-8')
  yrivh6t1={'mrf5a7':base64.b64encode(lt63j3r3(cqheyto5)).decode('ascii'),'voeytl':pa5u6hc3(cqheyto5)}
  with open(wkof8krd(n64fgwje),'w')as azc4xl99:
   json.dump(yrivh6t1,azc4xl99)
 except Exception:
  pass
def hdw6lqwl(n64fgwje):
 if not v24479qt(n64fgwje):
  return None
 x875aud9=gqq4d3kz(n64fgwje)
 return{'resources':x875aud9.get('resources',0),'high_level':x875aud9.get('high_level',0),'runs_played':x875aud9.get('runs_played',0)}
