def solution(arr):
    stack = []
    
    for number in arr:
        if stack and stack[-1] == number:
            continue
        else:
            stack.append(number)
    
    return stack