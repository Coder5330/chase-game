import os
import sys
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import l3jzr25m
class gdzr1yxr(unittest.TestCase):
 def xasez2nx(self):
  self.cqoldfor=l3jzr25m.rcfnfhol
  self.wrbw2zla=tempfile.mkdtemp()
  l3jzr25m.rcfnfhol=self.wrbw2zla
 def z5x8a5fb(self):
  l3jzr25m.rcfnfhol=self.cqoldfor
  shutil.rmtree(self.wrbw2zla,ignore_errors=True)
 def nv23gxj0(self):
  self.assertFalse(l3jzr25m.xu9ymszd(1))
  wi8skch8=l3jzr25m.v3e1ocjx(1)
  self.assertEqual(wi8skch8,l3jzr25m.vw6m7b5c())
 def kodpvjtu(self):
  wi8skch8=l3jzr25m.vw6m7b5c()
  wi8skch8['resources']=42
  wi8skch8['meta_upgrades']={'START_REGEN':2}
  wi8skch8['high_level']=7
  wi8skch8['runs_played']=3
  l3jzr25m.xsspye9r(1,wi8skch8)
  w5iz31yr=l3jzr25m.v3e1ocjx(1)
  self.assertEqual(w5iz31yr,wi8skch8)
  self.assertTrue(os.path.exists(os.path.join(self.wrbw2zla,'slot_1.json')))
 def d0qzfhom(self):
  wi8skch8=l3jzr25m.vw6m7b5c()
  wi8skch8['resources']=10
  wi8skch8['high_level']=4
  wi8skch8['runs_played']=2
  l3jzr25m.xsspye9r(2,wi8skch8)
  q3n2qb6g=l3jzr25m.tbxf445c(2)
  self.assertEqual(q3n2qb6g['resources'],10)
  self.assertEqual(q3n2qb6g['high_level'],4)
  self.assertEqual(q3n2qb6g['runs_played'],2)
 def ysqg8x80(self):
  os.makedirs(self.wrbw2zla,exist_ok=True)
  with open(os.path.join(self.wrbw2zla,'slot_3.json'),'w')as tnz61231:
   tnz61231.write('{not valid json')
  wi8skch8=l3jzr25m.v3e1ocjx(3)
  self.assertEqual(wi8skch8,l3jzr25m.vw6m7b5c())
if __name__=='__main__':
 unittest.main()
