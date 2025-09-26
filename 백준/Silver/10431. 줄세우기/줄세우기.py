import sys
input = sys.stdin.readline


N = int(input())
for _ in range(N):
  answer = 0  
  cases = list(map(int, input().split()))
  caseNum = cases[0]
  heights = cases[1:]
  for i in range (0, len(cases) - 1):
    for j in range (i + 1, len(cases) - 1):
      if heights[i] > heights[j]:
        heights[i], heights[j] = heights[j], heights[i]
        answer += 1
  print(caseNum, answer)

        




