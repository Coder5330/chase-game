import os
import sys
import json
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import ruhywm7s
class jdiuovw1(unittest.TestCase):
 def xxns2zyb(self):
  self.sk8yqk94=ruhywm7s.mvxdp5gj
  self.x52qc1iy=tempfile.mkdtemp()
  ruhywm7s.mvxdp5gj=self.x52qc1iy
 def p7pchcbn(self):
  ruhywm7s.mvxdp5gj=self.sk8yqk94
  shutil.rmtree(self.x52qc1iy,ignore_errors=True)
 def z7pwo6cm(self):
  self.assertFalse(ruhywm7s.cb2uuijn(1))
  vt6om1fb=ruhywm7s.xwqvr1h6(1)
  self.assertEqual(vt6om1fb,ruhywm7s.rzewviyt())
 def qxt6ridl(self):
  vt6om1fb=ruhywm7s.rzewviyt()
  vt6om1fb['resources']=42
  vt6om1fb['meta_upgrades']={'START_REGEN':2}
  vt6om1fb['high_level']=7
  vt6om1fb['runs_played']=3
  ruhywm7s.gj29yfc2(1,vt6om1fb)
  y2f7atwy=ruhywm7s.xwqvr1h6(1)
  self.assertEqual(y2f7atwy,vt6om1fb)
  self.assertTrue(os.path.exists(os.path.join(self.x52qc1iy,'slot_1.sav')))
  with open(os.path.join(self.x52qc1iy,'slot_1.sav'))as r98s4c3b:
   hay64yfd=r98s4c3b.read()
  self.assertNotIn('resources',hay64yfd)
  self.assertNotIn('START_REGEN',hay64yfd)
 def zanouof0(self):
  vt6om1fb=ruhywm7s.rzewviyt()
  vt6om1fb['resources']=10
  vt6om1fb['high_level']=4
  vt6om1fb['runs_played']=2
  ruhywm7s.gj29yfc2(2,vt6om1fb)
  yypp5zp7=ruhywm7s.xvzc7d2k(2)
  self.assertEqual(yypp5zp7['resources'],10)
  self.assertEqual(yypp5zp7['high_level'],4)
  self.assertEqual(yypp5zp7['runs_played'],2)
 def h4m2ec8r(self):
  os.makedirs(self.x52qc1iy,exist_ok=True)
  with open(os.path.join(self.x52qc1iy,'slot_3.sav'),'w')as r98s4c3b:
   r98s4c3b.write('{not valid json')
  vt6om1fb=ruhywm7s.xwqvr1h6(3)
  self.assertEqual(vt6om1fb,ruhywm7s.rzewviyt())
 def lu7jae58(self):
  os.makedirs(self.x52qc1iy,exist_ok=True)
  jxxgaear=ruhywm7s.rzewviyt()
  jxxgaear['resources']=99
  with open(os.path.join(self.x52qc1iy,'slot_4.json'),'w')as r98s4c3b:
   json.dump(jxxgaear,r98s4c3b)
  vt6om1fb=ruhywm7s.xwqvr1h6(4)
  self.assertEqual(vt6om1fb['resources'],99)
  self.assertTrue(os.path.exists(os.path.join(self.x52qc1iy,'slot_4.sav')))
 def gf8f3gr9(self):
  vt6om1fb=ruhywm7s.rzewviyt()
  vt6om1fb['resources']=10
  ruhywm7s.gj29yfc2(5,vt6om1fb)
  uj64qhks=os.path.join(self.x52qc1iy,'slot_5.sav')
  with open(uj64qhks)as r98s4c3b:
   qhkc856w=json.load(r98s4c3b)
  qhkc856w['e0s41k']=qhkc856w['e0s41k'][:-4]+'AAAA'
  with open(uj64qhks,'w')as r98s4c3b:
   json.dump(qhkc856w,r98s4c3b)
  y2f7atwy=ruhywm7s.xwqvr1h6(5)
  self.assertEqual(y2f7atwy,ruhywm7s.rzewviyt())
 def kc1fjotg(self):
  os.makedirs(self.x52qc1iy,exist_ok=True)
  with open(os.path.join(self.x52qc1iy,'slot_6.sav'),'w')as r98s4c3b:
   json.dump([1,2,3],r98s4c3b)
  self.assertEqual(ruhywm7s.xwqvr1h6(6),ruhywm7s.rzewviyt())
  with open(os.path.join(self.x52qc1iy,'slot_7.json'),'w')as r98s4c3b:
   json.dump('not a save at all',r98s4c3b)
  self.assertEqual(ruhywm7s.xwqvr1h6(7),ruhywm7s.rzewviyt())
  class rrcbpljd:
   pass
  ruhywm7s.gj29yfc2(8,{'resources':rrcbpljd()})
if __name__=='__main__':
 unittest.main()
