from itertools import permutations

numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pnumList = list(permutations(numList))
print(pnumList[999999])

# from math import factorial

# def modrem(dividend:int, divisor:int) -> list:
#   if dividend%divisor == 0:
#     mod = dividend//divisor - 1
#     rem = divisor
#   else:
#     mod = dividend//divisor
#     rem = dividend%divisor
#   return [mod, rem]

# def permutation(numList:list, number:int, pNumList:list=[]) -> list:
#   if numList == []:
#     return pNumList

#   headNum = 0
#   while factorial(len(numList)-headNum) > number:
#     headNum += 1
#   if headNum-1 > 0:
#     pNumList.extend(numList[0:headNum-1])
#     del numList[0:headNum-1]

#   if factorial(len(numList)) == number:
#     numList.reverse()
#     pNumList.extend(numList)
#     return pNumList

#   flagList = modrem(number, factorial(len(numList)-1))
#   pNumList.extend([numList[flagList[0]]])
#   numList.remove(numList[flagList[0]])
#   number = flagList[1]
  
#   return permutation(numList, number)
  
# numList = [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
# numList.sort()
# print(''.join(map(str, permutation(numList, 1000000))))
# print(numList)
# 可以计算任何范围内的排列，如第 500 项
# print(''.join(map(str, permutation(numList, 500))))
# 输出 0123849576