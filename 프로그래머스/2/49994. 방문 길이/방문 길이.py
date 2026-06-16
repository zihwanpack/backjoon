def is_valid_location(location):
    if -5 > location[0] or 5 < location[0] or -5 > location[1] or 5 < location[1]:
        return False
    return True

def solution(dirs):
    answer = 0
    current_location = (0, 0)
    move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    dirs_memory = set()
    
    for direction in dirs:
        x, y = current_location
        mx, my = move[direction]
        next_location = (x + mx, y + my)
                
        if is_valid_location(next_location):
            ## 길 기억하기
            dirs_memory.add((current_location, next_location))
            dirs_memory.add((next_location, current_location))
            current_location = next_location
    
    return len(dirs_memory) // 2