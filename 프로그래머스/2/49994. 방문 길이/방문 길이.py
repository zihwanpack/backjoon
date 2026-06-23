
def is_valid_location(next_location):
    x, y = next_location
    if abs(x) > 5 or abs(y) > 5:
        return False
    return True    

def solution(dirs):
    answer = 0
    move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    # list 함수 사용해 배열로 변환
    directions = list(dirs)
    moving_record = set()
    # 현재 위치 기록용 튜플
    current_location = (0, 0)
    
    for direction in directions:
        cur_x, cur_y = current_location
        move_x, move_y = move[direction]
        next_location = (cur_x + move_x, cur_y + move_y)
        
        if is_valid_location(next_location):
            moving_record.add((current_location, next_location))
            moving_record.add((next_location, current_location))
            current_location = next_location
            
    return len(moving_record) // 2