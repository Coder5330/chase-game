from fjzr5swk import*
luzbikci=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
for k44nlz15 in range(tp0lvsnu):
 jmpioygg=k44nlz15/max(1,tp0lvsnu-1)
 wrbw2zla=int(45*(1-jmpioygg))
 pygame.draw.line(luzbikci,(235,245,250,wrbw2zla),(0,k44nlz15),(ygspk9p3,k44nlz15))
def jqxs6esj(vmy9x8sy,nxxjve3d,v982n2at=120,xasez2nx=10):
 rserev36=pygame.Surface((nxxjve3d.width,nxxjve3d.height),pygame.SRCALPHA)
 pygame.draw.rect(rserev36,(255,255,255,v982n2at),rserev36.get_rect(),border_radius=xasez2nx)
 vmy9x8sy.blit(rserev36,nxxjve3d.topleft)
def zefqjg02(vmy9x8sy,mytn02yc):
 player=mytn02yc.player
 d1ieixwc=player.nxxjve3d.un9sz6rv-ygspk9p3//2
 pvasifpw=player.nxxjve3d.ehet25lz-tp0lvsnu//2
 d1ieixwc=max(min(d1ieixwc,v83tqll8-ygspk9p3),0)
 pvasifpw=max(min(pvasifpw,cqoldfor-tp0lvsnu),0)
 t54piwzn=stv18kgy=0
 if player.xxns2zyb:
  player.mn89ltaj-=1
  t54piwzn=random.randint(-s8qjnv8z,s8qjnv8z)
  stv18kgy=random.randint(-s8qjnv8z,s8qjnv8z)
  d1ieixwc+=t54piwzn
  pvasifpw+=stv18kgy
  if player.mn89ltaj<=0:
   player.xxns2zyb=False
 vmy9x8sy.fill(iq5c34dx['s1whhk'])
 vmy9x8sy.blit(luzbikci,(0,0))
 fp47b42g(vmy9x8sy,d1ieixwc,pvasifpw)
 for clkqzfpq in mytn02yc.x5m9j98c:
  clkqzfpq.fo75rh8l(vmy9x8sy,d1ieixwc,pvasifpw)
 player.fo75rh8l(vmy9x8sy,d1ieixwc,pvasifpw)
 for gubmc97c in mytn02yc.vhuds3qs:
  gubmc97c.fo75rh8l(vmy9x8sy,d1ieixwc,pvasifpw)
  for lcj883dh in gubmc97c.ytv3i12v:
   lcj883dh.fo75rh8l(vmy9x8sy,d1ieixwc,pvasifpw)
 for yw6zbnz8 in mytn02yc.f32ejx5t:
  yw6zbnz8.fo75rh8l(vmy9x8sy,d1ieixwc,pvasifpw)
 for hfb85p86 in mytn02yc.k7zgf9q5:
  hfb85p86.fo75rh8l(vmy9x8sy,d1ieixwc,pvasifpw)
 for gp6orsnc in mytn02yc.l3swebnv:
  pygame.draw.circle(vmy9x8sy,gp6orsnc['e56waf'],(int(gp6orsnc['th2p39']-d1ieixwc),int(gp6orsnc['zhbgcj']-pvasifpw)),gp6orsnc['yc1nlc'])
 for ej16dvtj in mytn02yc.ywcxz2ei:
  sygvwopl(vmy9x8sy,ej16dvtj,d1ieixwc,pvasifpw)
 for boih5csk in mytn02yc.zqcootnj:
  boih5csk.fo75rh8l(vmy9x8sy,d1ieixwc,pvasifpw)
 if mytn02yc.zflse45b is not None:
  mytn02yc.zflse45b.fo75rh8l(vmy9x8sy)
 eq3tq1s0=40+18*len(mytn02yc.n01uyzpd)
 jqxs6esj(vmy9x8sy,pygame.Rect(12,12,190,eq3tq1s0))
 rserev36=mytn02yc.ao4izasn.render(f'Enemies: {len(mytn02yc.vhuds3qs)}',True,(20,20,20))
 vmy9x8sy.blit(rserev36,(20+t54piwzn,20+stv18kgy))
 yjr0fzau=50
 for d5ixva1n in mytn02yc.n01uyzpd:
  nii6l3ue=player.ceb8753a.get(d5ixva1n,1)
  jslulzfy=mytn02yc.yp3cyazb.render(f'{uyhl1c32[d5ixva1n]} Lv.{nii6l3ue}',True,(30,30,30))
  vmy9x8sy.blit(jslulzfy,(20+t54piwzn,yjr0fzau+stv18kgy))
  yjr0fzau+=18
 jqxs6esj(vmy9x8sy,pygame.Rect(ygspk9p3-180,12,168,32))
 d46aexl6=mytn02yc.yp3cyazb.render(f'Resources: {mytn02yc.fd6rupw2}',True,(20,20,20))
 vmy9x8sy.blit(d46aexl6,(ygspk9p3-170+t54piwzn,20+stv18kgy))
 if mytn02yc.bllo3rbx:
  kcubods1=mytn02yc.yp3cyazb.render('Opening chest... weapons offline!',True,iq5c34dx['fzeeqn'])
  vmy9x8sy.blit(kcubods1,(ygspk9p3//2-kcubods1.get_width()//2+t54piwzn,12+stv18kgy))
 jqxs6esj(vmy9x8sy,pygame.Rect(12,tp0lvsnu-50,388,38))
 mctwjlsh=mytn02yc.title_font.render(f'Lv.{player.b78okz1p}',True,(20,20,20))
 vmy9x8sy.blit(mctwjlsh,(20+t54piwzn,tp0lvsnu-40+stv18kgy))
 iimoe0sy=m53a5qbs[min(player.b78okz1p,len(m53a5qbs)-1)]
 uypuplvq=min(1.0,player.cgsq7ait/iimoe0sy)
 x875aud9(vmy9x8sy,90,tp0lvsnu-34,290,uypuplvq,height=16,fg=iq5c34dx['x1qwee'],bg=(70,70,70))
 if mytn02yc.x9bp4m18:
  vyb6li07=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
  vyb6li07.fill((0,0,0,150))
  vmy9x8sy.blit(vyb6li07,(0,0))
  rserev36=mytn02yc.fcwtg1m8.render('GAME OVER',True,iq5c34dx['cparsg'])
  gj29yfc2=mytn02yc.fcwtg1m8.render('GAME OVER',True,(0,0,0))
  (cnqt3wve,do2m71hs)=(ygspk9p3//2-rserev36.get_width()//2,tp0lvsnu//2-rserev36.get_height()//2)
  vmy9x8sy.blit(gj29yfc2,(cnqt3wve+2,do2m71hs+2))
  vmy9x8sy.blit(rserev36,(cnqt3wve,do2m71hs))
  nv23gxj0=mytn02yc.ao4izasn.render(f'You reached Level {player.b78okz1p}  |  +{mytn02yc.fd6rupw2} resources',True,iq5c34dx['jyzqii'])
  vmy9x8sy.blit(nv23gxj0,(ygspk9p3//2-nv23gxj0.get_width()//2,do2m71hs+rserev36.get_height()+10))
  xxkdq95g=mytn02yc.yp3cyazb.render('Press ENTER to return to the Homebase',True,iq5c34dx['jyzqii'])
  vmy9x8sy.blit(xxkdq95g,(ygspk9p3//2-xxkdq95g.get_width()//2,do2m71hs+rserev36.get_height()+40))
 if mytn02yc.rk8r2ykc:
  vyb6li07=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
  vyb6li07.fill((0,0,0,150))
  vmy9x8sy.blit(vyb6li07,(0,0))
  rserev36=mytn02yc.fcwtg1m8.render('Get ready!',True,iq5c34dx['cparsg'])
  gj29yfc2=mytn02yc.fcwtg1m8.render('Get ready!',True,(0,0,0))
  (cnqt3wve,do2m71hs)=(ygspk9p3//2-rserev36.get_width()//2,tp0lvsnu//2-rserev36.get_height()//2)
  vmy9x8sy.blit(gj29yfc2,(cnqt3wve+2,do2m71hs+2))
  vmy9x8sy.blit(rserev36,(cnqt3wve,do2m71hs))
  nv23gxj0=mytn02yc.ao4izasn.render(f'Game continuing in {mytn02yc.amcixdu1}',True,iq5c34dx['jyzqii'])
  vmy9x8sy.blit(nv23gxj0,(ygspk9p3//2-nv23gxj0.get_width()//2,do2m71hs+rserev36.get_height()+10))
 if mytn02yc.cknfu84x:
  vyb6li07=pygame.Surface((ygspk9p3,tp0lvsnu),pygame.SRCALPHA)
  vyb6li07.fill((0,0,0,150))
  vmy9x8sy.blit(vyb6li07,(0,0))
  rserev36=mytn02yc.fcwtg1m8.render('Game Paused',True,iq5c34dx['cparsg'])
  gj29yfc2=mytn02yc.fcwtg1m8.render('Game Paused',True,(0,0,0))
  (cnqt3wve,do2m71hs)=(ygspk9p3//2-rserev36.get_width()//2,tp0lvsnu//2-rserev36.get_height()//2)
  vmy9x8sy.blit(gj29yfc2,(cnqt3wve+2,do2m71hs+2))
  vmy9x8sy.blit(rserev36,(cnqt3wve,do2m71hs))
 mytn02yc.vhxs58yr.fo75rh8l(vmy9x8sy)
