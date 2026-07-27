import pygame
import math
from en1x2gdg import*
from.um4vxjj2 import qc06xq9j,qtzk3ny9
pygame.init()
n2vlpys2=pygame.Surface((z0xkxwd8+16,14),pygame.SRCALPHA)
pygame.draw.ellipse(n2vlpys2,(0,0,0,90),n2vlpys2.get_rect())
class rqf5q14j:
 def __init__(self,meta_upgrades=None):
  meta_upgrades=meta_upgrades or{}
  jxxgaear=meta_upgrades.get('START_HEALTH',0)
  sye0a4ab=meta_upgrades.get('START_SPEED',0)
  zflv1xxl=meta_upgrades.get('START_DAMAGE',0)
  b78okz1p=meta_upgrades.get('START_COOLDOWN',0)
  ry181acj=meta_upgrades.get('START_ARMOR',0)
  crsb4gf1=meta_upgrades.get('START_REGEN',0)
  self.tp2ex5t5=hyihair4*lnf74t60(sye0a4ab)
  self.kz1uu7zy=self.tp2ex5t5
  self.f8rtm4j3=pygame.Rect((faqvkizz-z0xkxwd8)//2,(xd1wjcit-z0xkxwd8)//2,z0xkxwd8,z0xkxwd8)
  self.ugez7bh2=iq5c34dx['xj2dg1']
  self.b06xkxb9=int(1000*ls2zge2j(jxxgaear))
  self.ub68rerv=self.b06xkxb9
  self.sf337kuu=self.b06xkxb9
  self.bu4xszjn=0
  self.wvpw232u=1
  self.ayr1k12v=False
  self.ftrflqbm={'lcf4mn':0,'r4uov5':self.kz1uu7zy}
  self.ejbzutru={}
  self.m3hcws2w={key:0 for key in cq5uznof}
  self.i4fejgxa=n04cdpqv(zflv1xxl)
  self.ytv3i12v=mctwjlsh(b78okz1p)
  self.lcj883dh=q5amln4p(ry181acj)
  self.ejwtl9tq=d1b3jczu(crsb4gf1)
  self.ep6beffl=self.i4fejgxa
  self.i20cv3tl=self.ytv3i12v
  self.ucu7onz3=1.0
  self.iy6qktc8=self.lcj883dh
  self.cknfu84x=self.ejwtl9tq
  self.vhxs58yr=pi3qk2ia
  self.tj0nmeoq=False
  self.myrp5ge0=0
  self.wb7f6fdh=[]
 def jmpioygg(self,key):
  self.m3hcws2w[key]+=1
  fpa8hyex=self.m3hcws2w[key]
  if key=='n8k03w':
   tb4ldims=int(self.b06xkxb9*(1+0.2*fpa8hyex))
   self.sf337kuu+=tb4ldims-self.ub68rerv
   self.ub68rerv=tb4ldims
  elif key=='wtolaq':
   self.kz1uu7zy=self.tp2ex5t5*(1+0.08*fpa8hyex)
  elif key=='dq3b9s':
   self.cknfu84x=self.ejwtl9tq+fpa8hyex
  elif key=='sfshb0':
   self.ep6beffl=self.i4fejgxa*(1+0.06*fpa8hyex)
  elif key=='mcc1m3':
   self.i20cv3tl=self.ytv3i12v*max(0.6,1-0.05*fpa8hyex)
  elif key=='o76t94':
   self.iy6qktc8=self.lcj883dh+fpa8hyex*5
  elif key=='pqpva5':
   self.ucu7onz3=1+0.15*fpa8hyex
 def v3e1ocjx(self,wvndfdw7):
  self.ejbzutru[wvndfdw7]=self.ejbzutru.get(wvndfdw7,1)+1
 def y2f7atwy(self):
  semqgy27=pygame.key.get_pressed()
  mfyb8dal=eohswq40=0
  if semqgy27[pygame.K_UP]:
   eohswq40-=self.kz1uu7zy
  if semqgy27[pygame.K_DOWN]:
   eohswq40+=self.kz1uu7zy
  if semqgy27[pygame.K_LEFT]:
   mfyb8dal-=self.kz1uu7zy
  if semqgy27[pygame.K_RIGHT]:
   mfyb8dal+=self.kz1uu7zy
  if mfyb8dal!=0 and eohswq40!=0:
   mfyb8dal*=0.707
   eohswq40*=0.707
  if mfyb8dal!=0 or eohswq40!=0:
   self.ftrflqbm['lcf4mn']=mfyb8dal
   self.ftrflqbm['r4uov5']=eohswq40
  self.f8rtm4j3.qxb7gbdg+=mfyb8dal
  self.f8rtm4j3.n01uyzpd+=eohswq40
  self.f8rtm4j3.qxb7gbdg=max(min(self.f8rtm4j3.qxb7gbdg,faqvkizz-self.f8rtm4j3.width),0)
  self.f8rtm4j3.n01uyzpd=max(min(self.f8rtm4j3.n01uyzpd,xd1wjcit-self.f8rtm4j3.height),0)
  if self.cknfu84x>0 and self.sf337kuu<self.ub68rerv:
   self.vhxs58yr-=1
   if self.vhxs58yr<=0:
    self.vhxs58yr=pi3qk2ia
    self.sf337kuu=min(self.ub68rerv,self.sf337kuu+self.cknfu84x)
  if self.bu4xszjn>=ocij2v2h[min(self.wvpw232u,len(ocij2v2h)-1)]:
   self.ayr1k12v=True
   self.bu4xszjn=0
   self.wvpw232u+=1
 def do2m71hs(self,gmoft6yr,kybwmlun,i0x65muf):
  qxb7gbdg=self.f8rtm4j3.qxb7gbdg-kybwmlun
  n01uyzpd=self.f8rtm4j3.n01uyzpd-i0x65muf
  ruq9e5co=self.f8rtm4j3.centerx-kybwmlun
  wzs13c9x=self.f8rtm4j3.centery-i0x65muf
  gmoft6yr.blit(n2vlpys2,(ruq9e5co-n2vlpys2.get_width()//2,n01uyzpd+self.f8rtm4j3.height-8))
  ykipu1wy=pygame.Rect(qxb7gbdg,n01uyzpd,self.f8rtm4j3.width,self.f8rtm4j3.height)
  pygame.draw.rect(gmoft6yr,qc06xq9j(self.ugez7bh2,0.55),ykipu1wy,border_radius=10)
  vpbwhvnz=ykipu1wy.inflate(-5,-5)
  pygame.draw.rect(gmoft6yr,self.ugez7bh2,vpbwhvnz,border_radius=8)
  mpyxdw2z=pygame.Rect(vpbwhvnz.qxb7gbdg+3,vpbwhvnz.n01uyzpd+3,vpbwhvnz.width//2,vpbwhvnz.height//3)
  pygame.draw.rect(gmoft6yr,qc06xq9j(self.ugez7bh2,2.0),mpyxdw2z,border_radius=4)
  pygame.draw.rect(gmoft6yr,(15,15,30),ykipu1wy,width=2,border_radius=10)
  cp91i3vm=math.hypot(self.ftrflqbm['lcf4mn'],self.ftrflqbm['r4uov5'])or 1
  (mcup8ijl,zo3lqi7e)=(self.ftrflqbm['lcf4mn']/cp91i3vm,self.ftrflqbm['r4uov5']/cp91i3vm)
  s5r96khu=(ruq9e5co+mcup8ijl*20,wzs13c9x+zo3lqi7e*20)
  rk2u1rsu=(ruq9e5co-zo3lqi7e*7+mcup8ijl*4,wzs13c9x+mcup8ijl*7+zo3lqi7e*4)
  ljk4q5v7=(ruq9e5co+zo3lqi7e*7+mcup8ijl*4,wzs13c9x-mcup8ijl*7+zo3lqi7e*4)
  pygame.draw.polygon(gmoft6yr,iq5c34dx['pta5iv'],[s5r96khu,rk2u1rsu,ljk4q5v7])
  pygame.draw.polygon(gmoft6yr,(15,15,30),[s5r96khu,rk2u1rsu,ljk4q5v7],width=1)
  g5hcbbmh=self.sf337kuu/self.ub68rerv
  qtzk3ny9(gmoft6yr,qxb7gbdg,n01uyzpd-10,self.f8rtm4j3.width,g5hcbbmh,height=6)
