import json
import pickle
import os
import hmac
import hashlib
import base64
from zfiblejg import n2vlpys2,jsylztgx
mvxdp5gj=os.path.join(os.path.dirname(os.path.abspath(__file__)),'saves')
wkzorqqf=1000000
nd96qe3r=1000
g7s55j2o=100000
def diuu9k9x(fo75rh8l):
 if not isinstance(fo75rh8l,dict):
  return False
 h4l1vznq=fo75rh8l.get('resources',0)
 if isinstance(h4l1vznq,bool)or not isinstance(h4l1vznq,(int,float)):
  return False
 if not 0<=h4l1vznq<=wkzorqqf:
  return False
 w4rcb1kj=fo75rh8l.get('high_level',0)
 if isinstance(w4rcb1kj,bool)or not isinstance(w4rcb1kj,(int,float)):
  return False
 if not 0<=w4rcb1kj<=nd96qe3r:
  return False
 g1b3d505=fo75rh8l.get('runs_played',0)
 if isinstance(g1b3d505,bool)or not isinstance(g1b3d505,(int,float)):
  return False
 if not 0<=g1b3d505<=g7s55j2o:
  return False
 meta_upgrades=fo75rh8l.get('meta_upgrades',{})
 if not isinstance(meta_upgrades,dict):
  return False
 for(key,yvffqot8)in meta_upgrades.items():
  avfmh07w=jsylztgx.get(key)
  if avfmh07w is None:
   return False
  if isinstance(yvffqot8,bool)or not isinstance(yvffqot8,(int,float)):
   return False
  if not 0<=yvffqot8<=avfmh07w['jz6wmd']:
   return False
 return True
def lcj883dh(fo75rh8l,key):
 return bytes((rzs43c5b^key[bokzixza%len(key)]for(bokzixza,rzs43c5b)in enumerate(fo75rh8l)))
wrbw2zla=b'gr8-annoyance-pass!'
zs3kkv9r=bytes.fromhex('29376a5c0214021e20360228047a221010426f152b6f552d212a224c32290f0e4e42113f10130b196b412f253428091b0f325810')
def mnx39rbs():
 boih5csk=lcj883dh(zs3kkv9r,wrbw2zla)
 return base64.b64decode(boih5csk)
eqrl1n75=mnx39rbs()
def j1i2hgj1(fo75rh8l):
 return lcj883dh(fo75rh8l,eqrl1n75)
def x52qc1iy(v6xii5p5):
 return hmac.new(eqrl1n75,v6xii5p5,hashlib.sha256).hexdigest()
def v982n2at(svt8k06m):
 return os.path.join(mvxdp5gj,f'slot_{svt8k06m}.sav')
def jmpioygg(svt8k06m):
 return os.path.join(mvxdp5gj,f'slot_{svt8k06m}.json')
def t5wi6fqj(svt8k06m):
 return os.path.join(mvxdp5gj,f'slot_{svt8k06m}.pkl')
def fp47b42g():
 return{'resources':0,'meta_upgrades':{},'high_level':0,'runs_played':0}
def n64fgwje(svt8k06m):
 return os.path.exists(v982n2at(svt8k06m))or os.path.exists(jmpioygg(svt8k06m))or os.path.exists(t5wi6fqj(svt8k06m))
def sk8yqk94(svt8k06m):
 no0u93mz=jmpioygg(svt8k06m)
 if os.path.exists(no0u93mz):
  try:
   with open(no0u93mz,'r')as fddfgs3j:
    fo75rh8l=json.load(fddfgs3j)
   if isinstance(fo75rh8l,dict):
    return fo75rh8l
  except Exception:
   pass
  return None
 no0u93mz=t5wi6fqj(svt8k06m)
 if os.path.exists(no0u93mz):
  try:
   with open(no0u93mz,'rb')as fddfgs3j:
    fo75rh8l=pickle.load(fddfgs3j)
   if isinstance(fo75rh8l,dict):
    return fo75rh8l
  except Exception:
   pass
  return None
 return None
def iy6qktc8(svt8k06m):
 no0u93mz=v982n2at(svt8k06m)
 if not os.path.exists(no0u93mz):
  return None
 try:
  with open(no0u93mz,'r')as fddfgs3j:
   kx74d0gj=json.load(fddfgs3j)
  v6xii5p5=j1i2hgj1(base64.b64decode(kx74d0gj['onlt8d']))
  if hmac.compare_digest(x52qc1iy(v6xii5p5),kx74d0gj.get('zhbgcj','')):
   fo75rh8l=json.loads(v6xii5p5.decode('utf-8'))
   if isinstance(fo75rh8l,dict):
    return fo75rh8l
 except Exception:
  pass
 return None
def sne6loh2(svt8k06m):
 for no0u93mz in(jmpioygg(svt8k06m),t5wi6fqj(svt8k06m)):
  if os.path.exists(no0u93mz):
   try:
    os.remove(no0u93mz)
   except OSError:
    pass
def mcup8ijl(svt8k06m):
 try:
  fo75rh8l=iy6qktc8(svt8k06m)
  w2kql0ht=False
  if fo75rh8l is None:
   fo75rh8l=sk8yqk94(svt8k06m)
   w2kql0ht=fo75rh8l is not None
  if fo75rh8l is not None and(not diuu9k9x(fo75rh8l)):
   fo75rh8l=None
  t54piwzn=fp47b42g()
  if fo75rh8l:
   t54piwzn.update(fo75rh8l)
   iaq7b7v1(svt8k06m,t54piwzn)
   if w2kql0ht:
    sne6loh2(svt8k06m)
  return t54piwzn
 except Exception:
  return fp47b42g()
def iaq7b7v1(svt8k06m,fo75rh8l):
 try:
  os.makedirs(mvxdp5gj,exist_ok=True)
  v6xii5p5=json.dumps(fo75rh8l).encode('utf-8')
  kx74d0gj={'onlt8d':base64.b64encode(j1i2hgj1(v6xii5p5)).decode('ascii'),'zhbgcj':x52qc1iy(v6xii5p5)}
  with open(v982n2at(svt8k06m),'w')as fddfgs3j:
   json.dump(kx74d0gj,fddfgs3j)
 except Exception:
  pass
def jyjhu8my(svt8k06m):
 if not n64fgwje(svt8k06m):
  return None
 fo75rh8l=mcup8ijl(svt8k06m)
 return{'resources':fo75rh8l.get('resources',0),'high_level':fo75rh8l.get('high_level',0),'runs_played':fo75rh8l.get('runs_played',0)}
