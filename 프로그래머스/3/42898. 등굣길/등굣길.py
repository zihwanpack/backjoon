def solution(m, n, puddles):
    answer = 0
    dp = [[-1] * m for _ in range(n)]
    
    def get_shortest_path(current_x, current_y):
        # 경계선 체크
        if current_x > n - 1 or current_y > m - 1:
            return 0
        
        # 물웅덩이일 때
        if [current_y + 1, current_x + 1] in puddles:
            return 0
        
        if current_x == n - 1 and current_y == m - 1:
            return 1
        
        # 메모이제이션
        if dp[current_x][current_y] != -1:
            return dp[current_x][current_y]
        
        dp[current_x][current_y] = (get_shortest_path(current_x + 1, current_y) + get_shortest_path(current_x, current_y + 1)) % 1000000007
        
        return dp[current_x][current_y]
    answer = get_shortest_path(0, 0)
    
    return answer