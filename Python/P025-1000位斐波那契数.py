# 超出最大递归深度，默认最大递归深度为 1000
# def fibonaccii(num:int, fn:dict={1:1, 2:1}) -> int:
#   if num in fn:
#     return fn[num]
#   fn[num] = fibonacci(num-1) + fibonacci(num-2)
#   return fn[num]

# 下面这个算法与上面的效率一样
def fibonacci(num:int) -> int:
  fn, fnp1 = 1, 1
  if num == 1:
    return fn
  if num == 2:
    return fnp1
  for _ in range(num-1):
    fn, fnp1 = fnp1, fn+fnp1
  return fn

n = 1
while len(str(fibonacci(n))) < 1000:
  n += 1
print(n)