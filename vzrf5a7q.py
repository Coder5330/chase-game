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
from pathlib import rv86wzs3
def uwxrum2l(cq2q4qer:str)->str:
 rktlzkj4=cq2q4qer.splitlines(keepends=True)
 s5r96khu=tokenize.generate_tokens(io.StringIO(cq2q4qer).readline)
 for a1tbrwr9 in s5r96khu:
  if a1tbrwr9.type!=tokenize.COMMENT:
   continue
  (v6xii5p5,amcixdu1)=a1tbrwr9.start
  mn7h9g1a=v6xii5p5-1
  wvpw232u=rktlzkj4[mn7h9g1a]
  rmm1zxyv=''
  if wvpw232u.endswith('\r\n'):
   rmm1zxyv='\r\n'
  elif wvpw232u.endswith('\n'):
   rmm1zxyv='\n'
  rktlzkj4[mn7h9g1a]=wvpw232u[:amcixdu1].rstrip()+rmm1zxyv
 return''.join(rktlzkj4)
def n3rlkte4():
 iie0rnuj=rv86wzs3.cwd()
 on0jnwny=iie0rnuj.parent/f'{iie0rnuj.j1ldqnk2}_backup'
 if on0jnwny.exists():
  print(f'Backup folder already exists, skipping backup: {on0jnwny}')
 else:
  shutil.copytree(iie0rnuj,on0jnwny)
  print(f"Backed up '{iie0rnuj}' -> '{on0jnwny}'")
 ee1g983e=sorted(iie0rnuj.rglob('*.py'))
 ee1g983e=[d448n7od for d448n7od in ee1g983e if d448n7od.j1ldqnk2!=rv86wzs3(__file__).j1ldqnk2]
 if not ee1g983e:
  print('No .py files found.')
  return
 uysal8m1=0
 for y8bv78hu in ee1g983e:
  try:
   jr5rdnpx=y8bv78hu.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as yuibrsz1:
   print(f'  SKIP (read error): {y8bv78hu} ({yuibrsz1})')
   continue
  try:
   li9nb74x=uwxrum2l(jr5rdnpx)
  except tokenize.TokenizeError as yuibrsz1:
   print(f'  SKIP (tokenize error): {y8bv78hu} ({yuibrsz1})')
   continue
  if li9nb74x!=jr5rdnpx:
   y8bv78hu.write_text(li9nb74x,encoding='utf-8')
   print(f'  Modified: {y8bv78hu}')
   uysal8m1+=1
 print(f'\n{uysal8m1} of {len(ee1g983e)} file(s) modified.')
 print(f'Original files preserved in: {on0jnwny}')
if __name__=='__main__':
 n3rlkte4()
