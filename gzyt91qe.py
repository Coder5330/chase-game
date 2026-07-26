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
from pathlib import qqu7eeqt
def qertb74r(xwk2rv23:str)->str:
 gqj5sxvw=xwk2rv23.splitlines(keepends=True)
 k7vcneas=tokenize.generate_tokens(io.StringIO(xwk2rv23).readline)
 for nv23gxj0 in k7vcneas:
  if nv23gxj0.type!=tokenize.COMMENT:
   continue
  (zflse45b,li9nb74x)=nv23gxj0.start
  x9bp4m18=zflse45b-1
  gkz2u2tn=gqj5sxvw[x9bp4m18]
  do2m71hs=''
  if gkz2u2tn.endswith('\r\n'):
   do2m71hs='\r\n'
  elif gkz2u2tn.endswith('\n'):
   do2m71hs='\n'
  gqj5sxvw[x9bp4m18]=gkz2u2tn[:li9nb74x].rstrip()+do2m71hs
 return''.join(gqj5sxvw)
def w4rcb1kj():
 i20cv3tl=qqu7eeqt.cwd()
 j1i2hgj1=i20cv3tl.parent/f'{i20cv3tl.b78okz1p}_backup'
 if j1i2hgj1.exists():
  print(f'Backup folder already exists, skipping backup: {j1i2hgj1}')
 else:
  shutil.copytree(i20cv3tl,j1i2hgj1)
  print(f"Backed up '{i20cv3tl}' -> '{j1i2hgj1}'")
 wy0mahym=sorted(i20cv3tl.rglob('*.py'))
 wy0mahym=[ob7p0rnp for ob7p0rnp in wy0mahym if ob7p0rnp.b78okz1p!=qqu7eeqt(__file__).b78okz1p]
 if not wy0mahym:
  print('No .py files found.')
  return
 z0b6ugvs=0
 for r2muljav in wy0mahym:
  try:
   qo6q0usw=r2muljav.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as pv4ykade:
   print(f'  SKIP (read error): {r2muljav} ({pv4ykade})')
   continue
  try:
   qbm1enf3=qertb74r(qo6q0usw)
  except tokenize.TokenizeError as pv4ykade:
   print(f'  SKIP (tokenize error): {r2muljav} ({pv4ykade})')
   continue
  if qbm1enf3!=qo6q0usw:
   r2muljav.write_text(qbm1enf3,encoding='utf-8')
   print(f'  Modified: {r2muljav}')
   z0b6ugvs+=1
 print(f'\n{z0b6ugvs} of {len(wy0mahym)} file(s) modified.')
 print(f'Original files preserved in: {j1i2hgj1}')
if __name__=='__main__':
 w4rcb1kj()
