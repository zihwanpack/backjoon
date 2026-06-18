def solution(order):
    answer = 0
    main_box = 1
    stack = []
    n = len(order)
    
    for target_box in order:
        while main_box < target_box and main_box <= n:
            stack.append(main_box)
            main_box += 1
        if main_box == target_box:
            main_box += 1
            answer += 1
        elif stack[-1] == target_box:
            stack.pop()
            answer += 1
        else:
            break
            
    return answer