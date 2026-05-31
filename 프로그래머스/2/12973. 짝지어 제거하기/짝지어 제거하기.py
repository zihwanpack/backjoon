def solution(s):
    answer = 0
    stack = []
    for alphabet in s:
        if not stack or stack[-1] != alphabet:
            stack.append(alphabet)
        else:
            stack.pop()
    
    if not stack:
        answer = 1
    return answer