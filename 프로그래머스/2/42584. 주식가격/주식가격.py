# 단조스택 풀이
def solution(prices):
    N = len(prices)
    answer = [0] * N
    stack = []
    
    for index in range(N):
        price = prices[index]
        while stack and prices[stack[-1]] > price:
            past_index = stack.pop()
            answer[past_index] = index - past_index
        stack.append(index)
    while stack:
        past_index = stack.pop()
        answer[past_index] = N - 1 - past_index
    return answer