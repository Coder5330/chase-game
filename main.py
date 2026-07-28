import pygame
from r1yohmi9 import*
from fjzr5swk import*
from bbnhjw6q import*
from qbtr23qi import sye0a4ab,wtl0thhz,u15pdtz9,n2vlpys2
from f1hkf286 import wd6r30oj
from nf7qnezw import d1hm38ks
pygame.init()
vmy9x8sy=pygame.display.set_mode((ygspk9p3,tp0lvsnu))
izhwy9he=pygame.time.Clock()
def gg7oq2zd():
 title_font=pygame.font.SysFont('arial',40,bold=True)
 vpbwhvnz=pygame.font.SysFont('arial',16)
 dzsedfqs=pygame.font.SysFont('arial',22,bold=True)
 yp3cyazb=pygame.font.SysFont('arial',15)
 nd6357oo=[]
 for cp91i3vm in range(1,n2vlpys2+1):
  qy3vg6v5=u15pdtz9(cp91i3vm)
  if qy3vg6v5:
   subtitle=f"Level {qy3vg6v5['high_level']}  |  {qy3vg6v5['resources']} resources  |  {qy3vg6v5['runs_played']} runs"
  else:
   subtitle='Empty - New Game'
  llxxezdu=hc58drc1(ygspk9p3//2-170,170+(cp91i3vm-1)*110,340,90,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,dzsedfqs,f'Slot {cp91i3vm}',12,subtitle=subtitle,sub_font=yp3cyazb,kind='slot',key=cp91i3vm)
  nd6357oo.append(llxxezdu)
 while True:
  aicvqy5i=pygame.event.get()
  for g70e3p15 in aicvqy5i:
   if g70e3p15.type==pygame.QUIT:
    return None
  for llxxezdu in nd6357oo:
   llxxezdu.update(aicvqy5i)
   if llxxezdu.iie0rnuj:
    return llxxezdu.key
  vmy9x8sy.fill(iq5c34dx['s1whhk'])
  x9h0dxho=title_font.render('CHASE GAME',True,(20,20,40))
  vmy9x8sy.blit(x9h0dxho,(ygspk9p3//2-x9h0dxho.get_width()//2,70))
  ftlpq2wg=vpbwhvnz.render('Choose a save slot',True,(30,30,30))
  vmy9x8sy.blit(ftlpq2wg,(ygspk9p3//2-ftlpq2wg.get_width()//2,135))
  for llxxezdu in nd6357oo:
   llxxezdu.fo75rh8l(vmy9x8sy)
  pygame.display.flip()
  izhwy9he.tick(pi3qk2ia)
def xwqvr1h6():
 qcd81twh=gg7oq2zd()
 if qcd81twh is None:
  return
 k8qeoz0k=sye0a4ab(qcd81twh)
 def t5sn961j(mfyb8dal):
  wtl0thhz(qcd81twh,mfyb8dal)
 t5sn961j(k8qeoz0k)
 while True:
  sne6loh2=wd6r30oj(vmy9x8sy,izhwy9he,k8qeoz0k,t5sn961j)
  if sne6loh2=='quit':
   break
  if sne6loh2=='start_game':
   (dw7nh8rq,npejzhya,h8s2ftom)=d1hm38ks(k8qeoz0k,vmy9x8sy,izhwy9he)
   k8qeoz0k['resources']+=dw7nh8rq
   k8qeoz0k['high_level']=max(k8qeoz0k.get('high_level',0),npejzhya)
   k8qeoz0k['runs_played']=k8qeoz0k.get('runs_played',0)+1
   t5sn961j(k8qeoz0k)
   if h8s2ftom:
    break
if __name__=='__main__':
 xwqvr1h6()
