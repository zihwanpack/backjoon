import sys
sys.setrecursionlimit(10 ** 6)

def solution(n):
    answer = 0
    if n < 3:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    def fib(n):
        if dp[n] != 0:
            return dp[n]
        dp[n] = (fib(n - 1) + fib(n - 2)) % 1000000007
        return dp[n]
    
    return fib(n)