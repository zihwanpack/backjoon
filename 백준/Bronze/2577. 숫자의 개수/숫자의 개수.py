import sys

total = 1
for _ in range(3):
  num = int(sys.stdin.readline())
  total *= num

for i in range(10):
  print(str(total).count(str(i)))
