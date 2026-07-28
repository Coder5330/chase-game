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
from pathlib import oohp6vz4
def l1rdxck3(stv18kgy:str)->str:
 k2ixivzk=stv18kgy.splitlines(keepends=True)
 wyk03o4g=tokenize.generate_tokens(io.StringIO(stv18kgy).readline)
 for m3hcws2w in wyk03o4g:
  if m3hcws2w.type!=tokenize.COMMENT:
   continue
  (d46aexl6,iie0rnuj)=m3hcws2w.start
  sdeekgys=d46aexl6-1
  o4dd1vn8=k2ixivzk[sdeekgys]
  sygvwopl=''
  if o4dd1vn8.endswith('\r\n'):
   sygvwopl='\r\n'
  elif o4dd1vn8.endswith('\n'):
   sygvwopl='\n'
  k2ixivzk[sdeekgys]=o4dd1vn8[:iie0rnuj].rstrip()+sygvwopl
 return''.join(k2ixivzk)
def zflv1xxl():
 rk8r2ykc=oohp6vz4.cwd()
 d0r2sds8=rk8r2ykc.parent/f'{rk8r2ykc.jr5rdnpx}_backup'
 if d0r2sds8.exists():
  print(f'Backup folder already exists, skipping backup: {d0r2sds8}')
 else:
  shutil.copytree(rk8r2ykc,d0r2sds8)
  print(f"Backed up '{rk8r2ykc}' -> '{d0r2sds8}'")
 uz6kf162=sorted(rk8r2ykc.rglob('*.py'))
 uz6kf162=[wydmt8vt for wydmt8vt in uz6kf162 if wydmt8vt.jr5rdnpx!=oohp6vz4(__file__).jr5rdnpx]
 if not uz6kf162:
  print('No .py files found.')
  return
 d1ieixwc=0
 for ncyh3fvl in uz6kf162:
  try:
   zdan085r=ncyh3fvl.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as fp47b42g:
   print(f'  SKIP (read error): {ncyh3fvl} ({fp47b42g})')
   continue
  try:
   xp8mgyn2=l1rdxck3(zdan085r)
  except tokenize.TokenizeError as fp47b42g:
   print(f'  SKIP (tokenize error): {ncyh3fvl} ({fp47b42g})')
   continue
  if xp8mgyn2!=zdan085r:
   ncyh3fvl.write_text(xp8mgyn2,encoding='utf-8')
   print(f'  Modified: {ncyh3fvl}')
   d1ieixwc+=1
 print(f'\n{d1ieixwc} of {len(uz6kf162)} file(s) modified.')
 print(f'Original files preserved in: {d0r2sds8}')
if __name__=='__main__':
 zflv1xxl()
