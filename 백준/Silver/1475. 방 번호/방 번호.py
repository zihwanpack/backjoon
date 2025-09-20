import sys

digits = [int(ch) for ch in sys.stdin.readline().strip()]
count = [0] * 10

for digit in digits:
  count[digit] += 1

count[6] = (count[6] + count[9] + 1) // 2
count[9] = count[6]

print(max(count))