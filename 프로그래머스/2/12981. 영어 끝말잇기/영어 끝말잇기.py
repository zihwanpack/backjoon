import math
def solution(n, words):
    answer = []
    
    ## 집합 초기화
    used_word = {words[0]}
    
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        target_index = i + 2
        
        if word[-1] != next_word[0] or next_word in used_word:
            person_num = target_index % n
            if person_num == 0:
                person_num = n
            turn = math.ceil(target_index / n)
            return [person_num, turn]
        
        used_word.add(next_word)
    return [0, 0]