import sys, math

H, W, N, M = map(int, sys.stdin.readline().split())

print(math.ceil(H / (N + 1)) * math.ceil(W / (M + 1)))


