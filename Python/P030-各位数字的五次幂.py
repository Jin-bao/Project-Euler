def powerSumQ(num:int) -> bool:
  powerSum = 0
  for s in str(num):
    powerSum += int(s)**5
  return powerSum == num

numList = []
for num in range(2,9**5*5+1):
  if powerSumQ(num):
    numList += [num]
print(sum(numList))