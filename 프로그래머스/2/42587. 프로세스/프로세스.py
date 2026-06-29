from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    # queue 만들기
    for index, priority in enumerate(priorities):
        queue.append((index, priority))
    
    while queue:
        target_index, tartget_priority = queue.popleft()
        highest_priority = max(q[1] for q in queue) if queue else 0
        
        if highest_priority > tartget_priority:
            queue.append((target_index, tartget_priority))
        
        else:
            answer += 1
            if location == target_index:
                return answer
        
