def cubicPer(min:int, max:int) -> dict:
  cubicPerDict = {}
  for i in range(min, max+1):
    cubic = i**3
    cubicPerDict[cubic] = ''.join(sorted(str(cubic)))
  return cubicPerDict

def door(cubicDict:dict) -> list[list]:
  perDict = {}
  catList = []
  num = 0
  for key,val in cubicDict.items():
    if val in perDict:
      catList[perDict[val]] += [key]
    else:
      perDict[val] = num
      num += 1
      catList += [[key]]
  return catList

# 只能先猜测范围
guessCubicList = door(cubicPer(5, 9000))
for item in guessCubicList:
  if len(item) == 5:
    print(min(item))