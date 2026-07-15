def solution(sequence, k):
    answer = []
    answer_candidate = []
    start_p, end_p = 0, 0
    current_sum = 0
    n = len(sequence)
    
    while start_p <= end_p:
        if current_sum < k:
            if end_p >= n:
                break
            current_sum += sequence[end_p]
            end_p += 1
        elif current_sum > k:
            current_sum -= sequence[start_p]
            start_p += 1
        else:
            length = (end_p - 1) - start_p
            answer_candidate.append((start_p, end_p - 1, length))
            
            current_sum -= sequence[start_p]
            start_p += 1
    answer_candidate.sort(key=lambda x: x[2])
    return [answer_candidate[0][0], answer_candidate[0][1]]
                                    
    return answer