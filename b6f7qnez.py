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
from pathlib import yur7ko64
def p7b1ijiy(y9ayq6ww:str)->str:
 b78okz1p=y9ayq6ww.splitlines(keepends=True)
 x9h0dxho=tokenize.generate_tokens(io.StringIO(y9ayq6ww).readline)
 for i33e1i1p in x9h0dxho:
  if i33e1i1p.type!=tokenize.COMMENT:
   continue
  (xu9ymszd,lztkkfzz)=i33e1i1p.start
  arhnuxor=xu9ymszd-1
  ry181acj=b78okz1p[arhnuxor]
  velos6zl=''
  if ry181acj.endswith('\r\n'):
   velos6zl='\r\n'
  elif ry181acj.endswith('\n'):
   velos6zl='\n'
  b78okz1p[arhnuxor]=ry181acj[:lztkkfzz].rstrip()+velos6zl
 return''.join(b78okz1p)
def crsb4gf1():
 hfb85p86=yur7ko64.cwd()
 mpdzp6lf=hfb85p86.parent/f'{hfb85p86.hu9n79gi}_backup'
 if mpdzp6lf.exists():
  print(f'Backup folder already exists, skipping backup: {mpdzp6lf}')
 else:
  shutil.copytree(hfb85p86,mpdzp6lf)
  print(f"Backed up '{hfb85p86}' -> '{mpdzp6lf}'")
 ljk4q5v7=sorted(hfb85p86.rglob('*.py'))
 ljk4q5v7=[a2wspofv for a2wspofv in ljk4q5v7 if a2wspofv.hu9n79gi!=yur7ko64(__file__).hu9n79gi]
 if not ljk4q5v7:
  print('No .py files found.')
  return
 z9toqw9j=0
 for la3kkrzd in ljk4q5v7:
  try:
   mu4fmpkx=la3kkrzd.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as zefqjg02:
   print(f'  SKIP (read error): {la3kkrzd} ({zefqjg02})')
   continue
  try:
   x5m9j98c=p7b1ijiy(mu4fmpkx)
  except tokenize.TokenizeError as zefqjg02:
   print(f'  SKIP (tokenize error): {la3kkrzd} ({zefqjg02})')
   continue
  if x5m9j98c!=mu4fmpkx:
   la3kkrzd.write_text(x5m9j98c,encoding='utf-8')
   print(f'  Modified: {la3kkrzd}')
   z9toqw9j+=1
 print(f'\n{z9toqw9j} of {len(ljk4q5v7)} file(s) modified.')
 print(f'Original files preserved in: {mpdzp6lf}')
if __name__=='__main__':
 crsb4gf1()
