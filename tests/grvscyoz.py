import os
import sys
import json
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import j1bmqf7z
class mqp49kwv(unittest.TestCase):
 def y9ayq6ww(self):
  self.x52qc1iy=j1bmqf7z.khl1n13j
  self.gp84dyt9=tempfile.mkdtemp()
  j1bmqf7z.khl1n13j=self.gp84dyt9
 def mu118qqv(self):
  j1bmqf7z.khl1n13j=self.x52qc1iy
  shutil.rmtree(self.gp84dyt9,ignore_errors=True)
 def zanouof0(self):
  self.assertFalse(j1bmqf7z.v24479qt(1))
  x875aud9=j1bmqf7z.gqq4d3kz(1)
  self.assertEqual(x875aud9,j1bmqf7z.zefqjg02())
 def x9h0dxho(self):
  x875aud9=j1bmqf7z.zefqjg02()
  x875aud9['resources']=42
  x875aud9['meta_upgrades']={'START_REGEN':2}
  x875aud9['high_level']=7
  x875aud9['runs_played']=3
  j1bmqf7z.h8s2ftom(1,x875aud9)
  tb4ldims=j1bmqf7z.gqq4d3kz(1)
  self.assertEqual(tb4ldims,x875aud9)
  self.assertTrue(os.path.exists(os.path.join(self.gp84dyt9,'slot_1.sav')))
  with open(os.path.join(self.gp84dyt9,'slot_1.sav'))as azc4xl99:
   tby49e7e=azc4xl99.read()
  self.assertNotIn('resources',tby49e7e)
  self.assertNotIn('START_REGEN',tby49e7e)
 def f2voi8uy(self):
  x875aud9=j1bmqf7z.zefqjg02()
  x875aud9['resources']=10
  x875aud9['high_level']=4
  x875aud9['runs_played']=2
  j1bmqf7z.h8s2ftom(2,x875aud9)
  rwybow23=j1bmqf7z.hdw6lqwl(2)
  self.assertEqual(rwybow23['resources'],10)
  self.assertEqual(rwybow23['high_level'],4)
  self.assertEqual(rwybow23['runs_played'],2)
 def wfhj4d0j(self):
  os.makedirs(self.gp84dyt9,exist_ok=True)
  with open(os.path.join(self.gp84dyt9,'slot_3.sav'),'w')as azc4xl99:
   azc4xl99.write('{not valid json')
  x875aud9=j1bmqf7z.gqq4d3kz(3)
  self.assertEqual(x875aud9,j1bmqf7z.zefqjg02())
 def e8zgvwwu(self):
  os.makedirs(self.gp84dyt9,exist_ok=True)
  j1ldqnk2=j1bmqf7z.zefqjg02()
  j1ldqnk2['resources']=99
  with open(os.path.join(self.gp84dyt9,'slot_4.json'),'w')as azc4xl99:
   json.dump(j1ldqnk2,azc4xl99)
  x875aud9=j1bmqf7z.gqq4d3kz(4)
  self.assertEqual(x875aud9['resources'],99)
  self.assertTrue(os.path.exists(os.path.join(self.gp84dyt9,'slot_4.sav')))
 def rb1s9dwd(self):
  x875aud9=j1bmqf7z.zefqjg02()
  x875aud9['resources']=10
  j1bmqf7z.h8s2ftom(5,x875aud9)
  rgdej31g=os.path.join(self.gp84dyt9,'slot_5.sav')
  with open(rgdej31g)as azc4xl99:
   yrivh6t1=json.load(azc4xl99)
  yrivh6t1['mrf5a7']=yrivh6t1['mrf5a7'][:-4]+'AAAA'
  with open(rgdej31g,'w')as azc4xl99:
   json.dump(yrivh6t1,azc4xl99)
  tb4ldims=j1bmqf7z.gqq4d3kz(5)
  self.assertEqual(tb4ldims,j1bmqf7z.zefqjg02())
 def awnwlc83(self):
  os.makedirs(self.gp84dyt9,exist_ok=True)
  with open(os.path.join(self.gp84dyt9,'slot_6.sav'),'w')as azc4xl99:
   json.dump([1,2,3],azc4xl99)
  self.assertEqual(j1bmqf7z.gqq4d3kz(6),j1bmqf7z.zefqjg02())
  with open(os.path.join(self.gp84dyt9,'slot_7.json'),'w')as azc4xl99:
   json.dump('not a save at all',azc4xl99)
  self.assertEqual(j1bmqf7z.gqq4d3kz(7),j1bmqf7z.zefqjg02())
  class v4u89yjb:
   pass
  j1bmqf7z.h8s2ftom(8,{'resources':v4u89yjb()})
 def h4m2ec8r(self):
  x875aud9=j1bmqf7z.zefqjg02()
  x875aud9['resources']=999995752
  j1bmqf7z.h8s2ftom(9,x875aud9)
  tb4ldims=j1bmqf7z.gqq4d3kz(9)
  self.assertEqual(tb4ldims,j1bmqf7z.zefqjg02())
 def v7g0iiji(self):
  x875aud9=j1bmqf7z.zefqjg02()
  x875aud9['meta_upgrades']={'START_REGEN':999}
  j1bmqf7z.h8s2ftom(10,x875aud9)
  tb4ldims=j1bmqf7z.gqq4d3kz(10)
  self.assertEqual(tb4ldims,j1bmqf7z.zefqjg02())
 def eq3tq1s0(self):
  x875aud9=j1bmqf7z.zefqjg02()
  x875aud9['meta_upgrades']={'ifzkic':1}
  j1bmqf7z.h8s2ftom(11,x875aud9)
  tb4ldims=j1bmqf7z.gqq4d3kz(11)
  self.assertEqual(tb4ldims,j1bmqf7z.zefqjg02())
 def qxt6ridl(self):
  x875aud9=j1bmqf7z.zefqjg02()
  x875aud9['resources']=5000
  x875aud9['high_level']=40
  x875aud9['runs_played']=120
  x875aud9['meta_upgrades']={'START_REGEN':6,'START_HEALTH':10}
  j1bmqf7z.h8s2ftom(12,x875aud9)
  tb4ldims=j1bmqf7z.gqq4d3kz(12)
  self.assertEqual(tb4ldims,x875aud9)
if __name__=='__main__':
 unittest.main()
