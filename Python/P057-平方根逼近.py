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