# phi(n) = n*prod(p|n, 1-1/p)
# p 是 n 的质因数
# count = \sum_{i=1}^n\phi(i) - 1
# 大约运行 30 秒

from math import sqrt

# 素数判定
def isprime(n):
  if n < 2:
    return False
  if n==2 or n==3:
    return True
  if n%6!=1 and n%6!=5:
    return False
  for i in range(5, int(sqrt(n))+1, 6):
    if n%i==0 or n%(i+2)==0:
      return False
  return True

# 质因数分解
def pdivisors(n):
  if isprime(n):
    return [n]
  flag = int(sqrt(n))+1
  divs_list = []
  for i in range(2, flag):
    if n%i==0:
      if isprime(i):
        divs_list.append(i)
      if isprime(ndi:=int(n/i)) and ndi!=i:
        divs_list.append(ndi)
  return divs_list

# 欧拉 φ 函数
def phi(n):
  prime_list = pdivisors(n)
  phin = n
  for d in prime_list:
    phin *= (1-1/d)
  return int(phin)

count = 0
for i in range(1, 1000001):
  count += phi(i)
count -= 1
print(count)