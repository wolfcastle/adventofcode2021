#!/usr/bin/python3

lines = [line.strip() for line in open("input")]  

byteList = [[int(c) for c in line] for line in lines]
columns = list(zip(*byteList))
columnSums = [sum(x) for x in columns]
average = len(lines)/2
truths = [x > average for x in columnSums]
gamma = int(''.join(list(map(str, list(map(int, truths))))),2)
truths = [x < average for x in columnSums]
epsilon = int(''.join(list(map(str, list(map(int, truths))))),2)

print( "gamma: " + str(gamma) + ", epsilon: " + str(epsilon) + ", power: " + str(gamma*epsilon))
