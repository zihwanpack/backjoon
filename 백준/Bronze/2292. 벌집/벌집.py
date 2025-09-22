import sys

N = int(sys.stdin.readline())

sum = 1
count = 1

while sum < N:
  sum += 6 * count
  count += 1

print(count)