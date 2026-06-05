def is_valid(s):
    correct = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for parentheses in s:
        if parentheses in correct:
            stack.append(parentheses)
        else:
            if not stack:
                return False
            top_parentheses = stack.pop()
            if correct[top_parentheses] != parentheses:
                return False
    return len(stack) == 0
        

def solution(s):
    answer = 0
    n = len(s)
    if n % 2 == 1:
        return 0
    for i in range(n):
        if is_valid(s):
            answer += 1
        s = s[1:] + s[:1]
    return answer
    
    
    return answer