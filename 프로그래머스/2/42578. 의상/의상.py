def solution(clothes):
    answer = 1
    dictionary = {}
    
    # 의상 종류별로 세기
    for name, category in clothes:
        if category in dictionary:
            dictionary[category] += 1
        else:
            dictionary[category] = 1
    
    # 조합 계산
    for count in dictionary.values():
        answer *= (count + 1)
            
    return answer - 1