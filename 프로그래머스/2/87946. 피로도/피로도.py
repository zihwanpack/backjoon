from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons):
        count = 0
        current_health = k
        for limit, damage in p:
            if limit <= current_health:
                current_health -= damage
                count += 1
            else:
                break
        answer = max(count, answer)
    return answer