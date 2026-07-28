import pygame
from zfiblejg import*
from ok38p6fv import*
from wczh9ier import*
from fwftggz6 import mcup8ijl,iaq7b7v1,jyjhu8my,n2vlpys2
from vtempxkc import rk43safy
from cg5dog8c import kz1uu7zy
pygame.init()
uwxrum2l=pygame.display.set_mode((ygspk9p3,tp0lvsnu))
u1jhuwb6=pygame.time.Clock()
def gj29yfc2():
 title_font=pygame.font.SysFont('arial',40,bold=True)
 cp91i3vm=pygame.font.SysFont('arial',16)
 jm25len6=pygame.font.SysFont('arial',22,bold=True)
 hdw6lqwl=pygame.font.SysFont('arial',15)
 xp8mgyn2=[]
 for bokzixza in range(1,n2vlpys2+1):
  d0qzfhom=jyjhu8my(bokzixza)
  if d0qzfhom:
   subtitle=f"Level {d0qzfhom['high_level']}  |  {d0qzfhom['resources']} resources  |  {d0qzfhom['runs_played']} runs"
  else:
   subtitle='Empty - New Game'
  tacj4t0s=hc58drc1(ygspk9p3//2-170,170+(bokzixza-1)*110,340,90,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,jm25len6,f'Slot {bokzixza}',12,subtitle=subtitle,sub_font=hdw6lqwl,kind='slot',key=bokzixza)
  xp8mgyn2.append(tacj4t0s)
 while True:
  mqxlm5q2=pygame.event.get()
  for yrivh6t1 in mqxlm5q2:
   if yrivh6t1.type==pygame.QUIT:
    return None
  for tacj4t0s in xp8mgyn2:
   tacj4t0s.update(mqxlm5q2)
   if tacj4t0s.vw6m7b5c:
    return tacj4t0s.key
  uwxrum2l.fill(iq5c34dx['eqkwqh'])
  it04chsd=title_font.render('CHASE GAME',True,(20,20,40))
  uwxrum2l.blit(it04chsd,(ygspk9p3//2-it04chsd.get_width()//2,70))
  nd31k9qm=cp91i3vm.render('Choose a save slot',True,(30,30,30))
  uwxrum2l.blit(nd31k9qm,(ygspk9p3//2-nd31k9qm.get_width()//2,135))
  for tacj4t0s in xp8mgyn2:
   tacj4t0s.dw7nh8rq(uwxrum2l)
  pygame.display.flip()
  u1jhuwb6.tick(pi3qk2ia)
def vk3g84ut():
 v24479qt=gj29yfc2()
 if v24479qt is None:
  return
 f80ebkjf=mcup8ijl(v24479qt)
 def stv18kgy(fo75rh8l):
  iaq7b7v1(v24479qt,fo75rh8l)
 stv18kgy(f80ebkjf)
 while True:
  am2vajep=rk43safy(uwxrum2l,u1jhuwb6,f80ebkjf,stv18kgy)
  if am2vajep=='quit':
   break
  if am2vajep=='start_game':
   (jqzpniqf,fd6rupw2,ck7n3bfh)=kz1uu7zy(f80ebkjf,uwxrum2l,u1jhuwb6)
   f80ebkjf['resources']+=jqzpniqf
   f80ebkjf['high_level']=max(f80ebkjf.get('high_level',0),fd6rupw2)
   f80ebkjf['runs_played']=f80ebkjf.get('runs_played',0)+1
   stv18kgy(f80ebkjf)
   if ck7n3bfh:
    break
if __name__=='__main__':
 vk3g84ut()
