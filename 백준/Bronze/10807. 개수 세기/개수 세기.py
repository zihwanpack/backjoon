import sys

N =  int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
v =  int(sys.stdin.readline())
count = 0


for num in arr:
  if num == v:
    count += 1
print(count)

