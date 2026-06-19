    

def quad_compress(arr, row_index, col_index, N, answer):
    # 시작 숫자 (시작점 좌표)
    init_number = arr[row_index][col_index]
    
    for row in range(row_index, row_index + N):
        for col in range(col_index, col_index + N):
            if arr[row][col] != init_number:
                # 재귀적으로 간다.
                half = N // 2
                quad_compress(arr, row_index, col_index, half, answer)
                quad_compress(arr, row_index, col_index + half, half, answer)
                quad_compress(arr, row_index + half, col_index, half, answer)
                quad_compress(arr, row_index + half, col_index + half, half, answer)
                return
    answer[init_number] += 1
    

def solution(arr):
    answer = [0, 0]
    N = len(arr[0])    
    quad_compress(arr, 0, 0, N, answer)

    return answer