import sys

N = int(sys.stdin.readline())

for _ in range(N):
    commands = sys.stdin.readline().strip()
    left_stack = []
    right_stack = []

    for cmd in commands:
        if cmd == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif cmd == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        elif cmd == "-":
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(cmd)

    print("".join(left_stack + right_stack[::-1]))