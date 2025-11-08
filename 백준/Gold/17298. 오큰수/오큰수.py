import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = [-1] * N

nums = list(map(int, input().split()))

for i in range(N):
  num = nums[i]
  while stack and nums[stack[-1]] < num:
    idx = stack.pop()
    result[idx] = num
  stack.append(i)

print(" ".join(map(str, result)))