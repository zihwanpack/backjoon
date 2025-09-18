import sys

for line in sys.stdin:
    lst = list(map(int, line.split()))
    cnt = sum(lst)
    if cnt == 3: 
      print('A')
    elif cnt == 2: 
      print('B')
    elif cnt == 1: 
      print('C')
    elif cnt == 0: 
      print('D')
    elif cnt == 4: 
      print('E')
