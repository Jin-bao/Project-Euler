def Collatz(num:int, CollatzDict:dict={1: 1}) -> int:
  if num in CollatzDict:
    return CollatzDict[num]
  if num%2 == 0:
    CollatzDict[num] = Collatz(int(num/2))+1
    return CollatzDict[num]
  elif num%2 == 1:
    CollatzDict[num] = Collatz(3*num+1)+1
    return CollatzDict[num]
  return 0

maxNum = 1000000
sequenceNumList = []
for i in range(1,maxNum):
  sequenceNumList.extend([[Collatz(i),i]])
print(sorted(sequenceNumList, key=lambda sNL:sNL[0])[-1])