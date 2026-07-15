from collections import Counter

def solution(participant, completion):
    answer = ''
    diff = Counter(participant) - Counter(completion)
    return list(diff.keys())[0]