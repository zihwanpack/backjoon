import sys

N = int(sys.stdin.readline())
calls = list(map(int, sys.stdin.readline().split()))

def yCalc(call):
  fee = 0
  return (call // 30 + 1) * 10

def mCalc(call):
  fee = 0
  return (call // 60 + 1) * 15

yFee = sum(yCalc(call) for call in calls)
mFee = sum(mCalc(call) for call in calls)

if yFee < mFee:
    print("Y", yFee)
elif yFee > mFee:
    print("M", mFee)
else:
    print("Y M", yFee)
  