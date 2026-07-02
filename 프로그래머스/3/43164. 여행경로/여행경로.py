def solution(tickets):
    answer = []
    n = len(tickets)
    visited = [False] * n
    tickets.sort()
    
    def dfs(current_airport, routes):
        if len(routes) == n + 1:
            return routes
        for i in range(n):
            if current_airport == tickets[i][0] and not visited[i]:
                visited[i] = True
                result = dfs(tickets[i][1], routes + [tickets[i][1]])
                # 탐색 끝냈는데 모든 경로가 있을 때
                if result:
                    return result
                # 실패하면 백트래킹
                visited[i] = False
        return None
    return dfs("ICN", ["ICN"])