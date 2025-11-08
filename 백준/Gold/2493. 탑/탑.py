import sys
input = sys.stdin.readline

N = int(input())
results = [0] * N
towers = list(map(int, input().split()))
# 단조 스택을 이용하는 것 오름차순, 내림차순을 O(N)에 해결 가능하다.
stack = []
for i in range(N):
  tower = towers[i]

    
  while len(stack):
    # stack top이 현재 타워보다 크거나 같으면 삭제
    if stack[-1][1] <= tower:
      stack.pop()
    else:
      # stack top이 현재 타워보다 작으면 results에 추가
      results[i] = stack[-1][0] + 1
      break
  stack.append([i, tower])

print(" ".join(map(str, results)))