import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def lcj883dh(k1taa0i5):
 return os.path.join(dnq4fmyz,k1taa0i5)
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
iq5c34dx={'xy79kv':(255,0,0),'fnn16u':(255,102,102),'xj2dg1':(139,0,0),'o5rlqi':(0,255,0),'w65dlx':(144,238,144),'yf77lu':(0,100,0),'vmdk5n':(0,0,255),'xn8wwi':(0,255,255),'iwu3bf':(0,0,128),'r3hxyj':(135,206,235),'l226pa':(255,255,0),'jl1qwe':(255,255,224),'k7bpgy':(128,128,0),'txzuu8':(255,165,0),'w2zeeq':(255,200,124),'n8k03w':(255,140,0),'tcu9td':(128,0,128),'r4uov5':(238,130,238),'m9bn18':(75,0,130),'dzjssz':(255,192,203),'ldz09w':(255,182,193),'dq3b9s':(255,105,180),'h7kr0a':(139,69,19),'uq0e27':(181,101,29),'ehet25':(92,46,13),'xyhhg8':(128,128,128),'wtolaq':(211,211,211),'jy66p6':(64,64,64),'rthy25':(0,128,128),'v5ff1b':(102,178,178),'twvwvi':(0,77,77),'e8a1ar':(255,0,255),'xu7dkn':(218,112,214),'xel501':(139,0,139),'hb1ajo':(255,215,0),'x429om':(192,192,192),'pta5iv':(128,0,0),'lcf4mn':(64,224,208),'pswrgv':(250,128,114),'r8imoe':(255,127,80),'vsjchz':(245,245,220),'gkok3q':(255,255,240),'nk7y6q':(240,230,140),'ibxanj':(0,0,0),'yl4zjd':(255,255,255)}
n2vlpys2=(90,90,100)
cq5uznof=(50,50,58)
z0xkxwd8=(120,120,132)
hyihair4=(70,70,80)
gyljexq7=['o5rlqi','xn8wwi','vmdk5n','tcu9td','e8a1ar','txzuu8','xy79kv','xj2dg1','xyhhg8','hb1ajo']
def nd96qe3r(pcvsqame):
 return{'m44c68':100*1.3**(pcvsqame-1),'hx0gu4':min(rv86wzs3*0.75,1.3*1.13**(pcvsqame-1)),'p6fmr5':10*1.25**(pcvsqame-1),'w2lx2t':5*1.2**(pcvsqame-1),'j1f537':max(10,60*0.9**(pcvsqame-1)),'ozdcuj':26*1.27**(pcvsqame-1)}
s0clbr7t={'m1v3zo':{'dzjq7w':1,'rpeqyd':'o5rlqi','qc6dr0':(1.0,1.0,1.0,1.0,1.0,1.0)},'kou83g':{'dzjq7w':2,'rpeqyd':'xn8wwi','qc6dr0':(0.6,1.8,0.7,0.8,0.8,1.0),'c37qqy':True,'kqbrmq':150,'fkmuso':2.5,'i6ozx2':20,'w1q8f6':90},'n7csuy':{'dzjq7w':3,'rpeqyd':'xyhhg8','qc6dr0':(2.6,0.45,0.6,1.6,1.3,1.3),'e56waf':True,'eqkwqh':60,'w9mda9':1,'kk2y77':30},'ceb875':{'dzjq7w':4,'rpeqyd':'tcu9td','qc6dr0':(0.7,0.7,1.3,0.7,1.4,1.2),'fuxk0a':True,'t00ucr':260,'kp82kb':7},'vmwi9s':{'dzjq7w':5,'rpeqyd':'txzuu8','qc6dr0':(1.6,0.85,1.6,1.1,1.1,1.4),'w9laac':True,'gbwcv6':40,'nddqhk':2.0},'t0fzau':{'dzjq7w':6,'rpeqyd':'e8a1ar','qc6dr0':(0.55,2.1,1.5,0.6,0.7,1.3),'mrf5a7':True,'kj2jvq':10,'onlt8d':120,'rw8p74':150,'pcs4ke':25},'msz6rv':{'dzjq7w':7,'rpeqyd':'xy79kv','qc6dr0':(0.8,1.1,1.0,0.8,1.0,1.3),'wurvqt':True,'og8cd3':70},'wkgeq2':{'dzjq7w':8,'rpeqyd':'xj2dg1','qc6dr0':(1.8,0.75,0.9,2.4,1.2,1.5),'o6d10a':True,'v9hbn5':120,'da7yvd':0.5},'ew6tm2':{'dzjq7w':9,'rpeqyd':'hb1ajo','qc6dr0':(0.35,1.5,0.5,0.5,0.6,0.8),'pgsb98':3},'amyrsv':{'dzjq7w':10,'rpeqyd':'xel501','qc6dr0':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={zsw2292m:{'m44c68':int(nd96qe3r(d1ieixwc['dzjq7w'])['m44c68']*d1ieixwc['qc6dr0'][0]),'hx0gu4':round(nd96qe3r(d1ieixwc['dzjq7w'])['hx0gu4']*d1ieixwc['qc6dr0'][1],2),'p6fmr5':int(nd96qe3r(d1ieixwc['dzjq7w'])['p6fmr5']*d1ieixwc['qc6dr0'][2]),'w2lx2t':int(nd96qe3r(d1ieixwc['dzjq7w'])['w2lx2t']*d1ieixwc['qc6dr0'][3]),'j1f537':max(10,int(nd96qe3r(d1ieixwc['dzjq7w'])['j1f537']*d1ieixwc['qc6dr0'][4])),'ozdcuj':int(nd96qe3r(d1ieixwc['dzjq7w'])['ozdcuj']*d1ieixwc['qc6dr0'][5]),'rpeqyd':iq5c34dx[d1ieixwc['rpeqyd']],'dzjq7w':d1ieixwc['dzjq7w'],'fuxk0a':d1ieixwc.get('fuxk0a',False),'t00ucr':d1ieixwc.get('t00ucr'),'kp82kb':d1ieixwc.get('kp82kb'),'wurvqt':d1ieixwc.get('wurvqt',False),'og8cd3':d1ieixwc.get('og8cd3'),'pgsb98':d1ieixwc.get('pgsb98'),'c37qqy':d1ieixwc.get('c37qqy',False),'kqbrmq':d1ieixwc.get('kqbrmq'),'fkmuso':d1ieixwc.get('fkmuso'),'i6ozx2':d1ieixwc.get('i6ozx2'),'w1q8f6':d1ieixwc.get('w1q8f6'),'e56waf':d1ieixwc.get('e56waf',False),'eqkwqh':d1ieixwc.get('eqkwqh'),'w9mda9':d1ieixwc.get('w9mda9'),'kk2y77':d1ieixwc.get('kk2y77'),'mrf5a7':d1ieixwc.get('mrf5a7',False),'kj2jvq':d1ieixwc.get('kj2jvq'),'onlt8d':d1ieixwc.get('onlt8d'),'rw8p74':d1ieixwc.get('rw8p74'),'pcs4ke':d1ieixwc.get('pcs4ke'),'w9laac':d1ieixwc.get('w9laac',False),'gbwcv6':d1ieixwc.get('gbwcv6'),'nddqhk':d1ieixwc.get('nddqhk'),'o6d10a':d1ieixwc.get('o6d10a',False),'v9hbn5':d1ieixwc.get('v9hbn5'),'da7yvd':d1ieixwc.get('da7yvd')}for(zsw2292m,d1ieixwc)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda zsw2292m:k1wj0tpa[zsw2292m]['dzjq7w'])
uqjiujv6={'umfbuv':{'hx0gu4':10,'v3c71u':10,'xfq3jz':6,'mmgvu4':60,'ktaq6u':0,'t7fr91':None,'rpeqyd':iq5c34dx['yl4zjd'],'l4f9ye':lcj883dh('assets/normal.png'),'igc9ho':20,'az3m55':15},'cgsq7a':{'hx0gu4':5,'v3c71u':8,'xfq3jz':8,'mmgvu4':90,'ktaq6u':999,'t7fr91':'flyback','y3lxch':250,'rpeqyd':iq5c34dx['txzuu8'],'l4f9ye':lcj883dh('assets/boomerang.png'),'igc9ho':20,'az3m55':27},'xutxzb':{'hx0gu4':6,'v3c71u':6,'xfq3jz':5,'mmgvu4':100,'ktaq6u':0,'t7fr91':'homing','g8wze4':0.08,'rpeqyd':iq5c34dx['e8a1ar'],'l4f9ye':lcj883dh('assets/homing.png'),'igc9ho':20,'az3m55':20},'m314cq':{'hx0gu4':14,'v3c71u':12,'xfq3jz':4,'mmgvu4':50,'ktaq6u':3,'t7fr91':'ktaq6u','rpeqyd':iq5c34dx['xn8wwi'],'l4f9ye':lcj883dh('assets/pierce.png'),'igc9ho':20,'az3m55':7},'wxgnrf':{'hx0gu4':7,'v3c71u':15,'xfq3jz':10,'mmgvu4':70,'ktaq6u':0,'t7fr91':'explode','og8cd3':60,'rpeqyd':iq5c34dx['xy79kv'],'l4f9ye':lcj883dh('assets/explosive.png'),'igc9ho':20,'az3m55':20},'k7rrbe':{'hx0gu4':9,'v3c71u':7,'xfq3jz':5,'mmgvu4':60,'ktaq6u':0,'t7fr91':'split','bx1ego':3,'rpeqyd':iq5c34dx['hb1ajo'],'l4f9ye':lcj883dh('assets/split.png'),'igc9ho':20,'az3m55':9},'g0ht1t':{'hx0gu4':7,'v3c71u':12,'xfq3jz':6,'mmgvu4':90,'ktaq6u':0,'t7fr91':None,'rpeqyd':iq5c34dx['tcu9td']}}
uyhl1c32={'umfbuv':'Normal Shot','cgsq7a':'Boomerang','xutxzb':'Homing Shot','m314cq':'Piercing Shot','wxgnrf':'Explosive Shot','k7rrbe':'Split Shot'}
mjh75lxo={'umfbuv':15,'cgsq7a':25,'xutxzb':20,'m314cq':18,'wxgnrf':35,'k7rrbe':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
x37pqkoj=5
def hhl1737s(pcvsqame):
 return 1+(pcvsqame-1)*0.12
def mabkae6a(pcvsqame):
 return max(0.65,1-(pcvsqame-1)*0.07)
rqf5q14j={'pqpva5':{'cxf5x9':'Vitality','mviifr':'+20% Max Health','hzj7ub':8},'clslay':{'cxf5x9':'Swift Boots','mviifr':'+8% Move Speed','hzj7ub':5},'kjuw7w':{'cxf5x9':'Regeneration','mviifr':'+1 HP/sec','hzj7ub':6},'huplvq':{'cxf5x9':'Power','mviifr':'+6% Weapon Damage','hzj7ub':8},'zcjn99':{'cxf5x9':'Haste','mviifr':'-5% Attack Cooldown','hzj7ub':6},'jayeqa':{'cxf5x9':'Armor','mviifr':'+5 Defense','hzj7ub':6},'hn3ksg':{'cxf5x9':'Wisdom','mviifr':'+15% XP Gain','hzj7ub':5}}
ibps3y70={'START_HEALTH':{'k1yjfe':'i1yy1j','cxf5x9':'Heart Crystal','mviifr':'+8% Starting Max Health','hzj7ub':10,'yl6lgj':15,'wzwl3z':1.35},'START_REGEN':{'k1yjfe':'i1yy1j','cxf5x9':'Regen Charm','mviifr':'+0.5 Starting HP/sec','hzj7ub':6,'yl6lgj':25,'wzwl3z':1.4},'START_DAMAGE':{'k1yjfe':'bdoz6w','cxf5x9':'Sharp Edge','mviifr':'+4% Starting Damage','hzj7ub':10,'yl6lgj':20,'wzwl3z':1.35},'START_COOLDOWN':{'k1yjfe':'bdoz6w','cxf5x9':'Quick Hands','mviifr':'-3% Starting Cooldown','hzj7ub':8,'yl6lgj':25,'wzwl3z':1.4},'START_SPEED':{'k1yjfe':'e0s41k','cxf5x9':'Wind Charm','mviifr':'+3% Starting Speed','hzj7ub':8,'yl6lgj':18,'wzwl3z':1.35},'START_ARMOR':{'k1yjfe':'e0s41k','cxf5x9':'Iron Skin','mviifr':'+2 Starting Armor','hzj7ub':10,'yl6lgj':15,'wzwl3z':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(d1ieixwc['l4f9ye']),(d1ieixwc['igc9ho'],d1ieixwc['az3m55']))for(key,d1ieixwc)in uqjiujv6.items()if'l4f9ye'in d1ieixwc}
def mcup8ijl(pcvsqame):
 return 1+0.08*pcvsqame
def tb4ldims(pcvsqame):
 return 1+0.03*pcvsqame
def hp89fkbi(pcvsqame):
 return 1+0.04*pcvsqame
def y2f7atwy(pcvsqame):
 return max(0.7,1-0.03*pcvsqame)
def v6g298cq(pcvsqame):
 return pcvsqame*2
def zo3lqi7e(pcvsqame):
 return pcvsqame*0.5
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
cqoldfor=[int(100*1.3**(pcvsqame-1))for pcvsqame in range(1,61)]
