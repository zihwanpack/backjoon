def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(current_idx, current_number):
        # dfs의 탈출 조건 명시
        nonlocal answer
        if current_idx == n:
            if current_number == target:
                answer += 1
            return 
        dfs(current_idx + 1, current_number + numbers[current_idx])
        dfs(current_idx + 1, current_number - numbers[current_idx])
        
    dfs(0, 0)
    
    return answer