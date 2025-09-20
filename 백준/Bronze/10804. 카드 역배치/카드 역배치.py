import sys

nums = [i for i in range(21)]


for _ in range(10):
  A, B = map(int, sys.stdin.readline().split())
  nums[A : B + 1] = reversed(nums[A : B + 1])
  
  
print(" ".join(map(str, nums[1:])))

