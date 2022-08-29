from math import floor, sqrt

def primeQ(num:int) -> bool:
  if num < 2:
    return False
  if num==2 or num==3:
    return True
  if num%6!=1 and num%6!=5:
    return False
  for i in range(5,floor(sqrt(num))+1,6):
    if num%i==0 or num%(i+2)==0:
      return False
  return True

def quadraticPrimes() -> dict:
  qpDict = {}
  for a in range(-999, 1000):
    for b in range(-1000, 1001):
      n = 0
      len = 0
      while primeQ(n**2 + a*n + b):
        len += 1; n += 1
      ab = a*b
      if ab in qpDict:
        if len > qpDict[ab]:
          qpDict[ab] = len
      else:
        qpDict[a*b] = len
  return qpDict

qpDict = quadraticPrimes()
print(max(qpDict, key=qpDict.get))