import sys
from collections import deque 

input = sys.stdin.readline
N = int(input())
queue = deque([i + 1 for i in range(N)])

while len(queue) > 1:
  queue.popleft()
  if queue:
    queue.append(queue.popleft())

print(queue[0])



