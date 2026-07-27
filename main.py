import pygame
from i1arxabo import*
from tbzegbl2 import*
from entities import*
from riyojtpk import*
from o100vhmy import*
from zqy8yb7w import rk43safy
from nhx6zdcu import bokzixza,d46aexl6,q26yg3dx,jsylztgx
from uq91yy1j import npejzhya
import time
pygame.init()
tj0nmeoq=pygame.display.set_mode((dtx63cfl,rla5ju9b))
ebt3g2qz=pygame.time.Clock()
luzbikci=pygame.Surface((dtx63cfl,rla5ju9b),pygame.SRCALPHA)
for wkzorqqf in range(rla5ju9b):
 zs3kkv9r=wkzorqqf/max(1,rla5ju9b-1)
 cqoldfor=int(45*(1-zs3kkv9r))
 pygame.draw.line(luzbikci,(235,245,250,cqoldfor),(0,wkzorqqf),(dtx63cfl,wkzorqqf))
def wehlxslg(tj0nmeoq,todsx4nx,jmpioygg=120,vhxs58yr=10):
 jyjhu8my=pygame.Surface((todsx4nx.width,todsx4nx.height),pygame.SRCALPHA)
 pygame.draw.rect(jyjhu8my,(255,255,255,jmpioygg),jyjhu8my.get_rect(),border_radius=vhxs58yr)
 tj0nmeoq.blit(jyjhu8my,todsx4nx.topleft)
def nxxjve3d():
 title_font=pygame.font.SysFont('arial',40,bold=True)
 cn7zrwqe=pygame.font.SysFont('arial',16)
 wppsfnko=pygame.font.SysFont('arial',22,bold=True)
 t5sn961j=pygame.font.SysFont('arial',15)
 kybwmlun=[]
 for jo8e7flq in range(1,jsylztgx+1):
  v24479qt=q26yg3dx(jo8e7flq)
  if v24479qt:
   subtitle=f"Level {v24479qt['high_level']}  |  {v24479qt['resources']} resources  |  {v24479qt['runs_played']} runs"
  else:
   subtitle='Empty - New Game'
  fcwtg1m8=hc58drc1(dtx63cfl//2-170,170+(jo8e7flq-1)*110,340,90,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,wppsfnko,f'Slot {jo8e7flq}',12,subtitle=subtitle,sub_font=t5sn961j,kind='slot',key=jo8e7flq)
  kybwmlun.append(fcwtg1m8)
 while True:
  velos6zl=pygame.event.get()
  for yjluujmi in velos6zl:
   if yjluujmi.type==pygame.QUIT:
    return None
  for fcwtg1m8 in kybwmlun:
   fcwtg1m8.update(velos6zl)
   if fcwtg1m8.amcixdu1:
    return fcwtg1m8.key
  tj0nmeoq.fill(iq5c34dx['jl1qwe'])
  wfhj4d0j=title_font.render('CHASE GAME',True,(20,20,40))
  tj0nmeoq.blit(wfhj4d0j,(dtx63cfl//2-wfhj4d0j.get_width()//2,70))
  fekrcppr=cn7zrwqe.render('Choose a save slot',True,(30,30,30))
  tj0nmeoq.blit(fekrcppr,(dtx63cfl//2-fekrcppr.get_width()//2,135))
  for fcwtg1m8 in kybwmlun:
   fcwtg1m8.sl65wvjx(tj0nmeoq)
  pygame.display.flip()
  ebt3g2qz.tick(pi3qk2ia)
def ytb9xxay(bdgbk2l0):
 qhkc856w=pygame.font.SysFont('arial',28)
 ra73jgzl=pygame.font.SysFont('arial',48)
 t5sn961j=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',20,bold=True)
 wb7f6fdh=pygame.font.SysFont('arial',24,bold=True)
 wppsfnko=pygame.font.SysFont('arial',22,bold=True)
 y06nkwfg=pygame.font.SysFont('arial',16,bold=True)
 player=yur7ko64(meta_upgrades=bdgbk2l0.get('meta_upgrades',{}))
 uc1xi04b=[]
 bq349dxb=[]
 got7txkd=[]
 d1ieixwc=[]
 ruq9e5co=[]
 ouuylaja=[]
 klkjxjq5=[]
 m3hcws2w=[c8yfbntp[0]]
 wyk03o4g=['xutxzb']
 player.qxb7gbdg['xutxzb']=1
 eatvzkhi=False
 trdhw9re=False
 izhwy9he=False
 tk0qtl3q=3
 h8s2ftom=time.time()
 a2wspofv=player.swwnc21o
 cqheyto5=0
 rm0j36tc=bom5igqp*pi3qk2ia
 z0b6ugvs=dict(mjh75lxo)
 mfc79m96=None
 zorxdtg5=hc58drc1(dtx63cfl-40,rla5ju9b-40,30,30,n2vlpys2,cq5uznof,z0xkxwd8,hyihair4,t5sn961j,'| |',15)
 while True:
  velos6zl=pygame.event.get()
  for yjluujmi in velos6zl:
   if yjluujmi.type==pygame.QUIT:
    return(cqheyto5,player.swwnc21o,True)
   if eatvzkhi and yjluujmi.type==pygame.KEYDOWN and(yjluujmi.key in(pygame.K_RETURN,pygame.K_SPACE)):
    return(cqheyto5,player.swwnc21o,False)
   if yjluujmi.type==pygame.KEYDOWN:
    if yjluujmi.key==pygame.K_p and(not izhwy9he):
     if trdhw9re:
      izhwy9he=True
      tk0qtl3q=3
      h8s2ftom=time.time()
     trdhw9re=not trdhw9re
  dzsedfqs=False
  if izhwy9he:
   if time.time()-h8s2ftom>=1:
    h8s2ftom=time.time()
    tk0qtl3q-=1
    if tk0qtl3q<=0:
     izhwy9he=False
     tk0qtl3q=3
  if not player.ra9kepad and(not eatvzkhi)and(not trdhw9re)and(not izhwy9he):
   for tacj4t0s in d1ieixwc[:]:
    ftlpq2wg=tacj4t0s.update(player)
    if ftlpq2wg:
     dzsedfqs=True
    if tacj4t0s.s8438tgb:
     g1g1r1dw=random.randint(re7ur23g,uccblskr)
     cqheyto5+=g1g1r1dw
     for ygspk9p3 in range(10):
      got7txkd.append(g1b3d505([iq5c34dx['wdl5tg'],iq5c34dx['tcu9td']],2,4,-3,3,tacj4t0s.todsx4nx.centerx,tacj4t0s.todsx4nx.centery,life=30))
     d1ieixwc.remove(tacj4t0s)
   rm0j36tc-=1
   if rm0j36tc<=0:
    rm0j36tc=bom5igqp*pi3qk2ia
    if len(d1ieixwc)<r1yzoyn6:
     d1ieixwc.append(rk43safy(player))
   if not dzsedfqs:
    for eq3tq1s0 in wyk03o4g:
     z0b6ugvs[eq3tq1s0]-=1
     if z0b6ugvs[eq3tq1s0]<=0:
      bu4xszjn=player.qxb7gbdg.get(eq3tq1s0,1)
      yw6zbnz8=mjh75lxo[eq3tq1s0]*player.obc2nnuv*awnwlc83(bu4xszjn)
      z0b6ugvs[eq3tq1s0]=max(4,int(yw6zbnz8))
      wd6r30oj=uqjiujv6[eq3tq1s0]['eqkwqh']
      qtzk3ny9=player.u1jhuwb6*gsrtwlxd(bu4xszjn)
      bq349dxb.append(r0tvhhpb(eq3tq1s0,player.todsx4nx.centerx-wd6r30oj//2,player.todsx4nx.centery-wd6r30oj//2,wd6r30oj,wd6r30oj,player.i13n3bzt['v9hbn5'],player.i13n3bzt['da7yvd'],qtzk3ny9))
   kz1uu7zy=min(isj6bw3b,d60fkhmy*(1+0.12*(player.swwnc21o-1)))
   if random.random()<kz1uu7zy:
    gj29yfc2(uc1xi04b,m3hcws2w)
   player.mcup8ijl()
   if player.swwnc21o>a2wspofv:
    if player.swwnc21o<=len(c8yfbntp):
     mnwxuj3a=c8yfbntp[player.swwnc21o-1]
     if mnwxuj3a not in m3hcws2w:
      m3hcws2w.append(mnwxuj3a)
    a2wspofv=player.swwnc21o
   if player.mpyxdw2z<=0:
    eatvzkhi=True
   for x875aud9 in uc1xi04b:
    x875aud9.mcup8ijl(player)
    for yx4w6xlp in x875aud9.lt63j3r3:
     yx4w6xlp.mcup8ijl(player)
     yx4w6xlp.on0jnwny(uc1xi04b,got7txkd,bq349dxb,player=player,target='player')
    x875aud9.lt63j3r3=[mnx39rbs for mnx39rbs in x875aud9.lt63j3r3 if not mnx39rbs.k7zgf9q5]
   for f2sehe2a in ruq9e5co:
    f2sehe2a.mcup8ijl(player)
   for jc54wsqt in bq349dxb:
    jc54wsqt.mcup8ijl(player,s4rxyj38(uc1xi04b,jc54wsqt))
    jc54wsqt.on0jnwny(uc1xi04b,got7txkd,bq349dxb)
   for x875aud9 in uc1xi04b:
    for(tnz61231,pbo119xp,sygvwopl,rzewviyt)in x875aud9.lgbpj4uf:
     klkjxjq5.append(guxt9kls(tnz61231,pbo119xp,sygvwopl,y06nkwfg,color=rzewviyt))
    x875aud9.lgbpj4uf.clear()
   for oc4kl8cg in got7txkd[:]:
    oc4kl8cg['fuxk0a']+=oc4kl8cg['v9hbn5']
    oc4kl8cg['ijj0v6']+=oc4kl8cg['da7yvd']
    oc4kl8cg['i6ozx2']-=1
    if oc4kl8cg['i6ozx2']<=0:
     got7txkd.remove(oc4kl8cg)
   for w0p4e05q in klkjxjq5[:]:
    w0p4e05q['i6ozx2']-=1
    if w0p4e05q['i6ozx2']<=0:
     klkjxjq5.remove(w0p4e05q)
   for dw7nh8rq in ouuylaja[:]:
    dw7nh8rq.update()
    if dw7nh8rq.k7zgf9q5():
     ouuylaja.remove(dw7nh8rq)
  if player.ra9kepad and(not eatvzkhi):
   if mfc79m96==None:
    bihsa7he=[]
    for wvndfdw7 in uqjiujv6:
     if wvndfdw7=='s7002g':
      continue
     if wvndfdw7 not in wyk03o4g:
      bihsa7he.append(('qc6dr0',wvndfdw7))
    for wvndfdw7 in wyk03o4g:
     if player.qxb7gbdg.get(wvndfdw7,1)<ocij2v2h:
      bihsa7he.append(('kp82kb',wvndfdw7))
    for k in rqf5q14j:
     if player.kc1fjotg.get(k,0)<rqf5q14j[k]['fkmuso']:
      bihsa7he.append(('hpvwzo',k))
    if not bihsa7he:
     player.ra9kepad=False
    else:
     random.shuffle(bihsa7he)
     hugysm8t=bihsa7he[:3]
     x5m9j98c=120*len(hugysm8t)+20
     mfc79m96=yswjckjl(400,x5m9j98c+yswjckjl.gokc1msy,my6wktak,title='LEVEL UP! Choose an upgrade',title_font=wb7f6fdh)
     u3ifhv1x=x5m9j98c//len(hugysm8t)
     uos0fb4y=mfc79m96.todsx4nx.hhl1737s+mfc79m96.m8lw2qit
     for(jo8e7flq,(kind,key))in enumerate(hugysm8t):
      if kind=='qc6dr0':
       title=f'NEW WEAPON: {uyhl1c32[key]}'
       subtitle='Unlock this weapon'
      elif kind=='kp82kb':
       nyrid3dn=player.qxb7gbdg.get(key,1)
       title=f'{uyhl1c32[key]}  Lv.{nyrid3dn} -> {nyrid3dn + 1}'
       subtitle='+12% damage, faster cooldown'
      else:
       nyrid3dn=player.kc1fjotg.get(key,0)
       title=f"{rqf5q14j[key]['w1q8f6']}  Lv.{nyrid3dn} -> {nyrid3dn + 1}"
       subtitle=rqf5q14j[key]['j1f537']
      fcwtg1m8=hc58drc1(mfc79m96.todsx4nx.htgsiwg0+12,uos0fb4y+jo8e7flq*u3ifhv1x+6,mfc79m96.todsx4nx.width-24,u3ifhv1x-12,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,wppsfnko,title,12,subtitle=subtitle,sub_font=t5sn961j,kind=kind,key=key)
      mfc79m96.add(fcwtg1m8)
   if mfc79m96 is not None:
    for uidlrye8 in mfc79m96.semqgy27:
     uidlrye8.update(velos6zl)
     if uidlrye8.amcixdu1:
      if uidlrye8.kind=='qc6dr0':
       wyk03o4g.append(uidlrye8.key)
       player.qxb7gbdg[uidlrye8.key]=1
       z0b6ugvs[uidlrye8.key]=mjh75lxo[uidlrye8.key]
      elif uidlrye8.kind=='kp82kb':
       player.xd8wz42o(uidlrye8.key)
      elif uidlrye8.kind=='hpvwzo':
       player.diuu9k9x(uidlrye8.key)
      player.ra9kepad=False
      mfc79m96=None
  v6xii5p5(uc1xi04b)
  zorxdtg5.update(velos6zl)
  if zorxdtg5.amcixdu1 and(not izhwy9he):
   if trdhw9re:
    zorxdtg5.o9zqyahu='| |'
   else:
    zorxdtg5.o9zqyahu='X'
   if trdhw9re:
    izhwy9he=True
    tk0qtl3q=3
    h8s2ftom=time.time()
   trdhw9re=not trdhw9re
  (uc1xi04b,bq349dxb,ruq9e5co)=no0u93mz(uc1xi04b,bq349dxb,ruq9e5co,player,ouuylaja,klkjxjq5,y06nkwfg)
  for(ayr1k12v,zanouof0,e8zgvwwu,u1ni10kq)in player.lgbpj4uf:
   klkjxjq5.append(guxt9kls(ayr1k12v,zanouof0,e8zgvwwu,y06nkwfg,color=u1ni10kq))
  player.lgbpj4uf.clear()
  uysal8m1=player.todsx4nx.htgsiwg0-dtx63cfl//2
  giec4d14=player.todsx4nx.hhl1737s-rla5ju9b//2
  uysal8m1=max(min(uysal8m1,rrcbpljd-dtx63cfl),0)
  giec4d14=max(min(giec4d14,x37pqkoj-rla5ju9b),0)
  tbxf445c=pllkstn3=0
  if player.xu9ymszd:
   player.v0rxxf36-=1
   tbxf445c=random.randint(-mvxdp5gj,mvxdp5gj)
   pllkstn3=random.randint(-mvxdp5gj,mvxdp5gj)
   uysal8m1+=tbxf445c
   giec4d14+=pllkstn3
   if player.v0rxxf36<=0:
    player.xu9ymszd=False
  tj0nmeoq.fill(iq5c34dx['jl1qwe'])
  tj0nmeoq.blit(luzbikci,(0,0))
  mfyb8dal(tj0nmeoq,uysal8m1,giec4d14)
  for tacj4t0s in d1ieixwc:
   tacj4t0s.sl65wvjx(tj0nmeoq,uysal8m1,giec4d14)
  player.sl65wvjx(tj0nmeoq,uysal8m1,giec4d14)
  for x875aud9 in uc1xi04b:
   x875aud9.sl65wvjx(tj0nmeoq,uysal8m1,giec4d14)
   for yx4w6xlp in x875aud9.lt63j3r3:
    yx4w6xlp.sl65wvjx(tj0nmeoq,uysal8m1,giec4d14)
  for jc54wsqt in bq349dxb:
   jc54wsqt.sl65wvjx(tj0nmeoq,uysal8m1,giec4d14)
  for f2sehe2a in ruq9e5co:
   f2sehe2a.sl65wvjx(tj0nmeoq,uysal8m1,giec4d14)
  for oc4kl8cg in got7txkd:
   pygame.draw.circle(tj0nmeoq,oc4kl8cg['kou83g'],(int(oc4kl8cg['fuxk0a']-uysal8m1),int(oc4kl8cg['ijj0v6']-giec4d14)),oc4kl8cg['eqkwqh'])
  for w0p4e05q in klkjxjq5:
   rmm1zxyv(tj0nmeoq,w0p4e05q,uysal8m1,giec4d14)
  for dw7nh8rq in ouuylaja:
   dw7nh8rq.sl65wvjx(tj0nmeoq,uysal8m1,giec4d14)
  if mfc79m96!=None:
   mfc79m96.sl65wvjx(tj0nmeoq)
  rb1s9dwd=40+18*len(wyk03o4g)
  wehlxslg(tj0nmeoq,pygame.Rect(12,12,190,rb1s9dwd))
  jyjhu8my=qhkc856w.render(f'Enemies: {len(uc1xi04b)}',True,(20,20,20))
  tj0nmeoq.blit(jyjhu8my,(20+tbxf445c,20+pllkstn3))
  tza7x73q=50
  for wvndfdw7 in wyk03o4g:
   nyrid3dn=player.qxb7gbdg.get(wvndfdw7,1)
   ywcxz2ei=t5sn961j.render(f'{uyhl1c32[wvndfdw7]} Lv.{nyrid3dn}',True,(30,30,30))
   tj0nmeoq.blit(ywcxz2ei,(20+tbxf445c,tza7x73q+pllkstn3))
   tza7x73q+=18
  wehlxslg(tj0nmeoq,pygame.Rect(dtx63cfl-180,12,168,32))
  rgdej31g=t5sn961j.render(f'Resources: {cqheyto5}',True,(20,20,20))
  tj0nmeoq.blit(rgdej31g,(dtx63cfl-170+tbxf445c,20+pllkstn3))
  if dzsedfqs:
   ejbzutru=t5sn961j.render('Opening chest... weapons offline!',True,iq5c34dx['wyn6sj'])
   tj0nmeoq.blit(ejbzutru,(dtx63cfl//2-ejbzutru.get_width()//2+tbxf445c,12+pllkstn3))
  wehlxslg(tj0nmeoq,pygame.Rect(12,rla5ju9b-50,388,38))
  xk7n8la1=title_font.render(f'Lv.{player.swwnc21o}',True,(20,20,20))
  tj0nmeoq.blit(xk7n8la1,(20+tbxf445c,rla5ju9b-40+pllkstn3))
  huh17j8q=v4u89yjb[min(player.swwnc21o,len(v4u89yjb)-1)]
  mabkae6a=min(1.0,player.n01uyzpd/huh17j8q)
  eohswq40(tj0nmeoq,90,rla5ju9b-34,290,mabkae6a,height=16,fg=iq5c34dx['wdl5tg'],bg=(70,70,70))
  if eatvzkhi:
   wy0mahym=pygame.Surface((dtx63cfl,rla5ju9b),pygame.SRCALPHA)
   wy0mahym.fill((0,0,0,150))
   tj0nmeoq.blit(wy0mahym,(0,0))
   jyjhu8my=ra73jgzl.render('GAME OVER',True,iq5c34dx['w65dlx'])
   tby49e7e=ra73jgzl.render('GAME OVER',True,(0,0,0))
   (wi8skch8,iektsg7f)=(dtx63cfl//2-jyjhu8my.get_width()//2,rla5ju9b//2-jyjhu8my.get_height()//2)
   tj0nmeoq.blit(tby49e7e,(wi8skch8+2,iektsg7f+2))
   tj0nmeoq.blit(jyjhu8my,(wi8skch8,iektsg7f))
   svt8k06m=qhkc856w.render(f'You reached Level {player.swwnc21o}  |  +{cqheyto5} resources',True,iq5c34dx['m314cq'])
   tj0nmeoq.blit(svt8k06m,(dtx63cfl//2-svt8k06m.get_width()//2,iektsg7f+jyjhu8my.get_height()+10))
   z5x8a5fb=t5sn961j.render('Press ENTER to return to the Homebase',True,iq5c34dx['m314cq'])
   tj0nmeoq.blit(z5x8a5fb,(dtx63cfl//2-z5x8a5fb.get_width()//2,iektsg7f+jyjhu8my.get_height()+40))
  if izhwy9he:
   wy0mahym=pygame.Surface((dtx63cfl,rla5ju9b),pygame.SRCALPHA)
   wy0mahym.fill((0,0,0,150))
   tj0nmeoq.blit(wy0mahym,(0,0))
   jyjhu8my=ra73jgzl.render(f'Get ready!',True,iq5c34dx['w65dlx'])
   tby49e7e=ra73jgzl.render(f'Get ready!',True,(0,0,0))
   (wi8skch8,iektsg7f)=(dtx63cfl//2-jyjhu8my.get_width()//2,rla5ju9b//2-jyjhu8my.get_height()//2)
   tj0nmeoq.blit(tby49e7e,(wi8skch8+2,iektsg7f+2))
   tj0nmeoq.blit(jyjhu8my,(wi8skch8,iektsg7f))
   svt8k06m=qhkc856w.render(f'Game continuing in {tk0qtl3q}',True,iq5c34dx['m314cq'])
   tj0nmeoq.blit(svt8k06m,(dtx63cfl//2-svt8k06m.get_width()//2,iektsg7f+jyjhu8my.get_height()+10))
  if trdhw9re:
   wy0mahym=pygame.Surface((dtx63cfl,rla5ju9b),pygame.SRCALPHA)
   wy0mahym.fill((0,0,0,150))
   tj0nmeoq.blit(wy0mahym,(0,0))
   jyjhu8my=ra73jgzl.render(f'Game Paused',True,iq5c34dx['w65dlx'])
   tby49e7e=ra73jgzl.render(f'Game Paused',True,(0,0,0))
   (wi8skch8,iektsg7f)=(dtx63cfl//2-jyjhu8my.get_width()//2,rla5ju9b//2-jyjhu8my.get_height()//2)
   tj0nmeoq.blit(tby49e7e,(wi8skch8+2,iektsg7f+2))
   tj0nmeoq.blit(jyjhu8my,(wi8skch8,iektsg7f))
  zorxdtg5.sl65wvjx(tj0nmeoq)
  pygame.display.flip()
  ebt3g2qz.tick(pi3qk2ia)
def o4dd1vn8():
 qertb74r=nxxjve3d()
 if qertb74r is None:
  return
 bdgbk2l0=bokzixza(qertb74r)
 def qc06xq9j(hfb85p86):
  d46aexl6(qertb74r,hfb85p86)
 qc06xq9j(bdgbk2l0)
 while True:
  k44nlz15=npejzhya(tj0nmeoq,ebt3g2qz,bdgbk2l0,qc06xq9j)
  if k44nlz15=='quit':
   break
  if k44nlz15=='start_game':
   (wc7x0h3j,uj64qhks,h4l1vznq)=ytb9xxay(bdgbk2l0)
   bdgbk2l0['resources']+=wc7x0h3j
   bdgbk2l0['high_level']=max(bdgbk2l0.get('high_level',0),uj64qhks)
   bdgbk2l0['runs_played']=bdgbk2l0.get('runs_played',0)+1
   qc06xq9j(bdgbk2l0)
   if h4l1vznq:
    break
if __name__=='__main__':
 o4dd1vn8()
