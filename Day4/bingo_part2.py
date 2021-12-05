#!/usr/bin/python3

import textwrap

BOARD_SIZE = 5

class BingoCard:

    def __init__(self, board, id):
        self._board = board
        self._id = id
        self._calledNumbers = []

    def callNumber(self,number):
        self._calledNumbers.append(number)

    def isBingo(self):
        # check rows
        for row in range(0,BOARD_SIZE):
            numMatch = 0
            for col in range(0,BOARD_SIZE):
                if self._board[row*BOARD_SIZE + col] in self._calledNumbers:
                    numMatch += 1
            if numMatch == BOARD_SIZE:
                return True

        for col in range(0,BOARD_SIZE):
            numMatch = 0
            for row in range(0,BOARD_SIZE):
                if self._board[row*BOARD_SIZE + col] in self._calledNumbers:
                    numMatch += 1
            if numMatch == BOARD_SIZE:
                return True
        return False

    def getWinningScore(self):
        return sum(set(self._board).difference(self._calledNumbers))

    def getId(self):
        return self._id

    def prettyPrint(self):
        longString = ", ".join(list(map(str,self._board)))
        print(textwrap.fill(longString, 20))
        print(self._calledNumbers)


lines = [line.strip() for line in open("input")]
numbersToCall = [int(num) for num in lines[0].split(",")]
boards = []
numbers = []
for i in range(1,len(lines)):
    if not lines[i]:
        continue
    numbers.extend( [int(num.strip()) for num in lines[i].split() ])

    if len(numbers) == BOARD_SIZE * BOARD_SIZE:
        boards.append(BingoCard(numbers, int(i/5)))
        numbers = []

for num in numbersToCall:
    for board in boards:
        board.callNumber(num)

    boardsToRemove = []
    for board in boards:
        if board.isBingo():
            boardsToRemove.append(board)
            lastBoardToWin = board
            lastNumberCalled = num
    boards = [b for b in boards if b not in boardsToRemove]

print( "Losing card is on " + str(lastNumberCalled) + " Card is: " + str(lastBoardToWin.getId()) + ", "+ str(lastBoardToWin.getWinningScore()) + " score: " + str(lastNumberCalled*lastBoardToWin.getWinningScore()))