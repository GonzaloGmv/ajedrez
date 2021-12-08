import tablero_fichero
from tablero_fichero import f
from tablero_listas import tablero
movimiento = 0
f.write("Movimiento " + str(movimiento))
tablero_fichero.tablero_fichero()
while True:
    continuar = input("¿Quieres realizar un movimiento? ")
    if continuar == "si":
        movimiento = movimiento + 1
        while True:
            inicio = input("Elija la fila y la columna de la pieza que desea mover, separadas por espacios: ")
            inicio = inicio.split()
            if len(inicio) == 2:
                filaI = inicio[0]
                columnaI = inicio[1]
                try:
                    filaI = int(filaI)
                    columnaI = int(columnaI)
                except:
                    pass
                else:
                    if filaI >= 0 and filaI < 8 and columnaI >= 0 and columnaI < 8:
                        break
        while True:
            final = input("Elija la fila y la columna a la que desea mover la pieza, separadas por espacios: ")
            final = final.split()
            if len(final) == 2:
                filaF = final[0]
                columnaF = final[1]
                try:
                    filaF = int(filaF)
                    columnaF = int(columnaF)
                except:
                    pass
                else:
                    if filaF >= 0 and filaF < 8 and columnaF >= 0 and columnaF < 8 and final != inicio:
                        tablero[filaF][columnaF] = tablero[filaI][columnaI]
                        tablero[filaI][columnaI] = " "
                        break
        f.write("Movimiento " + str(movimiento))
        tablero_fichero.tablero_fichero()
    elif continuar == "no":
        break
while True:
    mostrar_mov = input("¿Desea que se muestre en pantalla algún movimiento? ")
    if mostrar_mov == "si":
        while True:
            paso = input("¿Cual es el movimiento que desea que se le muestre? ")
            try:
                paso = int(paso)
            except:
                pass
            else:
                break
        tablero_fichero.leer_tablero(paso)
    elif mostrar_mov == "no":
        f.close
        break