import os
import pygame
dnq4fmyz=os.path.dirname(os.path.abspath(__file__))
def j1i2hgj1(zflse45b):
 return os.path.join(dnq4fmyz,zflse45b)
(jdiuovw1,rla5ju9b)=(800,600)
(xd1wjcit,mqp49kwv)=(2000,2000)
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
iq5c34dx={'ehet25':(255,0,0),'jayeqa':(255,102,102),'rsuudq':(139,0,0),'yixva1':(0,255,0),'jgm32w':(144,238,144),'xj8qo0':(0,100,0),'vrwvbh':(0,0,255),'wx5ggo':(0,255,255),'msz6rv':(0,0,128),'xj2dg1':(135,206,235),'gkok3q':(255,255,0),'t0fzau':(255,255,224),'h7kr0a':(128,128,0),'vmwi9s':(255,165,0),'ob3hn1':(255,200,124),'hhl173':(255,140,0),'huplvq':(128,0,128),'xutxzb':(238,130,238),'kcubod':(75,0,130),'xn8wwi':(255,192,203),'ceb875':(255,182,193),'tudp2f':(255,105,180),'l2cwt0':(139,69,19),'cjpyue':(181,101,29),'r9ln1p':(92,46,13),'ym5p7e':(128,128,128),'npmlva':(211,211,211),'xlitnt':(64,64,64),'o5rlqi':(0,128,128),'g0ht1t':(102,178,178),'eenui3':(0,77,77),'vsjchz':(255,0,255),'zcjn99':(218,112,214),'jvs9kk':(139,0,139),'txb3n2':(255,215,0),'n8k03w':(192,192,192),'ibxanj':(128,0,0),'m1v3zo':(64,224,208),'yf77lu':(250,128,114),'xu01uy':(255,127,80),'ddxb7g':(245,245,220),'qpz1rh':(255,255,240),'mxhw0i':(240,230,140),'bhrdu4':(0,0,0),'dq3b9s':(255,255,255)}
gyljexq7=['yixva1','wx5ggo','vrwvbh','huplvq','vsjchz','vmwi9s','ehet25','rsuudq','ym5p7e','txb3n2']
def rrcbpljd(w4rcb1kj):
 return{'k7rrbe':100*1.3**(w4rcb1kj-1),'rpeqyd':min(hyihair4*0.75,1.3*1.13**(w4rcb1kj-1)),'nk7y6q':10*1.25**(w4rcb1kj-1),'m314cq':5*1.2**(w4rcb1kj-1),'uq0e27':max(10,60*0.9**(w4rcb1kj-1)),'kk2y77':26*1.27**(w4rcb1kj-1)}
s0clbr7t={'mbslul':{'wurvqt':1,'jl1qwe':'yixva1','p6fmr5':(1.0,1.0,1.0,1.0,1.0,1.0)},'amyrsv':{'wurvqt':2,'jl1qwe':'wx5ggo','p6fmr5':(0.6,1.8,0.7,0.8,0.8,1.0),'iwu3bf':True,'txzuu8':150,'xu7dkn':2.5,'k7bpgy':20,'umfbuv':90},'xyhhg8':{'wurvqt':3,'jl1qwe':'ym5p7e','p6fmr5':(2.6,0.45,0.6,1.6,1.3,1.3),'x429om':True,'r3hxyj':60,'kou83g':1,'clslay':30},'eq3tq1':{'wurvqt':4,'jl1qwe':'huplvq','p6fmr5':(0.7,0.7,1.3,0.7,1.4,1.2),'o6d10a':True,'da7yvd':260,'v9hbn5':7},'jchsdi':{'wurvqt':5,'jl1qwe':'vmwi9s','p6fmr5':(1.6,0.85,1.6,1.1,1.1,1.4),'fkmuso':True,'mviifr':40,'w2lx2t':2.0},'vrtwlx':{'wurvqt':6,'jl1qwe':'vsjchz','p6fmr5':(0.55,2.1,1.5,0.6,0.7,1.3),'v3c71u':True,'i6ozx2':10,'c37qqy':120,'w1q8f6':150,'yl6lgj':25},'wc7hr6':{'wurvqt':7,'jl1qwe':'ehet25','p6fmr5':(0.8,1.1,1.0,0.8,1.0,1.3),'kjuw7w':True,'pswrgv':70},'xel501':{'wurvqt':8,'jl1qwe':'rsuudq','p6fmr5':(1.8,0.75,0.9,2.4,1.2,1.5),'w2zeeq':True,'wtolaq':120,'w65dlx':0.5},'hb1ajo':{'wurvqt':9,'jl1qwe':'txb3n2','p6fmr5':(0.35,1.5,0.5,0.5,0.6,0.8),'tudttj':3},'cuuhcl':{'wurvqt':10,'jl1qwe':'jvs9kk','p6fmr5':(2.2,1.1,1.8,1.6,0.9,2.0)}}
k1wj0tpa={j1ldqnk2:{'k7rrbe':int(rrcbpljd(u23y30ys['wurvqt'])['k7rrbe']*u23y30ys['p6fmr5'][0]),'rpeqyd':round(rrcbpljd(u23y30ys['wurvqt'])['rpeqyd']*u23y30ys['p6fmr5'][1],2),'nk7y6q':int(rrcbpljd(u23y30ys['wurvqt'])['nk7y6q']*u23y30ys['p6fmr5'][2]),'m314cq':int(rrcbpljd(u23y30ys['wurvqt'])['m314cq']*u23y30ys['p6fmr5'][3]),'uq0e27':max(10,int(rrcbpljd(u23y30ys['wurvqt'])['uq0e27']*u23y30ys['p6fmr5'][4])),'kk2y77':int(rrcbpljd(u23y30ys['wurvqt'])['kk2y77']*u23y30ys['p6fmr5'][5]),'jl1qwe':iq5c34dx[u23y30ys['jl1qwe']],'wurvqt':u23y30ys['wurvqt'],'o6d10a':u23y30ys.get('o6d10a',False),'da7yvd':u23y30ys.get('da7yvd'),'v9hbn5':u23y30ys.get('v9hbn5'),'kjuw7w':u23y30ys.get('kjuw7w',False),'pswrgv':u23y30ys.get('pswrgv'),'tudttj':u23y30ys.get('tudttj'),'iwu3bf':u23y30ys.get('iwu3bf',False),'txzuu8':u23y30ys.get('txzuu8'),'xu7dkn':u23y30ys.get('xu7dkn'),'k7bpgy':u23y30ys.get('k7bpgy'),'umfbuv':u23y30ys.get('umfbuv'),'x429om':u23y30ys.get('x429om',False),'r3hxyj':u23y30ys.get('r3hxyj'),'kou83g':u23y30ys.get('kou83g'),'clslay':u23y30ys.get('clslay'),'v3c71u':u23y30ys.get('v3c71u',False),'i6ozx2':u23y30ys.get('i6ozx2'),'c37qqy':u23y30ys.get('c37qqy'),'w1q8f6':u23y30ys.get('w1q8f6'),'yl6lgj':u23y30ys.get('yl6lgj'),'fkmuso':u23y30ys.get('fkmuso',False),'mviifr':u23y30ys.get('mviifr'),'w2lx2t':u23y30ys.get('w2lx2t'),'w2zeeq':u23y30ys.get('w2zeeq',False),'wtolaq':u23y30ys.get('wtolaq'),'w65dlx':u23y30ys.get('w65dlx')}for(j1ldqnk2,u23y30ys)in s0clbr7t.items()}
c8yfbntp=sorted(k1wj0tpa,key=lambda j1ldqnk2:k1wj0tpa[j1ldqnk2]['wurvqt'])
uqjiujv6={'cgsq7a':{'rpeqyd':10,'pqpva5':10,'k1yjfe':6,'r4uov5':60,'j1f537':0,'w2ugl6':None,'jl1qwe':iq5c34dx['dq3b9s'],'n7csuy':j1i2hgj1('assets/normal.png'),'e56waf':20,'ew6tm2':15},'cqxm06':{'rpeqyd':5,'pqpva5':8,'k1yjfe':8,'r4uov5':90,'j1f537':999,'w2ugl6':'flyback','wkgeq2':250,'jl1qwe':iq5c34dx['vmwi9s'],'n7csuy':j1i2hgj1('assets/boomerang.png'),'e56waf':20,'ew6tm2':27},'whb0oq':{'rpeqyd':6,'pqpva5':6,'k1yjfe':5,'r4uov5':100,'j1f537':0,'w2ugl6':'homing','cm3v2p':0.08,'jl1qwe':iq5c34dx['vsjchz'],'n7csuy':j1i2hgj1('assets/homing.png'),'e56waf':20,'ew6tm2':20},'r8imoe':{'rpeqyd':14,'pqpva5':12,'k1yjfe':4,'r4uov5':50,'j1f537':3,'w2ugl6':'j1f537','jl1qwe':iq5c34dx['wx5ggo'],'n7csuy':j1i2hgj1('assets/pierce.png'),'e56waf':20,'ew6tm2':7},'pg3yu6':{'rpeqyd':7,'pqpva5':15,'k1yjfe':10,'r4uov5':70,'j1f537':0,'w2ugl6':'explode','pswrgv':60,'jl1qwe':iq5c34dx['ehet25'],'n7csuy':j1i2hgj1('assets/explosive.png'),'e56waf':20,'ew6tm2':20},'wxgnrf':{'rpeqyd':9,'pqpva5':7,'k1yjfe':5,'r4uov5':60,'j1f537':0,'w2ugl6':'split','bdoz6w':3,'jl1qwe':iq5c34dx['txb3n2'],'n7csuy':j1i2hgj1('assets/split.png'),'e56waf':20,'ew6tm2':9},'hlc83g':{'rpeqyd':7,'pqpva5':12,'k1yjfe':6,'r4uov5':90,'j1f537':0,'w2ugl6':None,'jl1qwe':iq5c34dx['huplvq']}}
uyhl1c32={'cgsq7a':'Normal Shot','cqxm06':'Boomerang','whb0oq':'Homing Shot','r8imoe':'Piercing Shot','pg3yu6':'Explosive Shot','wxgnrf':'Split Shot'}
mjh75lxo={'cgsq7a':15,'cqxm06':25,'whb0oq':20,'r8imoe':18,'pg3yu6':35,'wxgnrf':25}
bl6246hi=[(255,255,180),(255,255,0),(255,200,0),(255,140,0),(255,80,0),(220,30,0),(160,0,0)]
pecruyf3=5
def ra9kepad(w4rcb1kj):
 return 1+(w4rcb1kj-1)*0.12
def jdqqzrlf(w4rcb1kj):
 return max(0.65,1-(w4rcb1kj-1)*0.07)
cq5uznof={'vmdk5n':{'rthy25':'Vitality','dzjssz':'+20% Max Health','yl4zjd':8},'twvwvi':{'rthy25':'Swift Boots','dzjssz':'+8% Move Speed','yl4zjd':5},'jy66p6':{'rthy25':'Regeneration','dzjssz':'+1 HP/sec','yl4zjd':6},'kxtv76':{'rthy25':'Power','dzjssz':'+6% Weapon Damage','yl4zjd':8},'mgsiwg':{'rthy25':'Haste','dzjssz':'-5% Attack Cooldown','yl4zjd':6},'qnga41':{'rthy25':'Armor','dzjssz':'+5 Defense','yl4zjd':6},'m9bn18':{'rthy25':'Wisdom','dzjssz':'+15% XP Gain','yl4zjd':5}}
ibps3y70={'START_HEALTH':{'fnn16u':'og8cd3','rthy25':'Heart Crystal','dzjssz':'+8% Starting Max Health','yl4zjd':10,'ldz09w':15,'pta5iv':1.35},'START_REGEN':{'fnn16u':'og8cd3','rthy25':'Regen Charm','dzjssz':'+0.5 Starting HP/sec','yl4zjd':6,'ldz09w':25,'pta5iv':1.4},'START_DAMAGE':{'fnn16u':'e8a1ar','rthy25':'Sharp Edge','dzjssz':'+4% Starting Damage','yl4zjd':10,'ldz09w':20,'pta5iv':1.35},'START_COOLDOWN':{'fnn16u':'e8a1ar','rthy25':'Quick Hands','dzjssz':'-3% Starting Cooldown','yl4zjd':8,'ldz09w':25,'pta5iv':1.4},'START_SPEED':{'fnn16u':'l226pa','rthy25':'Wind Charm','dzjssz':'+3% Starting Speed','yl4zjd':8,'ldz09w':18,'pta5iv':1.35},'START_ARMOR':{'fnn16u':'l226pa','rthy25':'Iron Skin','dzjssz':'+2 Starting Armor','yl4zjd':10,'ldz09w':15,'pta5iv':1.3}}
vxvg0fn9={key:pygame.transform.scale(pygame.image.load(u23y30ys['n7csuy']),(u23y30ys['e56waf'],u23y30ys['ew6tm2']))for(key,u23y30ys)in uqjiujv6.items()if'n7csuy'in u23y30ys}
def b78okz1p(w4rcb1kj):
 return 1+0.08*w4rcb1kj
def jxxgaear(w4rcb1kj):
 return 1+0.03*w4rcb1kj
def q5amln4p(w4rcb1kj):
 return 1+0.04*w4rcb1kj
def wa45hvgo(w4rcb1kj):
 return max(0.7,1-0.03*w4rcb1kj)
def avfmh07w(w4rcb1kj):
 return w4rcb1kj*2
def mctwjlsh(w4rcb1kj):
 return w4rcb1kj*0.5
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
faqvkizz=[int(100*1.3**(w4rcb1kj-1))for w4rcb1kj in range(1,61)]
