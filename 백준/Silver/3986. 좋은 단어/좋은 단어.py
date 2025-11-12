import sys
input = sys.stdin.readline


N = int(input())
result = 0

for _ in range(N):
  word = input().rstrip()
  stack = []
  for string in word:
    if stack and stack[-1] == string:
      stack.pop()
      is_good_word = True
    else:
      stack.append(string)
  if not stack:
    result += 1
print(result)