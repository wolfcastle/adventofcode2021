#!/usr/bin/python3

def findByte(byteList, desiredValueFunction):
  oxygenByteList = byteList[:]
  bytePosition = 0
  while len(oxygenByteList) > 1:
    columns = list(zip(*oxygenByteList))
    columnSum = sum(columns[bytePosition])
    average = len(oxygenByteList)/2
    #print( "sum: " + str(columnSum) + ", average: " + str(average))
    desiredValue = int(desiredValueFunction(columnSum, average)) 
    oxygenByteList = [x for x in oxygenByteList if x[bytePosition] == desiredValue]
    #print("MCV: " + str(desiredValue) + ", bitposition: " + str(bytePosition))
    #print(oxygenByteList)
    bytePosition += 1
  return ''.join(list(map(str,oxygenByteList[0])))


lines = [line.strip() for line in open("input")]  

byteList = [[int(c) for c in line] for line in lines]

oxygenFunc = lambda sum,avg : sum >= avg
co2Func = lambda sum,avg : sum < avg

oxygen = int(findByte(byteList, oxygenFunc),2)
co2 = int(findByte(byteList, co2Func),2)
print( "oxygen: " + str(oxygen) + ", co2: " + str(co2) + ", life support: " + str(oxygen*co2))
#print( "gamma: " + str(gamma) + ", epsilon: " + str(epsilon) + ", power: " + str(gamma*epsilon))
