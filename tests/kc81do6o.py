import os
import sys
import json
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import entfk7or
class mqp49kwv(unittest.TestCase):
 def q3n2qb6g(self):
  self.sk8yqk94=entfk7or.khl1n13j
  self.x52qc1iy=tempfile.mkdtemp()
  entfk7or.khl1n13j=self.x52qc1iy
 def h4m2ec8r(self):
  entfk7or.khl1n13j=self.sk8yqk94
  shutil.rmtree(self.x52qc1iy,ignore_errors=True)
 def wyk03o4g(self):
  self.assertFalse(entfk7or.sfu38gl2(1))
  fo75rh8l=entfk7or.gqq4d3kz(1)
  self.assertEqual(fo75rh8l,entfk7or.fp47b42g())
 def jh55hewl(self):
  fo75rh8l=entfk7or.fp47b42g()
  fo75rh8l['resources']=42
  fo75rh8l['meta_upgrades']={'START_REGEN':2}
  fo75rh8l['high_level']=7
  fo75rh8l['runs_played']=3
  entfk7or.y9ayq6ww(1,fo75rh8l)
  tb4ldims=entfk7or.gqq4d3kz(1)
  self.assertEqual(tb4ldims,fo75rh8l)
  self.assertTrue(os.path.exists(os.path.join(self.x52qc1iy,'slot_1.sav')))
  with open(os.path.join(self.x52qc1iy,'slot_1.sav'))as mc8qizk3:
   v0rxxf36=mc8qizk3.read()
  self.assertNotIn('resources',v0rxxf36)
  self.assertNotIn('START_REGEN',v0rxxf36)
 def ywcxz2ei(self):
  fo75rh8l=entfk7or.fp47b42g()
  fo75rh8l['resources']=10
  fo75rh8l['high_level']=4
  fo75rh8l['runs_played']=2
  entfk7or.y9ayq6ww(2,fo75rh8l)
  yoyohaz7=entfk7or.l1rdxck3(2)
  self.assertEqual(yoyohaz7['resources'],10)
  self.assertEqual(yoyohaz7['high_level'],4)
  self.assertEqual(yoyohaz7['runs_played'],2)
 def y06nkwfg(self):
  os.makedirs(self.x52qc1iy,exist_ok=True)
  with open(os.path.join(self.x52qc1iy,'slot_3.sav'),'w')as mc8qizk3:
   mc8qizk3.write('{not valid json')
  fo75rh8l=entfk7or.gqq4d3kz(3)
  self.assertEqual(fo75rh8l,entfk7or.fp47b42g())
 def ayr1k12v(self):
  os.makedirs(self.x52qc1iy,exist_ok=True)
  nii6l3ue=entfk7or.fp47b42g()
  nii6l3ue['resources']=99
  with open(os.path.join(self.x52qc1iy,'slot_4.json'),'w')as mc8qizk3:
   json.dump(nii6l3ue,mc8qizk3)
  fo75rh8l=entfk7or.gqq4d3kz(4)
  self.assertEqual(fo75rh8l['resources'],99)
  self.assertTrue(os.path.exists(os.path.join(self.x52qc1iy,'slot_4.sav')))
 def e8zgvwwu(self):
  fo75rh8l=entfk7or.fp47b42g()
  fo75rh8l['resources']=10
  entfk7or.y9ayq6ww(5,fo75rh8l)
  ljk4q5v7=os.path.join(self.x52qc1iy,'slot_5.sav')
  with open(ljk4q5v7)as mc8qizk3:
   vvbc2vyh=json.load(mc8qizk3)
  vvbc2vyh['v00vhm']=vvbc2vyh['v00vhm'][:-4]+'AAAA'
  with open(ljk4q5v7,'w')as mc8qizk3:
   json.dump(vvbc2vyh,mc8qizk3)
  tb4ldims=entfk7or.gqq4d3kz(5)
  self.assertEqual(tb4ldims,entfk7or.fp47b42g())
if __name__=='__main__':
 unittest.main()
