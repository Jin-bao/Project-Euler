# https://pe.metaquant.org/pe082


def path_sum_tw(matrix:list) -> int:
  n = len(matrix)
  cost = [matrix[i][0] for i in range(n)]
  for column in range(1,n):
    cost[0] += matrix[0][column]
    for row in range(1,n):
      cost[row] = min(cost[row], cost[row-1]) + matrix[row][column]
    for row in range(n-2,-1,-1):
      cost[row] = min(cost[row], cost[row+1] + matrix[row][column])
      
  return min(cost)


# matrix = [
#   [131, 673, 234, 103,  18],
#   [201,  96, 342, 965, 150],
#   [630, 803, 746, 422, 111],
#   [537, 699, 497, 121, 956],
#   [805, 732, 524,  37, 331]
# ]

with open('./files/p082_matrix.txt', 'r') as file:
  date = file.read()
lines = date.split('\n')
matrix = [[int(num) for num in line.split(',')] for line in lines if line]


print(path_sum_tw(matrix))