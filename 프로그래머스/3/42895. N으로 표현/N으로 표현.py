def solution(N, number):
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
        for j in range(1, i):
            for operand1 in dp[j]:
                for operand2 in dp[i - j]:
                    dp[i].add(operand1 + operand2)
                    dp[i].add(operand1 - operand2)
                    dp[i].add(operand1 * operand2)
                    if operand2 != 0:
                        dp[i].add(operand1 // operand2)
                        
        if number in dp[i]:
            return i
            
    return -1