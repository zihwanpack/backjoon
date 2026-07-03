from math import isqrt

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, isqrt(number) + 1):
        if not number % i:
            return False
    return True

def solution(numbers):
    n = len(numbers)
    visited = [False] * n
    # 소수의 중복을 허락하면 안되니까 집합 사용
    prime_set = set()
    numbers = list(numbers)
    
    def backtrack(number_str):
        # 빈문자열이 아닌 경우
        if number_str:
            # 숫자로 형변환
            number = int(number_str)
            # 소수 검사
            if is_prime(number):
                prime_set.add(number)
        # 한번 조합으로 가능한 모든 수 도달 시 돌아가기
        if len(number_str) == n:
            return
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                backtrack(number_str + numbers[i])
                visited[i] = False
    backtrack('')
    
    return len(prime_set)
                