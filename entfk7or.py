import os
import sys
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
wrbw2zla=getattr(sys,'_MEIPASS',dnq4fmyz)
def sv5f1bcp(tbxf445c):
 return os.path.join(wrbw2zla,tbxf445c)
(ygspk9p3,tp0lvsnu)=(800,600)
(v83tqll8,cqoldfor)=(2000,2000)
pi3qk2ia=60
m7hv3izk=40
yswjckjl=4
rqf5q14j=30
zxa3kx7e=30
r4874frh=4
ue0ifd0t=140
d60fkhmy=0.01
isj6bw3b=0.045
y38daly8=1.4
cawudtse=40
b8cgvyie=300
s8qjnv8z=6
b18hafey=4
gncxll4z=6
iq5c34dx={'og8cd3':(255,0,0),'ifzkic':(255,102,102),'yaym0w':(139,0,0),'amntfv':(0,255,0),'s1whhk':(144,238,144),'dawe42':(0,100,0),'uu3bfx':(0,0,255),'s0w9ry':(0,255,255),'tjng7l':(0,0,128),'w9mda9':(135,206,235),'buzery':(255,255,0),'bdbpgv':(255,255,224),'fkmuso':(128,128,0),'w2lx2t':(255,165,0),'rlpefj':(255,200,124),'gyjckt':(255,140,0),'wurvqt':(128,0,128),'t7wqp3':(238,130,238),'cparsg':(75,0,130),'zmygy0':(255,192,203),'a8udtt':(255,182,193),'jhke22':(255,105,180),'wzuu80':(139,69,19),'qelb45':(181,101,29),'tmeusw':(92,46,13),'vl62cf':(128,128,128),'kqbsxl':(211,211,211),'p35ikg':(64,64,64),'cxf5x9':(0,128,128),'t6tbb6':(102,178,178),'a3g47r':(0,77,77),'gzyt91':(255,0,255),'mviifr':(218,112,214),'nomuwa':(139,0,139),'qk0lth':(255,215,0),'kk2y77':(192,192,192),'oud2zd':(128,0,0),'edxoq2':(64,224,208),'e56waf':(250,128,114),'ilohhc':(255,127,80),'za5ivr':(245,245,220),'p0s1f5':(255,255,240),'qye0qz':(240,230,140),'npva5k':(0,0,0),'mmgvu4':(255,255,255)}
hyihair4=(90,90,100)
qqu7eeqt=(50,50,58)
cq5uznof=(120,120,132)
wa11dpg8=(70,70,80)
gyljexq7=['amntfv','s0w9ry','uu3bfx','wurvqt','gzyt91','w2lx2t','og8cd3','yaym0w','vl62cf','qk0lth']
def bwiykid9(xwqvr1h6):
 return{'oarxab':100*1.3**(xwqvr1h6-1),'tgr8w2':min(yswjckjl*0.75,1.3*1.13**(xwqvr1h6-1)),'e0s41k':10*1.25**(xwqvr1h6-1),'v00vhm':5*1.2**(xwqvr1h6-1),'qc6dr0':max(10,60*0.9**(xwqvr1h6-1)),'qbtr23':26*1.27**(xwqvr1h6-1)}
s0clbr7t={'fv51zl':{'khkf28':1,'xfq3jz':'amntfv','rfu7bf':(1.0,1.0,1.0,1.0,1.0,1.0)},'az3m55':{'khkf28':2,'xfq3jz':'s0w9ry','rfu7bf':(0.6,1.8,0.7,0.8,0.8,1.0),'bx1ego':True,'onlt8d':150,'rw8p74':2.5,'mrf5a7':20,'jr87iy':90},'l4f9ye':{'khkf28':3,'xfq3jz':'vl62cf','rfu7bf':(2.6,0.45,0.6,1.6,1.3,1.3),'yc1nlc':True,'igc9ho':60,'ozdcuj':1,'urf1hx':30},'rn16ux':{'khkf28':4,'xfq3jz':'wurvqt','rfu7bf':(0.7,0.7,1.3,0.7,1.4,1.2),'voeytl':True,'th2p39':260,'f4c3ev':7},'l7dknn':{'khkf28':5,'xfq3jz':'w2lx2t','rfu7bf':(1.6,0.85,1.6,1.1,1.1,1.4),'v6idii':True,'nf7qne':40,'n5nhqr':2.0},'ga1arr':{'khkf28':6,'xfq3jz':'gzyt91','rfu7bf':(0.55,2.1,1.5,0.6,0.7,1.3),'vhbef4':True,'xbtfbs':10,'prf7bn':120,'gpm21b':150,'zhbgcj':25},'bfbuvl':{'khkf28':7,'xfq3jz':'og8cd3','rfu7bf':(0.8,1.1,1.0,0.8,1.0,1.3),'g8wze4':True,'dzjq7w':70},'eqkwqh':{'khkf28':8,'xfq3jz':'yaym0w','rfu7bf':(1.8,0.75,0.9,2.4,1.2,1.5),'kp82kb':True,'vcw2lb':120,'ktaq6u':0.5},'ntxrgn':{'khkf28':9,'xfq3jz':'qk0lth','rfu7bf':(0.35,1.5,0.5,0.5,0.6,0.8),'jo31yh':3},'p2xrw6':{'khkf28':10,'xfq3jz':'nomuwa','rfu7bf':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={got7txkd:{'oarxab':int(bwiykid9(lztkkfzz['khkf28'])['oarxab']*lztkkfzz['rfu7bf'][0]),'tgr8w2':round(bwiykid9(lztkkfzz['khkf28'])['tgr8w2']*lztkkfzz['rfu7bf'][1],2),'e0s41k':int(bwiykid9(lztkkfzz['khkf28'])['e0s41k']*lztkkfzz['rfu7bf'][2]),'v00vhm':int(bwiykid9(lztkkfzz['khkf28'])['v00vhm']*lztkkfzz['rfu7bf'][3]),'qc6dr0':max(10,int(bwiykid9(lztkkfzz['khkf28'])['qc6dr0']*lztkkfzz['rfu7bf'][4])),'qbtr23':int(bwiykid9(lztkkfzz['khkf28'])['qbtr23']*lztkkfzz['rfu7bf'][5]),'xfq3jz':iq5c34dx[lztkkfzz['xfq3jz']],'khkf28':lztkkfzz['khkf28'],'voeytl':lztkkfzz.get('voeytl',False),'th2p39':lztkkfzz.get('th2p39'),'f4c3ev':lztkkfzz.get('f4c3ev'),'g8wze4':lztkkfzz.get('g8wze4',False),'dzjq7w':lztkkfzz.get('dzjq7w'),'jo31yh':lztkkfzz.get('jo31yh'),'bx1ego':lztkkfzz.get('bx1ego',False),'onlt8d':lztkkfzz.get('onlt8d'),'rw8p74':lztkkfzz.get('rw8p74'),'mrf5a7':lztkkfzz.get('mrf5a7'),'jr87iy':lztkkfzz.get('jr87iy'),'yc1nlc':lztkkfzz.get('yc1nlc',False),'igc9ho':lztkkfzz.get('igc9ho'),'ozdcuj':lztkkfzz.get('ozdcuj'),'urf1hx':lztkkfzz.get('urf1hx'),'vhbef4':lztkkfzz.get('vhbef4',False),'xbtfbs':lztkkfzz.get('xbtfbs'),'prf7bn':lztkkfzz.get('prf7bn'),'gpm21b':lztkkfzz.get('gpm21b'),'zhbgcj':lztkkfzz.get('zhbgcj'),'v6idii':lztkkfzz.get('v6idii',False),'nf7qne':lztkkfzz.get('nf7qne'),'n5nhqr':lztkkfzz.get('n5nhqr'),'kp82kb':lztkkfzz.get('kp82kb',False),'vcw2lb':lztkkfzz.get('vcw2lb'),'ktaq6u':lztkkfzz.get('ktaq6u')}for(got7txkd,lztkkfzz)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda got7txkd:k1wj0tpa[got7txkd]['khkf28'])
uqjiujv6={'kqbrmq':{'tgr8w2':10,'hx0gu4':10,'pca7zv':6,'upgba9':60,'agbl2q':0,'ujqigy':None,'xfq3jz':iq5c34dx['mmgvu4'],'r7myow':sv5f1bcp('assets/normal.png'),'hipi78':20,'mjz6us':15},'cbpgyv':{'tgr8w2':5,'hx0gu4':8,'pca7zv':8,'upgba9':90,'agbl2q':999,'ujqigy':'flyback','i1yy1j':250,'xfq3jz':iq5c34dx['w2lx2t'],'r7myow':sv5f1bcp('assets/boomerang.png'),'hipi78':20,'mjz6us':27},'bjd5n3':{'tgr8w2':6,'hx0gu4':6,'pca7zv':5,'upgba9':100,'agbl2q':0,'ujqigy':'homing','xgmjmb':0.08,'xfq3jz':iq5c34dx['gzyt91'],'r7myow':sv5f1bcp('assets/homing.png'),'hipi78':20,'mjz6us':20},'cm3v2p':{'tgr8w2':14,'hx0gu4':12,'pca7zv':4,'upgba9':50,'agbl2q':3,'ujqigy':'agbl2q','xfq3jz':iq5c34dx['s0w9ry'],'r7myow':sv5f1bcp('assets/pierce.png'),'hipi78':20,'mjz6us':7},'r6q37c':{'tgr8w2':7,'hx0gu4':15,'pca7zv':10,'upgba9':70,'agbl2q':0,'ujqigy':'explode','dzjq7w':60,'xfq3jz':iq5c34dx['og8cd3'],'r7myow':sv5f1bcp('assets/explosive.png'),'hipi78':20,'mjz6us':20},'hpvwzo':{'tgr8w2':9,'hx0gu4':7,'pca7zv':5,'upgba9':60,'agbl2q':0,'ujqigy':'split','lpug99':3,'xfq3jz':iq5c34dx['qk0lth'],'r7myow':sv5f1bcp('assets/split.png'),'hipi78':20,'mjz6us':9},'x1qwee':{'tgr8w2':7,'hx0gu4':12,'pca7zv':6,'upgba9':90,'agbl2q':0,'ujqigy':None,'xfq3jz':iq5c34dx['wurvqt']}}
uyhl1c32={'kqbrmq':'Normal Shot','cbpgyv':'Boomerang','bjd5n3':'Homing Shot','cm3v2p':'Piercing Shot','r6q37c':'Explosive Shot','hpvwzo':'Split Shot'}
mjh75lxo={'kqbrmq':15,'cbpgyv':25,'bjd5n3':20,'cm3v2p':18,'r6q37c':35,'hpvwzo':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
v4u89yjb=5
def gdg1wjui(xwqvr1h6):
 return 1+(xwqvr1h6-1)*0.12
def n8k03w0f(xwqvr1h6):
 return max(0.65,1-(xwqvr1h6-1)*0.07)
rcfnfhol={'jyzqii':{'udt8cq':'Vitality','w9laac':'+20% Max Health','hrctlt':8},'m44c68':{'udt8cq':'Swift Boots','w9laac':'+8% Move Speed','hrctlt':5},'y3lxch':{'udt8cq':'Regeneration','w9laac':'+1 HP/sec','hrctlt':6},'z9kvls':{'udt8cq':'Power','w9laac':'+6% Weapon Damage','hrctlt':8},'c14cqe':{'udt8cq':'Haste','w9laac':'-5% Attack Cooldown','hrctlt':6},'eff1bl':{'udt8cq':'Armor','w9laac':'+5 Defense','hrctlt':6},'hzj7ub':{'udt8cq':'Wisdom','w9laac':'+15% XP Gain','hrctlt':5}}
jsylztgx={'START_HEALTH':{'fuxk0a':'futios','udt8cq':'Heart Crystal','w9laac':'+8% Starting Max Health','hrctlt':10,'t00ucr':15,'t7fr91':1.35},'START_REGEN':{'fuxk0a':'futios','udt8cq':'Regen Charm','w9laac':'+0.5 Starting HP/sec','hrctlt':6,'t00ucr':25,'t7fr91':1.4},'START_DAMAGE':{'fuxk0a':'pgsb98','udt8cq':'Sharp Edge','w9laac':'+4% Starting Damage','hrctlt':10,'t00ucr':20,'t7fr91':1.35},'START_COOLDOWN':{'fuxk0a':'pgsb98','udt8cq':'Quick Hands','w9laac':'-3% Starting Cooldown','hrctlt':8,'t00ucr':25,'t7fr91':1.4},'START_SPEED':{'fuxk0a':'bohxs7','udt8cq':'Wind Charm','w9laac':'+3% Starting Speed','hrctlt':8,'t00ucr':18,'t7fr91':1.35},'START_ARMOR':{'fuxk0a':'bohxs7','udt8cq':'Iron Skin','w9laac':'+2 Starting Armor','hrctlt':10,'t00ucr':15,'t7fr91':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(lztkkfzz['r7myow']),(lztkkfzz['hipi78'],lztkkfzz['mjz6us']))for(key,lztkkfzz)in uqjiujv6.items()if'r7myow'in lztkkfzz}
def d448n7od(xwqvr1h6):
 return 1+0.08*xwqvr1h6
def y8bv78hu(xwqvr1h6):
 return 1+0.03*xwqvr1h6
def bihsa7he(xwqvr1h6):
 return 1+0.04*xwqvr1h6
def k3z6bz8u(xwqvr1h6):
 return max(0.7,1-0.03*xwqvr1h6)
def a62c9t19(xwqvr1h6):
 return xwqvr1h6*2
def jl90pxrl(xwqvr1h6):
 return xwqvr1h6*0.5
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
m53a5qbs=[int(100*1.3**(xwqvr1h6-1))for xwqvr1h6 in range(1,61)]
