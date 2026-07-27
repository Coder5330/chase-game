import pygame
from en1x2gdg import*
from jxgbngz6 import*
from entities import*
from c4kek4ae import*
from p1onx0gu import*
from f60xng2i import t5sn961j
from tx48wze4 import n3rlkte4,xwk2rv23,d1hm38ks,jsylztgx
from ixo100vh import jenvg3kk
import time
pygame.init()
gmoft6yr=pygame.display.set_mode((mqp49kwv,rla5ju9b))
pvasifpw=pygame.time.Clock()
luzbikci=pygame.Surface((mqp49kwv,rla5ju9b),pygame.SRCALPHA)
for m53a5qbs in range(rla5ju9b):
 wrbw2zla=m53a5qbs/max(1,rla5ju9b-1)
 x37pqkoj=int(45*(1-wrbw2zla))
 pygame.draw.line(luzbikci,(235,245,250,x37pqkoj),(0,m53a5qbs),(mqp49kwv,m53a5qbs))
def sl65wvjx(gmoft6yr,f8rtm4j3,u8c2jwoc=120,zflse45b=10):
 xo2t8fy6=pygame.Surface((f8rtm4j3.width,f8rtm4j3.height),pygame.SRCALPHA)
 pygame.draw.rect(xo2t8fy6,(255,255,255,u8c2jwoc),xo2t8fy6.get_rect(),border_radius=zflse45b)
 gmoft6yr.blit(xo2t8fy6,f8rtm4j3.topleft)
def xsspye9r():
 title_font=pygame.font.SysFont('arial',40,bold=True)
 jq1ddpus=pygame.font.SysFont('arial',16)
 j2vmcqbn=pygame.font.SysFont('arial',22,bold=True)
 wd6r30oj=pygame.font.SysFont('arial',15)
 jc54wsqt=[]
 for z8z3v6di in range(1,jsylztgx+1):
  ck7n3bfh=d1hm38ks(z8z3v6di)
  if ck7n3bfh:
   subtitle=f"Level {ck7n3bfh['high_level']}  |  {ck7n3bfh['resources']} resources  |  {ck7n3bfh['runs_played']} runs"
  else:
   subtitle='Empty - New Game'
  rzs43c5b=hc58drc1(mqp49kwv//2-170,170+(z8z3v6di-1)*110,340,90,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,j2vmcqbn,f'Slot {z8z3v6di}',12,subtitle=subtitle,sub_font=wd6r30oj,kind='slot',key=z8z3v6di)
  jc54wsqt.append(rzs43c5b)
 while True:
  zefqjg02=pygame.event.get()
  for jqxs6esj in zefqjg02:
   if jqxs6esj.type==pygame.QUIT:
    return None
  for rzs43c5b in jc54wsqt:
   rzs43c5b.update(zefqjg02)
   if rzs43c5b.d1ieixwc:
    return rzs43c5b.key
  gmoft6yr.fill(iq5c34dx['uq0e27'])
  kn5gjj8m=title_font.render('CHASE GAME',True,(20,20,40))
  gmoft6yr.blit(kn5gjj8m,(mqp49kwv//2-kn5gjj8m.get_width()//2,70))
  cjn2fomd=jq1ddpus.render('Choose a save slot',True,(30,30,30))
  gmoft6yr.blit(cjn2fomd,(mqp49kwv//2-cjn2fomd.get_width()//2,135))
  for rzs43c5b in jc54wsqt:
   rzs43c5b.do2m71hs(gmoft6yr)
  pygame.display.flip()
  pvasifpw.tick(pi3qk2ia)
def k1taa0i5(nxxjve3d):
 g70e3p15=pygame.font.SysFont('arial',28)
 x03uvule=pygame.font.SysFont('arial',48)
 wd6r30oj=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',20,bold=True)
 zdan085r=pygame.font.SysFont('arial',24,bold=True)
 j2vmcqbn=pygame.font.SysFont('arial',22,bold=True)
 gf8f3gr9=pygame.font.SysFont('arial',16,bold=True)
 player=rqf5q14j(meta_upgrades=nxxjve3d.get('meta_upgrades',{}))
 wc7x0h3j=[]
 uww5wfcp=[]
 mmn32u1i=[]
 nd6357oo=[]
 izhwy9he=[]
 tnz61231=[]
 wfhj4d0j=[]
 e8zgvwwu=[c8yfbntp[0]]
 qxt6ridl=['twvwvi']
 player.ejbzutru['twvwvi']=1
 g5l8a78e=False
 mfc79m96=False
 uos0fb4y=False
 uysal8m1=3
 t54piwzn=time.time()
 m3pt5r5r=player.wvpw232u
 no0u93mz=0
 f2voi8uy=bom5igqp*pi3qk2ia
 f8wquuy5=dict(mjh75lxo)
 wy0mahym=None
 while True:
  zefqjg02=pygame.event.get()
  for jqxs6esj in zefqjg02:
   if jqxs6esj.type==pygame.QUIT:
    return(no0u93mz,player.wvpw232u,True)
   if g5l8a78e and jqxs6esj.type==pygame.KEYDOWN and(jqxs6esj.key in(pygame.K_RETURN,pygame.K_SPACE)):
    return(no0u93mz,player.wvpw232u,False)
   if jqxs6esj.type==pygame.KEYDOWN:
    if jqxs6esj.key==pygame.K_p:
     if mfc79m96:
      uos0fb4y=True
      uysal8m1=3
      t54piwzn=time.time()
     mfc79m96=not mfc79m96
  yw6zbnz8=False
  if uos0fb4y:
   if time.time()-t54piwzn>=1:
    t54piwzn=time.time()
    uysal8m1-=1
    if uysal8m1<=0:
     uos0fb4y=False
     uysal8m1=3
  if not player.ayr1k12v and(not g5l8a78e)and(not mfc79m96)and(not uos0fb4y):
   for dzsedfqs in nd6357oo[:]:
    onqyyf9r=dzsedfqs.update(player)
    if onqyyf9r:
     yw6zbnz8=True
    if dzsedfqs.a62c9t19:
     v6xii5p5=random.randint(re7ur23g,uccblskr)
     no0u93mz+=v6xii5p5
     for dtx63cfl in range(10):
      mmn32u1i.append(wtl0thhz([iq5c34dx['t753ay'],iq5c34dx['iwu3bf']],2,4,-3,3,dzsedfqs.f8rtm4j3.centerx,dzsedfqs.f8rtm4j3.centery,life=30))
     nd6357oo.remove(dzsedfqs)
   f2voi8uy-=1
   if f2voi8uy<=0:
    f2voi8uy=bom5igqp*pi3qk2ia
    if len(nd6357oo)<r1yzoyn6:
     nd6357oo.append(t5sn961j(player))
   if not yw6zbnz8:
    for wvndfdw7 in qxt6ridl:
     f8wquuy5[wvndfdw7]-=1
     if f8wquuy5[wvndfdw7]<=0:
      rm0j36tc=player.ejbzutru.get(wvndfdw7,1)
      u23y30ys=mjh75lxo[wvndfdw7]*player.i20cv3tl*ywcxz2ei(rm0j36tc)
      f8wquuy5[wvndfdw7]=max(4,int(u23y30ys))
      cq2q4qer=uqjiujv6[wvndfdw7]['mviifr']
      cnqt3wve=player.ep6beffl*r212pgym(rm0j36tc)
      uww5wfcp.append(yswjckjl(wvndfdw7,player.f8rtm4j3.centerx-cq2q4qer//2,player.f8rtm4j3.centery-cq2q4qer//2,cq2q4qer,cq2q4qer,player.ftrflqbm['lcf4mn'],player.ftrflqbm['r4uov5'],cnqt3wve))
   q26yg3dx=min(isj6bw3b,d60fkhmy*(1+0.12*(player.wvpw232u-1)))
   if random.random()<q26yg3dx:
    k8qeoz0k(wc7x0h3j,e8zgvwwu)
   player.y2f7atwy()
   if player.wvpw232u>m3pt5r5r:
    if player.wvpw232u<=len(c8yfbntp):
     gqq4d3kz=c8yfbntp[player.wvpw232u-1]
     if gqq4d3kz not in e8zgvwwu:
      e8zgvwwu.append(gqq4d3kz)
    m3pt5r5r=player.wvpw232u
   if player.sf337kuu<=0:
    g5l8a78e=True
   for uidlrye8 in wc7x0h3j:
    uidlrye8.y2f7atwy(player)
    for sk8yqk94 in uidlrye8.ia529603:
     sk8yqk94.y2f7atwy(player)
     sk8yqk94.sne6loh2(wc7x0h3j,mmn32u1i,uww5wfcp,player=player,target='player')
    uidlrye8.ia529603=[g7s55j2o for g7s55j2o in uidlrye8.ia529603 if not g7s55j2o.rk8r2ykc]
   for iie0rnuj in izhwy9he:
    iie0rnuj.y2f7atwy(player)
   for u3ifhv1x in uww5wfcp:
    u3ifhv1x.y2f7atwy(player,yrivh6t1(wc7x0h3j,u3ifhv1x))
    u3ifhv1x.sne6loh2(wc7x0h3j,mmn32u1i,uww5wfcp)
   for uidlrye8 in wc7x0h3j:
    for(mygfliji,b36htf4p,fp47b42g,g8kk791z)in uidlrye8.wb7f6fdh:
     wfhj4d0j.append(e9y3z2t4(mygfliji,b36htf4p,fp47b42g,gf8f3gr9,color=g8kk791z))
    uidlrye8.wb7f6fdh.clear()
   for pf0i9g5d in mmn32u1i[:]:
    pf0i9g5d['buzery']+=pf0i9g5d['lcf4mn']
    pf0i9g5d['qc6dr0']+=pf0i9g5d['r4uov5']
    pf0i9g5d['w2ugl6']-=1
    if pf0i9g5d['w2ugl6']<=0:
     mmn32u1i.remove(pf0i9g5d)
   for n64fgwje in wfhj4d0j[:]:
    n64fgwje['w2ugl6']-=1
    if n64fgwje['w2ugl6']<=0:
     wfhj4d0j.remove(n64fgwje)
   for sygvwopl in tnz61231[:]:
    sygvwopl.update()
    if sygvwopl.rk8r2ykc():
     tnz61231.remove(sygvwopl)
  if player.ayr1k12v and(not g5l8a78e):
   if wy0mahym==None:
    fdxj37c9=[]
    for i33e1i1p in uqjiujv6:
     if i33e1i1p=='n1p0vu':
      continue
     if i33e1i1p not in qxt6ridl:
      fdxj37c9.append(('cxf5x9',i33e1i1p))
    for i33e1i1p in qxt6ridl:
     if player.ejbzutru.get(i33e1i1p,1)<jdiuovw1:
      fdxj37c9.append(('mmgvu4',i33e1i1p))
    for k in cq5uznof:
     if player.m3hcws2w.get(k,0)<cq5uznof[k]['bdoz6w']:
      fdxj37c9.append(('y3lxch',k))
    if not fdxj37c9:
     player.ayr1k12v=False
    else:
     random.shuffle(fdxj37c9)
     zfb7r31q=fdxj37c9[:3]
     jm25len6=120*len(zfb7r31q)+20
     wy0mahym=wa11dpg8(400,jm25len6+wa11dpg8.gokc1msy,my6wktak,title='LEVEL UP! Choose an upgrade',title_font=zdan085r)
     aqclpoxk=jm25len6//len(zfb7r31q)
     xp8mgyn2=wy0mahym.f8rtm4j3.n01uyzpd+wy0mahym.v76ub7l8
     for(z8z3v6di,(kind,key))in enumerate(zfb7r31q):
      if kind=='cxf5x9':
       title=f'NEW WEAPON: {uyhl1c32[key]}'
       subtitle='Unlock this weapon'
      elif kind=='mmgvu4':
       fpa8hyex=player.ejbzutru.get(key,1)
       title=f'{uyhl1c32[key]}  Lv.{fpa8hyex} -> {fpa8hyex + 1}'
       subtitle='+12% damage, faster cooldown'
      else:
       fpa8hyex=player.m3hcws2w.get(key,0)
       title=f"{cq5uznof[key]['tudttj']}  Lv.{fpa8hyex} -> {fpa8hyex + 1}"
       subtitle=cq5uznof[key]['rthy25']
      rzs43c5b=hc58drc1(wy0mahym.f8rtm4j3.qxb7gbdg+12,xp8mgyn2+z8z3v6di*aqclpoxk+6,wy0mahym.f8rtm4j3.width-24,aqclpoxk-12,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,j2vmcqbn,title,12,subtitle=subtitle,sub_font=wd6r30oj,kind=kind,key=key)
      wy0mahym.add(rzs43c5b)
   if wy0mahym is not None:
    for wzlm72je in wy0mahym.ftlpq2wg:
     wzlm72je.update(zefqjg02)
     if wzlm72je.d1ieixwc:
      if wzlm72je.kind=='cxf5x9':
       qxt6ridl.append(wzlm72je.key)
       player.ejbzutru[wzlm72je.key]=1
       f8wquuy5[wzlm72je.key]=mjh75lxo[wzlm72je.key]
      elif wzlm72je.kind=='mmgvu4':
       player.v3e1ocjx(wzlm72je.key)
      elif wzlm72je.kind=='y3lxch':
       player.jmpioygg(wzlm72je.key)
      player.ayr1k12v=False
      wy0mahym=None
  uz6kf162(wc7x0h3j)
  (wc7x0h3j,uww5wfcp,izhwy9he)=uj64qhks(wc7x0h3j,uww5wfcp,izhwy9he,player,tnz61231,wfhj4d0j,gf8f3gr9)
  for(mlikwe4b,vm65q57t,l0sqg4ei,sfu38gl2)in player.wb7f6fdh:
   wfhj4d0j.append(e9y3z2t4(mlikwe4b,vm65q57t,l0sqg4ei,gf8f3gr9,color=sfu38gl2))
  player.wb7f6fdh.clear()
  kybwmlun=player.f8rtm4j3.qxb7gbdg-mqp49kwv//2
  i0x65muf=player.f8rtm4j3.n01uyzpd-rla5ju9b//2
  kybwmlun=max(min(kybwmlun,faqvkizz-mqp49kwv),0)
  i0x65muf=max(min(i0x65muf,xd1wjcit-rla5ju9b),0)
  fd6rupw2=tby49e7e=0
  if player.tj0nmeoq:
   player.myrp5ge0-=1
   fd6rupw2=random.randint(-oohp6vz4,oohp6vz4)
   tby49e7e=random.randint(-oohp6vz4,oohp6vz4)
   kybwmlun+=fd6rupw2
   i0x65muf+=tby49e7e
   if player.myrp5ge0<=0:
    player.tj0nmeoq=False
  gmoft6yr.fill(iq5c34dx['uq0e27'])
  gmoft6yr.blit(luzbikci,(0,0))
  elwf90km(gmoft6yr,kybwmlun,i0x65muf)
  for dzsedfqs in nd6357oo:
   dzsedfqs.do2m71hs(gmoft6yr,kybwmlun,i0x65muf)
  player.do2m71hs(gmoft6yr,kybwmlun,i0x65muf)
  for uidlrye8 in wc7x0h3j:
   uidlrye8.do2m71hs(gmoft6yr,kybwmlun,i0x65muf)
   for sk8yqk94 in uidlrye8.ia529603:
    sk8yqk94.do2m71hs(gmoft6yr,kybwmlun,i0x65muf)
  for u3ifhv1x in uww5wfcp:
   u3ifhv1x.do2m71hs(gmoft6yr,kybwmlun,i0x65muf)
  for iie0rnuj in izhwy9he:
   iie0rnuj.do2m71hs(gmoft6yr,kybwmlun,i0x65muf)
  for pf0i9g5d in mmn32u1i:
   pygame.draw.circle(gmoft6yr,pf0i9g5d['xy79kv'],(int(pf0i9g5d['buzery']-kybwmlun),int(pf0i9g5d['qc6dr0']-i0x65muf)),pf0i9g5d['mviifr'])
  for n64fgwje in wfhj4d0j:
   yuibrsz1(gmoft6yr,n64fgwje,kybwmlun,i0x65muf)
  for sygvwopl in tnz61231:
   sygvwopl.do2m71hs(gmoft6yr,kybwmlun,i0x65muf)
  if wy0mahym!=None:
   wy0mahym.do2m71hs(gmoft6yr)
  y06nkwfg=40+18*len(qxt6ridl)
  sl65wvjx(gmoft6yr,pygame.Rect(12,12,190,y06nkwfg))
  xo2t8fy6=g70e3p15.render(f'Enemies: {len(wc7x0h3j)}',True,(20,20,20))
  gmoft6yr.blit(xo2t8fy6,(20+fd6rupw2,20+tby49e7e))
  eq3tq1s0=50
  for i33e1i1p in qxt6ridl:
   fpa8hyex=player.ejbzutru.get(i33e1i1p,1)
   x9h0dxho=wd6r30oj.render(f'{uyhl1c32[i33e1i1p]} Lv.{fpa8hyex}',True,(30,30,30))
   gmoft6yr.blit(x9h0dxho,(20+fd6rupw2,eq3tq1s0+tby49e7e))
   eq3tq1s0+=18
  sl65wvjx(gmoft6yr,pygame.Rect(mqp49kwv-180,12,168,32))
  tkyrmjlj=wd6r30oj.render(f'Resources: {no0u93mz}',True,(20,20,20))
  gmoft6yr.blit(tkyrmjlj,(mqp49kwv-170+fd6rupw2,20+tby49e7e))
  if yw6zbnz8:
   jh55hewl=wd6r30oj.render('Opening chest... weapons offline!',True,iq5c34dx['sdypml'])
   gmoft6yr.blit(jh55hewl,(mqp49kwv//2-jh55hewl.get_width()//2+fd6rupw2,12+tby49e7e))
  sl65wvjx(gmoft6yr,pygame.Rect(12,rla5ju9b-50,388,38))
  rktlzkj4=title_font.render(f'Lv.{player.wvpw232u}',True,(20,20,20))
  gmoft6yr.blit(rktlzkj4,(20+fd6rupw2,rla5ju9b-40+tby49e7e))
  it04chsd=ocij2v2h[min(player.wvpw232u,len(ocij2v2h)-1)]
  htgsiwg0=min(1.0,player.bu4xszjn/it04chsd)
  qtzk3ny9(gmoft6yr,90,rla5ju9b-34,290,htgsiwg0,height=16,fg=iq5c34dx['t753ay'],bg=(70,70,70))
  if g5l8a78e:
   w8y72ivg=pygame.Surface((mqp49kwv,rla5ju9b),pygame.SRCALPHA)
   w8y72ivg.fill((0,0,0,150))
   gmoft6yr.blit(w8y72ivg,(0,0))
   xo2t8fy6=x03uvule.render('GAME OVER',True,iq5c34dx['xutxzb'])
   bdgbk2l0=x03uvule.render('GAME OVER',True,(0,0,0))
   (ruq9e5co,wzs13c9x)=(mqp49kwv//2-xo2t8fy6.get_width()//2,rla5ju9b//2-xo2t8fy6.get_height()//2)
   gmoft6yr.blit(bdgbk2l0,(ruq9e5co+2,wzs13c9x+2))
   gmoft6yr.blit(xo2t8fy6,(ruq9e5co,wzs13c9x))
   uoloeazc=g70e3p15.render(f'You reached Level {player.wvpw232u}  |  +{no0u93mz} resources',True,iq5c34dx['pta5iv'])
   gmoft6yr.blit(uoloeazc,(mqp49kwv//2-uoloeazc.get_width()//2,wzs13c9x+xo2t8fy6.get_height()+10))
   cb2uuijn=wd6r30oj.render('Press ENTER to return to the Homebase',True,iq5c34dx['pta5iv'])
   gmoft6yr.blit(cb2uuijn,(mqp49kwv//2-cb2uuijn.get_width()//2,wzs13c9x+xo2t8fy6.get_height()+40))
  if uos0fb4y:
   w8y72ivg=pygame.Surface((mqp49kwv,rla5ju9b),pygame.SRCALPHA)
   w8y72ivg.fill((0,0,0,150))
   gmoft6yr.blit(w8y72ivg,(0,0))
   xo2t8fy6=x03uvule.render(f'Get ready!',True,iq5c34dx['xutxzb'])
   bdgbk2l0=x03uvule.render(f'Get ready!',True,(0,0,0))
   (ruq9e5co,wzs13c9x)=(mqp49kwv//2-xo2t8fy6.get_width()//2,rla5ju9b//2-xo2t8fy6.get_height()//2)
   gmoft6yr.blit(bdgbk2l0,(ruq9e5co+2,wzs13c9x+2))
   gmoft6yr.blit(xo2t8fy6,(ruq9e5co,wzs13c9x))
   uoloeazc=g70e3p15.render(f'Game continuing in {uysal8m1}',True,iq5c34dx['pta5iv'])
   gmoft6yr.blit(uoloeazc,(mqp49kwv//2-uoloeazc.get_width()//2,wzs13c9x+xo2t8fy6.get_height()+10))
  if mfc79m96:
   w8y72ivg=pygame.Surface((mqp49kwv,rla5ju9b),pygame.SRCALPHA)
   w8y72ivg.fill((0,0,0,150))
   gmoft6yr.blit(w8y72ivg,(0,0))
   xo2t8fy6=x03uvule.render(f'Game Paused',True,iq5c34dx['xutxzb'])
   bdgbk2l0=x03uvule.render(f'Game Paused',True,(0,0,0))
   (ruq9e5co,wzs13c9x)=(mqp49kwv//2-xo2t8fy6.get_width()//2,rla5ju9b//2-xo2t8fy6.get_height()//2)
   gmoft6yr.blit(bdgbk2l0,(ruq9e5co+2,wzs13c9x+2))
   gmoft6yr.blit(xo2t8fy6,(ruq9e5co,wzs13c9x))
  pygame.display.flip()
  pvasifpw.tick(pi3qk2ia)
def pcvsqame():
 h4l1vznq=xsspye9r()
 if h4l1vznq is None:
  return
 nxxjve3d=n3rlkte4(h4l1vznq)
 def npejzhya(u1jhuwb6):
  xwk2rv23(h4l1vznq,u1jhuwb6)
 npejzhya(nxxjve3d)
 while True:
  win4olr6=jenvg3kk(gmoft6yr,pvasifpw,nxxjve3d,npejzhya)
  if win4olr6=='quit':
   break
  if win4olr6=='start_game':
   (rmm1zxyv,l3swebnv,tbxf445c)=k1taa0i5(nxxjve3d)
   nxxjve3d['resources']+=rmm1zxyv
   nxxjve3d['high_level']=max(nxxjve3d.get('high_level',0),l3swebnv)
   nxxjve3d['runs_played']=nxxjve3d.get('runs_played',0)+1
   npejzhya(nxxjve3d)
   if tbxf445c:
    break
if __name__=='__main__':
 pcvsqame()
