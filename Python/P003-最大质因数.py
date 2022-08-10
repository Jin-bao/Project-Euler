def maxPrimeFactor(num):
  if num < 2:
    return 1
  primeFactor = 2
  while primeFactor <= num:
    if primeFactor == num:
      return primeFactor
    if num > primeFactor and num%primeFactor == 0:
      num = num/primeFactor
      continue
    primeFactor = primeFactor+1
  return primeFactor

print(maxPrimeFactor(600851475143))