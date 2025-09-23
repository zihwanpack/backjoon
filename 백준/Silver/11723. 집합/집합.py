import sys
input = sys.stdin.readline

N = int(input())
s = set()

for _ in range(N):
    calc = input().split()
    cmd = calc[0]

    if cmd == 'add':
        s.add(int(calc[1]))
    elif cmd == 'remove':
        s.discard(int(calc[1]))
    elif cmd == 'check':
        print(1 if int(calc[1]) in s else 0)
    elif cmd == 'toggle':
        x = int(calc[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif cmd == 'all':
        s = set(range(1, 21))
    elif cmd == 'empty':
        s.clear()