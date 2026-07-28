import pygame
import math
from vnbnqbnx import*
from.s84d4r9v import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,nfn1r4kz,iimoe0sy,gdg1wjui):
  super().__init__(nfn1r4kz,iimoe0sy,gdg1wjui)
  self.kkzruin3=0
 def mabkae6a(self,player):
  self.kkzruin3+=1
  return False
 def sygvwopl(self,g1b3d505,xp8mgyn2,i20cv3tl):
  iimoe0sy=self.bdgbk2l0.iimoe0sy-xp8mgyn2
  gdg1wjui=self.bdgbk2l0.gdg1wjui-i20cv3tl
  yuibrsz1=self.bdgbk2l0.centerx-xp8mgyn2
  mfyb8dal=self.bdgbk2l0.centery-i20cv3tl
  kodpvjtu=(math.sin(self.kkzruin3*0.08)+1)/2
  xwk2rv23=int(self.bdgbk2l0.width*0.9+kodpvjtu*6)
  i4fejgxa=int(50+kodpvjtu*60)
  u9el8hl8=pygame.Surface((xwk2rv23*2,xwk2rv23*2),pygame.SRCALPHA)
  pygame.draw.circle(u9el8hl8,(255,215,0,i4fejgxa),(xwk2rv23,xwk2rv23),xwk2rv23,width=4)
  g1b3d505.blit(u9el8hl8,(yuibrsz1-xwk2rv23,mfyb8dal-xwk2rv23))
  self.eqrl1n75(g1b3d505,iimoe0sy,gdg1wjui,yuibrsz1,mfyb8dal)
