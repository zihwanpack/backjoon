import sys
input = sys.stdin.readline

N = int(input())
switches = list(map(int, input().split()))
num_of_student = int(input())

def change_switch(idx):
    switches[idx] = 1 - switches[idx]  

for _ in range(num_of_student):
    gender, num = map(int, input().split())
    num -= 1  
    
    if gender == 1:
        for i in range(num, N, num + 1):            
          change_switch(i)
    elif gender == 2:
        change_switch(num)
        left, right = num - 1, num + 1
        while left >= 0 and right < N and switches[left] == switches[right]:
            change_switch(left)
            change_switch(right)
            left -= 1
            right += 1

for i in range(0, N, 20):
    print(*switches[i:i + 20])