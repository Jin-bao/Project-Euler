from math import sqrt

def dn(num:int) -> int:
  flag = int(sqrt(num))+1
  divisorList = []
  for i in range(1, flag):
    if num%i == 0:
      numDi = int(num/i)
      divisorList.extend([i, numDi])
  divisorList.remove(max(divisorList))# 最大值有多个只会删一个
  return sum(divisorList)

amicableNumList = []
upLimit = 10000
for i in range(2, upLimit+1):
  dni = dn(i)
  dndni = dn(dn(i))
  if i==dndni and i!=dni:
    if dni > 10000:
      amicableNumList.extend([i])
    else:
      amicableNumList.extend([i, dni])
print(sum(list(set(amicableNumList))))
