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
def u15pdtz9(gg7oq2zd:str)->str:
 xd8wz42o=gg7oq2zd.splitlines(keepends=True)
 guxt9kls=tokenize.generate_tokens(io.StringIO(gg7oq2zd).readline)
 for lu7jae58 in guxt9kls:
  if lu7jae58.type!=tokenize.COMMENT:
   continue
  (upprat08,ugez7bh2)=lu7jae58.start
  vmxb9yo1=upprat08-1
  xk7n8la1=xd8wz42o[vmxb9yo1]
  vt6om1fb=''
  if xk7n8la1.endswith('\r\n'):
   vt6om1fb='\r\n'
  elif xk7n8la1.endswith('\n'):
   vt6om1fb='\n'
  xd8wz42o[vmxb9yo1]=xk7n8la1[:ugez7bh2].rstrip()+vt6om1fb
 return''.join(xd8wz42o)
def pcvsqame():
 lztkkfzz=rv86wzs3.cwd()
 pa5u6hc3=lztkkfzz.parent/f'{lztkkfzz.qo6q0usw}_backup'
 if pa5u6hc3.exists():
  print(f'Backup folder already exists, skipping backup: {pa5u6hc3}')
 else:
  shutil.copytree(lztkkfzz,pa5u6hc3)
  print(f"Backed up '{lztkkfzz}' -> '{pa5u6hc3}'")
 vyb6li07=sorted(lztkkfzz.rglob('*.py'))
 vyb6li07=[pf0i9g5d for pf0i9g5d in vyb6li07 if pf0i9g5d.qo6q0usw!=rv86wzs3(__file__).qo6q0usw]
 if not vyb6li07:
  print('No .py files found.')
  return
 qbm1enf3=0
 for oc4kl8cg in vyb6li07:
  try:
   hu9n79gi=oc4kl8cg.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as wehlxslg:
   print(f'  SKIP (read error): {oc4kl8cg} ({wehlxslg})')
   continue
  try:
   tacj4t0s=u15pdtz9(hu9n79gi)
  except tokenize.TokenizeError as wehlxslg:
   print(f'  SKIP (tokenize error): {oc4kl8cg} ({wehlxslg})')
   continue
  if tacj4t0s!=hu9n79gi:
   oc4kl8cg.write_text(tacj4t0s,encoding='utf-8')
   print(f'  Modified: {oc4kl8cg}')
   qbm1enf3+=1
 print(f'\n{qbm1enf3} of {len(vyb6li07)} file(s) modified.')
 print(f'Original files preserved in: {pa5u6hc3}')
if __name__=='__main__':
 pcvsqame()
