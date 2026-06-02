def solution(elements):
    answer = 0
    elements_arr = elements * 2
    results = set()
    
    for num in range(1, len(elements) + 1):
        for start in range(len(elements)):
            sub_result = sum(elements_arr[start : start + num])
            results.add(sub_result)
            
    return len(results)