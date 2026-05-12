from collections import Counter
def solution(k, tangerine):
    answer = 0
    num_of_tangerine = sorted(list(Counter(tangerine).values()), reverse=True)
    
    for num in num_of_tangerine:
        if k <= 0:
            break
        k -= num
        answer += 1
        
    return answer