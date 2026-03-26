import math
from itertools import permutations

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True
def get_all_numbers(string_numbers):
    every_numbers = set()
    for i in range(1, len(string_numbers) + 1):
        tuples = permutations(string_numbers, i)
        for permutation in tuples:
            number = int("".join(permutation))
            every_numbers.add(number)
    return every_numbers
        

    
def solution(string_numbers):
    answer = 0
    parsed_numbers = get_all_numbers(string_numbers)
    
    for n in parsed_numbers:
        if is_prime(n):
            answer += 1
    
    return answer