import sys

N = int(sys.stdin.readline())

for _ in range(N):
    A, B = map(str, sys.stdin.readline().split())
    if sorted(A) == sorted(B):
        print("Possible")
    else:
        print("Impossible")
        