#!/usr/bin/python3

X_SIZE = 1000
Y_SIZE = 1000

grid = [0 for i in range(X_SIZE*Y_SIZE)]

def markHorizontal(y, x1, x2):
    for i in range(y*Y_SIZE + min(x1, x2), y*Y_SIZE + max(x1, x2) + 1):
        grid[i] += 1

def markVertical(x, y1, y2):
    for i in range(min(y1, y2)*Y_SIZE+x, (max(y1,y2) + 1)*Y_SIZE+x, Y_SIZE):
        grid[i] += 1


lines = [line.strip() for line in open("input")]

for line in lines:
    coords = list(map(tuple,map(lambda s: s.split(","), map(lambda s: s.strip(), line.split("->")))))
    if coords[0][0] == coords[1][0]:
        # vertical, x co-ords same
        markVertical(int(coords[0][0]), int(coords[0][1]), int(coords[1][1]))
    elif coords[0][1] == coords[1][1]:
        # horizontal, y co-ords same
        markHorizontal(int(coords[0][1]), int(coords[0][0]), int(coords[1][0]))

print( len([p for p in grid if p > 1]))