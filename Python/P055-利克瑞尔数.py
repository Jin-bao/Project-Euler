def palindromeQ(num:int) -> bool:
  if (numStr := str(num)) == numStr[::-1]:
    return True
  else:
    return False

LychrelList = []
for i in range(1, 10001):
  iClone = i
  nOfT = 50
  while nOfT >= 0:
    iClone = iClone + int(str(iClone)[::-1])
    nOfT -= 1
    if palindromeQ(iClone):
      break
  else:
    LychrelList += [i]

print(len(LychrelList))