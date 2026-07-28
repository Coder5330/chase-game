import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def ykipu1wy(h4l1vznq):
 return os.path.join(dnq4fmyz,h4l1vznq)
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
iq5c34dx={'kk2y77':(255,0,0),'c37qqy':(255,102,102),'lcf4mn':(139,0,0),'j1f537':(0,255,0),'bdoz6w':(144,238,144),'ew6tm2':(0,100,0),'dzjssz':(0,0,255),'r3hxyj':(0,255,255),'mviifr':(0,0,128),'ntxrgn':(135,206,235),'ktaq6u':(255,255,0),'i6ozx2':(255,255,224),'zmygy0':(128,128,0),'wurvqt':(255,165,0),'wzwl3z':(255,200,124),'rthy25':(255,140,0),'eqkwqh':(128,0,128),'e0s41k':(238,130,238),'yl6lgj':(75,0,130),'e56waf':(255,192,203),'v3c71u':(255,182,193),'o6d10a':(255,105,180),'kjuw7w':(139,69,19),'w2ugl6':(181,101,29),'kou83g':(92,46,13),'p6fmr5':(128,128,128),'rpeqyd':(211,211,211),'k7rrbe':(64,64,64),'hzj7ub':(0,128,128),'w1q8f6':(102,178,178),'r4uov5':(0,77,77),'kqbrmq':(255,0,255),'og8cd3':(218,112,214),'n7csuy':(139,0,139),'l226pa':(255,215,0),'hpvwzo':(192,192,192),'fkmuso':(128,0,0),'buzery':(64,224,208),'m44c68':(250,128,114),'x429om':(255,127,80),'o0mb1l':(245,245,220),'k1yjfe':(255,255,240),'tudttj':(240,230,140),'m314cq':(0,0,0),'qc6dr0':(255,255,255)}
hyihair4=(90,90,100)
qqu7eeqt=(50,50,58)
cq5uznof=(120,120,132)
wa11dpg8=(70,70,80)
gyljexq7=['j1f537','r3hxyj','dzjssz','eqkwqh','kqbrmq','wurvqt','kk2y77','lcf4mn','p6fmr5','l226pa']
def sld4d6af(y2f7atwy):
 return{'r7myow':100*1.3**(y2f7atwy-1),'prf7bn':min(yswjckjl*0.75,1.3*1.13**(y2f7atwy-1)),'kp82kb':10*1.25**(y2f7atwy-1),'g8wze4':5*1.2**(y2f7atwy-1),'t00ucr':max(10,60*0.9**(y2f7atwy-1)),'o15o2n':26*1.27**(y2f7atwy-1)}
s0clbr7t={'v9hbn5':{'s6pb90':1,'bx1ego':'j1f537','th2p39':(1.0,1.0,1.0,1.0,1.0,1.0)},'cxf5x9':{'s6pb90':2,'bx1ego':'r3hxyj','th2p39':(0.6,1.8,0.7,0.8,0.8,1.0),'rw8p74':True,'w9laac':150,'nddqhk':2.5,'v00vhm':20,'kj2jvq':90},'mmgvu4':{'s6pb90':3,'bx1ego':'p6fmr5','th2p39':(2.6,0.45,0.6,1.6,1.3,1.3),'oarxab':True,'mjz6us':60,'riny2e':1,'yrp422':30},'h5kw3h':{'s6pb90':4,'bx1ego':'eqkwqh','th2p39':(0.7,0.7,1.3,0.7,1.4,1.2),'pca7zv':True,'be2wnf':260,'yoztp7':7},'pswrgv':{'s6pb90':5,'bx1ego':'wurvqt','th2p39':(1.6,0.85,1.6,1.1,1.1,1.4),'sce4qg':True,'futios':40,'khkf28':2.0},'vkxzuu':{'s6pb90':6,'bx1ego':'kqbrmq','th2p39':(0.55,2.1,1.5,0.6,0.7,1.3),'c6zvlh':True,'nf7qne':10,'v6idii':120,'n5nhqr':150,'jo31yh':25},'tcu9td':{'s6pb90':7,'bx1ego':'kk2y77','th2p39':(0.8,1.1,1.0,0.8,1.0,1.3),'yc1nlc':True,'urf1hx':70},'az3m55':{'s6pb90':8,'bx1ego':'lcf4mn','th2p39':(1.8,0.75,0.9,2.4,1.2,1.5),'ijj0v6':True,'fuxk0a':120,'pcs4ke':0.5},'t7wqp3':{'s6pb90':9,'bx1ego':'l226pa','th2p39':(0.35,1.5,0.5,0.5,0.6,0.8),'tn1th1':3},'yl4zjd':{'s6pb90':10,'bx1ego':'n7csuy','th2p39':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={zorxdtg5:{'r7myow':int(sld4d6af(iie0rnuj['s6pb90'])['r7myow']*iie0rnuj['th2p39'][0]),'prf7bn':round(sld4d6af(iie0rnuj['s6pb90'])['prf7bn']*iie0rnuj['th2p39'][1],2),'kp82kb':int(sld4d6af(iie0rnuj['s6pb90'])['kp82kb']*iie0rnuj['th2p39'][2]),'g8wze4':int(sld4d6af(iie0rnuj['s6pb90'])['g8wze4']*iie0rnuj['th2p39'][3]),'t00ucr':max(10,int(sld4d6af(iie0rnuj['s6pb90'])['t00ucr']*iie0rnuj['th2p39'][4])),'o15o2n':int(sld4d6af(iie0rnuj['s6pb90'])['o15o2n']*iie0rnuj['th2p39'][5]),'bx1ego':iq5c34dx[iie0rnuj['bx1ego']],'s6pb90':iie0rnuj['s6pb90'],'pca7zv':iie0rnuj.get('pca7zv',False),'be2wnf':iie0rnuj.get('be2wnf'),'yoztp7':iie0rnuj.get('yoztp7'),'yc1nlc':iie0rnuj.get('yc1nlc',False),'urf1hx':iie0rnuj.get('urf1hx'),'tn1th1':iie0rnuj.get('tn1th1'),'rw8p74':iie0rnuj.get('rw8p74',False),'w9laac':iie0rnuj.get('w9laac'),'nddqhk':iie0rnuj.get('nddqhk'),'v00vhm':iie0rnuj.get('v00vhm'),'kj2jvq':iie0rnuj.get('kj2jvq'),'oarxab':iie0rnuj.get('oarxab',False),'mjz6us':iie0rnuj.get('mjz6us'),'riny2e':iie0rnuj.get('riny2e'),'yrp422':iie0rnuj.get('yrp422'),'c6zvlh':iie0rnuj.get('c6zvlh',False),'nf7qne':iie0rnuj.get('nf7qne'),'v6idii':iie0rnuj.get('v6idii'),'n5nhqr':iie0rnuj.get('n5nhqr'),'jo31yh':iie0rnuj.get('jo31yh'),'sce4qg':iie0rnuj.get('sce4qg',False),'futios':iie0rnuj.get('futios'),'khkf28':iie0rnuj.get('khkf28'),'ijj0v6':iie0rnuj.get('ijj0v6',False),'fuxk0a':iie0rnuj.get('fuxk0a'),'pcs4ke':iie0rnuj.get('pcs4ke')}for(zorxdtg5,iie0rnuj)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda zorxdtg5:k1wj0tpa[zorxdtg5]['s6pb90'])
uqjiujv6={'cm3v2p':{'prf7bn':10,'onlt8d':10,'lpug99':6,'rfu7bf':60,'zhbgcj':0,'vhbef4':None,'bx1ego':iq5c34dx['qc6dr0'],'upgba9':ykipu1wy('assets/normal.png'),'gekxdr':20,'udt8cq':15},'xy79kv':{'prf7bn':5,'onlt8d':8,'lpug99':8,'rfu7bf':90,'zhbgcj':999,'vhbef4':'flyback','ozdcuj':250,'bx1ego':iq5c34dx['wurvqt'],'upgba9':ykipu1wy('assets/boomerang.png'),'gekxdr':20,'udt8cq':27},'da7yvd':{'prf7bn':6,'onlt8d':6,'lpug99':5,'rfu7bf':100,'zhbgcj':0,'vhbef4':'homing','gv4k00':0.08,'bx1ego':iq5c34dx['kqbrmq'],'upgba9':ykipu1wy('assets/homing.png'),'gekxdr':20,'udt8cq':20},'y3lxch':{'prf7bn':14,'onlt8d':12,'lpug99':4,'rfu7bf':50,'zhbgcj':3,'vhbef4':'zhbgcj','bx1ego':iq5c34dx['r3hxyj'],'upgba9':ykipu1wy('assets/pierce.png'),'gekxdr':20,'udt8cq':7},'hn3ksg':{'prf7bn':7,'onlt8d':15,'lpug99':10,'rfu7bf':70,'zhbgcj':0,'vhbef4':'explode','urf1hx':60,'bx1ego':iq5c34dx['kk2y77'],'upgba9':ykipu1wy('assets/explosive.png'),'gekxdr':20,'udt8cq':20},'edxoq2':{'prf7bn':9,'onlt8d':7,'lpug99':5,'rfu7bf':60,'zhbgcj':0,'vhbef4':'split','gpm21b':3,'bx1ego':iq5c34dx['l226pa'],'upgba9':ykipu1wy('assets/split.png'),'gekxdr':20,'udt8cq':9},'tk7bpg':{'prf7bn':7,'onlt8d':12,'lpug99':6,'rfu7bf':90,'zhbgcj':0,'vhbef4':None,'bx1ego':iq5c34dx['eqkwqh']}}
uyhl1c32={'cm3v2p':'Normal Shot','xy79kv':'Boomerang','da7yvd':'Homing Shot','y3lxch':'Piercing Shot','hn3ksg':'Explosive Shot','edxoq2':'Split Shot'}
mjh75lxo={'cm3v2p':15,'xy79kv':25,'da7yvd':20,'y3lxch':18,'hn3ksg':35,'edxoq2':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
ygspk9p3=5
def o5rlqiob(y2f7atwy):
 return 1+(y2f7atwy-1)*0.12
def a78iyhhg(y2f7atwy):
 return max(0.65,1-(y2f7atwy-1)*0.07)
rcfnfhol={'w2lx2t':{'hrctlt':'Vitality','en1x2g':'+20% Max Health','ua6wix':8},'l4f9ye':{'hrctlt':'Swift Boots','en1x2g':'+8% Move Speed','ua6wix':5},'w9mda9':{'hrctlt':'Regeneration','en1x2g':'+1 HP/sec','ua6wix':6},'clslay':{'hrctlt':'Power','en1x2g':'+6% Weapon Damage','ua6wix':8},'wkgeq2':{'hrctlt':'Haste','en1x2g':'-5% Attack Cooldown','ua6wix':6},'ffxb4y':{'hrctlt':'Armor','en1x2g':'+5 Defense','ua6wix':6},'vcw2lb':{'hrctlt':'Wisdom','en1x2g':'+15% XP Gain','ua6wix':5}}
jsylztgx={'START_HEALTH':{'pgsb98':'qbtr23','hrctlt':'Heart Crystal','en1x2g':'+8% Starting Max Health','ua6wix':10,'xfq3jz':15,'mrf5a7':1.35},'START_REGEN':{'pgsb98':'qbtr23','hrctlt':'Regen Charm','en1x2g':'+0.5 Starting HP/sec','ua6wix':6,'xfq3jz':25,'mrf5a7':1.4},'START_DAMAGE':{'pgsb98':'jr87iy','hrctlt':'Sharp Edge','en1x2g':'+4% Starting Damage','ua6wix':10,'xfq3jz':20,'mrf5a7':1.35},'START_COOLDOWN':{'pgsb98':'jr87iy','hrctlt':'Quick Hands','en1x2g':'-3% Starting Cooldown','ua6wix':8,'xfq3jz':25,'mrf5a7':1.4},'START_SPEED':{'pgsb98':'f4c3ev','hrctlt':'Wind Charm','en1x2g':'+3% Starting Speed','ua6wix':8,'xfq3jz':18,'mrf5a7':1.35},'START_ARMOR':{'pgsb98':'f4c3ev','hrctlt':'Iron Skin','en1x2g':'+2 Starting Armor','ua6wix':10,'xfq3jz':15,'mrf5a7':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(iie0rnuj['upgba9']),(iie0rnuj['gekxdr'],iie0rnuj['udt8cq']))for(key,iie0rnuj)in uqjiujv6.items()if'upgba9'in iie0rnuj}
def j0kgazu4(y2f7atwy):
 return 1+0.08*y2f7atwy
def zdan085r(y2f7atwy):
 return 1+0.03*y2f7atwy
def jl90pxrl(y2f7atwy):
 return 1+0.04*y2f7atwy
def wg25cfzf(y2f7atwy):
 return max(0.7,1-0.03*y2f7atwy)
def k3z6bz8u(y2f7atwy):
 return y2f7atwy*2
def y8bv78hu(y2f7atwy):
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
t1w1ht7p=[int(100*1.3**(y2f7atwy-1))for y2f7atwy in range(1,61)]
