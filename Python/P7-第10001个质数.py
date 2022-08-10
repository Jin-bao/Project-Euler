from math import floor, sqrt

def primeQ(num):
  # 大于等于5的质数一定和6的倍数相邻
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

k = 0; num = 1
while k<10001:
  num = num+1
  if primeQ(num): k = k+1
print(num)