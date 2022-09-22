def P3n() -> list:
  PnList = []
  for n in range(45, 141):
    Pn = int(n*(n+1) / 2)
    if (Pnr:=Pn%100) > 9:
      PnList += [[Pn//100, Pnr]]
  return PnList

def P4n() -> list:
  PnList = []
  for n in range(32, 100):
    Pn = n**2
    if (Pnr:=Pn%100) > 9:
      PnList += [[Pn//100, Pnr]]
  return PnList

def P5n() -> list:
  PnList = []
  for n in range(26, 82):
    Pn = int(n*(3*n-1) / 2)
    if (Pnr:=Pn%100) > 9:
      PnList += [[Pn//100, Pnr]]
  return PnList

def P6n() -> list:
  PnList = []
  for n in range(23, 71):
    Pn = n*(2*n-1)
    if (Pnr:=Pn%100) > 9:
      PnList += [[Pn//100, Pnr]]
  return PnList

def P7n() -> list:
  PnList = []
  for n in range(21, 64):
    Pn = int(n*(5*n-3) / 2)
    if (Pnr:=Pn%100) > 9:
      PnList += [[Pn//100, Pnr]]
  return PnList

def P8n() -> list:
  PnList = []
  for n in range(19, 59):
    Pn = n*(3*n-2)
    if (Pnr:=Pn%100) > 9:
      PnList += [[Pn//100, Pnr]]
  return PnList

from itertools import permutations

PnList = [P3n(), P4n(), P5n(), P6n(), P7n(), P8n()]
script = list(permutations([0,1,2,3,4,5], 6))

for sitem in script:
  leftChain = []
  for item1 in PnList[sitem[0]]:
    for item2 in PnList[sitem[1]]:
      for item3 in PnList[sitem[2]]:
        if item1[1]==item2[0] and item2[1]==item3[0]:
          leftChain += [[item1, item2, item3]]
  righChain = []
  for item1 in PnList[sitem[3]]:
    for item2 in PnList[sitem[4]]:
      for item3 in PnList[sitem[5]]:
        if item1[1]==item2[0] and item2[1]==item3[0]:
          righChain += [[item1, item2, item3]]
  cycleList = []
  for item1 in leftChain:
    for item2 in righChain:
      if item1[2][1]==item2[0][0] and item1[0][0]==item2[2][1]:
        cycleList = [
          item1[0][0]*100+item1[0][1],
          item1[1][0]*100+item1[1][1],
          item1[2][0]*100+item1[2][1],
          item2[0][0]*100+item2[0][1],
          item2[1][0]*100+item2[1][1],
          item2[2][0]*100+item2[2][1]
        ]
        print(sum(cycleList))
        exit(0)