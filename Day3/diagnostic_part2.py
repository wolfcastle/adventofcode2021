#!/usr/bin/python3

def findByte(byteList, desiredValueFunction):
  workingByteList = byteList[:]
  bytePosition = 0
  while len(workingByteList) > 1:
    columns = list(zip(*workingByteList))
    columnSum = sum(columns[bytePosition])
    average = len(workingByteList)/2
    desiredValue = int(desiredValueFunction(columnSum, average)) 
    workingByteList = [x for x in workingByteList if x[bytePosition] == desiredValue]
    bytePosition += 1
  return int(''.join(list(map(str,workingByteList[0]))),2)

lines = [line.strip() for line in open("input")]  
byteList = [[int(c) for c in line] for line in lines]

oxygenFunc = lambda sum,avg : sum >= avg
co2Func = lambda sum,avg : sum < avg

oxygen = findByte(byteList, oxygenFunc)
co2 = findByte(byteList, co2Func)
print( "oxygen: " + str(oxygen) + ", co2: " + str(co2) + ", life support: " + str(oxygen*co2))
