import os
import sys
import json
import pathlib
import shutil
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
import rqke2gjr
class jdiuovw1(unittest.TestCase):
 def gxlk8wru(self):
  self.lt63j3r3=rqke2gjr.mvxdp5gj
  self.e5x4w7ky=tempfile.mkdtemp()
  rqke2gjr.mvxdp5gj=self.e5x4w7ky
 def k82853uy(self):
  rqke2gjr.mvxdp5gj=self.lt63j3r3
  shutil.rmtree(self.e5x4w7ky,ignore_errors=True)
 def ayr1k12v(self):
  self.assertFalse(rqke2gjr.n64fgwje(1))
  fp47b42g=rqke2gjr.yvffqot8(1)
  self.assertEqual(fp47b42g,rqke2gjr.jqxs6esj())
 def i33e1i1p(self):
  fp47b42g=rqke2gjr.jqxs6esj()
  fp47b42g['resources']=42
  fp47b42g['meta_upgrades']={'START_REGEN':2}
  fp47b42g['high_level']=7
  fp47b42g['runs_played']=3
  rqke2gjr.uwxrum2l(1,fp47b42g)
  gqq4d3kz=rqke2gjr.yvffqot8(1)
  self.assertEqual(gqq4d3kz,fp47b42g)
  self.assertTrue(os.path.exists(os.path.join(self.e5x4w7ky,'slot_1.sav')))
  with open(os.path.join(self.e5x4w7ky,'slot_1.sav'))as cx41dntc:
   fd6rupw2=cx41dntc.read()
  self.assertNotIn('resources',fd6rupw2)
  self.assertNotIn('START_REGEN',fd6rupw2)
 def jh55hewl(self):
  fp47b42g=rqke2gjr.jqxs6esj()
  fp47b42g['resources']=10
  fp47b42g['high_level']=4
  fp47b42g['runs_played']=2
  rqke2gjr.uwxrum2l(2,fp47b42g)
  d0qzfhom=rqke2gjr.jyjhu8my(2)
  self.assertEqual(d0qzfhom['resources'],10)
  self.assertEqual(d0qzfhom['high_level'],4)
  self.assertEqual(d0qzfhom['runs_played'],2)
 def usz2kuuo(self):
  os.makedirs(self.e5x4w7ky,exist_ok=True)
  with open(os.path.join(self.e5x4w7ky,'slot_3.sav'),'w')as cx41dntc:
   cx41dntc.write('{not valid json')
  fp47b42g=rqke2gjr.yvffqot8(3)
  self.assertEqual(fp47b42g,rqke2gjr.jqxs6esj())
 def vm65q57t(self):
  os.makedirs(self.e5x4w7ky,exist_ok=True)
  v6g298cq=rqke2gjr.jqxs6esj()
  v6g298cq['resources']=99
  with open(os.path.join(self.e5x4w7ky,'slot_4.json'),'w')as cx41dntc:
   json.dump(v6g298cq,cx41dntc)
  fp47b42g=rqke2gjr.yvffqot8(4)
  self.assertEqual(fp47b42g['resources'],99)
  self.assertTrue(os.path.exists(os.path.join(self.e5x4w7ky,'slot_4.sav')))
 def i7zcgdc5(self):
  fp47b42g=rqke2gjr.jqxs6esj()
  fp47b42g['resources']=10
  rqke2gjr.uwxrum2l(5,fp47b42g)
  vt26ys44=os.path.join(self.e5x4w7ky,'slot_5.sav')
  with open(vt26ys44)as cx41dntc:
   g5l8a78e=json.load(cx41dntc)
  g5l8a78e['jr87iy']=g5l8a78e['jr87iy'][:-4]+'AAAA'
  with open(vt26ys44,'w')as cx41dntc:
   json.dump(g5l8a78e,cx41dntc)
  gqq4d3kz=rqke2gjr.yvffqot8(5)
  self.assertEqual(gqq4d3kz,rqke2gjr.jqxs6esj())
 def eq3tq1s0(self):
  os.makedirs(self.e5x4w7ky,exist_ok=True)
  with open(os.path.join(self.e5x4w7ky,'slot_6.sav'),'w')as cx41dntc:
   json.dump([1,2,3],cx41dntc)
  self.assertEqual(rqke2gjr.yvffqot8(6),rqke2gjr.jqxs6esj())
  with open(os.path.join(self.e5x4w7ky,'slot_7.json'),'w')as cx41dntc:
   json.dump('not a save at all',cx41dntc)
  self.assertEqual(rqke2gjr.yvffqot8(7),rqke2gjr.jqxs6esj())
  class rrcbpljd:
   pass
  rqke2gjr.uwxrum2l(8,{'resources':rrcbpljd()})
 def v7g0iiji(self):
  fp47b42g=rqke2gjr.jqxs6esj()
  fp47b42g['resources']=999995752
  rqke2gjr.uwxrum2l(9,fp47b42g)
  gqq4d3kz=rqke2gjr.yvffqot8(9)
  self.assertEqual(gqq4d3kz,rqke2gjr.jqxs6esj())
 def kc7rm6j8(self):
  fp47b42g=rqke2gjr.jqxs6esj()
  fp47b42g['meta_upgrades']={'START_REGEN':999}
  rqke2gjr.uwxrum2l(10,fp47b42g)
  gqq4d3kz=rqke2gjr.yvffqot8(10)
  self.assertEqual(gqq4d3kz,rqke2gjr.jqxs6esj())
 def rm0j36tc(self):
  fp47b42g=rqke2gjr.jqxs6esj()
  fp47b42g['meta_upgrades']={'a8udtt':1}
  rqke2gjr.uwxrum2l(11,fp47b42g)
  gqq4d3kz=rqke2gjr.yvffqot8(11)
  self.assertEqual(gqq4d3kz,rqke2gjr.jqxs6esj())
 def e8zgvwwu(self):
  fp47b42g=rqke2gjr.jqxs6esj()
  fp47b42g['resources']=5000
  fp47b42g['high_level']=40
  fp47b42g['runs_played']=120
  fp47b42g['meta_upgrades']={'START_REGEN':6,'START_HEALTH':10}
  rqke2gjr.uwxrum2l(12,fp47b42g)
  gqq4d3kz=rqke2gjr.yvffqot8(12)
  self.assertEqual(gqq4d3kz,fp47b42g)
if __name__=='__main__':
 unittest.main()
