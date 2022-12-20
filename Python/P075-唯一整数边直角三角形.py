from math import sqrt

def gcd(n:int, m:int) -> int:
  while n > 0:
    m, n = n, m%n
  return m

# 尝试一下生成器，虽然完全没有必要这样干
up_limit = 1500000
count = {}
black = set()

def gen():
  for i in range(2, int(sqrt(up_limit/2))):
    yield i
g = gen()

for d in g:
  for n in range(1, d):
    if gcd(n,d) == 1:
      d_square = d**2
      n_square = n**2
      a = d_square-n_square
      b = 2*n*d
      c = d_square+n_square
      a_clone = a
      b_clone = b
      c_clone = c
      k = 1
      kl = k * (a_clone+b_clone+c_clone)
      while kl <= up_limit:
        if kl in black:
          if kl in count:
            count.pop(kl)
          else:
            pass
        elif kl in count:
          if count[kl] != {a_clone, b_clone, c_clone}:
            black.add(kl)
            count.pop(kl)
        else:
          count[kl] = {a_clone, b_clone, c_clone}
        k += 1
        a_clone = k*a
        b_clone = k*b
        c_clone = k*c
        kl = a_clone + b_clone + c_clone
    else:
      continue

print(len(count))