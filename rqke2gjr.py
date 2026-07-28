import pygame
from e87f8tsx import*
from entities import qcd81twh
from cnqs3qt3 import oohp6vz4,hc58drc1
class zbqe7ckw:
 def __init__(self):
  self.pllkstn3=pygame.Rect(ygspk9p3//2-rqf5q14j//2,tp0lvsnu-90,rqf5q14j,rqf5q14j)
  self.hcxhgnze=yswjckjl
  self.hfb85p86=iq5c34dx['kqbrmq']
  self.ls2zge2j={'gbwcv6':0,'g8wze4':-1}
 def wb7f6fdh(self):
  b78okz1p=pygame.key.get_pressed()
  pbo119xp=mq7nc85e=0
  if b78okz1p[pygame.K_UP]:
   mq7nc85e-=self.hcxhgnze
  if b78okz1p[pygame.K_DOWN]:
   mq7nc85e+=self.hcxhgnze
  if b78okz1p[pygame.K_LEFT]:
   pbo119xp-=self.hcxhgnze
  if b78okz1p[pygame.K_RIGHT]:
   pbo119xp+=self.hcxhgnze
  if pbo119xp!=0 and mq7nc85e!=0:
   pbo119xp*=0.707
   mq7nc85e*=0.707
  if pbo119xp!=0 or mq7nc85e!=0:
   self.ls2zge2j['gbwcv6']=pbo119xp
   self.ls2zge2j['g8wze4']=mq7nc85e
  self.pllkstn3.j1kfk7y6+=pbo119xp
  self.pllkstn3.f1bl08kg+=mq7nc85e
  self.pllkstn3.j1kfk7y6=max(0,min(self.pllkstn3.j1kfk7y6,ygspk9p3-self.pllkstn3.width))
  self.pllkstn3.f1bl08kg=max(60,min(self.pllkstn3.f1bl08kg,tp0lvsnu-self.pllkstn3.height))
 def dw7nh8rq(self,byl68ntk):
  (j1kfk7y6,f1bl08kg)=(self.pllkstn3.j1kfk7y6,self.pllkstn3.f1bl08kg)
  (rmm1zxyv,g8kk791z)=(self.pllkstn3.centerx,self.pllkstn3.centery)
  u15pdtz9=pygame.Surface((self.pllkstn3.width+14,12),pygame.SRCALPHA)
  pygame.draw.ellipse(u15pdtz9,(0,0,0,80),u15pdtz9.get_rect())
  byl68ntk.blit(u15pdtz9,(rmm1zxyv-u15pdtz9.get_width()//2,f1bl08kg+self.pllkstn3.height-6))
  u23y30ys=pygame.Rect(j1kfk7y6,f1bl08kg,self.pllkstn3.width,self.pllkstn3.height)
  pygame.draw.rect(byl68ntk,qcd81twh(self.hfb85p86,0.55),u23y30ys,border_radius=10)
  k2ixivzk=u23y30ys.inflate(-5,-5)
  pygame.draw.rect(byl68ntk,self.hfb85p86,k2ixivzk,border_radius=8)
  rk2u1rsu=pygame.Rect(k2ixivzk.j1kfk7y6+3,k2ixivzk.f1bl08kg+3,k2ixivzk.width//2,k2ixivzk.height//3)
  pygame.draw.rect(byl68ntk,qcd81twh(self.hfb85p86,2.0),rk2u1rsu,border_radius=4)
  pygame.draw.rect(byl68ntk,(15,15,30),u23y30ys,width=2,border_radius=10)
class my6wktak:
 def __init__(self,trdhw9re,x5m9j98c,color,j1kfk7y6,f1bl08kg):
  self.trdhw9re=trdhw9re
  self.x5m9j98c=x5m9j98c
  self.hfb85p86=color
  self.pllkstn3=pygame.Rect(j1kfk7y6,f1bl08kg,34,34)
  self.q5amln4p=False
 def dw7nh8rq(self,byl68ntk,m8lw2qit):
  u15pdtz9=pygame.Surface((self.pllkstn3.width+10,10),pygame.SRCALPHA)
  pygame.draw.ellipse(u15pdtz9,(0,0,0,70),u15pdtz9.get_rect())
  byl68ntk.blit(u15pdtz9,(self.pllkstn3.centerx-u15pdtz9.get_width()//2,self.pllkstn3.bottom-4))
  u23y30ys=pygame.Rect(self.pllkstn3.j1kfk7y6,self.pllkstn3.f1bl08kg,self.pllkstn3.width,self.pllkstn3.height)
  pygame.draw.rect(byl68ntk,qcd81twh(self.hfb85p86,0.6),u23y30ys,border_radius=8)
  k2ixivzk=u23y30ys.inflate(-5,-5)
  pygame.draw.rect(byl68ntk,self.hfb85p86,k2ixivzk,border_radius=6)
  pygame.draw.rect(byl68ntk,(15,15,15),u23y30ys,width=2,border_radius=8)
  (rmm1zxyv,g8kk791z)=(self.pllkstn3.centerx,self.pllkstn3.centery)
  pygame.draw.circle(byl68ntk,iq5c34dx['hzj7ub'],(rmm1zxyv-6,g8kk791z-3),3)
  pygame.draw.circle(byl68ntk,iq5c34dx['hzj7ub'],(rmm1zxyv+6,g8kk791z-3),3)
  pygame.draw.circle(byl68ntk,iq5c34dx['k7bpgy'],(rmm1zxyv-6,g8kk791z-3),1)
  pygame.draw.circle(byl68ntk,iq5c34dx['k7bpgy'],(rmm1zxyv+6,g8kk791z-3),1)
  jxxgaear=m8lw2qit.render(self.trdhw9re,True,(20,20,20))
  byl68ntk.blit(jxxgaear,(rmm1zxyv-jxxgaear.get_width()//2,self.pllkstn3.f1bl08kg-20))
def ob7p0rnp():
 return[my6wktak('Vera','gv4k00',iq5c34dx['tudttj'],120,140),my6wktak('Duncan','t7fr91',iq5c34dx['bdoz6w'],383,110),my6wktak('Mira','rfu7bf',iq5c34dx['wzwl3z'],650,140)]
yex8fsv8={'gv4k00':'Vitality Shop - Vera','t7fr91':'Combat Shop - Duncan','rfu7bf':'Mobility Shop - Mira'}
def yjr0fzau(key,xwqvr1h6):
 o4dd1vn8=jsylztgx[key]
 return int(o4dd1vn8['fuxk0a']*o4dd1vn8['hx0gu4']**xwqvr1h6)
def tacj4t0s(gxlk8wru,x5m9j98c,mpyxdw2z):
 (m8lw2qit,rh0w064w,rgdej31g,ebt3g2qz)=mpyxdw2z
 b78okz1p=[k for(k,kr0aymk9)in jsylztgx.items()if kr0aymk9['pcs4ke']==x5m9j98c]
 pa8s8hmb=110*len(b78okz1p)+20
 vt26ys44=oohp6vz4(420,pa8s8hmb+oohp6vz4.rla5ju9b+60,z0xkxwd8,title=yex8fsv8.get(x5m9j98c,'Shop'),title_font=rgdej31g)
 pv4ykade=vt26ys44.pllkstn3.f1bl08kg+vt26ys44.nvuprt77
 li9nb74x=pa8s8hmb//len(b78okz1p)
 for(bokzixza,key)in enumerate(b78okz1p):
  o4dd1vn8=jsylztgx[key]
  vk3g84ut=gxlk8wru['meta_upgrades'].get(key,0)
  a62c9t19=vk3g84ut>=o4dd1vn8['zq9bc2']
  if a62c9t19:
   title=f"{o4dd1vn8['ykht8x']}  MAX LEVEL"
  else:
   cnqt3wve=yjr0fzau(key,vk3g84ut)
   title=f"{o4dd1vn8['ykht8x']}  Lv.{vk3g84ut} -> {vk3g84ut + 1}   [{cnqt3wve} res]"
  nd6357oo=hc58drc1(vt26ys44.pllkstn3.j1kfk7y6+12,pv4ykade+bokzixza*li9nb74x+6,vt26ys44.pllkstn3.width-24,li9nb74x-10,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,ebt3g2qz,title,12,subtitle=o4dd1vn8['nddqhk'],sub_font=rh0w064w,kind='meta',key=key)
  nd6357oo.maxed=a62c9t19
  vt26ys44.add(nd6357oo)
 rk8r2ykc=pv4ykade+len(b78okz1p)*li9nb74x+12
 u1jhuwb6=hc58drc1(vt26ys44.pllkstn3.j1kfk7y6+12,rk8r2ykc,vt26ys44.pllkstn3.width-24,40,(180,80,80),(120,40,40),(210,100,100),(150,60,60),ebt3g2qz,'Close (ESC)',10,kind='close',key=None)
 vt26ys44.add(u1jhuwb6)
 return vt26ys44
def t54piwzn(byl68ntk,vw6m7b5c,gxlk8wru,h8s2ftom):
 m8lw2qit=pygame.font.SysFont('arial',22)
 rh0w064w=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',26,bold=True)
 rgdej31g=pygame.font.SysFont('arial',22,bold=True)
 ebt3g2qz=pygame.font.SysFont('arial',20,bold=True)
 cp91i3vm=pygame.font.SysFont('arial',15)
 mpyxdw2z=(m8lw2qit,rh0w064w,rgdej31g,ebt3g2qz)
 c0hpmnz1=zbqe7ckw()
 y8dd2255=ob7p0rnp()
 ytb9xxay=pygame.Rect(ygspk9p3//2-70,tp0lvsnu-60,140,44)
 ytv3i12v=None
 uva2ieuc=None
 while True:
  xq46nouh=pygame.event.get()
  for mqxlm5q2 in xq46nouh:
   if mqxlm5q2.type==pygame.QUIT:
    return'quit'
   if mqxlm5q2.type==pygame.KEYDOWN and mqxlm5q2.key==pygame.K_ESCAPE and ytv3i12v:
    ytv3i12v=None
    uva2ieuc=None
  if ytv3i12v is None:
   c0hpmnz1.wb7f6fdh()
   d5ixva1n=None
   for a2wspofv in y8dd2255:
    if c0hpmnz1.pllkstn3.colliderect(a2wspofv.pllkstn3.inflate(24,24)):
     if not a2wspofv.q5amln4p:
      d5ixva1n=a2wspofv
      a2wspofv.q5amln4p=True
      break
    else:
     a2wspofv.q5amln4p=False
   if d5ixva1n:
    uva2ieuc=d5ixva1n.x5m9j98c
    ytv3i12v=tacj4t0s(gxlk8wru,uva2ieuc,mpyxdw2z)
   if c0hpmnz1.pllkstn3.colliderect(ytb9xxay):
    return'start_game'
  else:
   for aicvqy5i in ytv3i12v.wa45hvgo:
    aicvqy5i.update(xq46nouh)
   iektsg7f=next((le9oe941 for le9oe941 in ytv3i12v.wa45hvgo if le9oe941.iektsg7f),None)
   if iektsg7f is not None:
    if iektsg7f.kind=='close':
     ytv3i12v=None
     uva2ieuc=None
    elif iektsg7f.kind=='meta'and(not getattr(iektsg7f,'maxed',False)):
     key=iektsg7f.key
     vk3g84ut=gxlk8wru['meta_upgrades'].get(key,0)
     cnqt3wve=yjr0fzau(key,vk3g84ut)
     if gxlk8wru['resources']>=cnqt3wve:
      gxlk8wru['resources']-=cnqt3wve
      gxlk8wru['meta_upgrades'][key]=vk3g84ut+1
      h8s2ftom(gxlk8wru)
      ytv3i12v=tacj4t0s(gxlk8wru,uva2ieuc,mpyxdw2z)
  byl68ntk.fill((190,225,190))
  for onqyyf9r in range(0,ygspk9p3,vve92mpn):
   pygame.draw.line(byl68ntk,(160,205,160),(onqyyf9r,0),(onqyyf9r,tp0lvsnu),1)
  for jo8e7flq in range(0,tp0lvsnu,vve92mpn):
   pygame.draw.line(byl68ntk,(160,205,160),(0,jo8e7flq),(ygspk9p3,jo8e7flq),1)
  pygame.draw.rect(byl68ntk,iq5c34dx['r4uov5'],ytb9xxay,border_radius=10)
  pygame.draw.rect(byl68ntk,(150,110,0),ytb9xxay,width=3,border_radius=10)
  xasez2nx=rh0w064w.render('ENTER RUN',True,(40,30,0))
  byl68ntk.blit(xasez2nx,(ytb9xxay.centerx-xasez2nx.get_width()//2,ytb9xxay.centery-xasez2nx.get_height()//2))
  for a2wspofv in y8dd2255:
   a2wspofv.dw7nh8rq(byl68ntk,rh0w064w)
  c0hpmnz1.dw7nh8rq(byl68ntk)
  fpa8hyex=pygame.Rect(12,12,220,40)
  f55dmcxx=pygame.Surface((fpa8hyex.width,fpa8hyex.height),pygame.SRCALPHA)
  pygame.draw.rect(f55dmcxx,(255,255,255,160),f55dmcxx.get_rect(),border_radius=10)
  byl68ntk.blit(f55dmcxx,fpa8hyex.topleft)
  wd6r30oj=m8lw2qit.render(f"Resources: {gxlk8wru['resources']}",True,(20,20,20))
  byl68ntk.blit(wd6r30oj,(20,22))
  htgsiwg0=title_font.render('HOMEBASE',True,(20,40,20))
  byl68ntk.blit(htgsiwg0,(ygspk9p3//2-htgsiwg0.get_width()//2,12))
  nd31k9qm=cp91i3vm.render('Walk into a trader to shop. Walk into ENTER RUN to start a run.',True,(20,40,20))
  byl68ntk.blit(nd31k9qm,(ygspk9p3//2-nd31k9qm.get_width()//2,tp0lvsnu-105))
  if ytv3i12v:
   ytv3i12v.dw7nh8rq(byl68ntk)
  pygame.display.flip()
  vw6m7b5c.tick(pi3qk2ia)
