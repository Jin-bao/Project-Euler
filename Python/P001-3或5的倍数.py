providedNum = 1000
mtpList = []
for n in range(1,providedNum):
  if n%3 == 0:
    mtpList.extend([n])
  if (n%5==0) & (n%3!=0):
    mtpList.extend([n])
print(sum(mtpList))