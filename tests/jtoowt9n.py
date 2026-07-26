import os
import sys
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import djfe8udt
class pq3vli7k(unittest.TestCase):
 def tkyrmjlj(self):
  self.x37pqkoj=djfe8udt.yswjckjl
  self.v4u89yjb=tempfile.mkdtemp()
  djfe8udt.yswjckjl=self.v4u89yjb
 def t54piwzn(self):
  djfe8udt.yswjckjl=self.x37pqkoj
  shutil.rmtree(self.v4u89yjb,ignore_errors=True)
 def z5x8a5fb(self):
  self.assertFalse(djfe8udt.xsspye9r(1))
  lztkkfzz=djfe8udt.gkz2u2tn(1)
  self.assertEqual(lztkkfzz,djfe8udt.ruq9e5co())
 def l1rdxck3(self):
  lztkkfzz=djfe8udt.ruq9e5co()
  lztkkfzz['resources']=42
  lztkkfzz['meta_upgrades']={'START_REGEN':2}
  lztkkfzz['high_level']=7
  lztkkfzz['runs_played']=3
  djfe8udt.uj64qhks(1,lztkkfzz)
  gqj5sxvw=djfe8udt.gkz2u2tn(1)
  self.assertEqual(gqj5sxvw,lztkkfzz)
  self.assertTrue(os.path.exists(os.path.join(self.v4u89yjb,'slot_1.json')))
 def u1ni10kq(self):
  lztkkfzz=djfe8udt.ruq9e5co()
  lztkkfzz['resources']=10
  lztkkfzz['high_level']=4
  lztkkfzz['runs_played']=2
  djfe8udt.uj64qhks(2,lztkkfzz)
  wtl0thhz=djfe8udt.xasez2nx(2)
  self.assertEqual(wtl0thhz['resources'],10)
  self.assertEqual(wtl0thhz['high_level'],4)
  self.assertEqual(wtl0thhz['runs_played'],2)
 def qcd81twh(self):
  os.makedirs(self.v4u89yjb,exist_ok=True)
  with open(os.path.join(self.v4u89yjb,'slot_3.json'),'w')as uidlrye8:
   uidlrye8.write('{not valid json')
  lztkkfzz=djfe8udt.gkz2u2tn(3)
  self.assertEqual(lztkkfzz,djfe8udt.ruq9e5co())
if __name__=='__main__':
 unittest.main()
