from collections import deque

def solution(n, computers):
    queue = deque()
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            queue.append(i)
            visited[i] = True
            while queue:
                curComputer = queue.popleft()
                for j in range(n):
                    if computers[curComputer][j] == 1 and not visited[j]:
                        visited[j] = True
                        queue.append(j)
    return answer