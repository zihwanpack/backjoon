import sys

nums = sorted([int(line) for line in sys.stdin])

print(sum(nums) // len(nums))
print(nums[2])