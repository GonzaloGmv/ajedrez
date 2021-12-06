blancas = {
    'rey': chr(0x2654),
    'reina': chr(0x2655),
    'torre': chr(0x2656),
    'alfil': chr(0x2657),
    'caballo': chr(0x2658),
    'peon': chr(0x2659)
} 
negras = {
    'rey': chr(0x265A),
    'reina': chr(0x265B),
    'torre': chr(0x265C),
    'alfil': chr(0x265D),
    'caballo': chr(0x265E),
    'peon': chr(0x265F)
}

tablero = []
for i in range(8):
    tablero.append([' '] * 15)

def colocar_tablero(COLOR, FILA, FILA_PEON):
    tablero[FILA][0] = COLOR['torre']
    tablero[FILA][2] = COLOR['caballo']
    tablero[FILA][4] = COLOR['alfil']
    tablero[FILA][6] = COLOR['reina']
    tablero[FILA][8] = COLOR['rey']
    tablero[FILA][10] = COLOR['alfil']
    tablero[FILA][12] = COLOR['caballo']
    tablero[FILA][14] = COLOR['torre']
    for i in range(15):
        if i % 2 == 0:
            tablero[FILA_PEON][i] = COLOR['peon']

colocar_tablero(negras, 0, 1)
colocar_tablero(blancas, 7, 6)
for i in range(8):
    print(tablero[i])

f = open("partida-ajedrez.txt", "w", encoding="utf-8")
for i in range(8):
    f.write(str(tablero[i]) + '\n')
f.close