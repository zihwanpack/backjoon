import sys
input = sys.stdin.readline


N, X = map(int, input().split())

visitors = list(map(int, input().split()))

current_sum = sum(visitors[:X])
answer = current_sum
count = 1

for i in range(X, N):
  current_sum += visitors[i]
  current_sum -= visitors[i - X]
  if current_sum > answer:
    answer = current_sum
    count = 1
  elif current_sum == answer:
    count += 1

if sum(visitors) == 0:
  print('SAD')
else:
  print(answer)
  print(count)
