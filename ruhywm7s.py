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
def nabufwbu(uoloeazc:str)->str:
 d1b3jczu=uoloeazc.splitlines(keepends=True)
 rm0j36tc=tokenize.generate_tokens(io.StringIO(uoloeazc).readline)
 for ejbzutru in rm0j36tc:
  if ejbzutru.type!=tokenize.COMMENT:
   continue
  (ukshy8nb,wzs13c9x)=ejbzutru.su1hbj6t
  wvpw232u=ukshy8nb-1
  ls2zge2j=d1b3jczu[wvpw232u]
  b36htf4p=''
  if ls2zge2j.endswith('\r\n'):
   b36htf4p='\r\n'
  elif ls2zge2j.endswith('\n'):
   b36htf4p='\n'
  d1b3jczu[wvpw232u]=ls2zge2j[:wzs13c9x].rstrip()+b36htf4p
 return''.join(d1b3jczu)
def xwqvr1h6():
 pv4ykade=r0tvhhpb.cwd()
 nqimqodp=pv4ykade.parent/f'{pv4ykade.jl90pxrl}_backup'
 if nqimqodp.exists():
  print(f'Backup folder already exists, skipping backup: {nqimqodp}')
 else:
  shutil.copytree(pv4ykade,nqimqodp)
  print(f"Backed up '{pv4ykade}' -> '{nqimqodp}'")
 k1taa0i5=sorted(pv4ykade.rglob('*.py'))
 k1taa0i5=[gp6orsnc for gp6orsnc in k1taa0i5 if gp6orsnc.jl90pxrl!=r0tvhhpb(__file__).jl90pxrl]
 if not k1taa0i5:
  print('No .py files found.')
  return
 ugez7bh2=0
 for f8rtm4j3 in k1taa0i5:
  try:
   co4busu9=f8rtm4j3.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as velos6zl:
   print(f'  SKIP (read error): {f8rtm4j3} ({velos6zl})')
   continue
  try:
   vqnpcenl=nabufwbu(co4busu9)
  except tokenize.TokenizeError as velos6zl:
   print(f'  SKIP (tokenize error): {f8rtm4j3} ({velos6zl})')
   continue
  if vqnpcenl!=co4busu9:
   f8rtm4j3.write_text(vqnpcenl,encoding='utf-8')
   print(f'  Modified: {f8rtm4j3}')
   ugez7bh2+=1
 print(f'\n{ugez7bh2} of {len(k1taa0i5)} file(s) modified.')
 print(f'Original files preserved in: {nqimqodp}')
if __name__=='__main__':
 xwqvr1h6()
