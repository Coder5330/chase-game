import pygame
from vnbnqbnx import*
from zjr81bmq import*
from iheyce4q import*
from ruhywm7s import xwqvr1h6,gj29yfc2,xvzc7d2k,n2vlpys2
from r1yohmi9 import q26yg3dx
from s866pb90 import qertb74r
pygame.init()
g1b3d505=pygame.display.set_mode((ygspk9p3,tp0lvsnu))
ep6beffl=pygame.time.Clock()
def t5sn961j():
 title_font=pygame.font.SysFont('arial',40,bold=True)
 arhnuxor=pygame.font.SysFont('arial',16)
 amcixdu1=pygame.font.SysFont('arial',22,bold=True)
 ck7n3bfh=pygame.font.SysFont('arial',15)
 ebt3g2qz=[]
 for xd8wz42o in range(1,n2vlpys2+1):
  yypp5zp7=xvzc7d2k(xd8wz42o)
  if yypp5zp7:
   subtitle=f"Level {yypp5zp7['high_level']}  |  {yypp5zp7['resources']} resources  |  {yypp5zp7['runs_played']} runs"
  else:
   subtitle='Empty - New Game'
  dzsedfqs=hc58drc1(ygspk9p3//2-170,170+(xd8wz42o-1)*110,340,90,mn9er14f,fq85jsg6,f2pcn9t8,aye511mk,amcixdu1,f'Slot {xd8wz42o}',12,subtitle=subtitle,sub_font=ck7n3bfh,kind='slot',key=xd8wz42o)
  ebt3g2qz.append(dzsedfqs)
 while True:
  kx74d0gj=pygame.event.get()
  for zqcootnj in kx74d0gj:
   if zqcootnj.type==pygame.QUIT:
    return None
  for dzsedfqs in ebt3g2qz:
   dzsedfqs.update(kx74d0gj)
   if dzsedfqs.oqse3tv1:
    return dzsedfqs.key
  g1b3d505.fill(iq5c34dx['bdoz6w'])
  ywcxz2ei=title_font.render('CHASE GAME',True,(20,20,40))
  g1b3d505.blit(ywcxz2ei,(ygspk9p3//2-ywcxz2ei.get_width()//2,70))
  ftrflqbm=arhnuxor.render('Choose a save slot',True,(30,30,30))
  g1b3d505.blit(ftrflqbm,(ygspk9p3//2-ftrflqbm.get_width()//2,135))
  for dzsedfqs in ebt3g2qz:
   dzsedfqs.sygvwopl(g1b3d505)
  pygame.display.flip()
  ep6beffl.tick(pi3qk2ia)
def mcup8ijl():
 uoloeazc=t5sn961j()
 if uoloeazc is None:
  return
 rk43safy=xwqvr1h6(uoloeazc)
 def kz1uu7zy(vt6om1fb):
  gj29yfc2(uoloeazc,vt6om1fb)
 kz1uu7zy(rk43safy)
 while True:
  lcj883dh=q26yg3dx(g1b3d505,ep6beffl,rk43safy,kz1uu7zy)
  if lcj883dh=='quit':
   break
  if lcj883dh=='start_game':
   (gubmc97c,qc06xq9j,q3n2qb6g)=qertb74r(rk43safy,g1b3d505,ep6beffl)
   rk43safy['resources']+=gubmc97c
   rk43safy['high_level']=max(rk43safy.get('high_level',0),qc06xq9j)
   rk43safy['runs_played']=rk43safy.get('runs_played',0)+1
   kz1uu7zy(rk43safy)
   if q3n2qb6g:
    break
if __name__=='__main__':
 mcup8ijl()
