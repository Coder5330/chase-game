import pygame
from rlfzkicw import*
from fxc7urvq import*
from entities import*
from p2xrw6tm import*
from amntfvge import*
from z37csuyt import hay64yfd
from djfe8udt import gkz2u2tn,uj64qhks,xasez2nx,gncxll4z
from g0qzsa7y import zflse45b
pygame.init()
todsx4nx=pygame.display.set_mode((azebbk7w,gokc1msy))
tk0qtl3q=pygame.time.Clock()
def hfb85p86(todsx4nx,wb7f6fdh,wkzorqqf=120,mmn32u1i=10):
 vmy9x8sy=pygame.Surface((wb7f6fdh.width,wb7f6fdh.height),pygame.SRCALPHA)
 pygame.draw.rect(vmy9x8sy,(255,255,255,wkzorqqf),vmy9x8sy.get_rect(),border_radius=mmn32u1i)
 todsx4nx.blit(vmy9x8sy,wb7f6fdh.topleft)
def g5hcbbmh():
 title_font=pygame.font.SysFont('arial',40,bold=True)
 ao4izasn=pygame.font.SysFont('arial',16)
 rzs43c5b=pygame.font.SysFont('arial',22,bold=True)
 ytb9xxay=pygame.font.SysFont('arial',15)
 aqclpoxk=[]
 for mytn02yc in range(1,gncxll4z+1):
  wtl0thhz=xasez2nx(mytn02yc)
  if wtl0thhz:
   subtitle=f"Level {wtl0thhz['high_level']}  |  {wtl0thhz['resources']} resources  |  {wtl0thhz['runs_played']} runs"
  else:
   subtitle='Empty - New Game'
  ykipu1wy=q7vren93(azebbk7w//2-170,170+(mytn02yc-1)*110,340,90,uqjiujv6,aye511mk,mn9er14f,f2pcn9t8,rzs43c5b,f'Slot {mytn02yc}',12,subtitle=subtitle,sub_font=ytb9xxay,kind='slot',key=mytn02yc)
  aqclpoxk.append(ykipu1wy)
 while True:
  wehlxslg=pygame.event.get()
  for eohswq40 in wehlxslg:
   if eohswq40.type==pygame.QUIT:
    return None
  for ykipu1wy in aqclpoxk:
   ykipu1wy.update(wehlxslg)
   if ykipu1wy.yw6zbnz8:
    return ykipu1wy.key
  todsx4nx.fill(bom5igqp['xlitnt'])
  nabufwbu=title_font.render('CHASE GAME',True,(20,20,40))
  todsx4nx.blit(nabufwbu,(azebbk7w//2-nabufwbu.get_width()//2,70))
  r98s4c3b=ao4izasn.render('Choose a save slot',True,(30,30,30))
  todsx4nx.blit(r98s4c3b,(azebbk7w//2-r98s4c3b.get_width()//2,135))
  for ykipu1wy in aqclpoxk:
   ykipu1wy.u1jhuwb6(todsx4nx)
  pygame.display.flip()
  tk0qtl3q.tick(zy0ifznb)
def gp6orsnc(exvaj2k8):
 sygvwopl=pygame.font.SysFont('arial',28)
 d0r2sds8=pygame.font.SysFont('arial',48)
 ytb9xxay=pygame.font.SysFont('arial',16)
 title_font=pygame.font.SysFont('arial',20,bold=True)
 ob7p0rnp=pygame.font.SysFont('arial',24,bold=True)
 rzs43c5b=pygame.font.SysFont('arial',22,bold=True)
 player=rv86wzs3(meta_upgrades=exvaj2k8.get('meta_upgrades',{}))
 qbbz2sf6=[]
 g11kerpe=[]
 lhgk5bwi=[]
 u23y30ys=[]
 jm25len6=[]
 wc7x0h3j=[]
 az2ueaxy=[k1wj0tpa[0]]
 kodpvjtu=['kdsc4e']
 player.h4m2ec8r['kdsc4e']=1
 gubmc97c=False
 s8438tgb=player.onqyyf9r
 ee1g983e=0
 arjn2hz2=dxmo5bxx*zy0ifznb
 vvslh9bh=dict(uyhl1c32)
 chx3d43e=None
 while True:
  wehlxslg=pygame.event.get()
  for eohswq40 in wehlxslg:
   if eohswq40.type==pygame.QUIT:
    return(ee1g983e,player.onqyyf9r,True)
   if gubmc97c and eohswq40.type==pygame.KEYDOWN and(eohswq40.key in(pygame.K_RETURN,pygame.K_SPACE)):
    return(ee1g983e,player.onqyyf9r,False)
  bq349dxb=False
  if not player.rr9u1oe5 and(not gubmc97c):
   for llxxezdu in u23y30ys[:]:
    m8lw2qit=llxxezdu.update(player)
    if m8lw2qit:
     bq349dxb=True
    if llxxezdu.xwqvr1h6:
     y8dd2255=random.randint(uccblskr,oeimvihc)
     ee1g983e+=y8dd2255
     for mqp49kwv in range(10):
      lhgk5bwi.append(bdgbk2l0([bom5igqp['wpadah'],bom5igqp['mbslul']],2,4,-3,3,llxxezdu.wb7f6fdh.centerx,llxxezdu.wb7f6fdh.centery,life=30))
     u23y30ys.remove(llxxezdu)
   arjn2hz2-=1
   if arjn2hz2<=0:
    arjn2hz2=dxmo5bxx*zy0ifznb
    if len(u23y30ys)<yex8fsv8:
     u23y30ys.append(hay64yfd(player))
   if not bq349dxb:
    for n8sa3idy in kodpvjtu:
     vvslh9bh[n8sa3idy]-=1
     if vvslh9bh[n8sa3idy]<=0:
      a1tbrwr9=player.h4m2ec8r.get(n8sa3idy,1)
      j2vmcqbn=uyhl1c32[n8sa3idy]*player.hugysm8t*kc7rm6j8(a1tbrwr9)
      vvslh9bh[n8sa3idy]=max(4,int(j2vmcqbn))
      k1taa0i5=mjh75lxo[n8sa3idy]['uq0e27']
      vw6m7b5c=player.vqnpcenl*v7g0iiji(a1tbrwr9)
      g11kerpe.append(rqf5q14j(n8sa3idy,player.wb7f6fdh.centerx-k1taa0i5//2,player.wb7f6fdh.centery-k1taa0i5//2,k1taa0i5,k1taa0i5,player.mn7h9g1a['vmwi9s'],player.mn7h9g1a['zcjn99'],vw6m7b5c))
   gmoft6yr=min(d60fkhmy,zxa3kx7e*(1+0.12*(player.onqyyf9r-1)))
   if random.random()<gmoft6yr:
    qc06xq9j(qbbz2sf6,az2ueaxy)
   player.k2ixivzk()
   if player.onqyyf9r>s8438tgb:
    if player.onqyyf9r<=len(k1wj0tpa):
     zflv1xxl=k1wj0tpa[player.onqyyf9r-1]
     if zflv1xxl not in az2ueaxy:
      az2ueaxy.append(zflv1xxl)
    s8438tgb=player.onqyyf9r
   if player.mqxlm5q2<=0:
    gubmc97c=True
   for qtzk3ny9 in qbbz2sf6:
    qtzk3ny9.k2ixivzk(player)
    for u8c2jwoc in qtzk3ny9.bwiykid9:
     u8c2jwoc.k2ixivzk(player)
     u8c2jwoc.t5wi6fqj(qbbz2sf6,lhgk5bwi,g11kerpe,player=player,target='player')
    qtzk3ny9.bwiykid9=[cqoldfor for cqoldfor in qtzk3ny9.bwiykid9 if not cqoldfor.f2sehe2a]
   for bllo3rbx in jm25len6:
    bllo3rbx.k2ixivzk(player)
   for nrpj1epk in g11kerpe:
    nrpj1epk.k2ixivzk(player,pbo119xp(qbbz2sf6,nrpj1epk))
    nrpj1epk.t5wi6fqj(qbbz2sf6,lhgk5bwi,g11kerpe)
   for mnwxuj3a in lhgk5bwi[:]:
    mnwxuj3a['xy79kv']+=mnwxuj3a['vmwi9s']
    mnwxuj3a['pswrgv']+=mnwxuj3a['zcjn99']
    mnwxuj3a['wxgnrf']-=1
    if mnwxuj3a['wxgnrf']<=0:
     lhgk5bwi.remove(mnwxuj3a)
   for rmm1zxyv in wc7x0h3j[:]:
    rmm1zxyv.update()
    if rmm1zxyv.f2sehe2a():
     wc7x0h3j.remove(rmm1zxyv)
  if player.rr9u1oe5 and(not gubmc97c):
   if chx3d43e==None:
    y2f7atwy=[]
    for rk36m8jv in mjh75lxo:
     if rk36m8jv=='jq85x7':
      continue
     if rk36m8jv not in kodpvjtu:
      y2f7atwy.append(('txzuu8',rk36m8jv))
    for rk36m8jv in kodpvjtu:
     if player.h4m2ec8r.get(rk36m8jv,1)<s9skdgig:
      y2f7atwy.append(('dzjssz',rk36m8jv))
    for k in hyihair4:
     if player.rwybow23.get(k,0)<hyihair4[k]['xyhhg8']:
      y2f7atwy.append(('fnn16u',k))
    if not y2f7atwy:
     player.rr9u1oe5=False
    else:
     random.shuffle(y2f7atwy)
     giec4d14=y2f7atwy[:3]
     d1ieixwc=120*len(giec4d14)+20
     chx3d43e=cq5uznof(400,d1ieixwc+cq5uznof.pi3qk2ia,jsylztgx,title='LEVEL UP! Choose an upgrade',title_font=ob7p0rnp)
     ra73jgzl=d1ieixwc//len(giec4d14)
     pvasifpw=chx3d43e.wb7f6fdh.lu7jae58+chx3d43e.yrivh6t1
     for(mytn02yc,(kind,key))in enumerate(giec4d14):
      if kind=='txzuu8':
       title=f'NEW WEAPON: {vxvg0fn9[key]}'
       subtitle='Unlock this weapon'
      elif kind=='dzjssz':
       semqgy27=player.h4m2ec8r.get(key,1)
       title=f'{vxvg0fn9[key]}  Lv.{semqgy27} -> {semqgy27 + 1}'
       subtitle='+12% damage, faster cooldown'
      else:
       semqgy27=player.rwybow23.get(key,0)
       title=f"{hyihair4[key]['amyrsv']}  Lv.{semqgy27} -> {semqgy27 + 1}"
       subtitle=hyihair4[key]['h7kr0a']
      ykipu1wy=q7vren93(chx3d43e.wb7f6fdh.kn5gjj8m+12,pvasifpw+mytn02yc*ra73jgzl+6,chx3d43e.wb7f6fdh.width-24,ra73jgzl-12,uqjiujv6,aye511mk,mn9er14f,f2pcn9t8,rzs43c5b,title,12,subtitle=subtitle,sub_font=ytb9xxay,kind=kind,key=key)
      chx3d43e.add(ykipu1wy)
   if chx3d43e is not None:
    for cnqt3wve in chx3d43e.damdvlnk:
     cnqt3wve.update(wehlxslg)
     if cnqt3wve.yw6zbnz8:
      if cnqt3wve.kind=='txzuu8':
       kodpvjtu.append(cnqt3wve.key)
       player.h4m2ec8r[cnqt3wve.key]=1
       vvslh9bh[cnqt3wve.key]=uyhl1c32[cnqt3wve.key]
      elif cnqt3wve.kind=='dzjssz':
       player.gsmdzqcb(cnqt3wve.key)
      elif cnqt3wve.kind=='fnn16u':
       player.win4olr6(cnqt3wve.key)
      player.rr9u1oe5=False
      chx3d43e=None
  m3pt5r5r(qbbz2sf6)
  (qbbz2sf6,g11kerpe,jm25len6)=zorxdtg5(qbbz2sf6,g11kerpe,jm25len6,player,wc7x0h3j)
  u3ifhv1x=player.wb7f6fdh.kn5gjj8m-azebbk7w//2
  f8wquuy5=player.wb7f6fdh.lu7jae58-gokc1msy//2
  u3ifhv1x=max(min(u3ifhv1x,pecruyf3-azebbk7w),0)
  f8wquuy5=max(min(f8wquuy5,yr5uqpgb-gokc1msy),0)
  v6xii5p5=ljk4q5v7=0
  if player.vt26ys44:
   player.rgdej31g-=1
   v6xii5p5=random.randint(-rcfnfhol,rcfnfhol)
   ljk4q5v7=random.randint(-rcfnfhol,rcfnfhol)
   u3ifhv1x+=v6xii5p5
   f8wquuy5+=ljk4q5v7
   if player.rgdej31g<=0:
    player.vt26ys44=False
  todsx4nx.fill(bom5igqp['xlitnt'])
  bfoqmf5l(todsx4nx,u3ifhv1x,f8wquuy5)
  for llxxezdu in u23y30ys:
   llxxezdu.u1jhuwb6(todsx4nx,u3ifhv1x,f8wquuy5)
  player.u1jhuwb6(todsx4nx,u3ifhv1x,f8wquuy5)
  for qtzk3ny9 in qbbz2sf6:
   qtzk3ny9.u1jhuwb6(todsx4nx,u3ifhv1x,f8wquuy5)
   for u8c2jwoc in qtzk3ny9.bwiykid9:
    u8c2jwoc.u1jhuwb6(todsx4nx,u3ifhv1x,f8wquuy5)
  for nrpj1epk in g11kerpe:
   nrpj1epk.u1jhuwb6(todsx4nx,u3ifhv1x,f8wquuy5)
  for bllo3rbx in jm25len6:
   bllo3rbx.u1jhuwb6(todsx4nx,u3ifhv1x,f8wquuy5)
  for mnwxuj3a in lhgk5bwi:
   pygame.draw.circle(todsx4nx,mnwxuj3a['jgm32w'],(int(mnwxuj3a['xy79kv']-u3ifhv1x),int(mnwxuj3a['pswrgv']-f8wquuy5)),mnwxuj3a['uq0e27'])
  for rmm1zxyv in wc7x0h3j:
   rmm1zxyv.u1jhuwb6(todsx4nx,u3ifhv1x,f8wquuy5)
  if chx3d43e!=None:
   chx3d43e.u1jhuwb6(todsx4nx)
  qy3vg6v5=40+18*len(kodpvjtu)
  hfb85p86(todsx4nx,pygame.Rect(12,12,190,qy3vg6v5))
  vmy9x8sy=sygvwopl.render(f'Enemies: {len(qbbz2sf6)}',True,(20,20,20))
  todsx4nx.blit(vmy9x8sy,(20+v6xii5p5,20+ljk4q5v7))
  s5r96khu=50
  for rk36m8jv in kodpvjtu:
   semqgy27=player.h4m2ec8r.get(rk36m8jv,1)
   gqoagsus=ytb9xxay.render(f'{vxvg0fn9[rk36m8jv]} Lv.{semqgy27}',True,(30,30,30))
   todsx4nx.blit(gqoagsus,(20+v6xii5p5,s5r96khu+ljk4q5v7))
   s5r96khu+=18
  hfb85p86(todsx4nx,pygame.Rect(azebbk7w-180,12,168,32))
  wydmt8vt=ytb9xxay.render(f'Resources: {ee1g983e}',True,(20,20,20))
  todsx4nx.blit(wydmt8vt,(azebbk7w-170+v6xii5p5,20+ljk4q5v7))
  if bq349dxb:
   mu118qqv=ytb9xxay.render('Opening chest... weapons offline!',True,bom5igqp['y2wyjx'])
   todsx4nx.blit(mu118qqv,(azebbk7w//2-mu118qqv.get_width()//2+v6xii5p5,12+ljk4q5v7))
  hfb85p86(todsx4nx,pygame.Rect(12,gokc1msy-50,388,38))
  jo8e7flq=title_font.render(f'Lv.{player.onqyyf9r}',True,(20,20,20))
  todsx4nx.blit(jo8e7flq,(20+v6xii5p5,gokc1msy-40+ljk4q5v7))
  usz2kuuo=jdiuovw1[min(player.onqyyf9r,len(jdiuovw1)-1)]
  wfhj4d0j=min(1.0,player.frhzn4kg/usz2kuuo)
  l9enulqj(todsx4nx,90,gokc1msy-34,290,wfhj4d0j,height=16,fg=bom5igqp['wpadah'],bg=(70,70,70))
  if gubmc97c:
   tb4ldims=pygame.Surface((azebbk7w,gokc1msy),pygame.SRCALPHA)
   tb4ldims.fill((0,0,0,150))
   todsx4nx.blit(tb4ldims,(0,0))
   vmy9x8sy=d0r2sds8.render('GAME OVER',True,bom5igqp['mgsiwg'])
   z3olfark=d0r2sds8.render('GAME OVER',True,(0,0,0))
   (x5m9j98c,uos0fb4y)=(azebbk7w//2-vmy9x8sy.get_width()//2,gokc1msy//2-vmy9x8sy.get_height()//2)
   todsx4nx.blit(z3olfark,(x5m9j98c+2,uos0fb4y+2))
   todsx4nx.blit(vmy9x8sy,(x5m9j98c,uos0fb4y))
   t5sn961j=sygvwopl.render(f'You reached Level {player.onqyyf9r}  |  +{ee1g983e} resources',True,bom5igqp['ym5p7e'])
   todsx4nx.blit(t5sn961j,(azebbk7w//2-t5sn961j.get_width()//2,uos0fb4y+vmy9x8sy.get_height()+10))
   q26yg3dx=ytb9xxay.render('Press ENTER to return to the Homebase',True,bom5igqp['ym5p7e'])
   todsx4nx.blit(q26yg3dx,(azebbk7w//2-q26yg3dx.get_width()//2,uos0fb4y+vmy9x8sy.get_height()+40))
  pygame.display.flip()
  tk0qtl3q.tick(zy0ifznb)
def ftrflqbm():
 yg87oi0e=g5hcbbmh()
 if yg87oi0e is None:
  return
 exvaj2k8=gkz2u2tn(yg87oi0e)
 def vhxs58yr(lztkkfzz):
  uj64qhks(yg87oi0e,lztkkfzz)
 vhxs58yr(exvaj2k8)
 while True:
  t1w1ht7p=zflse45b(todsx4nx,tk0qtl3q,exvaj2k8,vhxs58yr)
  if t1w1ht7p=='quit':
   break
  if t1w1ht7p=='start_game':
   (i01nouht,mfc79m96,g1g1r1dw)=gp6orsnc(exvaj2k8)
   exvaj2k8['resources']+=i01nouht
   exvaj2k8['high_level']=max(exvaj2k8.get('high_level',0),mfc79m96)
   exvaj2k8['runs_played']=exvaj2k8.get('runs_played',0)+1
   vhxs58yr(exvaj2k8)
   if g1g1r1dw:
    break
if __name__=='__main__':
 ftrflqbm()
