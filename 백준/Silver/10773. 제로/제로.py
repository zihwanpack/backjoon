import sys
input = sys.stdin.readline

N = int(input())

stack = []
numbers = [int(input()) for _ in range(N)]


for number in numbers:
  if number == 0:
    stack.pop()
  else:
    stack.append(number)

print(sum(stack))