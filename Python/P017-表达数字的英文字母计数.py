def numName(num:int) -> str:
  name = 'numName'
  preName = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
  if 0<=num & num<=20:
    name = preName[num]
    return name
  elif 20<num & num<100:
    ty = ['twen', 'thir', 'for', 'fif', 'six', 'seven', 'eigh', 'nine']
    if num%10 == 0:
      name = ty[(num//10)%10-2] + 'ty'
    else:
      name = ty[(num//10)%10-2] + 'ty ' + preName[num%10]
    return name
  elif 100<=num & num<1000:
    ty = ['twen', 'thir', 'for', 'fif', 'six', 'seven', 'eigh', 'nine']
    if num%100 == 0:
      name = preName[num//100] + ' hundred'
    else:
      name = preName[num//100] + ' hundred and ' + numName(num%100)
    return name
  else:
    return 'one thousand'

letterNum = 0
for i in range(1,1001):
  letterNum += len(numName(i).replace(' ', ''))
print(letterNum)