def solution(sizes):
    answer = 0
    max_x = 0
    max_y = 0
    for size in sizes:
        x = max(size)
        y = min(size)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    return max_x * max_y