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
def rwybow23(u1ni10kq:str)->str:
 zo3lqi7e=u1ni10kq.splitlines(keepends=True)
 hjkuuhcl=tokenize.generate_tokens(io.StringIO(u1ni10kq).readline)
 for s7fbmenu in hjkuuhcl:
  if s7fbmenu.type!=tokenize.COMMENT:
   continue
  (g1b3d505,hfb85p86)=s7fbmenu.k7vcneas
  pcvsqame=g1b3d505-1
  mcup8ijl=zo3lqi7e[pcvsqame]
  xuu13i59=''
  if mcup8ijl.endswith('\r\n'):
   xuu13i59='\r\n'
  elif mcup8ijl.endswith('\n'):
   xuu13i59='\n'
  zo3lqi7e[pcvsqame]=mcup8ijl[:hfb85p86].rstrip()+xuu13i59
 return''.join(zo3lqi7e)
def chx3d43e():
 eohswq40=r0tvhhpb.cwd()
 nrpj1epk=eohswq40.parent/f'{eohswq40.trdhw9re}_backup'
 if nrpj1epk.exists():
  print(f'Backup folder already exists, skipping backup: {nrpj1epk}')
 else:
  shutil.copytree(eohswq40,nrpj1epk)
  print(f"Backed up '{eohswq40}' -> '{nrpj1epk}'")
 tj0nmeoq=sorted(eohswq40.rglob('*.py'))
 tj0nmeoq=[no0u93mz for no0u93mz in tj0nmeoq if no0u93mz.trdhw9re!=r0tvhhpb(__file__).trdhw9re]
 if not tj0nmeoq:
  print('No .py files found.')
  return
 iie0rnuj=0
 for ljk4q5v7 in tj0nmeoq:
  try:
   l3swebnv=ljk4q5v7.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as le9oe941:
   print(f'  SKIP (read error): {ljk4q5v7} ({le9oe941})')
   continue
  try:
   wi8skch8=rwybow23(l3swebnv)
  except tokenize.TokenizeError as le9oe941:
   print(f'  SKIP (tokenize error): {ljk4q5v7} ({le9oe941})')
   continue
  if wi8skch8!=l3swebnv:
   ljk4q5v7.write_text(wi8skch8,encoding='utf-8')
   print(f'  Modified: {ljk4q5v7}')
   iie0rnuj+=1
 print(f'\n{iie0rnuj} of {len(tj0nmeoq)} file(s) modified.')
 print(f'Original files preserved in: {nrpj1epk}')
if __name__=='__main__':
 chx3d43e()
