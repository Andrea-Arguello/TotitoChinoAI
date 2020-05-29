
# Based on David's algorithm for checking the board
def heuristic(board, board2):
    N = 6
    contador = 0
    acumulador = 0
    contadorPuntos = 0
    contadorPuntos2 = 0

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
            
            if board2[0][i] != 99 and board2[0][i + 1] != 99 and board2[1][contador + acumulador] != 99 and board2[1][contador + acumulador + 1] != 99:
                # En caso de que las 4 posiciones revisadas esten llenas, eso significa que se ha realizado un punto y se acumula
                contadorPuntos2 += 1

            # Variable que ayuda a determinar 2 posiciones para formar un cuadrado en la siguiente iteración
            acumulador += N
        # En caso de que se tenga que hacer un "salto de linea"
        else:
            # Variable que ayuda a determinar 2 posiciones para formar un cuadrado en la siguiente iteración
            contador += 1
            acumulador = 0
    return contadorPuntos2-contadorPuntos

""" def heuristic(initBoard, finalBoard):
    # NOTE: the heuristic changes depending on whether we are player 1 or player 2!
    difference = getSquaresDifference(initBoard, finalBoard)
    return difference """