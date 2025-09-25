import sys
input = sys.stdin.readline

N = int(input())
flag = 0


while N != 0:
  if N < 3:
    N -= 1
    flag += 1
  else:
    N -= 3
    flag += 1


if flag % 2:
  print("SK")
else:
  print("CY")
