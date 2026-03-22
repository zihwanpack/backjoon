from collections import deque

def solution(begin, target, words):
    queue = deque()
    if target not in words:
        return 0
    n = len(begin)
    queue.append([begin, 0])
    visited = [False] * n
    
    while queue:
        curWord, curWordIndex = queue.popleft()
        if curWord == target:
            return curWordIndex
        for word in words:
            count = 0
            for i in range(n):
                if curWord[i] != word[i]:
                    count += 1
            if count == 1:
                queue.append([word, curWordIndex + 1])
    return answer