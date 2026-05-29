def bin_transfer(num):
    return bin(num)[2:].count('1')
    

def solution(n):
    limit = 1000000
    for i in range(n + 1, limit):
        if bin_transfer(i) == bin_transfer(n):
            return i
