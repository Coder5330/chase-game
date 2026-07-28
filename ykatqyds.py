import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def ykipu1wy(d1hm38ks):
 return os.path.join(dnq4fmyz,d1hm38ks)
(cqoldfor,tp0lvsnu)=(800,600)
(m53a5qbs,v83tqll8)=(2000,2000)
pi3qk2ia=60
vve92mpn=40
yswjckjl=4
rqf5q14j=30
zxa3kx7e=30
r4874frh=4
ue0ifd0t=140
d60fkhmy=0.01
isj6bw3b=0.045
m7hv3izk=1.4
cawudtse=40
b8cgvyie=300
y38daly8=6
s8qjnv8z=4
gncxll4z=6
iq5c34dx={'az3m55':(255,0,0),'kqbrmq':(255,102,102),'bjd5n3':(139,0,0),'kqbsxl':(0,255,0),'oud2zd':(144,238,144),'vl62cf':(0,100,0),'wkvls9':(0,0,255),'a3g47r':(0,255,255),'wurvqt':(0,0,128),'edxoq2':(135,206,235),'fuxk0a':(255,255,0),'w2lx2t':(255,255,224),'y3lxch':(128,128,0),'e56waf':(255,165,0),'jyzqii':(255,200,124),'fv51zl':(255,140,0),'m44c68':(128,0,128),'ktaq6u':(238,130,238),'ifzkic':(75,0,130),'w9mda9':(255,192,203),'tjng7l':(255,182,193),'a8udtt':(255,105,180),'aq20hw':(139,69,19),'swyqml':(181,101,29),'r6q37c':(92,46,13),'qelb45':(128,128,128),'gzyt91':(211,211,211),'qk0lth':(64,64,64),'qc6dr0':(0,128,128),'fkmuso':(102,178,178),'jhke22':(0,77,77),'mviifr':(255,0,255),'eqkwqh':(218,112,214),'amntfv':(139,0,139),'qye0qz':(255,215,0),'cxf5x9':(192,192,192),'cm3v2p':(128,0,0),'vcw2lb':(64,224,208),'ntxrgn':(250,128,114),'yaym0w':(255,127,80),'nszwd0':(245,245,220),'t6tbb6':(255,255,240),'bdbpgv':(240,230,140),'utd0v2':(0,0,0),'kp82kb':(255,255,255)}
hyihair4=(90,90,100)
qqu7eeqt=(50,50,58)
cq5uznof=(120,120,132)
wa11dpg8=(70,70,80)
gyljexq7=['kqbsxl','a3g47r','wkvls9','m44c68','mviifr','e56waf','az3m55','bjd5n3','qelb45','qye0qz']
def sld4d6af(a8ax40dt):
 return{'jz6wmd':100*1.3**(a8ax40dt-1),'c6zvlh':min(yswjckjl*0.75,1.3*1.13**(a8ax40dt-1)),'pcs4ke':10*1.25**(a8ax40dt-1),'i1yy1j':5*1.2**(a8ax40dt-1),'ijj0v6':max(10,60*0.9**(a8ax40dt-1)),'zhywm7':26*1.27**(a8ax40dt-1)}
s0clbr7t={'s1whhk':{'gekxdr':1,'onlt8d':'kqbsxl','yoztp7':(1.0,1.0,1.0,1.0,1.0,1.0)},'mmgvu4':{'gekxdr':2,'onlt8d':'a3g47r','yoztp7':(0.6,1.8,0.7,0.8,0.8,1.0),'w9laac':True,'g8wze4':150,'en1x2g':2.5,'gbwcv6':20,'nddqhk':90},'e0s41k':{'gekxdr':3,'onlt8d':'qelb45','yoztp7':(2.6,0.45,0.6,1.6,1.3,1.3),'riny2e':True,'r7myow':60,'ykht8x':1,'udt8cq':30},'n9fkxz':{'gekxdr':4,'onlt8d':'m44c68','yoztp7':(0.7,0.7,1.3,0.7,1.4,1.2),'tgr8w2':True,'ujqigy':260,'jo31yh':7},'nomuwa':{'gekxdr':5,'onlt8d':'e56waf','yoztp7':(1.6,0.85,1.6,1.1,1.1,1.4),'gv4k00':True,'s6pb90':40,'hipi78':2.0},'rcqe4l':{'gekxdr':6,'onlt8d':'mviifr','yoztp7':(0.55,2.1,1.5,0.6,0.7,1.3),'nf7qne':True,'khkf28':10,'xgmjmb':120,'sce4qg':150,'lpug99':25},'l7wr0r':{'gekxdr':7,'onlt8d':'az3m55','yoztp7':(0.8,1.1,1.0,0.8,1.0,1.3),'ozdcuj':True,'mjz6us':70},'l4f9ye':{'gekxdr':8,'onlt8d':'bjd5n3','yoztp7':(1.8,0.75,0.9,2.4,1.2,1.5),'t7fr91':True,'xfq3jz':120,'pgsb98':0.5},'buzery':{'gekxdr':9,'onlt8d':'qye0qz','yoztp7':(0.35,1.5,0.5,0.5,0.6,0.8),'gpm21b':3},'cparsg':{'gekxdr':10,'onlt8d':'amntfv','yoztp7':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={lgbpj4uf:{'jz6wmd':int(sld4d6af(iie0rnuj['gekxdr'])['jz6wmd']*iie0rnuj['yoztp7'][0]),'c6zvlh':round(sld4d6af(iie0rnuj['gekxdr'])['c6zvlh']*iie0rnuj['yoztp7'][1],2),'pcs4ke':int(sld4d6af(iie0rnuj['gekxdr'])['pcs4ke']*iie0rnuj['yoztp7'][2]),'i1yy1j':int(sld4d6af(iie0rnuj['gekxdr'])['i1yy1j']*iie0rnuj['yoztp7'][3]),'ijj0v6':max(10,int(sld4d6af(iie0rnuj['gekxdr'])['ijj0v6']*iie0rnuj['yoztp7'][4])),'zhywm7':int(sld4d6af(iie0rnuj['gekxdr'])['zhywm7']*iie0rnuj['yoztp7'][5]),'onlt8d':iq5c34dx[iie0rnuj['onlt8d']],'gekxdr':iie0rnuj['gekxdr'],'tgr8w2':iie0rnuj.get('tgr8w2',False),'ujqigy':iie0rnuj.get('ujqigy'),'jo31yh':iie0rnuj.get('jo31yh'),'ozdcuj':iie0rnuj.get('ozdcuj',False),'mjz6us':iie0rnuj.get('mjz6us'),'gpm21b':iie0rnuj.get('gpm21b'),'w9laac':iie0rnuj.get('w9laac',False),'g8wze4':iie0rnuj.get('g8wze4'),'en1x2g':iie0rnuj.get('en1x2g'),'gbwcv6':iie0rnuj.get('gbwcv6'),'nddqhk':iie0rnuj.get('nddqhk'),'riny2e':iie0rnuj.get('riny2e',False),'r7myow':iie0rnuj.get('r7myow'),'ykht8x':iie0rnuj.get('ykht8x'),'udt8cq':iie0rnuj.get('udt8cq'),'nf7qne':iie0rnuj.get('nf7qne',False),'khkf28':iie0rnuj.get('khkf28'),'xgmjmb':iie0rnuj.get('xgmjmb'),'sce4qg':iie0rnuj.get('sce4qg'),'lpug99':iie0rnuj.get('lpug99'),'gv4k00':iie0rnuj.get('gv4k00',False),'s6pb90':iie0rnuj.get('s6pb90'),'hipi78':iie0rnuj.get('hipi78'),'t7fr91':iie0rnuj.get('t7fr91',False),'xfq3jz':iie0rnuj.get('xfq3jz'),'pgsb98':iie0rnuj.get('pgsb98')}for(lgbpj4uf,iie0rnuj)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda lgbpj4uf:k1wj0tpa[lgbpj4uf]['gekxdr'])
uqjiujv6={'og8cd3':{'c6zvlh':10,'v00vhm':10,'prf7bn':6,'f4c3ev':60,'pca7zv':0,'xbtfbs':None,'onlt8d':iq5c34dx['kp82kb'],'bohxs7':ykipu1wy('assets/normal.png'),'ozawny':20,'upgba9':15},'zgvz9a':{'c6zvlh':5,'v00vhm':8,'prf7bn':8,'f4c3ev':90,'pca7zv':999,'xbtfbs':'flyback','yrp422':250,'onlt8d':iq5c34dx['e56waf'],'bohxs7':ykipu1wy('assets/boomerang.png'),'ozawny':20,'upgba9':27},'rlpefj':{'c6zvlh':6,'v00vhm':6,'prf7bn':5,'f4c3ev':100,'pca7zv':0,'xbtfbs':'homing','qbtr23':0.08,'onlt8d':iq5c34dx['mviifr'],'bohxs7':ykipu1wy('assets/homing.png'),'ozawny':20,'upgba9':20},'kk2y77':{'c6zvlh':14,'v00vhm':12,'prf7bn':4,'f4c3ev':50,'pca7zv':3,'xbtfbs':'pca7zv','onlt8d':iq5c34dx['a3g47r'],'bohxs7':ykipu1wy('assets/pierce.png'),'ozawny':20,'upgba9':7},'p0s1f5':{'c6zvlh':7,'v00vhm':15,'prf7bn':10,'f4c3ev':70,'pca7zv':0,'xbtfbs':'explode','mjz6us':60,'onlt8d':iq5c34dx['az3m55'],'bohxs7':ykipu1wy('assets/explosive.png'),'ozawny':20,'upgba9':20},'hzj7ub':{'c6zvlh':9,'v00vhm':7,'prf7bn':5,'f4c3ev':60,'pca7zv':0,'xbtfbs':'split','v6idii':3,'onlt8d':iq5c34dx['qye0qz'],'bohxs7':ykipu1wy('assets/split.png'),'ozawny':20,'upgba9':9},'c1l631':{'c6zvlh':7,'v00vhm':12,'prf7bn':6,'f4c3ev':90,'pca7zv':0,'xbtfbs':None,'onlt8d':iq5c34dx['m44c68']}}
uyhl1c32={'og8cd3':'Normal Shot','zgvz9a':'Boomerang','rlpefj':'Homing Shot','kk2y77':'Piercing Shot','p0s1f5':'Explosive Shot','hzj7ub':'Split Shot'}
mjh75lxo={'og8cd3':15,'zgvz9a':25,'rlpefj':20,'kk2y77':18,'p0s1f5':35,'hzj7ub':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
ygspk9p3=5
def w2sq3b9s(a8ax40dt):
 return 1+(a8ax40dt-1)*0.12
def x3zo7utx(a8ax40dt):
 return max(0.65,1-(a8ax40dt-1)*0.07)
rcfnfhol={'zmygy0':{'rfu7bf':'Vitality','yc1nlc':'+20% Max Health','th2p39':8},'t7wqp3':{'rfu7bf':'Swift Boots','yc1nlc':'+8% Move Speed','th2p39':5},'hpvwzo':{'rfu7bf':'Regeneration','yc1nlc':'+1 HP/sec','th2p39':6},'p2xrw6':{'rfu7bf':'Power','yc1nlc':'+6% Weapon Damage','th2p39':8},'gyjckt':{'rfu7bf':'Haste','yc1nlc':'-5% Attack Cooldown','th2p39':6},'s2gqu7':{'rfu7bf':'Armor','yc1nlc':'+5 Defense','th2p39':6},'t00ucr':{'rfu7bf':'Wisdom','yc1nlc':'+15% XP Gain','th2p39':5}}
jsylztgx={'START_HEALTH':{'bx1ego':'jfquv9','rfu7bf':'Heart Crystal','yc1nlc':'+8% Starting Max Health','th2p39':10,'hx0gu4':15,'kj2jvq':1.35},'START_REGEN':{'bx1ego':'jfquv9','rfu7bf':'Regen Charm','yc1nlc':'+0.5 Starting HP/sec','th2p39':6,'hx0gu4':25,'kj2jvq':1.4},'START_DAMAGE':{'bx1ego':'rw8p74','rfu7bf':'Sharp Edge','yc1nlc':'+4% Starting Damage','th2p39':10,'hx0gu4':20,'kj2jvq':1.35},'START_COOLDOWN':{'bx1ego':'rw8p74','rfu7bf':'Quick Hands','yc1nlc':'-3% Starting Cooldown','th2p39':8,'hx0gu4':25,'kj2jvq':1.4},'START_SPEED':{'bx1ego':'zhbgcj','rfu7bf':'Wind Charm','yc1nlc':'+3% Starting Speed','th2p39':8,'hx0gu4':18,'kj2jvq':1.35},'START_ARMOR':{'bx1ego':'zhbgcj','rfu7bf':'Iron Skin','yc1nlc':'+2 Starting Armor','th2p39':10,'hx0gu4':15,'kj2jvq':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(iie0rnuj['bohxs7']),(iie0rnuj['ozawny'],iie0rnuj['upgba9']))for(key,iie0rnuj)in uqjiujv6.items()if'bohxs7'in iie0rnuj}
def y8bv78hu(a8ax40dt):
 return 1+0.08*a8ax40dt
def mmn32u1i(a8ax40dt):
 return 1+0.03*a8ax40dt
def w8y72ivg(a8ax40dt):
 return 1+0.04*a8ax40dt
def d448n7od(a8ax40dt):
 return max(0.7,1-0.03*a8ax40dt)
def s8438tgb(a8ax40dt):
 return a8ax40dt*2
def pf0i9g5d(a8ax40dt):
 return a8ax40dt*0.5
dxmo5bxx=10
oeimvihc=45
bom5igqp=25
r1yzoyn6=2
re7ur23g=15
uccblskr=30
n2vlpys2=3
z0xkxwd8=(245,245,235)
mn9er14f=(70,130,180)
fq85jsg6=(40,80,120)
f2pcn9t8=(100,160,210)
aye511mk=(60,110,160)
t1w1ht7p=[int(100*1.3**(a8ax40dt-1))for a8ax40dt in range(1,61)]
