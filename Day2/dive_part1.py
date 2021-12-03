#!/usr/bin/python3

lines = [line.strip() for line in open("input")]  
horizontal=0
depth=0
for line in lines:
  (direction, delta) = line.split()
  if direction == "forward":
    horizontal += int(delta)
  elif direction == "down":
    depth += int(delta)
  else:
    depth -= int(delta)
print("h=" + str(horizontal) + ", d=" + str(depth) + ", total=" + str(horizontal*depth))
