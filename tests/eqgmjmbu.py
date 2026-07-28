import os
import sys
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import pca7zvky
class pecruyf3(unittest.TestCase):
 def h4l1vznq(self):
  self.mnx39rbs=pca7zvky.ky20479t
  self.yw5py6b2=tempfile.mkdtemp()
  pca7zvky.ky20479t=self.yw5py6b2
 def nv23gxj0(self):
  pca7zvky.ky20479t=self.mnx39rbs
  shutil.rmtree(self.yw5py6b2,ignore_errors=True)
 def v7g0iiji(self):
  self.assertFalse(pca7zvky.xxns2zyb(1))
  qbbz2sf6=pca7zvky.q5amln4p(1)
  self.assertEqual(qbbz2sf6,pca7zvky.qtzk3ny9())
 def e9y3z2t4(self):
  qbbz2sf6=pca7zvky.qtzk3ny9()
  qbbz2sf6['resources']=42
  qbbz2sf6['meta_upgrades']={'START_REGEN':2}
  qbbz2sf6['high_level']=7
  qbbz2sf6['runs_played']=3
  pca7zvky.uaobt328(1,qbbz2sf6)
  ry181acj=pca7zvky.q5amln4p(1)
  self.assertEqual(ry181acj,qbbz2sf6)
  self.assertTrue(os.path.exists(os.path.join(self.yw5py6b2,'slot_1.json')))
 def wfhj4d0j(self):
  qbbz2sf6=pca7zvky.qtzk3ny9()
  qbbz2sf6['resources']=10
  qbbz2sf6['high_level']=4
  qbbz2sf6['runs_played']=2
  pca7zvky.uaobt328(2,qbbz2sf6)
  q6nqqb9l=pca7zvky.t54piwzn(2)
  self.assertEqual(q6nqqb9l['resources'],10)
  self.assertEqual(q6nqqb9l['high_level'],4)
  self.assertEqual(q6nqqb9l['runs_played'],2)
 def p7pchcbn(self):
  os.makedirs(self.yw5py6b2,exist_ok=True)
  with open(os.path.join(self.yw5py6b2,'slot_3.json'),'w')as qhkc856w:
   qhkc856w.write('{not valid json')
  qbbz2sf6=pca7zvky.q5amln4p(3)
  self.assertEqual(qbbz2sf6,pca7zvky.qtzk3ny9())
if __name__=='__main__':
 unittest.main()
