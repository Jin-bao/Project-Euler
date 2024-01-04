powerList = []
for a in range(2, 101):
  for b in range(2, 101):
    powerList.extend([a**b])
print(len(set(powerList)))