from math import factorial
def binomial(n, k):
  return int(factorial(n) / (factorial(n-k)*factorial(k)))

print(binomial(40,20))