from math import sqrt

def divisors(num):
  flag = int(sqrt(num))
  i = 1
  divisorList = []
  while i <= flag:
    if num%i == 0:
      numDi = int(num/i)
      divisorList.extend([i,numDi])
    i = i+1
  return sorted(divisorList)

i = 1
while len(divisors(i*(i+1)/2)) < 500:
  i = i+1
print(i, int(i*(i+1)/2))