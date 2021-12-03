#!/usr/bin/python3

depths = [int(line.rstrip()) for line in open("input")]
numIncrements = 0
lastDepth = depths[0]

for depth in depths[1:]:
  newDepth = depth
  if newDepth > lastDepth:
    numIncrements += 1
  lastDepth = newDepth

print(str(numIncrements))

