import json
import pickle
import os
import hmac
import hashlib
import base64
from entfk7or import n2vlpys2,jsylztgx
mvxdp5gj=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
g7s55j2o=1000000
wkzorqqf=1000
zs3kkv9r=100000
def ia529603(uc1xi04b):
 if not isinstance(uc1xi04b,dict):
  return False
 d1hm38ks=uc1xi04b.get('resources',0)
 if isinstance(d1hm38ks,bool)or not isinstance(d1hm38ks,(int,float)):
  return False
 if not 0<=d1hm38ks<=g7s55j2o:
  return False
 rk2u1rsu=uc1xi04b.get('high_level',0)
 if isinstance(rk2u1rsu,bool)or not isinstance(rk2u1rsu,(int,float)):
  return False
 if not 0<=rk2u1rsu<=wkzorqqf:
  return False
 xxns2zyb=uc1xi04b.get('runs_played',0)
 if isinstance(xxns2zyb,bool)or not isinstance(xxns2zyb,(int,float)):
  return False
 if not 0<=xxns2zyb<=zs3kkv9r:
  return False
 meta_upgrades=uc1xi04b.get('meta_upgrades',{})
 if not isinstance(meta_upgrades,dict):
  return False
 for(key,gqq4d3kz)in meta_upgrades.items():
  o4dd1vn8=jsylztgx.get(key)
  if o4dd1vn8 is None:
   return False
  if isinstance(gqq4d3kz,bool)or not isinstance(gqq4d3kz,(int,float)):
   return False
  if not 0<=gqq4d3kz<=o4dd1vn8['hrctlt']:
   return False
 return True
def uva2ieuc(uc1xi04b,key):
 return bytes((aqclpoxk^key[pcvsqame%len(key)]for(pcvsqame,aqclpoxk)in enumerate(uc1xi04b)))
nd96qe3r=b'gr8-annoyance-pass!'
eqrl1n75=bytes.fromhex('29376a5c0214021e20360228047a221010426f152b6f552d212a224c32290f0e4e42113f10130b196b412f253428091b0f325810')
def sld4d6af():
 xuu13i59=uva2ieuc(eqrl1n75,nd96qe3r)
 return base64.b64decode(xuu13i59)
win4olr6=sld4d6af()
def yx4w6xlp(uc1xi04b):
 return uva2ieuc(uc1xi04b,win4olr6)
def v982n2at(ljk4q5v7):
 return hmac.new(win4olr6,ljk4q5v7,hashlib.sha256).hexdigest()
def on0jnwny(n64fgwje):
 return os.path.join(mvxdp5gj,f'slot_{n64fgwje}.sav')
def t5wi6fqj(n64fgwje):
 return os.path.join(mvxdp5gj,f'slot_{n64fgwje}.json')
def iy6qktc8(n64fgwje):
 return os.path.join(mvxdp5gj,f'slot_{n64fgwje}.pkl')
def x875aud9():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def v24479qt(n64fgwje):
 return os.path.exists(on0jnwny(n64fgwje))or os.path.exists(t5wi6fqj(n64fgwje))or os.path.exists(iy6qktc8(n64fgwje))
def diuu9k9x(n64fgwje):
 vt26ys44=t5wi6fqj(n64fgwje)
 if os.path.exists(vt26ys44):
  try:
   with open(vt26ys44,'r')as mc8qizk3:
    uc1xi04b=json.load(mc8qizk3)
   if isinstance(uc1xi04b,dict):
    return uc1xi04b
  except Exception:
   pass
  return None
 vt26ys44=iy6qktc8(n64fgwje)
 if os.path.exists(vt26ys44):
  try:
   with open(vt26ys44,'rb')as mc8qizk3:
    uc1xi04b=pickle.load(mc8qizk3)
   if isinstance(uc1xi04b,dict):
    return uc1xi04b
  except Exception:
   pass
  return None
 return None
def sk8yqk94(n64fgwje):
 vt26ys44=on0jnwny(n64fgwje)
 if not os.path.exists(vt26ys44):
  return None
 try:
  with open(vt26ys44,'r')as mc8qizk3:
   vvbc2vyh=json.load(mc8qizk3)
  ljk4q5v7=yx4w6xlp(base64.b64decode(vvbc2vyh['kj2jvq']))
  if hmac.compare_digest(v982n2at(ljk4q5v7),vvbc2vyh.get('be2wnf','')):
   uc1xi04b=json.loads(ljk4q5v7.decode('utf-8'))
   if isinstance(uc1xi04b,dict):
    return uc1xi04b
 except Exception:
  pass
 return None
def lt63j3r3(n64fgwje):
 for vt26ys44 in(t5wi6fqj(n64fgwje),iy6qktc8(n64fgwje)):
  if os.path.exists(vt26ys44):
   try:
    os.remove(vt26ys44)
   except OSError:
    pass
def zo3lqi7e(n64fgwje):
 try:
  uc1xi04b=sk8yqk94(n64fgwje)
  yjr0fzau=False
  if uc1xi04b is None:
   uc1xi04b=diuu9k9x(n64fgwje)
   yjr0fzau=uc1xi04b is not None
  if uc1xi04b is not None and(not ia529603(uc1xi04b)):
   uc1xi04b=None
  stv18kgy=x875aud9()
  if uc1xi04b:
   stv18kgy.update(uc1xi04b)
   uwxrum2l(n64fgwje,stv18kgy)
   if yjr0fzau:
    lt63j3r3(n64fgwje)
  return stv18kgy
 except Exception:
  return x875aud9()
def uwxrum2l(n64fgwje,uc1xi04b):
 try:
  os.makedirs(mvxdp5gj,exist_ok=True)
  ljk4q5v7=json.dumps(uc1xi04b).encode('utf-8')
  vvbc2vyh={'kj2jvq':base64.b64encode(yx4w6xlp(ljk4q5v7)).decode('ascii'),'be2wnf':v982n2at(ljk4q5v7)}
  with open(on0jnwny(n64fgwje),'w')as mc8qizk3:
   json.dump(vvbc2vyh,mc8qizk3)
 except Exception:
  pass
def hdw6lqwl(n64fgwje):
 if not v24479qt(n64fgwje):
  return None
 uc1xi04b=zo3lqi7e(n64fgwje)
 return{'resources':uc1xi04b.get('resources',0),'high_level':uc1xi04b.get('high_level',0),'runs_played':uc1xi04b.get('runs_played',0)}
