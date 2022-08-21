import time

def Collatz(num):
  if num in CollatzDict:
    return CollatzDict[num]
  if num == 1:
    CollatzDict[num] = 1
    return CollatzDict[num]
  if num%2 == 0:
    CollatzDict[num] = Collatz(int(num/2))+1
    return CollatzDict[num]
  elif num%2 == 1:
    CollatzDict[num] = Collatz(3*num+1)+1
    return CollatzDict[num]

begin = time.time()
CollatzDict = {}
maxNum = 1000000
sequenceNumList = []
for i in range(1,maxNum):
  sequenceNumList.extend([[Collatz(i),i]])
end = time.time()
print(end-begin, sorted(sequenceNumList, key=lambda sNL:sNL[0])[-1])