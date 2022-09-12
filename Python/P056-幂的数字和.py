def digitalSum(num:int) -> int:
  sum = 0
  while (mod := num//10) > 0:
    sum += num%10
    num = mod
  sum += num
  return sum

powerList = []
for a in range(1, 100):
  for b in range(1, 100):
    powerList += [a**b]

print(max(map(digitalSum, powerList)))