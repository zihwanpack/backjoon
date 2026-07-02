from collections import deque

# field 그리기 함수
def get_field(rectangle):
    # 선타기 문제이기 때문에 주어진 좌표평면의 2배로 잡아야함
    field = [[0] * 102 for _ in range(102)]    
    
    # 실제 field 그리기
    for rect in rectangle:
        x1, y1, x2, y2 = rect[0] * 2, rect[1] * 2, rect[2] * 2, rect[3] * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                field[i][j] = 1
    # 외곽선만 뽑아내기
    for rect in rectangle:
        x1, y1, x2, y2 = rect[0] * 2, rect[1] * 2, rect[2] * 2, rect[3] * 2
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                field[i][j] = 0
                
    return field
    
def bfs(field, start_x, start_y, target_x, target_y):
    queue = deque()
    visited = [[False] * 102 for _ in range(102)]
    
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        current_x, current_y, count = queue.popleft()
        # 탈출 조건
        if current_x == target_x and current_y == target_y:
            return count // 2
        for i in range(4):
            mx = current_x + dx[i]
            my = current_y + dy[i]
            if mx < 0 or 102 <= mx or mx < 0 or 102 <= mx:
                continue
            if field[mx][my] == 1 and not visited[mx][my]:
                visited[mx][my] = True
                queue.append((mx, my, count + 1))
        


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 2배로 초기화
    start_x, start_y, target_x, target_y = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    
    field = get_field(rectangle)
    answer = bfs(field, start_x, start_y, target_x, target_y)
    
    return answer