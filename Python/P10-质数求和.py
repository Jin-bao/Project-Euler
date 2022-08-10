from math import floor, sqrt

def primeQ(num):
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

total = 0
for i in range(2000000):
  if primeQ(i):
    total = total+i
print(total)