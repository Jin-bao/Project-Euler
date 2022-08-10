class Fibonacci():
  def __init__(self, F1, F2):
    self.F1, self.F2 = F1, F2

  def getFN(self, N):
    Fn, Fnp1 = self.F1, self.F2
    if N==1:
      return self.F1
    if N==2:
      return self.F2
    for _ in range(N-1):
      Fn, Fnp1 = Fnp1, Fn+Fnp1
    return Fn

  def getFList(self, N):
    Fn, Fnp1 = self.F1, self.F2
    FibonacciList = []
    if N==1:
      return FibonacciList+[self.F1]
    if N==2:
      return FibonacciList+[self.F1, self.F2]
    for _ in range(N-1):
      Fn, Fnp1 = Fnp1, Fn+Fnp1
      FibonacciList.extend([Fn])
    return [self.F1]+FibonacciList

def getN(upperLimit):
  N = 1
  while Fibonacci.getFN(N) < upperLimit:
    N = N+1
  return N-1

Fibonacci = Fibonacci(1, 1)
upperLimit = 4000000

FibonacciEvenList = []
for item in Fibonacci.getFList(getN(upperLimit)):
  if item%2 == 0:
    FibonacciEvenList.extend([item])
print(sum(FibonacciEvenList))