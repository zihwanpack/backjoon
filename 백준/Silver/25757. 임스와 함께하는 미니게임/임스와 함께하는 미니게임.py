import sys
input = sys.stdin.readline

N, game = map(str, input().split())
N = int(N)

players = set([input().strip() for _ in range(N)])

if (game == 'Y'):
  result = len(players)
elif (game == 'F'):
  result = len(players) // 2 
elif (game == 'O'):
  result = len(players) // 3 

print(result)