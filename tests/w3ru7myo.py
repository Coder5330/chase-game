import os
import sys
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import tx48wze4
class zakoixnt(unittest.TestCase):
 def hay64yfd(self):
  self.v83tqll8=tx48wze4.rcfnfhol
  self.nd96qe3r=tempfile.mkdtemp()
  tx48wze4.rcfnfhol=self.nd96qe3r
 def w0p4e05q(self):
  tx48wze4.rcfnfhol=self.v83tqll8
  shutil.rmtree(self.nd96qe3r,ignore_errors=True)
 def kodpvjtu(self):
  self.assertFalse(tx48wze4.ukshy8nb(1))
  u1jhuwb6=tx48wze4.n3rlkte4(1)
  self.assertEqual(u1jhuwb6,tx48wze4.bfoqmf5l())
 def wigbiaf9(self):
  u1jhuwb6=tx48wze4.bfoqmf5l()
  u1jhuwb6['resources']=42
  u1jhuwb6['meta_upgrades']={'START_REGEN':2}
  u1jhuwb6['high_level']=7
  u1jhuwb6['runs_played']=3
  tx48wze4.xwk2rv23(1,u1jhuwb6)
  zmybd2qe=tx48wze4.n3rlkte4(1)
  self.assertEqual(zmybd2qe,u1jhuwb6)
  self.assertTrue(os.path.exists(os.path.join(self.nd96qe3r,'slot_1.json')))
 def gqoagsus(self):
  u1jhuwb6=tx48wze4.bfoqmf5l()
  u1jhuwb6['resources']=10
  u1jhuwb6['high_level']=4
  u1jhuwb6['runs_played']=2
  tx48wze4.xwk2rv23(2,u1jhuwb6)
  ck7n3bfh=tx48wze4.d1hm38ks(2)
  self.assertEqual(ck7n3bfh['resources'],10)
  self.assertEqual(ck7n3bfh['high_level'],4)
  self.assertEqual(ck7n3bfh['runs_played'],2)
 def holeyrvx(self):
  os.makedirs(self.nd96qe3r,exist_ok=True)
  with open(os.path.join(self.nd96qe3r,'slot_3.json'),'w')as vhuds3qs:
   vhuds3qs.write('{not valid json')
  u1jhuwb6=tx48wze4.n3rlkte4(3)
  self.assertEqual(u1jhuwb6,tx48wze4.bfoqmf5l())
if __name__=='__main__':
 unittest.main()
