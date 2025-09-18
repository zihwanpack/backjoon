import sys

A, B = map(int, sys.stdin.readline().split())

low, high = min(A, B), max(A, B)

if high - low == 1 or high == low:
    print(0)
else:
    print(high - low - 1)
    print(*range(low + 1, high))