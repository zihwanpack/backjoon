from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(index, priority) for index, priority in enumerate(priorities)])
    
    while queue:
        index, current_priority = queue.popleft()
        
        has_higher_priority = False
        
        for process in queue:
            if process[1] > current_priority:
                has_higher_priority = True
                break 
        
        if has_higher_priority:
            queue.append((index, current_priority))
        else:
            answer += 1
            if index == location:
                return answer