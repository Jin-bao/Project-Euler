def transform(matrix:list) -> list:
  matrix_prime = []
  order = len(matrix)

  for l in range(2*order-1):
    line_temp = []
    if l>=order:
      i = order-1; j = l-order+1
      while j<order:
        line_temp += [matrix[i][j]]
        i -= 1; j += 1
    else:
      i = l; j = 0
      while i>=0:
        line_temp += [matrix[i][j]]
        i -= 1; j += 1
    matrix_prime += [line_temp]

  return order, matrix_prime

def minval_path(matrix:list) -> int:
  order, matrix = transform(matrix)

  min_line = matrix[0]
  for l in range(1,len(matrix)):
    next_line = matrix[l]
    if l<order:
      for i in range(l_len:=len(next_line)):
        if i==0:
          next_line[i] += matrix[l-1][i]
        elif i<l_len-1:
          next_line[i] += min(matrix[l-1][i-1], matrix[l-1][i])
        else:
          next_line[i] += matrix[l-1][i-1]
      min_line = next_line
    else:
      for i in range(len(next_line)):
        next_line[i] += min(matrix[l-1][i], matrix[l-1][i+1])
      min_line = next_line
  
  return min_line

with open('./files/p081_matrix.txt', 'r') as file:
  date = file.read()
lines = date.split('\n')
matrix = [[int(num) for num in line.split(',')] for line in lines if line]

# matrix = [
#   [131, 673, 234, 103,  18],
#   [201,  96, 342, 965, 150],
#   [630, 803, 746, 422, 111],
#   [537, 699, 497, 121, 956],
#   [805, 732, 524,  37, 331]
# ]

print(minval_path(matrix))