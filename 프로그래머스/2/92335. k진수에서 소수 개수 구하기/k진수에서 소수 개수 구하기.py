import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def convert_k_base(number, k):
    k_base_str = ''
    while number > 0:
        number, remainder = divmod(number, k)
        k_base_str = str(remainder) + k_base_str
    return k_base_str
        

def solution(n, k):
    answer = 0
    converted_numbers = convert_k_base(n, k).split('0')
    for converted_number in converted_numbers:
        if converted_number != "": 
            if is_prime(int(converted_number)):
                answer += 1
    return answer