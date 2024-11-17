n = int(input())

for i in range(1, n + 1):
    print("*" * i +  " " * (n * 2 - i * 2) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i +  " " * (n * 2 - i * 2) + "*" * i)