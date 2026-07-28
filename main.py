import pygame
from z4w1arag import*
from umjmbukd import*
from entities import*
from kyow8dt8 import*
from eba9in2x import*
from c41kht8x import h8s2ftom
from e1gnfiue import ub68rerv,pllkstn3,xxns2zyb,jsylztgx
from tgv3dr2h import myrp5ge0
import time
pygame.init()
cq2q4qer=pygame.display.set_mode((rrcbpljd,rla5ju9b))
clkqzfpq=pygame.time.Clock()
luzbikci=pygame.Surface((rrcbpljd,rla5ju9b),pygame.SRCALPHA)
for mnx39rbs in range(rla5ju9b):
 k44nlz15=mnx39rbs/max(1,rla5ju9b-1)
 m53a5qbs=int(45*(1-k44nlz15))
 pygame.draw.line(luzbikci,(235,245,250,m53a5qbs),(0,mnx39rbs),(rrcbpljd,mnx39rbs))
def rzewviyt(cq2q4qer,cqheyto5,j1i2hgj1=120,rgdej31g=10):
 p7b1ijiy=pygame.Surface((cqheyto5.width,cqheyto5.height),pygame.SRCALPHA)
 pygame.draw.rect(p7b1ijiy,(255,255,255,j1i2hgj1),p7b1ijiy.get_rect(),border_radius=rgdej31g)
 cq2q4qer.blit(p7b1ijiy,cqheyto5.topleft)
def fd6rupw2():
 title_font=pygame.font.SysFont('arial',40,bold=True)
 o9ros7yt=pygame.font.SysFont('arial',16)
 giec4d14=pygame.font.SysFont('arial',22,bold=True)
 mn89ltaj=pygame.font.SysFont('arial',15)
 qbm1enf3=[]
 for semqgy27 in range(1,jsylztgx+1):
  ysqg8x80=xxns2zyb(semqgy27)
  if ysqg8x80:
   subtitle=f"Level {ysqg8x80['high_level']}  |  {ysqg8x80['resources']} resources  |  {ysqg8x80['runs_played']} runs"
  else:
   subtitle='Empty - New Game'
  z0b6ugvs=hc58drc1(rrcbpljd//2-170,170+(semqgy27-1)*110,340,90,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,giec4d14,f'Slot {semqgy27}',12,subtitle=subtitle,sub_font=mn89ltaj,kind='slot',key=semqgy27)
  qbm1enf3.append(z0b6ugvs)
 while True:
  ouuylaja=pygame.event.get()
  for vhuds3qs in ouuylaja:
   if vhuds3qs.type==pygame.QUIT:
    return None
  for z0b6ugvs in qbm1enf3:
   z0b6ugvs.update(ouuylaja)
   if z0b6ugvs.i20cv3tl:
    return z0b6ugvs.key
  cq2q4qer.fill(iq5c34dx['wkgeq2'])
  vm65q57t=title_font.render('CHASE GAME',True,(20,20,40))
  cq2q4qer.blit(vm65q57t,(rrcbpljd//2-vm65q57t.get_width()//2,70))
  nyfkjfpn=o9ros7yt.render('Choose a save slot',True,(30,30,30))
  cq2q4qer.blit(nyfkjfpn,(rrcbpljd//2-nyfkjfpn.get_width()//2,135))
  for z0b6ugvs in qbm1enf3:
   z0b6ugvs.g8kk791z(cq2q4qer)
  pygame.display.flip()
  clkqzfpq.tick(pi3qk2ia)
def tj0nmeoq(tbxf445c):
 yrivh6t1=pygame.font.SysFont('arial',28)
 g11kerpe=pygame.font.SysFont('arial',48)
 mn89ltaj=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',20,bold=True)
 co4busu9=pygame.font.SysFont('arial',24,bold=True)
 giec4d14=pygame.font.SysFont('arial',22,bold=True)
 njka34mq=pygame.font.SysFont('arial',16,bold=True)
 player=yur7ko64(meta_upgrades=tbxf445c.get('meta_upgrades',{}))
 mygfliji=[]
 uysal8m1=[]
 ee1g983e=[]
 ugez7bh2=[]
 vw6m7b5c=[]
 g70e3p15=[]
 zanouof0=[]
 f2voi8uy=[c8yfbntp[0]]
 wvndfdw7=['pqpva5']
 player.hhl1737s['pqpva5']=1
 fddfgs3j=False
 x6cnoljq=False
 oqse3tv1=False
 zfb7r31q=3
 xvzc7d2k=time.time()
 l3swebnv=player.bokzixza
 xasez2nx=0
 zgomf9pm=bom5igqp*pi3qk2ia
 u23y30ys=dict(mjh75lxo)
 m3pt5r5r=None
 a2wspofv=hc58drc1(rrcbpljd-40,rla5ju9b-40,30,30,n2vlpys2,cq5uznof,z0xkxwd8,hyihair4,mn89ltaj,'| |',15)
 while True:
  ouuylaja=pygame.event.get()
  for vhuds3qs in ouuylaja:
   if vhuds3qs.type==pygame.QUIT:
    return(xasez2nx,player.bokzixza,True)
   if fddfgs3j and vhuds3qs.type==pygame.KEYDOWN and(vhuds3qs.key in(pygame.K_RETURN,pygame.K_SPACE)):
    return(xasez2nx,player.bokzixza,False)
   if vhuds3qs.type==pygame.KEYDOWN:
    if vhuds3qs.key==pygame.K_p and(not oqse3tv1):
     if x6cnoljq:
      a2wspofv.z7pwo6cm='| |'
     else:
      a2wspofv.z7pwo6cm='X'
     if x6cnoljq:
      oqse3tv1=True
      zfb7r31q=3
      xvzc7d2k=time.time()
     x6cnoljq=not x6cnoljq
  pvasifpw=False
  if oqse3tv1:
   if time.time()-xvzc7d2k>=1:
    xvzc7d2k=time.time()
    zfb7r31q-=1
    if zfb7r31q<=0:
     oqse3tv1=False
     zfb7r31q=3
  if not player.r212pgym and(not fddfgs3j)and(not x6cnoljq)and(not oqse3tv1):
   for ebt3g2qz in ugez7bh2[:]:
    ftrflqbm=ebt3g2qz.update(player)
    if ftrflqbm:
     pvasifpw=True
    if ebt3g2qz.pf0i9g5d:
     nxxjve3d=random.randint(re7ur23g,uccblskr)
     xasez2nx+=nxxjve3d
     for v83tqll8 in range(10):
      ee1g983e.append(y9ayq6ww([iq5c34dx['amyrsv'],iq5c34dx['yl4zjd']],2,4,-3,3,ebt3g2qz.cqheyto5.centerx,ebt3g2qz.cqheyto5.centery,life=30))
     ugez7bh2.remove(ebt3g2qz)
   zgomf9pm-=1
   if zgomf9pm<=0:
    zgomf9pm=bom5igqp*pi3qk2ia
    if len(ugez7bh2)<r1yzoyn6:
     ugez7bh2.append(h8s2ftom(player))
   if not pvasifpw:
    for kt94ow3l in wvndfdw7:
     u23y30ys[kt94ow3l]-=1
     if u23y30ys[kt94ow3l]<=0:
      s7fbmenu=player.hhl1737s.get(kt94ow3l,1)
      li9nb74x=mjh75lxo[kt94ow3l]*player.f2sehe2a*huh17j8q(s7fbmenu)
      u23y30ys[kt94ow3l]=max(4,int(li9nb74x))
      kz1uu7zy=uqjiujv6[kt94ow3l]['pcs4ke']
      rmm1zxyv=player.pa8s8hmb*mabkae6a(s7fbmenu)
      uysal8m1.append(r0tvhhpb(kt94ow3l,player.cqheyto5.centerx-kz1uu7zy//2,player.cqheyto5.centery-kz1uu7zy//2,kz1uu7zy,kz1uu7zy,player.swwnc21o['w2lx2t'],player.swwnc21o['mviifr'],rmm1zxyv))
   uwxrum2l=min(isj6bw3b,d60fkhmy*(1+0.12*(player.bokzixza-1)))
   if random.random()<uwxrum2l:
    gxlk8wru(mygfliji,f2voi8uy)
   player.chx3d43e()
   if player.bokzixza>l3swebnv:
    if player.bokzixza<=len(c8yfbntp):
     fdxj37c9=c8yfbntp[player.bokzixza-1]
     if fdxj37c9 not in f2voi8uy:
      f2voi8uy.append(fdxj37c9)
    l3swebnv=player.bokzixza
   if player.a8lw2lm3<=0:
    fddfgs3j=True
   for velos6zl in mygfliji:
    velos6zl.chx3d43e(player)
    for pa5u6hc3 in velos6zl.reqy08p0:
     pa5u6hc3.chx3d43e(player)
     pa5u6hc3.lcj883dh(mygfliji,ee1g983e,uysal8m1,player=player,target='player')
    velos6zl.reqy08p0=[jmpioygg for jmpioygg in velos6zl.reqy08p0 if not jmpioygg.qbbz2sf6]
   for iektsg7f in vw6m7b5c:
    iektsg7f.chx3d43e(player)
   for llxxezdu in uysal8m1:
    llxxezdu.chx3d43e(player,mc8qizk3(mygfliji,llxxezdu))
    llxxezdu.lcj883dh(mygfliji,ee1g983e,uysal8m1)
   for velos6zl in mygfliji:
    for(pbo119xp,boih5csk,v15cqzcu,jqxs6esj)in velos6zl.y8dd2255:
     zanouof0.append(qxt6ridl(pbo119xp,boih5csk,v15cqzcu,njka34mq,color=jqxs6esj))
    velos6zl.y8dd2255.clear()
   for wydmt8vt in ee1g983e[:]:
    wydmt8vt['yc1nlc']+=wydmt8vt['w2lx2t']
    wydmt8vt['urf1hx']+=wydmt8vt['mviifr']
    wydmt8vt['cxf5x9']-=1
    if wydmt8vt['cxf5x9']<=0:
     ee1g983e.remove(wydmt8vt)
   for mnx4sn6s in zanouof0[:]:
    mnx4sn6s['cxf5x9']-=1
    if mnx4sn6s['cxf5x9']<=0:
     zanouof0.remove(mnx4sn6s)
   for gubmc97c in g70e3p15[:]:
    gubmc97c.update()
    if gubmc97c.qbbz2sf6():
     g70e3p15.remove(gubmc97c)
  if player.r212pgym and(not fddfgs3j):
   if m3pt5r5r==None:
    wy0mahym=[]
    for ucu7onz3 in uqjiujv6:
     if ucu7onz3=='t753ay':
      continue
     if ucu7onz3 not in wvndfdw7:
      wy0mahym.append(('gbwcv6',ucu7onz3))
    for ucu7onz3 in wvndfdw7:
     if player.hhl1737s.get(ucu7onz3,1)<x37pqkoj:
      wy0mahym.append(('dzjq7w',ucu7onz3))
    for k in rqf5q14j:
     if player.rm0j36tc.get(k,0)<rqf5q14j[k]['t7wqp3']:
      wy0mahym.append(('hx0gu4',k))
    if not wy0mahym:
     player.r212pgym=False
    else:
     random.shuffle(wy0mahym)
     jm25len6=wy0mahym[:3]
     cq6qdy4l=120*len(jm25len6)+20
     m3pt5r5r=yswjckjl(400,cq6qdy4l+yswjckjl.gokc1msy,my6wktak,title='LEVEL UP! Choose an upgrade',title_font=co4busu9)
     bq349dxb=cq6qdy4l//len(jm25len6)
     lztkkfzz=m3pt5r5r.cqheyto5.nngmx1gm+m3pt5r5r.cn7zrwqe
     for(semqgy27,(kind,key))in enumerate(jm25len6):
      if kind=='gbwcv6':
       title=f'NEW WEAPON: {uyhl1c32[key]}'
       subtitle='Unlock this weapon'
      elif kind=='dzjq7w':
       ry181acj=player.hhl1737s.get(key,1)
       title=f'{uyhl1c32[key]}  Lv.{ry181acj} -> {ry181acj + 1}'
       subtitle='+12% damage, faster cooldown'
      else:
       ry181acj=player.rm0j36tc.get(key,0)
       title=f"{rqf5q14j[key]['ntxrgn']}  Lv.{ry181acj} -> {ry181acj + 1}"
       subtitle=rqf5q14j[key]['fkmuso']
      z0b6ugvs=hc58drc1(m3pt5r5r.cqheyto5.d5ixva1n+12,lztkkfzz+semqgy27*bq349dxb+6,m3pt5r5r.cqheyto5.width-24,bq349dxb-12,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,giec4d14,title,12,subtitle=subtitle,sub_font=mn89ltaj,kind=kind,key=key)
      m3pt5r5r.add(z0b6ugvs)
   if m3pt5r5r is not None:
    for zefqjg02 in m3pt5r5r.i13n3bzt:
     zefqjg02.update(ouuylaja)
     if zefqjg02.i20cv3tl:
      if zefqjg02.kind=='gbwcv6':
       wvndfdw7.append(zefqjg02.key)
       player.hhl1737s[zefqjg02.key]=1
       u23y30ys[zefqjg02.key]=mjh75lxo[zefqjg02.key]
      elif zefqjg02.kind=='dzjq7w':
       player.nyrid3dn(zefqjg02.key)
      elif zefqjg02.kind=='hx0gu4':
       player.x52qc1iy(zefqjg02.key)
      player.r212pgym=False
      m3pt5r5r=None
  xsspye9r(mygfliji)
  a2wspofv.update(ouuylaja)
  if a2wspofv.i20cv3tl and(not oqse3tv1):
   if x6cnoljq:
    a2wspofv.z7pwo6cm='| |'
   else:
    a2wspofv.z7pwo6cm='X'
   if x6cnoljq:
    oqse3tv1=True
    zfb7r31q=3
    xvzc7d2k=time.time()
   x6cnoljq=not x6cnoljq
  (mygfliji,uysal8m1,vw6m7b5c)=upprat08(mygfliji,uysal8m1,vw6m7b5c,player,g70e3p15,zanouof0,njka34mq)
  for(j7f00ter,jh55hewl,kc1fjotg,nabufwbu)in player.y8dd2255:
   zanouof0.append(qxt6ridl(j7f00ter,jh55hewl,kc1fjotg,njka34mq,color=nabufwbu))
  player.y8dd2255.clear()
  f32ejx5t=player.cqheyto5.d5ixva1n-rrcbpljd//2
  dzsedfqs=player.cqheyto5.nngmx1gm-rla5ju9b//2
  f32ejx5t=max(min(f32ejx5t,ygspk9p3-rrcbpljd),0)
  dzsedfqs=max(min(dzsedfqs,v4u89yjb-rla5ju9b),0)
  nbwye6qv=qertb74r=0
  if player.wd6r30oj:
   player.gg7oq2zd-=1
   nbwye6qv=random.randint(-cq0b8ic8,cq0b8ic8)
   qertb74r=random.randint(-cq0b8ic8,cq0b8ic8)
   f32ejx5t+=nbwye6qv
   dzsedfqs+=qertb74r
   if player.gg7oq2zd<=0:
    player.wd6r30oj=False
  cq2q4qer.fill(iq5c34dx['wkgeq2'])
  cq2q4qer.blit(luzbikci,(0,0))
  vt6om1fb(cq2q4qer,f32ejx5t,dzsedfqs)
  for ebt3g2qz in ugez7bh2:
   ebt3g2qz.g8kk791z(cq2q4qer,f32ejx5t,dzsedfqs)
  player.g8kk791z(cq2q4qer,f32ejx5t,dzsedfqs)
  for velos6zl in mygfliji:
   velos6zl.g8kk791z(cq2q4qer,f32ejx5t,dzsedfqs)
   for pa5u6hc3 in velos6zl.reqy08p0:
    pa5u6hc3.g8kk791z(cq2q4qer,f32ejx5t,dzsedfqs)
  for llxxezdu in uysal8m1:
   llxxezdu.g8kk791z(cq2q4qer,f32ejx5t,dzsedfqs)
  for iektsg7f in vw6m7b5c:
   iektsg7f.g8kk791z(cq2q4qer,f32ejx5t,dzsedfqs)
  for wydmt8vt in ee1g983e:
   pygame.draw.circle(cq2q4qer,wydmt8vt['k1yjfe'],(int(wydmt8vt['yc1nlc']-f32ejx5t),int(wydmt8vt['urf1hx']-dzsedfqs)),wydmt8vt['pcs4ke'])
  for mnx4sn6s in zanouof0:
   uidlrye8(cq2q4qer,mnx4sn6s,f32ejx5t,dzsedfqs)
  for gubmc97c in g70e3p15:
   gubmc97c.g8kk791z(cq2q4qer,f32ejx5t,dzsedfqs)
  if m3pt5r5r!=None:
   m3pt5r5r.g8kk791z(cq2q4qer)
  jdqqzrlf=40+18*len(wvndfdw7)
  rzewviyt(cq2q4qer,pygame.Rect(12,12,190,jdqqzrlf))
  p7b1ijiy=yrivh6t1.render(f'Enemies: {len(mygfliji)}',True,(20,20,20))
  cq2q4qer.blit(p7b1ijiy,(20+nbwye6qv,20+qertb74r))
  hjkuuhcl=50
  for ucu7onz3 in wvndfdw7:
   ry181acj=player.hhl1737s.get(ucu7onz3,1)
   it04chsd=mn89ltaj.render(f'{uyhl1c32[ucu7onz3]} Lv.{ry181acj}',True,(30,30,30))
   cq2q4qer.blit(it04chsd,(20+nbwye6qv,hjkuuhcl+qertb74r))
   hjkuuhcl+=18
  rzewviyt(cq2q4qer,pygame.Rect(rrcbpljd-180,12,168,32))
  jenvg3kk=mn89ltaj.render(f'Resources: {xasez2nx}',True,(20,20,20))
  cq2q4qer.blit(jenvg3kk,(rrcbpljd-170+nbwye6qv,20+qertb74r))
  if pvasifpw:
   n01uyzpd=mn89ltaj.render('Opening chest... weapons offline!',True,iq5c34dx['dg4fbl'])
   cq2q4qer.blit(n01uyzpd,(rrcbpljd//2-n01uyzpd.get_width()//2+nbwye6qv,12+qertb74r))
  rzewviyt(cq2q4qer,pygame.Rect(12,rla5ju9b-50,388,38))
  pcvsqame=title_font.render(f'Lv.{player.bokzixza}',True,(20,20,20))
  cq2q4qer.blit(pcvsqame,(20+nbwye6qv,rla5ju9b-40+qertb74r))
  e1rhouu9=cqoldfor[min(player.bokzixza,len(cqoldfor)-1)]
  qic1l7dy=min(1.0,player.jslulzfy/e1rhouu9)
  wc7x0h3j(cq2q4qer,90,rla5ju9b-34,290,qic1l7dy,height=16,fg=iq5c34dx['amyrsv'],bg=(70,70,70))
  if fddfgs3j:
   trdhw9re=pygame.Surface((rrcbpljd,rla5ju9b),pygame.SRCALPHA)
   trdhw9re.fill((0,0,0,150))
   cq2q4qer.blit(trdhw9re,(0,0))
   p7b1ijiy=g11kerpe.render('GAME OVER',True,iq5c34dx['dzjssz'])
   h4l1vznq=g11kerpe.render('GAME OVER',True,(0,0,0))
   (l9enulqj,hfb85p86)=(rrcbpljd//2-p7b1ijiy.get_width()//2,rla5ju9b//2-p7b1ijiy.get_height()//2)
   cq2q4qer.blit(h4l1vznq,(l9enulqj+2,hfb85p86+2))
   cq2q4qer.blit(p7b1ijiy,(l9enulqj,hfb85p86))
   u1ni10kq=yrivh6t1.render(f'You reached Level {player.bokzixza}  |  +{xasez2nx} resources',True,iq5c34dx['lcf4mn'])
   cq2q4qer.blit(u1ni10kq,(rrcbpljd//2-u1ni10kq.get_width()//2,hfb85p86+p7b1ijiy.get_height()+10))
   su1hbj6t=mn89ltaj.render('Press ENTER to return to the Homebase',True,iq5c34dx['lcf4mn'])
   cq2q4qer.blit(su1hbj6t,(rrcbpljd//2-su1hbj6t.get_width()//2,hfb85p86+p7b1ijiy.get_height()+40))
  if oqse3tv1:
   trdhw9re=pygame.Surface((rrcbpljd,rla5ju9b),pygame.SRCALPHA)
   trdhw9re.fill((0,0,0,150))
   cq2q4qer.blit(trdhw9re,(0,0))
   p7b1ijiy=g11kerpe.render(f'Get ready!',True,iq5c34dx['dzjssz'])
   h4l1vznq=g11kerpe.render(f'Get ready!',True,(0,0,0))
   (l9enulqj,hfb85p86)=(rrcbpljd//2-p7b1ijiy.get_width()//2,rla5ju9b//2-p7b1ijiy.get_height()//2)
   cq2q4qer.blit(h4l1vznq,(l9enulqj+2,hfb85p86+2))
   cq2q4qer.blit(p7b1ijiy,(l9enulqj,hfb85p86))
   u1ni10kq=yrivh6t1.render(f'Game continuing in {zfb7r31q}',True,iq5c34dx['lcf4mn'])
   cq2q4qer.blit(u1ni10kq,(rrcbpljd//2-u1ni10kq.get_width()//2,hfb85p86+p7b1ijiy.get_height()+10))
  if x6cnoljq:
   trdhw9re=pygame.Surface((rrcbpljd,rla5ju9b),pygame.SRCALPHA)
   trdhw9re.fill((0,0,0,150))
   cq2q4qer.blit(trdhw9re,(0,0))
   p7b1ijiy=g11kerpe.render(f'Game Paused',True,iq5c34dx['dzjssz'])
   h4l1vznq=g11kerpe.render(f'Game Paused',True,(0,0,0))
   (l9enulqj,hfb85p86)=(rrcbpljd//2-p7b1ijiy.get_width()//2,rla5ju9b//2-p7b1ijiy.get_height()//2)
   cq2q4qer.blit(h4l1vznq,(l9enulqj+2,hfb85p86+2))
   cq2q4qer.blit(p7b1ijiy,(l9enulqj,hfb85p86))
  a2wspofv.g8kk791z(cq2q4qer)
  pygame.display.flip()
  clkqzfpq.tick(pi3qk2ia)
def zflv1xxl():
 g1b3d505=fd6rupw2()
 if g1b3d505 is None:
  return
 tbxf445c=ub68rerv(g1b3d505)
 def v0rxxf36(do2m71hs):
  pllkstn3(g1b3d505,do2m71hs)
 v0rxxf36(tbxf445c)
 while True:
  sk8yqk94=myrp5ge0(cq2q4qer,clkqzfpq,tbxf445c,v0rxxf36)
  if sk8yqk94=='quit':
   break
  if sk8yqk94=='start_game':
   (x875aud9,ljk4q5v7,wtl0thhz)=tj0nmeoq(tbxf445c)
   tbxf445c['resources']+=x875aud9
   tbxf445c['high_level']=max(tbxf445c.get('high_level',0),ljk4q5v7)
   tbxf445c['runs_played']=tbxf445c.get('runs_played',0)+1
   v0rxxf36(tbxf445c)
   if wtl0thhz:
    break
if __name__=='__main__':
 zflv1xxl()
