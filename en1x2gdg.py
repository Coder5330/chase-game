import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def yx4w6xlp(exvaj2k8):
 return os.path.join(dnq4fmyz,exvaj2k8)
(mqp49kwv,rla5ju9b)=(800,600)
(faqvkizz,xd1wjcit)=(2000,2000)
pi3qk2ia=60
ky20479t=40
hyihair4=4
z0xkxwd8=30
zxa3kx7e=30
r4874frh=4
ue0ifd0t=140
d60fkhmy=0.01
isj6bw3b=0.045
r0tvhhpb=1.4
cawudtse=40
b8cgvyie=300
yur7ko64=6
oohp6vz4=4
iq5c34dx={'xutxzb':(255,0,0),'eplvqe':(255,102,102),'sdypml':(139,0,0),'rsjr0f':(0,255,0),'i563bt':(144,238,144),'mjopz1':(0,100,0),'w37suu':(0,0,255),'awwbsl':(0,255,255),'xj2dg1':(0,0,128),'uq0e27':(135,206,235),'iwu3bf':(255,255,0),'w66p61':(255,255,224),'amyrsv':(128,128,0),'wxgnrf':(255,165,0),'iimoe0':(255,200,124),'xsijpy':(255,140,0),'m1v3zo':(128,0,128),'e8a1ar':(238,130,238),'da5xin':(75,0,130),'o5rlqi':(255,192,203),'q8wwii':(255,182,193),'acxx6m':(255,105,180),'c02g3y':(139,69,19),'jmofmm':(181,101,29),'m81udp':(92,46,13),'dkql0h':(128,128,128),'uk99jc':(211,211,211),'zoecub':(64,64,64),'v5ff1b':(0,128,128),'uet25l':(102,178,178),'tx1gm3':(0,77,77),'u77lu8':(255,0,255),'hb1ajo':(218,112,214),'purxhw':(139,0,139),'t753ay':(255,215,0),'nk7y6q':(192,192,192),'dg4fbl':(128,0,0),'jl1qwe':(64,224,208),'m9bn18':(250,128,114),'n7e104':(255,127,80),'mabkae':(245,245,220),'wdl5tg':(255,255,240),'q8uzb7':(240,230,140),'ja9hl1':(0,0,0),'pta5iv':(255,255,255)}
gyljexq7=['rsjr0f','awwbsl','w37suu','m1v3zo','u77lu8','wxgnrf','xutxzb','sdypml','dkql0h','t753ay']
def v4u89yjb(wvpw232u):
 return{'o6d10a':100*1.3**(wvpw232u-1),'wurvqt':min(hyihair4*0.75,1.3*1.13**(wvpw232u-1)),'umfbuv':10*1.25**(wvpw232u-1),'n7csuy':5*1.2**(wvpw232u-1),'k7bpgy':max(10,60*0.9**(wvpw232u-1)),'e0s41k':26*1.27**(wvpw232u-1)}
s0clbr7t={'wyn6sj':{'edxoq2':1,'kjuw7w':'rsjr0f','c37qqy':(1.0,1.0,1.0,1.0,1.0,1.0)},'w65dlx':{'edxoq2':2,'kjuw7w':'awwbsl','c37qqy':(0.6,1.8,0.7,0.8,0.8,1.0),'r3hxyj':True,'k7rrbe':150,'ew6tm2':2.5,'kou83g':20,'clslay':90},'fnn16u':{'edxoq2':3,'kjuw7w':'dkql0h','c37qqy':(2.6,0.45,0.6,1.6,1.3,1.3),'p6fmr5':True,'j1f537':60,'da7yvd':1,'v9hbn5':30},'zgomf9':{'edxoq2':4,'kjuw7w':'m1v3zo','c37qqy':(0.7,0.7,1.3,0.7,1.4,1.2),'fkmuso':True,'kqbrmq':260,'i6ozx2':7},'s3dxb3':{'edxoq2':5,'kjuw7w':'wxgnrf','c37qqy':(1.6,0.85,1.6,1.1,1.1,1.4),'az3m55':True,'ntxrgn':40,'hpvwzo':2.0},'gnt0mq':{'edxoq2':6,'kjuw7w':'u77lu8','c37qqy':(0.55,2.1,1.5,0.6,0.7,1.3),'e56waf':True,'w9mda9':10,'eqkwqh':120,'kk2y77':150,'w2lx2t':25},'dbmenu':{'edxoq2':7,'kjuw7w':'xutxzb','c37qqy':(0.8,1.1,1.0,0.8,1.0,1.3),'yl4zjd':True,'hn3ksg':70},'gkok3q':{'edxoq2':8,'kjuw7w':'sdypml','c37qqy':(1.8,0.75,0.9,2.4,1.2,1.5),'m314cq':True,'txzuu8':120,'xu7dkn':0.5},'ldz09w':{'edxoq2':9,'kjuw7w':'t753ay','c37qqy':(0.35,1.5,0.5,0.5,0.6,0.8),'cm3v2p':3},'zpfb3h':{'edxoq2':10,'kjuw7w':'purxhw','c37qqy':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={qo6q0usw:{'o6d10a':int(v4u89yjb(giec4d14['edxoq2'])['o6d10a']*giec4d14['c37qqy'][0]),'wurvqt':round(v4u89yjb(giec4d14['edxoq2'])['wurvqt']*giec4d14['c37qqy'][1],2),'umfbuv':int(v4u89yjb(giec4d14['edxoq2'])['umfbuv']*giec4d14['c37qqy'][2]),'n7csuy':int(v4u89yjb(giec4d14['edxoq2'])['n7csuy']*giec4d14['c37qqy'][3]),'k7bpgy':max(10,int(v4u89yjb(giec4d14['edxoq2'])['k7bpgy']*giec4d14['c37qqy'][4])),'e0s41k':int(v4u89yjb(giec4d14['edxoq2'])['e0s41k']*giec4d14['c37qqy'][5]),'kjuw7w':iq5c34dx[giec4d14['kjuw7w']],'edxoq2':giec4d14['edxoq2'],'fkmuso':giec4d14.get('fkmuso',False),'kqbrmq':giec4d14.get('kqbrmq'),'i6ozx2':giec4d14.get('i6ozx2'),'yl4zjd':giec4d14.get('yl4zjd',False),'hn3ksg':giec4d14.get('hn3ksg'),'cm3v2p':giec4d14.get('cm3v2p'),'r3hxyj':giec4d14.get('r3hxyj',False),'k7rrbe':giec4d14.get('k7rrbe'),'ew6tm2':giec4d14.get('ew6tm2'),'kou83g':giec4d14.get('kou83g'),'clslay':giec4d14.get('clslay'),'p6fmr5':giec4d14.get('p6fmr5',False),'j1f537':giec4d14.get('j1f537'),'da7yvd':giec4d14.get('da7yvd'),'v9hbn5':giec4d14.get('v9hbn5'),'e56waf':giec4d14.get('e56waf',False),'w9mda9':giec4d14.get('w9mda9'),'eqkwqh':giec4d14.get('eqkwqh'),'kk2y77':giec4d14.get('kk2y77'),'w2lx2t':giec4d14.get('w2lx2t'),'az3m55':giec4d14.get('az3m55',False),'ntxrgn':giec4d14.get('ntxrgn'),'hpvwzo':giec4d14.get('hpvwzo'),'m314cq':giec4d14.get('m314cq',False),'txzuu8':giec4d14.get('txzuu8'),'xu7dkn':giec4d14.get('xu7dkn')}for(qo6q0usw,giec4d14)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda qo6q0usw:k1wj0tpa[qo6q0usw]['edxoq2'])
uqjiujv6={'twvwvi':{'wurvqt':10,'x429om':10,'mviifr':6,'rpeqyd':60,'w1q8f6':0,'zmygy0':None,'kjuw7w':iq5c34dx['pta5iv'],'k1yjfe':yx4w6xlp('assets/normal.png'),'hzj7ub':20,'yl6lgj':15},'hjkuuh':{'wurvqt':5,'x429om':8,'mviifr':8,'rpeqyd':90,'w1q8f6':999,'zmygy0':'flyback','l226pa':250,'kjuw7w':iq5c34dx['wxgnrf'],'k1yjfe':yx4w6xlp('assets/boomerang.png'),'hzj7ub':20,'yl6lgj':27},'bk2wbx':{'wurvqt':6,'x429om':6,'mviifr':5,'rpeqyd':100,'w1q8f6':0,'zmygy0':'homing','l4f9ye':0.08,'kjuw7w':iq5c34dx['u77lu8'],'k1yjfe':yx4w6xlp('assets/homing.png'),'hzj7ub':20,'yl6lgj':20},'xyhhg8':{'wurvqt':14,'x429om':12,'mviifr':4,'rpeqyd':50,'w1q8f6':3,'zmygy0':'w1q8f6','kjuw7w':iq5c34dx['awwbsl'],'k1yjfe':yx4w6xlp('assets/pierce.png'),'hzj7ub':20,'yl6lgj':7},'lf0d0i':{'wurvqt':7,'x429om':15,'mviifr':10,'rpeqyd':70,'w1q8f6':0,'zmygy0':'explode','hn3ksg':60,'kjuw7w':iq5c34dx['xutxzb'],'k1yjfe':yx4w6xlp('assets/explosive.png'),'hzj7ub':20,'yl6lgj':20},'w2zeeq':{'wurvqt':9,'x429om':7,'mviifr':5,'rpeqyd':60,'w1q8f6':0,'zmygy0':'split','og8cd3':3,'kjuw7w':iq5c34dx['t753ay'],'k1yjfe':yx4w6xlp('assets/split.png'),'hzj7ub':20,'yl6lgj':9},'n1p0vu':{'wurvqt':7,'x429om':12,'mviifr':6,'rpeqyd':90,'w1q8f6':0,'zmygy0':None,'kjuw7w':iq5c34dx['m1v3zo']}}
uyhl1c32={'twvwvi':'Normal Shot','hjkuuh':'Boomerang','bk2wbx':'Homing Shot','xyhhg8':'Piercing Shot','lf0d0i':'Explosive Shot','w2zeeq':'Split Shot'}
mjh75lxo={'twvwvi':15,'hjkuuh':25,'bk2wbx':20,'xyhhg8':18,'lf0d0i':35,'w2zeeq':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
jdiuovw1=5
def r212pgym(wvpw232u):
 return 1+(wvpw232u-1)*0.12
def ywcxz2ei(wvpw232u):
 return max(0.65,1-(wvpw232u-1)*0.07)
cq5uznof={'n8k03w':{'tudttj':'Vitality','rthy25':'+20% Max Health','bdoz6w':8},'wtolaq':{'tudttj':'Swift Boots','rthy25':'+8% Move Speed','bdoz6w':5},'dq3b9s':{'tudttj':'Regeneration','rthy25':'+1 HP/sec','bdoz6w':6},'sfshb0':{'tudttj':'Power','rthy25':'+6% Weapon Damage','bdoz6w':8},'mcc1m3':{'tudttj':'Haste','rthy25':'-5% Attack Cooldown','bdoz6w':6},'o76t94':{'tudttj':'Armor','rthy25':'+5 Defense','bdoz6w':6},'pqpva5':{'tudttj':'Wisdom','rthy25':'+15% XP Gain','bdoz6w':5}}
ibps3y70={'START_HEALTH':{'tcu9td':'t7wqp3','tudttj':'Heart Crystal','rthy25':'+8% Starting Max Health','bdoz6w':10,'dzjssz':15,'wkgeq2':1.35},'START_REGEN':{'tcu9td':'t7wqp3','tudttj':'Regen Charm','rthy25':'+0.5 Starting HP/sec','bdoz6w':6,'dzjssz':25,'wkgeq2':1.4},'START_DAMAGE':{'tcu9td':'pswrgv','tudttj':'Sharp Edge','rthy25':'+4% Starting Damage','bdoz6w':10,'dzjssz':20,'wkgeq2':1.35},'START_COOLDOWN':{'tcu9td':'pswrgv','tudttj':'Quick Hands','rthy25':'-3% Starting Cooldown','bdoz6w':8,'dzjssz':25,'wkgeq2':1.4},'START_SPEED':{'tcu9td':'v3c71u','tudttj':'Wind Charm','rthy25':'+3% Starting Speed','bdoz6w':8,'dzjssz':18,'wkgeq2':1.35},'START_ARMOR':{'tcu9td':'v3c71u','tudttj':'Iron Skin','rthy25':'+2 Starting Armor','bdoz6w':10,'dzjssz':15,'wkgeq2':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(giec4d14['k1yjfe']),(giec4d14['hzj7ub'],giec4d14['yl6lgj']))for(key,giec4d14)in uqjiujv6.items()if'k1yjfe'in giec4d14}
def ls2zge2j(wvpw232u):
 return 1+0.08*wvpw232u
def lnf74t60(wvpw232u):
 return 1+0.03*wvpw232u
def n04cdpqv(wvpw232u):
 return 1+0.04*wvpw232u
def mctwjlsh(wvpw232u):
 return max(0.7,1-0.03*wvpw232u)
def q5amln4p(wvpw232u):
 return wvpw232u*2
def d1b3jczu(wvpw232u):
 return wvpw232u*0.5
dxmo5bxx=10
oeimvihc=45
bom5igqp=25
r1yzoyn6=2
re7ur23g=15
uccblskr=30
jsylztgx=3
my6wktak=(245,245,235)
mn9er14f=(70,130,180)
fq85jsg6=(40,80,120)
f2pcn9t8=(100,160,210)
aye511mk=(60,110,160)
ocij2v2h=[int(100*1.3**(wvpw232u-1))for wvpw232u in range(1,61)]
