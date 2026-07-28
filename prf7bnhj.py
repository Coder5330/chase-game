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
def su1hbj6t(iaq7b7v1:str)->str:
 wa45hvgo=iaq7b7v1.splitlines(keepends=True)
 ra9kepad=tokenize.generate_tokens(io.StringIO(iaq7b7v1).readline)
 for jdqqzrlf in ra9kepad:
  if jdqqzrlf.type!=tokenize.COMMENT:
   continue
  (myrp5ge0,izhwy9he)=jdqqzrlf.start
  nvuprt77=myrp5ge0-1
  k2ixivzk=wa45hvgo[nvuprt77]
  mygfliji=''
  if k2ixivzk.endswith('\r\n'):
   mygfliji='\r\n'
  elif k2ixivzk.endswith('\n'):
   mygfliji='\n'
  wa45hvgo[nvuprt77]=k2ixivzk[:izhwy9he].rstrip()+mygfliji
 return''.join(wa45hvgo)
def n04cdpqv():
 bfoqmf5l=oohp6vz4.cwd()
 b06xkxb9=bfoqmf5l.parent/f'{bfoqmf5l.zsw2292m}_backup'
 if b06xkxb9.exists():
  print(f'Backup folder already exists, skipping backup: {b06xkxb9}')
 else:
  shutil.copytree(bfoqmf5l,b06xkxb9)
  print(f"Backed up '{bfoqmf5l}' -> '{b06xkxb9}'")
 no0u93mz=sorted(bfoqmf5l.rglob('*.py'))
 no0u93mz=[co4busu9 for co4busu9 in no0u93mz if co4busu9.zsw2292m!=oohp6vz4(__file__).zsw2292m]
 if not no0u93mz:
  print('No .py files found.')
  return
 pvasifpw=0
 for a2wspofv in no0u93mz:
  try:
   oc4kl8cg=a2wspofv.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as x875aud9:
   print(f'  SKIP (read error): {a2wspofv} ({x875aud9})')
   continue
  try:
   i20cv3tl=su1hbj6t(oc4kl8cg)
  except tokenize.TokenizeError as x875aud9:
   print(f'  SKIP (tokenize error): {a2wspofv} ({x875aud9})')
   continue
  if i20cv3tl!=oc4kl8cg:
   a2wspofv.write_text(i20cv3tl,encoding='utf-8')
   print(f'  Modified: {a2wspofv}')
   pvasifpw+=1
 print(f'\n{pvasifpw} of {len(no0u93mz)} file(s) modified.')
 print(f'Original files preserved in: {b06xkxb9}')
if __name__=='__main__':
 n04cdpqv()
