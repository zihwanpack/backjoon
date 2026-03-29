

def solution(brown, yellow):
    allTiles = brown + yellow
    
    for x in range(3, int(allTiles ** 0.5) + 1):
        if allTiles % x == 0:
            y = allTiles // x
            if (x - 2) * (y - 2) == yellow:
                return sorted([x, y], reverse=True)