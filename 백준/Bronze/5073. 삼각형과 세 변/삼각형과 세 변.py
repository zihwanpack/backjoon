import sys

def checkTriangleType(A, B, C):
    if A == 0 and B == 0 and C == 0:
        return
    elif A + B <= C or A + C <= B or B + C <= A:
        print("Invalid")
    elif A == B == C:
        print("Equilateral")
    elif A == B or B == C or A == C:
        print("Isosceles")
    else:
        print("Scalene")

for line in sys.stdin:
    A, B, C = map(int, line.split())
    checkTriangleType(A, B, C)