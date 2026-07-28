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
def p7pchcbn(qdnai89y:str)->str:
 yvffqot8=qdnai89y.splitlines(keepends=True)
 x3n27m5p=tokenize.generate_tokens(io.StringIO(qdnai89y).readline)
 for pg3yu6vk in x3n27m5p:
  if pg3yu6vk.type!=tokenize.COMMENT:
   continue
  (xxns2zyb,k7zgf9q5)=pg3yu6vk.qy3vg6v5
  nyrid3dn=xxns2zyb-1
  zo3lqi7e=yvffqot8[nyrid3dn]
  qhkc856w=''
  if zo3lqi7e.endswith('\r\n'):
   qhkc856w='\r\n'
  elif zo3lqi7e.endswith('\n'):
   qhkc856w='\n'
  yvffqot8[nyrid3dn]=zo3lqi7e[:k7zgf9q5].rstrip()+qhkc856w
 return''.join(yvffqot8)
def ob7p0rnp():
 wehlxslg=r0tvhhpb.cwd()
 vvslh9bh=wehlxslg.parent/f'{wehlxslg.zorxdtg5}_backup'
 if vvslh9bh.exists():
  print(f'Backup folder already exists, skipping backup: {vvslh9bh}')
 else:
  shutil.copytree(wehlxslg,vvslh9bh)
  print(f"Backed up '{wehlxslg}' -> '{vvslh9bh}'")
 myrp5ge0=sorted(wehlxslg.rglob('*.py'))
 myrp5ge0=[vt26ys44 for vt26ys44 in myrp5ge0 if vt26ys44.zorxdtg5!=r0tvhhpb(__file__).zorxdtg5]
 if not myrp5ge0:
  print('No .py files found.')
  return
 izhwy9he=0
 for cqheyto5 in myrp5ge0:
  try:
   f8rtm4j3=cqheyto5.read_text(encoding='utf-8')
  except(UnicodeDecodeError,OSError)as jqzpniqf:
   print(f'  SKIP (read error): {cqheyto5} ({jqzpniqf})')
   continue
  try:
   iektsg7f=p7pchcbn(f8rtm4j3)
  except tokenize.TokenizeError as jqzpniqf:
   print(f'  SKIP (tokenize error): {cqheyto5} ({jqzpniqf})')
   continue
  if iektsg7f!=f8rtm4j3:
   cqheyto5.write_text(iektsg7f,encoding='utf-8')
   print(f'  Modified: {cqheyto5}')
   izhwy9he+=1
 print(f'\n{izhwy9he} of {len(myrp5ge0)} file(s) modified.')
 print(f'Original files preserved in: {vvslh9bh}')
if __name__=='__main__':
 ob7p0rnp()
