import sys
input = sys.stdin.readline
N, K = map(int, input().split())
countries = [list(map(int, input().split()))for _ in range(N)]
countries.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

for country in countries:
  if K == country[0]:
    target = country
    break

rank = 1
for country in countries:
  if target[1:] == country[1:]:
    print(rank)
    break
  rank += 1 