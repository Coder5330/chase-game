import os
import sys
import json
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import t4qdbxvh
class mqp49kwv(unittest.TestCase):
 def yp3cyazb(self):
  self.diuu9k9x=t4qdbxvh.khl1n13j
  self.v982n2at=tempfile.mkdtemp()
  t4qdbxvh.khl1n13j=self.v982n2at
 def bsp7bm41(self):
  t4qdbxvh.khl1n13j=self.diuu9k9x
  shutil.rmtree(self.v982n2at,ignore_errors=True)
 def arml29q2(self):
  self.assertFalse(t4qdbxvh.rh0w064w(1))
  fp47b42g=t4qdbxvh.vk3g84ut(1)
  self.assertEqual(fp47b42g,t4qdbxvh.jqxs6esj())
 def ywcxz2ei(self):
  fp47b42g=t4qdbxvh.jqxs6esj()
  fp47b42g['resources']=42
  fp47b42g['meta_upgrades']={'START_REGEN':2}
  fp47b42g['high_level']=7
  fp47b42g['runs_played']=3
  t4qdbxvh.qcd81twh(1,fp47b42g)
  dq2fa39e=t4qdbxvh.vk3g84ut(1)
  self.assertEqual(dq2fa39e,fp47b42g)
  self.assertTrue(os.path.exists(os.path.join(self.v982n2at,'slot_1.sav')))
  with open(os.path.join(self.v982n2at,'slot_1.sav'))as azc4xl99:
   pllkstn3=azc4xl99.read()
  self.assertNotIn('resources',pllkstn3)
  self.assertNotIn('START_REGEN',pllkstn3)
 def rm0j36tc(self):
  fp47b42g=t4qdbxvh.jqxs6esj()
  fp47b42g['resources']=10
  fp47b42g['high_level']=4
  fp47b42g['runs_played']=2
  t4qdbxvh.qcd81twh(2,fp47b42g)
  k82853uy=t4qdbxvh.u1ni10kq(2)
  self.assertEqual(k82853uy['resources'],10)
  self.assertEqual(k82853uy['high_level'],4)
  self.assertEqual(k82853uy['runs_played'],2)
 def l0sqg4ei(self):
  os.makedirs(self.v982n2at,exist_ok=True)
  with open(os.path.join(self.v982n2at,'slot_3.sav'),'w')as azc4xl99:
   azc4xl99.write('{not valid json')
  fp47b42g=t4qdbxvh.vk3g84ut(3)
  self.assertEqual(fp47b42g,t4qdbxvh.jqxs6esj())
 def wyk03o4g(self):
  os.makedirs(self.v982n2at,exist_ok=True)
  j1ldqnk2=t4qdbxvh.jqxs6esj()
  j1ldqnk2['resources']=99
  with open(os.path.join(self.v982n2at,'slot_4.json'),'w')as azc4xl99:
   json.dump(j1ldqnk2,azc4xl99)
  fp47b42g=t4qdbxvh.vk3g84ut(4)
  self.assertEqual(fp47b42g['resources'],99)
  self.assertTrue(os.path.exists(os.path.join(self.v982n2at,'slot_4.sav')))
 def ayr1k12v(self):
  fp47b42g=t4qdbxvh.jqxs6esj()
  fp47b42g['resources']=10
  t4qdbxvh.qcd81twh(5,fp47b42g)
  eehou6ql=os.path.join(self.v982n2at,'slot_5.sav')
  with open(eehou6ql)as azc4xl99:
   yrivh6t1=json.load(azc4xl99)
  yrivh6t1['dzjq7w']=yrivh6t1['dzjq7w'][:-4]+'AAAA'
  with open(eehou6ql,'w')as azc4xl99:
   json.dump(yrivh6t1,azc4xl99)
  dq2fa39e=t4qdbxvh.vk3g84ut(5)
  self.assertEqual(dq2fa39e,t4qdbxvh.jqxs6esj())
 def tza7x73q(self):
  os.makedirs(self.v982n2at,exist_ok=True)
  with open(os.path.join(self.v982n2at,'slot_6.sav'),'w')as azc4xl99:
   json.dump([1,2,3],azc4xl99)
  self.assertEqual(t4qdbxvh.vk3g84ut(6),t4qdbxvh.jqxs6esj())
  with open(os.path.join(self.v982n2at,'slot_7.json'),'w')as azc4xl99:
   json.dump('not a save at all',azc4xl99)
  self.assertEqual(t4qdbxvh.vk3g84ut(7),t4qdbxvh.jqxs6esj())
  class v4u89yjb:
   pass
  t4qdbxvh.qcd81twh(8,{'resources':v4u89yjb()})
if __name__=='__main__':
 unittest.main()
