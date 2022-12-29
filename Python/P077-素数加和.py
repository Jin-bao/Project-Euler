# https://pe.metaquant.org/pe077.html
from sympy import primepi, isprime
from functools import lru_cache

primes = [i for i in range(80) if isprime(i)]

@lru_cache(maxsize=2048)
def prime_sum(i, j):
  if i == 0:
    return 1
  elif i == 1:
    return 0
  elif j == 1:
    return 0 if i%2==1 else 1
  elif i < primes[j-1]:
    return prime_sum(i, j-1)
  else:
    return prime_sum(i, j-1) + prime_sum(i-primes[j-1], j)

if __name__ == '__main__':
  num = 2
  while True:
    num_sum = prime_sum(num, primepi(num))
    if num_sum > 5000:
      break
    else:
      num += 1

  print(num)

  # prime_sum(7, 3)   prime_sum(7, 4) 结果不对劲