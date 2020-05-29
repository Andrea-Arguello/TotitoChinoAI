import random
from heuristic import heuristic
from tree import Node

def minimax(node, isMax, alpha, beta): # with alpha beta pruning
    if len(node.children)==0:
        return node.currentScore
    
    if isMax:
        maxEval = float("-inf")
        for child in node.children:
            maxEval = max(maxEval, minimax(child, False, alpha, beta))
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
        return maxEval

    else:
        minEval = float("inf")
        for child in node.children:
            minEval = max(minEval, minimax(child, True, alpha, beta))
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return minEval


def callAI(board):
    possibleMoves = []
    for i in range(len(board[0])):
        # print(board[0][i])
        if board[0][i] == 99:
            possibleMoves.append([[0,i],minimax(Node(board,[0,i],2),True,float("-inf"),float("inf"))])
        if board[1][i] == 99:
            possibleMoves.append([[1,i],minimax(Node(board,[1,i],2),True,float("-inf"),float("inf"))])
    print(possibleMoves)
    maximum = possibleMoves[0]
    for i in possibleMoves:
        if i[1]>maximum[1]:
            maximum = i
    return maximum[0]