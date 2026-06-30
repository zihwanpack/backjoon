from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append((0, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            moving_x = dx[i] + current_x
            moving_y = dy[i] + current_y
            # 게임 맵 벗어나는지 체크
            if moving_x < 0 or moving_x >= n or moving_y < 0 or moving_y >= m:
                continue
            # 갈 수 있는 길 체크
            if maps[moving_x][moving_y] == 1:
                # 거리로 값 써버리기
                maps[moving_x][moving_y] = maps[current_x][current_y] + 1
                queue.append((moving_x, moving_y))
    if maps[n-1][m-1] == 1:
        return -1

    return maps[n-1][m-1]
        
