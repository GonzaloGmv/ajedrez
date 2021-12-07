from tablero_listas import tablero
f = open("partida-ajedrez.txt", "w", encoding="utf-8")
def tablero_fichero():
    for i in range(8):
        f.write('\n')
        for j in range(8):
            f.write(str(tablero[i][j]))
            f.write("   ")
    f.write('\n')
    f.close