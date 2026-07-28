import os
import sys
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import gjg2y8rg
class jdiuovw1(unittest.TestCase):
 def nbwye6qv(self):
  self.sld4d6af=gjg2y8rg.mvxdp5gj
  self.jmpioygg=tempfile.mkdtemp()
  gjg2y8rg.mvxdp5gj=self.jmpioygg
 def yypp5zp7(self):
  gjg2y8rg.mvxdp5gj=self.sld4d6af
  shutil.rmtree(self.jmpioygg,ignore_errors=True)
 def bsp7bm41(self):
  self.assertFalse(gjg2y8rg.f80ebkjf(1))
  qtzk3ny9=gjg2y8rg.zflv1xxl(1)
  self.assertEqual(qtzk3ny9,gjg2y8rg.yuibrsz1())
 def lu7jae58(self):
  qtzk3ny9=gjg2y8rg.yuibrsz1()
  qtzk3ny9['resources']=42
  qtzk3ny9['meta_upgrades']={'START_REGEN':2}
  qtzk3ny9['high_level']=7
  qtzk3ny9['runs_played']=3
  gjg2y8rg.wd6r30oj(1,qtzk3ny9)
  n04cdpqv=gjg2y8rg.zflv1xxl(1)
  self.assertEqual(n04cdpqv,qtzk3ny9)
  self.assertTrue(os.path.exists(os.path.join(self.jmpioygg,'slot_1.json')))
 def z7pwo6cm(self):
  qtzk3ny9=gjg2y8rg.yuibrsz1()
  qtzk3ny9['resources']=10
  qtzk3ny9['high_level']=4
  qtzk3ny9['runs_played']=2
  gjg2y8rg.wd6r30oj(2,qtzk3ny9)
  hcxhgnze=gjg2y8rg.uwxrum2l(2)
  self.assertEqual(hcxhgnze['resources'],10)
  self.assertEqual(hcxhgnze['high_level'],4)
  self.assertEqual(hcxhgnze['runs_played'],2)
 def yoyohaz7(self):
  os.makedirs(self.jmpioygg,exist_ok=True)
  with open(os.path.join(self.jmpioygg,'slot_3.json'),'w')as nfn1r4kz:
   nfn1r4kz.write('{not valid json')
  qtzk3ny9=gjg2y8rg.zflv1xxl(3)
  self.assertEqual(qtzk3ny9,gjg2y8rg.yuibrsz1())
if __name__=='__main__':
 unittest.main()
