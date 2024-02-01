def map_to_dict(matrix):
  matrix_dict = dict()
  n = len(matrix)
  for i in range(n):
    for j in range(n):
      matrix_dict[(i,j)] = matrix[i][j]
  
  return matrix_dict


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
n = len(matrix)
graph = map_to_dict(matrix)
total = sum(graph.values()) + 1
starting_nodes = {key:total for key in graph.keys()}
previous_node_table = {key:(n,n) for key in graph.keys()}


end_node = (n-1,n-1)
current_node = (0,0)
passed_nodes = {current_node}
starting_nodes[current_node] = graph[current_node]
while current_node != end_node:
  next_nodes = []
  for direction in [(-1,0), (0,1), (1,0), (0,-1)]:
    next_node = tuple(map(sum, zip(current_node, direction)))
    if next_node in graph and next_node not in passed_nodes:
      next_nodes += [next_node]
  
  for next_node in next_nodes:
    path_sum = starting_nodes[current_node] + graph[next_node]
    if path_sum < starting_nodes[next_node]:
      starting_nodes[next_node] = path_sum
      previous_node_table[next_node] = current_node
  
  passed_nodes.add(current_node)
  current_node = \
    min(starting_nodes.keys()-passed_nodes, key=starting_nodes.get)


path_value = []
while current_node != (0,0):
  path_value += [graph[current_node]]
  current_node = previous_node_table[current_node]
path_value += [graph[current_node]]


print(list(path_value.__reversed__()), sum(path_value))