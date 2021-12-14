#!/usr/bin/python3

X_SIZE = 10
Y_SIZE = 10

grid = [0 for i in range(X_SIZE*Y_SIZE)]

def markHorizontal(y, x1, x2):
    for i in range(y*Y_SIZE + min(x1, x2), y*Y_SIZE + max(x1, x2) + 1):
        grid[i] += 1

def markVertical(x, y1, y2):
    for i in range(min(y1, y2)*Y_SIZE+x, (max(y1,y2) + 1)*Y_SIZE+x, Y_SIZE):
        grid[i] += 1

def markDiagonal(x1, y1, x2, y2):
    startx = x1
    starty = y1
    endx = x2
    endy = y2

    if y2 > y1:
        startx = x2
        starty = y2
        endx = x1
        endy = y1

    offset = 1
    if x2 < x1:
        offset = -1
    for i in range(starty*Y_SIZE+startx, (endy + 1)*Y_SIZE+endx, Y_SIZE+offset):
        grid[i] += 1

lines = [line.strip() for line in open("small")]

for line in lines:
    coords = list(map(tuple,map(lambda s: s.split(","), map(lambda s: s.strip(), line.split("->")))))
    x1 = int(coords[0][0])
    y1 = int(coords[0][1])
    x2 = int(coords[1][0])
    y2 = int(coords[1][1])
    if x1 == x2:
        # vertical, x co-ords same
#         markVertical(x1, y1, y2)
        pass
    elif y1 == y2:
        # horizontal, y co-ords same
#         markHorizontal(y1, x1, x2)
        pass
    else:
        # assume diagonal
        print(coords)
        markDiagonal(x1, y1, x2, y2)

print(grid)
print( len([p for p in grid if p > 1]))