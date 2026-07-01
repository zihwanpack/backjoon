from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    # 시작, 레버, 끝 좌표 계산
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
                
    def bfs(start_cor, destination_cor):
        queue = deque()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[False] * m for _ in range(n)]
        start_cor_x, start_cor_y = start_cor
        queue.append((start_cor_x, start_cor_y, 0))
        visited[start_cor_x][start_cor_y] = True
        
        while queue:
            current_x, current_y, time = queue.popleft()
            if (current_x, current_y) == destination_cor:
                return time
            # 테두리 체크
            for i in range(4):
                mx = current_x + dx[i]
                my = current_y + dy[i]
                if mx < 0 or mx >= n or my < 0 or my >= m:
                    continue
                    
                if not visited[mx][my] and maps[mx][my] != 'X':
                    visited[mx][my] = True
                    queue.append((mx, my, time + 1))
        return -1
                    
    lever_time = bfs(start, lever)
    end_time = bfs(lever, end)
    
    if lever_time == -1 or end_time == -1:
        answer = -1
    else:
        answer = lever_time + end_time
        
    return answer