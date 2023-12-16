# cipher.txt 中出现最多的是 80
# 只有 空格^p==80，且 空格^p==94，所以 key 的第三个一定是 p
# 其次，txt 中第二个 80 与第一个 80 之间相差 30 多位，常见单词没有那么长的
# 然后，空格^x==88，逗号^t==88，句点^v==88
# txt 中有些 88 很近但没有连续的，因此不可能是标点符号，所以 key 的第二个是 x
# 同样，空格^e==69，逗号^i==69，句点^k==69
# 很多 69 很近但没有连续的，因此不可能是标点符号，所以 key 的第一个是 e
# 这样得出 key 为 `exp'，显然没有问题
# 以上统计一下 cipher 中数字的频率就能分析出来

chars_ascii_scp = [32, 44, 46]
chars_ascii_AZ  = list(range(65,91))
chars_ascii_az  = list(range(97,123))
chars_ascii = chars_ascii_scp + chars_ascii_AZ + chars_ascii_az
key = [ord('e'), ord('x'), ord('p')]

with open('./files/p059_cipher.txt', 'r') as cipher:
  codes = [int(i) for i in cipher.read().split(',')]


text = ''
total = 0
for i in range(len(codes)):
  char = chr(codes[i] ^ key[i%3])
  text += char
  total += ord(char)

print(text)
# 打印的结果包含一些未考虑字符，如引号、方括号等，但好在 key 足够简单
print(total)