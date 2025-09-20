import sys

word = sys.stdin.readline().strip()
nums = [i * 0 for i in range(26)]

for i in range(len(word)):
  nums[ord(word[i]) - 97] += 1
  
print(" ".join(map(str, nums)))

