import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def duhxid4n(ukshy8nb):
 return os.path.join(dnq4fmyz,ukshy8nb)
(ygspk9p3,tp0lvsnu)=(800,600)
(v83tqll8,cqoldfor)=(2000,2000)
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
iq5c34dx={'y3lxch':(255,0,0),'bdoz6w':(255,102,102),'ew6tm2':(139,0,0),'hn3ksg':(0,255,0),'tudttj':(144,238,144),'clslay':(0,100,0),'txzuu8':(0,0,255),'pswrgv':(0,255,255),'kqbrmq':(0,0,128),'m44c68':(135,206,235),'e0s41k':(255,255,0),'v3c71u':(255,255,224),'w2lx2t':(128,128,0),'mviifr':(255,165,0),'w2ugl6':(255,200,124),'k7rrbe':(255,140,0),'og8cd3':(128,0,128),'mmgvu4':(238,130,238),'v9hbn5':(75,0,130),'wurvqt':(255,192,203),'rpeqyd':(255,182,193),'j1f537':(255,105,180),'dzjssz':(139,69,19),'yl6lgj':(181,101,29),'x429om':(92,46,13),'yl4zjd':(128,128,128),'k1yjfe':(211,211,211),'r3hxyj':(64,64,64),'edxoq2':(0,128,128),'wzwl3z':(102,178,178),'n7csuy':(0,77,77),'c37qqy':(255,0,255),'cm3v2p':(218,112,214),'kou83g':(139,0,139),'r4uov5':(255,215,0),'w9mda9':(192,192,192),'w1q8f6':(128,0,0),'t7wqp3':(64,224,208),'eqkwqh':(250,128,114),'kjuw7w':(255,127,80),'umfbuv':(245,245,220),'da7yvd':(255,255,240),'o6d10a':(240,230,140),'k7bpgy':(0,0,0),'hzj7ub':(255,255,255)}
hyihair4=(90,90,100)
qqu7eeqt=(50,50,58)
cq5uznof=(120,120,132)
wa11dpg8=(70,70,80)
gyljexq7=['hn3ksg','pswrgv','txzuu8','og8cd3','c37qqy','mviifr','y3lxch','ew6tm2','yl4zjd','r4uov5']
def mnx39rbs(xwqvr1h6):
 return{'mjz6us':100*1.3**(xwqvr1h6-1),'lpug99':min(yswjckjl*0.75,1.3*1.13**(xwqvr1h6-1)),'qc6dr0':10*1.25**(xwqvr1h6-1),'w9laac':5*1.2**(xwqvr1h6-1),'vcw2lb':max(10,60*0.9**(xwqvr1h6-1)),'orc1yo':26*1.27**(xwqvr1h6-1)}
s0clbr7t={'l226pa':{'futios':1,'pgsb98':'hn3ksg','ua6wix':(1.0,1.0,1.0,1.0,1.0,1.0)},'hpvwzo':{'futios':2,'pgsb98':'pswrgv','ua6wix':(0.6,1.8,0.7,0.8,0.8,1.0),'jr87iy':True,'rw8p74':150,'kj2jvq':2.5,'onlt8d':20,'mrf5a7':90},'cxf5x9':{'futios':3,'pgsb98':'yl4zjd','ua6wix':(2.6,0.45,0.6,1.6,1.3,1.3),'igc9ho':True,'urf1hx':60,'oarxab':1,'ozdcuj':30},'e8a1ar':{'futios':4,'pgsb98':'og8cd3','ua6wix':(0.7,0.7,1.3,0.7,1.4,1.2),'zhbgcj':True,'voeytl':260,'th2p39':7},'tcu9td':{'futios':5,'pgsb98':'mviifr','ua6wix':(1.6,0.85,1.6,1.1,1.1,1.4),'n5nhqr':True,'xgmjmb':40,'nf7qne':2.0},'iwu3bf':{'futios':6,'pgsb98':'c37qqy','ua6wix':(0.55,2.1,1.5,0.6,0.7,1.3),'prf7bn':True,'c6zvlh':10,'gpm21b':120,'xbtfbs':150,'yoztp7':25},'xu7dkn':{'futios':7,'pgsb98':'y3lxch','ua6wix':(0.8,1.1,1.0,0.8,1.0,1.3),'en1x2g':True,'i1yy1j':70},'kk2y77':{'futios':8,'pgsb98':'ew6tm2','ua6wix':(1.8,0.75,0.9,2.4,1.2,1.5),'t00ucr':True,'ktaq6u':120,'kp82kb':0.5},'l4f9ye':{'futios':9,'pgsb98':'r4uov5','ua6wix':(0.35,1.5,0.5,0.5,0.6,0.8),'ujqigy':3},'rthy25':{'futios':10,'pgsb98':'kou83g','ua6wix':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={trdhw9re:{'mjz6us':int(mnx39rbs(vqnpcenl['futios'])['mjz6us']*vqnpcenl['ua6wix'][0]),'lpug99':round(mnx39rbs(vqnpcenl['futios'])['lpug99']*vqnpcenl['ua6wix'][1],2),'qc6dr0':int(mnx39rbs(vqnpcenl['futios'])['qc6dr0']*vqnpcenl['ua6wix'][2]),'w9laac':int(mnx39rbs(vqnpcenl['futios'])['w9laac']*vqnpcenl['ua6wix'][3]),'vcw2lb':max(10,int(mnx39rbs(vqnpcenl['futios'])['vcw2lb']*vqnpcenl['ua6wix'][4])),'orc1yo':int(mnx39rbs(vqnpcenl['futios'])['orc1yo']*vqnpcenl['ua6wix'][5]),'pgsb98':iq5c34dx[vqnpcenl['pgsb98']],'futios':vqnpcenl['futios'],'zhbgcj':vqnpcenl.get('zhbgcj',False),'voeytl':vqnpcenl.get('voeytl'),'th2p39':vqnpcenl.get('th2p39'),'en1x2g':vqnpcenl.get('en1x2g',False),'i1yy1j':vqnpcenl.get('i1yy1j'),'ujqigy':vqnpcenl.get('ujqigy'),'jr87iy':vqnpcenl.get('jr87iy',False),'rw8p74':vqnpcenl.get('rw8p74'),'kj2jvq':vqnpcenl.get('kj2jvq'),'onlt8d':vqnpcenl.get('onlt8d'),'mrf5a7':vqnpcenl.get('mrf5a7'),'igc9ho':vqnpcenl.get('igc9ho',False),'urf1hx':vqnpcenl.get('urf1hx'),'oarxab':vqnpcenl.get('oarxab'),'ozdcuj':vqnpcenl.get('ozdcuj'),'prf7bn':vqnpcenl.get('prf7bn',False),'c6zvlh':vqnpcenl.get('c6zvlh'),'gpm21b':vqnpcenl.get('gpm21b'),'xbtfbs':vqnpcenl.get('xbtfbs'),'yoztp7':vqnpcenl.get('yoztp7'),'n5nhqr':vqnpcenl.get('n5nhqr',False),'xgmjmb':vqnpcenl.get('xgmjmb'),'nf7qne':vqnpcenl.get('nf7qne'),'t00ucr':vqnpcenl.get('t00ucr',False),'ktaq6u':vqnpcenl.get('ktaq6u'),'kp82kb':vqnpcenl.get('kp82kb')}for(trdhw9re,vqnpcenl)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda trdhw9re:k1wj0tpa[trdhw9re]['futios'])
uqjiujv6={'fkmuso':{'lpug99':10,'bx1ego':10,'jo31yh':6,'hrctlt':60,'f4c3ev':0,'tgr8w2':None,'pgsb98':iq5c34dx['hzj7ub'],'udt8cq':duhxid4n('assets/normal.png'),'s6pb90':20,'yrp422':15},'m314cq':{'lpug99':5,'bx1ego':8,'jo31yh':8,'hrctlt':90,'f4c3ev':999,'tgr8w2':'flyback','yc1nlc':250,'pgsb98':iq5c34dx['mviifr'],'udt8cq':duhxid4n('assets/boomerang.png'),'s6pb90':20,'yrp422':27},'p6fmr5':{'lpug99':6,'bx1ego':6,'jo31yh':5,'hrctlt':100,'f4c3ev':0,'tgr8w2':'homing','sce4qg':0.08,'pgsb98':iq5c34dx['c37qqy'],'udt8cq':duhxid4n('assets/homing.png'),'s6pb90':20,'yrp422':20},'zmygy0':{'lpug99':14,'bx1ego':12,'jo31yh':4,'hrctlt':50,'f4c3ev':3,'tgr8w2':'f4c3ev','pgsb98':iq5c34dx['pswrgv'],'udt8cq':duhxid4n('assets/pierce.png'),'s6pb90':20,'yrp422':7},'lcf4mn':{'lpug99':7,'bx1ego':15,'jo31yh':10,'hrctlt':70,'f4c3ev':0,'tgr8w2':'explode','i1yy1j':60,'pgsb98':iq5c34dx['y3lxch'],'udt8cq':duhxid4n('assets/explosive.png'),'s6pb90':20,'yrp422':20},'ntxrgn':{'lpug99':9,'bx1ego':7,'jo31yh':5,'hrctlt':60,'f4c3ev':0,'tgr8w2':'split','tn1th1':3,'pgsb98':iq5c34dx['r4uov5'],'udt8cq':duhxid4n('assets/split.png'),'s6pb90':20,'yrp422':9},'pqpva5':{'lpug99':7,'bx1ego':12,'jo31yh':6,'hrctlt':90,'f4c3ev':0,'tgr8w2':None,'pgsb98':iq5c34dx['og8cd3']}}
uyhl1c32={'fkmuso':'Normal Shot','m314cq':'Boomerang','p6fmr5':'Homing Shot','zmygy0':'Piercing Shot','lcf4mn':'Explosive Shot','ntxrgn':'Split Shot'}
mjh75lxo={'fkmuso':15,'m314cq':25,'p6fmr5':20,'zmygy0':18,'lcf4mn':35,'ntxrgn':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
v4u89yjb=5
def un4regb1(xwqvr1h6):
 return 1+(xwqvr1h6-1)*0.12
def hiac2e4q(xwqvr1h6):
 return max(0.65,1-(xwqvr1h6-1)*0.07)
rcfnfhol={'i6ozx2':{'ykht8x':'Vitality','nddqhk':'+20% Max Health','zq9bc2':8},'az3m55':{'ykht8x':'Swift Boots','nddqhk':'+8% Move Speed','zq9bc2':5},'e56waf':{'ykht8x':'Regeneration','nddqhk':'+1 HP/sec','zq9bc2':6},'wkgeq2':{'ykht8x':'Power','nddqhk':'+6% Weapon Damage','zq9bc2':8},'xy79kv':{'ykht8x':'Haste','nddqhk':'-5% Attack Cooldown','zq9bc2':6},'pta5iv':{'ykht8x':'Armor','nddqhk':'+5 Defense','zq9bc2':6},'buzery':{'ykht8x':'Wisdom','nddqhk':'+15% XP Gain','zq9bc2':5}}
jsylztgx={'START_HEALTH':{'pcs4ke':'gv4k00','ykht8x':'Heart Crystal','nddqhk':'+8% Starting Max Health','zq9bc2':10,'fuxk0a':15,'hx0gu4':1.35},'START_REGEN':{'pcs4ke':'gv4k00','ykht8x':'Regen Charm','nddqhk':'+0.5 Starting HP/sec','zq9bc2':6,'fuxk0a':25,'hx0gu4':1.4},'START_DAMAGE':{'pcs4ke':'t7fr91','ykht8x':'Sharp Edge','nddqhk':'+4% Starting Damage','zq9bc2':10,'fuxk0a':20,'hx0gu4':1.35},'START_COOLDOWN':{'pcs4ke':'t7fr91','ykht8x':'Quick Hands','nddqhk':'-3% Starting Cooldown','zq9bc2':8,'fuxk0a':25,'hx0gu4':1.4},'START_SPEED':{'pcs4ke':'rfu7bf','ykht8x':'Wind Charm','nddqhk':'+3% Starting Speed','zq9bc2':8,'fuxk0a':18,'hx0gu4':1.35},'START_ARMOR':{'pcs4ke':'rfu7bf','ykht8x':'Iron Skin','nddqhk':'+2 Starting Armor','zq9bc2':10,'fuxk0a':15,'hx0gu4':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(vqnpcenl['udt8cq']),(vqnpcenl['s6pb90'],vqnpcenl['yrp422']))for(key,vqnpcenl)in uqjiujv6.items()if'udt8cq'in vqnpcenl}
def w8y72ivg(xwqvr1h6):
 return 1+0.08*xwqvr1h6
def wy0mahym(xwqvr1h6):
 return 1+0.03*xwqvr1h6
def d448n7od(xwqvr1h6):
 return 1+0.04*xwqvr1h6
def bihsa7he(xwqvr1h6):
 return max(0.7,1-0.03*xwqvr1h6)
def hu9n79gi(xwqvr1h6):
 return xwqvr1h6*2
def j0kgazu4(xwqvr1h6):
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
