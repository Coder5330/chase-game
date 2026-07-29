import os
import sys
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
wrbw2zla=getattr(sys,'_MEIPASS',dnq4fmyz)
def nrpj1epk(tbxf445c):
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
iq5c34dx={'mviifr':(255,0,0),'kqbsxl':(255,102,102),'p35ikg':(139,0,0),'p2xrw6':(0,255,0),'p0s1f5':(144,238,144),'s0w9ry':(0,100,0),'x1qwee':(0,0,255),'wzuu80':(0,255,255),'swyqml':(0,0,128),'y3lxch':(135,206,235),'edxoq2':(255,255,0),'rlpefj':(255,255,224),'oud2zd':(128,128,0),'jyzqii':(255,165,0),'qye0qz':(255,200,124),'tmeusw':(255,140,0),'w2lx2t':(128,0,128),'ntxrgn':(238,130,238),'amntfv':(75,0,130),'fkmuso':(255,192,203),'qelb45':(255,182,193),'vl62cf':(255,105,180),'npva5k':(139,69,19),'jhke22':(181,101,29),'c14cqe':(92,46,13),'a3g47r':(128,128,128),'cparsg':(211,211,211),'ilohhc':(64,64,64),'az3m55':(0,128,128),'s1whhk':(102,178,178),'dawe42':(0,77,77),'ifzkic':(255,0,255),'tjng7l':(218,112,214),'z9kvls':(139,0,139),'yaym0w':(255,215,0),'og8cd3':(192,192,192),'t6tbb6':(128,0,0),'hpvwzo':(64,224,208),'zmygy0':(250,128,114),'cbpgyv':(255,127,80),'rn16ux':(245,245,220),'fv51zl':(255,255,240),'bjd5n3':(240,230,140),'eff1bl':(0,0,0),'l4f9ye':(255,255,255)}
hyihair4=(90,90,100)
qqu7eeqt=(50,50,58)
cq5uznof=(120,120,132)
wa11dpg8=(70,70,80)
gyljexq7=['p2xrw6','wzuu80','x1qwee','w2lx2t','ifzkic','jyzqii','mviifr','p35ikg','a3g47r','yaym0w']
def yw5py6b2(y2f7atwy):
 return{'yc1nlc':100*1.3**(y2f7atwy-1),'be2wnf':min(yswjckjl*0.75,1.3*1.13**(y2f7atwy-1)),'t7wqp3':10*1.25**(y2f7atwy-1),'mrf5a7':5*1.2**(y2f7atwy-1),'mmgvu4':max(10,60*0.9**(y2f7atwy-1)),'futios':26*1.27**(y2f7atwy-1)}
s0clbr7t={'r6q37c':{'n5nhqr':1,'t00ucr':'p2xrw6','upgba9':(1.0,1.0,1.0,1.0,1.0,1.0)},'eqkwqh':{'n5nhqr':2,'t00ucr':'wzuu80','upgba9':(0.6,1.8,0.7,0.8,0.8,1.0),'xfq3jz':True,'hx0gu4':150,'bx1ego':2.5,'t7fr91':20,'pgsb98':90},'m44c68':{'n5nhqr':3,'t00ucr':'a3g47r','upgba9':(2.6,0.45,0.6,1.6,1.3,1.3),'g8wze4':True,'en1x2g':60,'i1yy1j':1,'dzjq7w':30},'eolaq6':{'n5nhqr':4,'t00ucr':'w2lx2t','upgba9':(0.7,0.7,1.3,0.7,1.4,1.2),'ua6wix':True,'rfu7bf':260,'bohxs7':7},'uu3bfx':{'n5nhqr':5,'t00ucr':'jyzqii','upgba9':(1.6,0.85,1.6,1.1,1.1,1.4),'prf7bn':True,'xbtfbs':40,'gpm21b':2.0},'qz09wf':{'n5nhqr':6,'t00ucr':'ifzkic','upgba9':(0.55,2.1,1.5,0.6,0.7,1.3),'ujqigy':True,'tn1th1':10,'tgr8w2':120,'lpug99':150,'agbl2q':25},'ga1arr':{'n5nhqr':7,'t00ucr':'mviifr','upgba9':(0.8,1.1,1.0,0.8,1.0,1.3),'v00vhm':True,'nddqhk':70},'wurvqt':{'n5nhqr':8,'t00ucr':'p35ikg','upgba9':(1.8,0.75,0.9,2.4,1.2,1.5),'e0s41k':True,'hzj7ub':120,'buzery':0.5},'w9mda9':{'n5nhqr':9,'t00ucr':'yaym0w','upgba9':(0.35,1.5,0.5,0.5,0.6,0.8),'zhbgcj':3},'nomuwa':{'n5nhqr':10,'t00ucr':'z9kvls','upgba9':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={got7txkd:{'yc1nlc':int(yw5py6b2(f2sehe2a['n5nhqr'])['yc1nlc']*f2sehe2a['upgba9'][0]),'be2wnf':round(yw5py6b2(f2sehe2a['n5nhqr'])['be2wnf']*f2sehe2a['upgba9'][1],2),'t7wqp3':int(yw5py6b2(f2sehe2a['n5nhqr'])['t7wqp3']*f2sehe2a['upgba9'][2]),'mrf5a7':int(yw5py6b2(f2sehe2a['n5nhqr'])['mrf5a7']*f2sehe2a['upgba9'][3]),'mmgvu4':max(10,int(yw5py6b2(f2sehe2a['n5nhqr'])['mmgvu4']*f2sehe2a['upgba9'][4])),'futios':int(yw5py6b2(f2sehe2a['n5nhqr'])['futios']*f2sehe2a['upgba9'][5]),'t00ucr':iq5c34dx[f2sehe2a['t00ucr']],'n5nhqr':f2sehe2a['n5nhqr'],'ua6wix':f2sehe2a.get('ua6wix',False),'rfu7bf':f2sehe2a.get('rfu7bf'),'bohxs7':f2sehe2a.get('bohxs7'),'v00vhm':f2sehe2a.get('v00vhm',False),'nddqhk':f2sehe2a.get('nddqhk'),'zhbgcj':f2sehe2a.get('zhbgcj'),'xfq3jz':f2sehe2a.get('xfq3jz',False),'hx0gu4':f2sehe2a.get('hx0gu4'),'bx1ego':f2sehe2a.get('bx1ego'),'t7fr91':f2sehe2a.get('t7fr91'),'pgsb98':f2sehe2a.get('pgsb98'),'g8wze4':f2sehe2a.get('g8wze4',False),'en1x2g':f2sehe2a.get('en1x2g'),'i1yy1j':f2sehe2a.get('i1yy1j'),'dzjq7w':f2sehe2a.get('dzjq7w'),'ujqigy':f2sehe2a.get('ujqigy',False),'tn1th1':f2sehe2a.get('tn1th1'),'tgr8w2':f2sehe2a.get('tgr8w2'),'lpug99':f2sehe2a.get('lpug99'),'agbl2q':f2sehe2a.get('agbl2q'),'prf7bn':f2sehe2a.get('prf7bn',False),'xbtfbs':f2sehe2a.get('xbtfbs'),'gpm21b':f2sehe2a.get('gpm21b'),'e0s41k':f2sehe2a.get('e0s41k',False),'hzj7ub':f2sehe2a.get('hzj7ub'),'buzery':f2sehe2a.get('buzery')}for(got7txkd,f2sehe2a)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda got7txkd:k1wj0tpa[got7txkd]['n5nhqr'])
uqjiujv6={'gzyt91':{'be2wnf':10,'ijj0v6':10,'voeytl':6,'r7myow':60,'zq9bc2':0,'yoztp7':None,'t00ucr':iq5c34dx['l4f9ye'],'oarxab':nrpj1epk('assets/normal.png'),'sce4qg':20,'igc9ho':15},'za5ivr':{'be2wnf':5,'ijj0v6':8,'voeytl':8,'r7myow':90,'zq9bc2':999,'yoztp7':'flyback','gbwcv6':250,'t00ucr':iq5c34dx['jyzqii'],'oarxab':nrpj1epk('assets/boomerang.png'),'sce4qg':20,'igc9ho':27},'qk0lth':{'be2wnf':6,'ijj0v6':6,'voeytl':5,'r7myow':100,'zq9bc2':0,'yoztp7':'homing','c6zvlh':0.08,'t00ucr':iq5c34dx['ifzkic'],'oarxab':nrpj1epk('assets/homing.png'),'sce4qg':20,'igc9ho':20},'kqbrmq':{'be2wnf':14,'ijj0v6':12,'voeytl':4,'r7myow':50,'zq9bc2':3,'yoztp7':'zq9bc2','t00ucr':iq5c34dx['wzuu80'],'oarxab':nrpj1epk('assets/pierce.png'),'sce4qg':20,'igc9ho':7},'gyjckt':{'be2wnf':7,'ijj0v6':15,'voeytl':10,'r7myow':70,'zq9bc2':0,'yoztp7':'explode','nddqhk':60,'t00ucr':iq5c34dx['mviifr'],'oarxab':nrpj1epk('assets/explosive.png'),'sce4qg':20,'igc9ho':20},'kk2y77':{'be2wnf':9,'ijj0v6':7,'voeytl':5,'r7myow':60,'zq9bc2':0,'yoztp7':'split','pca7zv':3,'t00ucr':iq5c34dx['yaym0w'],'oarxab':nrpj1epk('assets/split.png'),'sce4qg':20,'igc9ho':9},'fzeeqn':{'be2wnf':7,'ijj0v6':12,'voeytl':6,'r7myow':90,'zq9bc2':0,'yoztp7':None,'t00ucr':iq5c34dx['w2lx2t']}}
uyhl1c32={'gzyt91':'Normal Shot','za5ivr':'Boomerang','qk0lth':'Homing Shot','kqbrmq':'Piercing Shot','gyjckt':'Explosive Shot','kk2y77':'Split Shot'}
mjh75lxo={'gzyt91':15,'za5ivr':25,'qk0lth':20,'kqbrmq':18,'gyjckt':35,'kk2y77':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
v4u89yjb=5
def n8k03w0f(y2f7atwy):
 return 1+(y2f7atwy-1)*0.12
def cu8el501(y2f7atwy):
 return max(0.65,1-(y2f7atwy-1)*0.07)
rcfnfhol={'bdbpgv':{'mjz6us':'Vitality','onlt8d':'+20% Max Health','udt8cq':8},'e56waf':{'mjz6us':'Swift Boots','onlt8d':'+8% Move Speed','udt8cq':5},'cm3v2p':{'mjz6us':'Regeneration','onlt8d':'+1 HP/sec','udt8cq':6},'l7dknn':{'mjz6us':'Power','onlt8d':'+6% Weapon Damage','udt8cq':8},'bfbuvl':{'mjz6us':'Haste','onlt8d':'-5% Attack Cooldown','udt8cq':6},'g5dlxz':{'mjz6us':'Armor','onlt8d':'+5 Defense','udt8cq':6},'cxf5x9':{'mjz6us':'Wisdom','onlt8d':'+15% XP Gain','udt8cq':5}}
jsylztgx={'START_HEALTH':{'vcw2lb':'nf7qne','mjz6us':'Heart Crystal','onlt8d':'+8% Starting Max Health','udt8cq':10,'qc6dr0':15,'pcs4ke':1.35},'START_REGEN':{'vcw2lb':'nf7qne','mjz6us':'Regen Charm','onlt8d':'+0.5 Starting HP/sec','udt8cq':6,'qc6dr0':25,'pcs4ke':1.4},'START_DAMAGE':{'vcw2lb':'fuxk0a','mjz6us':'Sharp Edge','onlt8d':'+4% Starting Damage','udt8cq':10,'qc6dr0':20,'pcs4ke':1.35},'START_COOLDOWN':{'vcw2lb':'fuxk0a','mjz6us':'Quick Hands','onlt8d':'-3% Starting Cooldown','udt8cq':8,'qc6dr0':25,'pcs4ke':1.4},'START_SPEED':{'vcw2lb':'jz6wmd','mjz6us':'Wind Charm','onlt8d':'+3% Starting Speed','udt8cq':8,'qc6dr0':18,'pcs4ke':1.35},'START_ARMOR':{'vcw2lb':'jz6wmd','mjz6us':'Iron Skin','onlt8d':'+2 Starting Armor','udt8cq':10,'qc6dr0':15,'pcs4ke':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(f2sehe2a['oarxab']),(f2sehe2a['sce4qg'],f2sehe2a['igc9ho']))for(key,f2sehe2a)in uqjiujv6.items()if'oarxab'in f2sehe2a}
def jl90pxrl(y2f7atwy):
 return 1+0.08*y2f7atwy
def pf0i9g5d(y2f7atwy):
 return 1+0.03*y2f7atwy
def wg25cfzf(y2f7atwy):
 return 1+0.04*y2f7atwy
def s8438tgb(y2f7atwy):
 return max(0.7,1-0.03*y2f7atwy)
def fdxj37c9(y2f7atwy):
 return y2f7atwy*2
def w8y72ivg(y2f7atwy):
 return y2f7atwy*0.5
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
m53a5qbs=[int(100*1.3**(y2f7atwy-1))for y2f7atwy in range(1,61)]
