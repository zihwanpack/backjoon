def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = [[-1] * N for _ in range(N)]
    
    def get_max_sum(current_x, current_y):
        if current_x == N - 1:
            return triangle[current_x][current_y]
        if dp[current_x][current_y] != -1:
            return dp[current_x][current_y]
        dp[current_x][current_y] = triangle[current_x][current_y] + max(get_max_sum(current_x + 1, current_y), get_max_sum(current_x + 1, current_y + 1))
        return dp[current_x][current_y]
    
    answer = get_max_sum(0, 0)
    return answer