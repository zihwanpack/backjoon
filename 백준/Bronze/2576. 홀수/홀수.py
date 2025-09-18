import sys


oddNums = [int(line) for line in sys.stdin if int(line) % 2 == 1]

if len(oddNums) == 0:
    print(-1)
else:
    print(sum(oddNums))
    print(min(oddNums))