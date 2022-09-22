number = 0
for a in range(1, 10):
  for b in range(1, 22):
    result = a**b
    if len(str(result)) == b:
      number += 1
print(number)