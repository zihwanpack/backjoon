import sys
input = sys.stdin.readline


result = []
while True:
  line = input().rstrip()  
  if line == '.':
    break
  stack = []
  is_balanced = True
  for char in line:
    if char == '[' or char == '(':
      stack.append(char)
    elif char == ')':
      if not stack or stack[-1] != '(':
        is_balanced = False
        break
      stack.pop()
    elif char == ']':
      if not stack or stack[-1] != '[':
        is_balanced = False
        break
      stack.pop()
  if is_balanced == True and not stack:
    result.append('yes')
  else:
    result.append('no')

print('\n'.join(result))




  