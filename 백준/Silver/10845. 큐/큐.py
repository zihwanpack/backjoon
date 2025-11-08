import sys
input = sys.stdin.readline

N = int(input())
queue = []
commands = [input().split() for _ in range(N)]

for command in commands:
  com = command[0]
  if com == 'push':
    queue.append(command[1])
  elif com == 'pop':
    if queue:
      print(queue.pop(0))
    else:
      print(-1)
  elif com == 'size':
    print(len(queue))
  elif com == 'empty': 
    if queue:
      print(0)
    else:
      print(1)
  elif com == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif com == 'back': 
    if queue:
      print(queue[-1])  
    else:
      print(-1)
