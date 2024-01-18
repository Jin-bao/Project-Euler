from sys import setrecursionlimit
setrecursionlimit(100000)


def gpentagon(n):
  if n%2 == 0:
    n = n//2
    return int((3*n*n+n) / 2)
  else:
    n = n//2 + 1
    return int((3*n*n-n) / 2)
  

partition = {0:1}
def coin(n):
  if n in partition:
    return partition[n]
  
  pnum = 0
  k = 1
  while n >= (gp_k:=gpentagon(k)):
    coe = (-1)**((k-1)//2)
    pnum += coe * coin(n-gp_k)
    k += 1
  
  partition[n] = pnum
  return partition[n]

# def coin(n):
#   partition = {0: 1}
#   for i in range(1, n+1):
#     pnum = 0
#     k = 1
#     while i >= (gp_k:=gpentagon(k)):
#       coe = (-1)**((k-1)//2)
#       pnum += coe * partition[i-gp_k]
#       k += 1
#     partition[i] = pnum
#   return partition[n]


n = 1
while True:
  if coin(n)%1000000 != 0:
    n += 1
  else:
    print(n)
    break