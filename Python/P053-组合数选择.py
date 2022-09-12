from math import comb

geqMilionList = []
for n in range(1, 101):
  for r in range(0, n+1):
    if (c := comb(n, r)) > 1000000:
      geqMilionList += [c]
print(len(geqMilionList))