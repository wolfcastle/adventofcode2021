#!/usr/bin/python3

def main():
  lanternFishGroup = read_input('input')
  for i in range(80):
    lanternFishGroup = increment_day(lanternFishGroup)
    
  return len(lanternFishGroup);

def add_baby_fish(lanternFishGroup):
  return [8 for fish in lanternFishGroup if fish == 0]

def reset_fish_index_if_require(value):
  return 6 if value == 0 else value - 1

def read_input(filename):
  file1 = open(filename, 'r')
  Lines = file1.readlines()
  return [int(fish) for fish in Lines[0].split(",")]

def increment_day(lanternFishGroup):
  babyFish = add_baby_fish(lanternFishGroup)
  for index in range(len(lanternFishGroup)):
    lanternFishGroup[index] = reset_fish_index_if_require(lanternFishGroup[index])
  lanternFishGroup.extend(babyFish)
  return lanternFishGroup

def test_read_input():
  lanterFish = read_input('small')
  assert len(lanterFish) == 5

def test_increment_day():
  lanternFishGroup = increment_day([3,4,3,1,2])
  assert lanternFishGroup == [2,3,2,0,1]
  lanternFishGroup = increment_day([2,3,2,0,1])
  assert lanternFishGroup == [1,2,1,6,0,8]

def test_add_baby_fish():
  assert add_baby_fish([1,2,3]) == []
  assert add_baby_fish([1,2,0]) == [8]
  assert add_baby_fish([1,2,0,5,0]) == [8,8]

test_read_input()
test_increment_day()
test_add_baby_fish()
print(main())

