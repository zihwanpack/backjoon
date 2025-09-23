import sys
input = sys.stdin.readline

N = int(input())
channels = [input().strip() for _ in range(N)]

result = ''
cursor = 0

def cursorDown(cursor, result):
    cursor += 1
    result += '1'
    return cursor, result

def channelUp(cursor, channels, result):
    channels[cursor], channels[cursor-1] = channels[cursor-1], channels[cursor]
    cursor -= 1
    result += '4'
    return cursor, channels, result

# 1. KBS1 앞으로 옮기기
kbs1_idx = channels.index("KBS1")
for _ in range(kbs1_idx):
    cursor, result = cursorDown(cursor, result)
for _ in range(kbs1_idx):
    cursor, channels, result = channelUp(cursor, channels, result)

# 2. 이제 리스트가 바뀌었으니 KBS2 위치 다시 찾기
kbs2_idx = channels.index("KBS2")
for _ in range(kbs2_idx):
    cursor, result = cursorDown(cursor, result)
for _ in range(kbs2_idx - 1):
    cursor, channels, result = channelUp(cursor, channels, result)

print(result)