from numpy import outer

def palindromeQ(numList):
  palindromeList = []
  for num in numList:
    numReverse = str(num)[::-1]
    if str(num) == numReverse:
      palindromeList.extend([num])
  return palindromeList

print(max(palindromeQ(outer(range(100,1000), range(100,1000)).flatten())))