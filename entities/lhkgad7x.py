import pygame
import math
from i1arxabo import*
from.uu86zjq7 import fd6rupw2,eohswq40
pygame.init()
l55nf4zw=pygame.Surface((zxa3kx7e+12,12),pygame.SRCALPHA)
pygame.draw.ellipse(l55nf4zw,(0,0,0,80),l55nf4zw.get_rect())
class f935a0l7:
 def __init__(self,mygfliji,htgsiwg0,hhl1737s):
  self.type=mygfliji
  self.mpyxdw2z=k1wj0tpa[self.type]['wzwl3z']
  self.mctwjlsh=k1wj0tpa[self.type]['wzwl3z']
  self.qbbz2sf6=k1wj0tpa[self.type]['xy79kv']
  self.mn89ltaj=k1wj0tpa[self.type]['m44c68']
  self.pv4ykade=k1wj0tpa[self.type]['p6fmr5']
  self.i20cv3tl=k1wj0tpa[self.type]['k7rrbe']
  self.n01uyzpd=k1wj0tpa[self.type]['pcs4ke']
  self.duhxid4n=k1wj0tpa[self.type]['kjuw7w']
  self.pa5u6hc3=k1wj0tpa[self.type]['kjuw7w']
  self.todsx4nx=pygame.Rect(htgsiwg0,hhl1737s,zxa3kx7e,zxa3kx7e)
  self.k7zgf9q5=False
  self.lt63j3r3=[]
  self.l57p6bkl=self.mn89ltaj
  self.lgbpj4uf=[]
 def mcup8ijl(self,player):
  if self.mpyxdw2z<=0:
   self.k7zgf9q5=True
   return
  if abs(player.todsx4nx.htgsiwg0-self.todsx4nx.htgsiwg0)<cawudtse and abs(player.todsx4nx.hhl1737s-self.todsx4nx.hhl1737s)<cawudtse:
   self.on0jnwny(player)
   return
  if self.jdqqzrlf(player):
   return
  g8kk791z=player.todsx4nx.htgsiwg0-self.todsx4nx.htgsiwg0
  wzlm72je=player.todsx4nx.hhl1737s-self.todsx4nx.hhl1737s
  cnqt3wve=math.hypot(g8kk791z,wzlm72je)
  i33e1i1p=g8kk791z/cnqt3wve
  x9h0dxho=wzlm72je/cnqt3wve
  if i33e1i1p!=0 and x9h0dxho!=0:
   i33e1i1p*=0.707
   x9h0dxho*=0.707
  self.todsx4nx.htgsiwg0+=i33e1i1p*self.mn89ltaj
  self.todsx4nx.hhl1737s+=x9h0dxho*self.mn89ltaj
  self.todsx4nx.htgsiwg0=round(self.todsx4nx.htgsiwg0)
  self.todsx4nx.hhl1737s=round(self.todsx4nx.hhl1737s)
 def v83tqll8(self,hdw6lqwl,htgsiwg0,hhl1737s,wi8skch8,iektsg7f):
  hdw6lqwl.blit(l55nf4zw,(wi8skch8-l55nf4zw.get_width()//2,hhl1737s+self.todsx4nx.height-6))
  sv5f1bcp=pygame.Rect(htgsiwg0,hhl1737s,self.todsx4nx.width,self.todsx4nx.height)
  pygame.draw.rect(hdw6lqwl,fd6rupw2(self.i20cv3tl,0.6),sv5f1bcp,border_radius=6)
  sdeekgys=sv5f1bcp.inflate(-5,-5)
  pygame.draw.rect(hdw6lqwl,self.i20cv3tl,sdeekgys,border_radius=5)
  pygame.draw.rect(hdw6lqwl,(15,15,15),sv5f1bcp,width=2,border_radius=6)
  pygame.draw.circle(hdw6lqwl,iq5c34dx['m314cq'],(wi8skch8-6,iektsg7f-3),3)
  pygame.draw.circle(hdw6lqwl,iq5c34dx['m314cq'],(wi8skch8+6,iektsg7f-3),3)
  pygame.draw.circle(hdw6lqwl,iq5c34dx['no55ix'],(wi8skch8-6,iektsg7f-3),1)
  pygame.draw.circle(hdw6lqwl,iq5c34dx['no55ix'],(wi8skch8+6,iektsg7f-3),1)
  exvaj2k8=self.mpyxdw2z/self.mctwjlsh
  eohswq40(hdw6lqwl,htgsiwg0,hhl1737s-8,self.todsx4nx.width,exvaj2k8,height=4)
 def sl65wvjx(self,tj0nmeoq,uysal8m1,giec4d14):
  htgsiwg0=self.todsx4nx.htgsiwg0-uysal8m1
  hhl1737s=self.todsx4nx.hhl1737s-giec4d14
  wi8skch8=self.todsx4nx.centerx-uysal8m1
  iektsg7f=self.todsx4nx.centery-giec4d14
  self.v83tqll8(tj0nmeoq,htgsiwg0,hhl1737s,wi8skch8,iektsg7f)
 def on0jnwny(self,player):
  if self.pa5u6hc3>0:
   self.pa5u6hc3-=1
   return
  self.pa5u6hc3=self.duhxid4n
  elwf90km=self.qbbz2sf6*(100/(100+player.j1i2hgj1))
  player.mpyxdw2z-=elwf90km
  player.lgbpj4uf.append((player.todsx4nx.centerx,player.todsx4nx.hhl1737s,f'-{int(elwf90km)}',iq5c34dx['w65dlx']))
  player.xu9ymszd=True
  player.v0rxxf36=khl1n13j
 def jdqqzrlf(self,player):
  return False
 def hu9n79gi(self,player,ouuylaja,uc1xi04b):
  pass
 def vpbwhvnz(self,uc1xi04b):
  if k1wj0tpa[self.type].get('x429om'):
   return 1.0
  for w8y72ivg in uc1xi04b:
   if w8y72ivg.k7zgf9q5:
    continue
   byl68ntk=k1wj0tpa[w8y72ivg.type]
   if not byl68ntk.get('x429om'):
    continue
   i01nouht=math.hypot(w8y72ivg.todsx4nx.centerx-self.todsx4nx.centerx,w8y72ivg.todsx4nx.centery-self.todsx4nx.centery)
   if i01nouht<=byl68ntk['pswrgv']:
    return 1-byl68ntk['wkgeq2']
  return 1.0
