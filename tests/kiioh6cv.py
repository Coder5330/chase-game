import os
import sys
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import e1gnfiue
class pecruyf3(unittest.TestCase):
 def uaobt328(self):
  self.win4olr6=e1gnfiue.ky20479t
  self.bwiykid9=tempfile.mkdtemp()
  e1gnfiue.ky20479t=self.bwiykid9
 def bf7so8w5(self):
  e1gnfiue.ky20479t=self.win4olr6
  shutil.rmtree(self.bwiykid9,ignore_errors=True)
 def n8sa3idy(self):
  self.assertFalse(e1gnfiue.gj29yfc2(1))
  do2m71hs=e1gnfiue.ub68rerv(1)
  self.assertEqual(do2m71hs,e1gnfiue.elwf90km())
 def kn5gjj8m(self):
  do2m71hs=e1gnfiue.elwf90km()
  do2m71hs['resources']=42
  do2m71hs['meta_upgrades']={'START_REGEN':2}
  do2m71hs['high_level']=7
  do2m71hs['runs_played']=3
  e1gnfiue.pllkstn3(1,do2m71hs)
  q5amln4p=e1gnfiue.ub68rerv(1)
  self.assertEqual(q5amln4p,do2m71hs)
  self.assertTrue(os.path.exists(os.path.join(self.bwiykid9,'slot_1.json')))
 def gf8f3gr9(self):
  do2m71hs=e1gnfiue.elwf90km()
  do2m71hs['resources']=10
  do2m71hs['high_level']=4
  do2m71hs['runs_played']=2
  e1gnfiue.pllkstn3(2,do2m71hs)
  ysqg8x80=e1gnfiue.xxns2zyb(2)
  self.assertEqual(ysqg8x80['resources'],10)
  self.assertEqual(ysqg8x80['high_level'],4)
  self.assertEqual(ysqg8x80['runs_played'],2)
 def d0qzfhom(self):
  os.makedirs(self.bwiykid9,exist_ok=True)
  with open(os.path.join(self.bwiykid9,'slot_3.json'),'w')as xuu13i59:
   xuu13i59.write('{not valid json')
  do2m71hs=e1gnfiue.ub68rerv(3)
  self.assertEqual(do2m71hs,e1gnfiue.elwf90km())
if __name__=='__main__':
 unittest.main()
