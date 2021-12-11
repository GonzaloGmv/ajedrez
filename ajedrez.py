import tablero_fichero
from tablero_fichero import f
from tablero_listas import tablero, piezas_blancas, piezas_negras
movimiento = 0
f.write("Movimiento " + str(movimiento))
tablero_fichero.tablero_fichero()
while True:
    continuar = input("¿Quieres realizar un movimiento? ")
    if continuar == "si":
        movimiento = movimiento + 1
        while True:
            if movimiento % 2 == 1:
                print("Juegan blancas:")
            else:
                print("Juegan negras")
            inicio = input("Elija la fila y la columna de la pieza que desea mover, separadas por espacios: ")
            inicio = inicio.split()
            if len(inicio) == 2:
                filaI = inicio[0]
                columnaI = inicio[1]
                try:
                    filaI = int(filaI)
                    columnaI = int(columnaI)
                except:
                    print("No son válidas")
                    pass
                else:
                    if filaI >= 0 and filaI < 8 and columnaI >= 0 and columnaI < 8:
                        if movimiento % 2 == 1 and piezas_blancas.__contains__(tablero[filaI][columnaI]):
                            break
                        elif movimiento % 2 == 0 and piezas_negras.__contains__(tablero[filaI][columnaI]):
                            break
                        else:
                            print("No son válidas")
                    else:
                        print("No son válidas")
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
                    print("No son válidas")
                    pass
                else:
                    if filaF >= 0 and filaF < 8 and columnaF >= 0 and columnaF < 8 and final != inicio:
                        tablero[filaF][columnaF] = tablero[filaI][columnaI]
                        tablero[filaI][columnaI] = " "
                        break
                    else:
                        print("No son válidas")
        f.write("Movimiento " + str(movimiento))
        tablero_fichero.tablero_fichero()
    elif continuar == "no":
        break
    else:
        print("Escriba si o no")
while True:
    mostrar_mov = input("¿Desea que se muestre en pantalla algún movimiento? ")
    if mostrar_mov == "si":
        while True:
            paso = input("¿Cual es el movimiento que desea que se le muestre? ")
            try:
                paso = int(paso)
            except:
                print("Escriba un numero para referirse al movimiento que quiere que se le muestre")
                pass
            else:
                if paso <= movimiento and paso >= 0:
                    break
                else:
                    print("Ese movimiento no existe")
        tablero_fichero.leer_tablero(paso)
    elif mostrar_mov == "no":
        f.close
        break
    else:
        print("Escriba si o no")