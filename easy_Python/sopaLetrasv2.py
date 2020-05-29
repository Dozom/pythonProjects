import random
tablero = []
palabras = ["qwertyuiopqwertyuio","be","ce","de","ee","efe","ge","hache","i","jota"]
dicInici = {}
llistaTrobades = []
track = []
# posicionamos el tablero con formato fila columna
def pTablero():
    global tablero
    for i in range(20):
        row = []
        for j in range(20):
            row.append("%s%s" % (i,j))
        tablero.append(row)
# recorremos la lista
def recorrerPalabras():
    global palabras
    for p in palabras:
        opciones = ["a","b","c","d","e","f","g","h"]
        opcion = random.choice(opciones)
        randomMenu(opcion,p)
# opciones random para facilitar el debug y comprobar funciones
def randomMenu(opcion,p):
    if (opcion == "a"):
        checkAbajo(p)
    elif (opcion == "b"):
        checkArriba(p)
    elif (opcion == "c"):
        checkdDAbajo(p)
    elif (opcion == "d"):
        checkdDArriba(p)
    elif (opcion == "e"):
        checkDerecha(p)
    elif (opcion == "f"):
        checkdIAbajo(p)
    elif (opcion == "g"):
        checkdIArriba(p)
    elif (opcion == "h"):
        checkIzquierda(p)
def checkDerecha(p):
    global tablero
    contador = 0
    filarandom = random.randint(0,19)
    columnarandom = random.randint(0,19)-len(p)
    while columnarandom < 0:
        columnarandom = random.randint(0,19)-len(p)
    inicio = tablero[filarandom][columnarandom]
    dicInici.update({p:inicio})
    for i in range(len(p)):
        celda = tablero[filarandom][columnarandom+i]
        if celda.isdigit():
            contador += 1
    if contador == len(p):
        ponerDerecha(filarandom,columnarandom,p)
    else:
        checkDerecha(p)
def ponerDerecha(fila,columna,palabra):
    global tablero,track
    i = 0
    path = []
    for c in palabra:
        tablero[fila][columna+i] = c
        path.append("%s,%s" % (fila,columna+i))
        i += 1
    track.append(path)
def checkIzquierda(p):
    global tablero
    contador = 0
    filarandom = random.randint(0,19)
    columnarandom = random.randint(len(p),19)
    inicio = tablero[filarandom][columnarandom]
    dicInici.update({p:inicio})
    for i in range(len(p)):
        celda = tablero[filarandom][columnarandom-i]
        if celda.isdigit():
            contador += 1
    if contador == len(p):
        ponerIzquierda(filarandom,columnarandom,p)
    else:
        checkIzquierda(p)
def ponerIzquierda(fila,columna,palabra):
    global tablero,track
    i = 0
    path = []
    for c in palabra:
        tablero[fila][columna-i] = c
        path.append("%s,%s" % (fila,columna-i))
        i += 1
    track.append(path)
# De arriba a abajo
def checkArriba(p):
    global tablero
    contador = 0
    filarandom = random.randint(0,19)-len(p)
    columnarandom = random.randint(0,19)
    while filarandom < 0:
        filarandom = random.randint(0,19)-len(p)
    inicio = tablero[filarandom][columnarandom]
    dicInici.update({p:inicio})
    for i in range(len(p)):
        celda = tablero[filarandom+i][columnarandom]
        if celda.isdigit():
            contador += 1
    if contador == len(p):
        ponerArriba(filarandom,columnarandom,p)
    else:
        checkArriba(p)
def ponerArriba(fila,columna,palabra):
    global tablero,track
    i = 0
    path = []
    for c in palabra:
        tablero[fila+i][columna] = c
        path.append("%s,%s" % (fila+i,columna))
        i += 1
    track.append(path)
# De abajo a arriba
def checkAbajo(p):
    global tablero
    contador = 0
    filarandom = random.randint(len(p),19)
    columnarandom = random.randint(0,19)
    while filarandom < 0:
        filarandom = random.randint(len(p),19)
    inicio = tablero[filarandom][columnarandom]
    dicInici.update({p:inicio})
    for i in range(len(p)):
        celda = tablero[filarandom-i][columnarandom]
        if celda.isdigit():
            contador += 1
    if contador == len(p):
        ponerAbajo(filarandom,columnarandom,p)
    else:
        checkAbajo(p)
def ponerAbajo(fila,columna,palabra):
    global tablero,track
    i = 0
    path = []
    for c in palabra:
        tablero[fila-i][columna] = c
        path.append("%s,%s" % (fila-i,columna))
        i += 1
    track.append(path)
# diagonal derecha abajo
def checkdDAbajo(p):
    global tablero
    contador = 0
    filarandom = random.randint(0,19)-len(p)
    columnarandom = random.randint(0,19)-len(p)
    while filarandom < 0:
        filarandom = random.randint(0,19)-len(p)
    while columnarandom < 0:
        columnarandom = random.randint(0,19)-len(p)
    inicio = tablero[filarandom][columnarandom]
    dicInici.update({p:inicio})
    for i in range(len(p)):
        celda = tablero[filarandom+i][columnarandom+i]
        if celda.isdigit():
            contador += 1
    if contador == len(p):
        ponerdDabajo(filarandom,columnarandom,p)
    else:
        checkdDAbajo(p)
def ponerdDabajo(fila,columna,palabra):
    global tablero,track
    i = 0
    path = []
    for c in palabra:
        tablero[fila+i][columna+i] = c
        path.append("%s,%s" % (fila+i,columna+i))
        i += 1
    track.append(path)
#diagonal Derecha Arriba
def checkdDArriba(p):
    global tablero
    contador = 0
    filarandom = random.randint(len(p),19)
    columnarandom = random.randint(0,19)-len(p)
    while columnarandom < 0:
        columnarandom = random.randint(0,19)-len(p)
    inicio = tablero[filarandom][columnarandom]
    dicInici.update({p:inicio})
    for i in range(len(p)):
        celda = tablero[filarandom-i][columnarandom+i]
        if celda.isdigit():
            contador += 1
    if contador == len(p):
        ponerdDArriba(filarandom,columnarandom,p)
    else:
        checkdDArriba(p)
def ponerdDArriba(fila,columna,palabra):
    global tablero,track
    i = 0
    path = []
    for c in palabra:
        tablero[fila-i][columna+i] = c
        path.append("%s,%s" % (fila-i,columna+i))
        i += 1
    track.append(path)
#diagonal Izquierda Abajo
def checkdIAbajo(p):
    global tablero
    contador = 0
    filarandom = random.randint(0,19)-len(p)
    columnarandom = random.randint(len(p),19)
    while filarandom < 0:
        filarandom = random.randint(0,19)-len(p)
    inicio = tablero[filarandom][columnarandom]
    dicInici.update({p:inicio})
    for i in range(len(p)):
        celda = tablero[filarandom+i][columnarandom-i]
        if celda.isdigit():
            contador += 1
    if contador == len(p):
        ponerdIAbajo(filarandom,columnarandom,p)
    else:
        checkdIAbajo(p)
def ponerdIAbajo(fila,columna,palabra):
    global tablero,track
    i = 0
    path = []
    for c in palabra:
        tablero[fila+i][columna-i] = c
        path.append("%s,%s" % (fila+i,columna-i))
        i += 1
    track.append(path)
#diagonal Izquierda Arriba
def checkdIArriba(p):
    global tablero
    contador = 0
    filarandom = random.randint(len(p),19)
    columnarandom = random.randint(len(p),19)
    while filarandom < 0:
        filarandom = random.randint(len(p),19)
    inicio = tablero[filarandom][columnarandom]
    dicInici.update({p:inicio})
    for i in range(len(p)):
        celda = tablero[filarandom-i][columnarandom-i]
        if celda.isdigit():
            contador += 1
    if contador == len(p):
        ponerdIArriba(filarandom,columnarandom,p)
    else:
        checkdIArriba(p)
def ponerdIArriba(fila,columna,palabra):
    global tablero,track
    i = 0
    path = []
    for c in palabra:
        tablero[fila-i][columna-i] = c
        path.append("%s,%s" % (fila-i,columna))
        i += 1
    track.append(path)
def imprimirTablero():
    global tablero
    for row in tablero:
        printrow = ""
        for i in row:
            if i.isdigit():
                printrow += chr(random.randint(65,90))
            else:
                printrow += i
        print("%s\n" % (printrow))
def cambiarTablero(fila,columna):
    global track
    for paraula in track:
        if "%s,%s" % (fila,columna) in paraula:
            for fc in paraula:
                fila = fc[:fc.find(',')]
                columna = fc[fc.find(',')+1:]
                tablero[int(fila)][int(columna)] = '*'
def introduirParaula():
    global dicInici
    paraula = str(input("Introdueix la paraula: "))
    fila = int(input("Introdueix la fila: "))
    columna = int(input("Introdueix la columna: "))
    paraules = len(dicInici)
    while paraules > 0:
        if paraula in dicInici.keys() and dicInici[paraula] == "%s%s" % (fila,columna):
            print("Has trobat la paraula")
            dicInici.pop(paraula)
            cambiarTablero(fila,columna)
            imprimirTablero()
            paraules = len(dicInici)
            if paraules == 0:
                break
            else:
                print("Queden %s paraules" % (paraules))
                introduirParaula()
        else:
            paraules = len(dicInici)
            print("Has fallat")
            introduirParaula()
    print("Has trobat totes les paraules, enhorabona has guanyat")
pTablero()
recorrerPalabras()
imprimirTablero()
introduirParaula()
