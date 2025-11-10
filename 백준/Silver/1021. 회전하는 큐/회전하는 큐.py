import sys
from collections import deque 

input = sys.stdin.readline

N, M = map(int, input().strip().split())
target_nums = list(map(int, input().split()))

result = 0
dequeue = deque([i + 1 for i in range(N)])


for num in target_nums:
  num_idx = dequeue.index(num)
  middle_idx = len(dequeue) // 2

  if num_idx <= middle_idx:
    for _ in range(num_idx):
      result += 1
      dequeue.append(dequeue.popleft())
  else:
    for _ in range(len(dequeue) - num_idx):
      result += 1
      dequeue.appendleft(dequeue.pop())

  dequeue.popleft()
  
print(result)