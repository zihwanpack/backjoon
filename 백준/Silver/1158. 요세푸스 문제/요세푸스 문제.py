import sys
from collections import deque

answer = []
N, K = map(int,sys.stdin.readline().split())
queue = deque(range(1, N + 1))


while queue:
    for _ in range(K - 1):
        # 빼야할 값 맨 왼쪽으로 빼놓기
        queue.append(queue.popleft())
    # 값 빼서 answer에 넣기
    answer.append(queue.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))

