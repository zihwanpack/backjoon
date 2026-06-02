def solution(elements):
    ## 원형 수열의 경우 * 2해서 처리해도 간으
    extends_elements = elements * 2
    results = set()
    
    for i in range(1, len(elements) + 1):
        for start in range(len(elements)):
            result = sum(extends_elements[start : start + i])
            results.add(result)
            
    
    return len(results)