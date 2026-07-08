def solution(name):
    answer = 0
    n = len(name)
    min_move = n - 1
    
    for index, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        
        # 이동하기
        next_index = index + 1
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        
        min_move = min(min_move, 
                       index + index + n - next_index, 
                       (n - next_index) + (n - next_index) + index)
    
    return answer + min_move