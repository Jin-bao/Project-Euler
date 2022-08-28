def reciprocalCyclesLen(dividend:int, divisor:int) -> int:
  cycleList = []
  remList = []
  while True:
    if dividend >= divisor:
      dividend %= divisor
    if dividend == 0:
      return 0
    dividend *= 10
    mod = dividend//divisor
    rem = dividend% divisor
    if rem not in remList:
      cycleList.extend([mod])
      remList.extend([rem])
      dividend = rem
    else:
      cycleList.extend([mod])
      remList.extend([rem])
      if mod == cycleList[remList.index(rem)]:
        # 小数点第一位属于循环节
        # 这时就会对 cycleList 多 extend 一次
        return len(cycleList)-cycleList.index(mod)-1
      else:
        # 小数点后面几位不属于循环节
        return len(cycleList)-cycleList.index(mod)

numCycleLenDict = {}
for i in range(2, 1001):
  numCycleLenDict[i] = reciprocalCyclesLen(1, i)
for key,val in numCycleLenDict.items():
  if val == max(numCycleLenDict.values()):
    print({key: val})