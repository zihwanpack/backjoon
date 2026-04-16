def solution(nums):
    answer = len(nums) // 2
    if len(set(nums)) < answer:
        answer = len(set(nums))
    return answer