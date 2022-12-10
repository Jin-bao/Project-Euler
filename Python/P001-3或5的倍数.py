providedNum = 1000
mtpList = []
for n in range(1,providedNum):
  if n%3 == 0:
    mtpList.append(n)
  if (n%5==0) and (n%3!=0):
    mtpList.append(n)
print(sum(mtpList))