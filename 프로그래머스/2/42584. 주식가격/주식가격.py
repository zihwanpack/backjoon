from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        time = 0
        cost = queue.popleft()
        for after_price in queue:
            time += 1
            if after_price < cost:
                break
        answer.append(time)
    return answer