def difference(num):
  squareSum = 0
  sumSquare = 0
  for i in range(1,num+1):
    squareSum = squareSum + i**2
  sumSquare = int(((1+num)*num/2))**2
  return sumSquare-squareSum

print(difference(100))