def solution(storey):
    answer = 0
    # 그리디 문제임
    while storey > 0:
        digit = storey % 10
        next_digit = (storey // 10) % 10
        
        if digit > 5:
            storey += 10
            answer += (10 - digit)
        elif digit < 5:
            answer += digit
        # 첫자리가 5일 떄
        else:
            answer += 5
            if next_digit >= 5:
                storey += 10
        storey //= 10
    
    return answer