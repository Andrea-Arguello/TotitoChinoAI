from copy import copy

def squaresClosed(board1,board2,isMax):
    squareDifference = closedSquares(board2) - closedSquares(board1)
    if isMax:
        return squareDifference
    return -squareDifference

def heuristic(prevScore, board1, board2, isMax, turn, myTurn):
    # return squaresClosed(board1,board2,isMax)
    squareDifference = closedSquares(board2) - closedSquares(board1)
    # if isMax:
    #     return squareDifference
    # return -squareDifference
    realScore = 0
    if turn%2 == 0:
        realScore = copy(prevScore) - squareDifference
        if isMax and myTurn: # We want my answer to be positive
            return -realScore
        return realScore
    realScore = prevScore + squareDifference
    if isMax and myTurn:
        return realScore
    return -realScore


# Based on David's algorithm for checking the board

def currentScore(board):
    player1 = 0
    player2 = 0
    FILLEDP11 = 1
    FILLEDP12 = 2
    FILLEDP21 = -1
    FILLEDP22 = -2


    for i in range(len(board[0])):
        if board[0][i] == FILLEDP12:
            player1 = player1 + 2
        elif board[0][i] == FILLEDP11:
            player1 = player1 + 1
        elif board[0][i] == FILLEDP22:
            player2 = player2 + 2
        elif board[0][i] == FILLEDP21:
            player2 = player2 + 1

    for j in range(len(board[1])):
        if board[1][j] == FILLEDP12:
            player1 = player1 + 2
        elif board[1][j] == FILLEDP11:
            player1 = player1 + 1
        elif board[1][j] == FILLEDP22:
            player2 = player2 + 2
        elif board[1][j] == FILLEDP21:
            player2 = player2 + 1
    return player1+player2


def closedSquares(board):
    N = 6
    contador = 0
    acumulador = 0
    contadorPuntos = 0
    
    for i in range(len(board[0])):
        # La logica de esto si alguien tiene alguna duda se los puedo mandar en una demostración que hice a papel de la simetría de los tableros cuadrados en totito chino
        # Pero en general se revisa si la posicion siguiente de la que se tiene actualmente en la iteracion del arreglo se sale de la fila "física" que se está revisando
        # para hacer un "salto de fila" ya que los cuadrados nunca se pueden formar con lineas horizontales o verticales que esten en lados opuestos del tablero
        if ((i + 1) % N) != 0:
            # En caso no estemos haciendo un "salto de linea" se revisa si hay un cuadrado formado alrededor de la posicion sobre la que se esta iterando
            # Si alguien tiene duda de como funciona saber cuales son los otras 3 posiciones que formarian el cuadrado, avisenme para que les pase la demostración
            if board[0][i] != 99 and board[0][i + 1] != 99 and board[1][contador + acumulador] != 99 and board[1][contador + acumulador + 1] != 99:
                # En caso de que las 4 posiciones revisadas esten llenas, eso significa que se ha realizado un punto y se acumula
                contadorPuntos += 1
            
            # Variable que ayuda a determinar 2 posiciones para formar un cuadrado en la siguiente iteración
            acumulador += N
        # En caso de que se tenga que hacer un "salto de linea"
        else:
            # Variable que ayuda a determinar 2 posiciones para formar un cuadrado en la siguiente iteración
            contador += 1
            acumulador = 0
    return contadorPuntos