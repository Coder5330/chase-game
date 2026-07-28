import os
import sys
import json
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import jrk79ufu
class mqp49kwv(unittest.TestCase):
 def qcd81twh(self):
  self.diuu9k9x=jrk79ufu.khl1n13j
  self.v982n2at=tempfile.mkdtemp()
  jrk79ufu.khl1n13j=self.v982n2at
 def a1tbrwr9(self):
  jrk79ufu.khl1n13j=self.diuu9k9x
  shutil.rmtree(self.v982n2at,ignore_errors=True)
 def jdqqzrlf(self):
  self.assertFalse(jrk79ufu.w0p4e05q(1))
  uc1xi04b=jrk79ufu.tb4ldims(1)
  self.assertEqual(uc1xi04b,jrk79ufu.x875aud9())
 def f2voi8uy(self):
  uc1xi04b=jrk79ufu.x875aud9()
  uc1xi04b['resources']=42
  uc1xi04b['meta_upgrades']={'START_REGEN':2}
  uc1xi04b['high_level']=7
  uc1xi04b['runs_played']=3
  jrk79ufu.byl68ntk(1,uc1xi04b)
  vk3g84ut=jrk79ufu.tb4ldims(1)
  self.assertEqual(vk3g84ut,uc1xi04b)
  self.assertTrue(os.path.exists(os.path.join(self.v982n2at,'slot_1.sav')))
  with open(os.path.join(self.v982n2at,'slot_1.sav'))as cx41dntc:
   tbxf445c=cx41dntc.read()
  self.assertNotIn('resources',tbxf445c)
  self.assertNotIn('START_REGEN',tbxf445c)
 def r212pgym(self):
  uc1xi04b=jrk79ufu.x875aud9()
  uc1xi04b['resources']=10
  uc1xi04b['high_level']=4
  uc1xi04b['runs_played']=2
  jrk79ufu.byl68ntk(2,uc1xi04b)
  rk36m8jv=jrk79ufu.rh0w064w(2)
  self.assertEqual(rk36m8jv['resources'],10)
  self.assertEqual(rk36m8jv['high_level'],4)
  self.assertEqual(rk36m8jv['runs_played'],2)
 def z7pwo6cm(self):
  os.makedirs(self.v982n2at,exist_ok=True)
  with open(os.path.join(self.v982n2at,'slot_3.sav'),'w')as cx41dntc:
   cx41dntc.write('{not valid json')
  uc1xi04b=jrk79ufu.tb4ldims(3)
  self.assertEqual(uc1xi04b,jrk79ufu.x875aud9())
 def zanouof0(self):
  os.makedirs(self.v982n2at,exist_ok=True)
  v6g298cq=jrk79ufu.x875aud9()
  v6g298cq['resources']=99
  with open(os.path.join(self.v982n2at,'slot_4.json'),'w')as cx41dntc:
   json.dump(v6g298cq,cx41dntc)
  uc1xi04b=jrk79ufu.tb4ldims(4)
  self.assertEqual(uc1xi04b['resources'],99)
  self.assertTrue(os.path.exists(os.path.join(self.v982n2at,'slot_4.sav')))
 def qxt6ridl(self):
  uc1xi04b=jrk79ufu.x875aud9()
  uc1xi04b['resources']=10
  jrk79ufu.byl68ntk(5,uc1xi04b)
  cqheyto5=os.path.join(self.v982n2at,'slot_5.sav')
  with open(cqheyto5)as cx41dntc:
   g5l8a78e=json.load(cx41dntc)
  g5l8a78e['gbwcv6']=g5l8a78e['gbwcv6'][:-4]+'AAAA'
  with open(cqheyto5,'w')as cx41dntc:
   json.dump(g5l8a78e,cx41dntc)
  vk3g84ut=jrk79ufu.tb4ldims(5)
  self.assertEqual(vk3g84ut,jrk79ufu.x875aud9())
 def qxb7gbdg(self):
  os.makedirs(self.v982n2at,exist_ok=True)
  with open(os.path.join(self.v982n2at,'slot_6.sav'),'w')as cx41dntc:
   json.dump([1,2,3],cx41dntc)
  self.assertEqual(jrk79ufu.tb4ldims(6),jrk79ufu.x875aud9())
  with open(os.path.join(self.v982n2at,'slot_7.json'),'w')as cx41dntc:
   json.dump('not a save at all',cx41dntc)
  self.assertEqual(jrk79ufu.tb4ldims(7),jrk79ufu.x875aud9())
  class v4u89yjb:
   pass
  jrk79ufu.byl68ntk(8,{'resources':v4u89yjb()})
if __name__=='__main__':
 unittest.main()
