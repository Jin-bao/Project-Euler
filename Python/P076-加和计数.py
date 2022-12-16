# https://pe.metaquant.org/pe076.html
from functools import lru_cache

@lru_cache(maxsize=2048)
def partition(n, k):
  if n==1 or k==1:
    return 1
  elif n > k:
    return partition(n, k-1) + partition(n-k, k)
  else:
    return partition(n, n-1) + 1

print(partition(100, 99))