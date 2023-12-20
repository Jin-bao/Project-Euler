# 利用对数的计算性质 log(a^b)=b*log(a)

from math import log10

with open('./files/p099_base_exp.txt', 'r') as base_exp:
  nums = [[int(n) for n in num.split(',')] \
    for num in base_exp.read().splitlines()]


l = 0
bigestl = 0
bigestnum = 0
while l<1000-1:
  if (b:=nums[l][1]*log10(nums[l][0])) > bigestnum:
    bigestl = l+1
    bigestnum = b
  l += 1

print(bigestl)