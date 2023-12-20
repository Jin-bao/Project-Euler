def square_sum(num):
  num_sum = 0
  while (mod:=num//10) > 0:
    rem = num%10
    num_sum += rem**2
    num = mod
  num_sum += num**2
  
  return num_sum


count = 0

for n in range(1, 10000000):
  while (num_sum:=square_sum(n))!=1 and num_sum!=89:
    n = num_sum
  if num_sum==1:
    pass
  else:
    count += 1


print(count)