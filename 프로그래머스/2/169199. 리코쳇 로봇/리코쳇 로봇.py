from collections import deque

def solution(board):
    answer = 0
    queue = deque()
    location = {}
    row_size = len(board)
    column_size = len(board[0])
    visited = [[False] * column_size for _ in range(row_size)]
    
    for row in range(row_size):
        for column in range(column_size):
            if board[row][column] == 'R':
                queue.append((row, column, 0))
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        current_x, current_y, current_direction = queue.popleft()
        for i in range(4):
            mx = current_x + dx[i]
            my = current_y + dy[i]
            while 0 <= mx < row_size and 0 <= my < column_size and board[mx][my] != 'D':
                mx += dx[i]
                my += dy[i]
            mx -= dx[i]
            my -= dy[i]
            if board[mx][my] == 'G':
                return current_direction + 1
            if not visited[mx][my]:
                visited[mx][my] = True
                queue.append((mx, my, current_direction + 1))
    return -1
                                
    return answer