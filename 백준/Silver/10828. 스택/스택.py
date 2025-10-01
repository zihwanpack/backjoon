import sys
input = sys.stdin.readline

N = int(input())

commands = [input().split() for _ in range(N)]
stack = []

for command in commands:
  if command[0] == 'push':
    value = command[1]
    stack.append(value)
  elif command[0] == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  elif command[0] == 'size':
    print(len(stack))
  elif command[0] == 'empty':
    print(1) if len(stack) == 0 else print(0)
  elif command[0] == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])