import os
import sys
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import qbtr23qi
class mqp49kwv(unittest.TestCase):
 def kz1uu7zy(self):
  self.u8c2jwoc=qbtr23qi.khl1n13j
  self.t5wi6fqj=tempfile.mkdtemp()
  qbtr23qi.khl1n13j=self.t5wi6fqj
 def d0qzfhom(self):
  qbtr23qi.khl1n13j=self.u8c2jwoc
  shutil.rmtree(self.t5wi6fqj,ignore_errors=True)
 def wfhj4d0j(self):
  self.assertFalse(qbtr23qi.q3n2qb6g(1))
  mfyb8dal=qbtr23qi.sye0a4ab(1)
  self.assertEqual(mfyb8dal,qbtr23qi.wehlxslg())
 def rb1s9dwd(self):
  mfyb8dal=qbtr23qi.wehlxslg()
  mfyb8dal['resources']=42
  mfyb8dal['meta_upgrades']={'START_REGEN':2}
  mfyb8dal['high_level']=7
  mfyb8dal['runs_played']=3
  qbtr23qi.wtl0thhz(1,mfyb8dal)
  lnf74t60=qbtr23qi.sye0a4ab(1)
  self.assertEqual(lnf74t60,mfyb8dal)
  self.assertTrue(os.path.exists(os.path.join(self.t5wi6fqj,'slot_1.json')))
 def e8zgvwwu(self):
  mfyb8dal=qbtr23qi.wehlxslg()
  mfyb8dal['resources']=10
  mfyb8dal['high_level']=4
  mfyb8dal['runs_played']=2
  qbtr23qi.wtl0thhz(2,mfyb8dal)
  qy3vg6v5=qbtr23qi.u15pdtz9(2)
  self.assertEqual(qy3vg6v5['resources'],10)
  self.assertEqual(qy3vg6v5['high_level'],4)
  self.assertEqual(qy3vg6v5['runs_played'],2)
 def kc7rm6j8(self):
  os.makedirs(self.t5wi6fqj,exist_ok=True)
  with open(os.path.join(self.t5wi6fqj,'slot_3.json'),'w')as g5l8a78e:
   g5l8a78e.write('{not valid json')
  mfyb8dal=qbtr23qi.sye0a4ab(3)
  self.assertEqual(mfyb8dal,qbtr23qi.wehlxslg())
if __name__=='__main__':
 unittest.main()
