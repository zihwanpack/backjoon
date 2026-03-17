from collections import deque
def solution(numbers, target):
    queue = deque()
    answer = 0
    numbersLength = len(numbers)
    # 초기 진행
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    while queue:
        currentNumber, index = queue.popleft()
        # 다음 거 보기
        index += 1
        if index < numbersLength:
            queue.append([currentNumber + numbers[index], index])
            queue.append([currentNumber - numbers[index], index])
        else:
            if currentNumber == target:
                answer += 1
    
    return answer