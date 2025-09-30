import sys
input = sys.stdin.readline

N = int(input())
dataList = [list(map(int, input().split())) for _ in range(N)]
result = []

for i in range(N):
  rank = 1
  for j in range(N):
    if i != j:
      if dataList[i][0] < dataList[j][0] and dataList[i][1] < dataList[j][1]:
        rank += 1
  result.append(rank)

print(*result)