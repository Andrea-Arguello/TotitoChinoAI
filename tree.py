from heuristic import heuristic
from copy import deepcopy


class Node:
    def __init__(self, initBoard, movement):
        self.movement = movement
        self.initBoard = [x[:] for x in initBoard]
        self.finalBoard = getFinalBoard(self.initBoard, movement)
        self.currentScore = heuristic(initBoard, self.finalBoard)
        self.children = []
        self.giveBirth()

    def giveBirth(self):
        for i in self.possibleNextMoves():
            self.children.append(Node(self.finalBoard, i))

    def possibleNextMoves(self):
        available = []
        for i in range(len(self.finalBoard[0])):
            if self.finalBoard[0][i] == 99:
                available.append([0,i])
            if self.finalBoard[1][i] == 99:
                available.append([1,i])
        return available

def getFinalBoard(initBoard, movement):
    finalBoard = [x[:] for x in initBoard]
    finalBoard[movement[0]][movement[1]] = 0
    return finalBoard