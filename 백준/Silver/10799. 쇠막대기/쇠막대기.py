import sys

# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline 

data = input()
stack = []
result = 0

for  i  in range(len(data)):
  if data[i] == '(':
    stack.append(data[i])    
  elif data[i] == ')':
    stack.pop()
    if data[i - 1] == '(':
      result += len(stack)
    else:
      result += 1

print(result)

