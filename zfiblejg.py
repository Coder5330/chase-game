import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def c0hpmnz1(v0rxxf36):
 return os.path.join(dnq4fmyz,v0rxxf36)
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
iq5c34dx={'zmygy0':(255,0,0),'k1yjfe':(255,102,102),'r3hxyj':(139,0,0),'rthy25':(0,255,0),'da7yvd':(144,238,144),'pswrgv':(0,100,0),'sxqpva':(0,0,255),'dzjssz':(0,255,255),'c37qqy':(0,0,128),'eqkwqh':(135,206,235),'mmgvu4':(255,255,0),'w2ugl6':(255,255,224),'i6ozx2':(128,128,0),'kqbrmq':(255,165,0),'o6d10a':(255,200,124),'x429om':(255,140,0),'cm3v2p':(128,0,128),'cxf5x9':(238,130,238),'hn3ksg':(75,0,130),'mviifr':(255,192,203),'yl6lgj':(255,182,193),'yl4zjd':(255,105,180),'jldd9f':(139,69,19),'j1f537':(181,101,29),'xy79kv':(92,46,13),'n7csuy':(128,128,128),'v9hbn5':(211,211,211),'kjuw7w':(64,64,64),'ntxrgn':(0,128,128),'tudttj':(102,178,178),'clslay':(0,77,77),'bdoz6w':(255,0,255),'fkmuso':(218,112,214),'wkgeq2':(139,0,139),'ew6tm2':(255,215,0),'e56waf':(192,192,192),'wzwl3z':(128,0,0),'l4f9ye':(64,224,208),'og8cd3':(250,128,114),'m314cq':(255,127,80),'d68a1a':(245,245,220),'l226pa':(255,255,240),'p6fmr5':(240,230,140),'p4ta5i':(0,0,0),'edxoq2':(255,255,255)}
hyihair4=(90,90,100)
qqu7eeqt=(50,50,58)
cq5uznof=(120,120,132)
wa11dpg8=(70,70,80)
gyljexq7=['rthy25','dzjssz','sxqpva','cm3v2p','bdoz6w','kqbrmq','zmygy0','r3hxyj','n7csuy','ew6tm2']
def k44nlz15(j1ldqnk2):
 return{'urf1hx':100*1.3**(j1ldqnk2-1),'jo31yh':min(yswjckjl*0.75,1.3*1.13**(j1ldqnk2-1)),'hzj7ub':10*1.25**(j1ldqnk2-1),'rw8p74':5*1.2**(j1ldqnk2-1),'buzery':max(10,60*0.9**(j1ldqnk2-1)),'hipi78':26*1.27**(j1ldqnk2-1)}
s0clbr7t={'lcf4mn':{'xgmjmb':1,'pcs4ke':'rthy25','zq9bc2':(1.0,1.0,1.0,1.0,1.0,1.0)},'w9mda9':{'xgmjmb':2,'pcs4ke':'dzjssz','zq9bc2':(0.6,1.8,0.7,0.8,0.8,1.0),'t7fr91':True,'jr87iy':150,'mrf5a7':2.5,'bx1ego':20,'hx0gu4':90},'hpvwzo':{'xgmjmb':3,'pcs4ke':'n7csuy','zq9bc2':(2.6,0.45,0.6,1.6,1.3,1.3),'dzjq7w':True,'i1yy1j':60,'igc9ho':1,'yc1nlc':30},'owdz09':{'xgmjmb':4,'pcs4ke':'cm3v2p','zq9bc2':(0.7,0.7,1.3,0.7,1.4,1.2),'f4c3ev':True,'agbl2q':260,'ua6wix':7},'jvyv2g':{'xgmjmb':5,'pcs4ke':'kqbrmq','zq9bc2':(1.6,0.85,1.6,1.1,1.1,1.4),'xbtfbs':True,'v6idii':40,'c6zvlh':2.0},'bpl1qw':{'xgmjmb':6,'pcs4ke':'bdoz6w','zq9bc2':(0.55,2.1,1.5,0.6,0.7,1.3),'lpug99':True,'prf7bn':10,'tn1th1':120,'vhbef4':150,'th2p39':25},'rkw3hg':{'xgmjmb':7,'pcs4ke':'zmygy0','zq9bc2':(0.8,1.1,1.0,0.8,1.0,1.3),'nddqhk':True,'g8wze4':70},'y3lxch':{'xgmjmb':8,'pcs4ke':'r3hxyj','zq9bc2':(1.8,0.75,0.9,2.4,1.2,1.5),'vcw2lb':True,'e0s41k':120,'qc6dr0':0.5},'az3m55':{'xgmjmb':9,'pcs4ke':'ew6tm2','zq9bc2':(0.35,1.5,0.5,0.5,0.6,0.8),'be2wnf':3},'kou83g':{'xgmjmb':10,'pcs4ke':'wkgeq2','zq9bc2':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={wb7f6fdh:{'urf1hx':int(k44nlz15(cq6qdy4l['xgmjmb'])['urf1hx']*cq6qdy4l['zq9bc2'][0]),'jo31yh':round(k44nlz15(cq6qdy4l['xgmjmb'])['jo31yh']*cq6qdy4l['zq9bc2'][1],2),'hzj7ub':int(k44nlz15(cq6qdy4l['xgmjmb'])['hzj7ub']*cq6qdy4l['zq9bc2'][2]),'rw8p74':int(k44nlz15(cq6qdy4l['xgmjmb'])['rw8p74']*cq6qdy4l['zq9bc2'][3]),'buzery':max(10,int(k44nlz15(cq6qdy4l['xgmjmb'])['buzery']*cq6qdy4l['zq9bc2'][4])),'hipi78':int(k44nlz15(cq6qdy4l['xgmjmb'])['hipi78']*cq6qdy4l['zq9bc2'][5]),'pcs4ke':iq5c34dx[cq6qdy4l['pcs4ke']],'xgmjmb':cq6qdy4l['xgmjmb'],'f4c3ev':cq6qdy4l.get('f4c3ev',False),'agbl2q':cq6qdy4l.get('agbl2q'),'ua6wix':cq6qdy4l.get('ua6wix'),'nddqhk':cq6qdy4l.get('nddqhk',False),'g8wze4':cq6qdy4l.get('g8wze4'),'be2wnf':cq6qdy4l.get('be2wnf'),'t7fr91':cq6qdy4l.get('t7fr91',False),'jr87iy':cq6qdy4l.get('jr87iy'),'mrf5a7':cq6qdy4l.get('mrf5a7'),'bx1ego':cq6qdy4l.get('bx1ego'),'hx0gu4':cq6qdy4l.get('hx0gu4'),'dzjq7w':cq6qdy4l.get('dzjq7w',False),'i1yy1j':cq6qdy4l.get('i1yy1j'),'igc9ho':cq6qdy4l.get('igc9ho'),'yc1nlc':cq6qdy4l.get('yc1nlc'),'lpug99':cq6qdy4l.get('lpug99',False),'prf7bn':cq6qdy4l.get('prf7bn'),'tn1th1':cq6qdy4l.get('tn1th1'),'vhbef4':cq6qdy4l.get('vhbef4'),'th2p39':cq6qdy4l.get('th2p39'),'xbtfbs':cq6qdy4l.get('xbtfbs',False),'v6idii':cq6qdy4l.get('v6idii'),'c6zvlh':cq6qdy4l.get('c6zvlh'),'vcw2lb':cq6qdy4l.get('vcw2lb',False),'e0s41k':cq6qdy4l.get('e0s41k'),'qc6dr0':cq6qdy4l.get('qc6dr0')}for(wb7f6fdh,cq6qdy4l)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda wb7f6fdh:k1wj0tpa[wb7f6fdh]['xgmjmb'])
uqjiujv6={'w1q8f6':{'jo31yh':10,'pgsb98':10,'yoztp7':6,'ykht8x':60,'rfu7bf':0,'pca7zv':None,'pcs4ke':iq5c34dx['edxoq2'],'yrp422':c0hpmnz1('assets/normal.png'),'futios':20,'ozdcuj':15},'bxb4y4':{'jo31yh':5,'pgsb98':8,'yoztp7':8,'ykht8x':90,'rfu7bf':999,'pca7zv':'flyback','en1x2g':250,'pcs4ke':iq5c34dx['kqbrmq'],'yrp422':c0hpmnz1('assets/boomerang.png'),'futios':20,'ozdcuj':27},'r4uov5':{'jo31yh':6,'pgsb98':6,'yoztp7':5,'ykht8x':100,'rfu7bf':0,'pca7zv':'homing','n5nhqr':0.08,'pcs4ke':iq5c34dx['bdoz6w'],'yrp422':c0hpmnz1('assets/homing.png'),'futios':20,'ozdcuj':20},'w2lx2t':{'jo31yh':14,'pgsb98':12,'yoztp7':4,'ykht8x':50,'rfu7bf':3,'pca7zv':'rfu7bf','pcs4ke':iq5c34dx['dzjssz'],'yrp422':c0hpmnz1('assets/pierce.png'),'futios':20,'ozdcuj':7},'k7rrbe':{'jo31yh':7,'pgsb98':15,'yoztp7':10,'ykht8x':70,'rfu7bf':0,'pca7zv':'explode','g8wze4':60,'pcs4ke':iq5c34dx['zmygy0'],'yrp422':c0hpmnz1('assets/explosive.png'),'futios':20,'ozdcuj':20},'m44c68':{'jo31yh':9,'pgsb98':7,'yoztp7':5,'ykht8x':60,'rfu7bf':0,'pca7zv':'split','ujqigy':3,'pcs4ke':iq5c34dx['ew6tm2'],'yrp422':c0hpmnz1('assets/split.png'),'futios':20,'ozdcuj':9},'s55ff1':{'jo31yh':7,'pgsb98':12,'yoztp7':6,'ykht8x':90,'rfu7bf':0,'pca7zv':None,'pcs4ke':iq5c34dx['cm3v2p']}}
uyhl1c32={'w1q8f6':'Normal Shot','bxb4y4':'Boomerang','r4uov5':'Homing Shot','w2lx2t':'Piercing Shot','k7rrbe':'Explosive Shot','m44c68':'Split Shot'}
mjh75lxo={'w1q8f6':15,'bxb4y4':25,'r4uov5':20,'w2lx2t':18,'k7rrbe':35,'m44c68':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
v4u89yjb=5
def n8k03w0f(j1ldqnk2):
 return 1+(j1ldqnk2-1)*0.12
def cu8el501(j1ldqnk2):
 return max(0.65,1-(j1ldqnk2-1)*0.07)
rcfnfhol={'v3c71u':{'riny2e':'Vitality','kj2jvq':'+20% Max Health','jz6wmd':8},'kk2y77':{'riny2e':'Swift Boots','kj2jvq':'+8% Move Speed','jz6wmd':5},'wurvqt':{'riny2e':'Regeneration','kj2jvq':'+1 HP/sec','jz6wmd':6},'tcu9td':{'riny2e':'Power','kj2jvq':'+6% Weapon Damage','jz6wmd':8},'o0mb1l':{'riny2e':'Haste','kj2jvq':'-5% Attack Cooldown','jz6wmd':6},'t8nn16':{'riny2e':'Armor','kj2jvq':'+5 Defense','jz6wmd':6},'t7wqp3':{'riny2e':'Wisdom','kj2jvq':'+15% XP Gain','jz6wmd':5}}
jsylztgx={'START_HEALTH':{'kp82kb':'sce4qg','riny2e':'Heart Crystal','kj2jvq':'+8% Starting Max Health','jz6wmd':10,'ktaq6u':15,'xfq3jz':1.35},'START_REGEN':{'kp82kb':'sce4qg','riny2e':'Regen Charm','kj2jvq':'+0.5 Starting HP/sec','jz6wmd':6,'ktaq6u':25,'xfq3jz':1.4},'START_DAMAGE':{'kp82kb':'ijj0v6','riny2e':'Sharp Edge','kj2jvq':'+4% Starting Damage','jz6wmd':10,'ktaq6u':20,'xfq3jz':1.35},'START_COOLDOWN':{'kp82kb':'ijj0v6','riny2e':'Quick Hands','kj2jvq':'-3% Starting Cooldown','jz6wmd':8,'ktaq6u':25,'xfq3jz':1.4},'START_SPEED':{'kp82kb':'hrctlt','riny2e':'Wind Charm','kj2jvq':'+3% Starting Speed','jz6wmd':8,'ktaq6u':18,'xfq3jz':1.35},'START_ARMOR':{'kp82kb':'hrctlt','riny2e':'Iron Skin','kj2jvq':'+2 Starting Armor','jz6wmd':10,'ktaq6u':15,'xfq3jz':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(cq6qdy4l['yrp422']),(cq6qdy4l['futios'],cq6qdy4l['ozdcuj']))for(key,cq6qdy4l)in uqjiujv6.items()if'yrp422'in cq6qdy4l}
def wg25cfzf(j1ldqnk2):
 return 1+0.08*j1ldqnk2
def j0kgazu4(j1ldqnk2):
 return 1+0.03*j1ldqnk2
def s8438tgb(j1ldqnk2):
 return 1+0.04*j1ldqnk2
def hu9n79gi(j1ldqnk2):
 return max(0.7,1-0.03*j1ldqnk2)
def r2muljav(j1ldqnk2):
 return j1ldqnk2*2
def d448n7od(j1ldqnk2):
 return j1ldqnk2*0.5
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
m53a5qbs=[int(100*1.3**(j1ldqnk2-1))for j1ldqnk2 in range(1,61)]
