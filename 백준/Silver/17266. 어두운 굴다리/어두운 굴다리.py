import sys
import math 

input = sys.stdin.readline
N = int(input())
M = int(input())
x = list(map(int, input().split()))

max_height = max(x[0], N - x[-1])


for i in range(1, M):
  distance = x[i] - x[i-1]
  required_height = math.ceil(distance  / 2)
  max_height = max(max_height, required_height)

print(max_height)