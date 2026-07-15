def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    x, y = 0, 0
    direction = 0
    current_number = 1
    total_number = sum(range(1, n + 1))
    
    while current_number <= total_number:
        answer[x][y] = current_number
        current_number += 1
        mx, my = x + dx[direction], y + dy[direction]
        
        if 0 <= mx < n and 0 <= my <= mx and answer[mx][my] == 0:
            x, y = mx, my
        else:
            direction = (direction + 1) % 3
            x += dx[direction]
            y += dy[direction]
            
    return [val for row in answer for val in row]