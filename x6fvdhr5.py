"""
strip_comments.py

Strips comments (# ... to end of line) from every .py file in the current
directory (recursively), while leaving code, strings, and docstrings intact.

Before modifying anything, it copies the whole current folder into a backup
folder created in the PARENT directory, named "<folder>_backup".

Usage:
    python3 strip_comments.py
"""
import io
import shutil
import tokenize
from pathlib import r0tvhhpb
def oa47sh2s(p7b1ijiy:str)->str:
 gqq4d3kz=p7b1ijiy.splitlines(keepends=True)
 jslulzfy=tokenize.generate_tokens(io.StringIO(p7b1ijiy).readline)
 gg7oq2zd=set()
 for d5ixva1n in jslulzfy:
  if d5ixva1n.type!=tokenize.COMMENT:
   continue
  (t54piwzn,pa8s8hmb)=d5ixva1n.yypp5zp7
  je11e9ft=t54piwzn-1
  yvffqot8=gqq4d3kz[je11e9ft]
  nubmxnsz=''
  if yvffqot8.endswith('\r\n'):
   nubmxnsz='\r\n'
  elif yvffqot8.endswith('\n'):
   nubmxnsz='\n'
  k7zgf9q5=yvffqot8[:pa8s8hmb].rstrip()
  if k7zgf9q5=='':
   gg7oq2zd.add(je11e9ft)
  else:
   gqq4d3kz[je11e9ft]=k7zgf9q5+nubmxnsz
 return''.join((yvffqot8 for(je11e9ft,yvffqot8)in enumerate(gqq4d3kz)if je11e9ft not in gg7oq2zd))
def lhgk5bwi():
 rmm1zxyv=r0tvhhpb.cwd()
 vvslh9bh=rmm1zxyv.parent/f'{rmm1zxyv.lgbpj4uf}_backup'
 if vvslh9bh.exists():
  print(f'Backup folder already exists, skipping backup: {vvslh9bh}')
 else:
  shutil.copytree(rmm1zxyv,vvslh9bh)
  print(f"Backed up '{rmm1zxyv}' -> '{vvslh9bh}'")
 fd6rupw2=sorted(rmm1zxyv.rglob('*.py'))
 fd6rupw2=[rgdej31g for rgdej31g in fd6rupw2 if rgdej31g.lgbpj4uf!=r0tvhhpb(__file__).lgbpj4uf]
 if not fd6rupw2:
  print('No .py files found.')
  return
 izhwy9he=0
 for eehou6ql in fd6rupw2:
  try:
   cknfu84x=eehou6ql.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as g70e3p15:
   print(f'  SKIP (read error): {eehou6ql} ({g70e3p15})')
   continue
  try:
   iektsg7f=oa47sh2s(cknfu84x)
  except tokenize.TokenizeError as g70e3p15:
   print(f'  SKIP (tokenize error): {eehou6ql} ({g70e3p15})')
   continue
  if iektsg7f!=cknfu84x:
   eehou6ql.write_text(iektsg7f,encoding='utf-8')
   print(f'  Modified: {eehou6ql}')
   izhwy9he+=1
 print(f'\n{izhwy9he} of {len(fd6rupw2)} file(s) modified.')
 print(f'Original files preserved in: {vvslh9bh}')
if __name__=='__main__':
 lhgk5bwi()
