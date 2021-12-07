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

def tablero_inicial():
    def colocar_piezas(PIEZAS_COLOR):
        if PIEZAS_COLOR == piezas_negras:
            j = 0
            for i in range (9):
                if i % 2 == 0:
                    if j < 5:
                        f.write(PIEZAS_COLOR[j])
                        j = j + 1
                    else:
                        break
                else:
                    f.write("    ")
            j = 2
            for i in range (6):
                if i % 2 == 0:
                    f.write("    ")
                else:
                    if j >= 0:
                        f.write(PIEZAS_COLOR[j])
                        j = j - 1
                    else:
                        break
            f.write('\n')
            for i in range (15):
                if i % 2 == 0:
                    f.write(PIEZAS_COLOR[5])
                else:
                    f.write("    ")
        else:
            f.write('\n')
            for i in range (15):
                if i % 2 == 0:
                    f.write(PIEZAS_COLOR[5])
                else:
                    f.write("    ")
            f.write('\n')
            j = 0
            for i in range (9):
                if i % 2 == 0:
                    if j < 5:
                        f.write(PIEZAS_COLOR[j])
                        j = j + 1
                    else:
                        break
                else:
                    f.write("    ")
            j = 2
            for i in range (6):
                if i % 2 == 0:
                    f.write("    ")
                else:
                    if j >= 0:
                        f.write(PIEZAS_COLOR[j])
                        j = j - 1
                    else:
                        break
    f = open("partida-ajedrez.txt", "w", encoding="utf-8")
    colocar_piezas(piezas_negras)
    for i in range(4):
        f.write('\n')
    colocar_piezas(piezas_blancas)
    f.close