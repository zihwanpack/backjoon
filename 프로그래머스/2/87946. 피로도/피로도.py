def backtracking(answer, k, count, visited, dungeons):
    # answer를 계속 갱신해주기
    answer = max(answer, count)
    n = len(dungeons)
    
    for i in range(n):
        limit, cost = dungeons[i]
        # 방문하지 않았고 k가 limit보다 크거나 같으면 count 처리
        if not visited[i] and limit <= k:
            visited[i] = True
            answer = backtracking(answer, k - cost, count + 1, visited, dungeons)
            visited[i] = False
    return answer
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visited = [False] * n
    count = 0
    
    answer = backtracking(answer, k, count, visited, dungeons)
    
    return answer