def solution(s):
    stack = []
    for char in s:
        if char == ')' and stack and stack[-1] == '(':
            stack.pop()
        else: 
            stack.append(char)
    answer =  not bool(len(stack))
    return answer