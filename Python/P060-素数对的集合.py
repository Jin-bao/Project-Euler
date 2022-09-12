from math import floor, sqrt
from itertools import permutations, combinations

def primeQ(num:int) -> bool:
  if num < 2:
    return False
  if num==2 or num==3:
    return True
  if num%6!=1 and num%6!=5:
    return False
  for i in range(5,floor(sqrt(num))+1,6):
    if num%i==0 or num%(i+2)==0:
      return False
  return True

def generatePrimeList(maxNum:int) -> list:
  pList = []
  for i in range(1, maxNum+1):
    if primeQ(i):
      pList += [i]
  return pList

def primePairQ(iter:iter) -> bool:
  iterList = permutations(iter, 2)
  for item in iterList:
    itemNum = int(str(item[0])+str(item[1]))
    if not primeQ(itemNum):
      return False
  return True

# 这题类似于第 21 题，需要图论的知识。
# 我只能写出一个最温柔的暴力算法，
# 事实上只是计算 400 以内素数的组合，
# 就已经要很长时间了，
# 到 1000 以内时，计算量就大到无法计算出结果了，
# 而答案中的最大素数为 8389。
# https://pe.metaquant.org/pe060.html 作了讨论，给出了一个优雅的方法。
# 当然，可以代入一些包含答案的数，以验证算法没有问题。

# pList = generatePrimeList(10000)
pList = [13, 23, 43, 61, 409, 709, 1087, 1163, 5197, 5701, 6733, 8389]
# 其中 (13, 5197, 5701, 6733, 8389) 是符合要求的一组数

for item in combinations(pList, 5):
  if primePairQ(item):
    print(item)
    print(sum(item))