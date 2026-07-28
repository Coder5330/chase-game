import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def gp84dyt9(g1g1r1dw):
 return os.path.join(dnq4fmyz,g1g1r1dw)
(rrcbpljd,rla5ju9b)=(800,600)
(ygspk9p3,v4u89yjb)=(2000,2000)
pi3qk2ia=60
y38daly8=40
rv86wzs3=4
qqu7eeqt=30
zxa3kx7e=30
r4874frh=4
ue0ifd0t=140
d60fkhmy=0.01
isj6bw3b=0.045
s8qjnv8z=1.4
cawudtse=40
b8cgvyie=300
b18hafey=6
cq0b8ic8=4
iq5c34dx={'dzjssz':(255,0,0),'w2zeeq':(255,102,102),'dg4fbl':(139,0,0),'hb1ajo':(0,255,0),'uq0e27':(144,238,144),'uet25l':(0,100,0),'bk2wbx':(0,0,255),'i563bt':(0,255,255),'pta5iv':(0,0,128),'wkgeq2':(135,206,235),'yl4zjd':(255,255,0),'fnn16u':(255,255,224),'iwu3bf':(128,128,0),'umfbuv':(255,165,0),'wtolaq':(255,200,124),'u77lu8':(255,140,0),'m314cq':(128,0,128),'rthy25':(238,130,238),'xutxzb':(75,0,130),'xu7dkn':(255,192,203),'w65dlx':(255,182,193),'m1v3zo':(255,105,180),'wdl5tg':(139,69,19),'gkok3q':(181,101,29),'q8wwii':(92,46,13),'wxgnrf':(128,128,128),'nk7y6q':(211,211,211),'eplvqe':(64,64,64),'ew6tm2':(0,128,128),'ldz09w':(102,178,178),'n8k03w':(0,77,77),'v5ff1b':(255,0,255),'k7bpgy':(218,112,214),'w66p61':(139,0,139),'amyrsv':(255,215,0),'pswrgv':(192,192,192),'jl1qwe':(128,0,0),'n7csuy':(64,224,208),'xy79kv':(250,128,114),'uk99jc':(255,127,80),'rsjr0f':(245,245,220),'dq3b9s':(255,255,240),'m9bn18':(240,230,140),'wyn6sj':(0,0,0),'lcf4mn':(255,255,255)}
n2vlpys2=(90,90,100)
cq5uznof=(50,50,58)
z0xkxwd8=(120,120,132)
hyihair4=(70,70,80)
gyljexq7=['hb1ajo','i563bt','bk2wbx','m314cq','v5ff1b','umfbuv','dzjssz','dg4fbl','wxgnrf','amyrsv']
def nd96qe3r(bokzixza):
 return{'kk2y77':100*1.3**(bokzixza-1),'pgsb98':min(rv86wzs3*0.75,1.3*1.13**(bokzixza-1)),'hn3ksg':10*1.25**(bokzixza-1),'kqbrmq':5*1.2**(bokzixza-1),'l226pa':max(10,60*0.9**(bokzixza-1)),'igc9ho':26*1.27**(bokzixza-1)}
s0clbr7t={'xyhhg8':{'g8wze4':1,'tudttj':'hb1ajo','buzery':(1.0,1.0,1.0,1.0,1.0,1.0)},'r3hxyj':{'g8wze4':2,'tudttj':'i563bt','buzery':(0.6,1.8,0.7,0.8,0.8,1.0),'wzwl3z':True,'w1q8f6':150,'i6ozx2':2.5,'c37qqy':20,'v3c71u':90},'k7rrbe':{'g8wze4':3,'tudttj':'wxgnrf','buzery':(2.6,0.45,0.6,1.6,1.3,1.3),'og8cd3':True,'y3lxch':60,'eqkwqh':1,'e56waf':30},'zpfb3h':{'g8wze4':4,'tudttj':'m314cq','buzery':(0.7,0.7,1.3,0.7,1.4,1.2),'kp82kb':True,'ktaq6u':260,'vcw2lb':7},'q8uzb7':{'g8wze4':5,'tudttj':'umfbuv','buzery':(1.6,0.85,1.6,1.1,1.1,1.4),'kj2jvq':True,'w9laac':40,'v00vhm':2.0},'dkql0h':{'g8wze4':6,'tudttj':'v5ff1b','buzery':(0.55,2.1,1.5,0.6,0.7,1.3),'bx1ego':True,'onlt8d':10,'jr87iy':120,'mrf5a7':150,'t00ucr':25},'acxx6m':{'g8wze4':7,'tudttj':'dzjssz','buzery':(0.8,1.1,1.0,0.8,1.0,1.3),'cm3v2p':True,'zmygy0':70},'kjuw7w':{'g8wze4':8,'tudttj':'dg4fbl','buzery':(1.8,0.75,0.9,2.4,1.2,1.5),'v9hbn5':True,'p6fmr5':120,'j1f537':0.5},'kou83g':{'g8wze4':9,'tudttj':'amyrsv','buzery':(0.35,1.5,0.5,0.5,0.6,0.8),'ijj0v6':3},'xj2dg1':{'g8wze4':10,'tudttj':'w66p61','buzery':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={jr5rdnpx:{'kk2y77':int(nd96qe3r(tacj4t0s['g8wze4'])['kk2y77']*tacj4t0s['buzery'][0]),'pgsb98':round(nd96qe3r(tacj4t0s['g8wze4'])['pgsb98']*tacj4t0s['buzery'][1],2),'hn3ksg':int(nd96qe3r(tacj4t0s['g8wze4'])['hn3ksg']*tacj4t0s['buzery'][2]),'kqbrmq':int(nd96qe3r(tacj4t0s['g8wze4'])['kqbrmq']*tacj4t0s['buzery'][3]),'l226pa':max(10,int(nd96qe3r(tacj4t0s['g8wze4'])['l226pa']*tacj4t0s['buzery'][4])),'igc9ho':int(nd96qe3r(tacj4t0s['g8wze4'])['igc9ho']*tacj4t0s['buzery'][5]),'tudttj':iq5c34dx[tacj4t0s['tudttj']],'g8wze4':tacj4t0s['g8wze4'],'kp82kb':tacj4t0s.get('kp82kb',False),'ktaq6u':tacj4t0s.get('ktaq6u'),'vcw2lb':tacj4t0s.get('vcw2lb'),'cm3v2p':tacj4t0s.get('cm3v2p',False),'zmygy0':tacj4t0s.get('zmygy0'),'ijj0v6':tacj4t0s.get('ijj0v6'),'wzwl3z':tacj4t0s.get('wzwl3z',False),'w1q8f6':tacj4t0s.get('w1q8f6'),'i6ozx2':tacj4t0s.get('i6ozx2'),'c37qqy':tacj4t0s.get('c37qqy'),'v3c71u':tacj4t0s.get('v3c71u'),'og8cd3':tacj4t0s.get('og8cd3',False),'y3lxch':tacj4t0s.get('y3lxch'),'eqkwqh':tacj4t0s.get('eqkwqh'),'e56waf':tacj4t0s.get('e56waf'),'bx1ego':tacj4t0s.get('bx1ego',False),'onlt8d':tacj4t0s.get('onlt8d'),'jr87iy':tacj4t0s.get('jr87iy'),'mrf5a7':tacj4t0s.get('mrf5a7'),'t00ucr':tacj4t0s.get('t00ucr'),'kj2jvq':tacj4t0s.get('kj2jvq',False),'w9laac':tacj4t0s.get('w9laac'),'v00vhm':tacj4t0s.get('v00vhm'),'v9hbn5':tacj4t0s.get('v9hbn5',False),'p6fmr5':tacj4t0s.get('p6fmr5'),'j1f537':tacj4t0s.get('j1f537')}for(jr5rdnpx,tacj4t0s)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda jr5rdnpx:k1wj0tpa[jr5rdnpx]['g8wze4'])
uqjiujv6={'pqpva5':{'pgsb98':10,'bdoz6w':10,'pcs4ke':6,'edxoq2':60,'qc6dr0':0,'xfq3jz':None,'tudttj':iq5c34dx['lcf4mn'],'hpvwzo':gp84dyt9('assets/normal.png'),'i1yy1j':20,'w9mda9':15},'da5xin':{'pgsb98':5,'bdoz6w':8,'pcs4ke':8,'edxoq2':90,'qc6dr0':999,'xfq3jz':'flyback','wurvqt':250,'tudttj':iq5c34dx['umfbuv'],'hpvwzo':gp84dyt9('assets/boomerang.png'),'i1yy1j':20,'w9mda9':27},'o5rlqi':{'pgsb98':6,'bdoz6w':6,'pcs4ke':5,'edxoq2':100,'qc6dr0':0,'xfq3jz':'homing','nddqhk':0.08,'tudttj':iq5c34dx['v5ff1b'],'hpvwzo':gp84dyt9('assets/homing.png'),'i1yy1j':20,'w9mda9':20},'txzuu8':{'pgsb98':14,'bdoz6w':12,'pcs4ke':4,'edxoq2':50,'qc6dr0':3,'xfq3jz':'qc6dr0','tudttj':iq5c34dx['i563bt'],'hpvwzo':gp84dyt9('assets/pierce.png'),'i1yy1j':20,'w9mda9':7},'twvwvi':{'pgsb98':7,'bdoz6w':15,'pcs4ke':10,'edxoq2':70,'qc6dr0':0,'xfq3jz':'explode','zmygy0':60,'tudttj':iq5c34dx['dzjssz'],'hpvwzo':gp84dyt9('assets/explosive.png'),'i1yy1j':20,'w9mda9':20},'clslay':{'pgsb98':9,'bdoz6w':7,'pcs4ke':5,'edxoq2':60,'qc6dr0':0,'xfq3jz':'split','t7fr91':3,'tudttj':iq5c34dx['amyrsv'],'hpvwzo':gp84dyt9('assets/split.png'),'i1yy1j':20,'w9mda9':9},'t753ay':{'pgsb98':7,'bdoz6w':12,'pcs4ke':6,'edxoq2':90,'qc6dr0':0,'xfq3jz':None,'tudttj':iq5c34dx['m314cq']}}
uyhl1c32={'pqpva5':'Normal Shot','da5xin':'Boomerang','o5rlqi':'Homing Shot','txzuu8':'Piercing Shot','twvwvi':'Explosive Shot','clslay':'Split Shot'}
mjh75lxo={'pqpva5':15,'da5xin':25,'o5rlqi':20,'txzuu8':18,'twvwvi':35,'clslay':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
x37pqkoj=5
def mabkae6a(bokzixza):
 return 1+(bokzixza-1)*0.12
def huh17j8q(bokzixza):
 return max(0.65,1-(bokzixza-1)*0.07)
rqf5q14j={'e8a1ar':{'ntxrgn':'Vitality','fkmuso':'+20% Max Health','t7wqp3':8},'x429om':{'ntxrgn':'Swift Boots','fkmuso':'+8% Move Speed','t7wqp3':5},'tcu9td':{'ntxrgn':'Regeneration','fkmuso':'+1 HP/sec','t7wqp3':6},'iimoe0':{'ntxrgn':'Power','fkmuso':'+6% Weapon Damage','t7wqp3':8},'jmofmm':{'ntxrgn':'Haste','fkmuso':'-5% Attack Cooldown','t7wqp3':6},'lf0d0i':{'ntxrgn':'Armor','fkmuso':'+5 Defense','t7wqp3':6},'r4uov5':{'ntxrgn':'Wisdom','fkmuso':'+15% XP Gain','t7wqp3':5}}
ibps3y70={'START_HEALTH':{'o6d10a':'en1x2g','ntxrgn':'Heart Crystal','fkmuso':'+8% Starting Max Health','t7wqp3':10,'da7yvd':15,'rpeqyd':1.35},'START_REGEN':{'o6d10a':'en1x2g','ntxrgn':'Regen Charm','fkmuso':'+0.5 Starting HP/sec','t7wqp3':6,'da7yvd':25,'rpeqyd':1.4},'START_DAMAGE':{'o6d10a':'w2ugl6','ntxrgn':'Sharp Edge','fkmuso':'+4% Starting Damage','t7wqp3':10,'da7yvd':20,'rpeqyd':1.35},'START_COOLDOWN':{'o6d10a':'w2ugl6','ntxrgn':'Quick Hands','fkmuso':'-3% Starting Cooldown','t7wqp3':8,'da7yvd':25,'rpeqyd':1.4},'START_SPEED':{'o6d10a':'hzj7ub','ntxrgn':'Wind Charm','fkmuso':'+3% Starting Speed','t7wqp3':8,'da7yvd':18,'rpeqyd':1.35},'START_ARMOR':{'o6d10a':'hzj7ub','ntxrgn':'Iron Skin','fkmuso':'+2 Starting Armor','t7wqp3':10,'da7yvd':15,'rpeqyd':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(tacj4t0s['hpvwzo']),(tacj4t0s['i1yy1j'],tacj4t0s['w9mda9']))for(key,tacj4t0s)in uqjiujv6.items()if'hpvwzo'in tacj4t0s}
def qo6q0usw(bokzixza):
 return 1+0.08*bokzixza
def gqq4d3kz(bokzixza):
 return 1+0.03*bokzixza
def a8ax40dt(bokzixza):
 return 1+0.04*bokzixza
def xwqvr1h6(bokzixza):
 return max(0.7,1-0.03*bokzixza)
def nii6l3ue(bokzixza):
 return bokzixza*2
def mcup8ijl(bokzixza):
 return bokzixza*0.5
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
cqoldfor=[int(100*1.3**(bokzixza-1))for bokzixza in range(1,61)]
