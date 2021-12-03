#!/usr/bin/python3

AVG_SIZE=3
depths = [int(line.rstrip()) for line in open("input")]
numIncrements = 0
lastDepth = sum(depths[0:AVG_SIZE])

for i in range(1,len(depths)):
  newDepth = sum(depths[i:i+AVG_SIZE])
  if newDepth > lastDepth:
    numIncrements += 1
  lastDepth = newDepth

print(str(numIncrements))

