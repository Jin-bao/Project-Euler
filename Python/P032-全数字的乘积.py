# 假设 x*y = z，那么只有两种情况满足：x 是 1 位数，y 和 z 是四位数；x 是两位数，y 是三位数，z 是四位数

# from copy import deepcopy

def flattenToStr(numList:list) -> list:
  numStrList = []
  for item in numList:
    tempStr = ''
    for s in item:
      tempStr += str(s)
    if len(tempStr) == 9:
      numStrList += [tempStr]
  return numStrList

def pandigitalQ(strNum:str) -> bool:
  if '0' in strNum or len(set(strNum)) < 9:
    return False
  else:
    return True

productList = []
for x in range(1,10):
  for y in range(1000,10000):
    productList += [[x, y, x*y]]
for x in range(10,99):
  for y in range(100,1000):
    productList += [[x, y, x*y]]

productList = flattenToStr(productList)
resultList = []
for item in productList:
  if pandigitalQ(item):
    resultList += [item[5:10]]
print(sum(map(int, list(set(resultList)))))