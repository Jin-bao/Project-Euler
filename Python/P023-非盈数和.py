from math import sqrt

def abundant(num:int) -> bool:
  flag = int(sqrt(num))+1
  divisorList = []
  for i in range(1, flag):
    if num%i == 0:
      numDi = int(num/i)
      divisorList.extend([i, numDi])
  divisorList = list(set(divisorList))
  divisorList.remove(max(divisorList))
  if sum(divisorList) > num:
    return True
  else:
    return False

abundantList = []
for i in range(1, 28124):
  if abundant(i):
    abundantList.extend([i])

abundantListSum = []
for i in range(len(abundantList)):
  for j in range(i, len(abundantList)):
    if abundantList[i]+abundantList[j] >= 28124:
      break
    else:
      abundantListSum.extend([abundantList[i]+abundantList[j]])
abundantListSum = list(set(abundantListSum))

total = 0
for i in range(1, 28124):
  if i in abundantListSum:
    pass
  else:
    total += i
print(total)