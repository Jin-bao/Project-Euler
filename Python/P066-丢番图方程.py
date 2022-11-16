# 计算 sqrt(D) 的连分数表示，设其形式为 [a0; a1, a2, ..., ai, 2a0]，循环节长度为 m
# 把连分数表示的最后一项去掉，得到 [a0; a1, a2, ..., ai]，计算这个连分数表示的渐进收敛项，记为 p/q
# 当 m 为偶数时，原方程的最小正整数解为 (p, q)，当 m 是奇数，最小正整数解为 (p**2+D*q**2, 2*p*q)

def opsr(num:int) -> list:
  # 不再判断是否可以开平方了
  numInt  = int(num**0.5)
  divisor   = num - numInt**2
  intPart   = int((num**0.5+numInt)/divisor)
  numerator = intPart*divisor - numInt

  loopDict = {intPart:[divisor, numerator]}
  loopList = [intPart]
  while True:
    divisor   = int((num-numerator**2)/divisor)
    intPart   = int((num**0.5+numerator)/divisor)
    numerator = intPart*divisor - numerator
    if (intPart in loopDict) \
      and (divisor==loopDict[intPart][0]) and (numerator==loopDict[intPart][1]):
      return [num, numInt, loopList]
    else:
      loopList += [intPart]

def convergent(numList:list) -> int:
  num      = numList[0]
  intPart  = numList[1]
  loopList = numList[2]

  # 上面第一条
  m = len(loopList)
  # 上面第二条前半部分
  loopList.pop()
  # 上面第二条后半部分
  if len(loopList) == 0:
    # 第三条
    return intPart**2+num
  else:
    deno = loopList[-1]
    nomerator = 1
    for i in range(m-3, -1, -1):
      nextdeno = loopList[i]
      nomerator = nextdeno*deno + nomerator
      nomerator, deno = deno, nomerator
    nomerator = intPart*deno + nomerator
    # 第三条
    if m%2 == 0:
      return nomerator
    else:
      return nomerator**2+num*deno**2

minSol = 0
D = 0
for i in range(2, 1001):
  if int(i**0.5)**2 == i:
    continue
  else:
    if (res:=convergent(opsr(i))) > minSol:
      minSol = res
      D = i
print(minSol, D)