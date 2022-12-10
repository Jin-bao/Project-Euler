def gcd(n:int, m:int) -> int:
  while n > 0:
    m, n = n, m%n
  return m

up_limit = 12001
left  = 1 / 3
right = 1 / 2
count = 0
for d in range(2, up_limit):
  for n in range(1, d):
    if gcd(n,d) == 1:
      nd = n / d
      if nd>left and nd<right:
        count += 1
print(count)