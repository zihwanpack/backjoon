import sys
# strip을 해야 \n이 안들어옴
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

alphabet = [0] * 26

for s in str1:
    alphabet[ord(s) - 97] += 1

for s in str2:
    alphabet[ord(s) - 97] -= 1

answer = sum(abs(i) for i in alphabet)
print(answer)