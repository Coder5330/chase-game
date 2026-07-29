import os
import sys
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
nd96qe3r=getattr(sys,'_MEIPASS',dnq4fmyz)
def vvslh9bh(pllkstn3):
 return os.path.join(nd96qe3r,pllkstn3)
(cqoldfor,tp0lvsnu)=(800,600)
(m53a5qbs,v83tqll8)=(2000,2000)
pi3qk2ia=60
vve92mpn=40
rcfnfhol=4
yswjckjl=30
zxa3kx7e=30
r4874frh=4
ue0ifd0t=140
d60fkhmy=0.01
isj6bw3b=0.045
m7hv3izk=1.4
cawudtse=40
b8cgvyie=300
jsylztgx=225
y38daly8=6
s8qjnv8z=4
gncxll4z=6
iq5c34dx={'cm3v2p':(255,0,0),'s1whhk':(255,102,102),'ze429o':(139,0,0),'o2o04k':(0,255,0),'qye0qz':(144,238,144),'jp4juw':(0,100,0),'yjq4ta':(0,0,255),'jl6314':(0,255,255),'gzyt91':(0,0,128),'e56waf':(135,206,235),'t7wqp3':(255,255,0),'a8udtt':(255,255,224),'jyzqii':(128,128,0),'tjng7l':(255,165,0),'qelb45':(255,200,124),'tikgeq':(255,140,0),'mviifr':(128,0,128),'l4f9ye':(238,130,238),'z1zlbo':(75,0,130),'w2lx2t':(255,192,203),'kqbsxl':(255,182,193),'utfvge':(255,105,180),'gbfxb4':(139,69,19),'a26fmr':(181,101,29),'qhhcu9':(92,46,13),'uefq56':(128,128,128),'qll1d9':(211,211,211),'q9ry79':(64,64,64),'hpvwzo':(0,128,128),'rlpefj':(102,178,178),'km3hxy':(0,77,77),'t6tbb6':(255,0,255),'kqbrmq':(218,112,214),'ewr0r3':(139,0,139),'glmy62':(255,215,0),'y3lxch':(192,192,192),'bdbpgv':(128,0,0),'ntxrgn':(64,224,208),'wurvqt':(250,128,114),'rgqu7d':(255,127,80),'egzpl1':(245,245,220),'p5n3ks':(255,255,240),'fe226p':(240,230,140),'okg68a':(0,0,0),'cxf5x9':(255,255,255)}
cq5uznof=(90,90,100)
rv86wzs3=(50,50,58)
wa11dpg8=(120,120,132)
qqu7eeqt=(70,70,80)
gyljexq7=['o2o04k','jl6314','yjq4ta','mviifr','t6tbb6','tjng7l','cm3v2p','ze429o','uefq56','glmy62']
def jmpioygg(a8ax40dt):
 return{'igc9ho':100*1.3**(a8ax40dt-1),'pca7zv':min(rcfnfhol*0.75,1.3*1.13**(a8ax40dt-1)),'mmgvu4':10*1.25**(a8ax40dt-1),'onlt8d':5*1.2**(a8ax40dt-1),'hzj7ub':max(10,60*0.9**(a8ax40dt-1)),'gv4k00':26*1.27**(a8ax40dt-1)}
s0clbr7t={'xytaul':{'nf7qne':1,'fuxk0a':'o2o04k','hrctlt':(1.0,1.0,1.0,1.0,1.0,1.0)},'kk2y77':{'nf7qne':2,'fuxk0a':'jl6314','hrctlt':(0.6,1.8,0.7,0.8,0.8,1.0),'pgsb98':True,'bx1ego':150,'jr87iy':2.5,'hx0gu4':20,'t7fr91':90},'az3m55':{'nf7qne':3,'fuxk0a':'uefq56','hrctlt':(2.6,0.45,0.6,1.6,1.3,1.3),'en1x2g':True,'dzjq7w':60,'yc1nlc':1,'i1yy1j':30},'cjy62z':{'nf7qne':4,'fuxk0a':'mviifr','hrctlt':(0.7,0.7,1.3,0.7,1.4,1.2),'agbl2q':True,'ua6wix':260,'rfu7bf':7},'vuvldd':{'nf7qne':5,'fuxk0a':'tjng7l','hrctlt':(1.6,0.85,1.6,1.1,1.1,1.4),'gpm21b':True,'c6zvlh':40,'xbtfbs':2.0},'ygm55f':{'nf7qne':6,'fuxk0a':'t6tbb6','hrctlt':(0.55,2.1,1.5,0.6,0.7,1.3),'tgr8w2':True,'vhbef4':10,'lpug99':120,'tn1th1':150,'f4c3ev':25},'pivroc':{'nf7qne':7,'fuxk0a':'cm3v2p','hrctlt':(0.8,1.1,1.0,0.8,1.0,1.3),'w9laac':True,'gbwcv6':70},'og8cd3':{'nf7qne':8,'fuxk0a':'ze429o','hrctlt':(1.8,0.75,0.9,2.4,1.2,1.5),'qc6dr0':True,'buzery':120,'e0s41k':0.5},'m44c68':{'nf7qne':9,'fuxk0a':'glmy62','hrctlt':(0.35,1.5,0.5,0.5,0.6,0.8),'yoztp7':3},'i2lsla':{'nf7qne':10,'fuxk0a':'ewr0r3','hrctlt':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={mu4fmpkx:{'igc9ho':int(jmpioygg(ruq9e5co['nf7qne'])['igc9ho']*ruq9e5co['hrctlt'][0]),'pca7zv':round(jmpioygg(ruq9e5co['nf7qne'])['pca7zv']*ruq9e5co['hrctlt'][1],2),'mmgvu4':int(jmpioygg(ruq9e5co['nf7qne'])['mmgvu4']*ruq9e5co['hrctlt'][2]),'onlt8d':int(jmpioygg(ruq9e5co['nf7qne'])['onlt8d']*ruq9e5co['hrctlt'][3]),'hzj7ub':max(10,int(jmpioygg(ruq9e5co['nf7qne'])['hzj7ub']*ruq9e5co['hrctlt'][4])),'gv4k00':int(jmpioygg(ruq9e5co['nf7qne'])['gv4k00']*ruq9e5co['hrctlt'][5]),'fuxk0a':iq5c34dx[ruq9e5co['fuxk0a']],'nf7qne':ruq9e5co['nf7qne'],'agbl2q':ruq9e5co.get('agbl2q',False),'ua6wix':ruq9e5co.get('ua6wix'),'rfu7bf':ruq9e5co.get('rfu7bf'),'w9laac':ruq9e5co.get('w9laac',False),'gbwcv6':ruq9e5co.get('gbwcv6'),'yoztp7':ruq9e5co.get('yoztp7'),'pgsb98':ruq9e5co.get('pgsb98',False),'bx1ego':ruq9e5co.get('bx1ego'),'jr87iy':ruq9e5co.get('jr87iy'),'hx0gu4':ruq9e5co.get('hx0gu4'),'t7fr91':ruq9e5co.get('t7fr91'),'en1x2g':ruq9e5co.get('en1x2g',False),'dzjq7w':ruq9e5co.get('dzjq7w'),'yc1nlc':ruq9e5co.get('yc1nlc'),'i1yy1j':ruq9e5co.get('i1yy1j'),'tgr8w2':ruq9e5co.get('tgr8w2',False),'vhbef4':ruq9e5co.get('vhbef4'),'lpug99':ruq9e5co.get('lpug99'),'tn1th1':ruq9e5co.get('tn1th1'),'f4c3ev':ruq9e5co.get('f4c3ev'),'gpm21b':ruq9e5co.get('gpm21b',False),'c6zvlh':ruq9e5co.get('c6zvlh'),'xbtfbs':ruq9e5co.get('xbtfbs'),'qc6dr0':ruq9e5co.get('qc6dr0',False),'buzery':ruq9e5co.get('buzery'),'e0s41k':ruq9e5co.get('e0s41k')}for(mu4fmpkx,ruq9e5co)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda mu4fmpkx:k1wj0tpa[mu4fmpkx]['nf7qne'])
uqjiujv6={'oud2zd':{'pca7zv':10,'xfq3jz':10,'zhbgcj':6,'udt8cq':60,'bohxs7':0,'be2wnf':None,'fuxk0a':iq5c34dx['cxf5x9'],'mjz6us':vvslh9bh('assets/normal.png'),'khkf28':20,'urf1hx':15},'ta5kw3':{'pca7zv':5,'xfq3jz':8,'zhbgcj':8,'udt8cq':90,'bohxs7':999,'be2wnf':'flyback','g8wze4':250,'fuxk0a':iq5c34dx['tjng7l'],'mjz6us':vvslh9bh('assets/boomerang.png'),'khkf28':20,'urf1hx':27},'zm8kb9':{'pca7zv':6,'xfq3jz':6,'zhbgcj':5,'udt8cq':100,'bohxs7':0,'be2wnf':'homing','v6idii':0.08,'fuxk0a':iq5c34dx['t6tbb6'],'mjz6us':vvslh9bh('assets/homing.png'),'khkf28':20,'urf1hx':20},'fkmuso':{'pca7zv':14,'xfq3jz':12,'zhbgcj':4,'udt8cq':50,'bohxs7':3,'be2wnf':'bohxs7','fuxk0a':iq5c34dx['jl6314'],'mjz6us':vvslh9bh('assets/pierce.png'),'khkf28':20,'urf1hx':7},'vlou83':{'pca7zv':7,'xfq3jz':15,'zhbgcj':10,'udt8cq':70,'bohxs7':0,'be2wnf':'explode','gbwcv6':60,'fuxk0a':iq5c34dx['cm3v2p'],'mjz6us':vvslh9bh('assets/explosive.png'),'khkf28':20,'urf1hx':20},'w9mda9':{'pca7zv':9,'xfq3jz':7,'zhbgcj':5,'udt8cq':60,'bohxs7':0,'be2wnf':'split','jo31yh':3,'fuxk0a':iq5c34dx['glmy62'],'mjz6us':vvslh9bh('assets/split.png'),'khkf28':20,'urf1hx':9},'x2s8nn':{'pca7zv':7,'xfq3jz':12,'zhbgcj':6,'udt8cq':90,'bohxs7':0,'be2wnf':None,'fuxk0a':iq5c34dx['mviifr']}}
uyhl1c32={'oud2zd':'Normal Shot','ta5kw3':'Boomerang','zm8kb9':'Homing Shot','fkmuso':'Piercing Shot','vlou83':'Explosive Shot','w9mda9':'Split Shot'}
mjh75lxo={'oud2zd':15,'ta5kw3':25,'zm8kb9':20,'fkmuso':18,'vlou83':35,'w9mda9':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
ygspk9p3=5
def gdg1wjui(a8ax40dt):
 return 1+(a8ax40dt-1)*0.12
def n8k03w0f(a8ax40dt):
 return max(0.65,1-(a8ax40dt-1)*0.07)
oohp6vz4={'swyqml':{'yrp422':'Vitality','rw8p74':'+20% Max Health','ykht8x':8},'eqkwqh':{'yrp422':'Swift Boots','rw8p74':'+8% Move Speed','ykht8x':5},'zmygy0':{'yrp422':'Regeneration','rw8p74':'+1 HP/sec','ykht8x':6},'ckezjs':{'yrp422':'Power','rw8p74':'+6% Weapon Damage','ykht8x':8},'ffkxzu':{'yrp422':'Haste','rw8p74':'-5% Attack Cooldown','ykht8x':6},'ddzwdz':{'yrp422':'Armor','rw8p74':'+5 Defense','ykht8x':6},'edxoq2':{'yrp422':'Wisdom','rw8p74':'+15% XP Gain','ykht8x':5}}
my6wktak={'START_HEALTH':{'ktaq6u':'xgmjmb','yrp422':'Heart Crystal','rw8p74':'+8% Starting Max Health','ykht8x':10,'vcw2lb':15,'ijj0v6':1.35},'START_REGEN':{'ktaq6u':'xgmjmb','yrp422':'Regen Charm','rw8p74':'+0.5 Starting HP/sec','ykht8x':6,'vcw2lb':25,'ijj0v6':1.4},'START_DAMAGE':{'ktaq6u':'pcs4ke','yrp422':'Sharp Edge','rw8p74':'+4% Starting Damage','ykht8x':10,'vcw2lb':20,'ijj0v6':1.35},'START_COOLDOWN':{'ktaq6u':'pcs4ke','yrp422':'Quick Hands','rw8p74':'-3% Starting Cooldown','ykht8x':8,'vcw2lb':25,'ijj0v6':1.4},'START_SPEED':{'ktaq6u':'upgba9','yrp422':'Wind Charm','rw8p74':'+3% Starting Speed','ykht8x':8,'vcw2lb':18,'ijj0v6':1.35},'START_ARMOR':{'ktaq6u':'upgba9','yrp422':'Iron Skin','rw8p74':'+2 Starting Armor','ykht8x':10,'vcw2lb':15,'ijj0v6':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(ruq9e5co['mjz6us']),(ruq9e5co['khkf28'],ruq9e5co['urf1hx']))for(key,ruq9e5co)in uqjiujv6.items()if'mjz6us'in ruq9e5co}
def w8y72ivg(a8ax40dt):
 return 1+0.08*a8ax40dt
def wy0mahym(a8ax40dt):
 return 1+0.03*a8ax40dt
def d448n7od(a8ax40dt):
 return 1+0.04*a8ax40dt
def bihsa7he(a8ax40dt):
 return max(0.7,1-0.03*a8ax40dt)
def hu9n79gi(a8ax40dt):
 return a8ax40dt*2
def j0kgazu4(a8ax40dt):
 return a8ax40dt*0.5
dxmo5bxx=10
oeimvihc=45
bom5igqp=25
r1yzoyn6=2
re7ur23g=15
uccblskr=30
z0xkxwd8=3
hyihair4=(245,245,235)
mn9er14f=(70,130,180)
fq85jsg6=(40,80,120)
f2pcn9t8=(100,160,210)
aye511mk=(60,110,160)
t1w1ht7p=[int(100*1.3**(a8ax40dt-1))for a8ax40dt in range(1,61)]
