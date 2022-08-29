numList = [1]
for n in range(3, 1002, 2):
  d = n-1
  num = (n-2)**2+n-1
  for i in range(4):
    numList.extend([num])
    num += d

print(sum(numList))