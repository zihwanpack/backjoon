import sys
input = sys.stdin.readline

N = int(input())
distance_list = list(map(int, input().split()))
price_list = list(map(int, input().split()))

current_price = price_list[0]
result = 0

for i in range(N - 1):
  if price_list[i] < current_price:
    current_price = price_list[i]
  result += current_price * distance_list[i] 

print(result)