import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = 0 

concierges = [int(input()) for _ in range(N)]
for i in range(N):
  cur_concierge = concierges[i]

  while stack and cur_concierge >= stack[-1]:
    stack.pop()
      

  result += len(stack)
  stack.append(cur_concierge)

print(result)