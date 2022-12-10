def factorial(num:int) -> int:
  if num <= 1:
    return 1
  else:
    return num*factorial(num-1)

def digit_factorial_sum(num:int) -> int:
  df_sum = 0
  while num > 0:
    df_sum += factorial(num%10)
    num //= 10
  return df_sum

def digit_factorial_chains(num:int, digit_chains:set) -> int:
  digit_chains.add(num)
  df_sum = digit_factorial_sum(num)
  if df_sum in digit_chains:
    return len(digit_chains)
  digit_chains.add(df_sum)
  return digit_factorial_chains(df_sum, digit_chains)
# 这个函数按下面这样写死活不能得出正确的结果，好像第二个参数完全没效果，要小心
# def digit_factorial_chains(num:int, digit_chains:set=set()) -> int:
#   digit_chains.add(num)
#   df_sum = digit_factorial_sum(num)
#   if df_sum in digit_chains:
#     return len(digit_chains)
#   digit_chains.add(df_sum)
#   return digit_factorial_chains(df_sum)

count = 0
for i in range(1, 1000001):
  if digit_factorial_chains(i, set()) == 60:
    print(i)
    count += 1
print(count)