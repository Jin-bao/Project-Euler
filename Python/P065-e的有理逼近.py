def eConvergent(n:int) -> int:
  # 生成周期列表
  tList = []
  for i in range(1, n):
    if (rem:=i%3) == 2:
      tList += [2*(i//3)+rem]
    else:
      tList += [1]
  
  # 开始循环
  deno = tList[-1]
  nomerator = 1
  for i in range(n-2, 0, -1):
    nextdeno = tList[i-1]
    nomerator = nextdeno*deno + nomerator
    nomerator, deno = deno, nomerator
  deno = 2*deno + nomerator
  
  return deno

print(sum([int(s) for s in str(eConvergent(100))]))