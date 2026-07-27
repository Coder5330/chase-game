import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def v982n2at(z3olfark):
 return os.path.join(dnq4fmyz,z3olfark)
(dtx63cfl,rla5ju9b)=(800,600)
(rrcbpljd,x37pqkoj)=(2000,2000)
pi3qk2ia=60
b18hafey=40
rv86wzs3=4
qqu7eeqt=30
zxa3kx7e=30
r4874frh=4
ue0ifd0t=140
d60fkhmy=0.01
isj6bw3b=0.045
cq0b8ic8=1.4
cawudtse=40
b8cgvyie=300
khl1n13j=6
mvxdp5gj=4
iq5c34dx={'w65dlx':(255,0,0),'twvwvi':(255,102,102),'wyn6sj':(139,0,0),'jmofmm':(0,255,0),'dg4fbl':(144,238,144),'t753ay':(0,100,0),'t7wwbs':(0,0,255),'v7dypm':(0,255,255),'m1v3zo':(0,0,128),'jl1qwe':(135,206,235),'tcu9td':(255,255,0),'wxgnrf':(255,255,224),'dq3b9s':(128,128,0),'m9bn18':(255,165,0),'n8k03w':(255,200,124),'rsjr0f':(255,140,0),'wtolaq':(128,0,128),'xu7dkn':(238,130,238),'q8wwii':(75,0,130),'uq0e27':(255,192,203),'xj2dg1':(255,182,193),'iimoe0':(255,105,180),'nkoecu':(139,69,19),'w66p61':(181,101,29),'zpfb3h':(92,46,13),'q8uzb7':(128,128,128),'u77lu8':(211,211,211),'lf0d0i':(64,64,64),'k7bpgy':(0,128,128),'amyrsv':(102,178,178),'bk2wbx':(0,77,77),'hb1ajo':(255,0,255),'gkok3q':(218,112,214),'dkql0h':(139,0,139),'wdl5tg':(255,215,0),'v5ff1b':(192,192,192),'xyhhg8':(128,0,0),'txzuu8':(64,224,208),'ldz09w':(250,128,114),'t9sijp':(255,127,80),'zucc1m':(245,245,220),'eplvqe':(255,255,240),'uet25l':(240,230,140),'no55ix':(0,0,0),'m314cq':(255,255,255)}
n2vlpys2=(90,90,100)
cq5uznof=(50,50,58)
z0xkxwd8=(120,120,132)
hyihair4=(70,70,80)
gyljexq7=['jmofmm','v7dypm','t7wwbs','wtolaq','hb1ajo','m9bn18','w65dlx','wyn6sj','q8uzb7','wdl5tg']
def m53a5qbs(swwnc21o):
 return{'wzwl3z':100*1.3**(swwnc21o-1),'m44c68':min(rv86wzs3*0.75,1.3*1.13**(swwnc21o-1)),'xy79kv':10*1.25**(swwnc21o-1),'p6fmr5':5*1.2**(swwnc21o-1),'kjuw7w':max(10,60*0.9**(swwnc21o-1)),'pcs4ke':26*1.27**(swwnc21o-1)}
s0clbr7t={'uk99jc':{'vcw2lb':1,'k7rrbe':'jmofmm','cm3v2p':(1.0,1.0,1.0,1.0,1.0,1.0)},'pta5iv':{'vcw2lb':2,'k7rrbe':'v7dypm','cm3v2p':(0.6,1.8,0.7,0.8,0.8,1.0),'lcf4mn':True,'hn3ksg':150,'l226pa':2.5,'yl4zjd':20,'r4uov5':90},'umfbuv':{'vcw2lb':3,'k7rrbe':'q8uzb7','cm3v2p':(2.6,0.45,0.6,1.6,1.3,1.3),'tudttj':True,'w2ugl6':60,'bdoz6w':1,'rpeqyd':30},'s7fbme':{'vcw2lb':4,'k7rrbe':'wtolaq','cm3v2p':(0.7,0.7,1.3,0.7,1.4,1.2),'y3lxch':True,'og8cd3':260,'wurvqt':7},'btjopz':{'vcw2lb':5,'k7rrbe':'m9bn18','cm3v2p':(1.6,0.85,1.6,1.1,1.1,1.4),'mmgvu4':True,'buzery':40,'hzj7ub':2.0},'wz3dxb':{'vcw2lb':6,'k7rrbe':'hb1ajo','cm3v2p':(0.55,2.1,1.5,0.6,0.7,1.3),'ntxrgn':True,'edxoq2':10,'l4f9ye':120,'cxf5x9':150,'e56waf':25},'ktfshb':{'vcw2lb':7,'k7rrbe':'w65dlx','cm3v2p':(0.8,1.1,1.0,0.8,1.0,1.3),'o6d10a':True,'yl6lgj':70},'fnn16u':{'vcw2lb':8,'k7rrbe':'wyn6sj','cm3v2p':(1.8,0.75,0.9,2.4,1.2,1.5),'x429om':True,'pswrgv':120,'wkgeq2':0.5},'iwu3bf':{'vcw2lb':9,'k7rrbe':'wdl5tg','cm3v2p':(0.35,1.5,0.5,0.5,0.6,0.8),'kk2y77':3},'acxx6m':{'vcw2lb':10,'k7rrbe':'dkql0h','cm3v2p':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={gqq4d3kz:{'wzwl3z':int(m53a5qbs(gn89qkns['vcw2lb'])['wzwl3z']*gn89qkns['cm3v2p'][0]),'m44c68':round(m53a5qbs(gn89qkns['vcw2lb'])['m44c68']*gn89qkns['cm3v2p'][1],2),'xy79kv':int(m53a5qbs(gn89qkns['vcw2lb'])['xy79kv']*gn89qkns['cm3v2p'][2]),'p6fmr5':int(m53a5qbs(gn89qkns['vcw2lb'])['p6fmr5']*gn89qkns['cm3v2p'][3]),'kjuw7w':max(10,int(m53a5qbs(gn89qkns['vcw2lb'])['kjuw7w']*gn89qkns['cm3v2p'][4])),'pcs4ke':int(m53a5qbs(gn89qkns['vcw2lb'])['pcs4ke']*gn89qkns['cm3v2p'][5]),'k7rrbe':iq5c34dx[gn89qkns['k7rrbe']],'vcw2lb':gn89qkns['vcw2lb'],'y3lxch':gn89qkns.get('y3lxch',False),'og8cd3':gn89qkns.get('og8cd3'),'wurvqt':gn89qkns.get('wurvqt'),'o6d10a':gn89qkns.get('o6d10a',False),'yl6lgj':gn89qkns.get('yl6lgj'),'kk2y77':gn89qkns.get('kk2y77'),'lcf4mn':gn89qkns.get('lcf4mn',False),'hn3ksg':gn89qkns.get('hn3ksg'),'l226pa':gn89qkns.get('l226pa'),'yl4zjd':gn89qkns.get('yl4zjd'),'r4uov5':gn89qkns.get('r4uov5'),'tudttj':gn89qkns.get('tudttj',False),'w2ugl6':gn89qkns.get('w2ugl6'),'bdoz6w':gn89qkns.get('bdoz6w'),'rpeqyd':gn89qkns.get('rpeqyd'),'ntxrgn':gn89qkns.get('ntxrgn',False),'edxoq2':gn89qkns.get('edxoq2'),'l4f9ye':gn89qkns.get('l4f9ye'),'cxf5x9':gn89qkns.get('cxf5x9'),'e56waf':gn89qkns.get('e56waf'),'mmgvu4':gn89qkns.get('mmgvu4',False),'buzery':gn89qkns.get('buzery'),'hzj7ub':gn89qkns.get('hzj7ub'),'x429om':gn89qkns.get('x429om',False),'pswrgv':gn89qkns.get('pswrgv'),'wkgeq2':gn89qkns.get('wkgeq2')}for(gqq4d3kz,gn89qkns)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda gqq4d3kz:k1wj0tpa[gqq4d3kz]['vcw2lb'])
uqjiujv6={'xutxzb':{'m44c68':10,'rthy25':10,'eqkwqh':6,'kqbrmq':60,'zmygy0':0,'w9mda9':None,'k7rrbe':iq5c34dx['m314cq'],'c37qqy':v982n2at('assets/normal.png'),'t00ucr':20,'v3c71u':15},'x981ud':{'m44c68':5,'rthy25':8,'eqkwqh':8,'kqbrmq':90,'zmygy0':999,'w9mda9':'flyback','k1yjfe':250,'k7rrbe':iq5c34dx['m9bn18'],'c37qqy':v982n2at('assets/boomerang.png'),'t00ucr':20,'v3c71u':27},'i563bt':{'m44c68':6,'rthy25':6,'eqkwqh':5,'kqbrmq':100,'zmygy0':0,'w9mda9':'homing','e0s41k':0.08,'k7rrbe':iq5c34dx['hb1ajo'],'c37qqy':v982n2at('assets/homing.png'),'t00ucr':20,'v3c71u':20},'nk7y6q':{'m44c68':14,'rthy25':12,'eqkwqh':4,'kqbrmq':50,'zmygy0':3,'w9mda9':'zmygy0','k7rrbe':iq5c34dx['v7dypm'],'c37qqy':v982n2at('assets/pierce.png'),'t00ucr':20,'v3c71u':7},'da5xin':{'m44c68':7,'rthy25':15,'eqkwqh':10,'kqbrmq':70,'zmygy0':0,'w9mda9':'explode','yl6lgj':60,'k7rrbe':iq5c34dx['w65dlx'],'c37qqy':v982n2at('assets/explosive.png'),'t00ucr':20,'v3c71u':20},'pqpva5':{'m44c68':9,'rthy25':7,'eqkwqh':5,'kqbrmq':60,'zmygy0':0,'w9mda9':'split','az3m55':3,'k7rrbe':iq5c34dx['wdl5tg'],'c37qqy':v982n2at('assets/split.png'),'t00ucr':20,'v3c71u':9},'s7002g':{'m44c68':7,'rthy25':12,'eqkwqh':6,'kqbrmq':90,'zmygy0':0,'w9mda9':None,'k7rrbe':iq5c34dx['wtolaq']}}
uyhl1c32={'xutxzb':'Normal Shot','x981ud':'Boomerang','i563bt':'Homing Shot','nk7y6q':'Piercing Shot','da5xin':'Explosive Shot','pqpva5':'Split Shot'}
mjh75lxo={'xutxzb':15,'x981ud':25,'i563bt':20,'nk7y6q':18,'da5xin':35,'pqpva5':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
ocij2v2h=5
def gsrtwlxd(swwnc21o):
 return 1+(swwnc21o-1)*0.12
def awnwlc83(swwnc21o):
 return max(0.65,1-(swwnc21o-1)*0.07)
rqf5q14j={'o5rlqi':{'w1q8f6':'Vitality','j1f537':'+20% Max Health','fkmuso':8},'e8a1ar':{'w1q8f6':'Swift Boots','j1f537':'+8% Move Speed','fkmuso':5},'w2zeeq':{'w1q8f6':'Regeneration','j1f537':'+1 HP/sec','fkmuso':6},'kmx1gm':{'w1q8f6':'Power','j1f537':'+6% Weapon Damage','fkmuso':8},'yeurxh':{'w1q8f6':'Haste','j1f537':'-5% Attack Cooldown','fkmuso':6},'l6ijku':{'w1q8f6':'Armor','j1f537':'+5 Defense','fkmuso':6},'dzjssz':{'w1q8f6':'Wisdom','j1f537':'+15% XP Gain','fkmuso':5}}
ibps3y70={'START_HEALTH':{'clslay':'ktaq6u','w1q8f6':'Heart Crystal','j1f537':'+8% Starting Max Health','fkmuso':10,'r3hxyj':15,'n7csuy':1.35},'START_REGEN':{'clslay':'ktaq6u','w1q8f6':'Regen Charm','j1f537':'+0.5 Starting HP/sec','fkmuso':6,'r3hxyj':25,'n7csuy':1.4},'START_DAMAGE':{'clslay':'ew6tm2','w1q8f6':'Sharp Edge','j1f537':'+4% Starting Damage','fkmuso':10,'r3hxyj':20,'n7csuy':1.35},'START_COOLDOWN':{'clslay':'ew6tm2','w1q8f6':'Quick Hands','j1f537':'-3% Starting Cooldown','fkmuso':8,'r3hxyj':25,'n7csuy':1.4},'START_SPEED':{'clslay':'mviifr','w1q8f6':'Wind Charm','j1f537':'+3% Starting Speed','fkmuso':8,'r3hxyj':18,'n7csuy':1.35},'START_ARMOR':{'clslay':'mviifr','w1q8f6':'Iron Skin','j1f537':'+2 Starting Armor','fkmuso':10,'r3hxyj':15,'n7csuy':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(gn89qkns['c37qqy']),(gn89qkns['t00ucr'],gn89qkns['v3c71u']))for(key,gn89qkns)in uqjiujv6.items()if'c37qqy'in gn89qkns}
def lnf74t60(swwnc21o):
 return 1+0.08*swwnc21o
def xwqvr1h6(swwnc21o):
 return 1+0.03*swwnc21o
def crsb4gf1(swwnc21o):
 return 1+0.04*swwnc21o
def ls2zge2j(swwnc21o):
 return max(0.7,1-0.03*swwnc21o)
def zflv1xxl(swwnc21o):
 return swwnc21o*2
def nii6l3ue(swwnc21o):
 return swwnc21o*0.5
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
v4u89yjb=[int(100*1.3**(swwnc21o-1))for swwnc21o in range(1,61)]
