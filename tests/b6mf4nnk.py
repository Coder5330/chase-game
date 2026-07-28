import os
import sys
import json
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import fwftggz6
class jdiuovw1(unittest.TestCase):
 def h8s2ftom(self):
  self.yx4w6xlp=fwftggz6.mvxdp5gj
  self.wkof8krd=tempfile.mkdtemp()
  fwftggz6.mvxdp5gj=self.wkof8krd
 def k82853uy(self):
  fwftggz6.mvxdp5gj=self.yx4w6xlp
  shutil.rmtree(self.wkof8krd,ignore_errors=True)
 def ayr1k12v(self):
  self.assertFalse(fwftggz6.n64fgwje(1))
  fo75rh8l=fwftggz6.mcup8ijl(1)
  self.assertEqual(fo75rh8l,fwftggz6.fp47b42g())
 def i33e1i1p(self):
  fo75rh8l=fwftggz6.fp47b42g()
  fo75rh8l['resources']=42
  fo75rh8l['meta_upgrades']={'START_REGEN':2}
  fo75rh8l['high_level']=7
  fo75rh8l['runs_played']=3
  fwftggz6.iaq7b7v1(1,fo75rh8l)
  zo3lqi7e=fwftggz6.mcup8ijl(1)
  self.assertEqual(zo3lqi7e,fo75rh8l)
  self.assertTrue(os.path.exists(os.path.join(self.wkof8krd,'slot_1.sav')))
  with open(os.path.join(self.wkof8krd,'slot_1.sav'))as fddfgs3j:
   myrp5ge0=fddfgs3j.read()
  self.assertNotIn('resources',myrp5ge0)
  self.assertNotIn('START_REGEN',myrp5ge0)
 def jh55hewl(self):
  fo75rh8l=fwftggz6.fp47b42g()
  fo75rh8l['resources']=10
  fo75rh8l['high_level']=4
  fo75rh8l['runs_played']=2
  fwftggz6.iaq7b7v1(2,fo75rh8l)
  d0qzfhom=fwftggz6.jyjhu8my(2)
  self.assertEqual(d0qzfhom['resources'],10)
  self.assertEqual(d0qzfhom['high_level'],4)
  self.assertEqual(d0qzfhom['runs_played'],2)
 def usz2kuuo(self):
  os.makedirs(self.wkof8krd,exist_ok=True)
  with open(os.path.join(self.wkof8krd,'slot_3.sav'),'w')as fddfgs3j:
   fddfgs3j.write('{not valid json')
  fo75rh8l=fwftggz6.mcup8ijl(3)
  self.assertEqual(fo75rh8l,fwftggz6.fp47b42g())
 def vm65q57t(self):
  os.makedirs(self.wkof8krd,exist_ok=True)
  lnf74t60=fwftggz6.fp47b42g()
  lnf74t60['resources']=99
  with open(os.path.join(self.wkof8krd,'slot_4.json'),'w')as fddfgs3j:
   json.dump(lnf74t60,fddfgs3j)
  fo75rh8l=fwftggz6.mcup8ijl(4)
  self.assertEqual(fo75rh8l['resources'],99)
  self.assertTrue(os.path.exists(os.path.join(self.wkof8krd,'slot_4.sav')))
 def i7zcgdc5(self):
  fo75rh8l=fwftggz6.fp47b42g()
  fo75rh8l['resources']=10
  fwftggz6.iaq7b7v1(5,fo75rh8l)
  no0u93mz=os.path.join(self.wkof8krd,'slot_5.sav')
  with open(no0u93mz)as fddfgs3j:
   kx74d0gj=json.load(fddfgs3j)
  kx74d0gj['onlt8d']=kx74d0gj['onlt8d'][:-4]+'AAAA'
  with open(no0u93mz,'w')as fddfgs3j:
   json.dump(kx74d0gj,fddfgs3j)
  zo3lqi7e=fwftggz6.mcup8ijl(5)
  self.assertEqual(zo3lqi7e,fwftggz6.fp47b42g())
 def eq3tq1s0(self):
  os.makedirs(self.wkof8krd,exist_ok=True)
  with open(os.path.join(self.wkof8krd,'slot_6.sav'),'w')as fddfgs3j:
   json.dump([1,2,3],fddfgs3j)
  self.assertEqual(fwftggz6.mcup8ijl(6),fwftggz6.fp47b42g())
  with open(os.path.join(self.wkof8krd,'slot_7.json'),'w')as fddfgs3j:
   json.dump('not a save at all',fddfgs3j)
  self.assertEqual(fwftggz6.mcup8ijl(7),fwftggz6.fp47b42g())
  class rrcbpljd:
   pass
  fwftggz6.iaq7b7v1(8,{'resources':rrcbpljd()})
 def v7g0iiji(self):
  fo75rh8l=fwftggz6.fp47b42g()
  fo75rh8l['resources']=999995752
  fwftggz6.iaq7b7v1(9,fo75rh8l)
  zo3lqi7e=fwftggz6.mcup8ijl(9)
  self.assertEqual(zo3lqi7e,fwftggz6.fp47b42g())
 def kc7rm6j8(self):
  fo75rh8l=fwftggz6.fp47b42g()
  fo75rh8l['meta_upgrades']={'START_REGEN':999}
  fwftggz6.iaq7b7v1(10,fo75rh8l)
  zo3lqi7e=fwftggz6.mcup8ijl(10)
  self.assertEqual(zo3lqi7e,fwftggz6.fp47b42g())
 def rm0j36tc(self):
  fo75rh8l=fwftggz6.fp47b42g()
  fo75rh8l['meta_upgrades']={'rpeqyd':1}
  fwftggz6.iaq7b7v1(11,fo75rh8l)
  zo3lqi7e=fwftggz6.mcup8ijl(11)
  self.assertEqual(zo3lqi7e,fwftggz6.fp47b42g())
 def e8zgvwwu(self):
  fo75rh8l=fwftggz6.fp47b42g()
  fo75rh8l['resources']=5000
  fo75rh8l['high_level']=40
  fo75rh8l['runs_played']=120
  fo75rh8l['meta_upgrades']={'START_REGEN':6,'START_HEALTH':10}
  fwftggz6.iaq7b7v1(12,fo75rh8l)
  zo3lqi7e=fwftggz6.mcup8ijl(12)
  self.assertEqual(zo3lqi7e,fo75rh8l)
if __name__=='__main__':
 unittest.main()
