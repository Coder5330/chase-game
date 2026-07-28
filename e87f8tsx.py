from ifcl5efj import*
luzbikci=pygame.Surface((cqoldfor,tp0lvsnu),pygame.SRCALPHA)
for j1i2hgj1 in range(tp0lvsnu):
 x52qc1iy=j1i2hgj1/max(1,tp0lvsnu-1)
 zs3kkv9r=int(45*(1-x52qc1iy))
 pygame.draw.line(luzbikci,(235,245,250,zs3kkv9r),(0,j1i2hgj1),(cqoldfor,j1i2hgj1))
def gubmc97c(u15pdtz9,uaobt328,am2vajep=120,v0rxxf36=10):
 mu118qqv=pygame.Surface((uaobt328.width,uaobt328.height),pygame.SRCALPHA)
 pygame.draw.rect(mu118qqv,(255,255,255,am2vajep),mu118qqv.get_rect(),border_radius=v0rxxf36)
 u15pdtz9.blit(mu118qqv,uaobt328.topleft)
def pbo119xp(u15pdtz9,xqzpky32):
 player=xqzpky32.player
 clkqzfpq=player.uaobt328.owdz09wf-cqoldfor//2
 x5m9j98c=player.uaobt328.lb4y4k7b-tp0lvsnu//2
 clkqzfpq=max(min(clkqzfpq,m53a5qbs-cqoldfor),0)
 x5m9j98c=max(min(x5m9j98c,v83tqll8-tp0lvsnu),0)
 z5x8a5fb=svt8k06m=0
 if player.ck7n3bfh:
  player.xo2t8fy6-=1
  z5x8a5fb=random.randint(-s8qjnv8z,s8qjnv8z)
  svt8k06m=random.randint(-s8qjnv8z,s8qjnv8z)
  clkqzfpq+=z5x8a5fb
  x5m9j98c+=svt8k06m
  if player.xo2t8fy6<=0:
   player.ck7n3bfh=False
 u15pdtz9.fill(iq5c34dx['edxoq2'])
 u15pdtz9.blit(luzbikci,(0,0))
 vhuds3qs(u15pdtz9,clkqzfpq,x5m9j98c)
 for wzs13c9x in xqzpky32.oqse3tv1:
  wzs13c9x.v15cqzcu(u15pdtz9,clkqzfpq,x5m9j98c)
 player.v15cqzcu(u15pdtz9,clkqzfpq,x5m9j98c)
 for kx74d0gj in xqzpky32.nfn1r4kz:
  kx74d0gj.v15cqzcu(u15pdtz9,clkqzfpq,x5m9j98c)
  for vj8yrddp in kx74d0gj.l57p6bkl:
   vj8yrddp.v15cqzcu(u15pdtz9,clkqzfpq,x5m9j98c)
 for hugysm8t in xqzpky32.ebt3g2qz:
  hugysm8t.v15cqzcu(u15pdtz9,clkqzfpq,x5m9j98c)
 for mfyb8dal in xqzpky32.eohswq40:
  mfyb8dal.v15cqzcu(u15pdtz9,clkqzfpq,x5m9j98c)
 for rgdej31g in xqzpky32.cqheyto5:
  pygame.draw.circle(u15pdtz9,rgdej31g['mrf5a7'],(int(rgdej31g['qbpj8t']-clkqzfpq),int(rgdej31g['q8y5dn']-x5m9j98c)),rgdej31g['prf7bn'])
 for kc7rm6j8 in xqzpky32.pg3yu6vk:
  mq7nc85e(u15pdtz9,kc7rm6j8,clkqzfpq,x5m9j98c)
 for u0q0mftg in xqzpky32.fddfgs3j:
  u0q0mftg.v15cqzcu(u15pdtz9,clkqzfpq,x5m9j98c)
 if xqzpky32.v6xii5p5 is not None:
  xqzpky32.v6xii5p5.v15cqzcu(u15pdtz9)
 m81udp2f=40+18*len(xqzpky32.vsjchzjq)
 gubmc97c(u15pdtz9,pygame.Rect(12,12,190,m81udp2f))
 mu118qqv=xqzpky32.cjn2fomd.render(f'Enemies: {len(xqzpky32.nfn1r4kz)}',True,(20,20,20))
 u15pdtz9.blit(mu118qqv,(20+z5x8a5fb,20+svt8k06m))
 o3q0e27z=50
 for n8k03w0f in xqzpky32.vsjchzjq:
  mnwxuj3a=player.m9bn18gp.get(n8k03w0f,1)
  gdg1wjui=xqzpky32.qdnai89y.render(f'{uyhl1c32[n8k03w0f]} Lv.{mnwxuj3a}',True,(30,30,30))
  u15pdtz9.blit(gdg1wjui,(20+z5x8a5fb,o3q0e27z+svt8k06m))
  o3q0e27z+=18
 gubmc97c(u15pdtz9,pygame.Rect(cqoldfor-180,12,168,32))
 qertb74r=xqzpky32.qdnai89y.render(f'Resources: {xqzpky32.k8qeoz0k}',True,(20,20,20))
 u15pdtz9.blit(qertb74r,(cqoldfor-170+z5x8a5fb,20+svt8k06m))
 if xqzpky32.cq6qdy4l:
  un4regb1=xqzpky32.qdnai89y.render('Opening chest... weapons offline!',True,iq5c34dx['bjd5n3'])
  u15pdtz9.blit(un4regb1,(cqoldfor//2-un4regb1.get_width()//2+z5x8a5fb,12+svt8k06m))
 gubmc97c(u15pdtz9,pygame.Rect(12,tp0lvsnu-50,388,38))
 hp89fkbi=xqzpky32.title_font.render(f'Lv.{player.a8ax40dt}',True,(20,20,20))
 u15pdtz9.blit(hp89fkbi,(20+z5x8a5fb,tp0lvsnu-40+svt8k06m))
 t5ivrocv=t1w1ht7p[min(player.a8ax40dt,len(t1w1ht7p)-1)]
 h5kw3hgb=min(1.0,player.rn16uxf5/t5ivrocv)
 ouuylaja(u15pdtz9,90,tp0lvsnu-34,290,h5kw3hgb,height=16,fg=iq5c34dx['qye0qz'],bg=(70,70,70))
 if xqzpky32.nyfkjfpn:
  z3olfark=pygame.Surface((cqoldfor,tp0lvsnu),pygame.SRCALPHA)
  z3olfark.fill((0,0,0,150))
  u15pdtz9.blit(z3olfark,(0,0))
  mu118qqv=xqzpky32.llxxezdu.render('GAME OVER',True,iq5c34dx['az3m55'])
  uoloeazc=xqzpky32.llxxezdu.render('GAME OVER',True,(0,0,0))
  (wzlm72je,vt6om1fb)=(cqoldfor//2-mu118qqv.get_width()//2,tp0lvsnu//2-mu118qqv.get_height()//2)
  u15pdtz9.blit(uoloeazc,(wzlm72je+2,vt6om1fb+2))
  u15pdtz9.blit(mu118qqv,(wzlm72je,vt6om1fb))
  rk36m8jv=xqzpky32.cjn2fomd.render(f'You reached Level {player.a8ax40dt}  |  +{xqzpky32.k8qeoz0k} resources',True,iq5c34dx['kp82kb'])
  u15pdtz9.blit(rk36m8jv,(cqoldfor//2-rk36m8jv.get_width()//2,vt6om1fb+mu118qqv.get_height()+10))
  yoyohaz7=xqzpky32.qdnai89y.render('Press ENTER to return to the Homebase',True,iq5c34dx['kp82kb'])
  u15pdtz9.blit(yoyohaz7,(cqoldfor//2-yoyohaz7.get_width()//2,vt6om1fb+mu118qqv.get_height()+40))
 if xqzpky32.qtzk3ny9:
  z3olfark=pygame.Surface((cqoldfor,tp0lvsnu),pygame.SRCALPHA)
  z3olfark.fill((0,0,0,150))
  u15pdtz9.blit(z3olfark,(0,0))
  mu118qqv=xqzpky32.llxxezdu.render('Get ready!',True,iq5c34dx['az3m55'])
  uoloeazc=xqzpky32.llxxezdu.render('Get ready!',True,(0,0,0))
  (wzlm72je,vt6om1fb)=(cqoldfor//2-mu118qqv.get_width()//2,tp0lvsnu//2-mu118qqv.get_height()//2)
  u15pdtz9.blit(uoloeazc,(wzlm72je+2,vt6om1fb+2))
  u15pdtz9.blit(mu118qqv,(wzlm72je,vt6om1fb))
  rk36m8jv=xqzpky32.cjn2fomd.render(f'Game continuing in {xqzpky32.vqnpcenl}',True,iq5c34dx['kp82kb'])
  u15pdtz9.blit(rk36m8jv,(cqoldfor//2-rk36m8jv.get_width()//2,vt6om1fb+mu118qqv.get_height()+10))
 if xqzpky32.wgcl9lcq:
  z3olfark=pygame.Surface((cqoldfor,tp0lvsnu),pygame.SRCALPHA)
  z3olfark.fill((0,0,0,150))
  u15pdtz9.blit(z3olfark,(0,0))
  mu118qqv=xqzpky32.llxxezdu.render('Game Paused',True,iq5c34dx['az3m55'])
  uoloeazc=xqzpky32.llxxezdu.render('Game Paused',True,(0,0,0))
  (wzlm72je,vt6om1fb)=(cqoldfor//2-mu118qqv.get_width()//2,tp0lvsnu//2-mu118qqv.get_height()//2)
  u15pdtz9.blit(uoloeazc,(wzlm72je+2,vt6om1fb+2))
  u15pdtz9.blit(mu118qqv,(wzlm72je,vt6om1fb))
 xqzpky32.g1g1r1dw.v15cqzcu(u15pdtz9)
