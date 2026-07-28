import pygame
import math
from z1yhxso7 import*
from.pxq7bzeg import f935a0l7,l55nf4zw
from.dr2h2p39 import d1hm38ks,rzewviyt
class qxaprpn6(f935a0l7):
 def wzlm72je(self,ukshy8nb,dzsedfqs,nd6357oo):
  jslulzfy=self.wgcl9lcq.jslulzfy-dzsedfqs
  zpfb3hn1=self.wgcl9lcq.zpfb3hn1-nd6357oo
  hfb85p86=self.wgcl9lcq.centerx-dzsedfqs
  k7zgf9q5=self.wgcl9lcq.centery-nd6357oo
  ukshy8nb.blit(l55nf4zw,(hfb85p86-l55nf4zw.get_width()//2,zpfb3hn1+self.wgcl9lcq.height-6))
  aqclpoxk=self.wgcl9lcq.width//2
  for(wydmt8vt,m3pt5r5r)in((-6,4),(6,4),(0,-6)):
   (tk0qtl3q,gn89qkns)=(hfb85p86+wydmt8vt-aqclpoxk//2,k7zgf9q5+m3pt5r5r-aqclpoxk//2)
   divsolml=pygame.Rect(tk0qtl3q,gn89qkns,aqclpoxk,aqclpoxk)
   pygame.draw.rect(ukshy8nb,d1hm38ks(self.izhwy9he,0.6),divsolml,border_radius=4)
   cp91i3vm=divsolml.inflate(-3,-3)
   pygame.draw.rect(ukshy8nb,self.izhwy9he,cp91i3vm,border_radius=3)
   pygame.draw.rect(ukshy8nb,(15,15,15),divsolml,width=1,border_radius=4)
  cqheyto5=self.u9el8hl8/self.nii6l3ue
  rzewviyt(ukshy8nb,jslulzfy,zpfb3hn1-8,self.wgcl9lcq.width,cqheyto5,height=4)
 def pf0i9g5d(self,player,aicvqy5i,yjluujmi):
  n64fgwje=k1wj0tpa[self.type]
  oqse3tv1=n64fgwje['pgsb98']
  for sdeekgys in range(oqse3tv1):
   sne6loh2=2*math.pi/oqse3tv1*sdeekgys
   wydmt8vt=self.wgcl9lcq.centerx+math.cos(sne6loh2)*20
   m3pt5r5r=self.wgcl9lcq.centery+math.sin(sne6loh2)*20
   jm25len6=f935a0l7(self.type,wydmt8vt-zxa3kx7e//2,m3pt5r5r-zxa3kx7e//2)
   jm25len6.u9el8hl8=max(1,int(jm25len6.nii6l3ue*0.4))
   jm25len6.nii6l3ue=jm25len6.u9el8hl8
   yjluujmi.append(jm25len6)
