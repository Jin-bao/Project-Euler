# (i, j)  ->  \sum_{i,j}ij


def count_rects(i, j):
  return int((1+i)*(1+j)*i*j / 4)


N = 2000000

count = dict()
for i in range(1,2001):
  for j in range(1,2001):
    count[count_rects(i,j)] = [i,j]

interval = 2000000
area = 0
for k in count.keys():
  if (i:=abs(k-N)) < interval:
    interval = i
    area = count[k][0] * count[k][1]

print(area)