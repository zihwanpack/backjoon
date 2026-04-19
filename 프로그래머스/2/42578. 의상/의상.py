def solution(clothes):
    answer = 1
    hash = {}
    for name, kind in clothes:
        hash[kind] = hash.get(kind, 0) + 1
    for count in hash.values():
        answer *= (count + 1)
    
            
    return answer - 1