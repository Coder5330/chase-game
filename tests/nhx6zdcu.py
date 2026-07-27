import os
import sys
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import nvxjj2jv
class zakoixnt(unittest.TestCase):
 def nxxjve3d(self):
  self.v83tqll8=nvxjj2jv.rcfnfhol
  self.nd96qe3r=tempfile.mkdtemp()
  nvxjj2jv.rcfnfhol=self.nd96qe3r
 def v24479qt(self):
  nvxjj2jv.rcfnfhol=self.v83tqll8
  shutil.rmtree(self.nd96qe3r,ignore_errors=True)
 def yypp5zp7(self):
  self.assertFalse(nvxjj2jv.pllkstn3(1))
  iektsg7f=nvxjj2jv.xk7n8la1(1)
  self.assertEqual(iektsg7f,nvxjj2jv.u1jhuwb6())
 def rwybow23(self):
  iektsg7f=nvxjj2jv.u1jhuwb6()
  iektsg7f['resources']=42
  iektsg7f['meta_upgrades']={'START_REGEN':2}
  iektsg7f['high_level']=7
  iektsg7f['runs_played']=3
  nvxjj2jv.ytb9xxay(1,iektsg7f)
  xd8wz42o=nvxjj2jv.xk7n8la1(1)
  self.assertEqual(xd8wz42o,iektsg7f)
  self.assertTrue(os.path.exists(os.path.join(self.nd96qe3r,'slot_1.json')))
 def oa47sh2s(self):
  iektsg7f=nvxjj2jv.u1jhuwb6()
  iektsg7f['resources']=10
  iektsg7f['high_level']=4
  iektsg7f['runs_played']=2
  nvxjj2jv.ytb9xxay(2,iektsg7f)
  yp3cyazb=nvxjj2jv.uaobt328(2)
  self.assertEqual(yp3cyazb['resources'],10)
  self.assertEqual(yp3cyazb['high_level'],4)
  self.assertEqual(yp3cyazb['runs_played'],2)
 def w8wj0uun(self):
  os.makedirs(self.nd96qe3r,exist_ok=True)
  with open(os.path.join(self.nd96qe3r,'slot_3.json'),'w')as v15cqzcu:
   v15cqzcu.write('{not valid json')
  iektsg7f=nvxjj2jv.xk7n8la1(3)
  self.assertEqual(iektsg7f,nvxjj2jv.u1jhuwb6())
if __name__=='__main__':
 unittest.main()
