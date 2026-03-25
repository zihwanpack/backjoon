def solution(answers):
    result = []
    first_man = [1, 2, 3, 4, 5] 
    second_man = [2, 1, 2, 3, 2, 4, 2, 5]
    third_man = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count_of_answer = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == first_man[i % len(first_man)]:
            count_of_answer[0] += 1
        if answers[i] == second_man[i % len(second_man)]:
            count_of_answer[1] += 1
        if answers[i] == third_man[i % len(third_man)]:
            count_of_answer[2] += 1
    max_answer = max(count_of_answer)
    for i in range(len(count_of_answer)):
        if count_of_answer[i] == max_answer:
            result.append(i + 1)
            
        
    return result