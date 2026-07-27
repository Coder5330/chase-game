import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def yx4w6xlp(f8rtm4j3):
 return os.path.join(dnq4fmyz,f8rtm4j3)
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
iq5c34dx={'wxgnrf':(255,0,0),'h7kr0a':(255,102,102),'hfy981':(139,0,0),'nngmx1':(0,255,0),'vmdk5n':(144,238,144),'km3o55':(0,100,0),'vf9pml':(0,0,255),'inui3d':(0,255,255),'ehet25':(0,0,128),'xutxzb':(135,206,235),'v5ff1b':(255,255,0),'zcjn99':(255,255,224),'yf77lu':(128,128,0),'xel501':(255,165,0),'msz6rv':(255,200,124),'bkbtfs':(255,140,0),'amyrsv':(128,0,128),'w2zeeq':(238,130,238),'jayeqa':(75,0,130),'twvwvi':(255,192,203),'cgsq7a':(255,182,193),'ceb875':(255,105,180),'oqo09v':(139,69,19),'vsjchz':(181,101,29),'p3yu6v':(92,46,13),'i1l7dy':(128,128,128),'ibxanj':(211,211,211),'jb3n27':(64,64,64),'wtolaq':(0,128,128),'vmwi9s':(102,178,178),'sshkoe':(0,77,77),'r8imoe':(255,0,255),'n8k03w':(218,112,214),'h047ww':(139,0,139),'uuu9si':(255,215,0),'m1v3zo':(192,192,192),'xn8wwi':(128,0,0),'w65dlx':(64,224,208),'xyhhg8':(250,128,114),'ruudqf':(255,127,80),'rodwmq':(245,245,220),'g0ht1t':(255,255,240),'t0fzau':(240,230,140),'vpd2ts':(0,0,0),'ldz09w':(255,255,255)}
gyljexq7=['nngmx1','inui3d','vf9pml','amyrsv','r8imoe','xel501','wxgnrf','hfy981','i1l7dy','uuu9si']
def v4u89yjb(nd31k9qm):
 return{'l226pa':100*1.3**(nd31k9qm-1),'fkmuso':min(hyihair4*0.75,1.3*1.13**(nd31k9qm-1)),'jl1qwe':10*1.25**(nd31k9qm-1),'r3hxyj':5*1.2**(nd31k9qm-1),'e8a1ar':max(10,60*0.9**(nd31k9qm-1)),'edxoq2':26*1.27**(nd31k9qm-1)}
s0clbr7t={'f9w9pf':{'az3m55':1,'xu7dkn':'nngmx1','w2ugl6':(1.0,1.0,1.0,1.0,1.0,1.0)},'m9bn18':{'az3m55':2,'xu7dkn':'inui3d','w2ugl6':(0.6,1.8,0.7,0.8,0.8,1.0),'xy79kv':True,'wkgeq2':150,'x429om':2.5,'pswrgv':20,'kjuw7w':90},'uq0e27':{'az3m55':3,'xu7dkn':'i1l7dy','w2ugl6':(2.6,0.45,0.6,1.6,1.3,1.3),'lcf4mn':True,'r4uov5':60,'hn3ksg':1,'yl4zjd':30},'ucu7on':{'az3m55':4,'xu7dkn':'amyrsv','w2ugl6':(0.7,0.7,1.3,0.7,1.4,1.2),'v3c71u':True,'wzwl3z':260,'bdoz6w':7},'qe6a9h':{'az3m55':5,'xu7dkn':'xel501','w2ugl6':(1.6,0.85,1.6,1.1,1.1,1.4),'e56waf':True,'kk2y77':40,'eqkwqh':2.0},'ggxu8u':{'az3m55':6,'xu7dkn':'r8imoe','w2ugl6':(0.55,2.1,1.5,0.6,0.7,1.3),'cm3v2p':True,'og8cd3':10,'zmygy0':120,'wurvqt':150,'c37qqy':25},'k4ow3l':{'az3m55':7,'xu7dkn':'wxgnrf','w2ugl6':(0.8,1.1,1.0,0.8,1.0,1.3),'ew6tm2':True,'n7csuy':70},'o5rlqi':{'az3m55':8,'xu7dkn':'hfy981','w2ugl6':(1.8,0.75,0.9,2.4,1.2,1.5),'iwu3bf':True,'pta5iv':120,'pqpva5':0.5},'nk7y6q':{'az3m55':9,'xu7dkn':'uuu9si','w2ugl6':(0.35,1.5,0.5,0.5,0.6,0.8),'i6ozx2':3},'cr0tjo':{'az3m55':10,'xu7dkn':'h047ww','w2ugl6':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={a8ax40dt:{'l226pa':int(v4u89yjb(uysal8m1['az3m55'])['l226pa']*uysal8m1['w2ugl6'][0]),'fkmuso':round(v4u89yjb(uysal8m1['az3m55'])['fkmuso']*uysal8m1['w2ugl6'][1],2),'jl1qwe':int(v4u89yjb(uysal8m1['az3m55'])['jl1qwe']*uysal8m1['w2ugl6'][2]),'r3hxyj':int(v4u89yjb(uysal8m1['az3m55'])['r3hxyj']*uysal8m1['w2ugl6'][3]),'e8a1ar':max(10,int(v4u89yjb(uysal8m1['az3m55'])['e8a1ar']*uysal8m1['w2ugl6'][4])),'edxoq2':int(v4u89yjb(uysal8m1['az3m55'])['edxoq2']*uysal8m1['w2ugl6'][5]),'xu7dkn':iq5c34dx[uysal8m1['xu7dkn']],'az3m55':uysal8m1['az3m55'],'v3c71u':uysal8m1.get('v3c71u',False),'wzwl3z':uysal8m1.get('wzwl3z'),'bdoz6w':uysal8m1.get('bdoz6w'),'ew6tm2':uysal8m1.get('ew6tm2',False),'n7csuy':uysal8m1.get('n7csuy'),'i6ozx2':uysal8m1.get('i6ozx2'),'xy79kv':uysal8m1.get('xy79kv',False),'wkgeq2':uysal8m1.get('wkgeq2'),'x429om':uysal8m1.get('x429om'),'pswrgv':uysal8m1.get('pswrgv'),'kjuw7w':uysal8m1.get('kjuw7w'),'lcf4mn':uysal8m1.get('lcf4mn',False),'r4uov5':uysal8m1.get('r4uov5'),'hn3ksg':uysal8m1.get('hn3ksg'),'yl4zjd':uysal8m1.get('yl4zjd'),'cm3v2p':uysal8m1.get('cm3v2p',False),'og8cd3':uysal8m1.get('og8cd3'),'zmygy0':uysal8m1.get('zmygy0'),'wurvqt':uysal8m1.get('wurvqt'),'c37qqy':uysal8m1.get('c37qqy'),'e56waf':uysal8m1.get('e56waf',False),'kk2y77':uysal8m1.get('kk2y77'),'eqkwqh':uysal8m1.get('eqkwqh'),'iwu3bf':uysal8m1.get('iwu3bf',False),'pta5iv':uysal8m1.get('pta5iv'),'pqpva5':uysal8m1.get('pqpva5')}for(a8ax40dt,uysal8m1)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda a8ax40dt:k1wj0tpa[a8ax40dt]['az3m55'])
uqjiujv6={'jy66p6':{'fkmuso':10,'tcu9td':10,'w1q8f6':6,'o6d10a':60,'rpeqyd':0,'kqbrmq':None,'xu7dkn':iq5c34dx['ldz09w'],'j1f537':yx4w6xlp('assets/normal.png'),'l4f9ye':20,'p6fmr5':15},'huh17j':{'fkmuso':5,'tcu9td':8,'w1q8f6':8,'o6d10a':90,'rpeqyd':999,'kqbrmq':'flyback','rthy25':250,'xu7dkn':iq5c34dx['xel501'],'j1f537':yx4w6xlp('assets/boomerang.png'),'l4f9ye':20,'p6fmr5':27},'b7iyf0':{'fkmuso':6,'tcu9td':6,'w1q8f6':5,'o6d10a':100,'rpeqyd':0,'kqbrmq':'homing','w9mda9':0.08,'xu7dkn':iq5c34dx['r8imoe'],'j1f537':yx4w6xlp('assets/homing.png'),'l4f9ye':20,'p6fmr5':20},'xj2dg1':{'fkmuso':14,'tcu9td':12,'w1q8f6':4,'o6d10a':50,'rpeqyd':3,'kqbrmq':'rpeqyd','xu7dkn':iq5c34dx['inui3d'],'j1f537':yx4w6xlp('assets/pierce.png'),'l4f9ye':20,'p6fmr5':7},'n1eeur':{'fkmuso':7,'tcu9td':15,'w1q8f6':10,'o6d10a':70,'rpeqyd':0,'kqbrmq':'explode','n7csuy':60,'xu7dkn':iq5c34dx['wxgnrf'],'j1f537':yx4w6xlp('assets/explosive.png'),'l4f9ye':20,'p6fmr5':20},'gkok3q':{'fkmuso':9,'tcu9td':7,'w1q8f6':5,'o6d10a':60,'rpeqyd':0,'kqbrmq':'split','w2lx2t':3,'xu7dkn':iq5c34dx['uuu9si'],'j1f537':yx4w6xlp('assets/split.png'),'l4f9ye':20,'p6fmr5':9},'c88d0t':{'fkmuso':7,'tcu9td':12,'w1q8f6':6,'o6d10a':90,'rpeqyd':0,'kqbrmq':None,'xu7dkn':iq5c34dx['amyrsv']}}
uyhl1c32={'jy66p6':'Normal Shot','huh17j':'Boomerang','b7iyf0':'Homing Shot','xj2dg1':'Piercing Shot','n1eeur':'Explosive Shot','gkok3q':'Split Shot'}
mjh75lxo={'jy66p6':15,'huh17j':25,'b7iyf0':20,'xj2dg1':18,'n1eeur':35,'gkok3q':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
jdiuovw1=5
def jh55hewl(nd31k9qm):
 return 1+(nd31k9qm-1)*0.12
def j7f00ter(nd31k9qm):
 return max(0.65,1-(nd31k9qm-1)*0.07)
cq5uznof={'huplvq':{'v9hbn5':'Vitality','clslay':'+20% Max Health','yl6lgj':8},'dq3b9s':{'v9hbn5':'Swift Boots','clslay':'+8% Move Speed','yl6lgj':5},'hb1ajo':{'v9hbn5':'Regeneration','clslay':'+1 HP/sec','yl6lgj':6},'muhclr':{'v9hbn5':'Power','clslay':'+6% Weapon Damage','yl6lgj':8},'ka3yjt':{'v9hbn5':'Haste','clslay':'-5% Attack Cooldown','yl6lgj':6},'wcwt04':{'v9hbn5':'Armor','clslay':'+5 Defense','yl6lgj':6},'fnn16u':{'v9hbn5':'Wisdom','clslay':'+15% XP Gain','yl6lgj':5}}
ibps3y70={'START_HEALTH':{'k7bpgy':'hpvwzo','v9hbn5':'Heart Crystal','clslay':'+8% Starting Max Health','yl6lgj':10,'umfbuv':15,'dzjssz':1.35},'START_REGEN':{'k7bpgy':'hpvwzo','v9hbn5':'Regen Charm','clslay':'+0.5 Starting HP/sec','yl6lgj':6,'umfbuv':25,'dzjssz':1.4},'START_DAMAGE':{'k7bpgy':'m314cq','v9hbn5':'Sharp Edge','clslay':'+4% Starting Damage','yl6lgj':10,'umfbuv':20,'dzjssz':1.35},'START_COOLDOWN':{'k7bpgy':'m314cq','v9hbn5':'Quick Hands','clslay':'-3% Starting Cooldown','yl6lgj':8,'umfbuv':25,'dzjssz':1.4},'START_SPEED':{'k7bpgy':'tudttj','v9hbn5':'Wind Charm','clslay':'+3% Starting Speed','yl6lgj':8,'umfbuv':18,'dzjssz':1.35},'START_ARMOR':{'k7bpgy':'tudttj','v9hbn5':'Iron Skin','clslay':'+2 Starting Armor','yl6lgj':10,'umfbuv':15,'dzjssz':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(uysal8m1['j1f537']),(uysal8m1['l4f9ye'],uysal8m1['p6fmr5']))for(key,uysal8m1)in uqjiujv6.items()if'j1f537'in uysal8m1}
def n04cdpqv(nd31k9qm):
 return 1+0.08*nd31k9qm
def crsb4gf1(nd31k9qm):
 return 1+0.03*nd31k9qm
def mctwjlsh(nd31k9qm):
 return 1+0.04*nd31k9qm
def ry181acj(nd31k9qm):
 return max(0.7,1-0.03*nd31k9qm)
def wa45hvgo(nd31k9qm):
 return nd31k9qm*2
def jxxgaear(nd31k9qm):
 return nd31k9qm*0.5
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
ocij2v2h=[int(100*1.3**(nd31k9qm-1))for nd31k9qm in range(1,61)]
