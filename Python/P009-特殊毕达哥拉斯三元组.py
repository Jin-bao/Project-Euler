def sPT(abcSum):
  for a in range(abcSum):
    for b in range(a,abcSum):
      c = abcSum-a-b
      if c<=b:
        break
      if a**2+b**2 == c**2:
        return a*b*c

abcSum = 1000
print(sPT(abcSum))