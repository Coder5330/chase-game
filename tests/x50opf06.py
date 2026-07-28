import os
import sys
import json
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import kupnhzx9
class jdiuovw1(unittest.TestCase):
 def gxlk8wru(self):
  self.sne6loh2=kupnhzx9.mvxdp5gj
  self.reqy08p0=tempfile.mkdtemp()
  kupnhzx9.mvxdp5gj=self.reqy08p0
 def mu118qqv(self):
  kupnhzx9.mvxdp5gj=self.sne6loh2
  shutil.rmtree(self.reqy08p0,ignore_errors=True)
 def zanouof0(self):
  self.assertFalse(kupnhzx9.v24479qt(1))
  uc1xi04b=kupnhzx9.zo3lqi7e(1)
  self.assertEqual(uc1xi04b,kupnhzx9.x875aud9())
 def x9h0dxho(self):
  uc1xi04b=kupnhzx9.x875aud9()
  uc1xi04b['resources']=42
  uc1xi04b['meta_upgrades']={'START_REGEN':2}
  uc1xi04b['high_level']=7
  uc1xi04b['runs_played']=3
  kupnhzx9.uwxrum2l(1,uc1xi04b)
  yvffqot8=kupnhzx9.zo3lqi7e(1)
  self.assertEqual(yvffqot8,uc1xi04b)
  self.assertTrue(os.path.exists(os.path.join(self.reqy08p0,'slot_1.sav')))
  with open(os.path.join(self.reqy08p0,'slot_1.sav'))as mc8qizk3:
   fd6rupw2=mc8qizk3.read()
  self.assertNotIn('resources',fd6rupw2)
  self.assertNotIn('START_REGEN',fd6rupw2)
 def f2voi8uy(self):
  uc1xi04b=kupnhzx9.x875aud9()
  uc1xi04b['resources']=10
  uc1xi04b['high_level']=4
  uc1xi04b['runs_played']=2
  kupnhzx9.uwxrum2l(2,uc1xi04b)
  rwybow23=kupnhzx9.hdw6lqwl(2)
  self.assertEqual(rwybow23['resources'],10)
  self.assertEqual(rwybow23['high_level'],4)
  self.assertEqual(rwybow23['runs_played'],2)
 def wfhj4d0j(self):
  os.makedirs(self.reqy08p0,exist_ok=True)
  with open(os.path.join(self.reqy08p0,'slot_3.sav'),'w')as mc8qizk3:
   mc8qizk3.write('{not valid json')
  uc1xi04b=kupnhzx9.zo3lqi7e(3)
  self.assertEqual(uc1xi04b,kupnhzx9.x875aud9())
 def e8zgvwwu(self):
  os.makedirs(self.reqy08p0,exist_ok=True)
  nii6l3ue=kupnhzx9.x875aud9()
  nii6l3ue['resources']=99
  with open(os.path.join(self.reqy08p0,'slot_4.json'),'w')as mc8qizk3:
   json.dump(nii6l3ue,mc8qizk3)
  uc1xi04b=kupnhzx9.zo3lqi7e(4)
  self.assertEqual(uc1xi04b['resources'],99)
  self.assertTrue(os.path.exists(os.path.join(self.reqy08p0,'slot_4.sav')))
 def rb1s9dwd(self):
  uc1xi04b=kupnhzx9.x875aud9()
  uc1xi04b['resources']=10
  kupnhzx9.uwxrum2l(5,uc1xi04b)
  vt26ys44=os.path.join(self.reqy08p0,'slot_5.sav')
  with open(vt26ys44)as mc8qizk3:
   vvbc2vyh=json.load(mc8qizk3)
  vvbc2vyh['kj2jvq']=vvbc2vyh['kj2jvq'][:-4]+'AAAA'
  with open(vt26ys44,'w')as mc8qizk3:
   json.dump(vvbc2vyh,mc8qizk3)
  yvffqot8=kupnhzx9.zo3lqi7e(5)
  self.assertEqual(yvffqot8,kupnhzx9.x875aud9())
 def awnwlc83(self):
  os.makedirs(self.reqy08p0,exist_ok=True)
  with open(os.path.join(self.reqy08p0,'slot_6.sav'),'w')as mc8qizk3:
   json.dump([1,2,3],mc8qizk3)
  self.assertEqual(kupnhzx9.zo3lqi7e(6),kupnhzx9.x875aud9())
  with open(os.path.join(self.reqy08p0,'slot_7.json'),'w')as mc8qizk3:
   json.dump('not a save at all',mc8qizk3)
  self.assertEqual(kupnhzx9.zo3lqi7e(7),kupnhzx9.x875aud9())
  class rrcbpljd:
   pass
  kupnhzx9.uwxrum2l(8,{'resources':rrcbpljd()})
 def h4m2ec8r(self):
  uc1xi04b=kupnhzx9.x875aud9()
  uc1xi04b['resources']=999995752
  kupnhzx9.uwxrum2l(9,uc1xi04b)
  yvffqot8=kupnhzx9.zo3lqi7e(9)
  self.assertEqual(yvffqot8,kupnhzx9.x875aud9())
 def v7g0iiji(self):
  uc1xi04b=kupnhzx9.x875aud9()
  uc1xi04b['meta_upgrades']={'START_REGEN':999}
  kupnhzx9.uwxrum2l(10,uc1xi04b)
  yvffqot8=kupnhzx9.zo3lqi7e(10)
  self.assertEqual(yvffqot8,kupnhzx9.x875aud9())
 def eq3tq1s0(self):
  uc1xi04b=kupnhzx9.x875aud9()
  uc1xi04b['meta_upgrades']={'swyqml':1}
  kupnhzx9.uwxrum2l(11,uc1xi04b)
  yvffqot8=kupnhzx9.zo3lqi7e(11)
  self.assertEqual(yvffqot8,kupnhzx9.x875aud9())
 def qxt6ridl(self):
  uc1xi04b=kupnhzx9.x875aud9()
  uc1xi04b['resources']=5000
  uc1xi04b['high_level']=40
  uc1xi04b['runs_played']=120
  uc1xi04b['meta_upgrades']={'START_REGEN':6,'START_HEALTH':10}
  kupnhzx9.uwxrum2l(12,uc1xi04b)
  yvffqot8=kupnhzx9.zo3lqi7e(12)
  self.assertEqual(yvffqot8,uc1xi04b)
if __name__=='__main__':
 unittest.main()
