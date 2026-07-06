def backtracking(chess_board, current_row, queen_count, board_size):
    # 종료 조건
    if current_row == board_size:
        return queen_count + 1
    
    for current_column in range(board_size):
        # 일단 퀸 두기
        chess_board[current_row] = current_column
        is_safe = True
        # 행 순회 지난 행의 열과 겹치는지 여부 검증하기
        for prev_row in range(current_row):
            prev_column = chess_board[prev_row]
            if prev_column == current_column or (abs(current_row - prev_row) == abs(current_column - prev_column)):
                is_safe = False
                break
        if is_safe:
            queen_count = backtracking(chess_board, current_row + 1, queen_count, board_size)
    return queen_count
def solution(n):
    answer = 0
    chess_board = [0] * n
    current_row = 0
    queen_count = 0
    answer = backtracking(chess_board, current_row, queen_count, n)
    
    return answer