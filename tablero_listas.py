blancas = {
    'torre': chr(0x2656),
    'caballo': chr(0x2658),
    'alfil': chr(0x2657),
    'reina': chr(0x2655),
    'rey': chr(0x2654),
    'peon': chr(0x2659)
} 
negras = {
    'torre': chr(0x265C),
    'caballo': chr(0x265E),
    'alfil': chr(0x265D),
    'reina': chr(0x265B),
    'rey': chr(0x265A),
    'peon': chr(0x265F)
}
piezas_blancas = list(blancas.values())
piezas_negras = list(negras.values())
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