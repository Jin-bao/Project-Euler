from itertools import permutations as pt


order = 5
num = range(1, 2*order+1)
ring_o_list = \
  [list(ring) for ring in pt(num, order) if ring[0]==min(ring)]

solution = []

for ring_o in ring_o_list:
  ring_i_list = [list(ring) for ring in pt(list(set(num)-set(ring_o)))]
  for ring_i in ring_i_list:
    sol = []
    for idx in range(order):
      node_sum = ring_o[idx] + ring_i[idx] + ring_i[(idx+1)%order]
      sol +=[node_sum, ring_o[idx], ring_i[idx], ring_i[(idx+1)%order]]
    
    count = 1
    for idx in range(0, (order-1)*4, 4):
      if sol[idx] == sol[idx+4]:
        count +=1
      else:
        break
    
    if count==order:
      for idx in reversed(range(0,order*4,4)):
        del sol[idx]
      solution += [sol]

for sol in solution:
  print(sol)