import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def duhxid4n(myrp5ge0):
 return os.path.join(dnq4fmyz,myrp5ge0)
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
iq5c34dx={'yl6lgj':(255,0,0),'k7rrbe':(255,102,102),'pta5iv':(139,0,0),'xu7dkn':(0,255,0),'r3hxyj':(144,238,144),'v5ff1b':(0,100,0),'xutxzb':(0,0,255),'w65dlx':(0,255,255),'yl4zjd':(0,0,128),'bdoz6w':(135,206,235),'zmygy0':(255,255,0),'n7csuy':(255,255,224),'l226pa':(128,128,0),'p6fmr5':(255,165,0),'clslay':(255,200,124),'e8a1ar':(255,140,0),'o6d10a':(128,0,128),'w2lx2t':(238,130,238),'xy79kv':(75,0,130),'da7yvd':(255,192,203),'kou83g':(255,182,193),'tcu9td':(255,105,180),'gkok3q':(139,69,19),'wkgeq2':(181,101,29),'ldz09w':(92,46,13),'txzuu8':(128,128,128),'x429om':(211,211,211),'fnn16u':(64,64,64),'kqbrmq':(0,128,128),'ew6tm2':(102,178,178),'pqpva5':(0,77,77),'rthy25':(255,0,255),'j1f537':(218,112,214),'jl1qwe':(139,0,139),'k7bpgy':(255,215,0),'rpeqyd':(192,192,192),'lcf4mn':(128,0,0),'fkmuso':(64,224,208),'tudttj':(250,128,114),'wtolaq':(255,127,80),'o5rlqi':(245,245,220),'kjuw7w':(255,255,240),'pswrgv':(240,230,140),'m1v3zo':(0,0,0),'mviifr':(255,255,255)}
hyihair4=(90,90,100)
qqu7eeqt=(50,50,58)
cq5uznof=(120,120,132)
wa11dpg8=(70,70,80)
gyljexq7=['xu7dkn','w65dlx','xutxzb','o6d10a','rthy25','p6fmr5','yl6lgj','pta5iv','txzuu8','k7bpgy']
def mnx39rbs(crsb4gf1):
 return{'bx1ego':100*1.3**(crsb4gf1-1),'ykht8x':min(yswjckjl*0.75,1.3*1.13**(crsb4gf1-1)),'wurvqt':10*1.25**(crsb4gf1-1),'qc6dr0':5*1.2**(crsb4gf1-1),'og8cd3':max(10,60*0.9**(crsb4gf1-1)),'tgr8w2':26*1.27**(crsb4gf1-1)}
s0clbr7t={'m314cq':{'yoztp7':1,'hpvwzo':'xu7dkn','dzjq7w':(1.0,1.0,1.0,1.0,1.0,1.0)},'v3c71u':{'yoztp7':2,'hpvwzo':'w65dlx','dzjq7w':(0.6,1.8,0.7,0.8,0.8,1.0),'edxoq2':True,'hzj7ub':150,'buzery':2.5,'mmgvu4':20,'t7wqp3':90},'i6ozx2':{'yoztp7':3,'hpvwzo':'txzuu8','dzjq7w':(2.6,0.45,0.6,1.6,1.3,1.3),'xfq3jz':True,'pgsb98':60,'hx0gu4':1,'t7fr91':30},'hiac2e':{'yoztp7':4,'hpvwzo':'o6d10a','dzjq7w':(0.7,0.7,1.3,0.7,1.4,1.2),'ozdcuj':True,'urf1hx':260,'igc9ho':7},'nk7y6q':{'yoztp7':5,'hpvwzo':'p6fmr5','dzjq7w':(1.6,0.85,1.6,1.1,1.1,1.4),'agbl2q':True,'th2p39':40,'f4c3ev':2.0},'niyhhg':{'yoztp7':6,'hpvwzo':'rthy25','dzjq7w':(0.55,2.1,1.5,0.6,0.7,1.3),'hrctlt':True,'rfu7bf':10,'zq9bc2':120,'bohxs7':150,'oarxab':25},'dq3b9s':{'yoztp7':7,'hpvwzo':'yl6lgj','dzjq7w':(0.8,1.1,1.0,0.8,1.0,1.3),'t00ucr':True,'pcs4ke':70},'w2ugl6':{'yoztp7':8,'hpvwzo':'pta5iv','dzjq7w':(1.8,0.75,0.9,2.4,1.2,1.5),'eqkwqh':True,'y3lxch':120,'e56waf':0.5},'w1q8f6':{'yoztp7':9,'hpvwzo':'k7bpgy','dzjq7w':(0.35,1.5,0.5,0.5,0.6,0.8),'r7myow':3},'iwu3bf':{'yoztp7':10,'hpvwzo':'jl1qwe','dzjq7w':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={wy0mahym:{'bx1ego':int(mnx39rbs(obc2nnuv['yoztp7'])['bx1ego']*obc2nnuv['dzjq7w'][0]),'ykht8x':round(mnx39rbs(obc2nnuv['yoztp7'])['ykht8x']*obc2nnuv['dzjq7w'][1],2),'wurvqt':int(mnx39rbs(obc2nnuv['yoztp7'])['wurvqt']*obc2nnuv['dzjq7w'][2]),'qc6dr0':int(mnx39rbs(obc2nnuv['yoztp7'])['qc6dr0']*obc2nnuv['dzjq7w'][3]),'og8cd3':max(10,int(mnx39rbs(obc2nnuv['yoztp7'])['og8cd3']*obc2nnuv['dzjq7w'][4])),'tgr8w2':int(mnx39rbs(obc2nnuv['yoztp7'])['tgr8w2']*obc2nnuv['dzjq7w'][5]),'hpvwzo':iq5c34dx[obc2nnuv['hpvwzo']],'yoztp7':obc2nnuv['yoztp7'],'ozdcuj':obc2nnuv.get('ozdcuj',False),'urf1hx':obc2nnuv.get('urf1hx'),'igc9ho':obc2nnuv.get('igc9ho'),'t00ucr':obc2nnuv.get('t00ucr',False),'pcs4ke':obc2nnuv.get('pcs4ke'),'r7myow':obc2nnuv.get('r7myow'),'edxoq2':obc2nnuv.get('edxoq2',False),'hzj7ub':obc2nnuv.get('hzj7ub'),'buzery':obc2nnuv.get('buzery'),'mmgvu4':obc2nnuv.get('mmgvu4'),'t7wqp3':obc2nnuv.get('t7wqp3'),'xfq3jz':obc2nnuv.get('xfq3jz',False),'pgsb98':obc2nnuv.get('pgsb98'),'hx0gu4':obc2nnuv.get('hx0gu4'),'t7fr91':obc2nnuv.get('t7fr91'),'hrctlt':obc2nnuv.get('hrctlt',False),'rfu7bf':obc2nnuv.get('rfu7bf'),'zq9bc2':obc2nnuv.get('zq9bc2'),'bohxs7':obc2nnuv.get('bohxs7'),'oarxab':obc2nnuv.get('oarxab'),'agbl2q':obc2nnuv.get('agbl2q',False),'th2p39':obc2nnuv.get('th2p39'),'f4c3ev':obc2nnuv.get('f4c3ev'),'eqkwqh':obc2nnuv.get('eqkwqh',False),'y3lxch':obc2nnuv.get('y3lxch'),'e56waf':obc2nnuv.get('e56waf')}for(wy0mahym,obc2nnuv)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda wy0mahym:k1wj0tpa[wy0mahym]['yoztp7'])
uqjiujv6={'hn3ksg':{'ykht8x':10,'cxf5x9':10,'riny2e':6,'nddqhk':60,'yc1nlc':0,'udt8cq':None,'hpvwzo':iq5c34dx['mviifr'],'rw8p74':duhxid4n('assets/normal.png'),'jo31yh':20,'jr87iy':15},'m9bn18':{'ykht8x':5,'cxf5x9':8,'riny2e':8,'nddqhk':90,'yc1nlc':999,'udt8cq':'flyback','ijj0v6':250,'hpvwzo':iq5c34dx['p6fmr5'],'rw8p74':duhxid4n('assets/boomerang.png'),'jo31yh':20,'jr87iy':27},'dzjssz':{'ykht8x':6,'cxf5x9':6,'riny2e':5,'nddqhk':100,'yc1nlc':0,'udt8cq':'homing','voeytl':0.08,'hpvwzo':iq5c34dx['rthy25'],'rw8p74':duhxid4n('assets/homing.png'),'jo31yh':20,'jr87iy':20},'v9hbn5':{'ykht8x':14,'cxf5x9':12,'riny2e':4,'nddqhk':50,'yc1nlc':3,'udt8cq':'yc1nlc','hpvwzo':iq5c34dx['w65dlx'],'rw8p74':duhxid4n('assets/pierce.png'),'jo31yh':20,'jr87iy':7},'umfbuv':{'ykht8x':7,'cxf5x9':15,'riny2e':10,'nddqhk':70,'yc1nlc':0,'udt8cq':'explode','pcs4ke':60,'hpvwzo':iq5c34dx['yl6lgj'],'rw8p74':duhxid4n('assets/explosive.png'),'jo31yh':20,'jr87iy':20},'c37qqy':{'ykht8x':9,'cxf5x9':7,'riny2e':5,'nddqhk':60,'yc1nlc':0,'udt8cq':'split','jz6wmd':3,'hpvwzo':iq5c34dx['k7bpgy'],'rw8p74':duhxid4n('assets/split.png'),'jo31yh':20,'jr87iy':9},'fgb1aj':{'ykht8x':7,'cxf5x9':12,'riny2e':6,'nddqhk':90,'yc1nlc':0,'udt8cq':None,'hpvwzo':iq5c34dx['o6d10a']}}
uyhl1c32={'hn3ksg':'Normal Shot','m9bn18':'Boomerang','dzjssz':'Homing Shot','v9hbn5':'Piercing Shot','umfbuv':'Explosive Shot','c37qqy':'Split Shot'}
mjh75lxo={'hn3ksg':15,'m9bn18':25,'dzjssz':20,'v9hbn5':18,'umfbuv':35,'c37qqy':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
v4u89yjb=5
def vsjchzjq(crsb4gf1):
 return 1+(crsb4gf1-1)*0.12
def yjr0fzau(crsb4gf1):
 return max(0.65,1-(crsb4gf1-1)*0.07)
rcfnfhol={'r4uov5':{'kj2jvq':'Vitality','vcw2lb':'+20% Max Health','gbwcv6':8},'wzwl3z':{'kj2jvq':'Swift Boots','vcw2lb':'+8% Move Speed','gbwcv6':5},'k1yjfe':{'kj2jvq':'Regeneration','vcw2lb':'+1 HP/sec','gbwcv6':6},'w2zeeq':{'kj2jvq':'Power','vcw2lb':'+6% Weapon Damage','gbwcv6':8},'uq0e27':{'kj2jvq':'Haste','vcw2lb':'-5% Attack Cooldown','gbwcv6':6},'tqxgnr':{'kj2jvq':'Armor','vcw2lb':'+5 Defense','gbwcv6':6},'cm3v2p':{'kj2jvq':'Wisdom','vcw2lb':'+15% XP Gain','gbwcv6':5}}
jsylztgx={'START_HEALTH':{'w9mda9':'be2wnf','kj2jvq':'Heart Crystal','vcw2lb':'+8% Starting Max Health','gbwcv6':10,'kk2y77':15,'l4f9ye':1.35},'START_REGEN':{'w9mda9':'be2wnf','kj2jvq':'Regen Charm','vcw2lb':'+0.5 Starting HP/sec','gbwcv6':6,'kk2y77':25,'l4f9ye':1.4},'START_DAMAGE':{'w9mda9':'ntxrgn','kj2jvq':'Sharp Edge','vcw2lb':'+4% Starting Damage','gbwcv6':10,'kk2y77':20,'l4f9ye':1.35},'START_COOLDOWN':{'w9mda9':'ntxrgn','kj2jvq':'Quick Hands','vcw2lb':'-3% Starting Cooldown','gbwcv6':8,'kk2y77':25,'l4f9ye':1.4},'START_SPEED':{'w9mda9':'en1x2g','kj2jvq':'Wind Charm','vcw2lb':'+3% Starting Speed','gbwcv6':8,'kk2y77':18,'l4f9ye':1.35},'START_ARMOR':{'w9mda9':'en1x2g','kj2jvq':'Iron Skin','vcw2lb':'+2 Starting Armor','gbwcv6':10,'kk2y77':15,'l4f9ye':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(obc2nnuv['rw8p74']),(obc2nnuv['jo31yh'],obc2nnuv['jr87iy']))for(key,obc2nnuv)in uqjiujv6.items()if'rw8p74'in obc2nnuv}
def fdxj37c9(crsb4gf1):
 return 1+0.08*crsb4gf1
def bihsa7he(crsb4gf1):
 return 1+0.03*crsb4gf1
def r2muljav(crsb4gf1):
 return 1+0.04*crsb4gf1
def jr5rdnpx(crsb4gf1):
 return max(0.7,1-0.03*crsb4gf1)
def chx3d43e(crsb4gf1):
 return crsb4gf1*2
def hu9n79gi(crsb4gf1):
 return crsb4gf1*0.5
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
m53a5qbs=[int(100*1.3**(crsb4gf1-1))for crsb4gf1 in range(1,61)]
