import random
from heuristic import heuristic
from tree import Node

def minimax(node, isMax, alpha, beta): # with alpha beta pruning
    if len(node.children)==0:
        return node
    
    if isMax:
        maxEval = float("-inf")
        for child in node:
            maxEval = max(maxEval, minimax(child, False, alpha, beta))
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
        return maxEval

    else:
        minEval = float("inf")
        for child in node:
            minEval = max(minEval, minimax(child, True, alpha, beta))
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return minEval


def callAI(board):
    possibleMoves = []
    for i in range(len(board[0])):
        possibleMoves.append(minimax(Node(board,[0,i]),62,True,float(-"inf"),float("inf")))
        possibleMoves.append(minimax(Node(board,[1,i]),62,True,float(-"inf"),float("inf")))