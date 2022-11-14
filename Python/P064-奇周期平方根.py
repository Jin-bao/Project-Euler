from math import isqrt, sqrt
def oPSR(num:int) -> int:
  numInt  = isqrt(num)
  numSqrt = sqrt(num)
  if numInt == numSqrt:# 如果恰好开出整数
    return 0

  # 得到整数部分、因子、(传入数字、) 分子余下的数字
  divisor   = num - numInt**2
  intPart   = int((sqrt(num)+numInt)/divisor)
  numerator = intPart*divisor - numInt

  # 记录下终止条件
  loopDict = {intPart:[divisor, numerator]}
  loopList = [intPart]
  # 开始循环
  while True:
    divisor   = int((num-numerator**2)/divisor)
    intPart   = int((sqrt(num)+numerator)/divisor)
    numerator = intPart*divisor - numerator
    # 如果相同了则直接返回，结束
    if (intPart in loopDict) \
      and (divisor==loopDict[intPart][0]) and (numerator==loopDict[intPart][1]):
      return len(loopList)
    else:
      loopList += [intPart]

count = 0
for i in range(1, 10001):
  if oPSR(i)%2 == 1:
    count += 1
print(count)