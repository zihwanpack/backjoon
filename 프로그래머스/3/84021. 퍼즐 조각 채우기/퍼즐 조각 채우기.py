from collections import deque

def rotate_90_degree(matrix):
    transposed = list(map(list, zip(*matrix[::-1])))
    return transposed

def return_to_zero(piece):
    min_x = min([p[0] for p in piece])
    min_y = min([(p[1]) for p in piece])
    
    return sorted([(x - min_x, y - min_y) for x, y in piece])
    

def bfs(board, target_value):
    N = len(board)
    visited = [[False] * N for _ in range(N)]
    all_pieces = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(N):
        for j in range(N) :
            if not visited[i][j] and board[i][j] == target_value:
                queue = deque()
                # 시작점 큐에 넣기 
                queue.append((i, j))
                visited[i][j] = True
                current_piece = [(i, j)]
                
                while queue:
                    cx, cy = queue.popleft()
                    for k in range(4):
                        mx = cx + dx[k]
                        my = cy + dy[k]
                        if 0 <= mx < N and 0 <= my < N:
                            if not visited[mx][my] and board[mx][my] == target_value:
                                queue.append((mx, my))
                                visited[mx][my] = True
                                current_piece.append((mx, my))
                returned_piece = return_to_zero(current_piece)
                all_pieces.append(returned_piece)
        
    return all_pieces

def solution(game_board, table):
    answer = 0
    spaces = bfs(game_board, 0)
    pieces = bfs(table, 1)
    used_pieces = [False] * len(pieces)
    
    for space in spaces:
        is_match = False
        
        for i in range(len(pieces)):
            if used_pieces[i]:
                continue
            current_piece = pieces[i][:]
            for _ in range(4):
                if space == current_piece:
                    answer += len(current_piece)
                    used_pieces[i] = True
                    is_match = True
                    break
                rotated = [(-y, x) for x, y in current_piece]
                current_piece = return_to_zero(rotated)
            if is_match:
                break 
    return answer