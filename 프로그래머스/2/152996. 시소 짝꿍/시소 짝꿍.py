from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    sorted_counter = sorted(counter.keys())
    
    ratios = [4/2, 3/2, 4/3]
    
    for weight in sorted_counter:
        counts_of_weight = counter[weight]
        
        # 1. 같은 몸무게끼리 
        if counts_of_weight > 1:
            answer += (counts_of_weight * (counts_of_weight - 1)) // 2
            
        # 2. 비율이 맞는 다른 몸무게끼리
        for ratio in ratios:
            target_weight = weight * ratio
            if target_weight in counter:
                answer += counts_of_weight * counter[target_weight]
            
    return answer