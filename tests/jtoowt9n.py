import os
import sys
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import djfe8udt
class pq3vli7k(unittest.TestCase):
 def z3olfark(self):
  self.x37pqkoj=djfe8udt.yswjckjl
  self.v4u89yjb=tempfile.mkdtemp()
  djfe8udt.yswjckjl=self.v4u89yjb
 def stv18kgy(self):
  djfe8udt.yswjckjl=self.x37pqkoj
  shutil.rmtree(self.v4u89yjb,ignore_errors=True)
 def svt8k06m(self):
  self.assertFalse(djfe8udt.xasez2nx(1))
  lztkkfzz=djfe8udt.semqgy27(1)
  self.assertEqual(lztkkfzz,djfe8udt.ruq9e5co())
 def rh0w064w(self):
  lztkkfzz=djfe8udt.ruq9e5co()
  lztkkfzz['resources']=42
  lztkkfzz['meta_upgrades']={'START_REGEN':2}
  lztkkfzz['high_level']=7
  lztkkfzz['runs_played']=3
  djfe8udt.tkyrmjlj(1,lztkkfzz)
  sdeekgys=djfe8udt.semqgy27(1)
  self.assertEqual(sdeekgys,lztkkfzz)
  self.assertTrue(os.path.exists(os.path.join(self.v4u89yjb,'slot_1.json')))
 def qdnai89y(self):
  lztkkfzz=djfe8udt.ruq9e5co()
  lztkkfzz['resources']=10
  lztkkfzz['high_level']=4
  lztkkfzz['runs_played']=2
  djfe8udt.tkyrmjlj(2,lztkkfzz)
  vmy9x8sy=djfe8udt.npejzhya(2)
  self.assertEqual(vmy9x8sy['resources'],10)
  self.assertEqual(vmy9x8sy['high_level'],4)
  self.assertEqual(vmy9x8sy['runs_played'],2)
 def u15pdtz9(self):
  os.makedirs(self.v4u89yjb,exist_ok=True)
  with open(os.path.join(self.v4u89yjb,'slot_3.json'),'w')as uidlrye8:
   uidlrye8.write('{not valid json')
  lztkkfzz=djfe8udt.semqgy27(3)
  self.assertEqual(lztkkfzz,djfe8udt.ruq9e5co())
if __name__=='__main__':
 unittest.main()
