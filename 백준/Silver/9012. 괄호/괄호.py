import sys
input = sys.stdin.readline 

N = int(input())
results = []

for _ in range(N):
  data = input().rstrip()
  stack = []
  is_valid = True
  
  for char in data:
    if char == '(':
      stack.append(char)
      
    elif char == ')':
      if not stack:
        is_valid = False
        break
      else:
        stack.pop()
        
        
  if is_valid and not stack:
    results.append('YES')
  else:
    results.append('NO')

print('\n'.join(results))