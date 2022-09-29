# 至少要是一个四位数，可以从 1111 开始搜寻
# 重复的数位只能是 3 或 3 的倍数
# 重复的数字只能是 0, 1, 2 三个数

from sympy import nextprime,isprime
from collections import Counter

def isReplacablePrime(num:int) -> bool:
  numStr = str(num)
  countNumStr = Counter(numStr)
  num,m = countNumStr.most_common(1)[0]
  if m%3==0 and num in set('012'):
    total = 1
    for newDig in range(int(num)+1,10):
      newNum = numStr.replace(num,str(newDig))
      if isprime(int(newNum)):
        total += 1
    if total == 8:
      return True
  return False

num = 1111
while True:
  prime = nextprime(num)
  if isReplacablePrime(prime):
    print(prime)
    exit(0)
  else:
    num = prime