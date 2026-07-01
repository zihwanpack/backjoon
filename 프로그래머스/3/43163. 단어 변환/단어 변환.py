from collections import deque
        
def solution(begin, target, words):
    answer = 0
    # 반환 가능 여부 검증
    if target not in words:
        return 0
    
    n = len(words)
    queue = deque()
    visited = [False] * n
    # 변환 횟수 저장을 위해 튜플로 저장
    queue.append((begin, 0))
    
    while queue:
        current_word, count = queue.popleft()
        
        if current_word == target:
            return count
        
        for i in range(n):
            # 미방문 단어 처리
            if not visited[i]:
                different_count = 0
                for j in range(len(current_word)):
                    if current_word[j] != words[i][j]:
                        different_count += 1
                if different_count == 1:
                    visited[i] = True
                    queue.append((words[i], count + 1))

    return answer