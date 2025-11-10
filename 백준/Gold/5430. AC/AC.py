import sys
from collections import deque 

input = sys.stdin.readline

T = int(input())

results = []
for _ in range(T):
  commands = input().strip()
  n = int(input())
  arr_str = input().strip()
  if arr_str == '[]':
    dq = deque()
  else:
    dq = deque(list(map(int, arr_str.strip('[]').split(','))))

  is_reverse = False
  is_error = False     
  for command in commands:
    if command == 'R':
      is_reverse = not is_reverse
    elif command == 'D':
      if len(dq) == 0:
        is_error = True
        results.append('error')
        break
      else:
        if is_reverse:
          dq.pop()
        else:
          dq.popleft()
  if is_error == False:
    if is_reverse:
      dq.reverse()
    results.append('[' + ','.join(map(str, dq)) +']')

for result in results:
  print(result)