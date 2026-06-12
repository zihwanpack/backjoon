def count_toppings(topping):
    topping_counts = {}
    for t in topping:
        if t not in topping_counts:
            topping_counts[t] = 1 
        else:
            topping_counts[t] += 1
    return topping_counts

def solution(topping):
    answer = 0
    
    # left는 왼쪽 조각(철수)의 토핑 종류를 담을 세트
    # right는 오른쪽 조각(동생)의 토핑과 남은 개수를 담을 딕셔너리
    left_piece = set()
    right_piece = count_toppings(topping)
    
    for t in topping:
        # 1. 오른쪽 조각에서 토핑 하나를 빼서 왼쪽 조각에 주기
        right_piece[t] -= 1
        if right_piece[t] == 0:
            del right_piece[t]
            
        left_piece.add(t)
        
        # 2. 양쪽의 토핑 수 같은지 비교
        if len(left_piece) == len(right_piece):
            answer += 1
        
    return answer