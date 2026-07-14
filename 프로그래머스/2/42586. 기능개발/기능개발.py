from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    # 배포일 계산
    for index, current_progress in enumerate(progresses):
        current_speed = speeds[index]
        time = (100 - current_progress) // current_speed
        if (100 - current_progress) % current_speed:
            time += 1
        queue.append(time)
    
    while queue:
        target = queue.popleft()
        count = 1
        while queue and queue[0] <= target:
            count += 1
            queue.popleft()
        answer.append(count)
    return answer