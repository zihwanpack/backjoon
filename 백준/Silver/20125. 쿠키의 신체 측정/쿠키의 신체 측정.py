import sys
input = sys.stdin.readline


N = int(input())

coockie = [list(input().strip()) for _ in range(N)]

def getHead(N, coockie):
  for i in range(N):
    for j in range(N):
      if coockie[i][j] == '*':
        return (i, j)

head = getHead(N, coockie)
heart = (head[0] + 1, head[1])

heart_x = heart[0]
heart_y = heart[1]

left_arm = coockie[heart_x][:heart_y].count('*')
right_arm = coockie[heart_x][heart_y + 1:].count('*')

waist = 0
for i in range(heart_x + 1, N):
  if coockie[i][heart_y] == '*':
    waist += 1
  else:
    end_of_waist = i
    break


left_leg = 0
for i in range(end_of_waist, N):
  if coockie[i][heart_y - 1] == '*':
    left_leg += 1

right_leg = 0
for i in range(end_of_waist, N):
  if coockie[i][heart_y + 1] == '*':
    right_leg += 1

print(heart_x + 1, heart_y + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)