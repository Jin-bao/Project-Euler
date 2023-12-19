def int_to_Roman(num:int) -> str:
  roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '', '']
  idx = 0

  # 荒谬的钩子
  # 今天加上的，但是这个函数在很久前就写好了，今天看不懂写得是啥了
  if num >= 4000:
    prefix = 'MMM'
  else:
    prefix = ''
  
  roman = ''
  while num > 0:
    left   = roman_list[idx]
    middle = roman_list[idx+1]
    right  = roman_list[idx+2]
    roman_digit = ''

    digit = num % 10
    if digit == 0:
      pass
    elif 0 < digit < 4:
      while digit > 0:
        roman_digit += left
        digit -= 1
    elif 4 <= digit < 9:
      diff = digit - 5
      if diff < 0:
        roman_digit = left + middle
      else:
        roman_digit = middle
        while diff > 0:
          roman_digit += left
          diff -= 1
    else:
      roman_digit = left + right

    roman = roman_digit + roman
    num //= 10
    idx  += 2

  return prefix+roman

def romanToInt(s:str) -> int:
  romanNum = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  arabicNum = 0

  idx = 0
  idxLen = len(s)-1
  while idx < idxLen:
    if romanNum[s[idx]] < romanNum[s[idx+1]]:
      arabicNum -= romanNum[s[idx]]
    else:
      arabicNum += romanNum[s[idx]]
    
    idx += 1
  arabicNum += romanNum[s[idx]]

  return arabicNum


with open('./files/p089_roman.txt', 'r') as roman:
  roman_nums = [num for num in roman.read().splitlines()]
  roman_nums_new = [int_to_Roman(romanToInt(num)) for num in roman_nums]

count = 0
idx = 0
while idx<1000:
  count += len(roman_nums[idx]) - len(roman_nums_new[idx])
  idx += 1
print(count)