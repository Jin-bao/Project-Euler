# phi(n) = n*prod(p|n, 1-1/p)
# n/phi(n) = prod(p|n, p/(p-1))
from sympy import prime

upperLimit = 1000000
i, lastProd = 1, 1
while (prod:=lastProd*prime(i)) < upperLimit:
  lastProd = prod
  i += 1
print(lastProd)