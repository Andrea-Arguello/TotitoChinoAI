import random
import heuristic as h
from tree import Node

def boardAfterMove(initBoard, movement):
    finalBoard = [x[:] for x in initBoard]
    finalBoard[movement[0]][movement[1]] = 0
    return finalBoard

# def minimax(board, move, depth, isMax, alpha, beta):
#     if depth == 0 or h.squaresClosed(board, boardAfterMove(board, move), isMax)!=0:
#         return h.squaresClosed(board, boardAfterMove(board, move), isMax)
    
#     if isMax:
#         maxEval = float("-inf")
#         for nextMove in getPossibleMoves(boardAfterMove(board, move)):
#             maxEval = max(maxEval, -minimax(boardAfterMove(board, move), nextMove, depth-1, False, alpha, beta))
#             alpha = max(alpha, maxEval)
#             if beta <= alpha:
#                 break
#         return maxEval

#     else:
#         minEval = float("inf")
#         for nextMove in getPossibleMoves(boardAfterMove(board, move)):
#             minEval = min(minEval, -minimax(boardAfterMove(board, move), nextMove, depth-1, True, alpha, beta))
#             beta = min(beta, minEval)
#             if beta <= alpha:
#                 break
#         return minEval
    

# This is not doing what i want always returns inf or -inf
def minimaxog(node, isMax, alpha, beta): # with alpha beta pruning
    if node.depth==0: #we're at the bottom
        return node.currentScore
    
    if isMax:
        maxEval = float("-inf")
        for child in node.children:
            maxEval = max(maxEval, minimaxog(child, False, alpha, beta))
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                print("Got em max", alpha, beta)
                break
        return maxEval

    else:
        minEval = float("inf")
        for child in node.children:
            minEval = min(minEval, minimaxog(child, True, alpha, beta))
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return minEval


def callAI(board, myTurn):
    possibleMoves = []
    depth = 2
    for i in getPossibleMoves(board):
        while depth>len(getPossibleMoves(board)):
            depth -= 1
        # possibleMoves.append([i, minimax(board, i, 1, True, float("-inf"),float("inf"))])
        possibleMoves.append([i,minimaxog(Node(board,i, h.currentScore(board), depth, True, myTurn, myTurn),True,float("-inf"),float("inf"))])
    # for i in range(len(board[0])):
    #     if board[0][i] == 99:
    #         # possibleMoves.append([[0,i],minimax(Node(board,[0,i],2, myTurn),True,float("-inf"),float("inf"))]) # We send 2 because we want to look at our next turn
    #     if board[1][i] == 99:
    #         possibleMoves.append([[1,i],minimax(Node(board,[1,i],2, myTurn),True,float("-inf"),float("inf"))])
    # print(possibleMoves)
    maximum = random.choice(possibleMoves)
    for i in possibleMoves:
        # if myTurn == 2:
        #     if i[1]>maximum[1]:
        #         maximum = i
        # else:
        #     if i[1]<maximum[1]:
        #         maximum = i
        if i[1]>maximum[1]:
            maximum = i
    print(possibleMoves)
    print(maximum)
    return maximum[0]


def getPossibleMoves(board):
    possibleMoves = []
    for i in range(len(board[0])):
        if board[0][i] == 99:
            possibleMoves.append([0,i])
        if board[1][i] == 99:
            possibleMoves.append([1,i])
    return possibleMoves