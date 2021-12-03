#!/usr/bin/python3

lines = [line.strip() for line in open("input")]  
horizontal=0
depth=0
aim=0
for line in lines:
  (direction, delta) = line.split()
  delta = int(delta)
  if direction == "forward":
    horizontal += delta
    depth += (aim*delta)
  elif direction == "down":
    aim += delta
  else:
    aim -= delta
print("h=" + str(horizontal) + ", d=" + str(depth) + ", total=" + str(horizontal*depth))
