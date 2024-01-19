def divisors_sum(n):
  divisors = set()

  for d in range(1, int(n**0.5)+1):
    if n%d == 0:
      divisors.add(d)
      divisors.add(n//d)
  divisors.discard(n)

  return sum(divisors)


relation = dict()
def amicable_chain(n):
  chain = [n]
  while True:
    if n in relation:
      next_n = relation[n]
      if next_n in chain:
        if next_n == chain[0]:
          break
        else:
          return []
      elif next_n==1:
        return []
      else:
        chain += [next_n]
        n = next_n
    else:
      if (next_n:=divisors_sum(n)) <= 1000000:
        relation[n] = next_n
      else:
        return []

  return chain

chain_len = 1
for n in range(2, 1200000):
  chain = amicable_chain(n)
  if len(chain) >= chain_len:
    chain_len = len(chain)
    print(n, chain_len, min(chain), chain)
    print()