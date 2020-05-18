import random

def minmax(board):
    move = random.randint(0,1)
    position = random.randint(0,29)
    while board[move][position] != 99:
        move = random.randint(0,1)
        position = random.randint(0,29)
    mymovement = [move, position]
    print('next move:', mymovement)
    return mymovement