def solution(n, lost, reserve):
    answer = 0
    real_lost = sorted(set(lost) - set(reserve))
    real_reserve = sorted(set(reserve) - set(lost))
    
    for man in real_lost:
        if man - 1 in real_reserve:
            real_reserve.remove(man - 1)
        elif man + 1 in real_reserve:
            real_reserve.remove(man + 1)
        else:
            n -= 1
    return n