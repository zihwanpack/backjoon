from collections import deque

def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * (columns + 1) for _ in range(rows + 1)]
    number = 1
    
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = number
            number += 1
    
    for query in queries:
        queue = deque()
        start_x, start_y, end_x, end_y = query
        
        # 윗변 (좌 -> 우)
        for my in range(start_y, end_y):
            queue.append(matrix[start_x][my])
        # 우변 (위 -> 아래)
        for mx in range(start_x, end_x):
            queue.append(matrix[mx][end_y])
        # 밑변 (우 -> 좌)
        for my in range(end_y, start_y, -1):
            queue.append(matrix[end_x][my])
        # 좌변 (아래 -> 위)
        for mx in range(end_x, start_x, -1):
            queue.append(matrix[mx][start_y])
        
        answer.append(min(queue))
        # 오른쪽으로 한번 회전
        queue.rotate(1)
        # 돌아간 값 넣기
        # 윗변 (좌 -> 우)
        for my in range(start_y, end_y):
            matrix[start_x][my] = queue.popleft()
        # 우변 (위 -> 아래)
        for mx in range(start_x, end_x):
            matrix[mx][end_y] = queue.popleft()
        # 밑변 (우 -> 좌)
        for my in range(end_y, start_y, -1):
            matrix[end_x][my] = queue.popleft()            
        # 좌변 (아래 -> 위)
        for mx in range(end_x, start_x, -1):
            matrix[mx][start_y] = queue.popleft()            
        
    
    return answer