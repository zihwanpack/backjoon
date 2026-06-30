from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0, 1))
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        current_x, current_y, current_dist = queue.popleft()
        
        if current_x == n - 1 and current_y == m - 1:
            return current_dist
        
        for i in range(4):
            moving_x = current_x + dx[i]
            moving_y = current_y + dy[i]
            
            if moving_x < 0 or moving_x >= n or moving_y < 0 or moving_y >= m:
                continue
                
            if maps[moving_x][moving_y] == 1 and not visited[moving_x][moving_y]:
                visited[moving_x][moving_y] = True
                queue.append((moving_x, moving_y, current_dist + 1))
                
    return -1