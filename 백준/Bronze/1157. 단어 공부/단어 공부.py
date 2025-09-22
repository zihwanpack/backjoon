import sys
# 개행문자 제거
word = sys.stdin.readline().strip().lower()
lst = [0] * 26

for char in word:
  lst[ord(char) - ord('a')] += 1

maxNumber = max(lst)
if (lst.count(maxNumber) > 1):
  print('?')
else:
  print(chr(lst.index(maxNumber) + ord('A'))) 