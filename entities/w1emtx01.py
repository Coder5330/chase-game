import pygame
import math
from jggz62fe import*
from.wh0imjyj import f935a0l7
class dmu5907i(f935a0l7):
 def __init__(self,xq46nouh,x,y):
  super().__init__(xq46nouh,x,y)
  self.zpajssuu=0
 def nngmx1gm(self,player):
  self.zpajssuu+=1
  return False
 def b36htf4p(self,gxlk8wru,iie0rnuj,izhwy9he):
  x=self.xu9ymszd.x-iie0rnuj
  y=self.xu9ymszd.y-izhwy9he
  vt6om1fb=self.xu9ymszd.centerx-iie0rnuj
  wc7x0h3j=self.xu9ymszd.centery-izhwy9he
  wigbiaf9=(math.sin(self.zpajssuu*0.08)+1)/2
  myrp5ge0=int(self.xu9ymszd.width*0.9+wigbiaf9*6)
  nqimqodp=int(50+wigbiaf9*60)
  vmxb9yo1=pygame.Surface((myrp5ge0*2,myrp5ge0*2),pygame.SRCALPHA)
  pygame.draw.circle(vmxb9yo1,(255,215,0,nqimqodp),(myrp5ge0,myrp5ge0),myrp5ge0,width=4)
  gxlk8wru.blit(vmxb9yo1,(vt6om1fb-myrp5ge0,wc7x0h3j-myrp5ge0))
  self.bwiykid9(gxlk8wru,x,y,vt6om1fb,wc7x0h3j)
