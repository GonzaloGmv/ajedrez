# ajedrez

Mi dirección de github para este repositorio es: [ github](https://github.com/GonzaloGmv/ajedrez)

He realizado un programa que escribe los movimientos de una partida de ajedrez en un fichero de texto, en este programa,se pregunta al usuario si quiere hacer un movimiento, y una vez el usuario haya acabado, se pregunta si quiere que se imprima en la consola algún movimiento, y si es así cuál.

Para realizar esto, primero pensaba que había que utilizar listas, pero al imprimirlo quedaba muy mal por los "[]", así que lo hice directamente en un fichero. Una vez hecho esto, me di cuenta de que para realizar los movimientos iba a ser muy complicado usar solo el fichero, así que usé listas y posteriormente guardaría estas listas en el fichero, ambas cosas en funciones dentro de módulos, que implementaría en el código principal cuando fuera necesario. Finalmente, para imprimir en pantalla el movimiento que quería, recurría a una función que leía e imprimía las líneas del fichero referidas al movimiento que fuera.

Algun problema que he tenido, ha sido que al escribir en el fichero los caracteres del ajedrez, este no me los leía, y en internet, encontré que había que añadir *encoding="utf-8"* a la funcion *.open()* para que funcionara. Otro problema ha sido que a la hora de leer el archivo, me leía solamente un salto de línea, y en internet he encontrado que eso se debía a que al escribir, el cursor se queda al final, por lo que se lee desde ahi. Para solucionar esto, he utilizado la funcion *.seek()* con un 0 para que el cursor se colocara al principio.

Para realizar este ajedrez, he tenido en cuenta que el usuario conoce las reglas del ajedrez, por lo que no va a realizar ningún movimiento ilegal. Pero 

Mi **diagrama de flujo** para este proyecto es:

![diagrama_ajedrez](https://user-images.githubusercontent.com/91721237/145688877-6c2bac68-2b03-40fa-b1cb-c1e66b0895e7.jpg)

El código de este proyecto es el siguiente:

#### ajedrez.py
```
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
```

#### tablero_listas.py
```
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
```

#### tablero_fichero.py
```
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
```
