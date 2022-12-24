import decimal

decimal.getcontext().prec = 102

total = 0
square = {i**2 for i in range(1, 10)}
for i in range(1, 100):
  if i not in square:
    nums = str(decimal.Decimal(i).sqrt())[0:101]
    for s in nums:
      try:
        total += int(s)
      except:
        pass
      
print(total)