from math import gcd

def is_condition(first_array, second_array):
    current_gcd = gcd(*first_array)
    
    if current_gcd == 1:
        return 0
    for number in second_array:
        if number % current_gcd == 0:
            return 0
        
    return current_gcd

def solution(arrayA, arrayB):
    answer = 0
    result_A = is_condition(arrayA, arrayB)
    result_B = is_condition(arrayB, arrayA)
    answer = max(result_A, result_B)
    return answer