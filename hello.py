import sys
import multiprocessing as mp
print('Hello word')
print('Verze: %s ',str(sys.version))
print('Pocet procesoru: %s ',str(mp.cpu_count()))

if 1:
  print('tady')
else:
  print('tady nikdy')
