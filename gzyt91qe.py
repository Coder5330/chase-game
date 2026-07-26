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
def nbwye6qv(npejzhya:str)->str:
 ncyh3fvl=[]
 xxkdq95g=tokenize.generate_tokens(io.StringIO(npejzhya).readline)
 for(k7vcneas,nv23gxj0,xu9ymszd,do2m71hs,vpbwhvnz)in xxkdq95g:
  if k7vcneas==tokenize.COMMENT:
   continue
  ncyh3fvl.append((k7vcneas,nv23gxj0))
 return tokenize.untokenize(ncyh3fvl)
def ftrflqbm():
 i20cv3tl=qqu7eeqt.cwd()
 j1i2hgj1=i20cv3tl.parent/f'{i20cv3tl.q5amln4p}_backup'
 if j1i2hgj1.exists():
  print(f'Backup folder already exists, skipping backup: {j1i2hgj1}')
 else:
  shutil.copytree(i20cv3tl,j1i2hgj1)
  print(f"Backed up '{i20cv3tl}' -> '{j1i2hgj1}'")
 y8bv78hu=sorted(i20cv3tl.rglob('*.py'))
 y8bv78hu=[mnwxuj3a for mnwxuj3a in y8bv78hu if mnwxuj3a.q5amln4p!=qqu7eeqt(__file__).q5amln4p]
 if not y8bv78hu:
  print('No .py files found.')
  return
 z0b6ugvs=0
 for jr5rdnpx in y8bv78hu:
  try:
   a8ax40dt=jr5rdnpx.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as pv4ykade:
   print(f'  SKIP (read error): {jr5rdnpx} ({pv4ykade})')
   continue
  try:
   qbm1enf3=nbwye6qv(a8ax40dt)
  except tokenize.TokenizeError as pv4ykade:
   print(f'  SKIP (tokenize error): {jr5rdnpx} ({pv4ykade})')
   continue
  if qbm1enf3!=a8ax40dt:
   jr5rdnpx.write_text(qbm1enf3,encoding='utf-8')
   print(f'  Modified: {jr5rdnpx}')
   z0b6ugvs+=1
 print(f'\n{z0b6ugvs} of {len(y8bv78hu)} file(s) modified.')
 print(f'Original files preserved in: {j1i2hgj1}')
if __name__=='__main__':
 ftrflqbm()
