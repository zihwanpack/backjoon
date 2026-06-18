# x -> y로 가는 방안을 전부 다 해봐야함 (완전 탐색)
# 하나씩 순차적으로 판단하면서 가는게 좋음 BFS
# 역순으로 계산하는게 더 빠르다.
from collections import deque

def solution(x, y, n):
    answer = -1
    queue = deque()
    # queue에 시작하는 수(거꾸로 역산을 함) y와 계산 횟수를 기록
    queue.append((y, 0))
    visited = set()
    
    while queue:
        # 다음에 갈 경로 저장소
        next_number = []
        cur_number, count = queue.popleft()
        # 완료 조건
        if cur_number == x:
            answer = count
            break
        
        next_number.append(cur_number - n)
        if cur_number % 2 == 0:
            next_number.append(cur_number // 2)
        if cur_number % 3 == 0:
            next_number.append(cur_number // 3)
        for number in next_number:
            if number >= x and number not in visited:
                visited.add(number)
                queue.append((number, count + 1))
    
    return answer