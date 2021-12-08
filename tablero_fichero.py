from tablero_listas import tablero
fichero = input("Escriba el nombre del fichero en el que quiere que se cree su partida: ")
f = open(fichero, "a+", encoding="utf-8")
def tablero_fichero():
    for i in range(8):
        f.write('\n')
        for j in range(8):
            f.write(str(tablero[i][j]))
            f.write("   ")
    f.write('\n')
def leer_tablero(PASO):
    f.seek(0)
    lineas = f.readlines()
    for i in range(8):
        print(lineas[PASO * 9 + 1 + i], end='')