import sys, math

N, K = map(int, sys.stdin.readline().split())
mArr = [0] * 6
wArr = [0] * 6
answer = 0

for _ in range(N):
  S, Y = map(int, sys.stdin.readline().split())
  if (S == 0):
    wArr[Y - 1] += 1
  elif (S == 1):
    mArr[Y - 1] += 1
for w in wArr:
  if w > 0:
    answer += math.ceil(w / K)

for m in mArr:
  if m > 0:
    answer += math.ceil(m / K)

print(answer)