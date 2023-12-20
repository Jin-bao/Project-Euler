def primeQ(num):
  if num < 2:
    return False
  if num==2 or num==3:
    return True
  if num%6!=1 and num%6!=5:
    return False
  for i in range(5,int(num**0.5)+1,6):
    if num%i==0 or num%(i+2)==0:
      return False
  return True

N = 50000000
prime_list2 = [i for i in range(2, int(N**0.5)  +1) if primeQ(i)]
prime_list3 = [i for i in range(2, int(N**(1/3))+1) if primeQ(i)]
prime_list4 = [i for i in range(2, int(N**0.25) +1) if primeQ(i)]

nums = set()
for i in prime_list2:
  for j in prime_list3:
    for k in prime_list4:
      res = i**2 + j**3 + k**4
      if res<N:
        nums.add(res)
print(len(nums))