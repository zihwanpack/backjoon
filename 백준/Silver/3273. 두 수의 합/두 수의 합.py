import sys

n =  int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x =  int(sys.stdin.readline())
count = 0

set_arr = set(arr)
for num in set_arr:
  remain = x - num
  if remain in set_arr:
    count += 1

print(count // 2)