import sys
input = sys.stdin.readline

N = int(input())

stack = []
numbers = [int(input()) for _ in range(N)]
result = []
current = 1
is_impossible = False

for number in numbers:
  if current <= number:
    while current <= number:
      stack.append(current)
      current += 1
      result.append('+')
    stack.pop()
    result.append('-')
  elif stack[-1] == number:
    stack.pop()
    result.append('-')
  else:
    is_impossible = True
    break

if is_impossible:
  print('NO')
else:
  print('\n'.join(result))
