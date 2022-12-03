# 最大公因数
def gcd(n:int, m:int) -> int:
  while n > 0:
    m, n = n, m%n
  return m

# 依据题意
up_limit = 1_000_000
fraction = 3/7
frac_list = []
# 对每一个数，找到与 3/7 最接近的最简真分数，存起来
for d in range(1, up_limit):
  n = int(fraction*d)
  while n > 0:
    if gcd(n, d)==1 and (nd:=n/d)<fraction:
      frac_list.append([nd, n])
      break
    else:
      n -= 1
# 排序，输出
print(sorted(frac_list)[-1])