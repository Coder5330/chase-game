import os
import sys
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import nhx6zdcu
class azebbk7w(unittest.TestCase):
 def myrp5ge0(self):
  self.nd96qe3r=nhx6zdcu.ky20479t
  self.eqrl1n75=tempfile.mkdtemp()
  nhx6zdcu.ky20479t=self.eqrl1n75
 def qdnai89y(self):
  nhx6zdcu.ky20479t=self.nd96qe3r
  shutil.rmtree(self.eqrl1n75,ignore_errors=True)
 def p7pchcbn(self):
  self.assertFalse(nhx6zdcu.nbwye6qv(1))
  hfb85p86=nhx6zdcu.bokzixza(1)
  self.assertEqual(hfb85p86,nhx6zdcu.pa8s8hmb())
 def mu118qqv(self):
  hfb85p86=nhx6zdcu.pa8s8hmb()
  hfb85p86['resources']=42
  hfb85p86['meta_upgrades']={'START_REGEN':2}
  hfb85p86['high_level']=7
  hfb85p86['runs_played']=3
  nhx6zdcu.d46aexl6(1,hfb85p86)
  pcvsqame=nhx6zdcu.bokzixza(1)
  self.assertEqual(pcvsqame,hfb85p86)
  self.assertTrue(os.path.exists(os.path.join(self.eqrl1n75,'slot_1.json')))
 def kc7rm6j8(self):
  hfb85p86=nhx6zdcu.pa8s8hmb()
  hfb85p86['resources']=10
  hfb85p86['high_level']=4
  hfb85p86['runs_played']=2
  nhx6zdcu.d46aexl6(2,hfb85p86)
  v24479qt=nhx6zdcu.q26yg3dx(2)
  self.assertEqual(v24479qt['resources'],10)
  self.assertEqual(v24479qt['high_level'],4)
  self.assertEqual(v24479qt['runs_played'],2)
 def k7vcneas(self):
  os.makedirs(self.eqrl1n75,exist_ok=True)
  with open(os.path.join(self.eqrl1n75,'slot_3.json'),'w')as mq7nc85e:
   mq7nc85e.write('{not valid json')
  hfb85p86=nhx6zdcu.bokzixza(3)
  self.assertEqual(hfb85p86,nhx6zdcu.pa8s8hmb())
if __name__=='__main__':
 unittest.main()
