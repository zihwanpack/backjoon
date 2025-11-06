import sys
input = sys.stdin.readline

# 이진 탐색으로 0부터 찾기
def find_answer (budgets, limit):
  # 예외 처리
  if sum(budgets) <= limit:
    return max(budgets)
  start = 0
  end = max(budgets)
  answer = 0
  while start <= end:
    mid = (start + end) // 2
    total_budget = 0
    for budget in budgets:
      if budget > mid:
        total_budget += mid
      else:
        total_budget += budget
    if total_budget <= limit:
      answer = mid
      start = mid + 1
    else:
      end = mid - 1
  return answer
        


N = int(input())
budgets = list(map(int, input().split()))
limit = int(input())
print(find_answer(budgets, limit))