from tablero_fichero import blancas, negras

tablero = []
for i in range(8):
    tablero.append([' '] * 8)

def colocar_tablero(COLOR, FILA, FILA_PEON):
    tablero[FILA][0] = COLOR['torre']
    tablero[FILA][1] = COLOR['caballo']
    tablero[FILA][2] = COLOR['alfil']
    tablero[FILA][3] = COLOR['reina']
    tablero[FILA][4] = COLOR['rey']
    tablero[FILA][5] = COLOR['alfil']
    tablero[FILA][6] = COLOR['caballo']
    tablero[FILA][7] = COLOR['torre']
    for i in range(8):
        tablero[FILA_PEON][i] = COLOR['peon']
            
colocar_tablero(negras, 0, 1)
colocar_tablero(blancas, 7, 6)