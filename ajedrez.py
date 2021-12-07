import tablero_fichero
from tablero_listas import tablero
tablero_fichero.tablero_inicial()
while True:
    continuar = input("¿Quieres realizar un movimiento? ")
    if continuar == "SI":
        while True:
            inicio = input("Elija la fila y la columna de la pieza que desea mover separadas por espacios: ")
            inicio = inicio.split()
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
            final = input("Elija la fila y la columna de la pieza que desea mover separadas por espacios: ")
            final = final.split()
            filaF = final[0]
            columnaF = final[1]
            try:
                filaF = int(final)
                columnaF = int(columnaF)
            except:
                pass
            else:
                if filaF >= 0 and filaF < 8 and columnaF >= 0 and columnaF < 8:
                    tablero[filaF][columnaF] = tablero[filaI]
                    tablero[filaI][columnaI] = " "
                    break
    else:
        break
