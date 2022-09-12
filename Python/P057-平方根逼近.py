def squareRootConvergents(num:int) -> dict:
  numerator = 1
  denominator = 1
  srcDict = {}
  while num > 0:
    numerator += denominator
    numerator, denominator = denominator, numerator
    numerator += denominator
    srcDict[numerator] = denominator
    num -= 1
  return srcDict

total = 0
for key,val in squareRootConvergents(1000).items():
  if len(str(key)) > len(str(val)):
    total += 1
print(total)
'''
f(2) -> 3/2 -> (3+2)/2 = 5/2 -> 2/5 -> (2+5)/5 = 7/5
f(3) -> 7/5 -> (7+5)/5 = 12/5 -> 5/12 -> (5+12)/12 = 17/12
假设
f(1) -> 1/1 -> (1+1)/1 = 2/1 -> 1/2 -> (1+2)/2 = 3/2
'''