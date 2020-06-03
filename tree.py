import heuristic as h
from copy import deepcopy


class Node:
    def __init__(self, initBoard, movement, previousScore, depth, isMax, turn, myTurn):
        self.myTurn = myTurn #this is constant
        self.isMax = isMax
        self.turn = turn
        self.movement = movement
        self.initBoard = [x[:] for x in initBoard]
        self.finalBoard = getFinalBoard(self.initBoard, movement)
        self.previousScore = previousScore
        self.currentScore = h.heuristic(self.previousScore, self.initBoard, self.finalBoard, isMax, turn, myTurn)
        self.children = []
        self.depth = depth
        if self.depth > 0:
            self.giveBirth()
        # if self.currentScore != 0: # If we threw once, we throw again
        #     childrenThatScore = []
        #     for i in range(len(self.children)):
        #         if self.children[i].currentScore!=0:
        #             self.children[i].currentScore = -self.children[i].currentScore + self.currentScore
            #         childrenThatScore.append(self.children[i].currentScore)
            # if len(childrenThatScore)>0:
            #     maximumScore = -childrenThatScore[0] # we gotta change the sign because our children have the opposite score
            #     for j in childrenThatScore:
            #         if -j > maximumScore:
            #             maximumScore = -j
            #     print("our maximum score is:", maximumScore)
            #     self.currentScore += maximumScore
           

    def giveBirth(self):
        for i in self.possibleNextMoves():
            # if self.currentScore != self.initScore: #means we scored a point
            #     for j in Node(self.finalBoard, i, self.depth-1, self.turn).children:
            #         self.children.append(j)
            # else:
                self.children.append(Node(self.finalBoard, i, self.currentScore, self.depth-1, not self.isMax, self.turn%2+1, self.myTurn))

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