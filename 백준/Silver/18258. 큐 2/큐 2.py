import sys
from collections import deque 

input = sys.stdin.readline
N = int(input())
queue = deque() 
results = []

for _ in range(N):
  command = input().split() 
  
  com = command[0]
  
  if com == 'push':
    queue.append(command[1]) 
    
  elif com == 'pop':
    if queue:
      results.append(queue.popleft()) 
    else:
      results.append("-1")
      
  elif com == 'size':
    results.append(str(len(queue)))
    
  elif com == 'empty': 
    if queue:
      results.append("0")
    else:
      results.append("1")
      
  elif com == 'front':
    if queue:
      results.append(queue[0])
    else:
      results.append("-1")
      
  elif com == 'back': 
    if queue:
      results.append(queue[-1])  
    else:
      results.append("-1")

print('\n'.join(results))