import pygame
from v7bnhjw6 import*
from piua08ek import*
from entities import*
from xu7bfxq7 import*
from zhm40oey import*
from bixaw63d import u15pdtz9
from gjg2y8rg import zflv1xxl,wd6r30oj,uwxrum2l,my6wktak
from exso7vbg import tbxf445c
from ob07g2re import vhxs58yr
import time
pygame.init()
gg7oq2zd=pygame.display.set_mode((v4u89yjb,rla5ju9b))
obc2nnuv=pygame.time.Clock()
luzbikci=pygame.Surface((v4u89yjb,rla5ju9b),pygame.SRCALPHA)
for u8c2jwoc in range(rla5ju9b):
 yw5py6b2=u8c2jwoc/max(1,rla5ju9b-1)
 t1w1ht7p=int(45*(1-yw5py6b2))
 pygame.draw.line(luzbikci,(235,245,250,t1w1ht7p),(0,u8c2jwoc),(v4u89yjb,u8c2jwoc))
def uc1xi04b(gg7oq2zd,jenvg3kk,sne6loh2=120,g1g1r1dw=10):
 holeyrvx=pygame.Surface((jenvg3kk.width,jenvg3kk.height),pygame.SRCALPHA)
 pygame.draw.rect(holeyrvx,(255,255,255,sne6loh2),holeyrvx.get_rect(),border_radius=g1g1r1dw)
 gg7oq2zd.blit(holeyrvx,jenvg3kk.topleft)
def pllkstn3():
 title_font=pygame.font.SysFont('arial',40,bold=True)
 zpajssuu=pygame.font.SysFont('arial',16)
 tk0qtl3q=pygame.font.SysFont('arial',22,bold=True)
 h8s2ftom=pygame.font.SysFont('arial',15)
 gn89qkns=[]
 for ftrflqbm in range(1,my6wktak+1):
  hcxhgnze=uwxrum2l(ftrflqbm)
  if hcxhgnze:
   subtitle=f"Level {hcxhgnze['high_level']}  |  {hcxhgnze['resources']} resources  |  {hcxhgnze['runs_played']} runs"
  else:
   subtitle='Empty - New Game'
  wppsfnko=hc58drc1(v4u89yjb//2-170,170+(ftrflqbm-1)*110,340,90,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,tk0qtl3q,f'Slot {ftrflqbm}',12,subtitle=subtitle,sub_font=h8s2ftom,kind='slot',key=ftrflqbm)
  gn89qkns.append(wppsfnko)
 while True:
  mq7nc85e=pygame.event.get()
  for pbo119xp in mq7nc85e:
   if pbo119xp.type==pygame.QUIT:
    return None
  for wppsfnko in gn89qkns:
   wppsfnko.update(mq7nc85e)
   if wppsfnko.uos0fb4y:
    return wppsfnko.key
  gg7oq2zd.fill(iq5c34dx['n7csuy'])
  m3hcws2w=title_font.render('CHASE GAME',True,(20,20,40))
  gg7oq2zd.blit(m3hcws2w,(v4u89yjb//2-m3hcws2w.get_width()//2,70))
  vmxb9yo1=zpajssuu.render('Choose a save slot',True,(30,30,30))
  gg7oq2zd.blit(vmxb9yo1,(v4u89yjb//2-vmxb9yo1.get_width()//2,135))
  for wppsfnko in gn89qkns:
   wppsfnko.wc7x0h3j(gg7oq2zd)
  pygame.display.flip()
  obc2nnuv.tick(pi3qk2ia)
def v0rxxf36(d1hm38ks):
 eatvzkhi=pygame.font.SysFont('arial',28)
 aqclpoxk=pygame.font.SysFont('arial',48)
 h8s2ftom=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',20,bold=True)
 njxurgow=pygame.font.SysFont('arial',24,bold=True)
 tk0qtl3q=pygame.font.SysFont('arial',22,bold=True)
 ra9kepad=pygame.font.SysFont('arial',16,bold=True)
 player=r0tvhhpb(meta_upgrades=d1hm38ks.get('meta_upgrades',{}))
 dw7nh8rq=[]
 yw6zbnz8=[]
 vyb6li07=[]
 xp8mgyn2=[]
 bfoqmf5l=[]
 xuu13i59=[]
 kc1fjotg=[]
 eq3tq1s0=[c8yfbntp[0]]
 awnwlc83=['dzjssz']
 player.d5ixva1n['dzjssz']=1
 azc4xl99=False
 he9p3jpx=False
 iektsg7f=False
 pvasifpw=3
 v24479qt=time.time()
 todsx4nx=player.o4dd1vn8
 hay64yfd=0
 s7fbmenu=bom5igqp*pi3qk2ia
 giec4d14=dict(mjh75lxo)
 y8dd2255=None
 gp6orsnc=hc58drc1(v4u89yjb-40,rla5ju9b-40,30,30,z0xkxwd8,wa11dpg8,hyihair4,cq5uznof,h8s2ftom,'| |',15)
 while True:
  mq7nc85e=pygame.event.get()
  for pbo119xp in mq7nc85e:
   if pbo119xp.type==pygame.QUIT:
    return(hay64yfd,player.o4dd1vn8,True)
   if azc4xl99 and pbo119xp.type==pygame.KEYDOWN and(pbo119xp.key in(pygame.K_RETURN,pygame.K_SPACE)):
    return(hay64yfd,player.o4dd1vn8,False)
   if pbo119xp.type==pygame.KEYDOWN:
    if pbo119xp.key==pygame.K_p and(not iektsg7f):
     if he9p3jpx:
      gp6orsnc.vm65q57t='| |'
     else:
      gp6orsnc.vm65q57t='X'
     if he9p3jpx:
      iektsg7f=True
      pvasifpw=3
      v24479qt=time.time()
     he9p3jpx=not he9p3jpx
  amcixdu1=False
  if iektsg7f:
   if time.time()-v24479qt>=1:
    v24479qt=time.time()
    pvasifpw-=1
    if pvasifpw<=0:
     iektsg7f=False
     pvasifpw=3
  if not player.qxb7gbdg and(not azc4xl99)and(not he9p3jpx)and(not iektsg7f):
   for jm25len6 in xp8mgyn2[:]:
    rk2u1rsu=jm25len6.update(player)
    if rk2u1rsu:
     amcixdu1=True
    if jm25len6.wb7f6fdh:
     vhxs58yr('v3c71u')
     d46aexl6=random.randint(re7ur23g,uccblskr)
     hay64yfd+=d46aexl6
     for m53a5qbs in range(10):
      vyb6li07.append(cb2uuijn([iq5c34dx['dq3b9s'],iq5c34dx['o6d10a']],2,4,-3,3,jm25len6.jenvg3kk.centerx,jm25len6.jenvg3kk.centery,life=30))
     xp8mgyn2.remove(jm25len6)
   s7fbmenu-=1
   if s7fbmenu<=0:
    s7fbmenu=bom5igqp*pi3qk2ia
    if len(xp8mgyn2)<r1yzoyn6:
     xp8mgyn2.append(u15pdtz9(player))
   if not amcixdu1:
    for hjkuuhcl in awnwlc83:
     giec4d14[hjkuuhcl]-=1
     if giec4d14[hjkuuhcl]<=0:
      jslulzfy=player.d5ixva1n.get(hjkuuhcl,1)
      d1ieixwc=mjh75lxo[hjkuuhcl]*player.oqse3tv1*pg3yu6vk(jslulzfy)
      giec4d14[hjkuuhcl]=max(4,int(d1ieixwc))
      t54piwzn=uqjiujv6[hjkuuhcl]['mrf5a7']
      vt6om1fb=player.cnqt3wve*x3n27m5p(jslulzfy)
      yw6zbnz8.append(ky20479t(hjkuuhcl,player.jenvg3kk.centerx-t54piwzn//2,player.jenvg3kk.centery-t54piwzn//2,t54piwzn,t54piwzn,player.fpa8hyex['e56waf'],player.fpa8hyex['eqkwqh'],vt6om1fb))
      vhxs58yr('jr87iy',volume=0.5,min_interval_ms=90)
   qcd81twh=min(isj6bw3b,d60fkhmy*(1+0.12*(player.o4dd1vn8-1)))
   if random.random()<qcd81twh:
    yp3cyazb(dw7nh8rq,eq3tq1s0)
   player.r2muljav()
   if player.o4dd1vn8>todsx4nx:
    vhxs58yr('qc6dr0')
    if player.o4dd1vn8<=len(c8yfbntp):
     wg25cfzf=c8yfbntp[player.o4dd1vn8-1]
     if wg25cfzf not in eq3tq1s0:
      eq3tq1s0.append(wg25cfzf)
    todsx4nx=player.o4dd1vn8
   if player.mn7h9g1a<=0:
    azc4xl99=True
   for v15cqzcu in dw7nh8rq:
    v15cqzcu.r2muljav(player)
    for reqy08p0 in v15cqzcu.gp84dyt9:
     reqy08p0.r2muljav(player)
     reqy08p0.ytv3i12v(dw7nh8rq,vyb6li07,yw6zbnz8,player=player,target='player')
    v15cqzcu.gp84dyt9=[iy6qktc8 for iy6qktc8 in v15cqzcu.gp84dyt9 if not iy6qktc8.sl65wvjx]
   for rk8r2ykc in bfoqmf5l:
    rk8r2ykc.r2muljav(player)
   for uysal8m1 in yw6zbnz8:
    uysal8m1.r2muljav(player,q7i6yuj7(dw7nh8rq,uysal8m1))
    uysal8m1.ytv3i12v(dw7nh8rq,vyb6li07,yw6zbnz8)
   for v15cqzcu in dw7nh8rq:
    for(jqzpniqf,nubmxnsz,ouuylaja,mygfliji)in v15cqzcu.zflse45b:
     kc1fjotg.append(jdqqzrlf(jqzpniqf,nubmxnsz,ouuylaja,ra9kepad,color=mygfliji))
     vhxs58yr('mmgvu4',volume=0.4,min_interval_ms=60)
    v15cqzcu.zflse45b.clear()
   for a2wspofv in vyb6li07[:]:
    a2wspofv['r7myow']+=a2wspofv['e56waf']
    a2wspofv['ykht8x']+=a2wspofv['eqkwqh']
    a2wspofv['vcw2lb']-=1
    if a2wspofv['vcw2lb']<=0:
     vyb6li07.remove(a2wspofv)
   for xxkdq95g in kc1fjotg[:]:
    xxkdq95g['vcw2lb']-=1
    if xxkdq95g['vcw2lb']<=0:
     kc1fjotg.remove(xxkdq95g)
   for le9oe941 in xuu13i59[:]:
    le9oe941.update()
    if le9oe941.sl65wvjx():
     xuu13i59.remove(le9oe941)
  if player.qxb7gbdg and(not azc4xl99):
   if y8dd2255==None:
    got7txkd=[]
    for kt94ow3l in uqjiujv6:
     if kt94ow3l=='wdl5tg':
      continue
     if kt94ow3l not in awnwlc83:
      got7txkd.append(('ozdcuj',kt94ow3l))
    for kt94ow3l in awnwlc83:
     if player.d5ixva1n.get(kt94ow3l,1)<rrcbpljd:
      got7txkd.append(('yrp422',kt94ow3l))
    for k in yswjckjl:
     if player.tza7x73q.get(k,0)<yswjckjl[k]['kp82kb']:
      got7txkd.append(('w9laac',k))
    if not got7txkd:
     player.qxb7gbdg=False
    else:
     random.shuffle(got7txkd)
     clkqzfpq=got7txkd[:3]
     ruq9e5co=120*len(clkqzfpq)+20
     y8dd2255=rcfnfhol(400,ruq9e5co+rcfnfhol.gokc1msy,n2vlpys2,title='LEVEL UP! Choose an upgrade',title_font=njxurgow)
     kybwmlun=ruq9e5co//len(clkqzfpq)
     wzs13c9x=y8dd2255.jenvg3kk.vsjchzjq+y8dd2255.kkzruin3
     for(ftrflqbm,(kind,key))in enumerate(clkqzfpq):
      if kind=='ozdcuj':
       title=f'NEW WEAPON: {uyhl1c32[key]}'
       subtitle='Unlock this weapon'
      elif kind=='yrp422':
       jxxgaear=player.d5ixva1n.get(key,1)
       title=f'{uyhl1c32[key]}  Lv.{jxxgaear} -> {jxxgaear + 1}'
       subtitle='+12% damage, faster cooldown'
      else:
       jxxgaear=player.tza7x73q.get(key,0)
       title=f"{yswjckjl[key]['e0s41k']}  Lv.{jxxgaear} -> {jxxgaear + 1}"
       subtitle=yswjckjl[key]['y3lxch']
      wppsfnko=hc58drc1(y8dd2255.jenvg3kk.qic1l7dy+12,wzs13c9x+ftrflqbm*kybwmlun+6,y8dd2255.jenvg3kk.width-24,kybwmlun-12,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,tk0qtl3q,title,12,subtitle=subtitle,sub_font=h8s2ftom,kind=kind,key=key)
      y8dd2255.add(wppsfnko)
   if y8dd2255 is not None:
    for yjluujmi in y8dd2255.wvpw232u:
     yjluujmi.update(mq7nc85e)
     if yjluujmi.uos0fb4y:
      if yjluujmi.kind=='ozdcuj':
       awnwlc83.append(yjluujmi.key)
       player.d5ixva1n[yjluujmi.key]=1
       giec4d14[yjluujmi.key]=mjh75lxo[yjluujmi.key]
      elif yjluujmi.kind=='yrp422':
       player.wa45hvgo(yjluujmi.key)
      elif yjluujmi.kind=='w9laac':
       player.on0jnwny(yjluujmi.key)
      player.qxb7gbdg=False
      y8dd2255=None
  xwk2rv23(dw7nh8rq)
  gp6orsnc.update(mq7nc85e)
  if gp6orsnc.uos0fb4y and(not iektsg7f):
   if he9p3jpx:
    gp6orsnc.vm65q57t='| |'
   else:
    gp6orsnc.vm65q57t='X'
   if he9p3jpx:
    iektsg7f=True
    pvasifpw=3
    v24479qt=time.time()
   he9p3jpx=not he9p3jpx
  (dw7nh8rq,yw6zbnz8,bfoqmf5l)=ytb9xxay(dw7nh8rq,yw6zbnz8,bfoqmf5l,player,xuu13i59,kc1fjotg,ra9kepad)
  for(ejbzutru,rm0j36tc,wvndfdw7,rserev36)in player.zflse45b:
   kc1fjotg.append(jdqqzrlf(ejbzutru,rm0j36tc,wvndfdw7,ra9kepad,color=rserev36))
   vhxs58yr('hzj7ub')
  player.zflse45b.clear()
  li9nb74x=player.jenvg3kk.qic1l7dy-v4u89yjb//2
  zfb7r31q=player.jenvg3kk.vsjchzjq-rla5ju9b//2
  li9nb74x=max(min(li9nb74x,cqoldfor-v4u89yjb),0)
  zfb7r31q=max(min(zfb7r31q,ygspk9p3-rla5ju9b),0)
  vmy9x8sy=kz1uu7zy=0
  if player.k8qeoz0k:
   player.wtl0thhz-=1
   vmy9x8sy=random.randint(-b18hafey,b18hafey)
   kz1uu7zy=random.randint(-b18hafey,b18hafey)
   li9nb74x+=vmy9x8sy
   zfb7r31q+=kz1uu7zy
   if player.wtl0thhz<=0:
    player.k8qeoz0k=False
  gg7oq2zd.fill(iq5c34dx['n7csuy'])
  gg7oq2zd.blit(luzbikci,(0,0))
  uidlrye8(gg7oq2zd,li9nb74x,zfb7r31q)
  for jm25len6 in xp8mgyn2:
   jm25len6.wc7x0h3j(gg7oq2zd,li9nb74x,zfb7r31q)
  player.wc7x0h3j(gg7oq2zd,li9nb74x,zfb7r31q)
  for v15cqzcu in dw7nh8rq:
   v15cqzcu.wc7x0h3j(gg7oq2zd,li9nb74x,zfb7r31q)
   for reqy08p0 in v15cqzcu.gp84dyt9:
    reqy08p0.wc7x0h3j(gg7oq2zd,li9nb74x,zfb7r31q)
  for uysal8m1 in yw6zbnz8:
   uysal8m1.wc7x0h3j(gg7oq2zd,li9nb74x,zfb7r31q)
  for rk8r2ykc in bfoqmf5l:
   rk8r2ykc.wc7x0h3j(gg7oq2zd,li9nb74x,zfb7r31q)
  for a2wspofv in vyb6li07:
   pygame.draw.circle(gg7oq2zd,a2wspofv['c37qqy'],(int(a2wspofv['r7myow']-li9nb74x),int(a2wspofv['ykht8x']-zfb7r31q)),a2wspofv['mrf5a7'])
  for xxkdq95g in kc1fjotg:
   fp47b42g(gg7oq2zd,xxkdq95g,li9nb74x,zfb7r31q)
  for le9oe941 in xuu13i59:
   le9oe941.wc7x0h3j(gg7oq2zd,li9nb74x,zfb7r31q)
  if y8dd2255!=None:
   y8dd2255.wc7x0h3j(gg7oq2zd)
  j7f00ter=40+18*len(awnwlc83)
  uc1xi04b(gg7oq2zd,pygame.Rect(12,12,190,j7f00ter))
  holeyrvx=eatvzkhi.render(f'Enemies: {len(dw7nh8rq)}',True,(20,20,20))
  gg7oq2zd.blit(holeyrvx,(20+vmy9x8sy,20+kz1uu7zy))
  m81udp2f=50
  for kt94ow3l in awnwlc83:
   jxxgaear=player.d5ixva1n.get(kt94ow3l,1)
   huh17j8q=h8s2ftom.render(f'{uyhl1c32[kt94ow3l]} Lv.{jxxgaear}',True,(30,30,30))
   gg7oq2zd.blit(huh17j8q,(20+vmy9x8sy,m81udp2f+kz1uu7zy))
   m81udp2f+=18
  uc1xi04b(gg7oq2zd,pygame.Rect(v4u89yjb-180,12,168,32))
  nxxjve3d=h8s2ftom.render(f'Resources: {hay64yfd}',True,(20,20,20))
  gg7oq2zd.blit(nxxjve3d,(v4u89yjb-170+vmy9x8sy,20+kz1uu7zy))
  if amcixdu1:
   hhl1737s=h8s2ftom.render('Opening chest... weapons offline!',True,iq5c34dx['xyhhg8'])
   gg7oq2zd.blit(hhl1737s,(v4u89yjb//2-hhl1737s.get_width()//2+vmy9x8sy,12+kz1uu7zy))
  uc1xi04b(gg7oq2zd,pygame.Rect(12,rla5ju9b-50,388,38))
  k2ixivzk=title_font.render(f'Lv.{player.o4dd1vn8}',True,(20,20,20))
  gg7oq2zd.blit(k2ixivzk,(20+vmy9x8sy,rla5ju9b-40+kz1uu7zy))
  w2kql0ht=v83tqll8[min(player.o4dd1vn8,len(v83tqll8)-1)]
  yjr0fzau=min(1.0,player.nngmx1gm/w2kql0ht)
  fo75rh8l(gg7oq2zd,90,rla5ju9b-34,290,yjr0fzau,height=16,fg=iq5c34dx['dq3b9s'],bg=(70,70,70))
  if azc4xl99:
   ee1g983e=pygame.Surface((v4u89yjb,rla5ju9b),pygame.SRCALPHA)
   ee1g983e.fill((0,0,0,150))
   gg7oq2zd.blit(ee1g983e,(0,0))
   holeyrvx=aqclpoxk.render('GAME OVER',True,iq5c34dx['r3hxyj'])
   q26yg3dx=aqclpoxk.render('GAME OVER',True,(0,0,0))
   (pa8s8hmb,pv4ykade)=(v4u89yjb//2-holeyrvx.get_width()//2,rla5ju9b//2-holeyrvx.get_height()//2)
   gg7oq2zd.blit(q26yg3dx,(pa8s8hmb+2,pv4ykade+2))
   gg7oq2zd.blit(holeyrvx,(pa8s8hmb,pv4ykade))
   mnx4sn6s=eatvzkhi.render(f'You reached Level {player.o4dd1vn8}  |  +{hay64yfd} resources',True,iq5c34dx['v9hbn5'])
   gg7oq2zd.blit(mnx4sn6s,(v4u89yjb//2-mnx4sn6s.get_width()//2,pv4ykade+holeyrvx.get_height()+10))
   w8wj0uun=h8s2ftom.render('Press ENTER to return to the Homebase',True,iq5c34dx['v9hbn5'])
   gg7oq2zd.blit(w8wj0uun,(v4u89yjb//2-w8wj0uun.get_width()//2,pv4ykade+holeyrvx.get_height()+40))
  if iektsg7f:
   ee1g983e=pygame.Surface((v4u89yjb,rla5ju9b),pygame.SRCALPHA)
   ee1g983e.fill((0,0,0,150))
   gg7oq2zd.blit(ee1g983e,(0,0))
   holeyrvx=aqclpoxk.render(f'Get ready!',True,iq5c34dx['r3hxyj'])
   q26yg3dx=aqclpoxk.render(f'Get ready!',True,(0,0,0))
   (pa8s8hmb,pv4ykade)=(v4u89yjb//2-holeyrvx.get_width()//2,rla5ju9b//2-holeyrvx.get_height()//2)
   gg7oq2zd.blit(q26yg3dx,(pa8s8hmb+2,pv4ykade+2))
   gg7oq2zd.blit(holeyrvx,(pa8s8hmb,pv4ykade))
   mnx4sn6s=eatvzkhi.render(f'Game continuing in {pvasifpw}',True,iq5c34dx['v9hbn5'])
   gg7oq2zd.blit(mnx4sn6s,(v4u89yjb//2-mnx4sn6s.get_width()//2,pv4ykade+holeyrvx.get_height()+10))
  if he9p3jpx:
   ee1g983e=pygame.Surface((v4u89yjb,rla5ju9b),pygame.SRCALPHA)
   ee1g983e.fill((0,0,0,150))
   gg7oq2zd.blit(ee1g983e,(0,0))
   holeyrvx=aqclpoxk.render(f'Game Paused',True,iq5c34dx['r3hxyj'])
   q26yg3dx=aqclpoxk.render(f'Game Paused',True,(0,0,0))
   (pa8s8hmb,pv4ykade)=(v4u89yjb//2-holeyrvx.get_width()//2,rla5ju9b//2-holeyrvx.get_height()//2)
   gg7oq2zd.blit(q26yg3dx,(pa8s8hmb+2,pv4ykade+2))
   gg7oq2zd.blit(holeyrvx,(pa8s8hmb,pv4ykade))
  gp6orsnc.wc7x0h3j(gg7oq2zd)
  pygame.display.flip()
  obc2nnuv.tick(pi3qk2ia)
def crsb4gf1():
 iaq7b7v1=pllkstn3()
 if iaq7b7v1 is None:
  return
 d1hm38ks=zflv1xxl(iaq7b7v1)
 def h4l1vznq(qtzk3ny9):
  wd6r30oj(iaq7b7v1,qtzk3ny9)
 h4l1vznq(d1hm38ks)
 while True:
  ia529603=tbxf445c(gg7oq2zd,obc2nnuv,d1hm38ks,h4l1vznq)
  if ia529603=='quit':
   break
  if ia529603=='start_game':
   (sygvwopl,k1taa0i5,xxns2zyb)=v0rxxf36(d1hm38ks)
   d1hm38ks['resources']+=sygvwopl
   d1hm38ks['high_level']=max(d1hm38ks.get('high_level',0),k1taa0i5)
   d1hm38ks['runs_played']=d1hm38ks.get('runs_played',0)+1
   h4l1vznq(d1hm38ks)
   if xxns2zyb:
    break
if __name__=='__main__':
 crsb4gf1()
