import time

def Collatz(num):
  if num == 1:
    return 1
  if num%2 == 0:
    return Collatz(num/2)+1
  elif num%2 == 1:
    return Collatz(3*num+1)+1

begin = time.time()
maxNum = 1000000
sequenceNumList = []
for i in range(1,maxNum):
  sequenceNumList.extend([[Collatz(i),i]])
end = time.time()
print(end-begin, sorted(sequenceNumList, key=lambda sNL:sNL[0])[-1])