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
def ck7n3bfh(k8qeoz0k:str)->str:
 f55dmcxx=k8qeoz0k.splitlines(keepends=True)
 i7zcgdc5=tokenize.generate_tokens(io.StringIO(k8qeoz0k).readline)
 for l0sqg4ei in i7zcgdc5:
  if l0sqg4ei.type!=tokenize.COMMENT:
   continue
  (xasez2nx,i20cv3tl)=l0sqg4ei.start
  gsmdzqcb=xasez2nx-1
  fpa8hyex=f55dmcxx[gsmdzqcb]
  fo75rh8l=''
  if fpa8hyex.endswith('\r\n'):
   fo75rh8l='\r\n'
  elif fpa8hyex.endswith('\n'):
   fo75rh8l='\n'
  f55dmcxx[gsmdzqcb]=fpa8hyex[:i20cv3tl].rstrip()+fo75rh8l
 return''.join(f55dmcxx)
def o4dd1vn8():
 oqse3tv1=oohp6vz4.cwd()
 gp84dyt9=oqse3tv1.parent/f'{oqse3tv1.gqq4d3kz}_backup'
 if gp84dyt9.exists():
  print(f'Backup folder already exists, skipping backup: {gp84dyt9}')
 else:
  shutil.copytree(oqse3tv1,gp84dyt9)
  print(f"Backed up '{oqse3tv1}' -> '{gp84dyt9}'")
 g5hcbbmh=sorted(oqse3tv1.rglob('*.py'))
 g5hcbbmh=[oc4kl8cg for oc4kl8cg in g5hcbbmh if oc4kl8cg.gqq4d3kz!=oohp6vz4(__file__).gqq4d3kz]
 if not g5hcbbmh:
  print('No .py files found.')
  return
 f32ejx5t=0
 for mu4fmpkx in g5hcbbmh:
  try:
   wg25cfzf=mu4fmpkx.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as vt6om1fb:
   print(f'  SKIP (read error): {mu4fmpkx} ({vt6om1fb})')
   continue
  try:
   z9toqw9j=ck7n3bfh(wg25cfzf)
  except tokenize.TokenizeError as vt6om1fb:
   print(f'  SKIP (tokenize error): {mu4fmpkx} ({vt6om1fb})')
   continue
  if z9toqw9j!=wg25cfzf:
   mu4fmpkx.write_text(z9toqw9j,encoding='utf-8')
   print(f'  Modified: {mu4fmpkx}')
   f32ejx5t+=1
 print(f'\n{f32ejx5t} of {len(g5hcbbmh)} file(s) modified.')
 print(f'Original files preserved in: {gp84dyt9}')
if __name__=='__main__':
 o4dd1vn8()
