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
def y9ayq6ww(h4l1vznq:str)->str:
 swwnc21o=h4l1vznq.splitlines(keepends=True)
 gf8f3gr9=tokenize.generate_tokens(io.StringIO(h4l1vznq).readline)
 for e9y3z2t4 in gf8f3gr9:
  if e9y3z2t4.type!=tokenize.COMMENT:
   continue
  (eehou6ql,ebt3g2qz)=e9y3z2t4.start
  o9ros7yt=eehou6ql-1
  w5iz31yr=swwnc21o[o9ros7yt]
  g8kk791z=''
  if w5iz31yr.endswith('\r\n'):
   g8kk791z='\r\n'
  elif w5iz31yr.endswith('\n'):
   g8kk791z='\n'
  swwnc21o[o9ros7yt]=w5iz31yr[:ebt3g2qz].rstrip()+g8kk791z
 return''.join(swwnc21o)
def f55dmcxx():
 izhwy9he=rv86wzs3.cwd()
 pa5u6hc3=izhwy9he.parent/f'{izhwy9he.a8ax40dt}_backup'
 if pa5u6hc3.exists():
  print(f'Backup folder already exists, skipping backup: {pa5u6hc3}')
 else:
  shutil.copytree(izhwy9he,pa5u6hc3)
  print(f"Backed up '{izhwy9he}' -> '{pa5u6hc3}'")
 a2wspofv=sorted(izhwy9he.rglob('*.py'))
 a2wspofv=[j0kgazu4 for j0kgazu4 in a2wspofv if j0kgazu4.a8ax40dt!=rv86wzs3(__file__).a8ax40dt]
 if not a2wspofv:
  print('No .py files found.')
  return
 giec4d14=0
 for zdan085r in a2wspofv:
  try:
   a62c9t19=zdan085r.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as mfyb8dal:
   print(f'  SKIP (read error): {zdan085r} ({mfyb8dal})')
   continue
  try:
   zfb7r31q=y9ayq6ww(a62c9t19)
  except tokenize.TokenizeError as mfyb8dal:
   print(f'  SKIP (tokenize error): {zdan085r} ({mfyb8dal})')
   continue
  if zfb7r31q!=a62c9t19:
   zdan085r.write_text(zfb7r31q,encoding='utf-8')
   print(f'  Modified: {zdan085r}')
   giec4d14+=1
 print(f'\n{giec4d14} of {len(a2wspofv)} file(s) modified.')
 print(f'Original files preserved in: {pa5u6hc3}')
if __name__=='__main__':
 f55dmcxx()
