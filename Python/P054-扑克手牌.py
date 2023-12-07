def value_map(value) -> dict:
  rule = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'T', 11:'J', 12:'Q', 13:'K', 14:'A'}
  return {rule[v] for v in value}


def value_map_inverse(value) -> list:
  rule ={'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
  return [rule[v] for v in value]


def rank(hands) -> list:
  value = {card[0] for card in hands}
  suit  = {card[1] for card in hands}

  level = 0
  sorted_value = sorted(value_map_inverse([card[0] for card in hands]),reverse=True)

  # 同花
  if len(suit)==1 and len(value)!=2:
    # 同花
    level = 6
    # 同花顺
    if value in [value_map(range(v,v+5)) for v in range(2,11)]:
      level = 9
      # 皇家同花顺
      if sorted_value[0] == 14:
        level = 10
    return [level]+sorted_value
  
  # 5 张不同牌
  if len(value) == 5:
    # 单牌
    level = 1
    # 顺子
    if value in [value_map(range(v,v+5)) for v in range(2,11)]:
      level = 5
    return [level]+sorted_value
  
  # 4 张不同牌
  if len(value) == 4:
    # 对子
    level = 2
    for idx in range(0,4):
      if sorted_value[idx] == sorted_value[idx+1]:
        pair_value = sorted_value[idx]
        break
    res_value = [v for v in sorted_value if v!=pair_value]
    res_value.insert(0,pair_value)
    return [level]+res_value
  
  # 3 张不同牌
  if len(value) == 3:
    # 三条
    for idx in range(0,3):
      if sorted_value[idx] == sorted_value[idx+1] == sorted_value[idx+2]:
        level = 4
        tok_value = sorted_value[idx]
        res_value = [v for v in sorted_value if v!=tok_value]
        res_value.insert(0,tok_value)
        return [level]+res_value
    # 两对
    level = 3
    pair_value = []
    for idx in range(0,4):
      if sorted_value[idx] == sorted_value[idx+1]:
        pair_value += [sorted_value[idx]]
    res_value = [v for v in sorted_value if v not in pair_value]
    res_value = pair_value + res_value
    return [level]+res_value
  
  # 2 张不同牌
  if len(value) == 2:
    # 四条
    for idx in range(0,2):
      if sorted_value[idx] == sorted_value[idx+1] == sorted_value[idx+2] == sorted_value[idx+3]:
        level = 8
        fok_value = sorted_value[idx]
        res_value = [v for v in sorted_value if v!=fok_value]
        res_value.insert(0,fok_value)
        return [level]+res_value
    # 葫芦
    for idx in range(0,3):
      if sorted_value[idx] == sorted_value[idx+1] == sorted_value[idx+2]:
        level = 7
        fh_value = sorted_value[idx]
        res_value = [v for v in sorted_value if v!=fh_value]
        res_value.insert(0,fh_value)
        return [level]+res_value


def vs(hands1, hands2) -> int:
  rank1 = rank(hands1)
  rank2 = rank(hands2)
  i = 0
  while i<3:
    if rank1[i] > rank2[i]:
      return 1
    elif rank1[i] == rank2[i]:
      i += 1
      continue
    else:
      return 2


with open('./files/p054_poker.txt') as poker:
  cts = [g.split() for g in poker.read().splitlines()]
  cts = [[game[:5],game[5:]] for game in cts]

count = 0
for i in range(len(cts)):
  if vs(cts[i][0], cts[i][1]) == 1:
    count += 1
print(count)