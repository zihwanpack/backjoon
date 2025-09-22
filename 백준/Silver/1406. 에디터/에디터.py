import sys

# cursor를 기준으로 왼쪽과 오른쪽을 각각 스택으로 관리하기
left_stack = list(sys.stdin.readline().strip())
right_stack = []
N = int(sys.stdin.readline())
commands = [sys.stdin.readline().strip().split() for _ in range(N)]


for command in commands:
  cmd = command[0]
  if cmd == 'L' and len(left_stack) > 0:
    right_stack.append(left_stack.pop())
  elif cmd == 'D' and len(right_stack) > 0:
    left_stack.append(right_stack.pop())
  elif cmd == 'B' and len(left_stack) > 0:
    left_stack.pop()
  elif cmd == 'P':
    left_stack.append(command[1])

print("".join(left_stack + right_stack[::-1]))
