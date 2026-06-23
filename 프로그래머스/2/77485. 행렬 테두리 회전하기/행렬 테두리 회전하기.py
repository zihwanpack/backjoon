from collections import deque

def solution(rows, columns, queries):
    answer = []
   # 가로세로를 1씩 늘린 격자판 만들기
    matrix = [[0] * (columns + 1) for _ in range(rows + 1)]

    # 1부터 시작하는 인덱스에 맞게 값 채우기
    num = 1
    for r in range(1, rows + 1):
        for c in range(1, columns + 1):
            matrix[r][c] = num
            num += 1
    
    for query in queries:
        r1, c1, r2, c2 = query[0], query[1], query[2], query[3]
        temp_arr = []
        # 위쪽 변 좌우로 진행
        for c in range(c1, c2):
            temp_arr.append(matrix[r1][c])
        # 오른쪽 변 상하로 진행
        for r in range(r1, r2):
            temp_arr.append(matrix[r][c2])
        # 아래쪽 변 우좌로 진행
        for c in range(c2, c1, -1):
            temp_arr.append(matrix[r2][c])
        # 왼쪽 변 하상으로 진행
        for r in range(r2, r1, -1):
            temp_arr.append(matrix[r][c1])
        
        answer.append(min(temp_arr))
        
        curr_deck = deque(temp_arr)
        curr_deck.rotate(1)
            
        idx = 0
        
        # 위쪽 변 다시 채우기
        for c in range(c1, c2):
            matrix[r1][c] = curr_deck[idx]
            idx += 1
            
        # 오른쪽 변 다시 채우기
        for r in range(r1, r2):
            matrix[r][c2] = curr_deck[idx]
            idx += 1
            
        # 아래쪽 변 다시 채우기
        for c in range(c2, c1, -1):
            matrix[r2][c] = curr_deck[idx]
            idx += 1
            
        # 왼쪽 변 다시 채우기
        for r in range(r2, r1, -1):
            matrix[r][c1] = curr_deck[idx]
            idx += 1
    
    return answer