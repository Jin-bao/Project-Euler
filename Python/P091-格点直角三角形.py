O = (0,0)


coordinates = list()
for x in range(51):
  for y in range(51):
    coordinates += [(x,y)]
del coordinates[0]


count = 0
for P in coordinates:
  for Q in coordinates[coordinates.index(P)+1:]:
    OP = P
    OQ = Q
    PQ = (Q[0]-P[0], Q[1]-P[1])
    if OP[0]*OQ[0] + OP[1]*OQ[1] == 0:
      count += 1
      continue
    if OP[0]*PQ[0] + OP[1]*PQ[1] == 0:
      count += 1
      continue
    if OQ[0]*PQ[0] + OQ[1]*PQ[1] == 0:
      count += 1


print(count)
