def solution(routes):
    answer = 1
    routes.sort(key=lambda x : x[1])
    N = len(routes)
    last_camera = routes[0][1]
    for i in range(1, N):
        if last_camera < routes[i][0]:
            answer += 1
            last_camera = routes[i][1]
        
    return answer