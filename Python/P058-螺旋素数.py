from math import floor, sqrt
from itertools import count

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

numList = [1]
primeNumList = []

for n in count(3, 2):
  d = n-1
  num = (n-2)**2+n-1
  for _ in range(4):
    if primeQ(num):
      primeNumList += [num]
    numList += [num]
    num += d
  
  rate = len(primeNumList) / len(numList)
  if rate < 0.1:
    print(n)
    exit(0)